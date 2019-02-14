# [linuxserver/mylar](https://github.com/linuxserver/docker-mylar)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/mylar.svg)](https://microbadger.com/images/linuxserver/mylar "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/mylar.svg)](https://microbadger.com/images/linuxserver/mylar "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/mylar.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/mylar.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-mylar/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-mylar/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/mylar/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/mylar/latest/index.html)

[Mylar](https://github.com/evilhero/mylar) is an automated Comic Book downloader (cbr/cbz) for use with SABnzbd, NZBGet and torrents.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list). 

Simply pulling `linuxserver/mylar` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=mylar \
  -e PUID=1001 \
  -e PGID=1001 \
  -p 8090:8090 \
  -v <path to data>:/config \
  -v <comics-folder>:/comics \
  -v <downloads-folder>:/downloads \
  --restart unless-stopped \
  linuxserver/mylar
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  mylar:
    image: linuxserver/mylar
    container_name: mylar
    environment:
      - PUID=1001
      - PGID=1001
    volumes:
      - <path to data>:/config
      - <comics-folder>:/comics
      - <downloads-folder>:/downloads
    ports:
      - 8090:8090
    mem_limit: 4096m
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8090` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1001` | for UserID - see below for explanation |
| `PGID=1001` | for GroupID - see below for explanation |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where mylar should store config files. |
| `/comics` | Map to your comics folder. |
| `/downloads` | Map to your downloads folder. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1001` and `PGID=1001`, to find yours use `id user` as below:

```
  $ id username
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Application Setup

The web ui for settings etc, is on `<your-ip>:8090`
For more detailed setup refer [Mylar](https://github.com/evilhero/mylar).



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it mylar /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f mylar`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' mylar`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/mylar`

## Versions

* **11.02.19:** - Pipeline logic and multi arch.
* **17.08.18:** - Rebase to alpine 3.8.
* **06.07.18:** - Add `html5lib` python package.
* **14.06.18:** - Add `requests` python package.
* **12.12.17:** - Rebase to alpine 3.7.
* **21.07.17:** - Internal git pull instead of at runtime.
* **25.05.17:** - Rebase to alpine 3.6.
* **19.02.17:** - Use quiet option for cleaner console log, app logs to file anyways.
* **07.02.17:** - Rebase to alpine 3.5.
* **14.10.16:** - Add version layer information.
* **10.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README.
* **08.08.16:** - Rebase to alpine linux.
* **26.01.16:** - Initial release.
