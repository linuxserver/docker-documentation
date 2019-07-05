# [linuxserver/syncthing](https://github.com/linuxserver/docker-syncthing)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/syncthing.svg)](https://microbadger.com/images/linuxserver/syncthing "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/syncthing.svg)](https://microbadger.com/images/linuxserver/syncthing "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/syncthing.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/syncthing.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-syncthing/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-syncthing/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/syncthing/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/syncthing/latest/index.html)

[Syncthing](https://syncthing.net) replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/syncthing` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=syncthing \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e UMASK_SET=<022> \
  -p 8384:8384 \
  -p 22000:22000 \
  -p 21027:21027/udp \
  -v </path/to/appdata/config>:/config \
  -v </path/to/data1>:/data1 \
  -v </path/to/data2>:/data2 \
  --restart unless-stopped \
  linuxserver/syncthing
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  syncthing:
    image: linuxserver/syncthing
    container_name: syncthing
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - UMASK_SET=<022>
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/data1>:/data1
      - </path/to/data2>:/data2
    ports:
      - 8384:8384
      - 22000:22000
      - 21027:21027/udp
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8384` | Application WebUI |
| `22000` | Listening port |
| `21027/udp` | Protocol discovery |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `UMASK_SET=<022>` | Umask setting - [explaination](https://askubuntu.com/questions/44542/what-is-umask-and-how-does-it-work) |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Configuration files. |
| `/data1` | Data1 |
| `/data2` | Data2 |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

**Note: ** The Syncthing devs highly suggest setting a password for this container as it listens on 0.0.0.0. To do this go to `Actions -> Settings -> set user/password` for the webUI.


## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it syncthing /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f syncthing`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' syncthing`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/syncthing`

## Versions

* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **05.03.19:** - Update Build process for v1.1.0 release.
* **22.02.19:** - Rebasing to alpine 3.9.
* **16.01.19:** - Add pipeline logic and multi arch.
* **30.07.18:** - Rebase to alpine 3.8 and use buildstage.
* **13.12.17:** - Rebase to alpine 3.7.
* **25.10.17:** - Add env for manual setting of umask.
* **29.07.17:** - Simplify build structure as symlinks failing on > 0.14.32
* **28.05.17:** - Rebase to alpine 3.6.
* **08.02.17:** - Rebase to alpine 3.5.
* **01.11.16:** - Switch to compiling latest version from git source.
* **14.10.16:** - Add version layer information.
* **30.09.16:** - Fix umask.
* **09.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README.
* **11.08.16:** - Rebase to alpine linux.
* **18.12.15:** - Initial testing / release (IronicBadger)
* **24.09.15:** - Inital dev complete (Lonix)
