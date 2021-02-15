---
title: guacd
---
# [linuxserver/guacd](https://github.com/linuxserver/docker-guacd)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-guacd.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-guacd)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-guacd.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-guacd/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-guacd/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-guacd/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/guacd.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/guacd "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/guacd.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/guacd)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/guacd.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/guacd)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-guacd%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-guacd/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fguacd%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/guacd/latest/index.html)

[Guacd](https://guacamole.apache.org/) - Apache Guacamole is a clientless remote desktop gateway. It supports standard protocols like VNC, RDP, and SSH. This container is only the backend server component needed to use The official or 3rd party HTML5 frontends.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `ghcr.io/linuxserver/guacd` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker-compose ([recommended](https://docs.linuxserver.io/general/docker-compose))

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  guacd:
    image: ghcr.io/linuxserver/guacd
    container_name: guacd
    ports:
      - 4822:4822
    restart: unless-stopped
```

### docker cli

```
docker run -d \
  --name=guacd \
  -p 4822:4822 \
  --restart unless-stopped \
  ghcr.io/linuxserver/guacd
```


## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `4822` | Port Guacamole server listens on |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |



## Environment variables from files (Docker secrets)

You can set any environment variable from a file by using a special prepend `FILE__`.

As an example:

```
-e FILE__PASSWORD=/run/secrets/mysecretpassword
```

Will set the environment variable `PASSWORD` based on the contents of the `/run/secrets/mysecretpassword` file.

## Umask for running applications

For all of our images we provide the ability to override the default umask settings for services started within the containers using the optional `-e UMASK=022` setting.
Keep in mind umask is not chmod it subtracts from permissions based on it's value it does not add. Please read up [here](https://en.wikipedia.org/wiki/Umask) before asking for support.


## Application Setup

This is a backend only service, to leverage Guacd server you need to use either the official Java frontend [guacamole-client](https://github.com/apache/guacamole-client) or an open source alterantive like [guacamole-lite](https://github.com/vadimpronin/guacamole-lite). 


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=guacd&query=%24.mods%5B%27guacd%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=guacd "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it guacd /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f guacd`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' guacd`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ghcr.io/linuxserver/guacd`

## Versions

* **27.07.20:** - Bump to 1.2.0.
* **17.04.20:** - Bump back 1.1.0, rebase to focal
* **08.02.20:** - Bump to 1.1.0.
* **25.05.19:** - Initial Release.
