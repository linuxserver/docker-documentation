---
title: diskover
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-diskover/blob/master/.github/CONTRIBUTING.md -->
# [linuxserver/diskover](https://github.com/linuxserver/docker-diskover)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Fdiskover?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh/gateway/linuxserver-ci/docker/linuxserver%2Fdiskover)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-diskover.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-diskover)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-diskover.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-diskover/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-diskover/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-diskover/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/diskover)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/diskover.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/diskover)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/diskover.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/diskover)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-diskover%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-diskover/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fdiskover%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/diskover/latest/index.html)

[diskover](https://github.com/diskoverdata/diskover-community) is an open source file system indexer that uses Elasticsearch to index and manage data across heterogeneous storage systems.

[![diskover](https://raw.githubusercontent.com/diskoverdata/diskover-community/master/diskover-web/public/images/diskover.png)](https://github.com/diskoverdata/diskover-community)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/diskover:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64v8-\<version tag\> |
| armhf | ❌ | |

## Application Setup

This application is dependent on an ElasticSearch instance. Please see the example compose file for additional information.

The default username is diskover with the password of **darkdata**, access the container at `http://<host-ip>/`. The UI may be unusable until a valid index has been created.

The default diskover-web Constants.php file located at `/config/diskover-web.conf.d/Constants.php` will need to be edited to allow diskover-web to communicate with the ElasticSearch container. The following entries will need to be edited:
* `const ES_HOST = 'elasticsearch';`
* `const ES_PORT = 9200;`

The application doesn't start an index by default. A crontab is created inside of the `/config` directory and can be set up to run automated indexes of `/data`. Changes to this crontab file require a restart to apply. You can also manually run an index by executing `/app/diskover/diskover.py` either in interactive or detached mode:

* `docker exec -u abc -d diskover python3 /app/diskover/diskover.py -i diskover-my_index_name /data` Will run an index in the background
* `docker exec -u abc -it diskover python3 /app/diskover/diskover.py -i diskover-my_index_name /data` Will run an index in the foreground

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
version: '2'
services:
  diskover:
    image: lscr.io/linuxserver/diskover
    container_name: diskover
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/New_York
      - ES_HOST=elasticsearch
      - ES_PORT=9200
    volumes:
      - /path/to/diskover/config:/config
      - /path/to/diskover/data:/data
    ports:
      - 80:80
    mem_limit: 4096m
    restart: unless-stopped
    depends_on:
      - elasticsearch
  elasticsearch:
    container_name: elasticsearch
    image: docker.elastic.co/elasticsearch/elasticsearch:7.10.2
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=true
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms1g -Xmx1g"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - /path/to/esdata:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
    depends_on:
      - elasticsearch-helper
    restart: unless-stopped
  elasticsearch-helper:
    image: alpine
    command: sh -c "sysctl -w vm.max_map_count=262144"
    privileged: true
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=diskover \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e ES_HOST=elasticsearch \
  -e ES_PORT=9200 \
  -e ES_USER=elastic \
  -e ES_PASS=changeme \
  -p 80:80 \
  -v /path/to/diskover/config:/config \
  -v /path/to/diskover/data:/data \
  --restart unless-stopped \
  lscr.io/linuxserver/diskover:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | diskover Web UI |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Etc/UTC` | specify a timezone to use, see this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| `ES_HOST=elasticsearch` | ElasticSearch host (optional) |
| `ES_PORT=9200` | ElasticSearch port (optional) |
| `ES_USER=elastic` | ElasticSearch username (optional) |
| `ES_PASS=changeme` | ElasticSearch password (optional) |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Persistent config files |
| `/data` | Default mount point to crawl |

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

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=diskover&query=%24.mods%5B%27diskover%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=diskover "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it diskover /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f diskover
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' diskover
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/diskover:latest
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
        docker-compose pull diskover
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d diskover
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/diskover:latest
    ```

* Stop the running container:

    ```bash
    docker stop diskover
    ```

* Delete the container:

    ```bash
    docker rm diskover
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
      --run-once diskover
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
git clone https://github.com/linuxserver/docker-diskover.git
cd docker-diskover
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/diskover:latest .
```

The ARM variants can be built on x86_64 hardware using `multiarch/qemu-user-static`

```bash
docker run --rm --privileged multiarch/qemu-user-static:register --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

## Versions

* **25.05.23:** - Rebase to Alpine 3.18, deprecate armhf.
* **13.04.23:** - Move ssl.conf include to default.conf.
* **02.03.23:** - Set permissions on crontabs during init.
* **20.08.22:** - Rebasing to alpine 3.17 with php8.1. Restructure nginx configs ([see changes announcement](https://info.linuxserver.io/issues/2022-08-20-nginx-base)).
* **25.02.22:** - Add php7-sqlite3 to support rc4 release.
* **03.11.21:** - Added more support for potential config files.
* **31.10.21:** - Added xpack.security variable to ElasticSearch; added instructions to edit Constants.php in diskover; corrected command needed to manually generate an index in diskover
* **11.10.21:** - Updated to diskover-community v2.
* **19.11.20:** - Fix pip packages.
* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **12.04.19:** - Rebase to Alpine 3.9.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **01.11.18:** - Initial Release.