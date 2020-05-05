# [linuxserver/davos](https://github.com/linuxserver/docker-davos)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-davos.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-davos)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-davos.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-davos/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-davos/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-davos/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/davos)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/davos.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/davos "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/davos.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/davos)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/davos.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/davos)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-davos/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-davos/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/davos/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/davos/latest/index.html)

[Davos](https://github.com/linuxserver/davos) is an FTP automation tool that periodically scans given host locations for new files. It can be configured for various purposes, including listening for specific files to appear in the host location, ready for it to download and then move, if required. It also supports completion notifications as well as downstream API calls, to further the workflow.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/davos` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=davos \
  -e PUID=1000 \
  -e PGID=1000 \
  -p 8080:8080 \
  -v <path to data>:/config \
  -v <path to downloads folder>:/download \
  --restart unless-stopped \
  linuxserver/davos
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  davos:
    image: linuxserver/davos
    container_name: davos
    environment:
      - PUID=1000
      - PGID=1000
    volumes:
      - <path to data>:/config
      - <path to downloads folder>:/download
    ports:
      - 8080:8080
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8080` | This is the default port that davos runs under |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | davos's config location. This is where it stores its database file and logs. |
| `/download` | davos's file download location |




## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

The application does not require any set up other than starting the docker container. Further documentation can be found on the [davos GitHub repository page](https://github.com/linuxserver/davos).


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27davos%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=davos "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it davos /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f davos`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' davos`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/davos`

## Versions

* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.03.19:** - Updating runtime deps due to change in OpenJRE.
* **08.03.19:** - Updating build environment to pass proper build flags and use gradle wrapper.
* **22.02.19:** - Rebasing to alpine 3.9.
* **18.11.16:** - Initial Release.
