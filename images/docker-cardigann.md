# [linuxserver/cardigann](https://github.com/linuxserver/docker-cardigann)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-cardigann.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-cardigann)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-cardigann.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-cardigann/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-cardigann/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-cardigann/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/cardigann)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/cardigann.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/cardigann "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/cardigann.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/cardigann)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/cardigann.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/cardigann)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-cardigann/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-cardigann/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/cardigann/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/cardigann/latest/index.html)

THIS IMAGE IS DEPRECATED. We will no longer be making updates or rebuilding this image. The Dockerhub endpoint will stay online with the current tags for this software. We recommend current users switch to linuxserver/jackett.
[Cardigann](https://github.com/cardigann/cardigann) a server for adding extra indexers to Sonarr, SickRage and CouchPotato via Torznab and TorrentPotato proxies. Behind the scenes Cardigann logs in and runs searches and then transforms the results into a compatible format.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/cardigann` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=cardigann \
  -e PUID=1000 \
  -e PGID=1000 \
  -e SOCKS_PROXY=IP:PORT \
  -e HTTP_PROXY=IP:PORT \
  -p 5060:5060 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/cardigann
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  cardigann:
    image: linuxserver/cardigann
    container_name: cardigann
    environment:
      - PUID=1000
      - PGID=1000
      - SOCKS_PROXY=IP:PORT
      - HTTP_PROXY=IP:PORT
    volumes:
      - <path to data>:/config
    ports:
      - 5060:5060
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `5060` | The port for the Cardigann webinterface |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `SOCKS_PROXY=IP:PORT` | for using a socks proxy (optional) |
| `HTTP_PROXY=IP:PORT` | for using a HTTP proxy (optional) |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Cardigann config |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `<your-ip>:5060`, for more information check out [Cardigann](https://github.com/cardigann/cardigann).

By adding a variable to the run command, `SOCKS_PROXY` or `HTTP_PROXY` cardigann can be used with a proxy, *eg* `-e SOCKS_PROXY=localhost:1080`

The folder `/config/definitions` can be used to add additional tracker definitions (for more info see [Additional definitions](https://github.com/cardigann/cardigann#definitions) ).



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it cardigann /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f cardigann`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' cardigann`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/cardigann`

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **01.02.19:** - Multi arch images and pipeline build logic
* **14.01.19:** - Add multi arch and pipeline logic
* **22.08.18:** - Rebase to alpine 3.8
* **06.05.18:** - Use buildstage in Dockerfile
* **06.12.17:** - Rebase to alpine 3.7
* **12.08.17:** - Add npm install to build stage
* **25.05.17:** - Rebase to alpine 3.6
* **07.02.17:** - Rebase to alpine 3.5
* **03.11.16:** - Compiled using [sstamoulis'](https://github.com/sstamoulis) method
* **01.11.16:** - Initial Release
