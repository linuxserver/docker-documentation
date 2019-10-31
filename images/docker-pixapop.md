# [lsiocommunity/pixapop](https://github.com/linuxserver/docker-pixapop)

[![GitHub Stars](https://img.shields.io/github/stars/lsiocommunity/docker-pixapop.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pixapop)
[![GitHub Release](https://img.shields.io/github/release/lsiocommunity/docker-pixapop.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pixapop/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pixapop/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-pixapop/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/pixapop)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/lsiocommunity/pixapop.svg?style=flat-square&color=E68523)](https://microbadger.com/images/lsiocommunity/pixapop "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/lsiocommunity/pixapop.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/lsiocommunity/pixapop)
[![Docker Stars](https://img.shields.io/docker/stars/lsiocommunity/pixapop.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/lsiocommunity/pixapop)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-pixapop/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-pixapop/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/lsiocommunity/pixapop/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/lsiocommunity/pixapop/latest/index.html)

[Pixapop](https://github.com/bierdok/pixapop) is an open-source single page application to view your photos in the easiest way possible.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lsiocommunity/pixapop` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=pixapop \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e APP_USERNAME=admin `#optional` \
  -e APP_PASSWORD=admin `#optional` \
  -p 80:80 \
  -v <path to config>:/config \
  -v <path to photos>:/photos \
  --restart unless-stopped \
  lsiocommunity/pixapop
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  pixapop:
    image: lsiocommunity/pixapop
    container_name: pixapop
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - APP_USERNAME=admin #optional
      - APP_PASSWORD=admin #optional
    volumes:
      - <path to config>:/config
      - <path to photos>:/photos
    ports:
      - 80:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `APP_USERNAME=admin` | Specify a username to enable authentication. |
| `APP_PASSWORD=admin` | Specify a password to enable authentication. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Stores config and logs for nginx base. |
| `/photos` | Your local folder of photos. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Any photos included in /photos will be presented as galleries split by month. Config settings are persistent and stored into /config.



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it pixapop /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f pixapop`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' pixapop`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' lsiocommunity/pixapop`

## Versions

* **18.03.19** - Update build dependencies
* **18.03.19** - Add build dependencies
* **17.03.19** - Initial release
