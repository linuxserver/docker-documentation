# Selkies

**Repository:** [selkies-project/selkies](https://github.com/selkies-project/selkies) · **License:** MPL-2.0 · **Website:** [selkies.io](https://selkies.io/) · **Upstream docs:** [docs.selkies.io](https://docs.selkies.io/)

Selkies is the heart of the platform: a ground up, web native remote desktop protocol and the Python server plus web client that implement it. It began in the Selkies project founded by Dan Isla (ex Google, ex NASA) with Seungmin Kim, targeting cloud gaming class remote desktops for Linux, and it is developed today in partnership between the Selkies organization and LinuxServer.io.

## What the server does

`selkies` is a Python asyncio application (console script `selkies`, installed in the baseimages at `/lsiopy/bin/selkies`) that owns the session:

- **Video**: drives [pixelflux](pixelflux.md) capture and encoding, and broadcasts encoded frames to all connected clients over the WebSocket, with per client backpressure (frame acknowledgements, RTT smoothing, and stall detection) so one slow viewer does not degrade the rest. An opt in [WebRTC transport](../user-guide/webrtc.md) carries the same video and Opus streams over UDP with a priority pacer and optional congestion control; clients can switch transports at runtime.
- **Audio out**: drives pcmflux, which captures the PulseAudio `output.monitor` source and Opus encodes at up to 510kbps, with Opus RED redundancy against packet loss.
- **Microphone in**: receives PCM from the browser and plays it into a virtual PulseAudio source (`SelkiesVirtualMic`) that session apps consume as a normal mic.
- **Input**: injects keyboard, mouse, touch, and scroll. On Wayland, injection goes through pixelflux's compositor seat with an xkbcommon keymap, falling back to an in process virtual keyboard client for text the layout lacks, with no forked tools. On X11, through in process XTEST over a vendored python-xlib, with a spare keycode overlay for unicode and IME text. Gamepads are handled by per slot Unix socket servers feeding the input interposer (below), or by kernel uinput devices where `/dev/uinput` is writable.
- **Clipboard**: bidirectional, event driven sync, XFixes selection events on X11 and the compositor's data control on Wayland, with formatted text, optional binary (image) clipboard support, and chunked transfer for large payloads.
- **Files**: receives chunked uploads over the socket into the session and serves the file browser and downloads itself under `/api/files/`, paced against the video stream.
- **Printing**: runs a CUPS queue as the session user and hands each printed document to the browser as a PDF.
- **Operator API**: lists and closes connected pages, starts and stops a fragmented MP4 recording with audio, and takes screenshots, under `/api`, with an audit webhook that reports every transfer, print, connection, and recording.
- **Settings and stats**: pushes the sanitized settings schema to the client (this is what builds the sidebar UI, including which controls are locked), and streams CPU, GPU, memory, and network stats.
- **Sharing and roles**: manages controller, view only, and player 2 to 4 roles, either via URL fragments (`#shared`, `#player2`, with a second page on the plain address joining as a controller) or, in secure deployments, via a token table posted to `/api/tokens` with `SELKIES_MASTER_TOKEN` or read from `SELKIES_TOKENS_FILE`, which is what [SealSkin](sealskin.md) uses for its collaboration rooms. A page holds its token in the URL fragment, where no proxy log sees it.

Configuration is uniform: every setting is simultaneously a CLI flag (`--framerate`) and an environment variable (`SELKIES_FRAMERATE`), with the value syntax (ranges, enums, `|locked`) described in the [Configuration Reference](../user-guide/configuration.md). The protocol itself is documented in [The Streaming Protocol](../developer-guide/protocol.md).

## The web client

The client lives in the same repository under `addons/`:

- **selkies-web-core**: the engine. Connects the WebSocket, demultiplexes binary frames, decodes H.264, H.265, VP8, VP9, or AV1 with WebCodecs `VideoDecoder`, JPEG stripes with `createImageBitmap`, and Opus in a worker, renders to canvas, plays audio through an AudioWorklet, and captures all input including trackpad gestures and pointer lock. It exposes a documented `postMessage` API so any UI can be built on top of it.
- **selkies-dashboard**: the standard React sidebar UI described in [Using the Web Client](../user-guide/web-client.md), fully internationalized. Variants exist (`selkies-dashboard-wish` is the TypeScript rewrite with the same sections in an accordion layout), and the container's `DASHBOARD` variable selects between built dashboards. The postMessage split means a white label or kiosk frontend is just another dashboard. Browsers without WebCodecs audio get Opus decoded by a WebAssembly build of libopus, so Safari and older Firefox still carry sound, the microphone, and the webcam over WebSockets.
- **universal-touch-gamepad**: an on screen touch gamepad that injects itself into the browser's Gamepad API with configurable layouts.

## The gamepad trick

Two small C addons make plug and play gamepads work in unprivileged containers with no kernel devices:

- **input-interposer**: an `LD_PRELOAD` library that intercepts `open()` calls to `/dev/input/js*` and `/dev/input/event*` and transparently redirects them to Unix sockets served by Selkies, faithfully emulating the Linux joystick and evdev APIs (ioctls included). Apps think they opened a real Xbox 360 pad. It works in the other direction too: a preloaded application that opens `/dev/uinput` to create its own virtual device (Steam Input, a remapper) gets a socket backed device that sibling applications discover through fake udev, and with `SELKIES_PUBLISH_INPUT_DEVICES` the same pool carries a copy of the session keyboard and pointer for applications that enumerate evdev directly.
- **fake-udev**: a stub `libudev` that makes device enumeration APIs report the synthetic pads with a plausible sysfs hierarchy, for apps and engines (SDL, browsers) that discover devices through udev rather than by opening device nodes.

Both are preloaded automatically in the baseimages, and `NO_GAMEPAD=true` turns the whole mechanism off. Where `/dev/uinput` is writable Selkies registers real kernel devices instead, which need no preload, and a game's force feedback on either path is played back on the controller in the browser.

## Ports (inside a container)

| Port | What |
| --- | --- |
| 8082 | The Selkies server (`SELKIES_PORT`, upstream default is 8080, the baseimages set 8082 via `CUSTOM_WS_PORT`). Nginx proxies everything under `/api` to it: the data WebSocket at `/api/websockets`, WebRTC signaling at `/api/webrtc/signaling`, the transport switch, the file browser at `/api/files/`, printed documents, the operator API, and the token control plane at `/api/tokens`, which only the master token unlocks |
| 3000 / 3001 | Nginx HTTP and HTTPS in front of everything ([baseimage](baseimages.md) territory) |

## Relationship to the rest of the stack

Selkies deliberately does not do: TLS, HTTP auth, process supervision, GPU detection, or app packaging. All of that belongs to the [baseimage](baseimages.md). And it does not do capture or encoding itself, that is [pixelflux and pcmflux](pixelflux.md). This separation is what makes the pieces independently reusable: you can run the Selkies server against your own frontend, or embed pixelflux without any of Selkies.
