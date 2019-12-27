# [linuxserver/pydio-cells](https://github.com/linuxserver/docker-pydio-cells)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-pydio-cells.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pydio-cells)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-pydio-cells.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pydio-cells/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pydio-cells/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-pydio-cells/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/pydio-cells)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/pydio-cells.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/pydio-cells "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/pydio-cells.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/pydio-cells)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/pydio-cells.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/pydio-cells)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-pydio-cells/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-pydio-cells/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/pydio-cells/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/pydio-cells/latest/index.html)

[Pydio-cells](https://pydio.com/) is the nextgen file sharing platform for organizations. It is a full rewrite of the Pydio project using the Go language following a micro-service architecture.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/pydio-cells` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=pydio-cells \
  --hostname=pydio-cells \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e EXTERNALURL=yourdomain.url \
  -p 8080:8080 \
  -v </path/to/appdata/config>:/config \
  --restart unless-stopped \
  linuxserver/pydio-cells
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  pydio-cells:
    image: linuxserver/pydio-cells
    container_name: pydio-cells
    hostname: pydio-cells
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - EXTERNALURL=yourdomain.url
    volumes:
      - </path/to/appdata/config>:/config
    ports:
      - 8080:8080
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8080` | Http port |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `EXTERNALURL=yourdomain.url` | The external url you would like to use to access Pydio Cells (Can be https://domain.url or http://IP:PORT). |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | All the config files reside here. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

You must first create a mysql database for Pydio Cells. Using our [mariadb image](https://hub.docker.com/r/linuxserver/mariadb) is recommended.  



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it pydio-cells /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f pydio-cells`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' pydio-cells`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/pydio-cells`

## Versions

* **19.12.19:** - Rebasing to alpine 3.11.
* **12.12.19:** - Initial Release
