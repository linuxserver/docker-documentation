---
title: foldingathome
tags:
    - Science
description: "[Folding@home](https://foldingathome.org/) is a distributed computing project for simulating protein dynamics, including the process of protein folding and the movements of proteins implicated in a variety of diseases. It brings together citizen scientists who volunteer to run simulations of protein dynamics on their personal computers. Insights from this data are helping scientists to better understand biology, and providing new opportunities for developing therapeutics."
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-foldingathome/blob/master/.github/CONTRIBUTING.md -->
# [linuxserver/foldingathome](https://github.com/linuxserver/docker-foldingathome)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Ffoldingathome?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-foldingathome.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-foldingathome)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-foldingathome.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-foldingathome/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-foldingathome/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-foldingathome/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/foldingathome)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/foldingathome.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/foldingathome)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/foldingathome.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/foldingathome)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-foldingathome%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-foldingathome/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Ffoldingathome%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/foldingathome/latest/index.html)

[Folding@home](https://foldingathome.org/) is a distributed computing project for simulating protein dynamics, including the process of protein folding and the movements of proteins implicated in a variety of diseases. It brings together citizen scientists who volunteer to run simulations of protein dynamics on their personal computers. Insights from this data are helping scientists to better understand biology, and providing new opportunities for developing therapeutics.

[![foldingathome](https://foldingathome.org/wp-content/uploads/2016/09/folding-at-home-logo.png)](https://foldingathome.org/)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/foldingathome:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64v8-\<version tag\> |

## Application Setup

This image sets up the Folding@home client. The interface is available at [https://app.foldingathome.org](https://app.foldingathome.org).

Before setting up this container, please register for an account on [https://app.foldingathome.org](https://app.foldingathome.org) and retrieve the account token shown in the account settings. That value should be populated in the `ACCOUNT_TOKEN` env var.

Once the container is created with the token and the machine name, the instance should be listed in the web app and can be controlled there.

Afterwards, the `ACCOUNT_TOKEN` and the `MACHINE_NAME` vars can be removed as the instance will already be associated with the online account and the info stored in the config folder.

## Migration from version 7.6

Version 8 of fah-client has been rewritten and has some breaking changes that we can't automatically mitigate in this container.

Unlike v7, v8 no longer bundles a local webgui. The web app is loaded from an online source and can only auto-detect instances that are running on the same machine (bare metal) as the browser. This is not possible in a docker container. Therefore, upgrading to v8 requires registering for an online account, retrieving the account token and setting it in the new env var `ACCOUNT_TOKEN`, along with a friendly name in `MACHINE_NAME`.

## GPU Hardware Acceleration

### Nvidia

Hardware acceleration users for Nvidia will need to install the container runtime provided by Nvidia on their host, instructions can be found here:
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
We automatically add the necessary environment variable that will utilise all the features available on a GPU on the host. Once nvidia container toolkit is installed on your host you will need to re/create the docker container with the nvidia container runtime `--runtime=nvidia` and add an environment variable `-e NVIDIA_VISIBLE_DEVICES=all` (can also be set to a specific gpu's UUID, this can be discovered by running `nvidia-smi --query-gpu=gpu_name,gpu_uuid --format=csv` ). NVIDIA automatically mounts the GPU and drivers from your host into the foldingathome docker container.

## Read-Only Operation

This image can be run with a read-only container filesystem. For details please [read the docs](https://docs.linuxserver.io/misc/read-only/).

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

!!! info

    Unless a parameter is flaged as 'optional', it is *mandatory* and a value must be provided.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
---
services:
  foldingathome:
    image: lscr.io/linuxserver/foldingathome:latest
    container_name: foldingathome
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - ACCOUNT_TOKEN=
      - MACHINE_NAME=
      - CLI_ARGS= #optional
    volumes:
      - /path/to/foldingathome/data:/config
    ports:
      - 7396:7396 #optional
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=foldingathome \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e ACCOUNT_TOKEN= \
  -e MACHINE_NAME= \
  -e CLI_ARGS= `#optional` \
  -p 7396:7396 `#optional` \
  -v /path/to/foldingathome/data:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/foldingathome:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `7396:7396` | Folding@home web gui (redirects to [https://app.foldingathome.org](https://app.foldingathome.org)). |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Etc/UTC` | specify a timezone to use, see this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| `ACCOUNT_TOKEN=` | Register for an account on `https://app.foldingathome.org` and retrieve account token in settings. Required on first start. |
| `MACHINE_NAME=` | Assign a friendly name to this instance (no spaces). Required on first start. |
| `CLI_ARGS=` | Optionally pass additional cli arguments to `fah-client` on container start. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where Folding@home should store its database and config. |

#### Miscellaneous Options

| Parameter | Function |
| :-----:   | --- |
| `--read-only=true` | Run container with a read-only filesystem. Please [read the docs](https://docs.linuxserver.io/misc/read-only/). |

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

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=foldingathome&query=%24.mods%5B%27foldingathome%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=foldingathome "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it foldingathome /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f foldingathome
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' foldingathome
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/foldingathome:latest
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
        docker-compose pull foldingathome
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d foldingathome
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/foldingathome:latest
    ```

* Stop the running container:

    ```bash
    docker stop foldingathome
    ```

* Delete the container:

    ```bash
    docker rm foldingathome
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
git clone https://github.com/linuxserver/docker-foldingathome.git
cd docker-foldingathome
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/foldingathome:latest .
```

The ARM variants can be built on x86_64 hardware and vice versa using `lscr.io/linuxserver/qemu-static`

```bash
docker run --rm --privileged lscr.io/linuxserver/qemu-static --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

To help with development, we generate this dependency graph.

??? info "Init dependency graph"

    ```d2
    "foldingathome:latest": {
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
      init-config -> init-config-end
      init-crontab-config -> init-config-end
      init-foldingathome-video -> init-config-end
      init-config -> init-crontab-config
      init-mods-end -> init-custom-files
      init-adduser -> init-device-perms
      base -> init-envfile
      init-config -> init-foldingathome-config
      init-foldingathome-config -> init-foldingathome-video
      base -> init-migrations
      init-config-end -> init-mods
      init-mods-package-install -> init-mods-end
      init-mods -> init-mods-package-install
      init-adduser -> init-os-end
      init-device-perms -> init-os-end
      init-envfile -> init-os-end
      init-custom-files -> init-services
      init-services -> svc-cron
      svc-cron -> legacy-services
      init-services -> svc-foldingathome
      svc-foldingathome -> legacy-services
    }
    Base Images: {
      "baseimage-ubuntu:noble"
    }
    "foldingathome:latest" <- Base Images
    ```

## Versions

* **10.08.24:** - Add libexpat1 for Nvidia support.
* **25.06.24:** - ***Breaking Changes*** - Please see the Application Setup section for more details. Restructure image for F@H v8.
* **15.06.24:** - Rebase to Ubuntu Noble, add optional cli args.
* **14.12.22:** - Rebase to Ubuntu Jammy, migrate to s6v3.
* **15.01.22:** - Rebase to Ubuntu Focal. Add arm64v8 builds (cpu only). Increase verbosity about gpu driver permission settings.
* **09.01.21:** - Add nvidia.icd.
* **14.04.20:** - Add Folding@home donation links.
* **20.03.20:** - Initial release.
