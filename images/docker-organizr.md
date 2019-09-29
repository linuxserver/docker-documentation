# linuxserver/organizr

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-organizr.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-organizr/releases) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/organizr.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/organizr) [![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/organizr.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/organizr) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/organizr.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/organizr) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/organizr.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/organizr) [![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-organizr/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-organizr/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/organizr/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/organizr/latest/index.html)

[Organizr](https://github.com/causefx/Organizr) is a HTPC/Homelab Services Organizer - Written in PHP

Do you have quite a bit of services running on your computer or server? Do you have a lot of bookmarks or have to memorize a bunch of ip's and ports? Well, Organizr is here to help with that. Organizr allows you to setup "Tabs" that will be loaded all in one webpage. You can then work on your server with ease. You can even open up two tabs side by side. Want to give users access to some Tabs? No problem, just enable user support and have them make an account. Want guests to be able to visit too? Enable Guest support for those tabs.

For more information on Organizr and information on how to use it visit their site at [https://github.com/causefx/Organizr](https://github.com/causefx/Organizr)

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/organizr` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=organizr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=<your timezone, eg Europe/London> \
  -p 9983:80 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/organizr
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  organizr:
    image: linuxserver/organizr
    container_name: organizr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=<your timezone, eg Europe/London>
    volumes:
      - <path to data>:/config
    ports:
      - 9983:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `80` | will map the container's port 80 to port 9983 on the host |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=<your timezone, eg Europe/London>` | for specifying your timezone |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | this is where your user data and logs will live |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Dead simple to get running, create the container as instructed and start it. When up and running, load the site.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it organizr /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f organizr`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' organizr`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/organizr`

## Versions

* **18.04.19:** - Fix new install not working.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **26.02.19:** - Upgrade packages during install to prevent mismatch with baseimage.
* **22.02.19:** - Rebasing to alpine 3.9.
* **11.02.19:** - Fix permissions on new app location
* **31.12.18:** - Moved to pipeline building from v1-master branch
* **05.09.18:** - Rebase to Alpine 3.8
* **10.01.18:** - Rebase to Alpine 3.7
* **25.05.17:** - Rebase to Alpine 3.6
* **02.05.17:** - Added php7-curl package
* **12.04.17:** - Added php7-ldap package
* **10.03.18:** - Initial Release.

