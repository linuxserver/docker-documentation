# [linuxserver/minetest](https://github.com/linuxserver/docker-minetest)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/minetest.svg)](https://microbadger.com/images/linuxserver/minetest "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/minetest.svg)](https://microbadger.com/images/linuxserver/minetest "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/minetest.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/minetest.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-minetest/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-minetest/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/minetest/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/minetest/latest/index.html)

[Minetest](http://www.minetest.net/) (server) is a near-infinite-world block sandbox game and a game engine, inspired by InfiniMiner, Minecraft, and the like.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/minetest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=minetest \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e CLI_ARGS="--gameid minetest" `#optional` \
  -p 30000:30000/udp \
  -v <path to data>:/config/.minetest \
  --restart unless-stopped \
  linuxserver/minetest
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  minetest:
    image: linuxserver/minetest
    container_name: minetest
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - CLI_ARGS="--gameid minetest" #optional
    volumes:
      - <path to data>:/config/.minetest
    ports:
      - 30000:30000/udp
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `30000/udp` | Port Minetest listens on. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `CLI_ARGS="--gameid minetest"` | Optionally specify any [CLI variables](https://wiki.minetest.net/Command_line) you want to launch the app with |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config/.minetest` | Where minetest stores config files and maps etc. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

You can find the world maps, mods folder and config files in /config/.minetest.

Client and server must be the same version, please browse the tags here to pull the appropriate version for your server:

https://hub.docker.com/r/linuxserver/minetest/tags



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it minetest /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f minetest`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' minetest`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/minetest`

## Versions

* **28.06.19:** - Rebasing to alpine 3.10.
* **03.06.19:** - Adding custom cli vars to options.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **04.03.19:** - Rebase to alpine 3.9 to compile 5.0.0 minetest with new build args.
* **14.01.19:** - Add pipeline logic and multi arch.
* **08.08.18:** - Rebase to alpine 3.8, build from latest release tag instead of master.
* **03.01.18:** - Deprecate cpu_core routine lack of scaling.
* **08.12.17:** - Rebase to alpine 3.7.
* **30.11.17:** - Use cpu core counting routine to speed up build time.
* **26.05.17:** - Rebase to alpine 3.6.
* **14.02.17:** - Rebase to alpine 3.5.
* **25.11.16:** - Rebase to alpine linux, move to main repo.
* **27.02.16:** - Bump to latest version.
* **19.02.16:** - Change port to UDP, thanks to slashopt for pointing this out.
* **15.02.16:** - Make minetest app a service.
* **01.02.16:** - Add lua-socket dependency.
* **06.11.15:** - Initial Release.
