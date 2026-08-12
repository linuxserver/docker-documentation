# The Streaming Protocol

The wire protocol between the Selkies server and the web client, for anyone implementing a client, embedding the engine, or debugging with a network inspector. Everything rides **one WebSocket** (proxied at `<base>/websocket`), carrying a mix of binary frames and terse text messages. There is no negotiation dance: connect, receive settings, start receiving media.

## Connection and roles

The client connects to `wss://host/<subfolder>websocket`. Role assignment happens one of two ways:

- **Fragment mode** (default): the URL fragment the page was opened with decides the role, `#shared` (view only), `#collab` (full control), `#player2` through `#player4` (gamepad slot only), `#display2-right` and friends (second monitor surface). No fragment means primary.
- **Token mode** (when the server was started with `SELKIES_MASTER_TOKEN`): the client must present `?token=<token>` in the WebSocket URL. Tokens and their roles are registered by the orchestrator via `POST /tokens` on the internal control port with the master token as a bearer credential. Close codes: `4001` invalid token, `4002` revoked, `4029` reconnecting too fast.

On success the server sends `MODE websockets`, an auth confirmation with the assigned role, and a `server_settings` JSON message containing every tunable setting with its value, allowed range or enum, and locked flag, this single message is what renders the sidebar UI, which is why locking a setting server side removes the control everywhere.

## Binary messages, server to client

The first byte of every binary frame is a type tag:

| Tag | Payload | Header layout (big endian) |
| --- | --- | --- |
| `0x00` | Full frame H.264 | `[1]` keyframe flag, `[2:4]` uint16 frame id, payload follows |
| `0x01` | Opus audio packet | 2 byte header, then the Opus packet |
| `0x03` | JPEG stripe | `[2:4]` frame id, `[4:6]` stripe Y offset, then the JPEG |
| `0x04` | H.264 stripe | `[1]` frame type (1 IDR, 2 I, 0 other), `[2:4]` frame id, `[4:6]` stripe Y offset, `[6:8]` width, `[8:10]` height, then Annex B NALs |

