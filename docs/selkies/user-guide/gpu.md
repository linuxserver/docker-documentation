# GPU Acceleration

A GPU is optional. The CPU pipeline is fast enough for smooth desktop sessions on modest hardware. Add a GPU when you want 3D applications, gaming, hardware video decode inside apps, or the lowest possible CPU usage through zero copy encoding.

## The two GPU jobs

The platform uses a GPU for two separate jobs, controlled by two separate variables:

| Variable | Job | Meaning |
| --- | --- | --- |
| `DRINODE` | **Rendering** | Which GPU applications use for EGL and 3D acceleration, e.g. `/dev/dri/renderD128` |
| `DRI_NODE` | **Encoding** | Which GPU encodes the video stream (VAAPI or NVENC), e.g. `/dev/dri/renderD128` |

Yes, the names differ by one underscore. `DRINODE` renders, `DRI_NODE` encodes.

- If **both point at the same device**, the container enables **zero copy** encoding: the frame is rendered and encoded on the card without ever being copied to system RAM. This drastically lowers CPU usage and latency.
- If they point at **different devices**, one card renders and the other encodes, with a CPU readback in between. Useful, but not zero copy.

## Automatic configuration

You usually do not need to set either variable. When a GPU is mounted into the container it is detected and configured automatically for both rendering and encoding with zero copy (`AUTO_GPU` behavior, the first available GPU is used).

To mount a GPU but *not* use it, set `AUTO_GPU=false`.

## Which codecs a GPU encodes

