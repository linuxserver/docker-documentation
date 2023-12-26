---
title: plex-meta-manager
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-plex-meta-manager/blob/main/.github/CONTRIBUTING.md -->
# [linuxserver/plex-meta-manager](https://github.com/linuxserver/docker-plex-meta-manager)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Fplex-meta-manager?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh/gateway/linuxserver-ci/docker/linuxserver%2Fplex-meta-manager)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-plex-meta-manager.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-plex-meta-manager)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-plex-meta-manager.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-plex-meta-manager/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-plex-meta-manager/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-plex-meta-manager/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/plex-meta-manager)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/plex-meta-manager.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/plex-meta-manager)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/plex-meta-manager.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/plex-meta-manager)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-plex-meta-manager%2Fjob%2Fmain%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-plex-meta-manager/job/main/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fplex-meta-manager%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/plex-meta-manager/latest/index.html)

[Plex-meta-manager](https://github.com/meisnate12/Plex-Meta-Manager) is a Python 3 script that can be continuously run using YAML configuration files to update on a schedule the metadata of the movies, shows, and collections in your libraries as well as automatically build collections based on various methods all detailed in the wiki.

[![plex-meta-manager](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/plex-meta-manager-banner.png)](https://github.com/meisnate12/Plex-Meta-Manager)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/plex-meta-manager:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | ✅ | Stable releases. |
| develop | ✅ | Latest commits from the develop branch |
| nightly | ✅ | Latest commits from the nightly branch |

## Application Setup

There is a [walkthrough](https://metamanager.wiki/en/latest/home/guides/docker.html#setting-up-the-initial-config-file) available to help get you up and running.

This image supports all of the environment variables listed [here](https://metamanager.wiki/en/latest/home/environmental.html) and all commandline arguments.

To perform a one-time run use `docker run` (or `docker-compose run`) with the `--rm` and `-e PMM_RUN=True` arguments. This will cause the container to process your config immediately instead of waiting for the scheduled time, and delete the old container after completion.

For more information see the [official wiki](https://metamanager.wiki).

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
---
version: "2.1"
services:
  plex-meta-manager:
    image: lscr.io/linuxserver/plex-meta-manager:latest
    container_name: plex-meta-manager
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - PMM_CONFIG=/config/config.yml #optional
      - PMM_TIME=03:00 #optional
      - PMM_RUN=False #optional
      - PMM_TEST=False #optional
      - PMM_NO_MISSING=False #optional
    volumes:
      - /path/to/appdata/config:/config
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=plex-meta-manager \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e PMM_CONFIG=/config/config.yml `#optional` \
  -e PMM_TIME=03:00 `#optional` \
  -e PMM_RUN=False `#optional` \
  -e PMM_TEST=False `#optional` \
  -e PMM_NO_MISSING=False `#optional` \
  -v /path/to/appdata/config:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/plex-meta-manager:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Etc/UTC` | specify a timezone to use, see this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| `PMM_CONFIG=/config/config.yml` | Specify a custom config file to use. |
| `PMM_TIME=03:00` | Comma-separated list of times to update each day. Format: `HH:MM`. |
| `PMM_RUN=False` | Set to `True` to run without the scheduler. |
| `PMM_TEST=False` | Set to `True` to run in debug mode with only collections that have `test: true`. |
| `PMM_NO_MISSING=False` | Set to `True` to run without any of the missing movie/show functions. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Local path for plex-meta-manager config files. |

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

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=plex-meta-manager&query=%24.mods%5B%27plex-meta-manager%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=plex-meta-manager "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it plex-meta-manager /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f plex-meta-manager
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' plex-meta-manager
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/plex-meta-manager:latest
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
        docker-compose pull plex-meta-manager
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d plex-meta-manager
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/plex-meta-manager:latest
    ```

* Stop the running container:

    ```bash
    docker stop plex-meta-manager
    ```

* Delete the container:

    ```bash
    docker rm plex-meta-manager
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
      --run-once plex-meta-manager
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
git clone https://github.com/linuxserver/docker-plex-meta-manager.git
cd docker-plex-meta-manager
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/plex-meta-manager:latest .
```

The ARM variants can be built on x86_64 hardware using `multiarch/qemu-user-static`

```bash
docker run --rm --privileged multiarch/qemu-user-static:register --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

## Versions

* **10.06.23:** - Rebase to Alpine 3.18, deprecate armhf.
* **05.03.23:** - Add nightly branch.
* **11.12.22:** - Rebase master to Alpine 3.17.
* **08.11.22:** - Add develop branch.
* **25.10.22:** - Support commandline args and relative paths.
* **03.10.22:** - Rebase to Alpine 3.16, migrate to s6v3.
* **30.01.22:** - Initial Release.