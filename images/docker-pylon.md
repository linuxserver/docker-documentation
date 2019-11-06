# [linuxserver/pylon](https://github.com/linuxserver/docker-pylon)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-pylon.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pylon)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-pylon.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pylon/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pylon/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-pylon/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/pylon)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/pylon.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/pylon "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/pylon.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/pylon)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/pylon.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/pylon)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-pylon/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-pylon/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/pylon/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/pylon/latest/index.html)

[Pylon](https://github.com/pylonide/pylon) is a web based integrated development environment built with Node.js as a backend and with a supercharged JavaScript/HTML5 frontend, licensed under GPL version 3. This project originates from Cloud9 v2 project.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/pylon` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=pylon \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e GITURL=https://github.com/linuxserver/docker-pylon.git `#optional` \
  -e PYUSER=myuser `#optional` \
  -e PYPASS=mypass `#optional` \
  -p 3131:3131 \
  -v <path to your code>:/code `#optional` \
  --restart unless-stopped \
  linuxserver/pylon
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  pylon:
    image: linuxserver/pylon
    container_name: pylon
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - GITURL=https://github.com/linuxserver/docker-pylon.git #optional
      - PYUSER=myuser #optional
      - PYPASS=mypass #optional
    volumes:
    volumes:
      - <path to your code>:/code #optional
    ports:
      - 3131:3131
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3131` | The port for the Pylon web interface |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `GITURL=https://github.com/linuxserver/docker-pylon.git` | Specify a git repo to checkout on first startup |
| `PYUSER=myuser` | Specify a basic auth user. |
| `PYPASS=mypass` | Specify a basic auth password. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/code` | Optionally if you want the bind mount your own code and have changes survive container upgrades. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at http://your-ip:3131, more information [here](https://github.com/pylonide/pylon).



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it pylon /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f pylon`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' pylon`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/pylon`

## Versions

* **19.09.19:** - Initial Release.
