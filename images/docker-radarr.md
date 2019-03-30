# linuxserver/radarr

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn) [![](https://images.microbadger.com/badges/version/linuxserver/radarr.svg)](https://microbadger.com/images/linuxserver/radarr) [![](https://images.microbadger.com/badges/image/linuxserver/radarr.svg)](https://microbadger.com/images/linuxserver/radarr) ![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/radarr.svg) ![Docker Stars](https://img.shields.io/docker/stars/linuxserver/radarr.svg) [![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-radarr/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-radarr/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/radarr/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/radarr/latest/index.html)

[Radarr](https://github.com/Radarr/Radarr) - A fork of Sonarr to work with movies à la Couchpotato.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/radarr` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :---: | :--- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=radarr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 7878:7878 \
  -v <path to data>:/config \
  -v <path/to/movies>:/movies \
  -v <path/to/downloadclient-downloads>:/downloads \
  --restart unless-stopped \
  linuxserver/radarr
```

You can choose between ,using tags, various branch versions of radarr, no tag is required to remain on the main branch.

Add one of the tags, if required, to the linuxserver/radarr line of the run/create command in the following format, linuxserver/radarr:nightly

The nightly branch and master branch can from time to time be the same version.

HOWEVER , USE THE NIGHTLY BRANCH AT YOUR OWN PERIL !!!!!!!!!

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  radarr:
    image: linuxserver/radarr
    container_name: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <path/to/movies>:/movies
      - <path/to/downloadclient-downloads>:/downloads
    ports:
      - 7878:7878
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `7878` | The port for the Radarr webinterface |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London, this is required for Radarr |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Database and Radarr configs |
| `/movies` | Location of Movie library on disk |
| `/downloads` | Location of download managers output directory |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `<your-ip>:7878`, for more information check out [Radarr](https://github.com/Radarr/Radarr).

## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it radarr /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f radarr`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' radarr`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/radarr`

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **09.09.18:** - Add pipeline build process.
* **24.02.18:** - Add nightly branch.
* **06.02.18:** - Radarr repo changed owner.
* **15.12.17:** - Fix continuation lines.
* **17.04.17:** - Switch to using inhouse mono baseimage, adds python also.
* **13.04.17:** - Switch to official mono repository.
* **10.01.17:** - Initial Release.

