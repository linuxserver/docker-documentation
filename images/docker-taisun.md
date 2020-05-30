# [linuxserver/taisun](https://github.com/linuxserver/docker-taisun)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-taisun.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-taisun)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-taisun.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-taisun/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-taisun/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-taisun/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/taisun.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/taisun "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/taisun.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/taisun)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/taisun.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/taisun)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-taisun%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-taisun/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flspipepr%2Ftaisun%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/taisun/latest/index.html)

[Taisun](https://www.taisun.io/) is an application for a Docker enabled device with an emphasis on providing a web based interface for managing a single server.
Taisun allows you to:

  - Deploy and manage web based virtual desktops.
  - Deploy Taisun specific stacks of applications
  - Browse available images on popular Docker repositories
  - Import a Docker project from any git repository and start developing on your choice of web based IDE or full Linux desktop
  - Spinup a developer container based on popular frameworks and work from a web based IDE
  - Single click remote server access to Taisun and your Docker applications


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/taisun` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=taisun \
  -p 3000:3000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --restart unless-stopped \
  linuxserver/taisun
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  taisun:
    image: linuxserver/taisun
    container_name: taisun
    network_mode: bridge
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - 3000:3000
    restart: unless-stopped

```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3000` | Taisun WebUI. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/var/run/docker.sock` | Docker Socket on the system |



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

The webui is at http://localhost:3000, for more information on usage see [here](https://github.com/Taisun-Docker/taisun/wiki/Usage).


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27taisun%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=taisun "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it taisun /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f taisun`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' taisun`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/taisun`

## Versions

* **19.12.19:** - Rebasing to alpine 3.11.
* **20.07.19:** - Build compose bins from source, use minimal docker install from repos.
* **28.06.19:** - Rebasing to alpine 3.10.
* **30.03.19:** - Updating docker-compose build dependancies for musl libc.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **13.02.19:** - Initial release.
