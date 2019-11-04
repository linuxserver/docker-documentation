# [linuxserver/calibre-web](https://github.com/linuxserver/docker-calibre-web)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-calibre-web.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-calibre-web)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-calibre-web.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-calibre-web/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-calibre-web/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-calibre-web/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/calibre-web)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/calibre-web.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/calibre-web "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/calibre-web.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/calibre-web)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/calibre-web.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/calibre-web)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-calibre-web/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-calibre-web/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/calibre-web/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/calibre-web/latest/index.html)

[Calibre-web](https://github.com/janeczku/calibre-web) is a web app providing a clean interface for browsing, reading and downloading eBooks using an existing Calibre database.   It is also possible to integrate google drive and edit metadata and your calibre library through the app itself.

This software is a fork of library and licensed under the GPL v3 License.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/calibre-web` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=calibre-web \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e DOCKER_MODS=linuxserver/calibre-web:calibre \
  -p 8083:8083 \
  -v <path to data>:/config \
  -v <path to calibre library>:/books \
  --restart unless-stopped \
  linuxserver/calibre-web
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  calibre-web:
    image: linuxserver/calibre-web
    container_name: calibre-web
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - DOCKER_MODS=linuxserver/calibre-web:calibre
    volumes:
      - <path to data>:/config
      - <path to calibre library>:/books
    ports:
      - 8083:8083
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8083` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `DOCKER_MODS=linuxserver/calibre-web:calibre` | #optional & **x86-64 only** Adds the ability to perform ebook conversion |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where calibre-web stores the internal database and config. |
| `/books` | Where your calibre database is locate. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Webui can be found at `http://your-ip:8083`

On the initial setup screen, enter `/books` as your calibre library location.

**Default admin login:**
*Username:* admin
*Password:* admin123

Unrar is included by default and needs to be set in the Calibre-Web admin page (Basic Configuration:External Binaries) with a path of `/usr/bin/unrar`

**x86-64 only** We have implemented the optional ability to pull in the dependencies to enable ebook conversion utilising Calibre, this means if you don't require this feature the container isn't uneccessarily bloated but should you require it, it is easily available.
This optional layer will be rebuilt automatically on our CI pipeline upon new Calibre releases so you can stay up to date.
To use this option add the optional environmental variable as detailed above to pull an addition docker layer to enable ebook conversion and then in the Calibre-Web admin page (Basic Configuration:External Binaries) set the path to converter tool to `/usr/bin/ebook-convert`  


To reverse proxy with our Letsencrypt docker container we include a preconfigured reverse proxy config, for other instances of Nginx use the following location block:
```
        location /calibre-web {
                proxy_pass              http://<your-ip>:8083;
                proxy_set_header        Host            $http_host;
                proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header        X-Scheme        $scheme;
                proxy_set_header        X-Script-Name   /calibre-web;
        }
```



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it calibre-web /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f calibre-web`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' calibre-web`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/calibre-web`

## Versions

* **10.13.19:** - Migrate to Python3.
* **01.08.19:** - Add libxcomposite1.
* **13.06.19:** - Add docker mod to enable optional ebook conversion on x86-64.  Add unrar.
* **02.06.19:** - Rebase to Ubuntu Bionic & add Gdrive support.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **23.02.19:** - Rebase to alpine 3.9, use repo version of imagemagick.
* **11.02.19:** - Add pipeline logic and multi arch.
* **03.01.19:** - Remove guest user from default app.db.
* **16.08.18:** - Rebase to alpine 3.8.
* **03.07.18:** - New build pushed, all versions below `67` have [vulnerability](https://github.com/janeczku/calibre-web/issues/534).
* **05.01.18:** - Deprecate cpu_core routine lack of scaling.
* **06.12.17:** - Rebase to alpine 3.7.
* **27.11.17:** - Use cpu core counting routine to speed up build time.
* **24.07.17:** - Curl version for imagemagick.
* **17.07.17:** - Initial release.
