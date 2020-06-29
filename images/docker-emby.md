# linuxserver/emby

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-emby.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-emby) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-emby.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-emby/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-emby/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-emby/container_registry) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/emby.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/emby) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/emby.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/emby) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/emby.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/emby) [![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-emby%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-emby/job/master/) [![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Femby%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/emby/latest/index.html)

[Emby](https://emby.media/) organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/emby` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | Stable emby releases |
| beta | Beta emby releases |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
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
  -v /opt/vc/lib:/opt/vc/lib `#optional` \
  --device /dev/dri:/dev/dri `#optional` \
  --device /dev/vchiq:/dev/vchiq `#optional` \
  --device /dev/video10:/dev/video10 `#optional` \
  --device /dev/video11:/dev/video11 `#optional` \
  --device /dev/video12:/dev/video12 `#optional` \
  --restart unless-stopped \
  linuxserver/emby
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
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
      - /opt/vc/lib:/opt/vc/lib #optional
    ports:
      - 8096:8096
    ports:
      - 8920:8920 #optional
    devices:
      - /dev/dri:/dev/dri #optional
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
| `8920` | Https webUI \(you need to setup your own certificate\). |

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
| `/config` | Emby data storage location. _This can grow very large, 50gb+ is likely for a large collection._ |
| `/data/tvshows` | Media goes here. Add as many as needed e.g. `/data/movies`, `/data/tv`, etc. |
| `/data/movies` | Media goes here. Add as many as needed e.g. `/data/movies`, `/data/tv`, etc. |
| `/transcode` | Path for transcoding folder, _optional_. |
| `/opt/vc/lib` | Path for Raspberry Pi OpenMAX libs _optional_. |

#### Device Mappings \(`--device`\)

| Parameter | Function |
| :---: | :--- |
| `/dev/dri` | Only needed if you want to use your Intel GPU for hardware accelerated video encoding \(vaapi\). |
| `/dev/vchiq` | Only needed if you want to use your Raspberry Pi OpenMax video encoding \(Bellagio\). |
| `/dev/video10` | Only needed if you want to use your Raspberry Pi V4L2 video encoding. |
| `/dev/video11` | Only needed if you want to use your Raspberry Pi V4L2 video encoding. |
| `/dev/video12` | Only needed if you want to use your Raspberry Pi V4L2 video encoding. |

## Environment variables from files \(Docker secrets\)

You can set any environment variable from a file by using a special prepend `FILE__`.

As an example:

```text
-e FILE__PASSWORD=/run/secrets/mysecretpassword
```

Will set the environment variable `PASSWORD` based on the contents of the `/run/secrets/mysecretpassword` file.

## Umask for running applications

For all of our images we provide the ability to override the default umask settings for services started within the containers using the optional `-e UMASK=022` setting. Keep in mind umask is not chmod it subtracts from permissions based on it's value it does not add. Please read up [here](https://en.wikipedia.org/wiki/Umask) before asking for support.

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

Emby has very complete and verbose documentation located [here](https://github.com/MediaBrowser/Wiki/wiki) .

Hardware acceleration users for Intel Quicksync will need to mount their /dev/dri video device inside of the container by passing the following command when running or creating the container:

```text
We will automatically ensure the abc user inside of the container has the proper permissions to access this device.

Hardware acceleration users for Nvidia will need to install the container runtime provided by Nvidia on their host, instructions can be found here:

https://github.com/NVIDIA/nvidia-docker

We automatically add the necessary environment variable that will utilise all the features available on a GPU on the host. Once nvidia-docker is installed on your host you will need to re/create the docker container with the nvidia container runtime `--runtime=nvidia` and add an environment variable `-e NVIDIA_VISIBLE_DEVICES=all` (can also be set to a specific gpu's UUID, this can be discovered by running `nvidia-smi --query-gpu=gpu_name,gpu_uuid --format=csv` ). NVIDIA automatically mounts the GPU and drivers from your host into the emby docker.

### OpenMAX (Raspberry Pi)

Hardware acceleration users for Raspberry Pi OpenMAX will need to mount their /dev/vchiq video device inside of the container and their system OpenMax libs by passing the following options when running or creating the container:
```

--device=/dev/vchiq:/dev/vchiq -v /opt/vc/lib:/opt/vc/lib

```text
### V4L2 (Raspberry Pi)

Hardware acceleration users for Raspberry Pi V4L2 will need to mount their /dev/video1X devices inside of the container by passing the following options when running or creating the container:
```

--device=/dev/video10:/dev/video10 --device=/dev/video11:/dev/video11 --device=/dev/video12:/dev/video12

\`\`\`

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27emby%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=emby)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

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

* **29.02.20:** - Add v4l2 support on Raspberry Pi.
* **26.02.20:** - Add openmax support on Raspberry Pi.
* **15.02.20:** - Allow restarting emby from the gui \(also allows for auto restarts after addon updates\).
* **02.10.19:** - Improve permission fixing for render and dvb devices.
* **13.08.19:** - Add umask environment variable.
* **24.06.19:** - Fix typos in readme.
* **30.05.19:** - Initial release.

