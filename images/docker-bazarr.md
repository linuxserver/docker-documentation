# [linuxserver/bazarr](https://github.com/linuxserver/docker-bazarr)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-bazarr.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-bazarr)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-bazarr.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-bazarr/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-bazarr/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-bazarr/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/bazarr)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/bazarr.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/bazarr "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/bazarr.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/bazarr)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/bazarr.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/bazarr)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-bazarr/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-bazarr/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/bazarr/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/bazarr/latest/index.html)

[Bazarr](https://www.bazarr.media/) is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/bazarr` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=bazarr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e UMASK_SET=022 `#optional` \
  -p 6767:6767 \
  -v </path/to/bazarr/config>:/config \
  -v </path/to/movies>:/movies \
  -v </path/to/tv>:/tv \
  --restart unless-stopped \
  linuxserver/bazarr
```

You can choose between ,using tags, various branch versions of bazarr, no tag is required to remain on the main branch.
Add one of the tags,  if required,  to the linuxserver/bazarr line of the run/create command in the following format, linuxserver/bazarr:development
The development tag will be the latest commit in the development branch of bazarr.
HOWEVER , USE THE DEVELOPMENT BRANCH AT YOUR OWN PERIL !!!!!!!!!


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  bazarr:
    image: linuxserver/bazarr
    container_name: bazarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - UMASK_SET=022 #optional
    volumes:
      - </path/to/bazarr/config>:/config
      - </path/to/movies>:/movies
      - </path/to/tv>:/tv
    ports:
      - 6767:6767
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `6767` | Allows HTTP access to the internal webserver. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `UMASK_SET=022` | control permissions of files and directories created by Bazarr |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Bazarr data |
| `/movies` | Location of your movies |
| `/tv` | Location of your TV Shows |




## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

- Once running the URL will be `http://<host-ip>:6767`.
- You must complete all the setup parameters in the webui before you can save the config.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27bazarr%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=bazarr "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it bazarr /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f bazarr`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' bazarr`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/bazarr`

## Versions

* **13.05.20:** - Add donation links for Bazarr to Github sponsors button and container log.
* **08.04.20:** - Removed /movies and /tv volumes from Dockerfiles.
* **28.12.19:** - Upgrade to Python 3.
* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **13.06.19:** - Add env variable for setting umask.
* **12.06.19:** - Swap to install deps using maintainers requirements.txt, add ffmpeg for ffprobe.
* **17.04.19:** - Add default UTC timezone if user does not set it.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **11.09.18:** - Initial release.
