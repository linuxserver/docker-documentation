# linuxserver/guacd

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-guacd.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-guacd/releases) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/guacd.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/guacd) [![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/guacd.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/guacd) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/guacd.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/guacd) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/guacd.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/guacd) [![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-guacd/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-guacd/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/guacd/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/guacd/latest/index.html)

[Guacd](https://guacamole.apache.org/) - Apache Guacamole is a clientless remote desktop gateway. It supports standard protocols like VNC, RDP, and SSH. This container is only the backend server component needed to use The official or 3rd party HTML5 frontends.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/guacd` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :---: | :--- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=guacd \
  -p 4822:4822 \
  --restart unless-stopped \
  linuxserver/guacd
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  guacd:
    image: linuxserver/guacd
    container_name: guacd
    ports:
      - 4822:4822
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `4822` | Port Guacamole server listens on |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |


### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |


## Application Setup

This is a backend only service, to leverage Guacd server you need to use either the official Java frontend [guacamole-client](https://github.com/apache/guacamole-client) or an open source alterantive like [guacamole-lite](https://github.com/vadimpronin/guacamole-lite).

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it guacd /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f guacd`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' guacd`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/guacd`

## Versions

* **25.05.19:** - Initial Release.

