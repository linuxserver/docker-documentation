# linuxserver/lidarr

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-lidarr.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-lidarr/releases) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/lidarr.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/lidarr) [![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/lidarr.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/lidarr) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/lidarr.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/lidarr) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/lidarr.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/lidarr) [![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-lidarr/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-lidarr/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/lidarr/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/lidarr/latest/index.html)

[Lidarr](https://github.com/lidarr/Lidarr) is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/lidarr` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :---: | :--- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :---: | :--- |
| latest | Stable Lidarr releases. |
| preview | Nightly Lidarr Releases. |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=lidarr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e UMASK_SET=022 `#optional` \
  -p 8686:8686 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/music>:/music \
  -v </path/to/downloads>:/downloads \
  --restart unless-stopped \
  linuxserver/lidarr
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  lidarr:
    image: linuxserver/lidarr
    container_name: lidarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - UMASK_SET=022 #optional
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/music>:/music
      - </path/to/downloads>:/downloads
    ports:
      - 8686:8686
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `8686` | Application WebUI |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `UMASK_SET=022` | control permissions of files and directories created by Sonarr |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Configuration files for Lidarr. |
| `/music` | Music files. |
| `/downloads` | Path to your download folder for music. |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `<your-ip>:8686`, for more information check out [Lidarr](https://github.com/lidarr/Lidarr).

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it lidarr /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f lidarr`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' lidarr`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/lidarr`

## Versions

* **01.08.19:** - Rebase to Linuxserver LTS mono version.
* **13.06.19:** - Add env variable for setting umask.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **08.03.19:** - Rebase to Bionic, use proposed endpoint for libchromaprint.
* **26.01.19:** - Add pipeline logic and multi arch.
* **22.04.18:** - Switch to beta builds.
* **17.03.18:** - Add ENV XDG\_CONFIG\_HOME="/config/xdg" to Dockerfile for signalr fix.
* **27.02.18:** - Use json to query for new version.
* **23.02.18:** - Initial Release.