The encoder menu covers six codecs, described in the [Video encoders](configuration.md#video-encoders) table. Each full frame codec is encoded on the GPU when the encoding device has an engine for it, and by the software encoder in the pixelflux build otherwise. Zero copy applies to every hardware codec, not only H.264: the frame is passed as a DMA-BUF to whichever engine encodes it.

| GPU | Hardware codecs | Notes |
| --- | --- | --- |
| Nvidia NVENC | H.264, H.265, AV1 | AV1 needs Ada (RTX 40 series) or newer. VP8 and VP9 are always software on Nvidia |
| Intel VA-API | H.264, H.265, VP9, and AV1 on Arc and recent integrated graphics | Depends on generation and media driver, `vainfo` lists the encode entry points. VP8 engines only exist on older generations |
| AMD VA-API | H.264, H.265, and AV1 from RDNA 3 | No VP8 or VP9 encode engines |

At startup Selkies probes the encoding device once and drops every encoder that neither the GPU nor the software build can serve, and the container log says which were left off. A codec that falls back to software costs a readback plus a full frame software encode, which for H.265, VP9, and AV1 is several times heavier than x264 and never striped across cores. On a card without the engine, leave `h264enc` first in the menu and treat the other codecs as options for hosts that carry them.

## Intel and AMD (open source drivers)

The simple case. Mount the DRI devices and you are done:

```bash
docker run --rm -it \
  --shm-size=1gb \
  -p 3001:3001 \
  --device /dev/dri \
  lscr.io/linuxserver/webtop:ubuntu-kde bash
```

Compose:

```yaml
    devices:
      - /dev/dri:/dev/dri
```

For multi GPU systems, list the render nodes on the host (`ls /dev/dri`) and pin the one you want:

```yaml
    environment:
      - DRINODE=/dev/dri/renderD129
      - DRI_NODE=/dev/dri/renderD129
```

## Nvidia (proprietary drivers)

!!! warning "Prerequisites matter here"
    Nvidia is the platform where "run the minimal command first" pays off most. Get the host driver right before touching compose files.

**Not available on Alpine based images.**

Whatever the driver version, install it from the `.run` file downloaded directly from Nvidia. Distribution packaged drivers frequently cause problems. On Unraid, use the production branch of the Nvidia Driver Plugin.

### Driver 595.80 and newer

This is the easy path and where the platform is headed: no kernel parameters, no dummy plugs. The only host requirement is that `/dev/nvidia-modeset` exists, on some systems you may need to run this once (or at boot) to activate the device:

```bash
sudo nvidia-modprobe --modeset
```

Then mount it alongside the GPU. `--device /dev/nvidia-modeset` is required for proper Vulkan support:

```bash
docker run --rm -it \
  --shm-size=1gb \
  -p 3001:3001 \
  --runtime nvidia \
  --gpus all \
  --device /dev/nvidia-modeset \
  lscr.io/linuxserver/webtop:ubuntu-kde bash
```

### Driver 580 to 594

Older drivers work but need host preparation:

1. **Kernel parameters**: set `nvidia-drm.modeset=1 nvidia_drm.fbdev=1` on the host bootloader.

    On GRUB systems, edit `/etc/default/grub`:

    ```text
    GRUB_CMDLINE_LINUX_DEFAULT="<existing options> nvidia-drm.modeset=1 nvidia_drm.fbdev=1"
    ```

    then `sudo update-grub` and reboot. On Unraid, add the same string to the `append` line in `/boot/syslinux/syslinux.cfg`.

2. **Dummy plug**: on truly headless machines, the card may need a physical dummy plug inserted so DRM initializes properly.
3. **`/dev/nvidia-modeset`** may still need to be passed, same run command as above.

### Compose

First configure the Nvidia runtime on the host:

```bash
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

```yaml
---
services:
  webtop:
    image: lscr.io/linuxserver/webtop:ubuntu-kde
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [compute,video,graphics,utility]
```

On Unraid, set `DRINODE` and `DRI_NODE` appropriately and add `--gpus all --runtime nvidia` to the extra parameters.

## FullColor 4:4:4 and hardware encoders

If you notice blurry text, especially light text on dark backgrounds, enable **FullColor 4:4:4** encoding in the sidebar, or use the JPEG encoder. This sends true 8 bit color to the browser.

FullColor is carried by H.264 and H.265 on NVENC, x264, and x265, and by VP9 profile 1 on VA-API and libvpx. VP8, AV1, and the OpenH264 software encoder stay 4:2:0 whatever you set, and the sidebar only shows the switch on a codec that carries it.

The caveat is H.264 on Intel and AMD. Current VA-API drivers expose no 4:4:4 H.264 profile, so pixelflux honors the request on the CPU with x264 rather than silently downgrading, which forces a pixel readback from the GPU and costs significant performance. On those cards prefer the default 4:2:0 for motion and let paint over handle static clarity, or try H.265 or VP9, where the driver may negotiate a 4:4:4 surface and stay on the card. The log line `Colorspace:` reports what the session settled on.

## Wayland and X11

Zero copy works on both display stacks. On Wayland the pixelflux compositor renders into GPU buffers and hands them to the encoder. On X11 the containers run a patched XLibre Xvfb with glamor, so the screen pixmap lives on the GPU, and pixelflux pulls each frame out with a DRI3 blit into a DMA-BUF the encoder imports in place. Intel, AMD, and Nvidia all take this path, and the container log says which capture path was chosen. Images that run both stacks select X11 with `-e PIXELFLUX_WAYLAND=false`.

The same rule applies on either stack: rendering and encoding must happen on the same device for zero copy. A session the DRI3 path cannot serve, for example software encoding or a codec the GPU has no engine for, streams through shared memory capture instead, and the log line says why.

## Related environment variables

| Variable | Description |
| --- | --- |
| `AUTO_GPU` | Auto detection of a mounted GPU for rendering and encoding, enabled by default. Set `false` to disable. |
| `DRINODE` | Rendering GPU (EGL / 3D). |
| `DRI_NODE` | Encoding GPU (VAAPI / NVENC). |
| `DISABLE_DRI3` | X11 mode only, start Xvfb without the GPU. Applications render on the CPU and capture falls back to shared memory. |
| `PIXELFLUX_WAYLAND` | `true` runs the Wayland compositor stack, `false` runs X11. Zero copy encoding works on both. |

## Debugging GPU problems

Follow the minimal command loop from the [Quickstart](quickstart.md):

1. Run the container with **no** GPU flags. Confirm the base experience works with CPU encoding.
2. Add only the device mount (`--device /dev/dri` or the Nvidia trio). Check container logs for GPU detection messages.
3. Inside the session, open a terminal and run `vkcube`. A spinning cube at full speed means rendering on the card works, this is the go to in container GPU test. `vainfo` (Intel/AMD) and `nvidia-smi` (Nvidia) confirm the container sees the card and its encode capabilities.
4. Only then start pinning `DRINODE` and `DRI_NODE` manually.

If the container works without the GPU flags and breaks with them, the problem is host side: driver version, kernel parameters, or device permissions.
