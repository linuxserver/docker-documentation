# [linuxserver/medusa](https://github.com/linuxserver/docker-medusa)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/medusa.svg)](https://microbadger.com/images/linuxserver/medusa "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/medusa.svg)](https://microbadger.com/images/linuxserver/medusa "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/medusa.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/medusa.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-medusa/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-medusa/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/medusa/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/medusa/latest/index.html)

[Medusa](https://pymedusa.com/) is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/medusa` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=medusa \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8081:8081 \
  -v <path to data>:/config \
  -v <path to downloads>:/downloads \
  -v <path to tv shows>:/tv \
  --restart unless-stopped \
  linuxserver/medusa
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  medusa:
    image: linuxserver/medusa
    container_name: medusa
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <path to downloads>:/downloads
      - <path to tv shows>:/tv
    ports:
      - 8081:8081
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8081` | The port for the Medusa webui |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use e.g. Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Cardigann config |
| `/downloads` | Download location |
| `/tv` | TV Shows location |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Web interface is at `<your ip>:8081` , set paths for downloads, tv-shows to match docker mappings via the webui, for more information check out [Medusa](https://pymedusa.com/).



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it medusa /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f medusa`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' medusa`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/medusa`

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **14.01.19:** - Adding multi arch and pipeline logic
* **16.08.18:** - Rebase to alpine 3.8
* **08.12.17:** - Rebase to alpine 3.7
* **29.11.17:** - Add py-gdbm for subtitles support
* **26.10.17:** - Mediainfo moved from testing to community repo
* **10.10.17:** - Use repo version of mediainfo to shorten build time
* **05.08.17:** - Internal git pull instead of at runtime
* **25.05.17:** - Rebase to alpine 3.6
* **07.02.17:** - Rebase to alpine 3.5
* **02.01.17:** - Initial Release
