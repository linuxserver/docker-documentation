# linuxserver/freshrss

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-freshrss.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-freshrss/releases) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/freshrss.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/freshrss) [![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/freshrss.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/freshrss) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/freshrss.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/freshrss) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/freshrss.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/freshrss) [![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-freshrss/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-freshrss/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/freshrss/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/freshrss/latest/index.html)

[Freshrss](https://freshrss.org/) is a free, self-hostable aggregator for rss feeds.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/freshrss` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=freshrss \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 80:80 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/freshrss
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  freshrss:
    image: linuxserver/freshrss
    container_name: freshrss
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
    ports:
      - 80:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `80` | WebUI |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Local storage for freshrss site files. |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Create a user and database in your mysql/mariadb server \(not root\) and then follow the setup wizard in the webui. Use the IP address for "host" of your database server.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it freshrss /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f freshrss`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' freshrss`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/freshrss`

## Versions

* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **14.01.19:** - Add multi arch and pipeline logic.
* **05.09.18:** - Rebase to alpine linux 3.8.
* **17.03.18:** - Update nginx config to resolve api not working.
* **08.01.18:** - Rebase to alpine linux 3.7.
* **25.05.17:** - Rebase to alpine linux 3.6.
* **23.02.17:** - Rebase to alpine linux 3.5 and nginx.
* **14.10.16:** - Add version layer information.
* **08.10.16:** - Add Sqlite support for standalone operation.
* **27.09.16:** - Fix for cron job.
* **11.09.16:** - Add layer badges to README.
* **23.11.15:** - Update dependencies to latest requirements.
* **21.08.15:** - Initial Release.

