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

One caveat: only Nvidia GPUs can encode 4:4:4 in zero copy mode. Enabling FullColor on Intel or AMD falls back to CPU encoding, which forces a pixel readback from the GPU and costs significant performance. On those cards, prefer the default 4:2:0 for motion and let paint over handle static clarity.

## Wayland and X11

The Wayland stack is the default and is where all GPU acceleration development happens. You can force the legacy X11 stack with `-e PIXELFLUX_WAYLAND=false`, but GPU acceleration under X11 is not currently seeing development attention. If you are on X11 and using acceleration, clamp the virtual display to avoid memory exhaustion, e.g. `-e MAX_RES=3840x2160`, and if you still have problems lock the resolution down:

```bash
-e SELKIES_MANUAL_WIDTH=1920
-e SELKIES_MANUAL_HEIGHT=1080
-e MAX_RES=1920x1080
```

## Related environment variables

| Variable | Description |
| --- | --- |
| `AUTO_GPU` | Auto detection of a mounted GPU for rendering and encoding, enabled by default. Set `false` to disable. |
| `DRINODE` | Rendering GPU (EGL / 3D). |
| `DRI_NODE` | Encoding GPU (VAAPI / NVENC). |
| `DISABLE_ZINK` | X11 mode only, do not set Zink variables when a card is detected, applications fall back to CPU rendering. |
| `DISABLE_DRI3` | X11 mode only, disable DRI3 acceleration, applications fall back to CPU rendering. |
| `PIXELFLUX_WAYLAND` | `true` is the modern Wayland stack with zero copy support, `false` forces legacy X11. |

## Debugging GPU problems

Follow the minimal command loop from the [Quickstart](quickstart.md):

1. Run the container with **no** GPU flags. Confirm the base experience works with CPU encoding.
2. Add only the device mount (`--device /dev/dri` or the Nvidia trio). Check container logs for GPU detection messages.
3. Inside the session, open a terminal and run `vkcube`. A spinning cube at full speed means rendering on the card works, this is the go to in container GPU test. `vainfo` (Intel/AMD) and `nvidia-smi` (Nvidia) confirm the container sees the card and its encode capabilities.
4. Only then start pinning `DRINODE` and `DRI_NODE` manually.

If the container works without the GPU flags and breaks with them, the problem is host side: driver version, kernel parameters, or device permissions.
