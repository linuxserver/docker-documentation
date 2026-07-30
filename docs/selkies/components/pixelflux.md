# Pixelflux and Pcmflux

**Repository:** [linuxserver/pixelflux](https://github.com/linuxserver/pixelflux) · **PyPI:** `pip install pixelflux` · **License:** MPL-2.0

Pixelflux is the rendering and capture pipeline at the core of the entire platform. It captures a Linux framebuffer, decides what changed, encodes it as JPEG or H.264, and hands the encoded frames to your code through a Python callback. Selkies is its primary consumer, but it is a standalone library you can embed in anything.

Pcmflux is its audio sibling: it captures PulseAudio output and encodes Opus frames for delivery to the browser, and handles the microphone return path. Both ship as prebuilt wheels for x86_64 and aarch64 on glibc and musl.

## What it actually is

As of the 2.0.0 release, pixelflux is a **Rust** library exposed to Python through PyO3 (earlier versions were C++ with ctypes). One extension module contains:

- An **X11 backend**: XShm screen capture with XFixes cursor tracking, for the legacy X11 stack.
- A **Wayland backend**: a full headless Wayland compositor built on [Smithay](https://github.com/Smithay/smithay), running in process. This is the key architectural point of the modern stack: **pixelflux does not capture a Wayland compositor, it is the compositor.** It synthesizes the output, seat, and clipboard itself, which is why the framebuffer can live directly on a GPU and why input is injected through its API rather than tools like xdotool.
- Four encoders and the damage tracking, paint over, and rate control logic shared between them.

## Encoders

| Encoder | Hardware | Mode | Notes |
| --- | --- | --- | --- |
| JPEG | CPU | Striped | Stateless, per stripe quality. Kept as the compatibility path for browsers that cannot decode video frames; 4:4:4 H.264 with paint over matches it visually everywhere else |
| x264 | CPU | Striped or full frame | Default software H.264, ultrafast zerolatency, 4:4:4 capable |
| OpenH264 | CPU | Full frame only | Opt in alternative software encoder, 4:2:0 only |
| NVENC | Nvidia GPU | Full frame | Direct NVENC via runtime library loading, no CUDA toolkit needed, supports High 4:4:4, zero copy from DMA-BUF |
| VA-API | Intel and AMD GPU | Full frame | Through FFmpeg's `h264_vaapi`, zero copy from DMA-BUF, no 4:4:4 (falls back to CPU) |

### Striped encoding

On the CPU paths the screen is divided into horizontal stripes, one per CPU core (each at least 64 rows). Each stripe has its own encoder instance and its own damage history, and stripes are encoded in parallel across a thread pool. Only stripes that changed are encoded and sent. This is the "hybrid VNC and video codec" idea that lets a CPU only server idle at nearly zero cost and still deliver 60fps where the screen is actually moving.

Hardware encoders always operate full frame, delivered as a single full height stripe, since the GPU encodes the whole surface in one shot anyway.

### Damage detection

- **X11:** each stripe's pixels are hashed (xxh3) every frame, a changed hash marks the stripe dirty. Continuously changing regions enter a "damage block" state that skips re hashing for a configured number of frames to save CPU.
- **Wayland:** no hashing needed, the compositor knows exactly which rectangles clients damaged and maps them to stripes.
- A fully idle screen takes a fast path that skips the encode thread pool entirely.

### Paint over

The signature quality feature. After a region has been static for a configurable number of frames (`paint_over_trigger_frames`), it is re sent at high quality: a higher quality JPEG, or for H.264 a burst of frames at a lower CRF. Motion cancels an in flight burst. The result is video efficiency during motion and pixel perfect text the moment you stop scrolling.

### Rate control

- **CRF/CQP mode** (default): constant quality, bits go wherever needed.
- Infinite GOP by default: keyframes are only sent on demand (client join, recovery, or an optional periodic interval). Bitrate, framerate, and quality are all adjustable live without restarting the capture.

## Zero copy on Wayland

When the compositor renders on a GPU and the encoder is on the same GPU, frames flow as DMA-BUF handles from the render buffer straight into NVENC or VA-API. The pixels never touch system RAM and the CPU never sees them. If the render and encode devices differ, or a software encoder is selected, pixelflux falls back to a readback path automatically and logs which decision it made.

GPU selection is automatic: it walks `/sys/class/drm`, identifies cards by driver (`nvidia` goes to NVENC, `i915` and `amdgpu` to VA-API), and can be pinned by device path, index, or an `auto_gpu` token matching a driver or vendor ID.

## API sketch

```python
from pixelflux import CaptureSettings, ScreenCapture, ensure_wayland_display

settings = CaptureSettings()
settings.capture_width = 1920
settings.capture_height = 1080
settings.target_fps = 60.0
settings.output_mode = 1          # 0 = JPEG, 1 = H.264
settings.video_crf = 25
settings.use_paint_over_quality = True

def on_frame(frame):
    # frame is a StripeFrame: zero copy buffer protocol object
    # frame.data_type: 1 = JPEG, 2 = H.264
    # bytes(frame) or memoryview(frame) for the payload
    ws.send(bytes(frame))

capture = ScreenCapture()
capture.start_capture(on_frame, settings)
```

Each encoded stripe arrives with a compact binary header (6 bytes for JPEG, 10 for H.264 carrying frame type, frame number, stripe offset, and dimensions) that the web client parses to place stripes on the canvas. Headers can be omitted for embedding in your own protocol.

The Wayland backend additionally exposes input injection (keyboard by scancode with a hot swappable XKB keymap, absolute and relative pointer, buttons, scroll), clipboard get and set, cursor callbacks delivering PNG cursor images out of band, and live rate updates. `example/screen_to_browser.py` in the repository is a complete working WebSocket streaming server in one file, with a matching browser client in `example/index.html`.

## Extras worth knowing about

- **Computer Use API**: setting the `PIXELFLUX_CU=<port>` environment variable starts a small HTTP server with a `POST /computer-use` endpoint accepting JSON actions (`screenshot`, `left_click`, `type`, `key`, `scroll`, `zoom`, and friends). This is the raw input and vision layer that [Pelorus](pelorus.md) builds on.
- **Recording sink**: point `recording_socket` (or `PIXELFLUX_RECORDING_SOCKET`) at a Unix socket path and pixelflux serves the raw Annex-B H.264 bitstream to any connected client, forcing a keyframe when someone connects. Requires a full frame H.264 mode.
- **Watermarking**: composite a PNG over the stream at any corner, centered, or animated (it bounces). On the GPU path the watermark is composited before encode with no readback penalty.
- **Fractional scaling**, HiDPI support, and cursor theme control on the Wayland backend.

## Selkies environment variable mapping

The library itself is configured purely through `CaptureSettings`. The familiar container variables (`DRINODE`, `DRI_NODE`, `AUTO_GPU`, `PIXELFLUX_WAYLAND`, `SELKIES_*`) are read by Selkies and the baseimage init scripts, which translate them into settings fields. Keep that separation in mind when embedding pixelflux directly.

## Building from source

`pip install .` drives a `setuptools-rust` build. On Debian or Ubuntu the build dependencies are roughly: `python3-dev cmake nasm libclang-dev libavcodec-dev libavutil-dev libx264-dev libturbojpeg0-dev libgbm-dev libdrm-dev libwayland-dev libinput-dev libxkbcommon-dev libva-dev` plus a Rust toolchain. Any system FFmpeg from 6.0 through 8.1 works (only used for VA-API). Most users should just take the prebuilt wheels.
