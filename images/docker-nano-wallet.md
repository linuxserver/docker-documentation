# [linuxserver/nano-wallet](https://github.com/linuxserver/docker-nano-wallet)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-nano-wallet.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nano-wallet)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-nano-wallet.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nano-wallet/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nano-wallet/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-nano-wallet/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/nano-wallet)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/nano-wallet.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/nano-wallet "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/nano-wallet.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/nano-wallet)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/nano-wallet.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/nano-wallet)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-nano-wallet/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-nano-wallet/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nano-wallet/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nano-wallet/latest/index.html)

[Nano-wallet](https://nano.org/) is a digital payment protocol designed to be accessible and lightweight, with a focus on removing inefficiencies present in other cryptocurrencies. With ultrafast transactions and zero fees on a secure, green and decentralized network, this makes Nano ideal for everyday transactions.

This container is a simple nginx wrapper for the light wallet located [here](https://github.com/linuxserver/nano-wallet). You will need to pass a valid RPC host when accessing this container.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/nano-wallet` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=nano-wallet \
  -p 80:80 \
  --restart unless-stopped \
  linuxserver/nano-wallet
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  nano-wallet:
    image: linuxserver/nano-wallet
    container_name: nano-wallet
    ports:
      - 80:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | Webserver port |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |




## Application Setup


This container requires a Nano RPC endpoint to communicate with whether a public network or your own, see [here](https://hub.docker.com/r/linuxserver/nano) for more information.

Simply access the container at the URL:

http://localhost/#/THE_IP_OR_HOSTNAME_OF_RPC_ENDPOINT


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27nano-wallet%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=nano-wallet "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it nano-wallet /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f nano-wallet`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' nano-wallet`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/nano-wallet`

## Versions

* **23.05.20:** - Initial Release.
