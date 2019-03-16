# linuxserver/sickrage

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn) [![](https://images.microbadger.com/badges/version/linuxserver/sickrage.svg)](https://microbadger.com/images/linuxserver/sickrage) [![](https://images.microbadger.com/badges/image/linuxserver/sickrage.svg)](https://microbadger.com/images/linuxserver/sickrage) ![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/sickrage.svg) ![Docker Stars](https://img.shields.io/docker/stars/linuxserver/sickrage.svg) [![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-sickrage/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-sickrage/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/sickrage/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/sickrage/latest/index.html)

[Sickrage](https://sick-rage.github.io/) is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/sickrage` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :---: | :--- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=sickrage \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8081:8081 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/downloads>:/downloads \
  -v </path/to/tv/shows>:/tv \
  --restart unless-stopped \
  linuxserver/sickrage
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  sickrage:
    image: linuxserver/sickrage
    container_name: sickrage
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/downloads>:/downloads
      - </path/to/tv/shows>:/tv
    ports:
      - 8081:8081
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `8081` | Application WebUI |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Configuration files. |
| `/downloads` | ISOs. |
| `/tv` | TV library directory. |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Web interface is at `<your ip>:8081` , set paths for downloads, tv-shows to match docker mappings via the webui.

## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it sickrage /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f sickrage`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' sickrage`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/sickrage`

## Versions

* **22.02.19:** - Rebasing to alpine 3.9.
* **16.01.19:** - Add pipeline logic and multi arch.
* **09.08.18:** - Change repository to Sick-Rage
* **17.08.18:** - Rebase to alpine 3.8.
* **20.03.18:** - In lieu of a definite fix from SR, add nodejs package for use with torrentz and other sources.
* **12.12.17:** - Rebase to alpine 3.7.
* **06.08.17:** - Internal git pull instead of at runtime.
* **25.05.17:** - Rebase to alpine 3.6.
* **07.02.17:** - Rebase to alpine 3.5.
* **14.10.16:** - Add version layer information.
* **30.09.16:** - Fix umask.
* **09.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README.
* **08.08.16:** - Rebase to alpine linux.
* **30.12.15:** - Build later version of unrar from source, removed uneeded mako package.
* **20.11.15:** - Updated to new repo, by SickRage Team.
* **15.10.15:** - Initial Release.

