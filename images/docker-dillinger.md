# [linuxserver/dillinger](https://github.com/linuxserver/docker-dillinger)

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-dillinger.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-dillinger/releases)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/dillinger.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/dillinger "Get your own version badge on microbadger.com")
[![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/dillinger.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/dillinger "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/dillinger.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/dillinger)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/dillinger.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/dillinger)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-dillinger/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-dillinger/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/dillinger/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/dillinger/latest/index.html)

[Dillinger](https://github.com/joemccann/dillinger) is a cloud-enabled, mobile-ready, offline-storage, AngularJS powered HTML5 Markdown editor.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/dillinger` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=dillinger \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8080:8080 \
  -v <path to configs>:/config \
  --restart unless-stopped \
  linuxserver/dillinger
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  dillinger:
    image: linuxserver/dillinger
    container_name: dillinger
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to configs>:/config
    ports:
      - 8080:8080
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8080` | The port for the Dillinger web interface |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Dillinger plugin config files |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at http://your-ip:8080 , keep in mind that storage for this application is in your browser session not server side. Only plugin configurations will ever be stored server side. 



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it dillinger /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f dillinger`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' dillinger`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/dillinger`

## Versions

* **31.05.19:** - Initial Release.
