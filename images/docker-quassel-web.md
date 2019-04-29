# [linuxserver/quassel-web](https://github.com/linuxserver/docker-quassel-web)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/quassel-web.svg)](https://microbadger.com/images/linuxserver/quassel-web "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/quassel-web.svg)](https://microbadger.com/images/linuxserver/quassel-web "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/quassel-web.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/quassel-web.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-quassel-web/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-quassel-web/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/quassel-web/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/quassel-web/latest/index.html)

[Quassel-web](https://github.com/magne4000/quassel-webserver) is a web client for Quassel.  Note that a Quassel-Core instance is required, we have a container available [here.](https://hub.docker.com/r/linuxserver/quassel-core/) 


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/quassel-web` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=quassel-web \
  -e PUID=1000 \
  -e PGID=1000 \
  -e QUASSEL_CORE=192.168.1.10 \
  -e QUASSEL_PORT=4242 \
  -e URL_BASE=/quassel \
  -e HTTPS=true \
  -e FORCE_DEFAULT=false \
  -p 64080:64080 \
  -p 64443:64443 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/quassel-web
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  quassel-web:
    image: linuxserver/quassel-web
    container_name: quassel-web
    environment:
      - PUID=1000
      - PGID=1000
      - QUASSEL_CORE=192.168.1.10
      - QUASSEL_PORT=4242
      - URL_BASE=/quassel
      - HTTPS=true
      - FORCE_DEFAULT=false
    volumes:
      - <path to data>:/config
    ports:
      - 64080:64080
      - 64443:64443
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `64080` | will map the container's port 64080 to port 64080 on the host |
| `64443` | will map the container's port 64443 to port 64443 on the host |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `QUASSEL_CORE=192.168.1.10` | specify the URL or IP address of your Quassel Core instance |
| `QUASSEL_PORT=4242` | specify the port of your Quassel Core instance |
| `URL_BASE=/quassel` | Specify a url-base in reverse proxy setups ie. `/quassel` |
| `HTTPS=true` | specify `true` to use https on `64443` or false to use http on `64080` |
| `FORCE_DEFAULT=false` | specify `true` to use only the default instance of Quassel Core specified above |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | this will store config on the docker host |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

By default this container webui will be available on `https://$SERVER_IP:64443`.  To setup this container you can either use the environmental variables as specified above and these will overwrite the respective settings in `/config/settings-user.js` or omit the environmental variables and edit `/config/settings-user.js` directly.



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it quassel-web /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f quassel-web`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' quassel-web`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/quassel-web`

## Versions

* **28.04.19:** - Initial Release.
