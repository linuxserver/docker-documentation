# [linuxserver/bazarr](https://github.com/linuxserver/docker-bazarr)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/bazarr.svg)](https://microbadger.com/images/linuxserver/bazarr "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/bazarr.svg)](https://microbadger.com/images/linuxserver/bazarr "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/bazarr.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/bazarr.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-bazarr/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-bazarr/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/bazarr/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/bazarr/latest/index.html)

[Bazarr](https://github.com/morpheus65535/bazarr) is a companion application to Sonarr and Radarr. It can manage and download subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you.

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
  -p 6767:6767 \
  -v </path/to/bazarr/config>:/config \
  -v </path/to/movies>:/movies \
  -v </path/to/tv:/tv \
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
version: "2"
services:
  bazarr:
    image: linuxserver/bazarr
    container_name: bazarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/bazarr/config>:/config
      - </path/to/movies>:/movies
      - </path/to/tv:/tv
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

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **11.09.18:** - Initial release.
