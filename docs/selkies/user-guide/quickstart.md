# Quickstart

The single most important idea in this whole guide: **start minimal**. Almost every problem report we see involves a giant docker command assembled from years of forum posts. The containers are designed to work with almost nothing.

## One command

Pick an app (here Firefox) and run:

```bash
docker run --rm -it \
  --shm-size=1gb \
  -p 3001:3001 \
  lscr.io/linuxserver/firefox:latest bash
```

Open **https://localhost:3001** in your browser (note the `https`), accept the self signed certificate warning, and you are using Firefox running in a container. The trailing `bash` drops you into a shell inside the container, so when you are done, press `ctrl+d` and the container exits and cleans itself up.

That is the entire quickstart. Everything else on this page and in this guide is an additive layer on top of that command.

Want a full desktop instead of one app?

```bash
docker run --rm -it \
  --shm-size=1gb \
  -p 3001:3001 \
  lscr.io/linuxserver/webtop:ubuntu-kde bash
```

## Why these exact flags

| Flag | Why |
| --- | --- |
| `--rm -it ... bash` | Throwaway foreground container with a shell inside it. You can poke around from the command line, and `ctrl+d` exits the shell and removes the container. Perfect for testing, switch to `-d` and a name for real deployments. |
| `--shm-size=1gb` | Browsers and Electron apps need more shared memory than the Docker default of 64MB. Without this, expect tab crashes. |
| `-p 3001:3001` | 3001 is the HTTPS port. HTTPS is required, the client uses modern browser APIs (WebCodecs) that only work in a secure context. Port 3000 serves plain HTTP for use behind a reverse proxy, do not browse to it directly. |

## The debugging philosophy

If a container misbehaves, do not add flags, remove them. Run the minimal command above for your app and see if the problem persists:

```bash
docker run --rm -it --shm-size=1gb -p 3001:3001 lscr.io/linuxserver/firefox:latest bash
```

- **Works minimal but not in your setup?** Re-add your options one at a time (volumes, then env vars, then GPU flags) until it breaks. The last thing you added is the problem.
- **Broken even minimal?** Now you have a clean one line reproduction to include in a bug report, which is exactly what the maintainers will ask for.

This loop solves the majority of issues, especially GPU issues, faster than anything else.

## Adding the usual options

A more realistic long term run, still deliberately small:

```bash
docker run -d \
  --name=firefox \
  --shm-size=1gb \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -p 3001:3001 \
  -v /path/to/config:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/firefox:latest
```

- `PUID` and `PGID` map the in container user `abc` to your host user so files in the volume have sane ownership.
- `/config` is the persistent home directory. Everything the user saves, browser profiles, app settings, lives here and survives container recreation.

Or as compose:

```yaml
---
services:
  firefox:
    image: lscr.io/linuxserver/firefox:latest
    container_name: firefox
    shm_size: 1gb
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - /path/to/config:/config
    ports:
      - 3001:3001
    restart: unless-stopped
```

## Adding basic auth

By default there is **no authentication**. On anything other than a trusted LAN, set at minimum:

```bash
  -e CUSTOM_USER=me \
  -e PASSWORD=changeme \
```

This enables HTTP basic auth. It is fine for a home network. For anything internet facing, put the container behind a reverse proxy with real authentication, see [Security and Hardening](security.md).

## Adding a GPU

If the host has an Intel or AMD GPU with open source drivers, one flag gets you rendering and zero copy encoding on the card:

```bash
docker run --rm -it \
  --shm-size=1gb \
  -p 3001:3001 \
  --device /dev/dri \
  lscr.io/linuxserver/webtop:ubuntu-kde bash
```

For Nvidia with the proprietary drivers:

```bash
docker run --rm -it \
  --shm-size=1gb \
  -p 3001:3001 \
  --runtime nvidia \
  --gpus all \
  --device /dev/nvidia-modeset \
  lscr.io/linuxserver/webtop:ubuntu-kde bash
```

In both cases the GPU is detected and configured automatically. Nvidia has driver version prerequisites on the host, see [GPU Acceleration](gpu.md) for the full story including multi GPU selection and troubleshooting.

## Where to next

- Full install options and conventions: [Installation](installation.md)
- Everything the web client can do (files, clipboard, gamepads, sharing): [Using the Web Client](web-client.md)
- The complete list of apps and desktop flavors: [Available Apps and Desktops](apps.md)
- Locking things down: [Security and Hardening](security.md)
