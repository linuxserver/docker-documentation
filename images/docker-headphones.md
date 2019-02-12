# [linuxserver/headphones](https://github.com/linuxserver/docker-headphones)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/headphones.svg)](https://microbadger.com/images/linuxserver/headphones "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/headphones.svg)](https://microbadger.com/images/linuxserver/headphones "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/headphones.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/headphones.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-headphones/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-headphones/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/headphones/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/headphones/latest/index.html)

[Headphones](https://github.com/rembo10/headphones) is an automated music downloader for NZB and Torrent, written in Python. It supports SABnzbd, NZBget, Transmission, µTorrent and Blackhole.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list). 

Simply pulling `linuxserver/headphones` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=headphones \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=Europe/London \
  -p 8181:8181 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/downloads>:/downloads \
  -v </path/to/music>:/music \
  --restart unless-stopped \
  linuxserver/headphones
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  headphones:
    image: linuxserver/headphones
    container_name: headphones
    environment:
      - PUID=1001
      - PGID=1001
      - TZ=Europe/London
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/downloads>:/downloads
      - </path/to/music>:/music
    ports:
      - 8181:8181
    mem_limit: 4096m
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8181` | Application WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1001` | for UserID - see below for explanation |
| `PGID=1001` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Configuration files. |
| `/downloads` | ISOs. |
| `/music` | Your music directory. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1001` and `PGID=1001`, to find yours use `id user` as below:

```
  $ id username
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it headphones /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f headphones`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' headphones`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/headphones`

## Versions

* **16.01.19:** - Add pipeline logic and multi arch.
* **18.08.18:** - Rebase to alpine 3.8.
* **03.04.18:** - Remove forced port and update README.
* **05.01.18:** - Deprecate cpu_core routine lack of scaling.
* **12.12.17:** - Rebase to alpine 3.7.
* **20.07.17:** - Internal git pull instead of at runtime.
* **12.07.17:** - Add inspect commands to README, move to jenkins build and push.
* **28.05.17:** - Add flac package to handle FLAC based .cue.
* **25.05.17:** - Rebase to alpine 3.6.
* **03.05.17:** - Reduce layer, replace broken source for shntool.
* **07.02.17:** - Rebase to alpine 3.5.
* **23.12.16:** - Fix capitalisation in README.
* **09.09.16:** - Add layer badges to README.
* **27.08.16:** - Add badges to README, compile shntool.
* **08.08.16:** - Rebase to alpine linux.
* **18.07.15:** - Inital Release
