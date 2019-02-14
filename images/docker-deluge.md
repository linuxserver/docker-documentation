# [linuxserver/deluge](https://github.com/linuxserver/docker-deluge)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/deluge.svg)](https://microbadger.com/images/linuxserver/deluge "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/deluge.svg)](https://microbadger.com/images/linuxserver/deluge "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/deluge.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/deluge.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-deluge/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-deluge/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/deluge/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/deluge/latest/index.html)

[Deluge](http://deluge-torrent.org/) is a lightweight, Free Software, cross-platform BitTorrent client.

* Full Encryption
* WebUI
* Plugin System
* Much more...


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list). 

Simply pulling `linuxserver/deluge` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=deluge \
  --net=host \
  -e PUID=1001 \
  -e PGID=1001 \
  -e UMASK_SET=<022> \
  -e TZ=<timezone> \
  -v </path/to/deluge/config>:/config \
  -v </path/to/your/downloads>:/downloads \
  --restart unless-stopped \
  linuxserver/deluge
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  deluge:
    image: linuxserver/deluge
    container_name: deluge
    network_mode: host
    environment:
      - PUID=1001
      - PGID=1001
      - UMASK_SET=<022>
      - TZ=<timezone>
    volumes:
      - </path/to/deluge/config>:/config
      - </path/to/your/downloads>:/downloads
    mem_limit: 4096m
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |

#### Networking (`--net`)
| Parameter | Function |
| :-----:   | --- |
| `--net=host` | Shares host networking with container, **required**. |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1001` | for UserID - see below for explanation |
| `PGID=1001` | for GroupID - see below for explanation |
| `UMASK_SET=<022>` | for umask setting of deluge, *optional* , default if left unset is 022. |
| `TZ=<timezone>` | Specify a timezone to use EG Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | deluge configs |
| `/downloads` | torrent download directory |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1001` and `PGID=1001`, to find yours use `id user` as below:

```
  $ id username
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Application Setup

The admin interface is available at http://<ip>:8112 with a default user/password of admin/deluge.

To change the password (recommended) log in to the web interface and go to Preferences->Interface->Password.

Change the downloads location in the webui in Preferences->Downloads and use /downloads for completed downloads.



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it deluge /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f deluge`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' deluge`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/deluge`

## Versions

* **15.11.18:** - Add deluge-console.
* **11.11.18:** - Rebase to Ubuntu Bionic, add pipeline multiarch logic.
* **09.04.18:** - update to libressl2.7-libssl.
* **29.03.18:** - Rebase to alpine edge.
* **07.12.17:** - Rebase to alpine 3.7.
* **20.11.17:** - Change libressl2.6-libssl repo.
* **01.07.17:** - Add curl package.
* **26.05.17:** - Rebase to alpine 3.6.
* **29.04.17:** - Add variable for user defined umask.
* **28.04.17:** - update to libressl2.5-libssl.
* **28.12.16:** - Rebase to alpine 3.5 baseimage.
* **17.11.16:** - Rebase to edge baseimage.
* **13.10.16:** - Switch to libressl as openssl deprecated from alpine linux and deluge dependency no longer installs
* **30.09.16:** - Fix umask.
* **09.09.16:** - Add layer badges to README.
* **30.08.16:** - Use pip packages for some critical dependencies.
* **28.08.16:** - Add badges to README.
* **15.08.16:** - Rebase to alpine linux.
* **09.11.15:** - Add unrar and unzip
* **15.10.15:** - Initial Release.
