---
title: minetest
---
# [linuxserver/minetest](https://github.com/linuxserver/docker-minetest)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-minetest.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-minetest)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-minetest.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-minetest/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-minetest/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-minetest/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/minetest.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/minetest "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/minetest.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/minetest)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/minetest.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/minetest)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-minetest%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-minetest/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fminetest%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/minetest/latest/index.html)

[Minetest](http://www.minetest.net/) (server) is a near-infinite-world block sandbox game and a game engine, inspired by InfiniMiner, Minecraft, and the like.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `ghcr.io/linuxserver/minetest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  minetest:
    image: ghcr.io/linuxserver/minetest
    container_name: minetest
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - CLI_ARGS="--gameid minetest" #optional
    volumes:
      - <path to data>:/config/.minetest
    ports:
      - 30000:30000/udp
    restart: unless-stopped
```

### docker cli

```
docker run -d \
  --name=minetest \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e CLI_ARGS="--gameid minetest" `#optional` \
  -p 30000:30000/udp \
  -v <path to data>:/config/.minetest \
  --restart unless-stopped \
  ghcr.io/linuxserver/minetest
```


## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `30000/udp` | Port Minetest listens on. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `CLI_ARGS="--gameid minetest"` | Optionally specify any [CLI variables](https://wiki.minetest.net/Command_line) you want to launch the app with |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config/.minetest` | Where minetest stores config files and maps etc. |



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


## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

You can find the world maps, mods folder and config files in /config/.minetest.

Client and server must be the same version, please browse the tags here to pull the appropriate version for your server:

https://hub.docker.com/r/linuxserver/minetest/tags


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=minetest&query=%24.mods%5B%27minetest%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=minetest "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it minetest /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f minetest`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' minetest`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ghcr.io/linuxserver/minetest`

## Versions

* **02.06.20:** - Rebasing to alpine 3.12.
* **19.12.19:** - Rebasing to alpine 3.11.
* **12.07.19:** - Bugfix to support multiple CLI variables.
* **28.06.19:** - Rebasing to alpine 3.10.
* **03.06.19:** - Adding custom cli vars to options.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **04.03.19:** - Rebase to alpine 3.9 to compile 5.0.0 minetest with new build args.
* **14.01.19:** - Add pipeline logic and multi arch.
* **08.08.18:** - Rebase to alpine 3.8, build from latest release tag instead of master.
* **03.01.18:** - Deprecate cpu_core routine lack of scaling.
* **08.12.17:** - Rebase to alpine 3.7.
* **30.11.17:** - Use cpu core counting routine to speed up build time.
* **26.05.17:** - Rebase to alpine 3.6.
* **14.02.17:** - Rebase to alpine 3.5.
* **25.11.16:** - Rebase to alpine linux, move to main repo.
* **27.02.16:** - Bump to latest version.
* **19.02.16:** - Change port to UDP, thanks to slashopt for pointing this out.
* **15.02.16:** - Make minetest app a service.
* **01.02.16:** - Add lua-socket dependency.
* **06.11.15:** - Initial Release.
