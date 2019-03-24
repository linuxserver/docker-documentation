# [linuxserver/sabnzbd](https://github.com/linuxserver/docker-sabnzbd)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/sabnzbd.svg)](https://microbadger.com/images/linuxserver/sabnzbd "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/sabnzbd.svg)](https://microbadger.com/images/linuxserver/sabnzbd "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/sabnzbd.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/sabnzbd.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-sabnzbd/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-sabnzbd/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/sabnzbd/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/sabnzbd/latest/index.html)

[Sabnzbd](http://sabnzbd.org/) makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/sabnzbd` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :----: | --- |
| latest | Stable SABnzbd releases |
| unstable | Beta/Stable SABnzbd releases at edge |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=sabnzbd \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8080:8080 \
  -p 9090:9090 \
  -v <path to data>:/config \
  -v <path to downloads>:/downloads \
  -v <path to incomplete downloads>:/incomplete-downloads `#optional` \
  --restart unless-stopped \
  linuxserver/sabnzbd
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  sabnzbd:
    image: linuxserver/sabnzbd
    container_name: sabnzbd
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <path to downloads>:/downloads
    volumes:
      - <path to incomplete downloads>:/incomplete-downloads #optional
    ports:
      - 8080:8080
      - 9090:9090
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8080` | HTTP port for the WebUI. |
| `9090` | HTTPS port for the WebUI. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Local path for sabnzbd config files. |
| `/downloads` | Local path for finished downloads. |
| `/incomplete-downloads` | Local path for incomplete-downloads. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Initial setup is done from the http port.
Https access for sabnzbd needs to be enabled in either the intial setup wizard or in the configure settings of the webui, be sure to use 9090 as port for https.
See here for info on some of the switch settings for sabnzbd https://sabnzbd.org/wiki/configuration/2.3/switches .



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it sabnzbd /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f sabnzbd`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' sabnzbd`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/sabnzbd`

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **25.02.19:** - Rebase to Bionic, add python deps for scripts.
* **26.01.19:** - Add pipeline logic and multi arch.
* **13.12.17:** - Fix continuation lines.
* **12.07.17:** - Add inspect commands to README, move to jenkins build and push.
* **10.04.17:** - Bump to 2.0 Release.
* **25.02.17:** - Switch to nobetas repo for master/latest branch and add unstable branch.
* **08.02.17:** - Add pythonioenconding=utf8 as env.
* **15.09.16:** - Compile par2 multicore as per latest info sabnzbd git [readme](https://github.com/sabnzbd/sabnzbd#resolving-dependencies).
* **11.09.16:** - Bump to release of 1.10.
* **09.09.16:** - Rebase back to xenial, issues with alpine version of python and 1.10 branch of sab.
* **28.08.16:** - Rebase to alpine, using git version of sab.
* **17.03.16:** - Bump to install 1.0 final at startup.
* **14.03.16:** - Refresh image to pick up latest RC.
* **23.01.15:** - Refresh image.
* **14.12.15:** - Refresh image to pick up latest beta.
* **21.08.15:** - Initial Release.
