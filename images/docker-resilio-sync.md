# [linuxserver/resilio-sync](https://github.com/linuxserver/docker-resilio-sync)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-resilio-sync.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-resilio-sync)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-resilio-sync.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-resilio-sync/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-resilio-sync/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-resilio-sync/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/resilio-sync)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/resilio-sync.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/resilio-sync "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/resilio-sync.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/resilio-sync)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/resilio-sync.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/resilio-sync)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-resilio-sync/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-resilio-sync/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/resilio-sync/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/resilio-sync/latest/index.html)

[Resilio-sync](https://www.resilio.com/individuals/) (formerly BitTorrent Sync) uses the BitTorrent protocol to sync files and folders between all of your devices. There are both free and paid versions, this container supports both. There is an official sync image but we created this one as it supports user mapping to simplify permissions for volumes.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/resilio-sync` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=resilio-sync \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e UMASK_SET=<022> \
  -p 8888:8888 \
  -p 55555:55555 \
  -v <path to config>:/config \
  -v <path to downloads>:/downloads \
  -v <path to data>:/sync \
  --restart unless-stopped \
  linuxserver/resilio-sync
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  resilio-sync:
    image: linuxserver/resilio-sync
    container_name: resilio-sync
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - UMASK_SET=<022>
    volumes:
      - <path to config>:/config
      - <path to downloads>:/downloads
      - <path to data>:/sync
    ports:
      - 8888:8888
      - 55555:55555
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8888` | WebUI |
| `55555` | Sync Port. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `UMASK_SET=<022>` | For umask setting of resilio-sync, default if left unset is 022. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where resilio-sync should store its config file. |
| `/downloads` | Folder for downloads/cache. |
| `/sync` | Sync folders root. |




## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

* Webui is at `<your-ip>:8888`, for account creation and configuration.
* More info on setup at [Resilio Sync](https://www.resilio.com/individuals/)


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27resilio-sync%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=resilio-sync "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it resilio-sync /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f resilio-sync`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' resilio-sync`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/resilio-sync`

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **11.02.19:** - Rebase to bionic, add pipeline logic and multi arch.
* **05.02.18:** - Add downloads volume mount.
* **28.01.18:** - Add /sync to dir whitelist.
* **26.01.18:** - Use variable for arch to bring in line with armhf arch repo.
* **15.12.17:** - Fix continuation lines.
* **02.06.17:** - Rebase to ubuntu xenial, alpine linux no longer works with resilio.
* **22.05.17:** - Add variable for user defined umask.
* **14.05.17:** - Use fixed version instead of latest, while 2.5.0 is broken on non glibc (alpine).
* **08.02.17:** - Rebase to alpine 3.5.
* **02.11.16:** - Initial Release.
