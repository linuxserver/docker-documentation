# [linuxserver/qbittorrent](https://github.com/linuxserver/docker-qbittorrent)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-qbittorrent.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-qbittorrent)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-qbittorrent.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-qbittorrent/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-qbittorrent/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-qbittorrent/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/qbittorrent)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/qbittorrent.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/qbittorrent "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/qbittorrent.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/qbittorrent)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/qbittorrent.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/qbittorrent)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-qbittorrent/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-qbittorrent/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/qbittorrent/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/qbittorrent/latest/index.html)

The [Qbittorrent](https://www.qbittorrent.org/) project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/qbittorrent` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :----: | --- |
| latest | Stable qbittorrent releases |
| unstable | Unstable qbittorrent releases |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=qbittorrent \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e UMASK_SET=022 \
  -e WEBUI_PORT=8080 \
  -p 6881:6881 \
  -p 6881:6881/udp \
  -p 8080:8080 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/downloads>:/downloads \
  --restart unless-stopped \
  linuxserver/qbittorrent
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  qbittorrent:
    image: linuxserver/qbittorrent
    container_name: qbittorrent
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - UMASK_SET=022
      - WEBUI_PORT=8080
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/downloads>:/downloads
    ports:
      - 6881:6881
      - 6881:6881/udp
      - 8080:8080
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `6881` | tcp connection port |
| `6881/udp` | udp connection port |
| `8080` | http gui |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `UMASK_SET=022` | for umask setting of qbittorrent, optional , default if left unset is 022 |
| `WEBUI_PORT=8080` | for changing the port of the webui, see below for explanation |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains all relevant configuration files. |
| `/downloads` | Location of downloads on disk. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

The webui is at `<your-ip>:8080` and the default username/password is `admin/adminadmin`.  

Change username/password via the webui in the webui section of settings.  


### WEBUI_PORT variable

Due to issues with CSRF and port mapping, should you require to alter the port for the webui you need to change both sides of the -p 8080 switch AND set the WEBUI_PORT variable to the new port.  

For example, to set the port to 8090 you need to set -p 8090:8090 and -e WEBUI_PORT=8090  

This should alleviate the "white screen" issue.  

If you have no webui , check the file /config/qBittorrent/qBittorrent.conf  

edit or add the following lines  

```
WebUI\Address=*

WebUI\ServerDomains=*
```



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it qbittorrent /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f qbittorrent`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' qbittorrent`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/qbittorrent`

## Versions

* **02.08.19:** - Add qbitorrent-cli for processing scripts.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **14.01.19:** - Rebase to Ubuntu, add multi arch and pipeline logic.
* **25.09.18:** - Use buildstage type build, bump qbitorrent to 4.1.3.
* **14.08.18:** - Rebase to alpine 3.8, bump libtorrent to 1.1.9 and qbitorrent to 4.1.2.
* **08.06.18:** - Bump qbitorrent to 4.1.1.
* **26.04.18:** - Bump libtorrent to 1.1.7.
* **02.03.18:** - Bump qbitorrent to 4.0.4 and libtorrent to 1.1.6.
* **02.01.18:** - Deprecate cpu_core routine lack of scaling.
* **19.12.17:** - Update to v4.0.3.
* **09.02.17:** - Rebase to alpine 3.7
* **01.12.17:** - Update to v4.0.2.
* **27.11.17:** - Update to v4 and use cpu_core routine to speed up builds.
* **16.09.17:** - Bump to 3.3.16, Add WEBUI_PORT variable and notes to README to allow changing port of webui.
* **01.08.17:** - Initial Release.
* **12.02.18:** - Initial Release.
