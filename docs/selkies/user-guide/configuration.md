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
| `PIXELFLUX_WAYLAND` | If set to true the container initializes in Wayland mode running [Smithay](https://github.com/Smithay/smithay) and labwc, `false` runs the X11 stack with Xvfb and Openbox. Zero copy GPU encoding works on both. Each image bakes in the stack its application or desktop runs on, see the [support matrix](apps.md#webtop-full-desktops) |
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
| `PIXELFLUX_CU` | Port of pixelflux's own Computer Use API server, the standalone fallback for `SELKIES_COMPUTER_USE_BIND`. `PELORUS=true` sets it to `5000`. The server takes a bearer token from `PIXELFLUX_CU_TOKEN`, see [Display backend](#display-backend) |
| `SUBFOLDER` | Subfolder when running behind a subfolder reverse proxy, needs both slashes, e.g. `/subfolder/`. Nginx and the Selkies server both read it, Selkies as the fallback for `SELKIES_SUBFOLDER` |
| `TITLE` | Name of the page when it is installed as a web app (the PWA manifest), default `Selkies`. The sidebar header and the browser tab follow `SELKIES_UI_TITLE` |
| `DASHBOARD` | Select the web client dashboard: `selkies-dashboard` or `selkies-dashboard-wish` |
| `FILE_MANAGER_PATH` | Change the default upload and download path, must be writable by the `abc` user. Fallback for `SELKIES_FILE_MANAGER_PATH` |
| `START_DOCKER` | If `false`, a privileged container will not automatically start the Docker in Docker setup |
| `DISABLE_IPV6` | Set to `true` or any value to disable IPv6 |
| `LC_ALL` | Session language, e.g. `fr_FR.UTF-8`, see [Internationalization](#internationalization) |
| `NO_DECOR` | Run the application without window borders, for PWA style use. Toggle at runtime with `ctrl+shift+d` |
| `NO_FULL` | Do not automatically fullscreen applications when using the single app window manager |
| `NO_GAMEPAD` | Disable the userspace gamepad interposer injection. Also locks `SELKIES_GAMEPAD_ENABLED` and the player 2 to 4 sharing links off, and hides the gamepad section of the sidebar |
| `NO_STEAM` | Remove the built in Steam installer, see [Installing Applications](installing-apps.md#steam-built-in-reinstalls-itself) |
| `NO_WEBCAM` | Disable the virtual webcam. Without it the container creates `/dev/video0`, preloads the V4L2 interposer, and turns on `SELKIES_WEBCAM_ENABLED` so the browser can forward a camera into the session |
| `DISABLE_DRI3` | X11 mode only, start Xvfb without the GPU. Applications render on the CPU and capture falls back to shared memory |
| `CUPS_SERVER` | Set by the container to the session's own print queue socket unless you set it yourself or turn printing off. Point it at a network CUPS server to print there instead of through the browser |
| `PAPERSIZE` | Paper size the Selkies print queue prints on, default `A4`, e.g. `letter` |
| `WATERMARK_PNG` | Full path inside the container to a watermark PNG, e.g. `/usr/share/selkies/www/icon.png` |
| `WATERMARK_LOCATION` | Where to paint the watermark, integer 1 to 6 |

**`WATERMARK_LOCATION` values:** `1` top left, `2` top right, `3` bottom left, `4` bottom right, `5` centered, `6` animated.

### How the baseimage feeds Selkies

The Selkies server reads its own `SELKIES_*` variables, and the baseimage's init scripts translate the container level variables above into them. A few of those translations are worth knowing because they change the defaults you would otherwise read off the upstream project:

| Selkies setting | Container default | Upstream default | Why |
| --- | --- | --- | --- |
| `SELKIES_ENCODER` | `h264enc,h265enc,vp8enc,vp9enc,av1enc,jpeg` | `h264enc,h265enc,vp8enc,vp9enc,av1enc,h264enc-striped,jpeg` | The striped H.264 encoder is left out of the sidebar menu. Selkies then drops any encoder this host cannot serve, see [Video encoders](#video-encoders) |
| `SELKIES_VIDEO_STREAMING_MODE` | `false` | `true` | Desktop use favors damage tracking and paint over. Turn it on for gaming and video |
| `SELKIES_RATE_CONTROL_MODE` | `crf,cbr` | `cbr,crf` | Desktop use favors constant quality, so CRF stays first and CBR is selectable. Upstream defaults to CBR on both transports |
| `SELKIES_ENABLE_BASIC_AUTH` | `false` | `true` | Nginx handles the login using `CUSTOM_USER` and `PASSWORD`, so the Selkies server's own basic auth stays off. Upstream refuses to start with it on and no password set |
| `SELKIES_ALLOWED_ORIGINS` | `*` | same origin only | Nginx fronts the server, so the cross origin guard is relaxed inside the container |
| `SELKIES_COMMAND_ENABLED` | `true` | `false` | The sidebar apps and launcher section depends on command messages. `HARDEN_DESKTOP=true` flips it back to `false` |
| `SELKIES_ENABLE_DUAL_MODE` | `false` | `true` | The WebSocket / WebRTC switch is hidden until you configure WebRTC, see [WebRTC Transport](webrtc.md) |
| `SELKIES_MODE` | `websockets` | `websockets` | Becomes `webrtc` automatically when any WebRTC, STUN, or TURN variable is set |
| `SELKIES_WEBCAM_ENABLED` | `true` | `false` | Turned on when the virtual webcam device can be created, `NO_WEBCAM` prevents it |
| `CUSTOM_WS_PORT` | `8082` | `8080` | Port the Selkies server listens on behind Nginx |

Everything the container does not translate keeps its upstream default. Two of those are worth knowing: `SELKIES_CONGESTION_CONTROL` is on, and only acts once a session runs under CBR, and `SELKIES_USE_PAINT_OVER_QUALITY` is on because Turbo mode is off.

`HARDEN_DESKTOP=true` also sets `SELKIES_FILE_TRANSFERS` to empty, turns `SELKIES_PRINTING_ENABLED` off, and hides the files and apps sidebar sections unless you set those variables yourself. Anything you pass explicitly always wins over these defaults.

## Selkies application settings

Every facet of the streaming application can be configured with `SELKIES_*` variables. These also drive what the user can change in the sidebar UI: the server sends the resolved settings schema to the client, so a locked or single valued setting simply has no control to change.

Each setting is also a CLI flag with the same name, `SELKIES_VIDEO_CRF` is `--video-crf`. Precedence is CLI flag, then the `SELKIES_*` variable, then the legacy container variable where one exists (`PASSWORD`, `DRI_NODE`, and so on), then the built in default. The upstream [Settings Reference](https://docs.selkies.io/settings) is generated from the server's own definitions and is the authoritative list; this page describes the same settings as the containers ship them.

### Value syntax

- **Booleans and locking.** `true` or `1` (case insensitive) is on, anything else is off. Append `|locked` to prevent the user changing the setting in the UI: `-e SELKIES_USE_CPU="true|locked"`
- **Enums and lists.** Comma separated values, the first item is the default and the full list is what the user may pick from. A single item hides the UI dropdown entirely: `-e SELKIES_ENCODER="jpeg"`. Matching is case insensitive and invalid items are dropped; if nothing valid is left the built in menu is kept.
- **Ranges.** Three forms. `min-max` restricts the allowed span and keeps the built in initial value: `SELKIES_FRAMERATE="8-120"`. A bare value sets the initial value and keeps the built in span, widening it when the value falls outside: `SELKIES_FRAMERATE="60"`. Both at once: `SELKIES_FRAMERATE="60,8-120"`. A degenerate span such as `"60-60"` locks the setting.
- **Empty means default.** Setting a variable to `""` means "use the built in default", except for list type settings where `""` or `none` means disabled (for example `SELKIES_FILE_TRANSFERS`).
- **Manual resolution.** Setting `SELKIES_MANUAL_WIDTH` or `SELKIES_MANUAL_HEIGHT` to a positive value forces manual resolution mode.
- **Per user overrides.** Some settings say "users may override unless locked": the browser keeps the user's choice for that setting and applies it on later visits, so the variable sets the starting position rather than a fixed value. Append `|locked` to pin it.

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
| `openh264enc` as a `SELKIES_ENCODER` value | `h264enc` | Selkies itself maps it. Software H.264 is whatever encoder the pixelflux build carries, x264 in the wheels the containers ship |

### Transport

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_MODE` | `websockets` | Streaming transport, `websockets` or `webrtc`. The containers switch this to `webrtc` automatically when any WebRTC variable is set, see [WebRTC Transport](webrtc.md) |
| `SELKIES_ENABLE_DUAL_MODE` | `false` (upstream `true`) | Show the transport switch in the UI so users can move between WebSockets and WebRTC at runtime. With it on, a page whose WebRTC media path keeps failing is offered WebSockets |
| `SELKIES_BACKPRESSURE_QUEUE_SIZE` | `120` | WebSockets mode only. Max frames or audio chunks buffered per stream before dropping under backpressure, `1` to `100000`. Higher tolerates larger client hiccups at the cost of latency |
| `SELKIES_WEBRTC_PACER` | `true` | WebRTC mode only. Pace outgoing packets with strict priorities (audio and RTCP, then data channel, then video) so audio and input stay responsive when video bursts on a congested link. `SELKIES_WEBRTC_PACER_STALE_MS` sets the stale GOP purge deadline in milliseconds, `0` disables |
| `SELKIES_CONGESTION_CONTROL` | `true` | Under CBR on either transport, adapt a display's bitrate to what its path carries, never above the bitrate the client chose: over WebRTC from the receiver's transport wide feedback (loss and a rise in one way delay), over WebSockets from the queue the frame round trip shows. A page keeps the rate its display settled on for ten seconds, and a restarted server starts that page's stream there for a day or until the user sets a bitrate. `false` holds the chosen bitrate whatever the path carries, so a slower path lags or drops frames. No effect under CRF, the container default |

### Video encoders

`SELKIES_ENCODER` is a comma separated menu of the values below. The first item is the default and the whole list is what the sidebar offers. Every full frame codec is encoded on the GPU when the encoding device has an engine for it, and by the software encoder in the pixelflux build otherwise, so the same menu works on a CPU only host, an Intel or AMD card, and an Nvidia card. The container default is `h264enc,h265enc,vp8enc,vp9enc,av1enc,jpeg`.

| Value | Codec | Hardware | Software | Shape | FullColor 4:4:4 | 10-bit | WebRTC | Browser decode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `h264enc` | H.264 | NVENC, VA-API | x264 | Full frame | NVENC and x264. VA-API has no 4:4:4 H.264 profile on current drivers, so the request is honored on the CPU instead | x264 only | Yes | Every browser |
| `h265enc` | H.265 (HEVC) | NVENC, VA-API | x265 | Full frame | NVENC and x265, VA-API negotiates per device | NVENC, VA-API, x265 | Yes | Safari, and Chromium where the operating system supplies an HEVC decoder. Chrome and Firefox on Linux decode no HEVC |
| `vp8enc` | VP8 | VA-API, on the few GPUs that still carry a VP8 engine | libvpx | Full frame | No | No | Yes | Every browser |
| `vp9enc` | VP9 | VA-API | libvpx | Full frame | Profile 1 on VA-API and libvpx | VA-API and libvpx, profiles 2 and 3 | Yes | Chromium, Firefox |
| `av1enc` | AV1 | NVENC on Ada and newer, VA-API on GPUs with an AV1 engine | SVT-AV1 | Full frame | No | NVENC, VA-API, SVT-AV1 | Yes | Chromium, Firefox. WebKit refuses it at decode time |
| `h264enc-striped` | H.264 | None, always CPU | x264 | Striped, one stripe per core | x264 | No | No | Every browser |
| `jpeg` | JPEG | None, always CPU | libjpeg-turbo | Striped, one stripe per core | Always full color | No | No | Every browser, including ones without WebCodecs |

Nvidia has no VP8 or VP9 encode engine, so those two codecs are software on every Nvidia card. AMD has no VP8 or VP9 engine either, and AV1 starts with RDNA 3. Intel carries VP9 and, on Arc and newer integrated graphics, AV1. Run `vainfo` inside the container to see the encode entry points your card exposes. The same pixelflux wheels also carry a Jetson's Tegra encoder and V4L2 memory to memory engines; this guide covers the three desktop GPU vendors.

How the menu behaves at runtime:

- **The host trims the menu.** At startup Selkies probes the encoding device once and drops every encoder that neither the GPU nor the pixelflux software build can serve, logging `Encoders not served on this host are left off the menu`. If the default itself is not served the session starts on the next encoder down the ladder below. The wheels in the containers carry a software encoder for all five codecs, so on a CPU only host the full menu still appears, all of it in software.
- **The browser greys out what it cannot decode.** Encoders the browser has no decoder for stay in the menu disabled and labelled `(Unsupported Browser)`. A browser that cannot decode the server default steps down one ladder: the codecs this host encodes in hardware, most efficient first (AV1, H.265, VP9, H.264, VP8), then the ones it encodes in software in order of encode time (H.264, AV1, VP8, H.265, VP9), then `h264enc-striped`, and `jpeg` last. Only encoders in the allowed menu are stepped to, so a browser facing a single valued locked encoder it cannot play gets an on page error instead.
- **Only H.264 and JPEG are striped.** H.265, VP8, VP9, and AV1 always encode the whole frame, so they never get the per core parallelism or the dirty stripe savings of the H.264 and JPEG paths. In software they also cost several times the CPU of x264. On a machine whose GPU lacks the engine, keep `h264enc` first and treat the other codecs as options for GPU hosts.
- **Software encoding toggle.** The sidebar's CPU encoding switch only appears for a codec the host serves both ways, since it moves the session between the GPU and the software encoder and would be a no-op otherwise. `SELKIES_USE_CPU` still applies to every full frame codec. While a session encodes in software the sidebar also shows the multithreading switch behind `SELKIES_CPU_ENCODE_THREADING`.
- **Demotion.** If pixelflux still cannot serve the codec once capture starts it walks the same ladder itself, the other codecs the host serves in hardware first, then software, then striped H.264, then JPEG, and Selkies rewrites the encoder setting to match, logging `no encoder served`. Trust the encoder shown in the sidebar over the one you configured.
- **10-bit.** `SELKIES_VIDEO_10BIT` asks for 10 bits per sample where the codec and encoder carry it. The desktop is an 8-bit source, so the extra bits add precision to the color conversion rather than new shades, and a software encoder pays for them in CPU. It is only worth pairing with FullColor 4:4:4, and the sidebar offers it only where the browser's decoder returns a 10-bit picture for that codec.
- **Colors.** VP8 cannot signal BT.709, so it is encoded and declared BT.601 and looks very slightly different from the other codecs. Firefox before 157 paints AV1 received over WebRTC as BT.601 for the same reason.

### Video encoding

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_ENCODER` | `h264enc,h265enc,vp8enc,vp9enc,av1enc,jpeg` (upstream adds `h264enc-striped`) | Menu of video encoders, first is default, see [Video encoders](#video-encoders). Encoders the host cannot serve are dropped at startup, and the five full frame codecs are the ones that stream over WebRTC |
| `SELKIES_FRAMERATE` | `8-240`, initial `60` | Framerate range, initial value, or both. The sidebar also offers the client display's own refresh rate |
| `SELKIES_RATE_CONTROL_MODE` | `crf,cbr` (upstream `cbr,crf`) | Menu of rate control modes for every video codec, first is default: `crf` constant quality, `cbr` constant bitrate. A single value locks it. The container keeps CRF first on both transports, upstream defaults to CBR. CBR is what [congestion control](#transport) steers, so pick it for lossy links |
| `SELKIES_ENABLE_RATE_CONTROL` | `true` | Let the client pick the rate control mode. Set `false` to lock the encoder to the first mode in the menu |
| `SELKIES_VIDEO_CRF` | `5-50`, initial `25` | CRF range, initial value, or both. Lower is higher quality. The value is on the H.264 QP scale and pixelflux maps it onto each codec's own quantizer range, so one number means the same quality on every encoder |
| `SELKIES_VIDEO_BITRATE` | `100-1000000`, initial `8000` | CBR bitrate in kbps: range, initial value, or both. `8000` is 8 Mbps |
| `SELKIES_VIDEO_MIN_QP` | `0` | CBR mode minimum quantizer on the H.264 QP scale, `0` to `51`, mapped onto each codec's own range. `0` is the encoder default. Raising it caps bit spend on easy content |
| `SELKIES_VIDEO_MAX_QP` | `0` | CBR mode maximum quantizer on the same scale, `0` is the encoder default. Lowering it keeps text legible under motion at the cost of overshooting the bitrate target |
| `SELKIES_KEYFRAME_INTERVAL` | `0` | Seconds between scheduled recovery keyframes, `0` to `300`. `0` keeps the GOP infinite and sends keyframes only on demand, which keeps bitrate and quality steady |
| `SELKIES_VIDEO_FULLCOLOR` | `false` | Encode 4:4:4 chroma instead of 4:2:0 where the codec and encoder carry it: H.264 and H.265 on NVENC, x264, and x265, H.265 on VA-API where the driver negotiates a surface, VP9 profile 1 on VA-API and libvpx. VP8, AV1, and OpenH264 stay 4:2:0. The server knows which of its encoders carry it on this host and the browser reports which 4:4:4 profiles it decodes, so a client without the profile streams 4:2:0 on the same codec; where it is locked, such a client steps to the next allowed encoder whose 4:4:4 it decodes, JPEG last. See the [GPU caveats](gpu.md#fullcolor-444-and-hardware-encoders) |
| `SELKIES_VIDEO_10BIT` | `false` | Encode 10 bits per sample where the codec has a 10-bit profile an encoder on this host codes: H.264 on x264, and H.265, VP9, and AV1 on VA-API, x265, libvpx, and SVT-AV1, and H.265 and AV1 on NVENC. A GPU that does not encode the format hands the session to the software encoder, as it does a 4:4:4 it lacks. Costs CPU on software encoders, so only recommended together with FullColor. A client whose decoder shows no 10-bit picture turns it off for itself; where it is locked, such a client steps to the next allowed encoder it decodes. Chromium decodes AV1 over WebRTC at 8 bits only |
| `SELKIES_VIDEO_STREAMING_MODE` | `false` (upstream `true`) | Turbo mode: encode every frame like a traditional video stream instead of damage tracking. Useful for gaming and full motion video |
| `SELKIES_USE_CPU` | `false` | Force software encoding for the full frame codecs even when the encoding GPU serves them. The striped encoders are CPU regardless |
| `SELKIES_CPU_ENCODE_THREADING` | `true` | Spread each frame a software encoder codes across threads: x264 codes a frame in slices on several threads, libvpx, x265, and SVT-AV1 run their worker threads, and the striped encoders code their stripes in parallel. Set `false` on hosts that pack many sessions onto their cores so each session's encode keeps to one thread, at the cost of a slower frame that a high frame rate notices. Hardware encoders are unaffected, so the sidebar shows the switch only while the session encodes in software. Users may override unless locked |
| `SELKIES_JPEG_QUALITY` | `1-100`, initial `40` | JPEG encoder quality range, initial value, or both |
| `SELKIES_USE_PAINT_OVER_QUALITY` | `true` | Clean up a still screen at the paint over quality. Left unset it is on except while Turbo mode drives a video encoder, so the container default is on. Under CRF, and for JPEG, a still screen is only cleaned up with it on. Under CBR a video stream is cleaned up to the paint over CRF whatever this says, since a rate control alone leaves a low bitrate short of a clean picture, so the sidebar hides the switch there |
| `SELKIES_PAINT_OVER_JPEG_QUALITY` | `1-100`, initial `90` | JPEG paint over quality range, initial value, or both |
| `SELKIES_VIDEO_PAINTOVER_CRF` | `5-50`, initial `18` | Paint over quality for every video codec, on the CRF scale: range, initial value, or both. Under CRF it must be lower than the CRF to trigger. Under CBR it is the finest a still screen is refined to, reached as fast as the path carries |
| `SELKIES_VIDEO_PAINTOVER_BURST_FRAMES` | `1-30`, initial `5` | Frames a video encoder keeps sending after a cleanup or a key frame on a still screen so rate control settles: range, initial value, or both. Under CBR most encoders keep sending until the screen is clean instead |
| `SELKIES_GPU_ID` | `''` | Hardware encoder GPU index, selects `/dev/dri/renderD{128 + n}` and the GPU stats index. Empty encodes on the first GPU or the one `AUTO_GPU` chose, `-1` disables hardware encoding. Ignored when `DRI_NODE` gives a device path |
| `SELKIES_ENCODE_DRI` (or `DRI_NODE`) | `''` | DRI render node the encoder uses for VA-API or NVENC |
| `SELKIES_RENDER_DRI` (or `DRINODE`) | `''` | DRI render node the display server renders on, the Wayland compositor or Xvfb through glamor. Defaults to the `AUTO_GPU` pick, else software rendering |
| `SELKIES_AUTO_GPU` (or `AUTO_GPU`) | `true` | GPU auto selection for rendering: `true` picks the first GPU, `false` disables, or a vendor name, kernel driver name, devicetree prefix, or PCI vendor ID picks the first GPU it matches |
| `SELKIES_RECORDING_SOCKET` (or `PIXELFLUX_RECORDING_SOCKET`) | `''` | Unix socket path for an out of band recording tap, pixelflux multiplexes the elementary stream of the full frame codec to connected clients: Annex B for H.264 and H.265, OBU for AV1, IVF for VP8 and VP9. Not available on striped H.264 or JPEG. Empty is off. The operator API's own recorder, a fragmented MP4 with the session's audio, needs no socket, see the upstream [Operator API](https://docs.selkies.io/usage#operator-api) |

### Audio

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_AUDIO_BITRATE` | `128000` | Opus bitrate in bps. The UI offers `32000` through `510000` in steps, any value from `6000` to `510000` is accepted |
| `SELKIES_AUDIO_FRAME_DURATION_MS` | `10` | Opus frame duration: `2.5`, `5`, `10`, `20`, `40`, or `60`. Lower cuts audio latency at a small bandwidth and packet rate cost |
| `SELKIES_AUDIO_REDUNDANCY` | `true` | Opus RED (RFC 2198) redundancy to cut dropouts under packet loss. On WebSockets it only engages when every connected client supports it |
| `SELKIES_AUDIO_REDUNDANCY_DISTANCE` | `2` | Number of prior Opus frames carried as redundancy, `0` to `4`. Higher survives longer loss bursts at proportionally more bandwidth |
| `SELKIES_AUDIO_CHANNELS` | `2` | Number of audio channels. `6` or `8` creates a surround sink, which a WebSockets page plays as is and a WebRTC page receives where its browser decodes multichannel Opus, folded to stereo otherwise |
| `SELKIES_AUDIO_DEVICE_NAME` | `output.monitor` | PulseAudio source pcmflux captures |

### Display and input

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_MANUAL_RESOLUTION` | `false` | Lock the resolution to the manual width and height |
| `SELKIES_MANUAL_WIDTH` | `0` | Fixed width up to `16384`, a positive value forces manual resolution mode |
| `SELKIES_MANUAL_HEIGHT` | `0` | Fixed height up to `16384`, a positive value forces manual resolution mode |
| `SELKIES_ENABLE_RESIZE` | `true` | Dynamically resize the display to match the browser window |
| `SELKIES_SCALING_DPI` | `96` | Default DPI for UI scaling, `96` to `288` in steps of `24`. Set explicitly it pins the desktop's DPI against the pages' own picks |
| `SELKIES_FORCE_ALIGNED_RESOLUTION` | `false` | Forces the display resolution to be a multiple of 16 pixels |
| `SELKIES_USE_CSS_SCALING` | `false` | HiDPI when false. When true a lower resolution is sent and the canvas is stretched; the UI scaling pick then divides that resolution and the desktop stays at 96 DPI |
| `SELKIES_SECOND_SCREEN` | `true` | Offer the Add Screen button for a second monitor. Set `false` to hide it. On X11 each display is a RandR output of its own, since the containers' Xvfb starts with spare outputs. On Wayland the button only appears when Selkies detects compositor support (labwc or KWin) regardless of this value |
| `SELKIES_ENABLE_CURSORS` | `true` | Send the remote application cursor to the client |
| `SELKIES_USE_BROWSER_CURSORS` | `true` | Use browser CSS cursors instead of rendering the cursor onto the canvas |
| `SELKIES_CURSOR_SIZE` (or `XCURSOR_SIZE`) | `-1` | Cursor size in points at 96 DPI, scaled with the session DPI. `-1` is the platform default, 32 on X11 and 24 on Wayland. An application's own cursor is delivered whole up to 128 points, the most a browser shows, and a larger size set here raises that cap with it |
| `SELKIES_MAC_CMD_AS_CTRL` | `true` | macOS clients send Command chords as Control, so Cmd+C copies remotely. Set `false` when the session's window manager binds Super itself, Command then arrives as Super. Users may override unless locked |
| `SELKIES_KEYBOARD_SHORTCUTS` | `true` | Keep the client's own chords (Ctrl+Shift with F, M, X, or G, and Ctrl+Shift+click) for the sidebar instead of passing them to the session. Set `false` to pass them through; the sidebar buttons still work and three presses of Escape still leave gaming mode. Users may override unless locked |
| `SELKIES_PUBLISH_INPUT_DEVICES` | `false` | Mirror the session keyboard and pointer onto evdev input devices for applications that enumerate evdev directly, such as fullscreen games and remappers. Uses a kernel uinput device where `/dev/uinput` is writable, else the input interposer |
| `SELKIES_RAW_POINTER_MOTION` | `true` | Ask the browser for unaccelerated pointer movement under pointer lock (gaming mode). Windows and macOS honor it, Linux and Android do not. Clients on macOS leave it off unless chosen. Users may override unless locked |
| `SELKIES_DEBUG_CURSORS` | `false` | Cursor debug logging |

### Feature toggles and session start state

The `*_ENABLED` variables decide what the server offers at all. The `*_ON_START` variables decide whether a feature is already running when a client connects, or waits for the user to press its sidebar button. Whatever starts off is not captured at all until it is turned on.

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_AUDIO_ENABLED` | `true` | Server to client audio streaming. Disabling it also disables the microphone |
| `SELKIES_MICROPHONE_ENABLED` | `false` | Client to server microphone forwarding |
| `SELKIES_WEBCAM_ENABLED` | `true` (upstream `false`) | Client to server webcam forwarding into the virtual V4L2 device. Set by the baseimage unless `NO_WEBCAM` is present |
| `SELKIES_GAMEPAD_ENABLED` | `true` | Gamepad support. Locked off by `NO_GAMEPAD` |
| `SELKIES_VIDEO_ON_START` | `true` | Start with video on. Off, nothing is captured for the primary display until the user turns video on; shared viewers and second screens always start their stream |
| `SELKIES_AUDIO_ON_START` | `true` | Start with audio on. Off, capture stays stopped until the user turns audio on. Unlike `SELKIES_AUDIO_ENABLED=false` nothing is torn down and the microphone keeps working |
| `SELKIES_MICROPHONE_ON_START` | `false` | Microphone policy: `true` asks the browser for the device as soon as the session connects, `false` waits for the sidebar toggle, `demand` asks only while an application in the session records from the virtual source and releases it ten seconds after the last one stops. Under `demand` any process on the desktop can raise a permission prompt, so every ask and release is logged and audited |
| `SELKIES_WEBCAM_ON_START` | `false` | Webcam policy: `true` asks the browser for the camera as soon as the session connects, `false` waits for the sidebar toggle, `demand` asks only while an application holds the virtual device open and releases it two seconds after the last one closes it. Under `demand` the device exists before any uplink, so a pixel format of `auto` resolves to I420 |
| `SELKIES_GAMEPAD_ON_START` | `true` | Start with gamepad input on. The user's choice is remembered by the browser and takes precedence on later visits |
| `SELKIES_COMMAND_ENABLED` | `true` (upstream `false`) | Parsing of command messages from the client, which the sidebar apps section needs. `HARDEN_DESKTOP` turns it off |
| `SELKIES_DEBUG` | `false` | Debug logging |

### Clipboard, files, and apps

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_ENABLE_CLIPBOARD` | `true` | Clipboard policy: `true` both directions, `in` client to server only, `out` server to client only, `false` disabled. `out` is what stops the page reading the local clipboard at all, which is the read Firefox and Safari raise a paste prompt for |
| `SELKIES_ENABLE_BINARY_CLIPBOARD` | `true` | Allow binary data such as images on the clipboard. Rich text pasted from the browser into the session follows the same switch |
| `SELKIES_CLIPBOARD_SEAMLESS` | `true` | Sync the clipboard automatically on every copy on either side. Set `false` and the clipboard only moves through the sidebar's clipboard box. The direction policy above still bounds it. Users may override unless locked |
| `SELKIES_FILE_TRANSFERS` | `upload,download` | Allowed transfer directions, comma separated. Empty or `none` disables. A view only viewer is refused both regardless |
| `SELKIES_FILE_TRANSFER_LIMIT_MBPS` | `0` | Static throttle in Mbit/s shared by all uploads and downloads, for links whose rate you know. `0` disables. Transfers are already paced to protect the video stream without it |
| `SELKIES_FILE_MANAGER_PATH` (or `FILE_MANAGER_PATH`) | `~/Desktop` | Directory uploads land in and the file browser serves, created at startup if missing |
| `SELKIES_APPS_REPO_FOLDER` (or `PA_REPO_FOLDER`) | `''` | Directory of a proot-apps local repository, the folder `proot-apps localrepo` fills, mounted into the session read only. The apps panel then lists that folder's catalog instead of the remote one and installs from it. Set `PA_REPO_FOLDER` on the container so `proot-apps` in a terminal reads the same folder, see [Installing Applications](installing-apps.md) |

A copy a password manager marks as sensitive is kept out of the sidebar's clipboard view and off the local clipboard, and formatted content travels with its plain text so a terminal paste gets text rather than markup.

### Webcam

The containers create a virtual `/dev/video0` and preload a V4L2 interposer so ordinary applications see the browser's camera as a normal webcam. Set `NO_WEBCAM` to skip all of it.

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_WEBCAM_WIDTH` | `1280` | Width of the virtual webcam device, client frames are scaled and letterboxed to fit |
| `SELKIES_WEBCAM_HEIGHT` | `720` | Height of the virtual webcam device |
| `SELKIES_WEBCAM_PIXEL_FORMAT` | `auto` | Pixel format of the virtual device. `auto` follows the uplink (MJPEG for a browser sending JPEG, otherwise I420). Or pin `I420`, `NV12`, `YUYV`, or `MJPEG` |
| `SELKIES_WEBCAM_ENCODER` | `auto` | Codec the browser uses for the camera uplink: `auto`, `h264`, `h265`, `vp8`, `vp9`, `av1`, or `mjpeg`. Over WebSockets `auto` tries H.264, then VP8, then VP9, AV1, or H.265 where the browser encodes them, and JPEG where nothing keeps up; Firefox sends JPEG. A codec name pins it, still dropping to JPEG when it cannot keep up. Over WebRTC the browser sends the named codec when the session negotiated it. Users may override unless locked |
| `SELKIES_WEBCAM_DEVICE` | `auto` | Also mirror the webcam into a v4l2loopback kernel device: `auto` uses the first one found (usually only on a host or privileged container), a path such as `/dev/video10` uses that device, `false` never does |
| `SELKIES_WEBCAM_SOCKET_PATH` | `''` | Directory for the V4L2 interposer socket, `selkies_webcam0.sock`. Empty uses `XDG_RUNTIME_DIR`, which the containers set to `/config/.XDG` |

### Gamepads

Inside the containers the interposer serves four slots as `js0` to `js3` and `event1000` to `event1003`. A game's rumble is mixed per slot and played on the controller of the browser driving it; each browser can turn that off in its gamepad section.

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_JS_SOCKET_PATH` | `''` | Directory for the input interposer sockets, `selkies_js{0-3}.sock` and `selkies_event{1000-1003}.sock`. Empty uses `XDG_RUNTIME_DIR`, which the containers set to `/config/.XDG`, and the interposer looks in the same place |
| `SELKIES_UINPUT_GAMEPAD` | `auto` | Register gamepads as kernel devices through `/dev/uinput`, which Steam, Proton, and browsers inside the session find without the interposer. `auto` only does so where the interposer is not configured and `/dev/uinput` is writable, `true` always attempts it, `false` never does |
| `SELKIES_UINPUT_MOUSE_SOCKET` | `''` | Path to a uinput mouse socket, if not provided uinput is used directly |

### Printing and audit

The session has a printer named `Selkies`. Selkies runs the CUPS queue itself as the session user, the containers ship `cups-daemon` and `cups-filters` and point `CUPS_SERVER` at it, and every printed document is turned into a PDF and handed to the browser, which opens its own print dialog. Documents also collect in the sidebar's printing section for reprinting or saving. The queue prints on A4 unless `PAPERSIZE` names another size such as `letter`.

Selkies can also post an audit event for each clipboard transfer, file transfer, print, connect, disconnect, recording, and `demand` camera or microphone request, plus an `audit.dropped` count once an overflowed queue drains.

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_PRINTING_ENABLED` | `true` | Offer the `Selkies` printer to the session and hand each document to the browser. `false` runs no queue and hides the printing section. `HARDEN_DESKTOP` turns it off unless you set it yourself. Documents go to the page holding the session, shared viewers receive none |
| `SELKIES_PRINT_SPOOL_PATH` | `''` | Directory finished print jobs land in as PDFs until a page takes them. Empty uses `selkies/print` under `XDG_STATE_HOME`, `/config/.local/state/selkies/print` in the containers |
| `SELKIES_AUDIT_WEBHOOK_URL` | `''` | URL that receives one JSON POST per audit event. Metadata only, never content. Empty is off, and a queue of 1024 pending events drops on overflow with no retry |
| `SELKIES_AUDIT_WEBHOOK_TOKEN` | `''` | Bearer token sent in the `Authorization` header of every audit POST |
| `SELKIES_AUDIT_WEBHOOK_TIMEOUT` | `2.0` | Seconds one audit POST may take before it counts as failed and the next one is sent |

### Sharing

Without a master token the sharing section hands out view only and player links, and a second page opened on the session's own address joins as a controller beside the first rather than taking it over. With a master token the session is in secure mode: every page presents a provisioned token that carries its role, and the fragments are ignored. See [Security](security.md#sharing-links).

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_ENABLE_SHARING` | `true` | Master toggle for all sharing features. Off, one page holds the session and a second one takes it over instead of joining |
| `SELKIES_ENABLE_COLLAB` | `true` | Let a viewer holding the session's master key token act as a read write collaborator. Secure mode only, this is not a sharing link of its own |
| `SELKIES_ENABLE_SHARED` | `true` | View only sharing links |
| `SELKIES_ENABLE_PLAYER2` | `true` | Sharing link for gamepad player 2. Locked off by `NO_GAMEPAD` |
| `SELKIES_ENABLE_PLAYER3` | `true` | Sharing link for gamepad player 3. Locked off by `NO_GAMEPAD` |
| `SELKIES_ENABLE_PLAYER4` | `true` | Sharing link for gamepad player 4. Locked off by `NO_GAMEPAD` |
| `SELKIES_MASTER_TOKEN` | `''` | Master token that enables secure mode and authorizes the token control plane (`POST /api/tokens`), used by [SealSkin](../components/sealskin.md) |
| `SELKIES_TOKENS_FILE` | `''` | JSON file holding the session token table in the body format of `POST /api/tokens`, provisioned at start and again whenever it changes, so a restart needs no POST. Root or the server's user must own it and no one else may write to it |
| `SELKIES_BASIC_AUTH_VIEWONLY_PASSWORD` (or `VIEWONLY_PASSWORD`) | `''` | Optional second basic auth password that grants view only access when the Selkies server's own basic auth is on. Ignored in secure mode |

### Client UI visibility

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_UI_TITLE` | `Selkies` | Title in the top left corner of the sidebar, and of the browser tab when set |
| `SELKIES_UI_SHOW_LOGO` | `true` | Show the Selkies logo in the sidebar |
| `SELKIES_UI_SHOW_SIDEBAR` | `true` | Show the main sidebar UI |
| `SELKIES_UI_SHOW_CORE_BUTTONS` | `true` | Show the display, audio, microphone, webcam, and gamepad core buttons |
| `SELKIES_UI_SHOW_CONNECTION_INDICATOR` | `true` | Show the poor connection mark over the stream while the server finds the client's connection losing frames, with or without the sidebar |
| `SELKIES_UI_SIDEBAR_SHOW_VIDEO_SETTINGS` | `true` | Video settings section |
| `SELKIES_UI_SIDEBAR_SHOW_SCREEN_SETTINGS` | `true` | Screen settings section |
| `SELKIES_UI_SIDEBAR_SHOW_AUDIO_SETTINGS` | `true` | Audio settings section |
| `SELKIES_UI_SIDEBAR_SHOW_STATS` | `true` | Stats section |
| `SELKIES_UI_SIDEBAR_SHOW_SHORTCUTS` | `true` | Keyboard shortcuts section |
| `SELKIES_UI_SIDEBAR_SHOW_CLIPBOARD` | `true` | Clipboard section |
| `SELKIES_UI_SIDEBAR_SHOW_FILES` | `true` | File transfer section. `HARDEN_DESKTOP` hides it |
| `SELKIES_UI_SIDEBAR_SHOW_APPS` | `true` | Applications section. `HARDEN_DESKTOP` hides it, and the session hides it on its own where the host denies `ptrace`, which proot needs |
| `SELKIES_UI_SIDEBAR_SHOW_SHARING` | `true` | Sharing section |
| `SELKIES_UI_SIDEBAR_SHOW_GAMEPADS` | `true` | Gamepads section. `NO_GAMEPAD` hides it |
| `SELKIES_UI_SIDEBAR_SHOW_WEBCAM` | `true` | Webcam toggle among the core buttons. Hides the control only, `SELKIES_WEBCAM_ENABLED` governs whether the server accepts frames |
| `SELKIES_UI_SIDEBAR_SHOW_FULLSCREEN` | `true` | Fullscreen button |
| `SELKIES_UI_SIDEBAR_SHOW_GAMING_MODE` | `true` | Gaming mode button |
| `SELKIES_UI_SIDEBAR_SHOW_TRACKPAD` | `true` | Virtual trackpad button |
| `SELKIES_UI_SIDEBAR_SHOW_KEYBOARD_BUTTON` | `true` | On screen keyboard button in the display area |
| `SELKIES_UI_SIDEBAR_SHOW_SOFT_BUTTONS` | `true` | Soft buttons section |

### Server and diagnostics

The container's built in Nginx owns the listening ports, TLS, basic auth, and the `SUBFOLDER` prefix, and the init scripts hand the matching values to Selkies. Use the container variables (`CUSTOM_PORT`, `CUSTOM_HTTPS_PORT`, `CUSTOM_WS_PORT`, `CUSTOM_USER`, `PASSWORD`, `SUBFOLDER`) rather than the Selkies server's own listener (`SELKIES_ADDR`, `SELKIES_PORT`, `SELKIES_UNIX_SOCKET`), HTTPS, and basic auth settings, which exist for running the `selkies` binary outside these containers.

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_ALLOWED_ORIGINS` | `*` (upstream same origin) | Comma separated browser Origins allowed to open the streaming WebSocket, a cross site WebSocket hijacking guard. Relaxed in the containers because Nginx fronts the server |
| `SELKIES_FRAME_ANCESTORS` | `'self'` | Comma separated pages allowed to show the client in a frame, sent as the Content-Security-Policy `frame-ancestors` directive. `'self'` admits the container's own origin only, an origin such as `https://portal.example.com` admits a portal embedding the desktop from elsewhere, `*` any page, `'none'` no frame at all. A page the list does not name gets an empty frame |
| `SELKIES_SUBFOLDER` (or `SUBFOLDER`) | `''` | URL path prefix the server is proxied under, prepended to every route. The container's Nginx reads the same `SUBFOLDER`, so set that one |
| `SELKIES_PUBLIC` | `false` | Listen on every interface instead of loopback. Leave it alone in the containers, Nginx is the public face and the server refuses to start when both this and `SELKIES_ADDR` are set |
| `SELKIES_ENABLE_METRICS_HTTP` | `false` | Prometheus metrics endpoint at `/api/metrics` on the Selkies server, behind the session's login |
| `SELKIES_ENABLE_WEBRTC_STATISTICS` | `false` | Dump WebRTC statistics CSVs from the client |
| `SELKIES_WEBRTC_STATISTICS_DIR` | `/tmp` | Directory for those CSVs, `selkies-stats-video-[timestamp].csv` and `selkies-stats-audio-[timestamp].csv` |

### Display backend

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_WAYLAND` (or `PIXELFLUX_WAYLAND`) | `false` | Run the Wayland headless compositor backend instead of X11 capture and input. Each container image bakes in `PIXELFLUX_WAYLAND` for the stack its application or desktop runs on |
| `SELKIES_APP_WAYLAND_DISPLAY` | `''` | Wayland socket applications run on when it differs from the capture compositor, for a nested session. Empty auto detects |
| `SELKIES_WAYLAND_HOST_DISPLAY` | `''` | Socket of an external compositor (labwc started headless, for example) that pixelflux captures and injects into as a client instead of compositing itself. Empty keeps the built in compositor |
| `SELKIES_WAYLAND_SOCKET_INDEX` | `0` | Index for the Wayland command socket, `0` is `wayland-0` |
| `SELKIES_COMPUTER_USE_BIND` | `''` | Start pixelflux's Computer Use HTTP server on comma separated entries, a bare port listens on loopback only, which every account in the container can reach, `host:port` names the address. A caller drives the desktop with the session user's full authority, so the server needs `SELKIES_COMPUTER_USE_TOKEN` and does not start without it. `PIXELFLUX_CU` remains the standalone fallback |
| `SELKIES_COMPUTER_USE_TOKEN` (or `PIXELFLUX_CU_TOKEN`) | `''` | Bearer token every Computer Use request has to carry as `Authorization: Bearer <token>`. Never sent to clients |

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
| `SELKIES_WATERMARK_PATH` (or `WATERMARK_PNG`) | `''` | Absolute path to a watermark PNG. On the X11 DRI3 path the X server composites it, so it costs no readback |
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
