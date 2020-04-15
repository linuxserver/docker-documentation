# [linuxserver/nzbhydra2](https://github.com/linuxserver/docker-nzbhydra2)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-nzbhydra2.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nzbhydra2)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-nzbhydra2.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nzbhydra2/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nzbhydra2/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-nzbhydra2/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/nzbhydra2)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/nzbhydra2.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/nzbhydra2 "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/nzbhydra2.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/nzbhydra2)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/nzbhydra2.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/nzbhydra2)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-nzbhydra2/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-nzbhydra2/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nzbhydra2/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nzbhydra2/latest/index.html)

[Nzbhydra2](https://github.com/theotherp/nzbhydra2) is a meta search application for NZB indexers, the "spiritual successor" to NZBmegasearcH, and an evolution of the original application [NZBHydra](https://github.com/theotherp/nzbhydra).

It provides easy access to a number of raw and newznab based indexers. The application NZBHydra 2 is replacing NZBHydra 1 and supports migrating from V1. Be wary that there may be some compatibility issues for those migrating from V1 to V2, so ensure you back up your old configuration before moving over to the new version. **NOTE:** The last version that supports migration is `linuxserver/nzbhydra2:v2.10.2-ls49`


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/nzbhydra2` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :----: | --- |
| latest | Stable releases |
| dev | Prereleases from their GitHub |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=nzbhydra2 \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 5076:5076 \
  -v <path to data>:/config \
  -v <nzb download>:/downloads \
  --restart unless-stopped \
  linuxserver/nzbhydra2
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  nzbhydra2:
    image: linuxserver/nzbhydra2
    container_name: nzbhydra2
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <nzb download>:/downloads
    ports:
      - 5076:5076
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `5076` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where nzbhydra2 should store config files. |
| `/downloads` | NZB download folder. |




## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

The web interface is at `<your ip>:5076` , to set up indexers and connections to your nzb download applications.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27nzbhydra2%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=nzbhydra2 "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it nzbhydra2 /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f nzbhydra2`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' nzbhydra2`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/nzbhydra2`

## Versions

* **14.04.20:** - Correct Name, Hydra2 -> NZBHydra2.
* **08.01.20:** - Switch to python3.
* **05.01.20:** - Add dev tag for prereleases.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **11.02.19:** - Add pipeline logic and multi arch.
* **18.08.18:** - Bump java version to 10, (bionic currently refers to it as version 11).
* **10.08.18:** - Rebase to ubuntu bionic.
* **15.04.18:** - Change to port 5076 in the Dockerfile.
* **11.01.18:** - Initial Release.
