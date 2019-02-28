# [linuxserver/duplicati](https://github.com/linuxserver/docker-duplicati)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/duplicati.svg)](https://microbadger.com/images/linuxserver/duplicati "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/duplicati.svg)](https://microbadger.com/images/linuxserver/duplicati "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/duplicati.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/duplicati.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-duplicati/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-duplicati/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/duplicati/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/duplicati/latest/index.html)

[Duplicati](https://www.duplicati.com/) works with standard protocols like FTP, SSH, WebDAV as well as popular services like Microsoft OneDrive, Amazon Cloud Drive & S3, Google Drive, box.com, Mega, hubiC and many others.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/duplicati` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=duplicati \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=Europe/London \
  -p 8200:8200 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/backups>:/backups \
  -v </path/to/source>:/source \
  --restart unless-stopped \
  linuxserver/duplicati
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  duplicati:
    image: linuxserver/duplicati
    container_name: duplicati
    environment:
      - PUID=1001
      - PGID=1001
      - TZ=Europe/London
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/backups>:/backups
      - </path/to/source>:/source
    ports:
      - 8200:8200
    mem_limit: 4096m
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8200` | http gui |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1001` | for UserID - see below for explanation |
| `PGID=1001` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains all relevant configuration files. |
| `/backups` | Path to store local backups. |
| `/source` | Path to source for files to backup. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1001` and `PGID=1001`, to find yours use `id user` as below:

```
  $ id username
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Application Setup

The webui is at `<your ip>:8200` , create backup jobs etc via the webui, for local backups select `/backups` as the destination. For more information see [Duplicati](https://www.duplicati.com/).



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it duplicati /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f duplicati`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' duplicati`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/duplicati`

## Versions

* **11.01.19:** - Multi-arch image.
* **09.12.17:** - Fix continuation lines.
* **31.08.17:** - Build only beta or release versions (thanks deasmi).
* **24.04.17:** - Initial release.
