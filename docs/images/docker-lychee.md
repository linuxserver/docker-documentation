---
title: lychee
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-lychee/blob/master/.github/CONTRIBUTING.md -->
# [linuxserver/lychee](https://github.com/linuxserver/docker-lychee)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Flychee?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh/gateway/linuxserver-ci/docker/linuxserver%2Flychee)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-lychee.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-lychee)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-lychee.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-lychee/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-lychee/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-lychee/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/lychee)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/lychee.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/lychee)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/lychee.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/lychee)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-lychee%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-lychee/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Flychee%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/lychee/latest/index.html)

[Lychee](https://lycheeorg.github.io/) is a free photo-management tool, which runs on your server or web-space. Installing is a matter of seconds. Upload, manage and share photos like from a native application. Lychee comes with everything you need and all your photos are stored securely."

### UPGRADE WARNING

Please note that the v4 upgrade process resets ALL password-protected albums. Any albums that were made public with a password will need to be re-secured.

[![lychee](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/lychee-icon.png)](https://lycheeorg.github.io/)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/lychee:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64v8-\<version tag\> |
| armhf | ❌ | |

## Application Setup

**This image will not work with a prefilled `/pictures` mount, lychee wants total control over this folder**

Setup mysql/mariadb and account via the webui, accessible at http://SERVERIP:PORT
More info at [lychee](https://lycheeorg.github.io/).

### Customization

In certain scenarios, you might need to change the default settings of Lychee. For instance, if you encounter limitations when uploading large files, you can increase this limit.

#### Increasing Upload Limit

The upload limit is defined in the `user.ini` file located in the config directory (`/config`). You can increase this limit by modifying the following values:

```ini
post_max_size = 500M
upload_max_filesize = 500M
```

After making these changes, you'll need to restart the Docker container for the changes to take effect. Here's how to do it:

**Please note that these changes might have implications on your server's performance, depending on its available resources. Thus, it's recommended to modify these settings with caution.**

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
version: "3"
services:
  mariadb:
    image: lscr.io/linuxserver/mariadb:latest
    container_name: lychee_mariadb
    restart: always
    volumes:
      - /path/to/mariadb/data:/config
    environment:
      - MYSQL_ROOT_PASSWORD=rootpassword
      - MYSQL_DATABASE=lychee
      - MYSQL_USER=lychee
      - MYSQL_PASSWORD=dbpassword
      - PGID=1000
      - PUID=1000
      - TZ=Europe/London
  lychee:
    image: lscr.io/linuxserver/lychee:latest
    container_name: lychee
    restart: always
    depends_on:
      - mariadb
    volumes:
      - /path/to/config:/config
      - /path/to/pictures:/pictures
    environment:
      - DB_CONNECTION=mysql
      - DB_HOST=mariadb
      - DB_PORT=3306
      - DB_USERNAME=lychee
      - DB_PASSWORD=dbpassword
      - DB_DATABASE=lychee
      - PGID=1000
      - PUID=1000
      - TZ=Europe/London
    ports:
      - 80:80
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=lychee \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e DB_CONNECTION=mysql \
  -e DB_HOST=mariadb \
  -e DB_PORT=3306 \
  -e DB_USERNAME=lychee \
  -e DB_PASSWORD=dbpassword \
  -e DB_DATABASE=lychee \
  -p 80:80 \
  -v /path/to/config:/config \
  -v /path/to/pictures:/pictures \
  --restart unless-stopped \
  lscr.io/linuxserver/lychee:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | http gui |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Etc/UTC` | specify a timezone to use, see this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| `DB_CONNECTION=mysql` | for specifying the database type |
| `DB_HOST=mariadb` | for specifying the database host |
| `DB_PORT=3306` | for specifying the database port |
| `DB_USERNAME=lychee` | for specifying the database user |
| `DB_PASSWORD=dbpassword` | for specifying the database password |
| `DB_DATABASE=lychee` | for specifying the database to be used |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains all relevant configuration files. |
| `/pictures` | Where lychee will store uploaded data. |

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

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=lychee&query=%24.mods%5B%27lychee%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=lychee "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it lychee /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f lychee
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lychee
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/lychee:latest
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
        docker-compose pull lychee
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d lychee
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/lychee:latest
    ```

* Stop the running container:

    ```bash
    docker stop lychee
    ```

* Delete the container:

    ```bash
    docker rm lychee
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
      --run-once lychee
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
git clone https://github.com/linuxserver/docker-lychee.git
cd docker-lychee
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/lychee:latest .
```

The ARM variants can be built on x86_64 hardware using `multiarch/qemu-user-static`

```bash
docker run --rm --privileged multiarch/qemu-user-static:register --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

## Versions

* **25.12.23:** - Existing users should update: site-confs/default.conf - Cleanup default site conf. Build npm dependencies into image.
* **25.05.23:** - Rebase to Alpine 3.18, deprecate armhf.
* **13.04.23:** - Move ssl.conf include to default.conf.
* **11.01.23:** - Rebasing to alpine 3.17 with php8.1. Restructure nginx configs ([see changes announcement](https://info.linuxserver.io/issues/2022-08-20-nginx-base)). Switch to git clone as builds fail with the release artifact.
* **13.05.21:** - Make readme clearer.
* **18.04.21:** - Add php-intl for v4.3.
* **31.01.21:** - Add jpegoptim.
* **15.01.21:** - Rebase to alpine 3.13, add php7-ctype.
* **10.07.20:** - Upgrade to Lychee v4 and rebased to alpine 3.12.
* **19.12.19:** - Rebasing to alpine 3.11.
* **23.10.19:** - Increase fastcgi timeouts (existing users need to manually update).
* **19.09.19:** - Update project website url.
* **28.06.19:** - Rebasing to alpine 3.10.
* **05.05.19:** - Rebase to alpine 3.9, use new armv7 image format.
* **21.01.18:** - Added ffmpeg for video thumbnail creation, switched to installing zip release instead of source tarball, created small thumbnails folder, switched to dynamic readme.
* **14.01.19:** - Adding pipeline logic and multi arch..
* **04.09.18:** - Rebase to alpine 3.8, switch to LycheeOrg repository.
* **08.01.18:** - Rebase to alpine 3.7.
* **25.05.17:** - Rebase to alpine 3.6.
* **03.05.17:** - Use repo pinning to better solve dependencies, use repo version of php7-imagick.
* **12.02.17:** - Initial Release.