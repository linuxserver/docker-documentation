# Selkies

**Repository:** [selkies-project/selkies](https://github.com/selkies-project/selkies) · **License:** MPL-2.0 · **Upstream docs:** [selkies-project.github.io/selkies](https://selkies-project.github.io/selkies/)

Selkies is the heart of the platform: a ground up, web native remote desktop protocol and the Python server plus web client that implement it. It began in the Selkies project founded by Dan Isla (ex Google, ex NASA) with Seungmin Kim, targeting cloud gaming class remote desktops for Linux, and it is developed today in partnership between the Selkies organization and LinuxServer.io.

## What the server does

`selkies` is a Python asyncio application (console script `selkies`, installed in the baseimages at `/lsiopy/bin/selkies`) that owns the session:

- **Video**: drives [pixelflux](pixelflux.md) capture and encoding, and broadcasts encoded frames to all connected clients over the WebSocket, with per client backpressure (frame acknowledgements, RTT smoothing, and stall detection) so one slow viewer does not degrade the rest.
- **Audio out**: drives pcmflux, which captures the PulseAudio `output.monitor` source and Opus encodes at up to 320kbps.
- **Microphone in**: receives PCM from the browser and plays it into a virtual PulseAudio source (`SelkiesVirtualMic`) that session apps consume as a normal mic.
- **Input**: injects keyboard, mouse, touch, and scroll. On Wayland, injection goes through pixelflux's compositor APIs with an xkbcommon keymap (plus [waylandtyper](https://github.com/linuxserver/waylandtyper), our maintained fork of `wtype`, for unicode text batches). On X11, through pynput, xdotool, and python-xlib. Gamepads are handled by per slot Unix socket servers feeding the joystick interposer (below).
- **Clipboard**: bidirectional sync via `wl-clipboard` on Wayland or `xclip` on X11, with optional binary (image) clipboard support and chunked transfer for large payloads.
- **Files**: receives chunked uploads over the socket into the session; downloads are served by the container's Nginx file index.
- **Settings and stats**: pushes the sanitized settings schema to the client (this is what builds the sidebar UI, including which controls are locked), and streams CPU, GPU, memory, and network stats.
- **Sharing and roles**: manages primary, collaborator, view only, and player 2 to 4 roles, either via URL fragments (`#shared`, `#collab`, `#player2`) or, in secure deployments, via a token control plane on an internal port (`POST /tokens` authorized by `SELKIES_MASTER_TOKEN`), which is what [SealSkin](sealskin.md) uses for its collaboration rooms.

Configuration is uniform: every setting is simultaneously a CLI flag (`--framerate`) and an environment variable (`SELKIES_FRAMERATE`), with the value syntax (ranges, enums, `|locked`) described in the [Configuration Reference](../user-guide/configuration.md). The protocol itself is documented in [The Streaming Protocol](../developer-guide/protocol.md).

## The web client

The client lives in the same repository under `addons/`:

- **selkies-web-core**: the engine. Connects the WebSocket, demultiplexes binary frames, decodes H.264 with WebCodecs `VideoDecoder`, JPEG stripes with `createImageBitmap`, and Opus in a worker, renders to canvas, plays audio through an AudioWorklet, and captures all input including trackpad gestures and pointer lock. It exposes a documented `postMessage` API so any UI can be built on top of it.
- **selkies-dashboard**: the standard React sidebar UI described in [Using the Web Client](../user-guide/web-client.md), fully internationalized. Variants exist (`selkies-dashboard-wish` is a newer TypeScript and shadcn based rewrite), and the container's `DASHBOARD` variable selects between built dashboards. The postMessage split means a white label or kiosk frontend is just another dashboard.
- **universal-touch-gamepad**: an on screen touch gamepad that injects itself into the browser's Gamepad API with configurable layouts.

## The gamepad trick

Two small C addons make plug and play gamepads work in unprivileged containers with no kernel devices:

- **js-interposer**: an `LD_PRELOAD` library that intercepts `open()` calls to `/dev/input/js*` and `/dev/input/event*` and transparently redirects them to Unix sockets served by Selkies, faithfully emulating the Linux joystick and evdev APIs (ioctls included). Apps think they opened a real Xbox 360 pad.
- **fake-udev**: a stub `libudev` that makes device enumeration APIs report the synthetic pads with a plausible sysfs hierarchy, for apps and engines (SDL, browsers) that discover devices through udev rather than by opening device nodes.

Both are preloaded automatically in the baseimages, and `NO_GAMEPAD=true` turns the whole mechanism off.

## Ports (inside a container)

| Port | What |
| --- | --- |
| 8082 | The data WebSocket (`SELKIES_PORT`; upstream default is 8081, the baseimages set 8082), proxied by Nginx at `/websocket` |
| 8083 | Token control plane for secure sharing mode, never expose it |
| 3000 / 3001 | Nginx HTTP and HTTPS in front of everything ([baseimage](baseimages.md) territory) |

## Relationship to the rest of the stack

Selkies deliberately does not do: TLS, HTTP auth, process supervision, GPU detection, or app packaging. All of that belongs to the [baseimage](baseimages.md). And it does not do capture or encoding itself, that is [pixelflux and pcmflux](pixelflux.md). This separation is what makes the pieces independently reusable: you can run the Selkies server against your own frontend, or embed pixelflux without any of Selkies.
