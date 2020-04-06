# [linuxserver/rdesktop](https://github.com/linuxserver/docker-rdesktop)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-rdesktop.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-rdesktop)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-rdesktop.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-rdesktop/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-rdesktop/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-rdesktop/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/rdesktop)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/rdesktop.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/rdesktop "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/rdesktop.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/rdesktop)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/rdesktop.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/rdesktop)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-rdesktop/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-rdesktop/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/rdesktop/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/rdesktop/latest/index.html)

[Rdesktop](http://xrdp.org/) - Ubuntu based containers containing full desktop environments in officially supported flavors accessible via RDP.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/rdesktop` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | XFCE Focal |
| xfce-bionic | XFCE Bionic |
| kde-focal | KDE Focal |
| kde-bionic | KDE Bionic |
| mate-focal | MATE Focal |
| mate-bionic | MATE Bionic |
| i3-focal | i3 Focal |
| i3-bionic | i3 Bionic |
| openbox-focal | Openbox Focal |
| openbox-bionic | Openbox Bionic |
| icewm-focal | IceWM Focal |
| icewm-bionic | IceWM Bionic |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=rdesktop \
  --privileged `#optional` \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 3389:3389 \
  -v /var/run/docker.sock:/var/run/docker.sock `#optional` \
  -v /path/to/data:/config `#optional` \
  --restart unless-stopped \
  linuxserver/rdesktop
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  rdesktop:
    image: linuxserver/rdesktop
    container_name: rdesktop
    privileged: true #optional
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock #optional
      - /path/to/data:/config #optional
    ports:
      - 3389:3389
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3389` | RDP access port |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/var/run/docker.sock` | Docker Socket on the system, if you want to use Docker in the container |
| `/config` | abc users home directory |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

**The Default USERNAME and PASSWORD is: abc/abc**

**Unlike our other containers these Desktops are not designed to be upgraded by Docker, you will keep your home directoy but anything you installed system level will be lost if you upgrade an existing container. To keep packages up to date instead use Ubuntu's own apt program**

**The KDE and i3 flavors need to be run in privileged mode to function properly**

You will need a Remote Desktop client to access this container [Wikipedia List](https://en.wikipedia.org/wiki/Comparison_of_remote_desktop_software), by default it listens on 3389, but you can change that port to whatever you wish on the host side IE `3390:3389`.
The first thing you should do when you login to the container is to change the abc users password by issuing the `passwd` command. 
If you ever lose your password you can always reset it by execing into the container as root:
```
docker exec -it rdesktop passwd abc
```
By default we perform all logic for the abc user and we reccomend using that user only in the container, but new users can be added as long as there is a `startwm.sh` executable script in their home directory.
All of these containers are configured with passwordless sudo, we make no efforts to secure or harden these containers and we do not reccomend ever publishing their ports to the public Internet. 



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it rdesktop /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f rdesktop`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' rdesktop`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/rdesktop`

## Versions

* **06.04.20:** - Start PulseAudio in images to support audio
* **28.02.20:** - Initial Releases
