# linuxserver/pyload

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-pyload.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pyload) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-pyload.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pyload/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pyload/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-pyload/container_registry) [![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/pyload) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/pyload.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/pyload) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/pyload.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/pyload) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/pyload.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/pyload) [![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-pyload/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-pyload/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/pyload/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/pyload/latest/index.html)

[Pyload](https://pyload.net/) is a Free and Open Source download manager written in Python and designed to be extremely lightweight, easily extensible and fully manageable via web.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/pyload` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=pyload \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8000:8000 \
  -p 7227:7227 `#optional` \
  -v </path/to/pyload/config>:/config \
  -v </path/to/downloads>:/downloads \
  --restart unless-stopped \
  linuxserver/pyload
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  pyload:
    image: linuxserver/pyload
    container_name: pyload
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/pyload/config>:/config
      - </path/to/downloads>:/downloads
    ports:
      - 8000:8000
    ports:
      - 7227:7227 #optional
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `8000` | Allows HTTP access to the application |
| `7227` | pyLoad control port |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | pyLoad Configuration and files database |
| `/downloads` | Destination of pyLoad downloads |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the web interface at `http://your-ip:8000` the default login is: username - **admin** password - **password**

For general usage please see the pyLoad wiki [here](https://github.com/pyload/pyload/wiki) .

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27pyload%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=pyload)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it pyload /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f pyload`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' pyload`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/pyload`

## Versions

* **18.07.19:** - Add ffmpeg for plugins the do video processing.
* **28.06.19:** - Rebasing to alpine 3.10.
* **08.06.19:** - Initial release.