These headers are produced by pixelflux itself (see the [wire format details](../components/pixelflux.md#api-sketch)); the Python server broadcasts them untouched. A full frame is just a stripe at Y offset 0 with full height. The client feeds H.264 to a WebCodecs `VideoDecoder` per stream, decodes JPEG stripes with `createImageBitmap`, and composites stripes onto the canvas at their Y offsets. The frame type byte reflects what the encoder actually emitted, clients use it to recover decoder state after drops.

## Binary messages, client to server

| Tag | Meaning |
| --- | --- |
| `0x01` | File upload chunk (between `FILE_UPLOAD_START` and `FILE_UPLOAD_END` text messages) |
| `0x02` | Microphone PCM, s16le mono 24kHz |

## Text messages, client to server

Compact comma separated commands. The important families:

| Command                              | Parameters                | Description                                                                 |
| ------------------------------------ | ------------------------- | --------------------------------------------------------------------------- |
| `kd,<keysym>`                        | `keysym`                  | Key down event                                                              |
| `ku,<keysym>`                        | `keysym`                  | Key up event                                                                |
| `kr`                                 | —                         | Reset keyboard modifiers                                                    |
| `m,<x>,<y>,<mask>,<mag>`             | `x`, `y`, `mask`, `mag`   | Absolute pointer event with button mask and scroll magnitude                |
| `m2,<dx>,<dy>,<mask>,<mag>`          | `dx`, `dy`, `mask`, `mag` | Relative pointer event (trackpad and pointer lock modes)                    |
| `r,<WxH>,<displayId>`                | `WxH`, `displayId`        | Resize request                                                              |
| `s,<dpi>`                            | `dpi`                     | Set display DPI                                                             |
| `js,c\|d\|b\|a,...`                  | Event-specific            | Gamepad connect (`c`), disconnect (`d`), button (`b`), or axis (`a`) events |
| `cw,<b64>`                           | `b64`                     | Clipboard write (text)                                                      |
| `cb,<mime>,<b64>`                    | `mime`, `b64`             | Binary clipboard write                                                      |
| `cws` / `cbs`                        | —                         | Chunked clipboard transfer start (text / binary)                            |
| `cwd` / `cbd`                        | Chunk data                | Chunked clipboard transfer data (text / binary)                             |
| `cwe` / `cbe`                        | —                         | Chunked clipboard transfer end (text / binary)                              |
| `co,end,<text>`                      | `text`                    | Commit composed text (IME)                                                  |
| `SETTINGS,<json>`                    | `json`                    | Change stream settings (validated and clamped server-side)                  |
| `CLIENT_FRAME_ACK <id>`              | `id`                      | Backpressure acknowledgement                                                |
| `START_VIDEO`                        | —                         | Start video stream                                                          |
| `STOP_VIDEO`                         | —                         | Stop video stream                                                           |
| `START_AUDIO`                        | —                         | Start audio stream                                                          |
| `STOP_AUDIO`                         | —                         | Stop audio stream                                                           |
| `FILE_UPLOAD_START:<relpath>:<size>` | `relpath`, `size`         | Begin file upload                                                           |
| `FILE_UPLOAD_END:<path>`             | `path`                    | Complete file upload                                                        |
| `cmd,<shell>`                        | `shell`                   | Run a command in the session (gated by `SELKIES_COMMAND_ENABLED`)           |
| `_f,<fps>`                           | `fps`                     | Client FPS telemetry                                                        |
| `_l,<ms>`                            | `ms`                      | Client latency telemetry                                                    |

Every input bearing message is filtered by role: viewers get settings and video control only, players get their `js` slot, `mk_control` grants of mouse and keyboard can be toggled live in token mode.

## Text and JSON messages, server to client

- `cursor,{...}`: PNG cursor images with hotspots, delivered out of band so the canvas cursor is pixel perfect without burning it into the video.
- `clipboard,<b64>` and the chunked variants: server clipboard changes.
- `system_stats`, `gpu_stats`, `network_stats` JSON blobs every few seconds for the Stats UI.
- `stream_resolution` and `display_config_update` for resize and multi monitor layout changes.
- `VIDEO_STARTED`, `AUDIO_STOPPED`, `PIPELINE_RESETTING <display>` lifecycle notices, and `system,{"action":"reload"}` when the client should reconnect fresh.

## Backpressure

The server stamps every video frame with a wrapping uint16 id; the client periodically acknowledges the last id it presented. The server computes each client's desync, subtracts an RTT allowance (smoothed over recent samples), and if a client falls more than the allowed window behind, frames are withheld for that client *before* encode where possible, keeping H.264 reference chains valid. A client stalled beyond a timeout is disconnected. The intended behavior: one person on hotel wifi does not blur the session for four people on a LAN.

## Settings flow

Client sends `SETTINGS,{"framerate":60,"h264_crf":20,...}`; the server validates each key against its schema (range clamp, enum membership, locked flag) and applies what survives, live where pixelflux supports it (quality, framerate, paint over) or with a pipeline restart where it does not (encoder, color mode). The authoritative state then flows back in `server_settings` so all connected clients converge.

## Implementing a client: a minimal path

1. Open the WebSocket with `binaryType = 'arraybuffer'`, send `START_VIDEO` and `START_AUDIO` after receiving `server_settings`.
2. Demux on byte zero. Feed `0x00` and `0x04` frames (strip the header, respect the keyframe flag) into a WebCodecs H.264 decoder configured from the stripe dimensions; paint `0x03` JPEGs at their offsets; queue `0x01` Opus into an audio decoder.
3. Send `CLIENT_FRAME_ACK` with the latest presented frame id a few times per second.
4. Map your input events to the `kd`, `ku`, `m` or `m2` grammar.

That is a functioning viewer; everything else (clipboard, files, gamepads, stats) is additive. Start from the example client in the [pixelflux repository](https://github.com/linuxserver/pixelflux): `example/screen_to_browser.py` plus `example/index.html` are a complete working server and client pair, with the frame parsing in about a page of code.
