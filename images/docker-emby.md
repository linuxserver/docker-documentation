# [linuxserver/emby](https://github.com/linuxserver/docker-emby)

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-emby.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-emby/releases)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/emby.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/emby "Get your own version badge on microbadger.com")
[![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/emby.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/emby "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/emby.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/emby)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/emby.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/emby)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-emby/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-emby/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/emby/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/emby/latest/index.html)

[Emby](https://emby.media/) organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/emby` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | Stable emby releases |
| beta | Beta emby releases |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=emby \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e UMASK_SET=<022> `#optional` \
  -p 8096:8096 \
  -p 8920:8920 `#optional` \
  -v /path/to/library:/config \
  -v /path/to/tvshows:/data/tvshows \
  -v /path/to/movies:/data/movies \
  -v /path/for/transcoding:/transcode `#optional` \
  --device /dev/dri:/dev/dri `#optional` \
  --restart unless-stopped \
  linuxserver/emby
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  emby:
    image: linuxserver/emby
    container_name: emby
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - UMASK_SET=<022> #optional
    volumes:
      - /path/to/library:/config
      - /path/to/tvshows:/data/tvshows
      - /path/to/movies:/data/movies
    volumes:
      - /path/for/transcoding:/transcode #optional
    ports:
      - 8096:8096
    ports:
      - 8920:8920 #optional
    devices:
      - /dev/dri:/dev/dri #optional
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8096` | Http webUI. |
| `8920` | Https webUI (you need to setup your own certificate). |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `UMASK_SET=<022>` | for umask setting of Emby, default if left unset is 022. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Emby data storage location. *This can grow very large, 50gb+ is likely for a large collection.* |
| `/data/tvshows` | Media goes here. Add as many as needed e.g. `/data/movies`, `/data/tv`, etc. |
| `/data/movies` | Media goes here. Add as many as needed e.g. `/data/movies`, `/data/tv`, etc. |
| `/transcode` | Path for transcoding folder, *optional*. |

#### Device Mappings (`--device`)
| Parameter | Function |
| :-----:   | --- |
| `/dev/dri` | Only needed if you want to use your Intel GPU for hardware accelerated video encoding (vaapi). |


## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Webui can be found at `http://<your-ip>:8096`

Emby has very complete and verbose documentation located [here](https://github.com/MediaBrowser/Wiki/wiki) .

Hardware acceleration users for Intel Quicksync will need to mount their /dev/dri video device inside of the container by passing the following command when running or creating the container:

```--device=/dev/dri:/dev/dri```

We will automatically ensure the abc user inside of the container has the proper permissions to access this device.

Hardware acceleration users for Nvidia will need to install the container runtime provided by Nvidia on their host, instructions can be found here:

https://github.com/NVIDIA/nvidia-docker

We automatically add the necessary environment variable that will utilise all the features available on a GPU on the host. Once nvidia-docker is installed on your host you will need to re/create the docker container with the nvidia container runtime `--runtime=nvidia` and add an environment variable `-e NVIDIA_VISIBLE_DEVICES=all` (can also be set to a specific gpu's UUID, this can be discovered by running `nvidia-smi --query-gpu=gpu_name,gpu_uuid --format=csv` ). NVIDIA automatically mounts the GPU and drivers from your host into the emby docker.



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it emby /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f emby`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' emby`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/emby`

## Versions

* **13.08.19:** - Add umask environment variable.
* **24.06.19:** - Fix typos in readme.
* **30.05.19:** - Initial release.
