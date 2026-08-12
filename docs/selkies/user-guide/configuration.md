# Configuration Reference

Every Selkies based container is configured through environment variables. This page collects all of them in one place. They fall into three groups:

1. **Container variables**: standard LinuxServer.io conventions plus Selkies baseimage options (ports, auth, GPU, language).
2. **Selkies application settings** (`SELKIES_*`): stream, client UI, and feature toggles, with a locking syntax.
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
| `CUSTOM_WS_PORT` | Internal WebSocket port, default `8082` |
| `CUSTOM_USER` | HTTP basic auth username, default `abc` |
| `PASSWORD` | HTTP basic auth password, default `abc`. If unset there is no auth |
| `DRI_NODE` | Encoding GPU, enables VAAPI/NVENC stream encoding on the given device, e.g. `/dev/dri/renderD128` |
| `DRINODE` | Rendering GPU for EGL and 3D acceleration, e.g. `/dev/dri/renderD128` |
| `AUTO_GPU` | Automatic GPU configuration when one is detected, first available GPU used for encoding and rendering. Set `false` to disable |
| `PIXELFLUX_CU` | Port to enable the Computer Use API server for AI agent control of the desktop, Wayland mode only |
| `SUBFOLDER` | Subfolder when running behind a subfolder reverse proxy, needs both slashes, e.g. `/subfolder/` |
| `TITLE` | Page title shown in the browser, default `Selkies` |
| `DASHBOARD` | Select the web client dashboard: `selkies-dashboard`, `selkies-dashboard-zinc`, or `selkies-dashboard-wish` |
| `FILE_MANAGER_PATH` | Change the default upload and download path, must be writable by the `abc` user |
| `START_DOCKER` | If `false`, a privileged container will not automatically start the Docker in Docker setup |
| `DISABLE_IPV6` | Set to `true` or any value to disable IPv6 |
| `LC_ALL` | Session language, e.g. `fr_FR.UTF-8`, see [Internationalization](#internationalization) |
| `NO_DECOR` | Run the application without window borders, for PWA style use. Toggle at runtime with `ctrl+shift+d` |
| `NO_FULL` | Do not automatically fullscreen applications when using the single app window manager |
| `NO_GAMEPAD` | Disable the userspace gamepad interposer injection |
| `DISABLE_ZINK` | Do not set Zink variables when a GPU is detected, applications use CPU rendering |
| `DISABLE_DRI3` | X11 mode only, disable DRI3 acceleration |
| `MAX_RES` | Maximum virtual display resolution, default 16K (`15360x8640`) |
| `WATERMARK_PNG` | Full path inside the container to a watermark PNG, e.g. `/usr/share/selkies/www/icon.png` |
| `WATERMARK_LOCATION` | Where to paint the watermark, integer 1 to 6 |

**`WATERMARK_LOCATION` values:** `1` top left, `2` top right, `3` bottom left, `4` bottom right, `5` centered, `6` animated.

## Selkies application settings

Every facet of the streaming application can be configured with `SELKIES_*` variables. These also drive what the user can change in the sidebar UI.

### Value syntax

- **Booleans and locking.** Booleans accept `true` or `false`. Append `|locked` to prevent the user changing the setting in the UI: `-e SELKIES_USE_CPU="true|locked"`
- **Enums and lists.** Comma separated values, the first item is the default. A single item hides the UI dropdown entirely: `-e SELKIES_ENCODER="jpeg"`
- **Ranges.** `min-max` renders a slider, a single number locks the value: `-e SELKIES_FRAMERATE="60"`
- **Manual resolution.** Setting `SELKIES_MANUAL_WIDTH` or `SELKIES_MANUAL_HEIGHT` locks the resolution to those values.

### Stream settings

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_ENCODER` | `'x264enc,x264enc-striped,jpeg'` | Available video encoders, first is default |
| `SELKIES_FRAMERATE` | `'8-120'` | Framerate range or fixed value |
| `SELKIES_H264_CRF` | `'5-50'` | H.264 CRF range or fixed value, lower is higher quality |
| `SELKIES_JPEG_QUALITY` | `'1-100'` | JPEG quality range or fixed value |
| `SELKIES_H264_FULLCOLOR` | `False` | H.264 full color 4:4:4 range for pixelflux encoders |
| `SELKIES_H264_STREAMING_MODE` | `False` | H.264 streaming mode for pixelflux encoders |
| `SELKIES_FORCE_ALIGNED_RESOLUTION` | `False` | Forces the display resolution to be a multiple of 16 pixels. |
| `SELKIES_USE_CPU` | `False` | Force CPU encoding |
| `SELKIES_USE_PAINT_OVER_QUALITY` | `True` | High quality paint over for static scenes |
| `SELKIES_PAINT_OVER_JPEG_QUALITY` | `'1-100'` | JPEG paint over quality range or fixed value |
| `SELKIES_H264_PAINTOVER_CRF` | `'5-50'` | H.264 paint over CRF range or fixed value |
| `SELKIES_H264_PAINTOVER_BURST_FRAMES` | `'1-30'` | H.264 paint over burst frames range or fixed value |
| `SELKIES_SECOND_SCREEN` | `True` | Support for a second monitor |
| `SELKIES_AUDIO_BITRATE` | `'320000'` | Default audio bitrate |
| `SELKIES_IS_MANUAL_RESOLUTION_MODE` | `False` | Lock resolution to the manual width and height |
| `SELKIES_MANUAL_WIDTH` | `0` | Fixed width, setting this forces manual resolution mode |
| `SELKIES_MANUAL_HEIGHT` | `0` | Fixed height, setting this forces manual resolution mode |
| `SELKIES_SCALING_DPI` | `'96'` | Default DPI for UI scaling |
| `SELKIES_USE_BROWSER_CURSORS` | `False` | Use browser CSS cursors instead of canvas rendering |
| `SELKIES_USE_CSS_SCALING` | `False` | HiDPI when false. When true a lower resolution is sent and the canvas is stretched |

### Feature toggles

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_AUDIO_ENABLED` | `True` | Server to client audio streaming |
| `SELKIES_MICROPHONE_ENABLED` | `True` | Client to server microphone forwarding |
| `SELKIES_GAMEPAD_ENABLED` | `True` | Gamepad support |
| `SELKIES_CLIPBOARD_ENABLED` | `True` | Clipboard synchronization |
| `SELKIES_ENABLE_BINARY_CLIPBOARD` | `False` | Allow binary data on the clipboard |
| `SELKIES_COMMAND_ENABLED` | `True` | Parsing of command websocket messages |
| `SELKIES_FILE_TRANSFERS` | `'upload,download'` | Allowed transfer directions, comma separated. Empty or `none` disables |
| `SELKIES_DEBUG` | `False` | Debug logging |

### Sharing toggles

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_ENABLE_SHARING` | `True` | Master toggle for all sharing features |
| `SELKIES_ENABLE_COLLAB` | `True` | Collaborative read write sharing link |
| `SELKIES_ENABLE_SHARED` | `True` | View only sharing links |
| `SELKIES_ENABLE_PLAYER2` | `True` | Sharing link for gamepad player 2 |
| `SELKIES_ENABLE_PLAYER3` | `True` | Sharing link for gamepad player 3 |
| `SELKIES_ENABLE_PLAYER4` | `True` | Sharing link for gamepad player 4 |

### Client UI visibility

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_UI_TITLE` | `'Selkies'` | Title in the top left corner of the sidebar |
| `SELKIES_UI_SHOW_LOGO` | `True` | Show the Selkies logo in the sidebar |
| `SELKIES_UI_SHOW_SIDEBAR` | `True` | Show the main sidebar UI |
| `SELKIES_UI_SHOW_CORE_BUTTONS` | `True` | Show display, audio, microphone, and gamepad core buttons |
| `SELKIES_UI_SIDEBAR_SHOW_VIDEO_SETTINGS` | `True` | Video settings section |
| `SELKIES_UI_SIDEBAR_SHOW_SCREEN_SETTINGS` | `True` | Screen settings section |
| `SELKIES_UI_SIDEBAR_SHOW_AUDIO_SETTINGS` | `True` | Audio settings section |
| `SELKIES_UI_SIDEBAR_SHOW_STATS` | `True` | Stats section |
| `SELKIES_UI_SIDEBAR_SHOW_CLIPBOARD` | `True` | Clipboard section |
| `SELKIES_UI_SIDEBAR_SHOW_FILES` | `True` | File transfer section |
| `SELKIES_UI_SIDEBAR_SHOW_APPS` | `True` | Applications section |
| `SELKIES_UI_SIDEBAR_SHOW_SHARING` | `True` | Sharing section |
| `SELKIES_UI_SIDEBAR_SHOW_GAMEPADS` | `True` | Gamepads section |
| `SELKIES_UI_SIDEBAR_SHOW_FULLSCREEN` | `True` | Fullscreen button |
| `SELKIES_UI_SIDEBAR_SHOW_GAMING_MODE` | `True` | Gaming mode button |
| `SELKIES_UI_SIDEBAR_SHOW_TRACKPAD` | `True` | Virtual trackpad button |
| `SELKIES_UI_SIDEBAR_SHOW_KEYBOARD_BUTTON` | `True` | On screen keyboard button in the display area |
| `SELKIES_UI_SIDEBAR_SHOW_SOFT_BUTTONS` | `True` | Soft buttons section |

### Plumbing

| Variable | Default | Description |
| --- | --- | --- |
| `SELKIES_PORT` (or `CUSTOM_WS_PORT`) | `8082` | Data WebSocket server port |
| `SELKIES_DRI_NODE` (or `DRI_NODE`) | `''` | DRI render node for VA-API |
| `SELKIES_AUDIO_DEVICE_NAME` | `'output.monitor'` | Audio device for pcmflux capture |
| `SELKIES_WATERMARK_PATH` (or `WATERMARK_PNG`) | `''` | Absolute path to watermark PNG |
| `SELKIES_WATERMARK_LOCATION` (or `WATERMARK_LOCATION`) | `-1` | Watermark location enum 0 to 6 |

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
