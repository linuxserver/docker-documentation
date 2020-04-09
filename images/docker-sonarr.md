# [linuxserver/sonarr](https://github.com/linuxserver/docker-sonarr)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-sonarr.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-sonarr)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-sonarr.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-sonarr/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-sonarr/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-sonarr/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/sonarr)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/sonarr.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/sonarr "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/sonarr.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/sonarr)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/sonarr.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/sonarr)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-sonarr/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-sonarr/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/sonarr/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/sonarr/latest/index.html)

[Sonarr](https://sonarr.tv/) (formerly NZBdrone) is a PVR for usenet and bittorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/sonarr` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | Stable releases from Sonarr (currently v2) |
| develop | Development releases from Sonarr (currently v2) |
| preview | Preview releases from Sonarr (currently v3) |
| 5.14 | Stable Sonarr releases, but run on Mono 5.14 |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=sonarr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e UMASK_SET=022 `#optional` \
  -p 8989:8989 \
  -v /path/to/data:/config \
  -v /path/to/tvseries:/tv \
  -v /path/to/downloadclient-downloads:/downloads \
  --restart unless-stopped \
  linuxserver/sonarr
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  sonarr:
    image: linuxserver/sonarr
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - UMASK_SET=022 #optional
    volumes:
      - /path/to/data:/config
      - /path/to/tvseries:/tv
      - /path/to/downloadclient-downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8989` | The port for the Sonarr webinterface |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London, this is required for Sonarr |
| `UMASK_SET=022` | control permissions of files and directories created by Sonarr |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Database and sonarr configs |
| `/tv` | Location of TV library on disk (See note in Application setup) |
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

Access the webui at `<your-ip>:8989`, for more information check out [Sonarr](https://sonarr.tv/).
Special Note: Following our current folder structure will result in an inability to hardlink from your downloads to your TV folder because they are on seperate volumes. To support hardlinking, simply ensure that the TV and downloads data are on a single volume. For example, if you have /mnt/storage/TV and /mnt/storage/downloads/completed/TV, you would want something like /mnt/storage:/media for your volume. Then you can hardlink from /media/downloads/completed to /media/TV.
Another item to keep in mind, is that within sonarr itself, you should then map your torrent client folder to your sonarr folder: Settings -> Download Client -> advanded -> remote path mappings. I input the host of my download client (matches the download client defined) remote path is /downloads/TV (relative to the internal container path) and local path is /media/downloads/completed/TV, assuming you have folders to seperate your downloaded data types.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27sonarr%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=sonarr "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it sonarr /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f sonarr`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' sonarr`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/sonarr`

## Versions

* **05.04.20:** - Move app to /app.
* **01.08.19:** - Rebase to Linuxserver LTS mono version.
* **13.06.19:** - Add env variable for setting umask.
* **10.05.19:** - Rebase to Bionic.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **01.02.19:** - Multi arch images and pipeline build logic
* **15.12.17:** - Fix continuation lines.
* **12.07.17:** - Add inspect commands to README, move to jenkins build and push.
* **17.04.17:** - Switch to using inhouse mono baseimage, adds python also.
* **14.04.17:** - Change to mount /etc/localtime in README, thanks cbgj.
* **13.04.17:** - Switch to official mono repository.
* **30.09.16:** - Fix umask
* **23.09.16:** - Add cd to /opt fixes redirects with althub (issue #25) , make XDG config environment variable
* **15.09.16:** - Add libcurl3 package.
* **09.09.16:** - Add layer badges to README.
* **27.08.16:** - Add badges to README.
* **20.07.16:** - Rebase to xenial.
* **31.08.15:** - Cleanup, changed sources to fetch binarys from. also a new baseimage.
