---
title: quassel-web
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-quassel-web/blob/master/.github/CONTRIBUTING.md -->
# DEPRECATION NOTICE 
This image is deprecated. We will not offer support for this image and it will not be updated.


# [linuxserver/quassel-web](https://github.com/linuxserver/docker-quassel-web)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Fquassel-web?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-quassel-web.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-quassel-web)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-quassel-web.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-quassel-web/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-quassel-web/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-quassel-web/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/quassel-web)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/quassel-web.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/quassel-web)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/quassel-web.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/quassel-web)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-quassel-web%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-quassel-web/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fquassel-web%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/quassel-web/latest/index.html)

[Quassel-web](https://github.com/magne4000/quassel-webserver) is a web client for Quassel.  Note that a Quassel-Core instance is required, we have a container available [here.](https://hub.docker.com/r/linuxserver/quassel-core/)

[![quassel-web](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/quassel-web-banner.png)](https://github.com/magne4000/quassel-webserver)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/quassel-web:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64v8-\<version tag\> |
| armhf | ❌ | |

## Application Setup

By default this container webui will be available on `https://$SERVER_IP:64443`. To setup this container you can either use the environment variables we recommend or manually setup the configuration file by leaving out the `QUASSEL_CORE` environment variable among others.
The configuration file using this method can be found at:

```text
/config/settings-user.js
```

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
  quassel-web:
    image: lscr.io/linuxserver/quassel-web:latest
    container_name: quassel-web
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - QUASSEL_CORE=192.168.1.10 #optional
      - QUASSEL_PORT=4242 #optional
      - QUASSEL_HTTPS= #optional
      - URL_BASE=/quassel #optional
    volumes:
      - /path/to/quassel-web/data:/config
    ports:
      - 64080:64080 #optional
      - 64443:64443 #optional
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=quassel-web \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e QUASSEL_CORE=192.168.1.10 `#optional` \
  -e QUASSEL_PORT=4242 `#optional` \
  -e QUASSEL_HTTPS= `#optional` \
  -e URL_BASE=/quassel `#optional` \
  -p 64080:64080 `#optional` \
  -p 64443:64443 `#optional` \
  -v /path/to/quassel-web/data:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/quassel-web:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `64080:64080` | Quassel-web http webui |
| `64443:64443` | Quassel-web https webui |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Etc/UTC` | specify a timezone to use, see this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| `QUASSEL_CORE=192.168.1.10` | specify the URL or IP address of your Quassel Core instance |
| `QUASSEL_PORT=4242` | specify the port of your Quassel Core instance |
| `QUASSEL_HTTPS=` | Set to `true` to have Quassel web serve over https on port 64443 instead of http on port 64080. |
| `URL_BASE=/quassel` | Specify a url-base in reverse proxy setups ie. `/quassel` |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | this will store config on the docker host |

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

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=quassel-web&query=%24.mods%5B%27quassel-web%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=quassel-web "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it quassel-web /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f quassel-web
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' quassel-web
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/quassel-web:latest
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
        docker-compose pull quassel-web
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d quassel-web
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/quassel-web:latest
    ```

* Stop the running container:

    ```bash
    docker stop quassel-web
    ```

* Delete the container:

    ```bash
    docker rm quassel-web
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
git clone https://github.com/linuxserver/docker-quassel-web.git
cd docker-quassel-web
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/quassel-web:latest .
```

The ARM variants can be built on x86_64 hardware and vice versa using `lscr.io/linuxserver/qemu-static`

```bash
docker run --rm --privileged lscr.io/linuxserver/qemu-static --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

To help with development, we generate this dependency graph.

??? info "Init dependency graph"

    ```d2
    "quassel-web:latest": {
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
      init-quassel-web-config -> init-config-end
      init-os-end -> init-crontab-config
      init-mods-end -> init-custom-files
      init-config-end -> init-deprecate
      base -> init-envfile
      base -> init-migrations
      base -> init-mods
      init-config-end -> init-mods
      init-mods -> init-mods-end
      init-mods-package-install -> init-mods-end
      init-mods -> init-mods-package-install
      base -> init-os-end
      init-adduser -> init-os-end
      init-envfile -> init-os-end
      init-migrations -> init-os-end
      init-config -> init-quassel-web-config
      init-custom-files -> init-services
      init-deprecate -> init-services
      init-mods-end -> init-services
      init-services -> svc-cron
      svc-cron -> legacy-services
      init-services -> svc-quassel-web
      svc-quassel-web -> legacy-services
    }
    Base Images: {
      "baseimage-alpine:3.20"
    }
    "quassel-web:latest" <- Base Images
    ```

## Versions

* **26.12.24:** - Deprecate.
* **25.05.24:** - Rebase to Alpine 3.20.
* **10.11.23:** - Rebase to Alpine 3.18. Rename settings-user.js to .cjs to match upstream.
* **06.07.23:** - Deprecate armhf. As announced [here](https://www.linuxserver.io/blog/a-farewell-to-arm-hf)
* **13.02.23:** - Rebasing to Alpine 3.17, migrate to s6v3.
* **12.02.22:** - Rebasing to alpine 3.15.
* **01.06.20:** - Rebasing to alpine 3.12.
* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **18.05.19:** - Reconfigure environmental variable setup.
* **28.04.19:** - Initial Release.
