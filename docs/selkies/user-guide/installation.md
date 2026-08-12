# Installation

This page covers running the prebuilt containers properly for long term use. If you have not run one at all yet, do the [Quickstart](quickstart.md) first.

## Requirements

- A modern browser on the client. The client uses WebCodecs and other current APIs; recent Chrome, Edge, Brave, Vivaldi, Firefox, and Safari work. Chromium family browsers give the best experience.
- Docker (docker-ce) on any x86_64 or aarch64 Linux host. Alternative runtimes such as Podman may work but are not officially supported, we support docker-ce.
- No GPU required. See [GPU Acceleration](gpu.md) when you want one.

## docker run

```bash
docker run -d \
  --name=webtop \
  --shm-size=1gb \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -p 3001:3001 \
  -v /path/to/config:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/webtop:ubuntu-kde
```

## docker compose

```yaml
---
services:
  webtop:
    image: lscr.io/linuxserver/webtop:ubuntu-kde
    container_name: webtop
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

Then browse to `https://<host>:3001`.

## The conventions, explained

These containers follow every LinuxServer.io convention, so if you have run any LSIO image before, nothing here will surprise you.

### Ports

| Port | Protocol | Purpose |
| --- | --- | --- |
| `3001` | HTTPS | The port you use. Self signed certificate out of the box |
| `3000` | HTTP | Only for use behind a reverse proxy that terminates TLS. Browsing to it directly gives you a broken client, because the required browser APIs need a secure context |

Both are served by an Nginx instance inside the container which also proxies the internal WebSocket streaming port. You never need to publish anything else. `CUSTOM_PORT`, `CUSTOM_HTTPS_PORT`, and `CUSTOM_WS_PORT` change the internal ports if they collide with something in your network stack (mostly relevant with `network_mode: host`).

### The /config volume

`/config` is the in container home directory of the desktop user (`abc`). Browser profiles, application settings, downloads, everything the user touches lives here. **Anything outside `/config` is lost on image update.** That is by design, see [Installing Applications](installing-apps.md) for the persistence options.

A useful property: `/config` is portable across image flavors. You can move a home directory from an Ubuntu based tag to a Fedora based tag and user data carries over.

### PUID and PGID

The desktop user `abc` is remapped to these IDs at start, so files created in the `/config` volume belong to your host user. Find yours with `id`. One caveat: if you use the Docker in Docker feature, the Docker data itself runs as root and does not respect PUID and PGID.

### shm_size

Set `--shm-size=1gb` on everything. Browsers and Electron apps crash tabs with the Docker default of 64MB, and audio machinery also uses `/dev/shm`. It costs nothing when unused.

### Timezone and language

- `TZ` sets the timezone (e.g. `Europe/Amsterdam`).
- `LC_ALL` sets the session language, e.g. `LC_ALL=de_DE.UTF-8`. All locales are prebuilt in the images. See the [Configuration Reference](configuration.md#internationalization) for the common values.

## Updating

Standard container hygiene: pull the new image and recreate.

```bash
docker compose pull && docker compose up -d
```

Because `/config` holds all user state, updates are non destructive. Tools like Watchtower or Diun work fine.

## Special modes

### Docker in Docker

Run with `--privileged` and the container starts its own Docker daemon, letting the desktop user run containers inside the session (handy for development desktops). Mount `-v /path/to/docker:/var/lib/docker` for reasonable performance, and set `START_DOCKER=false` if you want privilege without the daemon.

Alternatively mount the host socket, `-v /var/run/docker.sock:/var/run/docker.sock`, to control the host's Docker from inside the session. Understand the security implication: that is effectively root on the host.

### Host networking

Host networking is discouraged. These containers run a lot of internal services, and on the host network every one of them competes with your host and every other container for ports. Prefer normal bridged networking with the single published port. If you genuinely need `network_mode: host` (some VPN or discovery setups), it does work, use `CUSTOM_PORT`, `CUSTOM_HTTPS_PORT`, and `CUSTOM_WS_PORT` to move the internal ports out of the way of collisions.

## Where next

- [GPU Acceleration](gpu.md) for hardware rendering and encoding
- [Security and Hardening](security.md) before exposing anything
- [Reverse Proxy](reverse-proxy.md) for clean URLs and real TLS certificates
