# [linuxserver/raneto](https://github.com/linuxserver/docker-raneto)

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-raneto.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-raneto/releases)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/raneto.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/raneto "Get your own version badge on microbadger.com")
[![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/raneto.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/raneto "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/raneto.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/raneto)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/raneto.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/raneto)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-raneto/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-raneto/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/raneto/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/raneto/latest/index.html)

[Raneto](http://raneto.com/) - is an open source Knowledgebase platform that uses static Markdown files to power your Knowledgebase.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/raneto` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=raneto \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 3000:3000 \
  -v /path/to/appdata:/config \
  --restart unless-stopped \
  linuxserver/raneto
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  raneto:
    image: linuxserver/raneto
    container_name: raneto
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /path/to/appdata:/config
    ports:
      - 3000:3000
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3000` | The port for the Raneto web interface |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Raneto config and Markdown files |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at http://<your-ip>:3000

The default username and password is *admin/password*

This application can only be configured through file storage the web interface is only for editing Markdown files.
You need to understand the following paths and the role they play for the application:

* /config/config.default.js - Main configuration file to setup your user, site name, etc.
* /config/content - All of your Markdown files go here [more info](http://docs.raneto.com/usage/creating-pages).
* /config/images - This folder will serve content on http://<your-ip>:3000/images/<image name>.png you can put anything in here but it is specifically for image files so you can embed them in your Markdown files without using external hosting.



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it raneto /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f raneto`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' raneto`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/raneto`

## Versions

* **28.06.19:** - Rebasing to alpine 3.10.
* **01.06.19:** - Initial Release.
