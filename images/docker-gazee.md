# linuxserver/gazee

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn) [![](https://images.microbadger.com/badges/version/linuxserver/gazee.svg)](https://microbadger.com/images/linuxserver/gazee) [![](https://images.microbadger.com/badges/image/linuxserver/gazee.svg)](https://microbadger.com/images/linuxserver/gazee) ![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/gazee.svg) ![Docker Stars](https://img.shields.io/docker/stars/linuxserver/gazee.svg) [![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-gazee/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-gazee/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/gazee/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/gazee/latest/index.html)

[Gazee](https://github.com/hubbcaps/gazee) is a WebApp Comic Reader for your favorite digital comics. Reach and read your comic library from any web connected device with a modern web browser.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/gazee` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :---: | :--- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=gazee \
  -e PUID=1000 \
  -e PGID=1000 \
  -p 4242:4242 \
  -v </path/to/appdata/config>:/config \
  -v <path to comics>:/comics \
  -v <path to mylar data>:/mylar \
  -v <path to SSL certs>:/certs \
  --restart unless-stopped \
  linuxserver/gazee
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  gazee:
    image: linuxserver/gazee
    container_name: gazee
    environment:
      - PUID=1000
      - PGID=1000
    volumes:
      - </path/to/appdata/config>:/config
      - <path to comics>:/comics
      - <path to mylar data>:/mylar
      - <path to SSL certs>:/certs
    ports:
      - 4242:4242
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `4242` | WebUI |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Where Gazee should store config files. |
| `/comics` | Path to comics folder. |
| `/mylar` | Path to Mylar DB. |
| `/certs` | Where SSL certs should be stored. |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Webui can be found at `your-ip:4242`

Default username and password for the web interface:

* **Username:** `admin`
* **Password:** `gazee`

Click the gear icon to go to the settings page.

Change the default admin password or add a new admin and remove the admin user altogether.

Comic path should be set to `/comics`

_Optional_ Mylar DB path should be set to `/mylar`

_Optional_ path for certificates and keys should be set to `/certs`

After you update the settings, Gazee will restart and begin an intial scan of your comic library.

Happy Reading!

## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it gazee /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f gazee`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' gazee`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/gazee`

## Versions

* **11.02.19:** - Add pipeline logic and multi arch.
* **17.08.18:** - Rebase to alpine 3.8.
* **30.12.17:** - Ensure version 11 of cherrypy.
* **07.12.17:** - Initial Release.

