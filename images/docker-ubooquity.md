# [linuxserver/ubooquity](https://github.com/linuxserver/docker-ubooquity)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-ubooquity.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-ubooquity)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-ubooquity.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-ubooquity/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-ubooquity/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-ubooquity/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/ubooquity)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/ubooquity.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/ubooquity "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/ubooquity.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/ubooquity)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/ubooquity.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/ubooquity)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-ubooquity/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-ubooquity/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ubooquity/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ubooquity/latest/index.html)

[Ubooquity](https://vaemendis.net/ubooquity/) is a free, lightweight and easy-to-use home server for your comics and ebooks. Use it to access your files from anywhere, with a tablet, an e-reader, a phone or a computer.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/ubooquity` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=ubooquity \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e MAXMEM=<maxmem> \
  -p 2202:2202 \
  -p 2203:2203 \
  -v <path to data>:/config \
  -v <path to books>:/books \
  -v <path to comics>:/comics \
  -v <path to raw files>:/files \
  --restart unless-stopped \
  linuxserver/ubooquity
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  ubooquity:
    image: linuxserver/ubooquity
    container_name: ubooquity
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - MAXMEM=<maxmem>
    volumes:
      - <path to data>:/config
      - <path to books>:/books
      - <path to comics>:/comics
      - <path to raw files>:/files
    ports:
      - 2202:2202
      - 2203:2203
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `2202` | The library port. |
| `2203` | The admin port. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `MAXMEM=<maxmem>` | To set the maximum memory. ( ex: set '1024' for 1GB ) |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Config files and database for ubooquity. |
| `/books` | Location of books. |
| `/comics` | Location of comics. |
| `/files` | Location of raw files. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

**IMPORTANT**
Ubooquity has now been upgraded to [version 2](http://vaemendis.net/ubooquity/article19/ubooquity-2-1-0) and for existing v1.x users we recommend cleaning your appdata and reinstalling, due to changes in the application itself making the two versions essentially incompatible with each other. Also the admin page and library pages are now on separate ports as detailed below.

Access the admin page at `http://<your-ip>:2203/ubooquity/admin` and set a password.

Then you can access the webui at `http://<your-ip>:2202/ubooquity/`

This container will automatically scan your files at startup.

### MAXMEM

The quantity of memory allocated to Ubooquity depends on the hardware your are running it on. If this quantity is too small, you might sometime saturate it with when performing memory intensive operations. That’s when you get `java.lang.OutOfMemoryError:` Java heap space errors.

You can explicitly set the amount of memory Ubooquity is allowed to use (be careful to set a value lower than the actual physical memory of your hardware). Value is a number of megabytes ( put just a number, without MB )

If no value is set it will default to 512MB.



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it ubooquity /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f ubooquity`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ubooquity`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/ubooquity`

## Versions

* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **28.01.19:** - Add pipeline logic and multi arch.
* **15.10.18:** - Upgrade to Ubooquity 2.1.2.
* **23.08.18:** - Rebase to alpine 3.8.
* **09.12.17:** - Rebase to alpine 3.7.
* **07.10.17:** - Upgrade to Ubooquity 2.1.1.
* **16.07.17:** - Upgrade to Ubooquity 2.1.0, see setting up application section for important info for existing v1.x users.
* **26.05.17:** - Rebase to alpine 3.6.
* **08.04.17:** - Switch to java from 3.5 repo, fixes login crashes.
* **06.02.17:** - Rebase to alpine 3.5.
* **06.12.16:** - Initial Release.
