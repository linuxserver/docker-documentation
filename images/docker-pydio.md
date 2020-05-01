# [linuxserver/pydio](https://github.com/linuxserver/docker-pydio)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-pydio.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pydio)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-pydio.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pydio/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-pydio/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-pydio/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/pydio)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/pydio.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/pydio "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/pydio.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/pydio)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/pydio.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/pydio)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-pydio/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-pydio/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/pydio/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/pydio/latest/index.html)

[Pydio](https://pydio.com/) (formerly AjaXplorer) is a mature open source software solution for file sharing and synchronization. With intuitive user interfaces (web / mobile / desktop), Pydio provides enterprise-grade features to gain back control and privacy of your data: user directory connectors, legacy filesystems drivers, comprehensive admin interface, and much more.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/pydio` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=pydio \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 443:443 \
  -v <path to data>:/config \
  -v <path to data>:/data \
  --restart unless-stopped \
  linuxserver/pydio
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  pydio:
    image: linuxserver/pydio
    container_name: pydio
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <path to data>:/data
    ports:
      - 443:443
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `443` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where pydio should store it's configuration files. |
| `/data` | Where pydio should store uploaded files. |




## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

You must create a user and database for pydio to use in a mysql/mariadb or postgresql server. You can use sqlite with no further config needed, but this should only be considered for testing purposes.
In the setup page for database, use the ip address rather than hostname...

Self-signed keys are generated the first time you run the container and can be found in /config/keys , if needed, you can replace them with your own.

For public link sharing to function correctly be sure to change the Detected Server Url to the URL of your pydio instance in the setup wizard.

For email settings edit the file /config/ssmtp.conf and restart the container.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27pydio%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=pydio "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it pydio /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f pydio`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' pydio`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/pydio`

## Versions

* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **11.02.19:** - Add pipeline logic and multi arch, rebase to alpine 3.8.
* **12.01.18:** - Rebase to alpine linux 3.7.
* **28.10.17:** - php7-ssh2 moved from testing to community repo.
* **25.05.17:** - Rebase to alpine linux 3.6.
* **17.05.17:** - Make default install pydio 8.
* **03.05.17:** - Use repo pinning to better solve dependencies, use repo version of php7-imagick.
* **28.02.17:** - Modify sed for data path.
* **18.02.17:** - Rebase to alpine linux 3.5.
* **05.11.16:** - Pinned at latest sourceforge download version, in lieu of a full rewrite.
* **14.10.16:** - Add version layer information.
* **10.09.16:** - Add layer badges to README.
* **08.09.15:** - Initial Release.
