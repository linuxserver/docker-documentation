# Configuration Reference

Every Selkies based container is configured through environment variables. This page collects all of them in one place. They fall into three groups:

1. **Container variables**: standard LinuxServer.io conventions plus Selkies baseimage options (ports, auth, GPU, language).
2. **Selkies application settings** (`SELKIES_*`): transport, stream, client UI, and feature toggles, with a locking syntax.
3. **Hardening variables**: lockdown options covered in detail on the [Security page](security.md).

## Standard LinuxServer variables

These work in every LinuxServer.io container:

| Variable | Default | Description |
| --- | --- | --- |
| `PUID` | `911` | User ID the in container user `abc` runs as, match it to your host user for sane volume ownership |
| `PGID` | `911` | Group ID for `abc` |
| `TZ` | `Etc/UTC` | Timezone, e.g. `Europe/London` |
| `DOCKER_MODS` | unset | Layer additional functionality at runtime, see [Installing Applications](installing-apps.md) |

## Baseimage variables

| Variable | Description |
| --- | --- |
| `PIXELFLUX_WAYLAND` | If set to true the container will initialize in Wayland mode running [Smithay](https://github.com/Smithay/smithay) and labwc while enabling zero copy encoding with a GPU. This is the default on supported hardware; set `false` to force legacy X11 |
| `SELKIES_DESKTOP` | If set to true and in Wayland mode, a simple desktop shell (panel, start menu, wallpaper, desktop icons) is initialized with labwc, see [Selkies Desktop](../components/selkies-desktop.md) |
| `PELORUS` | If set to true, the [Pelorus](../components/pelorus.md) agentic interface and accessibility stack are started alongside the session |
| `CUSTOM_PORT` | Internal HTTP port, default `3000` |
| `CUSTOM_HTTPS_PORT` | Internal HTTPS port, default `3001` |
| `CUSTOM_WS_PORT` | Internal port the Selkies server listens on behind Nginx, default `8082` |
| `CUSTOM_USER` | HTTP basic auth username, default `abc` |
| `PASSWORD` | HTTP basic auth password, default `abc`. If unset there is no auth |
| `DRI_NODE` | Encoding GPU, enables VAAPI/NVENC stream encoding on the given device, e.g. `/dev/dri/renderD128` |
| `DRINODE` | Rendering GPU for EGL and 3D acceleration, e.g. `/dev/dri/renderD128` |
| `AUTO_GPU` | Automatic GPU configuration when one is detected, first available GPU used for encoding and rendering. Set `false` to disable, or a vendor or driver name such as `nvidia`, `amdgpu`, or `intel` to pick a specific GPU on multi GPU hosts |
| `PIXELFLUX_CU` | Port to enable the Computer Use API server for AI agent control of the desktop, Wayland mode only |
| `SUBFOLDER` | Subfolder when running behind a subfolder reverse proxy, needs both slashes, e.g. `/subfolder/` |
| `TITLE` | Page title shown in the browser, default `Selkies` |
| `DASHBOARD` | Select the web client dashboard: `selkies-dashboard` or `selkies-dashboard-wish` |
| `FILE_MANAGER_PATH` | Change the default upload and download path, must be writable by the `abc` user |
| `START_DOCKER` | If `false`, a privileged container will not automatically start the Docker in Docker setup |
| `DISABLE_IPV6` | Set to `true` or any value to disable IPv6 |
| `LC_ALL` | Session language, e.g. `fr_FR.UTF-8`, see [Internationalization](#internationalization) |
| `NO_DECOR` | Run the application without window borders, for PWA style use. Toggle at runtime with `ctrl+shift+d` |
| `NO_FULL` | Do not automatically fullscreen applications when using the single app window manager |
| `NO_GAMEPAD` | Disable the userspace gamepad interposer injection. Also turns off `SELKIES_GAMEPAD_ENABLED`, the player 2 to 4 sharing links, and hides the gamepad section of the sidebar |
| `NO_WEBCAM` | Disable the virtual webcam. Without it the container creates `/dev/video0`, preloads the V4L2 interposer, and turns on `SELKIES_WEBCAM_ENABLED` so the browser can forward a camera into the session |
| `DISABLE_ZINK` | Do not set Zink variables when a GPU is detected, applications use CPU rendering |
| `DISABLE_DRI3` | X11 mode only, disable DRI3 acceleration |
| `MAX_RES` | Maximum virtual display resolution, default 16K (`15360x8640`) |
| `WATERMARK_PNG` | Full path inside the container to a watermark PNG, e.g. `/usr/share/selkies/www/icon.png` |
| `WATERMARK_LOCATION` | Where to paint the watermark, integer 1 to 6 |

**`WATERMARK_LOCATION` values:** `1` top left, `2` top right, `3` bottom left, `4` bottom right, `5` centered, `6` animated.

### How the baseimage feeds Selkies

The Selkies server reads its own `SELKIES_*` variables, and the baseimage's init scripts translate the container level variables above into them. A few of those translations are worth knowing because they change the defaults you would otherwise read off the upstream project:

| Selkies setting | Container default | Upstream default | Why |
| --- | --- | --- | --- |
| `SELKIES_ENCODER` | `h264enc,jpeg` | `h264enc,h264enc-striped,jpeg` | The striped H.264 encoder is left out of the sidebar menu |
| `SELKIES_VIDEO_STREAMING_MODE` | `false` | `true` | Desktop use favors damage tracking and paint over. Turn it on for gaming and video |
| `SELKIES_ENABLE_BASIC_AUTH` | `false` | `true` | Nginx handles the login using `CUSTOM_USER` and `PASSWORD`, so the Selkies server's own basic auth stays off |
| `SELKIES_ALLOWED_ORIGINS` | `*` | same origin only | Nginx fronts the server, so the cross origin guard is relaxed inside the container |
| `SELKIES_COMMAND_ENABLED` | `true` | `false` | The sidebar apps and launcher section depends on command messages. `HARDEN_DESKTOP=true` flips it back to `false` |
| `SELKIES_ENABLE_DUAL_MODE` | `false` | `true` | The WebSocket / WebRTC switch is hidden until you configure WebRTC, see [WebRTC Transport](webrtc.md) |
| `SELKIES_MODE` | `websockets` | `websockets` | Becomes `webrtc` automatically when any WebRTC, STUN, or TURN variable is set |
| `SELKIES_WEBCAM_ENABLED` | `true` | `false` | Turned on when the virtual webcam device can be created, `NO_WEBCAM` prevents it |
| `CUSTOM_WS_PORT` | `8082` | `8080` | Port the Selkies server listens on behind Nginx |

`HARDEN_DESKTOP=true` also sets `SELKIES_FILE_TRANSFERS` to empty and hides the files and apps sidebar sections unless you set those variables yourself. Anything you pass explicitly always wins over these defaults.

## Selkies application settings

Every facet of the streaming application can be configured with `SELKIES_*` variables. These also drive what the user can change in the sidebar UI: the server sends the resolved settings schema to the client, so a locked or single valued setting simply has no control to change.

Each setting is also a CLI flag with the same name, `SELKIES_VIDEO_CRF` is `--video-crf`. Precedence is CLI flag, then the `SELKIES_*` variable, then the legacy container variable where one exists (`PASSWORD`, `DRI_NODE`, and so on), then the built in default.

### Value syntax

- **Booleans and locking.** `true` or `1` (case insensitive) is on, anything else is off. Append `|locked` to prevent the user changing the setting in the UI: `-e SELKIES_USE_CPU="true|locked"`
- **Enums and lists.** Comma separated values, the first item is the default and the full list is what the user may pick from. A single item hides the UI dropdown entirely: `-e SELKIES_ENCODER="jpeg"`. Matching is case insensitive and invalid items are dropped; if nothing valid is left the built in menu is kept.
- **Ranges.** Three forms. `min-max` restricts the allowed span and keeps the built in initial value: `SELKIES_FRAMERATE="8-120"`. A bare value sets the initial value and keeps the built in span: `SELKIES_FRAMERATE="60"`. Both at once: `SELKIES_FRAMERATE="60,8-120"`. A degenerate span such as `"60-60"` locks the setting.
- **Empty means default.** Setting a variable to `""` means "use the built in default", except for list type settings where `""` or `none` means disabled (for example `SELKIES_FILE_TRANSFERS`).
- **Manual resolution.** Setting `SELKIES_MANUAL_WIDTH` or `SELKIES_MANUAL_HEIGHT` to a positive value forces manual resolution mode.

### Legacy variables

These names are no longer Selkies settings, but the containers still accept them. At startup the init script copies a legacy value into its current equivalent when you have not set the current name yourself, so existing compose files keep working. Prefer the current names for anything new.

| Legacy name | Current name | Notes |
| --- | --- | --- |
| `SELKIES_H264_CRF` | `SELKIES_VIDEO_CRF` | |
| `SELKIES_H264_FULLCOLOR` | `SELKIES_VIDEO_FULLCOLOR` | |
| `SELKIES_H264_STREAMING_MODE` | `SELKIES_VIDEO_STREAMING_MODE` | The legacy value overrides the container default of `false` |
| `SELKIES_H264_PAINTOVER_CRF` | `SELKIES_VIDEO_PAINTOVER_CRF` | |
| `SELKIES_H264_PAINTOVER_BURST_FRAMES` | `SELKIES_VIDEO_PAINTOVER_BURST_FRAMES` | |
| `SELKIES_IS_MANUAL_RESOLUTION_MODE` | `SELKIES_MANUAL_RESOLUTION` | |
| `SELKIES_CLIPBOARD_ENABLED` | `SELKIES_ENABLE_CLIPBOARD` | The current setting is a policy (`true`, `in`, `out`, `false`). A legacy `|locked` suffix is dropped |
| `x264enc` and `x264enc-striped` as `SELKIES_ENCODER` values | `h264enc` and `h264enc-striped` | Rewritten in place, the rest of the list is kept |

### Transport

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_MODE` | `websockets` | Streaming transport, `websockets` or `webrtc`. The containers switch this to `webrtc` automatically when any WebRTC variable is set, see [WebRTC Transport](webrtc.md) |
| `SELKIES_ENABLE_DUAL_MODE` | `false` (upstream `true`) | Show the transport switch in the UI so users can move between WebSockets and WebRTC at runtime |
| `SELKIES_BACKPRESSURE_QUEUE_SIZE` | `120` | WebSockets mode only. Max frames or audio chunks buffered per stream before dropping under backpressure, `1` to `100000`. Higher tolerates larger client hiccups at the cost of latency |
| `SELKIES_WEBRTC_PACER` | `true` | WebRTC mode only. Pace outgoing packets with strict priorities (audio and RTCP, then data channel, then video) so audio and input stay responsive when video bursts on a congested link. `SELKIES_WEBRTC_PACER_STALE_MS` sets the stale GOP purge deadline in milliseconds, `0` disables |
| `SELKIES_CONGESTION_CONTROL` | `false` | WebRTC mode only. Adapt the video bitrate to the bandwidth estimate from receiver feedback. Effective in CBR rate control mode, may trade quality for responsiveness |

### Video encoding

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_ENCODER` | `h264enc,jpeg` (upstream `h264enc,h264enc-striped,jpeg`) | Available video encoders, first is default. `h264enc` is full frame H.264 on NVENC or VA-API, falling back to the software encoder pixelflux was built with (x264, or OpenH264 in a GPL free build). `h264enc-striped` is CPU striped H.264 on that software encoder. `jpeg` is CPU striped JPEG. Only `h264enc` streams over WebRTC |
| `SELKIES_FRAMERATE` | `8-240`, initial `60` | Framerate range, initial value, or both |
| `SELKIES_RATE_CONTROL_MODE` | `crf` | H.264 rate control, `crf` (constant quality) or `cbr` (constant bitrate). WebRTC mode defaults to `cbr` unless you pin this |
| `SELKIES_ENABLE_RATE_CONTROL` | `true` | Let the client pick the rate control mode. Set `false` to lock the encoder to CRF |
| `SELKIES_VIDEO_CRF` | `5-50`, initial `25` | CRF range, initial value, or both. Lower is higher quality |
| `SELKIES_VIDEO_BITRATE` | `100-1000000`, initial `8000` | CBR bitrate in kbps: range, initial value, or both. `8000` is 8 Mbps |
| `SELKIES_VIDEO_MIN_QP` | `0` | CBR mode minimum H.264 QP, `0` to `51`, `0` is the encoder default. Raising it caps bit spend on easy content |
| `SELKIES_VIDEO_MAX_QP` | `0` | CBR mode maximum H.264 QP, `0` to `51`, `0` is the encoder default. Lowering it keeps text legible under motion at the cost of overshooting the bitrate target |
| `SELKIES_KEYFRAME_INTERVAL` | `0` | Seconds between scheduled recovery keyframes, `0` to `300`. `0` keeps the GOP infinite and sends keyframes only on demand, which keeps bitrate and quality steady |
| `SELKIES_VIDEO_FULLCOLOR` | `false` | Encode H.264 with 4:4:4 chroma instead of 4:2:0. A client whose decoder has no 4:4:4 profile turns it off for itself; where it is locked on such a client falls back to JPEG. See the [GPU caveats](gpu.md#fullcolor-444-and-hardware-encoders) |
| `SELKIES_VIDEO_STREAMING_MODE` | `false` (upstream `true`) | Turbo mode: encode every frame like a traditional video stream instead of damage tracking. Useful for gaming and full motion video |
| `SELKIES_USE_CPU` | `false` | Force CPU encoding even when a GPU encoder is available |
| `SELKIES_JPEG_QUALITY` | `1-100`, initial `40` | JPEG encoder quality range, initial value, or both |
| `SELKIES_USE_PAINT_OVER_QUALITY` | `true` | High quality paint over for static scenes |
| `SELKIES_PAINT_OVER_JPEG_QUALITY` | `1-100`, initial `90` | JPEG paint over quality range, initial value, or both |
| `SELKIES_VIDEO_PAINTOVER_CRF` | `5-50`, initial `18` | H.264 paint over CRF range, initial value, or both |
| `SELKIES_VIDEO_PAINTOVER_BURST_FRAMES` | `1-30`, initial `5` | H.264 paint over burst frames range, initial value, or both |
| `SELKIES_GPU_ID` | `''` | Hardware encoder GPU index, selects `/dev/dri/renderD{128 + n}` and the GPU stats index. Empty encodes on the first GPU or the one `AUTO_GPU` chose, `-1` disables hardware encoding. Ignored when `DRI_NODE` gives a device path |
| `SELKIES_ENCODE_DRI` (or `DRI_NODE`) | `''` | DRI render node the encoder uses for VA-API or NVENC |
| `SELKIES_RENDER_DRI` (or `DRINODE`) | `''` | DRI render node the Wayland compositor renders on, defaults to the `AUTO_GPU` pick, else software rendering |
| `SELKIES_AUTO_GPU` (or `AUTO_GPU`) | `true` | GPU auto selection for rendering: `true` picks the first GPU, `false` disables, or a vendor name, kernel driver name, devicetree prefix, or PCI vendor ID picks the first GPU it matches |
| `SELKIES_RECORDING_SOCKET` (or `PIXELFLUX_RECORDING_SOCKET`) | `''` | Unix socket path for an out of band H.264 recording tap, pixelflux multiplexes the elementary stream to connected clients. Empty is off |

### Audio

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_AUDIO_BITRATE` | `128000` | Opus bitrate in bps. The UI offers `32000` through `510000` in steps, any value from `6000` to `510000` is accepted |
| `SELKIES_AUDIO_FRAME_DURATION_MS` | `10` | Opus frame duration: `2.5`, `5`, `10`, `20`, `40`, or `60`. Lower cuts audio latency at a small bandwidth and packet rate cost |
| `SELKIES_AUDIO_REDUNDANCY` | `true` | Opus RED (RFC 2198) redundancy to cut dropouts under packet loss. On WebSockets it only engages when every connected client supports it |
| `SELKIES_AUDIO_REDUNDANCY_DISTANCE` | `2` | Number of prior Opus frames carried as redundancy, `0` to `4`. Higher survives longer loss bursts at proportionally more bandwidth |
| `SELKIES_AUDIO_CHANNELS` | `2` | Number of audio channels |
| `SELKIES_AUDIO_DEVICE_NAME` | `output.monitor` | PulseAudio source pcmflux captures |

### Display and input

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_MANUAL_RESOLUTION` | `false` | Lock the resolution to the manual width and height |
| `SELKIES_MANUAL_WIDTH` | `0` | Fixed width up to `16384`, a positive value forces manual resolution mode |
| `SELKIES_MANUAL_HEIGHT` | `0` | Fixed height up to `16384`, a positive value forces manual resolution mode |
| `SELKIES_ENABLE_RESIZE` | `true` | Dynamically resize the display to match the browser window |
| `SELKIES_SCALING_DPI` | `96` | Default DPI for UI scaling, `96` to `288` in steps of `24` |
| `SELKIES_FORCE_ALIGNED_RESOLUTION` | `false` | Forces the display resolution to be a multiple of 16 pixels |
| `SELKIES_USE_CSS_SCALING` | `false` | HiDPI when false. When true a lower resolution is sent and the canvas is stretched |
| `SELKIES_SECOND_SCREEN` | `true` | Offer the Add Screen button for a second monitor. Set `false` to hide it. On Wayland the button only appears when Selkies detects compositor support (labwc or KWin) regardless of this value |
| `SELKIES_ENABLE_CURSORS` | `true` | Send the remote application cursor to the client |
| `SELKIES_USE_BROWSER_CURSORS` | `true` | Use browser CSS cursors instead of rendering the cursor onto the canvas |
| `SELKIES_CURSOR_SIZE` (or `XCURSOR_SIZE`) | `-1` | Cursor size in points at 96 DPI, scaled with the session DPI. `-1` is the platform default, 32 on X11 and 24 on Wayland |
| `SELKIES_RAW_POINTER_MOTION` | `true` | Ask the browser for unaccelerated pointer movement under pointer lock (gaming mode). Windows and macOS honor it, Linux and Android do not. Clients on macOS leave it off unless chosen. Users may override unless locked |
| `SELKIES_DEBUG_CURSORS` | `false` | Cursor debug logging |

### Feature toggles and session start state

The `*_ENABLED` variables decide what the server offers at all. The `*_ON_START` variables decide whether a feature is already running when a client connects, or waits for the user to press its sidebar button.

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_AUDIO_ENABLED` | `true` | Server to client audio streaming. Disabling it also disables the microphone |
| `SELKIES_MICROPHONE_ENABLED` | `false` | Client to server microphone forwarding |
| `SELKIES_WEBCAM_ENABLED` | `true` (upstream `false`) | Client to server webcam forwarding into the virtual V4L2 device. Set by the baseimage unless `NO_WEBCAM` is present |
| `SELKIES_GAMEPAD_ENABLED` | `true` | Gamepad support. Forced off by `NO_GAMEPAD` |
| `SELKIES_VIDEO_ON_START` | `true` | Start with video on. Off, nothing is captured for the primary display until the user turns video on; shared viewers and second screens always start their stream |
| `SELKIES_AUDIO_ON_START` | `true` | Start with audio on. Off, capture stays stopped until the user turns audio on. Unlike `SELKIES_AUDIO_ENABLED=false` nothing is torn down and the microphone keeps working |
| `SELKIES_MICROPHONE_ON_START` | `false` | Start with the microphone on, so the browser asks for the device as soon as the session connects |
| `SELKIES_WEBCAM_ON_START` | `false` | Start with the webcam on, so the browser asks for the camera as soon as the session connects |
| `SELKIES_GAMEPAD_ON_START` | `true` | Start with gamepad input on. The user's choice is remembered by the browser and takes precedence on later visits |
| `SELKIES_COMMAND_ENABLED` | `true` (upstream `false`) | Parsing of command messages from the client, which the sidebar apps section needs. `HARDEN_DESKTOP` turns it off |
| `SELKIES_DEBUG` | `false` | Debug logging |

### Clipboard and files

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_ENABLE_CLIPBOARD` | `true` | Clipboard policy: `true` both directions, `in` client to server only, `out` server to client only, `false` disabled. `out` is what stops the page reading the local clipboard at all, which is the read Firefox and Safari raise a paste prompt for |
| `SELKIES_ENABLE_BINARY_CLIPBOARD` | `true` | Allow binary data such as images on the clipboard |
| `SELKIES_FILE_TRANSFERS` | `upload,download` | Allowed transfer directions, comma separated. Empty or `none` disables |
| `SELKIES_FILE_TRANSFER_LIMIT_MBPS` | `0` | Static throttle in Mbit/s shared by all uploads and downloads, for links whose rate you know. `0` disables. Transfers are already paced to protect the video stream without it |
| `SELKIES_FILE_MANAGER_PATH` (or `FILE_MANAGER_PATH`) | `~/Desktop` | Directory uploads land in and the file browser serves, created at startup if missing |

### Webcam

The containers create a virtual `/dev/video0` and preload a V4L2 interposer so ordinary applications see the browser's camera as a normal webcam. Set `NO_WEBCAM` to skip all of it.

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_WEBCAM_WIDTH` | `1280` | Width of the virtual webcam device, client frames are scaled and letterboxed to fit |
| `SELKIES_WEBCAM_HEIGHT` | `720` | Height of the virtual webcam device |
| `SELKIES_WEBCAM_PIXEL_FORMAT` | `auto` | Pixel format of the virtual device. `auto` follows the uplink (MJPEG for a browser sending JPEG, otherwise I420). Or pin `I420`, `NV12`, `YUYV`, or `MJPEG` |
| `SELKIES_WEBCAM_ENCODER` | `auto` | Codec WebSocket clients use for the camera uplink: `auto`, `h264`, `vp8`, or `mjpeg`. `auto` tries H.264, then VP8, and JPEG where neither keeps up. Users may override unless locked. WebRTC encodes in the browser and ignores this |
| `SELKIES_WEBCAM_DEVICE` | `auto` | Also mirror the webcam into a v4l2loopback kernel device: `auto` uses the first one found (usually only on a host or privileged container), a path such as `/dev/video10` uses that device, `false` never does |
| `SELKIES_WEBCAM_SOCKET_PATH` | `/tmp` | Directory for the V4L2 interposer socket, `selkies_webcam0.sock` |

### Gamepads

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_JS_SOCKET_PATH` | `/tmp` | Directory for the joystick interposer sockets, `selkies_js{0-3}.sock` |
| `SELKIES_UINPUT_GAMEPAD` | `auto` | Register gamepads as kernel devices through `/dev/uinput`, which Steam, Proton, and browsers inside the session find without the interposer. `auto` only does so where the interposer is not configured and `/dev/uinput` is writable, `true` always attempts it, `false` never does |
| `SELKIES_UINPUT_MOUSE_SOCKET` | `''` | Path to a uinput mouse socket, if not provided uinput is used directly |

### Sharing

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_ENABLE_SHARING` | `true` | Master toggle for all sharing features |
| `SELKIES_ENABLE_COLLAB` | `true` | Let a viewer holding the session's master key token act as a read write collaborator. Secure mode only, this is not a sharing link of its own |
| `SELKIES_ENABLE_SHARED` | `true` | View only sharing links |
| `SELKIES_ENABLE_PLAYER2` | `true` | Sharing link for gamepad player 2. Forced off by `NO_GAMEPAD` |
| `SELKIES_ENABLE_PLAYER3` | `true` | Sharing link for gamepad player 3. Forced off by `NO_GAMEPAD` |
| `SELKIES_ENABLE_PLAYER4` | `true` | Sharing link for gamepad player 4. Forced off by `NO_GAMEPAD` |
| `SELKIES_MASTER_TOKEN` | `''` | Master token that enables secure mode and protects the token control plane API, used by [SealSkin](../components/sealskin.md) |
| `SELKIES_BASIC_AUTH_VIEWONLY_PASSWORD` (or `VIEWONLY_PASSWORD`) | `''` | Optional second basic auth password that grants view only access when the Selkies server's own basic auth is on. Ignored in secure mode |

### Client UI visibility

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_UI_TITLE` | `Selkies` | Title in the top left corner of the sidebar |
| `SELKIES_UI_SHOW_LOGO` | `true` | Show the Selkies logo in the sidebar |
| `SELKIES_UI_SHOW_SIDEBAR` | `true` | Show the main sidebar UI |
| `SELKIES_UI_SHOW_CORE_BUTTONS` | `true` | Show the display, audio, microphone, webcam, and gamepad core buttons |
| `SELKIES_UI_SIDEBAR_SHOW_VIDEO_SETTINGS` | `true` | Video settings section |
| `SELKIES_UI_SIDEBAR_SHOW_SCREEN_SETTINGS` | `true` | Screen settings section |
| `SELKIES_UI_SIDEBAR_SHOW_AUDIO_SETTINGS` | `true` | Audio settings section |
| `SELKIES_UI_SIDEBAR_SHOW_STATS` | `true` | Stats section |
| `SELKIES_UI_SIDEBAR_SHOW_SHORTCUTS` | `true` | Keyboard shortcuts section |
| `SELKIES_UI_SIDEBAR_SHOW_CLIPBOARD` | `true` | Clipboard section |
| `SELKIES_UI_SIDEBAR_SHOW_FILES` | `true` | File transfer section. `HARDEN_DESKTOP` hides it |
| `SELKIES_UI_SIDEBAR_SHOW_APPS` | `true` | Applications section. `HARDEN_DESKTOP` hides it |
| `SELKIES_UI_SIDEBAR_SHOW_SHARING` | `true` | Sharing section |
| `SELKIES_UI_SIDEBAR_SHOW_GAMEPADS` | `true` | Gamepads section. `NO_GAMEPAD` hides it |
| `SELKIES_UI_SIDEBAR_SHOW_WEBCAM` | `true` | Webcam toggle among the core buttons. Hides the control only, `SELKIES_WEBCAM_ENABLED` governs whether the server accepts frames |
| `SELKIES_UI_SIDEBAR_SHOW_FULLSCREEN` | `true` | Fullscreen button |
| `SELKIES_UI_SIDEBAR_SHOW_GAMING_MODE` | `true` | Gaming mode button |
| `SELKIES_UI_SIDEBAR_SHOW_TRACKPAD` | `true` | Virtual trackpad button |
| `SELKIES_UI_SIDEBAR_SHOW_KEYBOARD_BUTTON` | `true` | On screen keyboard button in the display area |
| `SELKIES_UI_SIDEBAR_SHOW_SOFT_BUTTONS` | `true` | Soft buttons section |

### Server and diagnostics

The container's built in Nginx owns the listening ports, TLS, basic auth, and the `SUBFOLDER` prefix, and the init scripts hand the matching values to Selkies. Use the container variables (`CUSTOM_PORT`, `CUSTOM_HTTPS_PORT`, `CUSTOM_WS_PORT`, `CUSTOM_USER`, `PASSWORD`, `SUBFOLDER`) rather than the Selkies server's own listener, HTTPS, and basic auth settings, which exist for running the `selkies` binary outside these containers.

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_ALLOWED_ORIGINS` | `*` (upstream same origin) | Comma separated browser Origins allowed to open the streaming WebSocket, a cross site WebSocket hijacking guard. Relaxed in the containers because Nginx fronts the server |
| `SELKIES_ENABLE_METRICS_HTTP` | `false` | Prometheus metrics endpoint on the Selkies server |
| `SELKIES_ENABLE_WEBRTC_STATISTICS` | `false` | Dump WebRTC statistics CSVs from the client |
| `SELKIES_WEBRTC_STATISTICS_DIR` | `/tmp` | Directory for those CSVs, `selkies-stats-video-[timestamp].csv` and `selkies-stats-audio-[timestamp].csv` |

### Display backend

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_WAYLAND` (or `PIXELFLUX_WAYLAND`) | `false` | Run the Wayland headless compositor backend instead of X11 capture and input. The containers set `PIXELFLUX_WAYLAND` for you on supported hardware |
| `SELKIES_APP_WAYLAND_DISPLAY` | `''` | Wayland socket applications run on when it differs from the capture compositor, for a nested session. Empty auto detects |
| `SELKIES_WAYLAND_HOST_DISPLAY` | `''` | Socket of an external compositor (labwc started headless, for example) that pixelflux captures and injects into as a client instead of compositing itself. Empty keeps the built in compositor |
| `SELKIES_WAYLAND_SOCKET_INDEX` | `0` | Index for the Wayland command socket, `0` is `wayland-0` |
| `SELKIES_COMPUTER_USE_BIND` | `''` | Start pixelflux's Computer Use HTTP server on comma separated entries, a bare port listens on loopback only, `host:port` names the address. `PIXELFLUX_CU` remains the standalone fallback |

### Lifecycle hooks

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_RUN_AFTER_CONNECT` | `''` | Shell command run after the first client connects, and again whenever a client connects while no others are connected |
| `SELKIES_RUN_AFTER_DISCONNECT` | `''` | Shell command run after the last client disconnects, including on server shutdown while clients are connected |
| `SELKIES_APP_WAIT_READY` | `false` | Wait for the ready file to exist before starting the stream |
| `SELKIES_APP_READY_FILE` | `/tmp/selkies-appready` | File a sidecar creates to signal the application is ready |

### Watermark

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_WATERMARK_PATH` (or `WATERMARK_PNG`) | `''` | Absolute path to a watermark PNG |
| `SELKIES_WATERMARK_LOCATION` (or `WATERMARK_LOCATION`) | `-1` | Watermark location enum 0 to 6 |

### WebRTC networking, STUN, and TURN

Setting any of these switches the container into WebRTC mode with the transport switch enabled. They are only meaningful for WebRTC; the [WebRTC Transport](webrtc.md) page explains when you need which.

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_WEBRTC_PUBLIC_IP` | `''` | Public IPv4 and/or IPv6 address (comma or space separated) to advertise in host ICE candidates, for a host behind static 1:1 NAT such as a cloud instance with an elastic IP. STUN and TURN candidates are left untouched |
| `SELKIES_WEBRTC_PORT_RANGE` | `''` | Inclusive UDP port range `min-max` (e.g. `50000-50100`) that sessions bind into, both bounds within `1024` to `65535`. Empty uses ephemeral OS ports |
| `SELKIES_WEBRTC_UDP_MUX_PORT` | `0` | Single UDP port every session shares for its host candidates, so one forwarded port serves any number of sessions. `0` gives each session its own sockets |
| `SELKIES_WEBRTC_TCP_MUX_PORT` | `0` | Single TCP port the server accepts ICE-TCP connections on, so clients on networks that block UDP still connect. May equal the UDP mux port. `0` offers no TCP candidates |
| `SELKIES_WEBRTC_ICE_LITE` | `false` | Run the server's ICE agent as ICE-lite, offering host candidates only. Suits a server whose host candidates are reachable as advertised: a public address, a static NAT with the public IP set, or forwarded mux ports |
| `SELKIES_STUN_HOST` | `stun.l.google.com` | STUN host for NAT hole punching, change to an internal server on networks without internet |
| `SELKIES_STUN_PORT` | `19302` | STUN port |
| `SELKIES_RTC_CONFIG_JSON` | `/tmp/rtc.json` | JSON file with a full WebRTC ICE configuration, checked periodically. When it exists it overrides every other STUN and TURN setting |
| `SELKIES_TURN_REST_URI` | `''` | URI of a TURN REST API service that hands out time limited credentials, e.g. `http://localhost:8008`. Overrides the static TURN settings below |
| `SELKIES_TURN_REST_API_KEY` | `''` | API key sent to the TURN REST API service |
| `SELKIES_TURN_REST_USERNAME` | `''` | Username sent to the TURN REST API service, empty uses `selkies` |
| `SELKIES_TURN_REST_USERNAME_AUTH_HEADER` | `x-auth-user` | Header carrying the username to the TURN REST API |
| `SELKIES_TURN_REST_PROTOCOL_HEADER` | `x-turn-protocol` | Header carrying the desired TURN protocol to the TURN REST API |
| `SELKIES_TURN_REST_TLS_HEADER` | `x-turn-tls` | Header carrying the TURN TLS preference to the TURN REST API |
| `SELKIES_TURN_HOST` | `staticauth.openrelay.metered.ca` | TURN host for shared secret or long term credentials, IPv6 addresses in square brackets |
| `SELKIES_TURN_PORT` | `443` | TURN port |
| `SELKIES_TURN_PROTOCOL` | `udp` | TURN transport the client uses, `udp` or `tcp`. Use `tcp` only if UDP is blocked |
| `SELKIES_TURN_TLS` | `false` | TURN over TLS (TCP) or DTLS (UDP), requires a valid certificate on the TURN server |
| `SELKIES_TURN_SHARED_SECRET` | `openrelayprojectsecret` | Shared secret used to generate time limited HMAC credentials, with `SELKIES_TURN_HOST` and `SELKIES_TURN_PORT` |
| `SELKIES_TURN_USERNAME` | `''` | Long term credential username, with `SELKIES_TURN_HOST` and `SELKIES_TURN_PORT` |
| `SELKIES_TURN_PASSWORD` | `''` | Long term credential password |
| `SELKIES_ENABLE_CLOUDFLARE_TURN` | `false` | Use the Cloudflare TURN service, requires the two Cloudflare variables below |
| `SELKIES_CLOUDFLARE_TURN_TOKEN_ID` | `''` | Cloudflare TURN app token ID |
| `SELKIES_CLOUDFLARE_TURN_API_TOKEN` | `''` | Cloudflare TURN API token |

## Optional run configurations

| Argument | Description |
| --- | --- |
| `--privileged` | Starts a Docker in Docker environment inside the container. For better performance mount the Docker data directory from the host, e.g. `-v /path/to/docker-data:/var/lib/docker` |
| `-v /var/run/docker.sock:/var/run/docker.sock` | Manage host containers from inside this container |
| `--device /dev/dri:/dev/dri` | Mount a GPU, combine with `DRINODE` to pick a card |
| `--shm-size=1gb` | Required for Electron apps and browsers |
| `--security-opt seccomp=unconfined` | Last resort for older kernels or libseccomp versions where modern syscalls are blocked |

## Internationalization

Set `LC_ALL` to launch the session in another language:

- `-e LC_ALL=zh_CN.UTF-8` Chinese
- `-e LC_ALL=ja_JP.UTF-8` Japanese
- `-e LC_ALL=ko_KR.UTF-8` Korean
- `-e LC_ALL=ar_AE.UTF-8` Arabic
- `-e LC_ALL=ru_RU.UTF-8` Russian
- `-e LC_ALL=es_MX.UTF-8` Spanish (Latin America)
- `-e LC_ALL=de_DE.UTF-8` German
- `-e LC_ALL=fr_FR.UTF-8` French
- `-e LC_ALL=nl_NL.UTF-8` Dutch
- `-e LC_ALL=it_IT.UTF-8` Italian

## Hardening variables

`HARDEN_DESKTOP`, `HARDEN_OPENBOX`, `DISABLE_SUDO`, `DISABLE_TERMINALS`, `RESTART_APP`, and friends are documented with context on the [Security and Hardening](security.md) page.
