# [linuxserver/htpcmanager](https://github.com/linuxserver/docker-htpcmanager)

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-htpcmanager.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-htpcmanager/releases)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/htpcmanager.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/htpcmanager "Get your own version badge on microbadger.com")
[![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/htpcmanager.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/htpcmanager "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/htpcmanager.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/htpcmanager)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/htpcmanager.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/htpcmanager)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-htpcmanager/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-htpcmanager/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/htpcmanager/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/htpcmanager/latest/index.html)

[Htpcmanager](https://github.com/Hellowlol/HTPC-Manager) is a front end for many htpc related applications. Hellowlol version.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/htpcmanager` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=htpcmanager \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8085:8085 \
  -v </path/to/appdata/config>:/config \
  --restart unless-stopped \
  linuxserver/htpcmanager
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  htpcmanager:
    image: linuxserver/htpcmanager
    container_name: htpcmanager
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/appdata/config>:/config
    ports:
      - 8085:8085
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8085` | Application WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Configuration files. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

The webui is found at port 8085. Smartmontools has not been included, you can safely ignore the warning error in the log.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it htpcmanager /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f htpcmanager`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' htpcmanager`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/htpcmanager`

## Versions

* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **16.01.19:** - Add pipeline logic and multi arch.
* **17.08.18:** - Rebase to alpine 3.8.
* **12.12.17:** - Rebase to alpine 3.7.
* **20.07.17:** - Internal git pull instead of at runtime.
* **25.05.17:** - Rebase to alpine 3.6.
* **07.02.17:** - Rebase to alpine 3.5.
* **14.10.16:** - Add version layer information.
* **26.09.16:** - Add back cherrypy after removal from baseimage.
* **10.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README.
* **08.08.16:** - Rebase to alpine linux.
* **14.01.15:** - Remove hardcoded loglevel from the run command, set in webui
* **19.09.15:** - Initial Release.
