# [linuxserver/hydra2](https://github.com/linuxserver/docker-hydra2)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/hydra2.svg)](https://microbadger.com/images/linuxserver/hydra2 "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/hydra2.svg)](https://microbadger.com/images/linuxserver/hydra2 "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/hydra2.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/hydra2.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-hydra2/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-hydra2/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/hydra2/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/hydra2/latest/index.html)

[Hydra2](https://github.com/theotherp/nzbhydra2) is a meta search application for NZB indexers, the "spiritual successor" to NZBmegasearcH, and an evolution of the original application [NZBHydra](https://github.com/theotherp/nzbhydra).

It provides easy access to a number of raw and newznab based indexers. The application NZBHydra 2 is currently in its early stages and is in active development. Be wary that there may be some compatibility issues for those migrating from V1 to V2, so ensure you back up your old configuration before moving over to the new version.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/hydra2` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=hydra2 \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=Europe/London \
  -p 5076:5076 \
  -v <path to data>:/config \
  -v <nzb download>:/downloads \
  --restart unless-stopped \
  linuxserver/hydra2
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  hydra2:
    image: linuxserver/hydra2
    container_name: hydra2
    environment:
      - PUID=1001
      - PGID=1001
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <nzb download>:/downloads
    ports:
      - 5076:5076
    mem_limit: 4096m
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `5076` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1001` | for UserID - see below for explanation |
| `PGID=1001` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where hydra2 should store config files. |
| `/downloads` | NZB download folder. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1001` and `PGID=1001`, to find yours use `id user` as below:

```
  $ id username
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Application Setup

The web interface is at `<your ip>:5076` , to set up indexers and connections to your nzb download applications.



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it hydra2 /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f hydra2`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' hydra2`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/hydra2`

## Versions

* **11.02.19:** - Add pipeline logic and multi arch.
* **18.08.18:** - Bump java version to 10, (bionic currently refers to it as version 11).
* **10.08.18:** - Rebase to ubuntu bionic.
* **15.04.18:** - Change to port 5076 in the Dockerfile.
* **11.01.18:** - Initial Release.
