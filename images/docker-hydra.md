# linuxserver/hydra

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn) [![](https://images.microbadger.com/badges/version/linuxserver/hydra.svg)](https://microbadger.com/images/linuxserver/hydra) [![](https://images.microbadger.com/badges/image/linuxserver/hydra.svg)](https://microbadger.com/images/linuxserver/hydra) ![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/hydra.svg) ![Docker Stars](https://img.shields.io/docker/stars/linuxserver/hydra.svg) [![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-hydra/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-hydra/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/hydra/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/hydra/latest/index.html)

[Hydra](https://github.com/theotherp/nzbhydra) is a meta search for NZB indexers and the "spiritual successor" to NZBmegasearcH. It provides easy access to a number of raw and newznab based indexers.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/hydra` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=hydra \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 5075:5075 \
  -v <path to data>:/config \
  -v <nzb download>:/downloads \
  --restart unless-stopped \
  linuxserver/hydra
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  hydra:
    image: linuxserver/hydra
    container_name: hydra
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <nzb download>:/downloads
    ports:
      - 5075:5075
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `5075` | WebUI |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Where hydra should store config files. |
| `/downloads` | NZB download folder. |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

The web interface is at `<your ip>:5075` , to set up indexers and connections to your nzb download applications.

## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it hydra /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f hydra`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' hydra`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/hydra`

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **11.02.19:** - Add pipeline logic and multi arch.
* **17.08.18:** - Rebase to alpine 3.8.
* **12.12.17:** - Rebase to alpine 3.7.
* **20.07.17:** - Internal git pull instead of at runtime.
* **25.05.17:** - Rebase to alpine 3.6.
* **07.11.16:** - Move git clone internal to the container,point config, database and log to use same locations for existing users.
* **14.10.16:** - Add version layer information.
* **09.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README.
* **08.08.16:** - Rebase to alpine linux.
* **25.01.16:** - Initial Release.

