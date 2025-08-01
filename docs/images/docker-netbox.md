---
title: netbox
tags:
    - Administration
    - Business
description: "[Netbox](https://github.com/netbox-community/netbox) is an IP address management (IPAM) and data center infrastructure management (DCIM) tool. Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically to address the needs of network and infrastructure engineers. It is intended to function as a domain-specific source of truth for network operations."
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-netbox/blob/master/.github/CONTRIBUTING.md -->
# [linuxserver/netbox](https://github.com/linuxserver/docker-netbox)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Fnetbox?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-netbox.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-netbox)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-netbox.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-netbox/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-netbox/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-netbox/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/netbox)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/netbox.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/netbox)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/netbox.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/netbox)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-netbox%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-netbox/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fnetbox%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/netbox/latest/index.html)

[Netbox](https://github.com/netbox-community/netbox) is an IP address management (IPAM) and data center infrastructure management (DCIM) tool. Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically to address the needs of network and infrastructure engineers. It is intended to function as a domain-specific source of truth for network operations.

[![netbox](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/netbox-logo.png)](https://github.com/netbox-community/netbox)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/netbox:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64v8-\<version tag\> |

## Application Setup

Netbox requires a postgres database and a redis instance.

Access the WebUI at <your-ip>:8000. For more information, check out [NetBox](https://github.com/netbox-community/netbox).

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

!!! info

    Unless a parameter is flaged as 'optional', it is *mandatory* and a value must be provided.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
---
services:
  netbox:
    image: lscr.io/linuxserver/netbox:latest
    container_name: netbox
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - SUPERUSER_EMAIL=
      - SUPERUSER_PASSWORD=
      - ALLOWED_HOST=
      - DB_NAME=
      - DB_USER=
      - DB_PASSWORD=
      - DB_HOST=
      - DB_PORT=
      - REDIS_HOST=
      - REDIS_PORT=
      - REDIS_PASSWORD=
      - REDIS_DB_TASK=
      - REDIS_DB_CACHE=
      - BASE_PATH= #optional
      - REMOTE_AUTH_ENABLED= #optional
      - REMOTE_AUTH_BACKEND= #optional
      - REMOTE_AUTH_HEADER= #optional
      - REMOTE_AUTH_AUTO_CREATE_USER= #optional
      - REMOTE_AUTH_DEFAULT_GROUPS= #optional
      - REMOTE_AUTH_DEFAULT_PERMISSIONS= #optional
    volumes:
      - /path/to/netbox/config:/config
    ports:
      - 8000:8000
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=netbox \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e SUPERUSER_EMAIL= \
  -e SUPERUSER_PASSWORD= \
  -e ALLOWED_HOST= \
  -e DB_NAME= \
  -e DB_USER= \
  -e DB_PASSWORD= \
  -e DB_HOST= \
  -e DB_PORT= \
  -e REDIS_HOST= \
  -e REDIS_PORT= \
  -e REDIS_PASSWORD= \
  -e REDIS_DB_TASK= \
  -e REDIS_DB_CACHE= \
  -e BASE_PATH= `#optional` \
  -e REMOTE_AUTH_ENABLED= `#optional` \
  -e REMOTE_AUTH_BACKEND= `#optional` \
  -e REMOTE_AUTH_HEADER= `#optional` \
  -e REMOTE_AUTH_AUTO_CREATE_USER= `#optional` \
  -e REMOTE_AUTH_DEFAULT_GROUPS= `#optional` \
  -e REMOTE_AUTH_DEFAULT_PERMISSIONS= `#optional` \
  -p 8000:8000 \
  -v /path/to/netbox/config:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/netbox:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8000:8000` | will map the container's port 8000 to port 8000 on the host |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Etc/UTC` | specify a timezone to use, see this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| `SUPERUSER_EMAIL=` | Email address for `admin` account |
| `SUPERUSER_PASSWORD=` | Password for `admin` account |
| `ALLOWED_HOST=` | The hostname you will use to access the app (i.e., netbox.example.com) |
| `DB_NAME=` | Database name (default: netbox) |
| `DB_USER=` | Database user |
| `DB_PASSWORD=` | Database password |
| `DB_HOST=` | Database host (default: postgres) |
| `DB_PORT=` | Database port (default: 5432) |
| `REDIS_HOST=` | Redis host (default: redis) |
| `REDIS_PORT=` | Redis port number (default: 6379) |
| `REDIS_PASSWORD=` | Redis password (default: none) |
| `REDIS_DB_TASK=` | Redis database ID for tasks (default: 0) |
| `REDIS_DB_CACHE=` | Redis database ID for caching (default: 1) |
| `BASE_PATH=` | The path you will use to access the app (i.e., /netbox, optional, default: none) |
| `REMOTE_AUTH_ENABLED=` | Enable remote authentication (optional, default: False) |
| `REMOTE_AUTH_BACKEND=` | Python path to the custom Django authentication backend to use for external user authentication (optional, default: netbox.authentication.RemoteUserBackend) |
| `REMOTE_AUTH_HEADER=` | Name of the HTTP header which informs NetBox of the currently authenticated user. (optional, default: HTTP_REMOTE_USER) |
| `REMOTE_AUTH_AUTO_CREATE_USER=` | If true, NetBox will automatically create local accounts for users authenticated via a remote service (optional, default: False) |
| `REMOTE_AUTH_DEFAULT_GROUPS=` | The list of groups to assign a new user account when created using remote authentication (optional, default: []) |
| `REMOTE_AUTH_DEFAULT_PERMISSIONS=` | A mapping of permissions to assign a new user account when created using remote authentication (optional, default: {}) |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Persistent config files |

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

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=netbox&query=%24.mods%5B%27netbox%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=netbox "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it netbox /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f netbox
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' netbox
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/netbox:latest
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
        docker-compose pull netbox
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d netbox
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/netbox:latest
    ```

* Stop the running container:

    ```bash
    docker stop netbox
    ```

* Delete the container:

    ```bash
    docker rm netbox
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
git clone https://github.com/linuxserver/docker-netbox.git
cd docker-netbox
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/netbox:latest .
```

The ARM variants can be built on x86_64 hardware and vice versa using `lscr.io/linuxserver/qemu-static`

```bash
docker run --rm --privileged lscr.io/linuxserver/qemu-static --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

To help with development, we generate this dependency graph.

??? info "Init dependency graph"

    ```d2
    "netbox:latest": {
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
      init-netbox-config -> init-config-end
      init-os-end -> init-crontab-config
      init-mods-end -> init-custom-files
      init-adduser -> init-device-perms
      base -> init-envfile
      base -> init-migrations
      base -> init-mods
      init-config-end -> init-mods
      init-mods -> init-mods-end
      init-mods-package-install -> init-mods-end
      init-mods -> init-mods-package-install
      init-config -> init-netbox-config
      base -> init-os-end
      init-adduser -> init-os-end
      init-device-perms -> init-os-end
      init-envfile -> init-os-end
      init-migrations -> init-os-end
      init-custom-files -> init-services
      init-mods-end -> init-services
      init-services -> svc-cron
      svc-cron -> legacy-services
      svc-netbox-prepare -> svc-netbox
      svc-netbox -> legacy-services
      init-services -> svc-netbox-prepare
      svc-netbox-prepare -> legacy-services
    }
    Base Images: {
      "baseimage-alpine:3.20"
    }
    "netbox:latest" <- Base Images
    ```

## Versions

* **26.08.24:** - Restructure init to allow for plugins as mods.
* **16.07.24:** - Add required packages for LDAP support.
* **01.06.24:** - Rebase to Alpine 3.20.
* **23.12.23:** - Rebase to Alpine 3.19.
* **11.06.23:** - Rebase to Alpine 3.18, deprecate armhf.
* **14.05.23:** - Build local docs on first run.
* **05.03.23:** - Rebase to Alpine 3.17.
* **02.11.22:** - Rebase to Alpine 3.16, migrate to s6v3.
* **01.08.22:** - Remove py3-pillow, add tiff to fix deps.
* **26.07.22:** - Add py3-pillow package back on arm to fix build issue.
* **10.12.21:** - Remove py3-pillow package to fix dependency issue with 3.2.0.
* **10.12.21:** - Rebase to Alpine 3.15.
* **26.04.21:** - Added Redis database environment variables.
* **03.02.21:** - Added remote authentication environment variables.
* **02.01.21:** - Added BASE_PATH environment variable.
* **23.08.20:** - Initial Release.
