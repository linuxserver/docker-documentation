# Baseimage Internals

What actually happens inside a Selkies container, boot order, services, and the files involved. Reference material for image builders and anyone debugging a container from the inside.

## Build composition

The baseimage Dockerfile is a multi stage build assembling, onto a LinuxServer.io distro base (Debian, Ubuntu, Alpine, Fedora, Arch, or Kali):

- A patched **Xvfb** (adds a `-vfbdevice` flag for DRI3 GPU passthrough) from the LSIO xvfb image
- The **web frontend**: the Selkies repository pinned to an exact commit, with `selkies-web-core` and the dashboards built and dropped in `/usr/share/selkies/`
- **labwc 0.9.7** built from source with the IPC patch (adds `labwc -i`, a read only JSON window query socket at `$XDG_RUNTIME_DIR/labwc.sock`, consumed by Pelorus)
- A rebuilt **wlroots** with a defensive patch that catches SIGSEGV and SIGBUS inside pixman draw calls and skips the frame instead of crashing the compositor
- **selkies-desktop** and **[waylandtyper](https://github.com/linuxserver/waylandtyper)** (our maintained fork of wtype, fixing many bugs in the old codebase) built from source
- The **selkies** Python package installed into the `/lsiopy` virtualenv (pulling in pixelflux and pcmflux wheels), plus **pelorus**
- The **joystick interposer** (`/usr/lib/selkies_joystick_interposer.so`) and **fake udev** (`/opt/lib/libudev.so.1.0.0-fake`) compiled from the Selkies addons
- Nginx with fancyindex, PulseAudio, mesa and VA-API userspace, Vulkan loaders, all system locales, proot-apps, Docker in Docker machinery, and passwordless sudo for `abc`

Baked ENV defaults worth knowing: `HOME=/config`, `DISPLAY=:1`, `TITLE=Selkies`, `SELKIES_ENCODER="x264enc,jpeg"`, `START_DOCKER=true`, `DISABLE_ZINK=false`, `DISABLE_DRI3=false`, `NVIDIA_DRIVER_CAPABILITIES=all`, and the interposer path in `SELKIES_INTERPOSER`.

## Boot: the init chain

The Selkies oneshots hook into the standard LSIO s6 chain right after `init-os-end` (so PUID and PGID remapping, Docker mods, and custom files all run in their usual order around them):

```
init-os-end
 └─ init-selkies (marker)
     └─ init-nginx
         └─ init-selkies-config
             └─ init-video
                 └─ init-selkies-end → init-config → ... → init-services
```

**`init-nginx`** renders `/defaults/default.conf` into the live Nginx config with plain string substitution: ports (`CUSTOM_PORT`, `CUSTOM_HTTPS_PORT`, `CUSTOM_WS_PORT`), `SUBFOLDER` tokens, the download path, basic auth (generates `.htpasswd` and uncomments the auth lines when `PASSWORD` is set), IPv6 removal, dev mode rewiring, dashboard selection into `/usr/share/selkies/web`, and the PWA `manifest.json` with your `TITLE`. On first run it also generates the ten year self signed certificate into `/config/ssl/`.

**`init-selkies-config`** is the big one:

- Chooses the mode: `PIXELFLUX_WAYLAND=true` selects labwc paths (`$HOME/.config/labwc`, `/defaults/autostart_wayland`, `/defaults/menu_wayland.xml`) and forces `SELKIES_SECOND_SCREEN=false`; otherwise Openbox paths.
- First run copies of `autostart` and `menu.xml` into the config dir (persistent, user editable); `rc.xml` for labwc is regenerated from the template every boot.
- Recreates `$HOME/.XDG` as `XDG_RUNTIME_DIR` and clears stale PulseAudio state, so unclean shutdowns recover.
- Applies every hardening variable (permission stripping, sudoers corruption, menu and keybind editing, locking rc.xml and autostart when watchdog mode is on), the details are in the [Security guide](../user-guide/security.md).
- GPU env: with exactly one render node and nothing set, points `DRINODE` and `DRI_NODE` at it; wires `PIXELFLUX_CU=5000` and `ROOT_PATH=/pelorus` when `PELORUS=true`.
- Creates the gamepad device nodes (`/dev/input/js0-3` and event nodes) and sets the global `LD_PRELOAD` for the interposer and fake udev, unless `NO_GAMEPAD` is set.
- Syncs proot-apps into the user home and handles `LC_ALL` locale derivation.

**`init-video`** fixes `/dev/dri` and `/dev/dvb` group permissions for `abc` (creating a matching group for the device GID when needed), auto enables `AUTO_GPU` on x86_64 when a render node exists and nothing was configured, probes whether older Intel hardware needs the `i965` VA-API driver, and repairs Nvidia ICD, Vulkan, EGL, and GBM plumbing inside the container.

## The services

| Service | Behavior |
| --- | --- |
| `svc-nginx` | Reaps zombie workers then runs Nginx in the foreground |
| `svc-pulseaudio` | PulseAudio as `abc`, never idle exits, runtime dir under `/defaults` |
| `svc-xorg` | X11 mode: Xvfb on `:1` with a max resolution from `MAX_RES` and the DRI3 device flag. Wayland mode: sleeps |
| `svc-selkies` | Loads the `output` and `input` null sinks once PulseAudio is up, then runs `selkies --addr=localhost --mode=websockets` as `abc`. In Wayland mode this is what brings up the pixelflux compositor on `wayland-1` |
| `svc-de` | Waits for the display (the `wayland-1` socket, or `xset q` on X11), then executes `/defaults/startwm_wayland.sh` or `/defaults/startwm.sh` as `abc`, recording the PID for clean teardown. On X11 it also sets the initial 1024x768 mode (or `SELKIES_MANUAL_WIDTH` and `HEIGHT`) via xrandr |
| `svc-xsettingsd` | X11 only, DPI hinting for legacy toolkits |
| `svc-watchdog` | Only active with `RESTART_APP=true`: polls for the autostart process and relaunches it if it dies |
| `svc-dbus` | System D-Bus (present on distros that need it) |
| `svc-docker` | Detects privileged mode and starts the inner Docker daemon unless `START_DOCKER=false` |

Teardown is equally deliberate: `svc-de`'s finish script walks the session's process tree with a graceful TERM and a five second deadline, so recreating containers does not leave half dead sessions.

## Nginx layout

One config, two identical server blocks (HTTP 3000, HTTPS 3001):

| Location | Purpose |
| --- | --- |
| `SUBFOLDER` (default `/`) | The web client static files from `/usr/share/selkies/web/` |
| `SUBFOLDERwebsocket` | Proxy to the Selkies data WebSocket on 127.0.0.1:8082 |
| `SUBFOLDERfiles` | fancyindex download listing of `FILE_MANAGER_PATH` (default `/config/Desktop`), removed entirely when downloads are disabled or `HARDEN_DESKTOP` is on |
| `SUBFOLDERpelorus/` | Proxy to the Pelorus API on 127.0.0.1:5100 |
| `/devmode` | Proxy to a Vite dev server, see [Development Environment](development.md) |

All proxy locations use hour long timeouts, no buffering, and a 10MB body cap. Because substitution is plain `sed`, exotic characters in `PASSWORD` or `SUBFOLDER` can break the config, keep them simple.

## Internal port map

| Port | Owner | Exposure |
| --- | --- | --- |
| 3000, 3001 | Nginx | Published, everything user facing |
| 8082 | Selkies WebSocket | localhost only, via Nginx |
| 8083 | Selkies token control plane | localhost only, orchestrators call it, never expose |
| 5100 | Pelorus API | localhost only, via Nginx at `/pelorus/` |
| 5000 | pixelflux Computer Use API | localhost only |
| 5173 | Vite dev server | localhost only, via `/devmode` |

## Wayland session wiring

`/defaults/startwm_wayland.sh` in the baseimage handles four combinations of `PELORUS` and `SELKIES_DESKTOP`: plain labwc; labwc plus the selkies-desktop panel; labwc with IPC plus the Pelorus and AT-SPI stack; or all of it together, in each case exporting the cursor theme, `us` XKB defaults, and `WAYLAND_DISPLAY=wayland-1` for labwc while the shell and apps land on `wayland-0` with `DISPLAY=:0` for XWayland. Downstream desktops override this file wholesale, see [Building Custom Images](building-images.md#case-study-docker-webtop-ubuntu-kde-full-desktop).

## Things inherited from the LSIO base

Not implemented here, but always available: `PUID`, `PGID`, `TZ`, `UMASK`, `DOCKER_MODS`, `/custom-cont-init.d`, and `/custom-services.d`. Those hooks are the subject of [Customizing Containers](customization.md).
