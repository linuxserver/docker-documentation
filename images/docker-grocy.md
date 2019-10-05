# [linuxserver/grocy](https://github.com/linuxserver/docker-grocy)

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-grocy.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-grocy/releases)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/grocy.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/grocy "Get your own version badge on microbadger.com")
[![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/grocy.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/grocy "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/grocy.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/grocy)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/grocy.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/grocy)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-grocy/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-grocy/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/grocy/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/grocy/latest/index.html)

[Grocy](https://github.com/grocy/grocy) is an ERP system for your kitchen! Cut down on food waste, and manage your chores with this brilliant utulity.

Keep track of your purchaes, how much food you are wasting, what chores need doing and what batteries need charging with this proudly Open Source tool

For more information on grocy visit their website and check it out: https://grocy.info


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/grocy` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=grocy \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=<your timezone, eg Europe/London> \
  -p 9283:80 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/grocy
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  grocy:
    image: linuxserver/grocy
    container_name: grocy
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=<your timezone, eg Europe/London>
    volumes:
      - <path to data>:/config
    ports:
      - 9283:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | will map the container's port 80 to port 9283 on the host |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=<your timezone, eg Europe/London>` | for specifying your timezone |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | this will store any uploaded data on the docker host |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Grocy is simple to get running. Configure the container with the above instructions, start it, and you can then access it
by visiting http://your.ip:9283 - once the page loads, you can log in with the default username and password of admin / admin



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it grocy /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f grocy`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' grocy`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/grocy`

## Versions

* **22.09.19:** - Add 'gd' PHP extension.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **27.12.18:** - Initial Release.
