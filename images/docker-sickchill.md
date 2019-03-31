# [linuxserver/sickchill](https://github.com/linuxserver/docker-sickchill)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/sickchill.svg)](https://microbadger.com/images/linuxserver/sickchill "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/sickchill.svg)](https://microbadger.com/images/linuxserver/sickchill "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/sickchill.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/sickchill.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-sickchill/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-sickchill/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/sickchill/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/sickchill/latest/index.html)

[Sickchill](https://github.com/SickChill/SickChill) is an Automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic. 


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/sickchill` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=sickchill \
  -e PUID=1000 \
  -e PGID=1000 \
  -e PGID=<yourUID> \
  -e PUID=<yourGID> \
  -e TZ=<yourdbpass> \
  -p 8081:8081 \
  -v <path to data>:/config \
  -v <path to data>:/downloads \
  -v <path to data>:/tv \
  --restart unless-stopped \
  linuxserver/sickchill
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  sickchill:
    image: linuxserver/sickchill
    container_name: sickchill
    environment:
      - PUID=1000
      - PGID=1000
      - PGID=<yourUID>
      - PUID=<yourGID>
      - TZ=<yourdbpass>
    volumes:
      - <path to data>:/config
      - <path to data>:/downloads
      - <path to data>:/tv
    ports:
      - 8081:8081
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8081` | will map the container's port 8081 to port 8081 on the host |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `PGID=<yourUID>` | specify your UID |
| `PUID=<yourGID>` | specify your GID |
| `TZ=<yourdbpass>` | specify your TimeZone e.g. Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | this will store config on the docker host |
| `/downloads` | this will store any downloaded data on the docker host |
| `/tv` | this will allow sickchill to view what you already have |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Web interface is at `<your ip>:8081` , set paths for downloads, tv-shows to match docker mappings via the webui.



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it sickchill /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f sickchill`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' sickchill`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/sickchill`

## Versions

* **10.10.18:** - Initial Release.
