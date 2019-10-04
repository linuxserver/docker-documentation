# [linuxserver/calibre](https://github.com/linuxserver/docker-calibre)

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-calibre.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-calibre/releases)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/calibre.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/calibre "Get your own version badge on microbadger.com")
[![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/calibre.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/calibre "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/calibre.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/calibre)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/calibre.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/calibre)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-calibre/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-calibre/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/calibre/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/calibre/latest/index.html)

[Calibre](https://calibre-ebook.com/) is a powerful and easy to use e-book manager. Users say it’s outstanding and a must-have. It’ll allow you to do nearly everything and it takes things a step beyond normal e-book software. It’s also completely free and open source and great for both casual users and computer experts.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/calibre` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=calibre \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e GUAC_USER=abc `#optional` \
  -e GUAC_PASS=900150983cd24fb0d6963f7d28e17f72 `#optional` \
  -p 8080:8080 \
  -p 8081:8081 \
  -v /path/to/data:/config \
  --restart unless-stopped \
  linuxserver/calibre
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  calibre:
    image: linuxserver/calibre
    container_name: calibre
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - GUAC_USER=abc #optional
      - GUAC_PASS=900150983cd24fb0d6963f7d28e17f72 #optional
    volumes:
      - /path/to/data:/config
    ports:
      - 8080:8080
      - 8081:8081
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8080` | Calibre desktop gui. |
| `8081` | Calibre webserver gui. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `GUAC_USER=abc` | Username for the calibre desktop gui. |
| `GUAC_PASS=900150983cd24fb0d6963f7d28e17f72` | Password's md5 hash for the calibre desktop gui. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where calibre should store its database and library. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

This image sets up the calibre desktop app and makes its interface available via Guacamole server in the browser. The interface is available at `http://your-ip:8080`.

By default, there is no username or password set. Custom usernames and passwords can be set via optional docker environment variables. Keep in mind that the `GUACPASS` variable accepts the `md5 hash` of the desired password (the sample above is the hash for `abc`). The md5 hash can be generated by either of the following commands:

```
echo -n password | openssl md5
```

```
printf '%s' password | md5sum
```

Port 8081 is reserved for Calibre's built-in webserver, which can be enabled within the desktop app settings, and the internal port must be set to `8081` although it will then be available at the host mapped port for external access.

You can access advanced features of the Guacamole remote desktop using `ctrl`+`alt`+`shift` enabling you to use remote copy/paste and different languages.



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it calibre /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f calibre`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' calibre`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/calibre`

## Versions

* **04.10.19:** - Add libxkbcommon-x11-0 dependency to resolve issue with Calibre 4.
* **08.08.19:** - Add zenity for international character support in dialog boxes.
* **12.07.19:** - Download binary from calibre website instead of github.
* **29.04.19:** - Initial release.
