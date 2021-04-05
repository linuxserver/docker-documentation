---
title: rdesktop
---
# [linuxserver/rdesktop](https://github.com/linuxserver/docker-rdesktop)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-rdesktop.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-rdesktop)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-rdesktop.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-rdesktop/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-rdesktop/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-rdesktop/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/rdesktop.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/rdesktop "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/rdesktop.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/rdesktop)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/rdesktop.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/rdesktop)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-rdesktop%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-rdesktop/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Frdesktop%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/rdesktop/latest/index.html)

[Rdesktop](http://xrdp.org/) - Ubuntu based containers containing full desktop environments in officially supported flavors accessible via RDP.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `ghcr.io/linuxserver/rdesktop` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| alpine | XFCE Alpine |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker-compose ([recommended](https://docs.linuxserver.io/general/docker-compose))

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  rdesktop:
    image: ghcr.io/linuxserver/rdesktop
    container_name: rdesktop
    privileged: true #optional
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock #optional
      - /path/to/data:/config #optional
    ports:
      - 3389:3389
    shm_size: "1gb" #optional
    restart: unless-stopped
```

### docker cli

```
docker run -d \
  --name=rdesktop \
  --privileged `#optional` \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 3389:3389 \
  -v /var/run/docker.sock:/var/run/docker.sock `#optional` \
  -v /path/to/data:/config `#optional` \
  --shm-size="1gb" `#optional` \
  --restart unless-stopped \
  ghcr.io/linuxserver/rdesktop
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


#### Miscellaneous Options
| Parameter | Function |
| :-----:   | --- |
| `--shm-size=` | We set this to 1 gig to prevent modern web browsers from crashing |

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


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=rdesktop&query=%24.mods%5B%27rdesktop%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=rdesktop "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it rdesktop /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f rdesktop`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' rdesktop`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ghcr.io/linuxserver/rdesktop`

## Versions

* **05.04.21:** - Add Alpine flavor.
* **06.04.20:** - Start PulseAudio in images to support audio
* **28.02.20:** - Initial Releases
