# [linuxserver/codiad](https://github.com/linuxserver/docker-codiad)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/codiad.svg)](https://microbadger.com/images/linuxserver/codiad "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/codiad.svg)](https://microbadger.com/images/linuxserver/codiad "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/codiad.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/codiad.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-codiad/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-codiad/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/codiad/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/codiad/latest/index.html)

[Codiad](http://codiad.com/) is a web-based IDE framework with a small footprint and minimal requirements. We have added a few plugins. More can be added in the marketplace in the WebUI.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/codiad` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=codiad \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 80:80 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/codiad
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  codiad:
    image: linuxserver/codiad
    container_name: codiad
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
    ports:
      - 80:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where Codiad stores data. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it codiad /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f codiad`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' codiad`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/codiad`

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9, adding ssh client.
* **16.01.19:** - Add pipeline logic and multi arch.
* **26.09.18:** - Add sed to init file to configure projects folder correctly.
* **04.09.18:** - Rebase to alpine linux 3.8.
* **09.01.18:** - Rebase to alpine linux 3.7.
* **25.05.17:** - Rebase to alpine linux 3.6.
* **18.02.17:** - Rebase to alpine linux 3.5.
* **14.10.16:** - Add version layer information.
* **10.09.16:** - Add layer badges to README.
* **06.11.15:** - Initial Release.
