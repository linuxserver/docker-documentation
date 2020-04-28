# linuxserver/jellyfin

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-jellyfin.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-jellyfin) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-jellyfin.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-jellyfin/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-jellyfin/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-jellyfin/container_registry) [![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/jellyfin) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/jellyfin.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/jellyfin) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/jellyfin.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/jellyfin) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/jellyfin.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/jellyfin) [![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-jellyfin/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-jellyfin/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/jellyfin/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/jellyfin/latest/index.html)

[Jellyfin](https://jellyfin.github.io/) is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps. Jellyfin is descended from Emby's 3.5.2 release and ported to the .NET Core framework to enable full cross-platform support. There are no strings attached, no premium licenses or features, and no hidden agendas: just a team who want to build something better and work together to achieve it.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/jellyfin` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :---: | :--- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :---: | :--- |
| latest | Stable Jellyfin releases |
| nightly | Nightly Jellyfin releases |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=jellyfin \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e UMASK_SET=<022> `#optional` \
  -p 8096:8096 \
  -p 8920:8920 `#optional` \
  -v /path/to/library:/config \
  -v /path/to/tvseries:/data/tvshows \
  -v /path/to/movies:/data/movies \
  -v /opt/vc/lib:/opt/vc/lib `#optional` \
  --device /dev/dri:/dev/dri `#optional` \
  --device /dev/vc-mem:/dev/vc-mem `#optional` \
  --device /dev/vchiq:/dev/vchiq `#optional` \
  --device /dev/video10:/dev/video10 `#optional` \
  --device /dev/video11:/dev/video11 `#optional` \
  --device /dev/video12:/dev/video12 `#optional` \
  --restart unless-stopped \
  linuxserver/jellyfin
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  jellyfin:
    image: linuxserver/jellyfin
    container_name: jellyfin
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - UMASK_SET=<022> #optional
    volumes:
      - /path/to/library:/config
      - /path/to/tvseries:/data/tvshows
      - /path/to/movies:/data/movies
    volumes:
      - /opt/vc/lib:/opt/vc/lib #optional
    ports:
      - 8096:8096
    ports:
      - 8920:8920 #optional
    devices:
      - /dev/dri:/dev/dri #optional
      - /dev/vc-mem:/dev/vc-mem #optional
      - /dev/vchiq:/dev/vchiq #optional
      - /dev/video10:/dev/video10 #optional
      - /dev/video11:/dev/video11 #optional
      - /dev/video12:/dev/video12 #optional
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `8096` | Http webUI. |
| `8920` | Https webUI \(you need to set up your own certificate\). |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `UMASK_SET=<022>` | for umask setting of Emby, default if left unset is 022. |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Jellyfin data storage location. _This can grow very large, 50gb+ is likely for a large collection._ |
| `/data/tvshows` | Media goes here. Add as many as needed e.g. `/data/movies`, `/data/tv`, etc. |
| `/data/movies` | Media goes here. Add as many as needed e.g. `/data/movies`, `/data/tv`, etc. |
| `/opt/vc/lib` | Path for Raspberry Pi OpenMAX libs _optional_. |

#### Device Mappings \(`--device`\)

| Parameter | Function |
| :---: | :--- |
| `/dev/dri` | Only needed if you want to use your Intel GPU for hardware accelerated video encoding \(vaapi\). |
| `/dev/vc-mem` | Only needed if you want to use your Raspberry Pi MMAL video decoding \(Enabled as OpenMax H264 decode in gui settings\). |
| `/dev/vchiq` | Only needed if you want to use your Raspberry Pi OpenMax video encoding. |
| `/dev/video10` | Only needed if you want to use your Raspberry Pi V4L2 video encoding. |
| `/dev/video11` | Only needed if you want to use your Raspberry Pi V4L2 video encoding. |
| `/dev/video12` | Only needed if you want to use your Raspberry Pi V4L2 video encoding. |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Webui can be found at `http://<your-ip>:8096`

More information can be found in their official documentation [here](https://jellyfin.org/docs/general/quick-start.html) .

## Hardware Acceleration

### Intel

Hardware acceleration users for Intel Quicksync will need to mount their /dev/dri video device inside of the container by passing the following command when running or creating the container:

`--device=/dev/dri:/dev/dri`

We will automatically ensure the abc user inside of the container has the proper permissions to access this device.

### Nvidia

Hardware acceleration users for Nvidia will need to install the container runtime provided by Nvidia on their host, instructions can be found here:

[https://github.com/NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker)

We automatically add the necessary environment variable that will utilise all the features available on a GPU on the host. Once nvidia-docker is installed on your host you will need to re/create the docker container with the nvidia container runtime `--runtime=nvidia` and add an environment variable `-e NVIDIA_VISIBLE_DEVICES=all` \(can also be set to a specific gpu's UUID, this can be discovered by running `nvidia-smi --query-gpu=gpu_name,gpu_uuid --format=csv` \). NVIDIA automatically mounts the GPU and drivers from your host into the jellyfin docker container.

### OpenMAX \(Raspberry Pi\)

Hardware acceleration users for Raspberry Pi MMAL/OpenMAX will need to mount their `/dev/vc-mem` and `/dev/vchiq` video devices inside of the container and their system OpenMax libs by passing the following options when running or creating the container:

```text
--device=/dev/vc-mem:/dev/vc-mem
--device=/dev/vchiq:/dev/vchiq
-v /opt/vc/lib:/opt/vc/lib
```

### V4L2 \(Raspberry Pi\)

Hardware acceleration users for Raspberry Pi V4L2 will need to mount their `/dev/video1X` devices inside of the container by passing the following options when running or creating the container:

```text
--device=/dev/video10:/dev/video10
--device=/dev/video11:/dev/video11
--device=/dev/video12:/dev/video12
```

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27jellyfin%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=jellyfin)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it jellyfin /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f jellyfin`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' jellyfin`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/jellyfin`

## Versions

* **11.04.20:** - Enable hw decode \(mmal\) on Raspberry Pi, update readme instructions, add donation info, create missing default transcodes folder.
* **11.03.20:** - Add Pi V4L2 support, remove optional transcode mapping \(location is selected in the gui, defaults to path under `/config`\).
* **30.01.20:** - Add nightly tag.
* **09.01.20:** - Add Pi OpenMax support.
* **02.10.19:** - Improve permission fixing for render & dvb devices.
* **31.07.19:** - Add AMD drivers for vaapi support on x86.
* **13.06.19:** - Add Intel drivers for vaapi support on x86.
* **07.06.19:** - Initial release.

