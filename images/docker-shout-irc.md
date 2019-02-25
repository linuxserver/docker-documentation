# [linuxserver/shout-irc](https://github.com/linuxserver/docker-shout-irc)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/shout-irc.svg)](https://microbadger.com/images/linuxserver/shout-irc "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/shout-irc.svg)](https://microbadger.com/images/linuxserver/shout-irc "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/shout-irc.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/shout-irc.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-shout-irc/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-shout-irc/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/shout-irc/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/shout-irc/latest/index.html)

[Shout-irc](http://shout-irc.com/) is a web IRC client that you host on your own server.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/shout-irc` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=shout-irc \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=Europe/London \
  -p 9000:9000 \
  -v </path/to/appdata/config>:/config \
  --restart unless-stopped \
  linuxserver/shout-irc
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  shout-irc:
    image: linuxserver/shout-irc
    container_name: shout-irc
    environment:
      - PUID=1001
      - PGID=1001
      - TZ=Europe/London
    volumes:
      - </path/to/appdata/config>:/config
    ports:
      - 9000:9000
    mem_limit: 4096m
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `9000` | Application WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1001` | for UserID - see below for explanation |
| `PGID=1001` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Configuration files. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1001` and `PGID=1001`, to find yours use `id user` as below:

```
  $ id username
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Application Setup

 * To log in to the application, browse to https://<hostip>:9000. * To setup user account(s) edit `/config/config.json` * Change the value `public: true,` to `public: false,` * restart the container and enter the following from the command line of the host: * `docker exec -it thelounge thelounge add <user>` * Enter a password when prompted, refresh your browser. * You should now be prompted for a password on the webinterface. 


## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it shout-irc /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f shout-irc`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' shout-irc`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/shout-irc`

## Versions

* **22.02.19:** - Rebasing to alpine 3.9.
* **28.01.19:** - Add pipeline logic and multi arch.
* **25.08.18:** - Rebase to alpine 3.8.
* **13.12.17:** - Rebase to alpine 3.7.
* **27.05.17:** - Rebase to alpine 3.6.
* **09.02.17:** - Rebase to alpine 3.5.
* **14.10.16:** - Add version layer information.
* **31.08.16:** - Rebase to alpine linux, move to lsiocommunity
