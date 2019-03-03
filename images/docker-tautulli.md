# [linuxserver/tautulli](https://github.com/linuxserver/docker-tautulli)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/tautulli.svg)](https://microbadger.com/images/linuxserver/tautulli "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/tautulli.svg)](https://microbadger.com/images/linuxserver/tautulli "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/tautulli.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/tautulli.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-tautulli/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-tautulli/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/tautulli/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/tautulli/latest/index.html)

[Tautulli](http://tautulli.com) is a python based web application for monitoring, analytics and notifications for Plex Media Server.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/tautulli` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :----: | --- |
| latest | Stable Tautulli releases |
| develop | Built at head of Tautulli nightly branch |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=tautulli \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8181:8181 \
  -v <path to data>:/config \
  -v <path to plex logs>:/logs \
  --restart unless-stopped \
  linuxserver/tautulli
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  tautulli:
    image: linuxserver/tautulli
    container_name: tautulli
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <path to plex logs>:/logs
    ports:
      - 8181:8181
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8181` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains tautulli config and database. |
| `/logs` | Map this to Plex log directory - recommended RO. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `<your-ip>:8181`, for more information check out [Tautulli](http://tautulli.com).
In tautulli gui settings, under `Plex Media Server`, turn on `Show Advanced` and set the `Logs Folder` to `/logs`



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it tautulli /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f tautulli`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' tautulli`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/tautulli`

## Versions

* **22.02.19:** - Rebasing to alpine 3.9.
* **26.01.19:** - Add pipeline logic and multi arch.
* **23.10.18:** - Update plex logs info in readm.
* **16.08.18:** - Rebase to alpine 3.8.
* **10.03.18:** - Rebrand to tautulli.
* **12.12.17:** - Rebase to alpine 3.7.
* **21.07.17:** - Internal git pull instead of at runtime.
* **12.07.17:** - Add inspect commands to README, move to jenkins build and push.
* **25.05.17:** - Rebase to alpine 3.6.
* **20.04.17:** - Add pycryptodomex pip package.
* **07.02.17:** - Rebase to alpine 3.5.
* **09.09.16:** - Add layer badges to README.
* **27.08.16:** - Add badges to README.
* **08.08.16:** - Rebase to alpine linux.
* **16.07.15:** - Inital Release.
