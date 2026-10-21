# Using the Web Client

The web client is a complete workstation interface, not just a video player. This page tours everything it can do. Nearly all of it can be hidden or locked by the administrator with the `SELKIES_UI_*` variables in the [Configuration Reference](configuration.md).

## The sidebar

Toggle the sidebar with its handle on screen. At the top you get the core toggles: display, audio, microphone, webcam, and gamepad on or off, plus buttons for fullscreen, virtual trackpad, gaming mode, and the on screen keyboard.

## Video settings

- **Encoder**: H.264, H.265, VP8, VP9, AV1, or JPEG. Each video codec is encoded on the GPU when the card has an engine for it and in software otherwise, so the menu only lists what this host can serve. H.264 is the default and right for everything modern, with FullColor 4:4:4 plus paint over it is visually equal to lossless stills. Entries your browser cannot decode are greyed out as `(Unsupported Browser)`, H.265 outside Safari being the usual one, and a browser that cannot play the default steps down to the next codec it decodes. JPEG exists for browsers that cannot decode video frames at all. See the [Video encoders](configuration.md#video-encoders) table for what each codec needs.
- **Frames per second** and **CRF** (quality, lower is better) sliders, plus separate paint over quality controls. The frame rate slider also offers your own display's refresh rate. "Paint over" is the platform's signature feature: after the screen goes still, it is repainted at high quality so text stays crisp. The CRF slider means the same quality on every codec.
- **FullColor 4:4:4**: true 8 bit color with no chroma subsampling. Fixes blurry colored text. Offered on H.264, H.265, and VP9 only, and only where your browser decodes that codec's 4:4:4 profile. Note the [GPU caveats](gpu.md#fullcolor-444-and-hardware-encoders).
- **10-bit**: 10 bits per sample where the codec, the encoder, and your decoder all carry it. The desktop is an 8 bit source, so it adds precision to the color conversion rather than new shades, costs CPU on a software encoder, and is only worth pairing with FullColor.
- **Turbo mode** (streaming mode): disables all the damage tracking logic and encodes every frame like a traditional video stream. Can be useful for gaming and full motion video.
- **CPU encoding** toggle to force software encoding. It only appears when the current codec is available both on the GPU and in software on this host. While the session encodes in software a **multithreading** switch appears beside it, which an administrator turns off on hosts that pack many sessions onto their cores.
- **Rate control**: CRF (constant quality, the default in the containers on both transports) or CBR with a bitrate slider. Under CBR, congestion control steers the bitrate to what your link carries, and the paint over switch disappears because a still screen is cleaned up regardless.
- **Transport**: when the administrator has enabled WebRTC, a switch lets you move between WebSockets and WebRTC at runtime, see [WebRTC Transport](webrtc.md).

!!! tip "On a slow machine or a slow link, turn the stream down"
    The defaults favor fluidity. If your client device is low end or your bandwidth is poor, reduce **Frames per second** first and raise **CRF** if needed (higher CRF means smaller frames). Paint over still keeps static content sharp, so a lower FPS and quality setting costs far less than you would expect for desktop work.

## Screen settings

- **Resolution**: by default the remote resolution follows your browser window exactly. You can instead pick a preset (720p through 4K) or type a manual width and height.
- **UI scaling (DPI)** for HiDPI displays, with a choice between pixel perfect HiDPI rendering and CSS scaling (lighter on bandwidth, softer image).
- **Scale locally** stretches a fixed remote resolution to fit your window.
- **Add Screen +**: opens a second browser window that becomes a second monitor for the session, positioned left, right, above, or below the primary. Arrange each window on the matching physical monitor and you have a real dual screen remote desktop. Always available on X11, where the extra display is plugged in as a monitor of its own. On Wayland, Selkies detects at startup whether the running compositor supports it, which today means labwc (the single app containers and the default Webtop shell) and KWin (the KDE Webtops), and only offers the button when it does.

## Audio and microphone

Opus audio streams from the session to your browser, and output device selection if your browser exposes multiple sinks. The microphone button forwards your local mic into the session, where apps see it as a normal input device, video calls from inside a remote browser container work.

## Webcam

The webcam button forwards your local camera into the session as a virtual V4L2 device, so video conferencing inside a remote browser or any camera aware application works. The administrator can size the virtual device, have the browser ask for the camera only while an application in the session actually opens it (`SELKIES_WEBCAM_ON_START=demand`), and disable the feature entirely with `NO_WEBCAM`.

## Clipboard

Bidirectional clipboard sync between your machine and the session, automatic in both directions for text. Formatted content keeps its formatting, and travels with its plain text so a terminal paste gets text rather than markup. The sidebar shows an editable view of the server clipboard, an **Upload Image** button that puts a picture file on the session's clipboard, and three switches: send to session, receive from session, and **Seamless**, which is what makes every copy follow automatically. Off, content only moves through the clipboard box when you ask. **Image support** (binary clipboard, `SELKIES_ENABLE_BINARY_CLIPBOARD`) adds images and other binary formats, and rich text from the browser follows the same switch. A copy a password manager marks as sensitive stays out of the sidebar view and off your local clipboard. Clipboard direction and availability can be locked down by the admin with the `SELKIES_ENABLE_CLIPBOARD` policy.

## Files

- **Upload**: drag and drop files anywhere on the session window, or use the Upload button. Files land in the session's `~/Desktop` by default (configurable with `FILE_MANAGER_PATH`).
- **Download**: the Files section opens a file browser of the same directory, click to download.

Transfers can be restricted per direction or disabled entirely with `SELKIES_FILE_TRANSFERS`.

## Gamepads

Plug and play controller support for PlayStation, Xbox, and Switch pads, with mappings derived from the SDL game controller database. Inside the session, apps see a standard Xbox 360 style device provided by a userspace interposer, no kernel modules or privileged devices involved; where `/dev/uinput` is writable, on a privileged container for example, Selkies registers real kernel devices instead. Up to four controllers are supported, and the sharing feature can hand player 2 through 4 slots to remote friends. A game's rumble plays back on your controller through the browser, with a **Rumble** toggle in the gamepad section to turn it off. A configurable **touch gamepad** overlay provides on screen controls for phones and tablets, and vibrates on phones that allow it.

## Sharing and collaboration

The Sharing section generates links for other people to join your running session:

| Link | Capability |
| --- | --- |
| View only | Watch the session, no input |
| Player 2, 3, 4 | Gamepad input only, for couch co-op over the internet |

A second page opened on the session's own address, another tab or another browser, joins as a controller beside the first rather than taking it over: both stream and both drive input, and a stream setting picked in either applies to both. Each link is the page's own address with a fragment, so whatever guards the page guards the link. Anyone with the plain address has full control, treat it like a credential. Admins can disable any of this, see [Security](security.md#sharing-links).

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

- **Trackpad mode**: the screen becomes a laptop style trackpad with relative cursor movement, tap to click, tap and hold to drag, two finger scrolling, two finger tap to right click, and three finger tap to middle click. The pointer accelerates with the finger's speed, with a speed picker beside the touch controls. Ideal for desktop apps on a phone.
- **Direct touch mode**: taps map straight to absolute clicks, a long press right clicks, and a pinch reaches the session as Ctrl+wheel, best for touch friendly apps.
- The **on screen keyboard** button raises your device keyboard, with IME input (for example Chinese Pinyin) supported end to end. Soft modifier keys sit beside it, and **More keys** opens a palette of what a phone keyboard lacks: function keys, arrows, Home and End, and chords such as Alt+Tab or Ctrl+Alt+Del, plus any chord you type into it.

## macOS keyboards

Command chords are sent as Control by default, so Cmd+C and Cmd+V work as they do locally. If the session's window manager binds Super (a Cmd+Return terminal shortcut, for example), turn it off in the sidebar or with `SELKIES_MAC_CMD_AS_CTRL=false` and Command arrives as Super.

## Printing

Every session has a printer named **Selkies**. Print to it from any application and the document arrives in your browser as a PDF, where the browser's own print dialog offers whatever printers your local machine can reach. The sidebar's printing section lists each document so it can be printed again or saved as a PDF, its **Print automatically** switch is what opens the dialog on arrival. On a phone or tablet, where no browser prints a PDF from a frame, each document raises a notice with an **Open** link into a new tab instead. The queue prints on A4 unless the container sets `PAPERSIZE`. Documents go to the page holding the session, shared viewers do not receive them. Administrators turn the feature off with `SELKIES_PRINTING_ENABLED=false`, and `HARDEN_DESKTOP` does so by default.

## Gaming mode

Gaming mode grabs the pointer (pointer lock) and sends relative mouse movement for accurate FPS style aiming, pairs well with Turbo encoding mode and gamepads.

## Stats

Live overlay of client FPS, round trip latency, bandwidth, video bitrate against its target, frame timing from capture to the wire, and the CPU, memory, and GPU utilization of the server's own container. It also names the capture path and the encoder the session runs on, and why a faster path was declined. Independent of the sidebar, a **poor connection** mark appears in the corner of the stream while the server is losing frames on the way to your browser. Your first stop when something feels off, before diving into [Troubleshooting](troubleshooting.md).

## Apps section

A management panel for installing additional applications into the session (backed by the proot-apps ecosystem described in [Installing Applications](installing-apps.md)). Admins commonly hide this in locked down deployments.
