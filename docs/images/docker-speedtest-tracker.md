---
title: speedtest-tracker
tags:
    - Monitoring
description: "[Speedtest-tracker](https://github.com/alexjustesen/speedtest-tracker) is a self-hosted internet performance tracking application that runs speedtest checks against Ookla's Speedtest service."
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-speedtest-tracker/blob/main/.github/CONTRIBUTING.md -->
# [linuxserver/speedtest-tracker](https://github.com/linuxserver/docker-speedtest-tracker)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Fspeedtest-tracker?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-speedtest-tracker.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-speedtest-tracker)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-speedtest-tracker.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-speedtest-tracker/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-speedtest-tracker/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-speedtest-tracker/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/speedtest-tracker)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/speedtest-tracker.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/speedtest-tracker)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/speedtest-tracker.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/speedtest-tracker)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-speedtest-tracker%2Fjob%2Fmain%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-speedtest-tracker/job/main/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fspeedtest-tracker%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/speedtest-tracker/latest/index.html)

[Speedtest-tracker](https://github.com/alexjustesen/speedtest-tracker) is a self-hosted internet performance tracking application that runs speedtest checks against Ookla's Speedtest service.

[![speedtest-tracker](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/speedtest-tracker-logo.png)](https://github.com/alexjustesen/speedtest-tracker)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/speedtest-tracker:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64v8-\<version tag\> |

## Application Setup

Access the web UI at `<your-ip>:80`, the default credentials are admin@example.com / password

For more information check out the [project documentation](https://docs.speedtest-tracker.dev/).

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

!!! info

    Unless a parameter is flaged as 'optional', it is *mandatory* and a value must be provided.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
---
services:
  speedtest-tracker:
    image: lscr.io/linuxserver/speedtest-tracker:latest
    container_name: speedtest-tracker
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - APP_KEY=
      - APP_URL=
      - DB_CONNECTION=sqlite
      - SPEEDTEST_SCHEDULE=
      - SPEEDTEST_SERVERS=
      - DB_HOST= #optional
      - DB_PORT= #optional
      - DB_DATABASE= #optional
      - DB_USERNAME= #optional
      - DB_PASSWORD= #optional
      - DISPLAY_TIMEZONE=Etc/UTC #optional
      - PRUNE_RESULTS_OLDER_THAN=0 #optional
    volumes:
      - /path/to/speedtest-tracker/data:/config
    ports:
      - 80:80
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=speedtest-tracker \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e APP_KEY= \
  -e APP_URL= \
  -e DB_CONNECTION=sqlite \
  -e SPEEDTEST_SCHEDULE= \
  -e SPEEDTEST_SERVERS= \
  -e DB_HOST= `#optional` \
  -e DB_PORT= `#optional` \
  -e DB_DATABASE= `#optional` \
  -e DB_USERNAME= `#optional` \
  -e DB_PASSWORD= `#optional` \
  -e DISPLAY_TIMEZONE=Etc/UTC `#optional` \
  -e PRUNE_RESULTS_OLDER_THAN=0 `#optional` \
  -p 80:80 \
  -v /path/to/speedtest-tracker/data:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/speedtest-tracker:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80:80` | Web UI |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Etc/UTC` | specify a timezone to use, see this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| `APP_KEY=` | App key used for encrypting stored data. You can generate a key at [https://speedtest-tracker.dev](https://speedtest-tracker.dev) |
| `APP_URL=` | The IP:port or URL your application will be accessed on (ie. `http://192.168.1.1:6875` or `https://bookstack.mydomain.com` |
| `DB_CONNECTION=sqlite` | Set the database type to use. `sqlite`, `pgsql`, or `mysql` |
| `SPEEDTEST_SCHEDULE=` | Set the test schedule in cron format. e.g. `0 */6 * * *` |
| `SPEEDTEST_SERVERS=` | A comma-separated list of server IDs to test against. Run `docker run -it --rm --entrypoint /bin/bash lscr.io/linuxserver/speedtest-tracker:latest list-servers` to get a list of nearby servers. |
| `DB_HOST=` | Database hostname (postgres/mysql). |
| `DB_PORT=` | Database port (postgres/mysql). |
| `DB_DATABASE=` | Database name (postgres/mysql). |
| `DB_USERNAME=` | Database username (postgres/mysql). |
| `DB_PASSWORD=` | Database password (postgres/mysql). |
| `DISPLAY_TIMEZONE=Etc/UTC` | Timezone for the UI. |
| `PRUNE_RESULTS_OLDER_THAN=0` | Days to keep test results. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains speedtest-tracker config and database, if using sqlite. |

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

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=speedtest-tracker&query=%24.mods%5B%27speedtest-tracker%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=speedtest-tracker "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it speedtest-tracker /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f speedtest-tracker
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' speedtest-tracker
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/speedtest-tracker:latest
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
        docker-compose pull speedtest-tracker
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d speedtest-tracker
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/speedtest-tracker:latest
    ```

* Stop the running container:

    ```bash
    docker stop speedtest-tracker
    ```

* Delete the container:

    ```bash
    docker rm speedtest-tracker
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
git clone https://github.com/linuxserver/docker-speedtest-tracker.git
cd docker-speedtest-tracker
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/speedtest-tracker:latest .
```

The ARM variants can be built on x86_64 hardware and vice versa using `lscr.io/linuxserver/qemu-static`

```bash
docker run --rm --privileged lscr.io/linuxserver/qemu-static --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

To help with development, we generate this dependency graph.

??? info "Init dependency graph"

    ```d2
    "speedtest-tracker:latest": {
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
      init-nginx-end -> init-config
      init-os-end -> init-config
      init-config -> init-config-end
      init-crontab-config -> init-config-end
      init-speedtest-tracker-config -> init-config-end
      init-config -> init-crontab-config
      init-mods-end -> init-custom-files
      init-adduser -> init-device-perms
      base -> init-envfile
      init-os-end -> init-folders
      init-php -> init-keygen
      base -> init-migrations
      init-config-end -> init-mods
      init-mods-package-install -> init-mods-end
      init-mods -> init-mods-package-install
      init-samples -> init-nginx
      init-version-checks -> init-nginx-end
      init-adduser -> init-os-end
      init-device-perms -> init-os-end
      init-envfile -> init-os-end
      init-keygen -> init-permissions
      init-nginx -> init-php
      init-folders -> init-samples
      init-custom-files -> init-services
      init-nginx-end -> init-speedtest-tracker-config
      init-permissions -> init-version-checks
      init-services -> svc-cron
      svc-cron -> legacy-services
      init-services -> svc-nginx
      svc-nginx -> legacy-services
      init-services -> svc-php-fpm
      svc-php-fpm -> legacy-services
      init-services -> svc-speedtest-tracker
      svc-speedtest-tracker -> legacy-services
    }
    Base Images: {
      "baseimage-alpine-nginx:3.22" <- "baseimage-alpine:3.22"
    }
    "speedtest-tracker:latest" <- Base Images
    ```

## Versions

* **05.07.25:** - Rebase to Alpine 3.22.
* **20.12.24:** - Rebase to Alpine 3.21.
* **07.06.24:** - Cache Filament components and added APP_KEY as a required param.
* **27.05.24:** - Existing users should update their nginx confs to avoid http2 deprecation warnings.
* **24.05.24:** - Rebase to Alpine 3.20.
* **16.04.24:** - Rebase to Alpine 3.19, upgrade to php 8.3.
* **10.02.24:** - Initial Release.
