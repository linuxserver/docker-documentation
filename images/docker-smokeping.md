# [linuxserver/smokeping](https://github.com/linuxserver/docker-smokeping)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-smokeping.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-smokeping)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-smokeping.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-smokeping/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-smokeping/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-smokeping/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/smokeping)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/smokeping.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/smokeping "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/smokeping.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/smokeping)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/smokeping.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/smokeping)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-smokeping/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-smokeping/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/smokeping/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/smokeping/latest/index.html)

[Smokeping](https://oss.oetiker.ch/smokeping/) keeps track of your network latency. For a full example of what this application is capable of visit [UCDavis](http://smokeping.ucdavis.edu/cgi-bin/smokeping.fcgi).

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/smokeping` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=smokeping \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 80:80 \
  -v </path/to/smokeping/config>:/config \
  -v </path/to/smokeping/data>:/data \
  --restart unless-stopped \
  linuxserver/smokeping
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  smokeping:
    image: linuxserver/smokeping
    container_name: smokeping
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/smokeping/config>:/config
      - </path/to/smokeping/data>:/data
    ports:
      - 80:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | Allows HTTP access to the internal webserver. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Configure the `Targets` file here |
| `/data` | Storage location for db and application data (graphs etc) |




## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

- Once running the URL will be `http://<host-ip>/`.
- Basics are, edit the `Targets` file to ping the hosts you're interested in to match the format found there.
- Wait 10 minutes.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27smokeping%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=smokeping "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it smokeping /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f smokeping`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' smokeping`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/smokeping`

## Versions

* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **14.11.18:** - Allow access without /smokeping in URL.
* **28.04.18:** - Rebase to alpine 3.8.
* **09.04.18:** - Add bc package.
* **08.04.18:** - Add tccping script and tcptraceroute package (thanks rcarmo).
* **13.12.17:** - Expose httpd_conf to /config.
* **13.12.17:** - Rebase to alpine 3.7.
* **24.07.17:** - Add :unraid tag for hosts without ipv6.
* **12.07.17:** - Add inspect commands to README, move to jenkins build and push.
* **28.05.17:** - Rebase to alpine 3.6.
* **07.05.17:** - Expose smokeping.conf in /config/site-confs to allow user customisations
* **12.04.17:** - Fix cropper.js path, thanks nibbledeez.
* **09.02.17:** - Rebase to alpine 3.5.
* **17.10.16:** - Add ttf-dejavu package as per [LT forum](http://lime-technology.com/forum/index.php?topic=43602.msg507875#msg507875).
* **10.09.16:** - Add layer badges to README.
* **05.09.16:** - Add curl package.
* **28.08.16:** - Add badges to README.
* **25.07.16:** - Rebase to alpine linux.
* **23.07.16:** - Fix apt script confusion.
* **29.06.15:** - This is the first release, it is mostly stable, but may contain minor defects. (thus a beta tag)
