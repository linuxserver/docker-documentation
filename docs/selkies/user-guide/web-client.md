# Using the Web Client

The web client is a complete workstation interface, not just a video player. This page tours everything it can do. Nearly all of it can be hidden or locked by the administrator with the `SELKIES_UI_*` variables in the [Configuration Reference](configuration.md).

## The sidebar

Toggle the sidebar with its handle on screen. At the top you get the core toggles: display, audio, microphone, and gamepad on or off, plus buttons for fullscreen, virtual trackpad, gaming mode, and the on screen keyboard.

## Video settings

- **Encoder**: H.264 (`x264enc`), striped H.264, or JPEG. H.264 is the default and right for everything modern, with FullColor 4:4:4 plus paint over it is visually equal to lossless stills. JPEG exists for unsupported browsers that cannot decode video frames at all.
- **Frames per second** and **CRF** (H.264 quality, lower is better) sliders, plus separate paint over quality controls. "Paint over" is the platform's signature feature: after the screen goes still, it is repainted at high quality so text stays crisp.
- **FullColor 4:4:4**: true 8 bit color with no chroma subsampling. Fixes blurry colored text. Note the [GPU caveats](gpu.md#fullcolor-444-and-hardware-encoders).
- **Turbo mode** (streaming mode): disables all the damage tracking logic and encodes every frame like a traditional video stream. Can be useful for gaming and full motion video.
- **CPU encoding** toggle to force cpu encoding.

!!! tip "On a slow machine or a slow link, turn the stream down"
    The defaults favor fluidity. If your client device is low end or your bandwidth is poor, reduce **Frames per second** first and raise **CRF** if needed (higher CRF means smaller frames). Paint over still keeps static content sharp, so a lower FPS and quality setting costs far less than you would expect for desktop work.

## Screen settings

- **Resolution**: by default the remote resolution follows your browser window exactly. You can instead pick a preset (720p through 4K) or type a manual width and height.
- **UI scaling (DPI)** for HiDPI displays, with a choice between pixel perfect HiDPI rendering and CSS scaling (lighter on bandwidth, softer image).
- **Scale locally** stretches a fixed remote resolution to fit your window.
- **Add Screen +**: opens a second browser window that becomes a second monitor for the session, positioned left, right, above, or below the primary. Arrange each window on the matching physical monitor and you have a real dual screen remote desktop. (Second screen is currently a feature of the X11 stack; in Wayland mode it is disabled.)

## Audio and microphone

Opus audio streams from the session to your browser, and output device selection if your browser exposes multiple sinks. The microphone button forwards your local mic into the session, where apps see it as a normal input device, video calls from inside a remote browser container work.

## Clipboard

Bidirectional clipboard sync between your machine and the session, automatic in both directions for text. The sidebar shows an editable view of the server clipboard. Enabling **Image support** (binary clipboard, `SELKIES_ENABLE_BINARY_CLIPBOARD`) adds images and other binary formats. Clipboard direction and availability can be locked down by the admin.

## Files

- **Upload**: drag and drop files anywhere on the session window, or use the Upload button. Files land in the session's `~/Desktop` by default (configurable with `FILE_MANAGER_PATH`).
- **Download**: the Files section opens a dark themed file index of the same directory served by the container's Nginx, click to download.

Transfers can be restricted per direction or disabled entirely with `SELKIES_FILE_TRANSFERS`.

## Gamepads

Plug and play controller support for PlayStation, Xbox, and Switch pads, with mappings derived from the SDL game controller database. Inside the session, apps see a standard Xbox 360 style device provided by a userspace interposer, no kernel modules or privileged devices involved. Up to four controllers are supported, and the sharing feature can hand player 2 through 4 slots to remote friends. A configurable **touch gamepad** overlay provides on screen controls for phones and tablets.

## Sharing and collaboration

The Sharing section generates links for other people to join your running session:

| Link | Capability |
| --- | --- |
| Collaboration | Full interactive control alongside you |
| View only | Watch the session, no input |
| Player 2, 3, 4 | Gamepad input only, for couch co-op over the internet |

Anyone with a collaboration link has full control, treat these links like credentials. Admins can disable any of them, see [Security](security.md#sharing-links).

!!! warning "The built in sharing links are a demo"
    Out of the box these links carry no real authentication of their own, they are a demonstration of the underlying multi user protocol. For proper shared sessions, the token based access control that [SealSkin](../components/sealskin.md) wires up is the intended path: named participants, revocable access, and per user permissions. Use the raw links only on networks you trust.

## Inside a single app container

Full desktop Webtops behave like any desktop. Single app containers (Firefox, Chromium, and friends) instead run a minimal window manager, labwc on Wayland or Openbox on X11, with no panel or taskbar. Three gestures cover everything you need:

- **Right click the desktop** (any empty area behind or beside the app) to open the root menu, which lets you launch a terminal or other bundled tools.
- **Middle click the desktop** to see and restore minimized windows.
- `ctrl+shift+d` toggles window decorations if you need to move or resize the app window.

If these menus seem missing, the administrator has likely [hardened](security.md) the container, that is a feature, not a bug.

## Mobile and touch

On phones and tablets the client offers:

- **Trackpad mode**: the screen becomes a laptop style trackpad with relative cursor movement, tap to click, tap and hold to drag, and two finger scrolling. Ideal for desktop apps on a phone.
- **Direct touch mode**: taps map straight to absolute clicks, best for touch friendly apps.
- The **on screen keyboard** button raises your device keyboard, with IME input (for example Chinese Pinyin) supported end to end.

## Gaming mode

Gaming mode grabs the pointer (pointer lock) and sends relative mouse movement for accurate FPS style aiming, pairs well with Turbo encoding mode and gamepads.

## Stats

Live overlay of client FPS, round trip latency, bandwidth, video bitrate, CPU, memory, and GPU utilization of the server. Your first stop when something feels off, before diving into [Troubleshooting](troubleshooting.md).

## Apps section

A management panel for installing additional applications into the session (backed by the proot-apps ecosystem described in [Installing Applications](installing-apps.md)). Admins commonly hide this in locked down deployments.
