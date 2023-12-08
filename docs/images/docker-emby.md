---
title: emby
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-emby/blob/master/.github/CONTRIBUTING.md -->
# [linuxserver/emby](https://github.com/linuxserver/docker-emby)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Femby?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh/gateway/linuxserver-ci/docker/linuxserver%2Femby)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-emby.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-emby)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-emby.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-emby/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-emby/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-emby/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/emby)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/emby.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/emby)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/emby.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/emby)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-emby%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-emby/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Femby%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/emby/latest/index.html)

[Emby](https://emby.media/) organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

[![emby](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/emby-logo.png)](https://emby.media/)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/emby:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64v8-\<version tag\> |
| armhf | ❌ | |

## Version Tags

This image provides various versions that are available via tags. Please read the descriptions carefully and exercise caution when using unstable or development tags.

| Tag | Available | Description |
| :----: | :----: |--- |
| latest | ✅ | Stable emby releases |
| beta | ✅ | Beta emby releases |

## Application Setup

Webui can be found at `http://<your-ip>:8096`

Emby has very complete and verbose documentation located [here](https://github.com/MediaBrowser/Wiki/wiki) .

Hardware acceleration users for Intel Quicksync and AMD VAAPI will need to mount their /dev/dri video device inside of the container by passing the following command when running or creating the container:

```--device=/dev/dri:/dev/dri```

We will automatically ensure the abc user inside of the container has the proper permissions to access this device.

Hardware acceleration users for Nvidia will need to install the container runtime provided by Nvidia on their host, instructions can be found here:

https://github.com/NVIDIA/nvidia-docker

We automatically add the necessary environment variable that will utilise all the features available on a GPU on the host. Once nvidia-docker is installed on your host you will need to re/create the docker container with the nvidia container runtime `--runtime=nvidia` and add an environment variable `-e NVIDIA_VISIBLE_DEVICES=all` (can also be set to a specific gpu's UUID, this can be discovered by running `nvidia-smi --query-gpu=gpu_name,gpu_uuid --format=csv` ). NVIDIA automatically mounts the GPU and drivers from your host into the emby docker.

### OpenMAX (Raspberry Pi)

Hardware acceleration users for Raspberry Pi OpenMAX will need to mount their /dev/vchiq video device inside of the container and their system OpenMax libs by passing the following options when running or creating the container:
```
--device=/dev/vchiq:/dev/vchiq
-v /opt/vc/lib:/opt/vc/lib
```

### V4L2 (Raspberry Pi)

Hardware acceleration users for Raspberry Pi V4L2 will need to mount their /dev/video1X devices inside of the container by passing the following options when running or creating the container:
```
--device=/dev/video10:/dev/video10
--device=/dev/video11:/dev/video11
--device=/dev/video12:/dev/video12
```

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
---
version: "2.1"
services:
  emby:
    image: lscr.io/linuxserver/emby:latest
    container_name: emby
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - /path/to/library:/config
      - /path/to/tvshows:/data/tvshows
      - /path/to/movies:/data/movies
      - /opt/vc/lib:/opt/vc/lib #optional
    ports:
      - 8096:8096
      - 8920:8920 #optional
    devices:
      - /dev/dri:/dev/dri #optional
      - /dev/vchiq:/dev/vchiq #optional
      - /dev/video10:/dev/video10 #optional
      - /dev/video11:/dev/video11 #optional
      - /dev/video12:/dev/video12 #optional
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=emby \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -p 8096:8096 \
  -p 8920:8920 `#optional` \
  -v /path/to/library:/config \
  -v /path/to/tvshows:/data/tvshows \
  -v /path/to/movies:/data/movies \
  -v /opt/vc/lib:/opt/vc/lib `#optional` \
  --device /dev/dri:/dev/dri `#optional` \
  --device /dev/vchiq:/dev/vchiq `#optional` \
  --device /dev/video10:/dev/video10 `#optional` \
  --device /dev/video11:/dev/video11 `#optional` \
  --device /dev/video12:/dev/video12 `#optional` \
  --restart unless-stopped \
  lscr.io/linuxserver/emby:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

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
| `TZ=Etc/UTC` | specify a timezone to use, see this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Emby data storage location. *This can grow very large, 50gb+ is likely for a large collection.* |
| `/data/tvshows` | Media goes here. Add as many as needed e.g. `/data/movies`, `/data/tv`, etc. |
| `/data/movies` | Media goes here. Add as many as needed e.g. `/data/movies`, `/data/tv`, etc. |
| `/opt/vc/lib` | Path for Raspberry Pi OpenMAX libs *optional*. |

### Device Mappings (`--device`)

| Parameter | Function |
| :-----:   | --- |
| `/dev/dri` | Only needed if you want to use your Intel or AMD GPU for hardware accelerated video encoding (vaapi). |
| `/dev/vchiq` | Only needed if you want to use your Raspberry Pi OpenMax video encoding (Bellagio). |
| `/dev/video10` | Only needed if you want to use your Raspberry Pi V4L2 video encoding. |
| `/dev/video11` | Only needed if you want to use your Raspberry Pi V4L2 video encoding. |
| `/dev/video12` | Only needed if you want to use your Raspberry Pi V4L2 video encoding. |

#### Miscellaneous Options

| Parameter | Function |
| :-----:   | --- |

## Environment variables from files (Docker secrets)

You can set any environment variable from a file by using a special prepend `FILE__`.

As an example:

```bash
-e FILE__MYVAR=/run/secrets/mysecretvariable
```

Will set the environment variable `MYVAR` based on the contents of the `/run/secrets/mysecretvariable` file.

## Umask for running applications

For all of our images we provide the ability to override the default umask settings for services started within the containers using the optional `-e UMASK=022` setting.
Keep in mind umask is not chmod it subtracts from permissions based on it's value it does not add. Please read up [here](https://en.wikipedia.org/wiki/Umask) before asking for support.

## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id your_user` as below:

```bash
id your_user
```

Example output:

```text
uid=1000(your_user) gid=1000(your_user) groups=1000(your_user)
```

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=emby&query=%24.mods%5B%27emby%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=emby "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it emby /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f emby
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' emby
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/emby:latest
    ```

## Updating Info

Most of our images are static, versioned, and require an image update and container recreation to update the app inside. With some exceptions (ie. nextcloud, plex), we do not recommend or support updating apps inside the container. Please consult the [Application Setup](#application-setup) section above to see if it is recommended for the image.

Below are the instructions for updating containers:

### Via Docker Compose

* Update images:
    * All images:

        ```bash
        docker-compose pull
        ```

    * Single image:

        ```bash
        docker-compose pull emby
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d emby
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/emby:latest
    ```

* Stop the running container:

    ```bash
    docker stop emby
    ```

* Delete the container:

    ```bash
    docker rm emby
    ```

* Recreate a new container with the same docker run parameters as instructed above (if mapped correctly to a host folder, your `/config` folder and settings will be preserved)
* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Watchtower auto-updater (only use if you don't remember the original parameters)

* Pull the latest image at its tag and replace it with the same env variables in one run:

    ```bash
    docker run --rm \
      -v /var/run/docker.sock:/var/run/docker.sock \
      containrrr/watchtower \
      --run-once emby
    ```

* You can also remove the old dangling images: `docker image prune`

!!! warning 

    We do not endorse the use of Watchtower as a solution to automated updates of existing Docker containers. In fact we generally discourage automated updates. However, this is a useful tool for one-time manual updates of containers where you have forgotten the original parameters. In the long term, we highly recommend using [Docker Compose](https://docs.linuxserver.io/general/docker-compose).

### Image Update Notifications - Diun (Docker Image Update Notifier)

!!! tip 

    We recommend [Diun](https://crazymax.dev/diun/) for update notifications. Other tools that automatically update containers unattended are not recommended or supported.

## Building locally

If you want to make local modifications to these images for development purposes or just to customize the logic:

```bash
git clone https://github.com/linuxserver/docker-emby.git
cd docker-emby
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/emby:latest .
```

The ARM variants can be built on x86_64 hardware using `multiarch/qemu-user-static`

```bash
docker run --rm --privileged multiarch/qemu-user-static:register --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

## Versions

* **06.07.23:** - Deprecate armhf. As announced [here](https://www.linuxserver.io/blog/a-farewell-to-arm-hf)
* **08.06.23:** - Fix package extraction so it doesn't change /tmp perms.
* **31.05.23:** - Use upstream deb packages instead of rpm.
* **26.09.22:** - Update chown behavior.
* **18.09.22:** - Migrate to s6v3, rebase to Ubuntu Jammy.
* **19.05.21:** - Structural changes upstream.
* **17.01.21:** - Deprecate `UMASK_SET` in favor of UMASK in baseimage, see above for more information. Remove no longer used mapping for /transcode.
* **21.12.20:** - Rebase to Focal, see [here](https://docs.linuxserver.io/faq#my-host-is-incompatible-with-images-based-on-ubuntu-focal) for troubleshooting armhf.
* **03.11.20:** - Fix issue with missing samba folder.
* **13.11.20:** - Fix issue with samba and ffmpeg.
* **03.07.20:** - Add support for amd vaapi hw transcode.
* **29.02.20:** - Add v4l2 support on Raspberry Pi.
* **26.02.20:** - Add openmax support on Raspberry Pi.
* **15.02.20:** - Allow restarting emby from the gui (also allows for auto restarts after addon updates).
* **02.10.19:** - Improve permission fixing for render and dvb devices.
* **13.08.19:** - Add umask environment variable.
* **24.06.19:** - Fix typos in readme.
* **30.05.19:** - Initial release.