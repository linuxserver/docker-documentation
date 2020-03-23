# [linuxserver/radarr](https://github.com/linuxserver/docker-radarr)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-radarr.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-radarr)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-radarr.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-radarr/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-radarr/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-radarr/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/radarr)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/radarr.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/radarr "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/radarr.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/radarr)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/radarr.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/radarr)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-radarr/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-radarr/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/radarr/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/radarr/latest/index.html)

[Radarr](https://github.com/Radarr/Radarr) - A fork of Sonarr to work with movies à la Couchpotato.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/radarr` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | Stable Radarr releases |
| 5.14 | Stable Radarr releases, but run on Mono 5.14 |
| nightly | Nightly Radarr releases |
| preview | Alpha Radarr releases, unsupported and for development only |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=radarr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e UMASK_SET=022 `#optional` \
  -p 7878:7878 \
  -v /path/to/data:/config \
  -v /path/to/movies:/movies \
  -v /path/to/downloadclient-downloads:/downloads \
  --restart unless-stopped \
  linuxserver/radarr
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  radarr:
    image: linuxserver/radarr
    container_name: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - UMASK_SET=022 #optional
    volumes:
      - /path/to/data:/config
      - /path/to/movies:/movies
      - /path/to/downloadclient-downloads:/downloads
    ports:
      - 7878:7878
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `7878` | The port for the Radarr webinterface |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London, this is required for Radarr |
| `UMASK_SET=022` | control permissions of files and directories created by Radarr |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Database and Radarr configs |
| `/movies` | Location of Movie library on disk (See note in Application setup) |
| `/downloads` | Location of download managers output directory (See note in Application setup) |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `<your-ip>:7878`, for more information check out [Radarr](https://github.com/Radarr/Radarr).
Special Note: Following our current folder structure will result in an inability to hardlink from your downloads to your movies folder because they are on seperate volumes. To support hardlinking, simply ensure that the movies and downloads data are on a single volume. For example, if you have /mnt/storage/Movies and /mnt/storage/downloads/completed/Movies, you would want something like /mnt/storage:/media for your volume. Then you can hardlink from /media/downloads/completed to /media/Movies.
Another item to keep in mind, is that within radarr itself, you should then map your torrent client folder to your radarr folder: Settings -> Download Client -> advanded -> remote path mappings. I input the host of my download client (matches the download client defined) remote path is /downloads/Movies (relative to the internal container path) and local path is /media/downloads/completed/Movies, assuming you have folders to seperate your downloaded data types.



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it radarr /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f radarr`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' radarr`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/radarr`

## Versions

* **01.08.19:** - Rebase to Linuxserver LTS mono version.
* **13.06.19:** - Add env variable for setting umask.
* **10.05.19:** - Rebase to Bionic.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **09.09.18:** - Add pipeline build process.
* **24.02.18:** - Add nightly branch.
* **06.02.18:** - Radarr repo changed owner.
* **15.12.17:** - Fix continuation lines.
* **17.04.17:** - Switch to using inhouse mono baseimage, adds python also.
* **13.04.17:** - Switch to official mono repository.
* **10.01.17:** - Initial Release.
