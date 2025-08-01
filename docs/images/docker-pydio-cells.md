---
title: pydio-cells
tags:
    - File Sharing
description: "[Pydio-cells](https://pydio.com/) is the nextgen file sharing platform for organizations. It is a full rewrite of the Pydio project using the Go language following a micro-service architecture."
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-pydio-cells/blob/master/.github/CONTRIBUTING.md -->
# [linuxserver/pydio-cells](https://github.com/linuxserver/docker-pydio-cells)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Fpydio-cells?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-pydio-cells.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-pydio-cells)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-pydio-cells.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-pydio-cells/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-pydio-cells/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-pydio-cells/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/pydio-cells)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/pydio-cells.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/pydio-cells)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/pydio-cells.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/pydio-cells)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-pydio-cells%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-pydio-cells/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fpydio-cells%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/pydio-cells/latest/index.html)

[Pydio-cells](https://pydio.com/) is the nextgen file sharing platform for organizations. It is a full rewrite of the Pydio project using the Go language following a micro-service architecture.

[![pydio-cells](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/pydio-cells-icon.png)](https://pydio.com/)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/pydio-cells:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64v8-\<version tag\> |

## Application Setup

You must first create a mysql database for Pydio Cells. Using our [mariadb image](https://hub.docker.com/r/linuxserver/mariadb) is recommended.

Then access the web gui setup wizard at `https://SERVER_IP:8080` if accessing locally (must set `SERVER_IP` env var), or at `https://pydio-cells.domain.com` if reverse proxying.

### Strict reverse proxies

This image uses a self-signed certificate by default. This naturally means the scheme is `https`.
If you are using a reverse proxy which validates certificates, you need to [disable this check for the container](https://docs.linuxserver.io/faq#strict-proxy).

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

!!! info

    Unless a parameter is flaged as 'optional', it is *mandatory* and a value must be provided.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
---
services:
  pydio-cells:
    image: lscr.io/linuxserver/pydio-cells:latest
    container_name: pydio-cells
    hostname: pydio-cells
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - EXTERNALURL=yourdomain.url
      - SERVER_IP=0.0.0.0 #optional
    volumes:
      - /path/to/pydio-cells/config:/config
    ports:
      - 8080:8080
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=pydio-cells \
  --hostname=pydio-cells \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e EXTERNALURL=yourdomain.url \
  -e SERVER_IP=0.0.0.0 `#optional` \
  -p 8080:8080 \
  -v /path/to/pydio-cells/config:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/pydio-cells:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8080:8080` | Http port |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Etc/UTC` | specify a timezone to use, see this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| `EXTERNALURL=yourdomain.url` | The external url you would like to use to access Pydio Cells (Can be https://domain.url or https://IP:PORT). |
| `SERVER_IP=0.0.0.0` | Enter the LAN IP of the docker server. Required for local access by IP, added to self signed cert as SAN (not required if accessing only through reverse proxy). |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | All the config files reside here. |

#### Miscellaneous Options

| Parameter | Function |
| :-----:   | --- |
| `--hostname=` | Pydio Cells uses the hostname to verify local files. This setting is required and should not be changed after it has been set. |

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

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pydio-cells&query=%24.mods%5B%27pydio-cells%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=pydio-cells "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it pydio-cells /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f pydio-cells
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' pydio-cells
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/pydio-cells:latest
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
        docker-compose pull pydio-cells
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d pydio-cells
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/pydio-cells:latest
    ```

* Stop the running container:

    ```bash
    docker stop pydio-cells
    ```

* Delete the container:

    ```bash
    docker rm pydio-cells
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
git clone https://github.com/linuxserver/docker-pydio-cells.git
cd docker-pydio-cells
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/pydio-cells:latest .
```

The ARM variants can be built on x86_64 hardware and vice versa using `lscr.io/linuxserver/qemu-static`

```bash
docker run --rm --privileged lscr.io/linuxserver/qemu-static --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

To help with development, we generate this dependency graph.

??? info "Init dependency graph"

    ```d2
    "pydio-cells:latest": {
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
      init-pydio-cells-config -> init-config-end
      init-config -> init-crontab-config
      init-mods-end -> init-custom-files
      init-adduser -> init-device-perms
      base -> init-envfile
      base -> init-migrations
      init-config-end -> init-mods
      init-mods-package-install -> init-mods-end
      init-mods -> init-mods-package-install
      init-adduser -> init-os-end
      init-device-perms -> init-os-end
      init-envfile -> init-os-end
      init-config -> init-pydio-cells-config
      init-custom-files -> init-services
      init-services -> svc-cron
      svc-cron -> legacy-services
      init-services -> svc-pydio-cells
      svc-pydio-cells -> legacy-services
    }
    Base Images: {
      "baseimage-alpine:3.22"
    }
    "pydio-cells:latest" <- Base Images
    ```

## Versions

* **27.07.25:** - Rebasing to Alpine 3.22.
* **27.06.24:** - Rebasing to Alpine 3.20.
* **14.03.24:** - Rebasing to alpine 3.19. Grpc port defaults to 8080.
* **11.10.23:** - Rebasing to alpine 3.18. Build on alpine edge with Go 1.21.
* **06.07.23:** - Deprecate armhf. As announced [here](https://www.linuxserver.io/blog/a-farewell-to-arm-hf)
* **01.12.22:** - Rebasing to alpine 3.17. Adding multi-arch support. Updating cli arguments for v4 compatibility.
* **19.10.22:** - Rebasing to alpine 3.16. Upgrading to s6v3. Updating build instructions for v4.
* **19.09.22:** - Rebasing to alpine 3.15.
* **23.01.21:** - Rebasing to alpine 3.13.
* **01.06.20:** - Rebasing to alpine 3.12.
* **18.04.20:** - Switch to https as default (only affects new installs). Add self signed cert, add `SERVER_IP` var for adding to cert as SAN. Add optional gRPC port mapping for CellsSync.
* **17.04.20:** - Update compile options, previous release was broken for new installs.
* **19.12.19:** - Rebasing to alpine 3.11.
* **12.12.19:** - Initial Release
