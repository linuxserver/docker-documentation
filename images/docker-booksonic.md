# linuxserver/booksonic

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-booksonic.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-booksonic) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-booksonic.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-booksonic/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-booksonic/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-booksonic/container_registry) [![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/booksonic) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/booksonic.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/booksonic) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/booksonic.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/booksonic) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/booksonic.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/booksonic) [![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-booksonic/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-booksonic/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/booksonic/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/booksonic/latest/index.html)

[Booksonic](http://booksonic.org) is a server and an app for streaming your audiobooks to any pc or android phone. Most of the functionality is also availiable on other platforms that have apps for subsonic.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/booksonic` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | Stable Booksonic releases |
| prerelease | Booksonic Pre-releases |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=booksonic \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e CONTEXT_PATH=url-base \
  -p 4040:4040 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/audiobooks>:/audiobooks \
  -v </path/to/podcasts>:/podcasts \
  -v </path/to/othermedia>:/othermedia \
  --restart unless-stopped \
  linuxserver/booksonic
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  booksonic:
    image: linuxserver/booksonic
    container_name: booksonic
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - CONTEXT_PATH=url-base
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/audiobooks>:/audiobooks
      - </path/to/podcasts>:/podcasts
      - </path/to/othermedia>:/othermedia
    ports:
      - 4040:4040
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `4040` | Application WebUI |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `CONTEXT_PATH=url-base` | Base url for use with reverse proxies etc. |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Configuration files. |
| `/audiobooks` | Audiobooks. |
| `/podcasts` | Podcasts. |
| `/othermedia` | Other media. |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Default user/pass is admin/admin

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27booksonic%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=booksonic)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it booksonic /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f booksonic`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' booksonic`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/booksonic`

## Versions

* **22.12.19:** - Revert to pulling in external war, upgrade jetty.
* **30.04.19:** - Switching to build war from source, use stable booksonic releases.
* **24.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **16.01.19:** - Adding pipeline logic and multi arch.
* **05.01.19:** - Linting fixes.
* **27.08.18:** - Rebase to ubuntu bionic.
* **06.12.17:** - Rebase to alpine 3.7.
* **11.07.17:** - Rebase to alpine 3.6.
* **07.02.17:** - Rebase to alpine 3.5.
* **13.12.16:** - Initial Release.

