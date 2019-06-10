# [linuxserver/pyload](https://github.com/linuxserver/docker-pyload)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/pyload.svg)](https://microbadger.com/images/linuxserver/pyload "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/pyload.svg)](https://microbadger.com/images/linuxserver/pyload "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/pyload.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/pyload.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-pyload/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-pyload/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/pyload/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/pyload/latest/index.html)

[Pyload](https://pyload.net/) is a Free and Open Source download manager written in Python and designed to be extremely lightweight, easily extensible and fully manageable via web.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/pyload` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
version: "2"
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

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8000` | Allows HTTP access to the application |
| `7227` | pyLoad control port |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | pyLoad Configuration and files database |
| `/downloads` | Destination of pyLoad downloads |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the web interface at `http://your-ip:8000` the default login is: 
username - **admin**
password - **password**

For general usage please see the pyLoad wiki [here](https://github.com/pyload/pyload/wiki) .



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

* **08.06.19:** - Initial release.
