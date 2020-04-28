# linuxserver/mstream

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-mstream.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-mstream) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-mstream.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-mstream/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-mstream/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-mstream/container_registry) [![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/mstream) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/mstream.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/mstream) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/mstream.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/mstream) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/mstream.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/mstream) [![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-mstream/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-mstream/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/mstream/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/mstream/latest/index.html)

[mstream](https://mstream.io/) is a personal music streaming server. You can use mStream to stream your music from your home computer to any device, anywhere. There are mobile apps available for both Android and iPhone.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/mstream` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=mstream \
  -e PUID=1000 \
  -e PGID=1000 \
  -e USER=admin \
  -e PASSWORD=password \
  -e USE_JSON=true/false \
  -e TZ=Europe/London \
  -p 3000:3000 \
  -v <path to data>:/config \
  -v <path to music>:/music \
  --restart unless-stopped \
  linuxserver/mstream
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  mstream:
    image: linuxserver/mstream
    container_name: mstream
    environment:
      - PUID=1000
      - PGID=1000
      - USER=admin
      - PASSWORD=password
      - USE_JSON=true/false
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <path to music>:/music
    ports:
      - 3000:3000
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `3000` | The port for the mStream webinterface |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `USER=admin` | Set username to login |
| `PASSWORD=password` | Set password for user |
| `USE_JSON=true/false` | Run mStream using the config specified at `/config/config.json`, note this will mean user/password is defined in `config.json` |
| `TZ=Europe/London` | Specify a timezone to use e.g. Europe/London |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | mStream config |
| `/music` | Music location |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `http://<your-ip>:3000`, For most users specifying a `$USER` and `$PASSWORD` is sufficient, the `USE_JSON` option allows for more granular control of mStream, but with added complexity, requiring manual editing of `config.json` to configure your install, for more information check out [Mstream](https://github.com/IrosTheBeggar/mStream/blob/master/docs/json_config.md#json-config). Note using this option will make the default username:password `admin` and `password` respectively and any environmental variables will be ignored.

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27mstream%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=mstream)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it mstream /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f mstream`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' mstream`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/mstream`

## Versions

* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **18.05.19:** - Inital Release

