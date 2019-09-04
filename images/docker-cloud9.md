# [linuxserver/cloud9](https://github.com/linuxserver/docker-cloud9)

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-cloud9.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-cloud9/releases)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/cloud9.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/cloud9 "Get your own version badge on microbadger.com")
[![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/cloud9.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/cloud9 "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/cloud9.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/cloud9)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/cloud9.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/cloud9)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-cloud9/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-cloud9/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/cloud9/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/cloud9/latest/index.html)

[Cloud9](https://github.com/c9/core) Cloud9 is a complete web based IDE with terminal access. This container is for running their core SDK locally and developing plugins.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/cloud9` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | Docker and Compose environment pre-installed |
| go | Basic Golang environment pre-installed |
| nodejs | Current stable NodeJS/NPM environment pre-installed |
| python | Current Python3 environment pre-installed |
| ruby | Current Ruby environment pre-installed |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=cloud9 \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e GITURL=https://github.com/linuxserver/docker-cloud9.git `#optional` \
  -p 8000:8000 \
  -v <path to your code>:/code `#optional` \
  -v /var/run/docker.sock:/var/run/docker.sock `#optional` \
  --restart unless-stopped \
  linuxserver/cloud9
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  cloud9:
    image: linuxserver/cloud9
    container_name: cloud9
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - GITURL=https://github.com/linuxserver/docker-cloud9.git #optional
    volumes:
    volumes:
      - <path to your code>:/code #optional
      - /var/run/docker.sock:/var/run/docker.sock #optional
    ports:
      - 8000:8000
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8000` | The port for the Cloud9 web interface |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London, this is required for Radarr |
| `GITURL=https://github.com/linuxserver/docker-cloud9.git` | Specify a git repo to checkout on first startup |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/code` | Optionally if you want to mount up a local folder of code instead of checking out |
| `/var/run/docker.sock` | Needed if you plan to use Docker or compose commands |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at http://your-ip:8000, for more information check out [here](https://docs.c9.io/docs).



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it cloud9 /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f cloud9`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' cloud9`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/cloud9`

## Versions

* **02.06.19:** - Initial Release.
