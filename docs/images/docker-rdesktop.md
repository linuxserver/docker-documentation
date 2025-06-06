---
title: rdesktop
tags:
    - Remote Desktop
description: "[Rdesktop](http://xrdp.org/) - Containers containing full desktop environments in many popular flavors for Alpine, Ubuntu, Arch, and Fedora accessible via RDP."
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-rdesktop/blob/master/.github/CONTRIBUTING.md -->
# [linuxserver/rdesktop](https://github.com/linuxserver/docker-rdesktop)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Frdesktop?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-rdesktop.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-rdesktop)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-rdesktop.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-rdesktop/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-rdesktop/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-rdesktop/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/rdesktop)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/rdesktop.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/rdesktop)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/rdesktop.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/rdesktop)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-rdesktop%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-rdesktop/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Frdesktop%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/rdesktop/latest/index.html)

[Rdesktop](http://xrdp.org/) - Containers containing full desktop environments in many popular flavors for Alpine, Ubuntu, Arch, and Fedora accessible via RDP.

[![rdesktop](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/rdesktop.png)](http://xrdp.org/)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/rdesktop:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | ✅ | XFCE Alpine |
| ubuntu-xfce | ✅ | XFCE Ubuntu |
| fedora-xfce | ✅ | XFCE Fedora |
| arch-xfce | ✅ | XFCE Arch |
| debian-xfce | ✅ | XFCE Debian |
| alpine-kde | ✅ | KDE Alpine |
| ubuntu-kde | ✅ | KDE Ubuntu |
| fedora-kde | ✅ | KDE Fedora |
| arch-kde | ✅ | KDE Arch |
| debian-kde | ✅ | KDE Debian |
| alpine-mate | ✅ | MATE Alpine |
| ubuntu-mate | ✅ | MATE Ubuntu |
| fedora-mate | ✅ | MATE Fedora |
| arch-mate | ✅ | MATE Arch |
| debian-mate | ✅ | MATE Debian |
| alpine-i3 | ✅ | i3 Alpine |
| ubuntu-i3 | ✅ | i3 Ubuntu |
| fedora-i3 | ✅ | i3 Fedora |
| arch-i3 | ✅ | i3 Arch |
| debian-i3 | ✅ | i3 Debian |
| alpine-openbox | ✅ | Openbox Alpine |
| ubuntu-openbox | ✅ | Openbox Ubuntu |
| fedora-openbox | ✅ | Openbox Fedora |
| arch-openbox | ✅ | Openbox Arch |
| debian-openbox | ✅ | Openbox Debian |
| alpine-icewm | ✅ | IceWM Alpine |
| ubuntu-icewm | ✅ | IceWM Ubuntu |
| fedora-icewm | ✅ | IceWM Fedora |
| arch-icewm | ✅ | IceWM Arch |
| debian-icewm | ✅ | IceWM Debian |

## Application Setup

**The Default USERNAME and PASSWORD is: abc/abc**

**Unlike our other containers these Desktops are not designed to be upgraded by Docker, you will keep your home directory but anything you installed system level will be lost if you upgrade an existing container. To keep packages up to date instead use Ubuntu's own apt, Alpine's apk, Fedora's dnf, or Arch's pacman program**

You will need a Remote Desktop client to access this container [Wikipedia List](https://en.wikipedia.org/wiki/Comparison_of_remote_desktop_software), by default it listens on 3389, but you can change that port to whatever you wish on the host side IE `3390:3389`.
The first thing you should do when you login to the container is to change the abc users password by issuing the `passwd` command.

**Modern GUI desktop apps (including some flavors terminals) have issues with the latest Docker and syscall compatibility, you can use Docker with the `--security-opt seccomp=unconfined` setting to allow these syscalls or try [podman](https://podman.io/) as they have updated their codebase to support them**

If you ever lose your password you can always reset it by execing into the container as root:

```bash
docker exec -it rdesktop passwd abc
```

By default we perform all logic for the abc user and we recommend using that user only in the container, but new users can be added as long as there is a `startwm.sh` executable script in their home directory.
All of these containers are configured with passwordless sudo, we make no efforts to secure or harden these containers and we do not recommend ever publishing their ports to the public Internet.

## Options

All application settings are passed via environment variables:

| Variable | Description |
| :----: | --- |
| LC_ALL | Set the Language for the container to run as IE `fr_FR.UTF-8` `ar_AE.UTF-8` |
| NO_DECOR | If set the application will run without window borders. (Decor can be enabled and disabled with Ctrl+Shift+d) |
| NO_FULL | Do not autmatically fullscreen applications when using openbox. |

### Language Support - Internationalization

The environment variable `LC_ALL` can be used to start this image in a different language than English simply pass for example to launch the Desktop session in French `LC_ALL=fr_FR.UTF-8`. Some languages like Chinese, Japanese, or Korean will be missing fonts needed to render properly known as cjk fonts, but others may exist and not be installed. We only ensure fonts for Latin characters are present. Fonts can be installed with a mod on startup.

To install cjk fonts on startup as an example pass the environment variables(Debian):

```
-e DOCKER_MODS=linuxserver/mods:universal-package-install
-e INSTALL_PACKAGES=fonts-noto-cjk
-e LC_ALL=zh_CN.UTF-8
```

## PRoot Apps

All images include [proot-apps](https://github.com/linuxserver/proot-apps) which allow portable applications to be installed to persistent storage in the user's `$HOME` directory. These applications and their settings will persist upgrades of the base container and can be mounted into different flavors of rdesktop containers. IE if you are running an Alpine based container you will be able to use the same `/config` directory mounted into an Ubuntu based container and retain the same applications and settings as long as they were installed with `proot-apps install`.

A list of linuxserver.io supported applications is located [HERE](https://github.com/linuxserver/proot-apps?tab=readme-ov-file#supported-apps).

## Open Source GPU Acceleration

For accelerated apps or games, render devices can be mounted into the container and leveraged by applications using:

`--device /dev/dri:/dev/dri`

This feature only supports **Open Source** GPU drivers:

| Driver | Description |
| :----: | --- |
| Intel | i965 and i915 drivers for Intel iGPU chipsets |
| AMD | AMDGPU, Radeon, and ATI drivers for AMD dedicated or APU chipsets |
| NVIDIA | nouveau2 drivers only, closed source NVIDIA drivers lack DRI3 support |

## Nvidia GPU Support

**Nvidia is not compatible with Alpine based images**

Nvidia support is available by leveraging Zink for OpenGL support. This can be enabled with the following run flags:

| Variable | Description |
| :----: | --- |
| --gpus all | This can be filtered down but for most setups this will pass the one Nvidia GPU on the system |
| --runtime nvidia | Specify the Nvidia runtime which mounts drivers and tools in from the host |

The compose syntax is slightly different for this as you will need to set nvidia as the default runtime:

```
sudo nvidia-ctk runtime configure --runtime=docker --set-as-default
sudo service docker restart
```

And to assign the GPU in compose:

```
services:
  myimage:
    image: myname/myimage:mytag
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [compute,video,graphics,utility]
```

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

!!! info

    Unless a parameter is flaged as 'optional', it is *mandatory* and a value must be provided.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
---
services:
  rdesktop:
    image: lscr.io/linuxserver/rdesktop:latest
    container_name: rdesktop
    security_opt:
      - seccomp:unconfined #optional
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock #optional
      - /path/to/rdesktop/data:/config #optional
    ports:
      - 3389:3389
    devices:
      - /dev/dri:/dev/dri #optional
    shm_size: "1gb" #optional
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=rdesktop \
  --security-opt seccomp=unconfined `#optional` \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -p 3389:3389 \
  -v /var/run/docker.sock:/var/run/docker.sock `#optional` \
  -v /path/to/rdesktop/data:/config `#optional` \
  --device /dev/dri:/dev/dri `#optional` \
  --shm-size="1gb" `#optional` \
  --restart unless-stopped \
  lscr.io/linuxserver/rdesktop:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3389:3389` | RDP access port |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Etc/UTC` | specify a timezone to use, see this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/var/run/docker.sock` | Docker Socket on the system, if you want to use Docker in the container |
| `/config` | abc users home directory |

### Device Mappings (`--device`)

| Parameter | Function |
| :-----:   | --- |
| `/dev/dri` | Add this for GL support (Linux hosts only) |

#### Miscellaneous Options

| Parameter | Function |
| :-----:   | --- |
| `--shm-size=` | We set this to 1 gig to prevent modern web browsers from crashing |
| `--security-opt seccomp=unconfined` | For Docker Engine only, many modern gui apps need this to function as syscalls are unknown to Docker |

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

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=rdesktop&query=%24.mods%5B%27rdesktop%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=rdesktop "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it rdesktop /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f rdesktop
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' rdesktop
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/rdesktop:latest
    ```

## Updating Info

Most of our images are static, versioned, and require an image update and container recreation to update the app inside. With some exceptions (noted in the relevant readme.md), we do not recommend or support updating apps inside the container. Please consult the [Application Setup](#application-setup) section above to see if it is recommended for the image.

Below are the instructions for updating containers:

### Via Docker Compose

* Update images:
    * All images:

        ```bash
        docker-compose pull
        ```

    * Single image:

        ```bash
        docker-compose pull rdesktop
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d rdesktop
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/rdesktop:latest
    ```

* Stop the running container:

    ```bash
    docker stop rdesktop
    ```

* Delete the container:

    ```bash
    docker rm rdesktop
    ```

* Recreate a new container with the same docker run parameters as instructed above (if mapped correctly to a host folder, your `/config` folder and settings will be preserved)
* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Image Update Notifications - Diun (Docker Image Update Notifier)

!!! tip

    We recommend [Diun](https://crazymax.dev/diun/) for update notifications. Other tools that automatically update containers unattended are not recommended or supported.

## Building locally

If you want to make local modifications to these images for development purposes or just to customize the logic:

```bash
git clone https://github.com/linuxserver/docker-rdesktop.git
cd docker-rdesktop
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/rdesktop:latest .
```

The ARM variants can be built on x86_64 hardware and vice versa using `lscr.io/linuxserver/qemu-static`

```bash
docker run --rm --privileged lscr.io/linuxserver/qemu-static --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

To help with development, we generate this dependency graph.

??? info "Init dependency graph"

    ```d2
    "rdesktop:latest": {
      docker-mods
      base {
        fix-attr +\nlegacy cont-init
      }
      docker-mods -> base
      legacy-services
      custom services
      init-services -> legacy-services
      init-services -> custom services
      custom services -> legacy-services
      legacy-services -> ci-service-check
      init-migrations -> init-adduser
      init-os-end -> init-config
      init-rdesktop-end -> init-config
      init-config -> init-config-end
      init-os-end -> init-crontab-config
      init-mods-end -> init-custom-files
      init-adduser -> init-device-perms
      base -> init-envfile
      init-os-end -> init-keygen
      base -> init-migrations
      base -> init-mods
      init-config-end -> init-mods
      init-mods -> init-mods-end
      init-mods-package-install -> init-mods-end
      init-mods -> init-mods-package-install
      base -> init-os-end
      init-adduser -> init-os-end
      init-device-perms -> init-os-end
      init-envfile -> init-os-end
      init-migrations -> init-os-end
      init-keygen -> init-rdesktop
      init-keygen -> init-rdesktop-config
      init-video -> init-rdesktop-end
      init-custom-files -> init-services
      init-mods-end -> init-services
      init-rdesktop -> init-video
      init-rdesktop-config -> init-video
      init-services -> svc-cron
      svc-cron -> legacy-services
      init-services -> svc-xrdp
      svc-xrdp-sesman -> svc-xrdp
      svc-xrdp -> legacy-services
      init-services -> svc-xrdp-sesman
      svc-xrdp-sesman -> legacy-services
    }
    Base Images: {
      "baseimage-rdesktop:alpine320" <- "baseimage-alpine:3.20"
    }
    "rdesktop:latest" <- Base Images
    ```

## Versions

* **06.08.24:** - Refresh all images using new bases, add Debian, bump Ubuntu to Noble.
* **27.05.24:** - Rebase to Alpine 3.20 and Fedora 40.
* **17.01.24:** - Sync webtop logic changes rebase to Alpine 3.19 and Fedora 39.
* **18.05.23:** - Rebase all Alpine images to 3.18, deprecate armhf.
* **27.10.22:** - Rebase all Ubuntu images to Jammy 22.04.
* **26.10.22:** - Rebase Alpine xfce to 3.16, migrate to s6v3.
* **05.03.22:** - Organize tags differently to run Ubuntu at latest LTS, make Alpine latest, add docs about GPU accel.
* **05.05.21:** - Reduce default packages to their flavour specific basics.
* **05.04.21:** - Add Alpine flavour.
* **06.04.20:** - Start PulseAudio in images to support audio
* **28.02.20:** - Initial Releases
