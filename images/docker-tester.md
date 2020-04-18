# [linuxserver/tester](https://github.com/linuxserver/docker-tester)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-tester.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-tester)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-tester.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-tester/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-tester/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-tester/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/tester)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/tester.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/tester "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/tester.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/tester)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/tester.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/tester)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-tester/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-tester/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/tester/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/tester/latest/index.html)

This internal tool is used as a desktop sandbox in our CI process to grab a screenshot of a hopefully functional endpoint

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/tester` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=tester \
  -e URL=http://google.com \
  -p 3000:3000 \
  --restart unless-stopped \
  linuxserver/tester
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  tester:
    image: linuxserver/tester
    container_name: tester
    environment:
      - URL=http://google.com
    ports:
      - 3000:3000
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3000` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `URL=http://google.com` | Specify an endpoint, the container will automatically determine the correct protocol and program to use |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |





## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27tester%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=tester "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it tester /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f tester`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' tester`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/tester`

## Versions

* **18.04.20:** - Initial release.
