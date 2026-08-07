# Development Environment

How to hack on the stack itself. The short version: you do not build any of this on your desktop. The container is the development environment, you mount your source into it and the init system runs it live with hot reload.

## Dev mode in the containers

Every Selkies baseimage container ships a development mode designed for iterating on the Selkies server, web client, and pixelflux, using the container as your runtime so you never have to reproduce the compositor and audio stack locally.

### Selkies server and web client

Clone the [selkies repository](https://github.com/selkies-project/selkies), mount it at `/config/src`, and set `DEV_MODE` to the dashboard you want served:

```bash
git clone https://github.com/selkies-project/selkies.git
cd selkies
git checkout -f lsio
docker run --rm -it \
  --shm-size=1gb \
  -e DEV_MODE=selkies-dashboard \
  -e PUID=1000 \
  -e PGID=1000 \
  -v $(pwd):/config/src \
  -p 3001:3001 ghcr.io/linuxserver/webtop:ubuntu-kde bash
```

The application restarts on code changes to the mounted source directory and provides feedback for debugging. The web side runs through Vite with hot module reload, and Nginx swaps the dev server to the root path so `https://localhost:3001/` serves your live build.

`DEV_MODE` values:

| Value | Behavior |
| --- | --- |
| `selkies-dashboard` (or another dashboard directory name) | Runs the dashboard through Vite with hot module reload, watching your mounted source, with the Python server under a watcher as well |
| `core` | Watches and rebuilds `selkies-web-core`, the streaming engine itself |
| `pixelflux` | Rapid development against a mounted pixelflux checkout, see below |

### Pixelflux

The same pattern gives you a pixelflux rapid development environment. Mount a pixelflux checkout instead and set `DEV_MODE=pixelflux`:

```bash
git clone https://github.com/linuxserver/pixelflux.git
cd pixelflux
docker run --rm -it \
  --shm-size=1gb \
  -e DEV_MODE=pixelflux \
  -e PUID=1000 \
  -e PGID=1000 \
  -v $(pwd):/config/src \
  -p 3001:3001 ghcr.io/linuxserver/webtop:ubuntu-kde bash
```

The container builds the mounted source (all Rust build dependencies are present in the image) and runs the session against your working copy, so a compositor or encoder change is one container restart away from being on screen. For pipeline experiments outside of Selkies entirely, `example/screen_to_browser.py` in the pixelflux repository is a complete standalone streaming server against `example/index.html`, the fastest possible inner loop.

## Repository map

| Repository | What you touch there |
| --- | --- |
| [selkies-project/selkies](https://github.com/selkies-project/selkies) | Server, protocol, web client, dashboards, gamepad addons |
| [linuxserver/pixelflux](https://github.com/linuxserver/pixelflux) | Capture, compositor, encoders, Computer Use API |
| [linuxserver/docker-baseimage-selkies](https://github.com/linuxserver/docker-baseimage-selkies) | Packaging, init scripts, Nginx, hardening, patches. One branch per distro |
| [linuxserver/docker-webtop](https://github.com/linuxserver/docker-webtop) and the app repositories | Downstream images, one branch per flavor for Webtop |
| [selkies-project/sealskin](https://github.com/selkies-project/sealskin) | Orchestration server, extension, mobile |
| [linuxserver/sealskin-apps](https://github.com/linuxserver/sealskin-apps) | App manifests and autostart scripts |
| [linuxserver/pelorus](https://github.com/linuxserver/pelorus) | Agent API and chat UI |
| [selkies-project/selkies-desktop](https://github.com/selkies-project/selkies-desktop) | The minimal desktop shell |
| [linuxserver/waylandtyper](https://github.com/linuxserver/waylandtyper) | Our maintained fork of wtype for unicode text injection |

The baseimage Dockerfile is the authoritative recipe for everything compiled into the images (labwc with the IPC patch, the patched wlroots, selkies-desktop, waylandtyper), so when you need to know exactly how a piece is built, read the corresponding Dockerfile stage.

## Contributing

Development happens in the open across all of the above. Bug reports with the [minimal command](../user-guide/troubleshooting.md#step-zero-the-minimal-command) reproduction are gold. For discussion, the [LinuxServer.io Discord](https://linuxserver.io/discord) and the Selkies project community are the places to be. Licensing: the Python server, pixelflux, and selkies-desktop are MPL-2.0; the containers are GPL-3.
