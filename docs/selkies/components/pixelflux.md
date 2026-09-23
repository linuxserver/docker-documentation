# Pixelflux and Pcmflux

**Repositories:** [selkies-project/pixelflux](https://github.com/selkies-project/pixelflux) and [selkies-project/pcmflux](https://github.com/selkies-project/pcmflux) · **PyPI:** `pip install pixelflux pcmflux` · **License:** MPL-2.0 · **Upstream docs:** [docs.selkies.io](https://docs.selkies.io/) · **Rustdocs:** [pixelflux](https://pixelflux.selkies.io/pixelflux/index.html), [pcmflux](https://pcmflux.selkies.io/pcmflux/index.html)

Pixelflux is the rendering and capture pipeline at the core of the entire platform. It captures a Linux framebuffer, decides what changed, encodes it as JPEG, H.264, H.265, VP8, VP9, or AV1, and hands the encoded frames to your code through a Python callback. Selkies is its primary consumer, but it is a standalone library you can embed in anything.

Pcmflux is its audio sibling: it captures PulseAudio output and encodes Opus frames for delivery to the browser, and handles the microphone return path. Both ship as prebuilt wheels for x86_64 and aarch64 on glibc and musl.

## What it actually is

As of the 2.0.0 release, pixelflux is a **Rust** library exposed to Python through PyO3 (earlier versions were C++ with ctypes). One extension module contains:

- An **X11 backend**: DRI3 capture that blits the GPU resident screen into DMA-BUFs the encoder imports in place, and XShm capture with XFixes cursor tracking where that does not apply.
- A **Wayland backend**: a full headless Wayland compositor built on [Smithay](https://github.com/Smithay/smithay), running in process. This is the key architectural point of the Wayland stack: **pixelflux does not capture a Wayland compositor, it is the compositor.** It synthesizes the output, seat, and clipboard itself, which is why the framebuffer can live directly on a GPU and why input is injected through its API rather than tools like xdotool.
- Six codecs across software and hardware encoders, and the damage tracking, paint over, and rate control logic shared between them.

## Encoders

Every codec is selected by name (`codec = "h264"` and so on) and pixelflux resolves the encoder behind it: the GPU engine when the encoding device has one, the software encoder the build carries otherwise. `pixelflux.SOFTWARE_ENCODERS` names the software encoder per codec and `pixelflux.hardware_encoders(node)` the codecs a render node's NVENC or VA-API serves, which is how Selkies trims its menu at startup.

| Codec | Software | NVENC (Nvidia) | VA-API (Intel and AMD) | Shape | 4:4:4 |
| --- | --- | --- | --- | --- | --- |
| JPEG | libjpeg-turbo, vendored | No | No | Striped | Always, JFIF is full color |
| H.264 | x264, or OpenH264 in a GPL free build | Yes | Yes | Striped or full frame | x264 and NVENC. VA-API has no 4:4:4 H.264 profile on current drivers and hands the request to x264. OpenH264 is 4:2:0 only |
| H.265 | x265, or kvazaar in a GPL free build | Yes | Yes | Full frame | x265 and NVENC, VA-API negotiates a 4:4:4 surface per device |
| VP8 | libvpx | No | Where the GPU has an engine | Full frame | No, and VP8 declares BT.601 because its bitstream can name nothing else |
| VP9 | libvpx | No | Yes | Full frame | Profile 1 on libvpx and VA-API |
| AV1 | SVT-AV1 | Ada and newer | Where the GPU has an engine | Full frame | No |

Hardware encoders are loaded at runtime: NVENC through the driver's `libnvidia-encode` and `libcuda` with no CUDA toolkit, VA-API and the software H.265, VP8, VP9, and AV1 encoders through the system FFmpeg's `libavcodec`. The official wheels are GPL builds with x264 and x265; a `PIXELFLUX_ENABLE_GPL=0` source build swaps in OpenH264 and kvazaar and keeps everything else.

### Striped encoding

For JPEG and H.264 on the CPU the screen is divided into horizontal stripes, one per CPU core (each at least 64 rows). Each stripe has its own encoder instance and its own damage history, and stripes are encoded in parallel across a thread pool. Only stripes that changed are encoded and sent. This is the "hybrid VNC and video codec" idea that lets a CPU only server idle at nearly zero cost and still deliver 60fps where the screen is actually moving.

Hardware encoders always operate full frame, delivered as a single full height stripe, since the GPU encodes the whole surface in one shot anyway. H.265, VP8, VP9, and AV1 are full frame on the CPU too, so a software session on those codecs gets neither the per core parallelism nor the dirty stripe savings, and costs several times the CPU of striped x264.

### Damage detection

- **X11:** on the DRI3 path the Damage extension reports whether anything was drawn since the last frame, so nothing is hashed. On the XShm path each stripe's pixels are hashed (xxh3) every frame, a changed hash marks the stripe dirty. Continuously changing regions enter a "damage block" state that skips re hashing for a configured number of frames to save CPU.
- **Wayland:** no hashing needed, the compositor knows exactly which rectangles clients damaged and maps them to stripes.
- A fully idle screen takes a fast path that skips the encode thread pool entirely.

### Paint over

The signature quality feature. After a region has been static for a configurable number of frames (`paint_over_trigger_frames`), it is re sent at high quality: a higher quality JPEG, or for the video codecs a burst of frames at a lower CRF. Motion cancels an in flight burst. The result is video efficiency during motion and pixel perfect text the moment you stop scrolling.

### Rate control

- **CRF/CQP mode** (default): constant quality, bits go wherever needed.
- Infinite GOP by default: keyframes are only sent on demand (client join, recovery, or an optional periodic interval). Bitrate, framerate, and quality are all adjustable live without restarting the capture.

## Zero copy

**Wayland.** When the compositor renders on a GPU and the encoder is on the same GPU, frames flow as DMA-BUF handles from the render buffer straight into NVENC or VA-API. The pixels never touch system RAM and the CPU never sees them. If the render and encode devices differ, or a software encoder is selected, pixelflux falls back to a readback path automatically and logs which decision it made. Zero copy is a property of the capture path, not the codec: any codec the GPU carries takes it.

**X11.** On an X server whose screen lives on the GPU, which is what the containers run (XLibre Xvfb started with `-glamor -dri`), pixelflux allocates a small pool of DMA-BUFs through GBM on the render node the server draws with, hands each to the server as a pixmap through DRI3, and captures every frame as one `CopyArea` of the root window into the next buffer, a GPU blit in glamor. The encoder imports that buffer in place through the same path the Wayland capture uses, so no frame crosses to the CPU. The Damage extension gates capture so a static screen costs nothing, and the server composites the cursor and any watermark through Render. Nvidia, Intel, and AMD all take this path. It is declined, with one log line saying why, for software encoding, a codec the GPU has no engine for, a server drawing on a different device than the encoder, or a server without DRI3 1.2, Damage, or Render, and the session then streams through XShm with one copy per frame.

GPU selection is automatic: it walks `/sys/class/drm`, identifies cards by driver (`nvidia` goes to NVENC, `i915` and `amdgpu` to VA-API), and can be pinned by device path, index, or an `auto_gpu` token matching a driver or vendor ID.

## API sketch

```python
from pixelflux import CaptureSettings, ScreenCapture, ensure_wayland_display

settings = CaptureSettings()
settings.capture_width = 1920
settings.capture_height = 1080
settings.target_fps = 60.0
settings.codec = "h264"           # "jpeg", "h264", "h265", "vp8", "vp9", or "av1"
settings.video_crf = 25
settings.use_paint_over_quality = True

def on_frame(frame):
    # frame is a StripeFrame: zero copy buffer protocol object
    # frame.data_type: 0 = JPEG, 1 = H.264, 2 = VP8, 3 = VP9, 4 = AV1, 5 = H.265
    # bytes(frame) or memoryview(frame) for the payload
    ws.send(bytes(frame))

capture = ScreenCapture()
capture.start_capture(on_frame, settings)
```

Each encoded stripe arrives with a compact binary header (6 bytes for JPEG, 10 for the video codecs carrying frame type and codec id, frame number, stripe offset, and dimensions) that the web client parses to place stripes on the canvas. Headers can be omitted for embedding in your own protocol.

The Wayland backend additionally exposes input injection (keyboard by scancode with a hot swappable XKB keymap, absolute and relative pointer, buttons, scroll), clipboard get and set, cursor callbacks delivering PNG cursor images out of band, and live rate updates. `example/screen_to_browser.py` in the repository is a complete working WebSocket streaming server in one file, with a matching browser client in `example/index.html`.

## Extras worth knowing about

- **Computer Use API**: setting the `PIXELFLUX_CU=<port>` environment variable starts a small HTTP server with a `POST /computer-use` endpoint accepting JSON actions (`screenshot`, `left_click`, `type`, `key`, `scroll`, `zoom`, and friends). This is the raw input and vision layer that [Pelorus](pelorus.md) builds on.
- **Recording sink**: point `recording_socket` (or `PIXELFLUX_RECORDING_SOCKET`) at a Unix socket path and pixelflux serves the raw elementary stream to any connected client, forcing a keyframe when someone connects: Annex B for H.264 and H.265, an OBU stream for AV1, IVF for VP8 and VP9. Requires a full frame codec, striped H.264 and JPEG are not served.
- **Watermarking**: composite a PNG over the stream at any corner, centered, or animated (it bounces). On the GPU path the watermark is composited before encode with no readback penalty.
- **Fractional scaling**, HiDPI support, and cursor theme control on the Wayland backend.

## Selkies environment variable mapping

The library itself is configured purely through `CaptureSettings`. The familiar container variables (`DRINODE`, `DRI_NODE`, `AUTO_GPU`, `PIXELFLUX_WAYLAND`, `SELKIES_*`) are read by Selkies and the baseimage init scripts, which translate them into settings fields. Keep that separation in mind when embedding pixelflux directly.

## Building from source

`pip install .` drives a `setuptools-rust` build. On Debian or Ubuntu the build dependencies are roughly: `python3-dev cmake nasm libclang-dev libavcodec-dev libavutil-dev libx264-dev libturbojpeg0-dev libgbm-dev libdrm-dev libwayland-dev libinput-dev libxkbcommon-dev libva-dev` plus a Rust toolchain. Any system FFmpeg from 6.0 through 9.0 works, it supplies the VA-API encoders and the software H.265, VP8, VP9, and AV1 encoders, so a codec whose encoder that FFmpeg lacks has no software path. Most users should just take the prebuilt wheels.
