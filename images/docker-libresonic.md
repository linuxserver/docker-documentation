# [linuxserver/libresonic](https://github.com/linuxserver/docker-libresonic)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/libresonic.svg)](https://microbadger.com/images/linuxserver/libresonic "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/libresonic.svg)](https://microbadger.com/images/linuxserver/libresonic "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/libresonic.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/libresonic.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-libresonic/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-libresonic/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/libresonic/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/libresonic/latest/index.html)

[Libresonic](https://github.com/Libresonic/libresonic) is a free, web-based media streamer, providing ubiqutious access to your music. Use it to share your music with friends, or to listen to your own music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/libresonic` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=libresonic \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e CONTEXT_PATH=<URL_BASE> `#optional` \
  -p 4040:4040 \
  -v </path/to/config>:/config \
  -v </path/to/music>:/music \
  -v </path/to/playlists>:/playlists \
  -v </path/to/podcasts>:/podcasts \
  -v </path/to/other media>:/media `#optional` \
  --restart unless-stopped \
  linuxserver/libresonic
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  libresonic:
    image: linuxserver/libresonic
    container_name: libresonic
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - CONTEXT_PATH=<URL_BASE> #optional
    volumes:
      - </path/to/config>:/config
      - </path/to/music>:/music
      - </path/to/playlists>:/playlists
      - </path/to/podcasts>:/podcasts
    volumes:
      - </path/to/other media>:/media #optional
    ports:
      - 4040:4040
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `4040` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `CONTEXT_PATH=<URL_BASE>` | For setting url-base in reverse proxy setups. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Configuration file location. |
| `/music` | Location of music. |
| `/playlists` | Location for playlists to be saved to. |
| `/podcasts` | Location of podcasts. |
| `/media` | Location of other media. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access WebUI at `<your-ip>:4040`.

Default user/pass is admin/admin



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it libresonic /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f libresonic`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' libresonic`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/libresonic`

## Versions

* **24.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **15.01.19:** - Pull war from github, adding pipeline multi arch builds.
* **05.01.19:** - Linting fixes.
* **27.08.18:** - Rebase to ubuntu bionic.
* **12.12.17:** - Rebase to alpine 3.7.
* **11.07.17:** - Rebase to alpine 3.6.
* **12.05.17:** - Add annotation timeout (primarily for armhf and lower powered hosts).
* **08.02.17:** - Rebase to alpine 3.5.
* **04.12.16:** - Update jetty runner version.
* **29.11.16:** - Switch to building from release tags following v6.1 stable release.
* **17.11.16:** - Initial Release.
