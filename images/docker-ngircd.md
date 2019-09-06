# [linuxserver/ngircd](https://github.com/linuxserver/docker-ngircd)

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-ngircd.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-ngircd/releases)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/ngircd.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/ngircd "Get your own version badge on microbadger.com")
[![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/ngircd.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/ngircd "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/ngircd.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/ngircd)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/ngircd.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/ngircd)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-ngircd/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-ngircd/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ngircd/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ngircd/latest/index.html)

[Ngircd](https://ngircd.barton.de/) is a free, portable and lightweight Internet Relay Chat server for small or private networks, developed under the GNU General Public License (GPL). It is easy to configure, can cope with dynamic IP addresses, and supports IPv6, SSL-protected connections as well as PAM for authentication. It is written from scratch and not based on the original IRCd.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/ngircd` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=ngircd \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 6667:6667 \
  -v </path/to/ngircd/config>:/config \
  --restart unless-stopped \
  linuxserver/ngircd
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  ngircd:
    image: linuxserver/ngircd
    container_name: ngircd
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/ngircd/config>:/config
    ports:
      - 6667:6667
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `6667` | ngircd port |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use e.g. Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where `ngircd.conf` is stored |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

- To setup ngircd you will need to edit `/config/ngircd.conf` which is created the first time the container is run, edit the file and restart the container to implement any config changes.  
- For information see the ngircd site [here.](https://github.com/ngircd/ngircd/blob/master/doc/sample-ngircd.conf.tmpl)



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it ngircd /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f ngircd`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ngircd`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/ngircd`

## Versions

* **04.07.19:** - Initial release.
