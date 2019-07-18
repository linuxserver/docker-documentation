# [linuxserver/lazylibrarian](https://github.com/linuxserver/docker-lazylibrarian)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/lazylibrarian.svg)](https://microbadger.com/images/linuxserver/lazylibrarian "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/lazylibrarian.svg)](https://microbadger.com/images/linuxserver/lazylibrarian "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/lazylibrarian.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/lazylibrarian.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-lazylibrarian/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-lazylibrarian/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/lazylibrarian/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/lazylibrarian/latest/index.html)

[Lazylibrarian](https://github.com/DobyTang/LazyLibrarian) is a program to follow authors and grab metadata for all your digital reading needs. It uses a combination of Goodreads Librarything and optionally GoogleBooks as sources for author info and book info.  This container is based on the DobyTang fork.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/lazylibrarian` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=lazylibrarian \
  -e PUID=1000 \
  -e PGID=1000 \
  -e DOCKER_MODS=linuxserver/calibre-web:calibre #*optional* & **x86-64 only** \
  -e TZ=Europe/London \
  -p 5299:5299 \
  -v <path to data>:/config \
  -v <path to downloads>:/downloads \
  -v <path to data>:/books \
  --restart unless-stopped \
  linuxserver/lazylibrarian
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  lazylibrarian:
    image: linuxserver/lazylibrarian
    container_name: lazylibrarian
    environment:
      - PUID=1000
      - PGID=1000
      - DOCKER_MODS=linuxserver/calibre-web:calibre #*optional* & **x86-64 only**
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <path to downloads>:/downloads
      - <path to data>:/books
    ports:
      - 5299:5299
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `5299` | The port for the LazyLibrarian webinterface |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `DOCKER_MODS=linuxserver/calibre-web:calibre #*optional* & **x86-64 only**` | #optional & **x86-64 only** Adds the ability to enable the Calibredb import program |
| `TZ=Europe/London` | Specify a timezone to use e.g. Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | LazyLibrarian config |
| `/downloads` | Download location |
| `/books` | Books location |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `http://<your-ip>:5299/home`, for more information check out [Lazylibrarian](https://github.com/DobyTang/LazyLibrarian).

**x86-64 only** We have implemented the optional ability to pull in the dependencies to enable the Calibredb import program:, this means if you don't require this feature the container isn't uneccessarily bloated but should you require it, it is easily available.
This optional layer will be rebuilt automatically on our CI pipeline upon new Calibre releases so you can stay up to date.
To use this option add the optional environmental variable as detailed above to pull an addition docker layer to enable ebook conversion and then in the LazyLibrarian config page (Processing:Calibredb import program:) set the path to converter tool to `/usr/bin/calibredb`



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it lazylibrarian /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f lazylibrarian`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' lazylibrarian`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/lazylibrarian`

## Versions

* **09.07.19:** - Rebase to Ubuntu Bionic, enables Calibre docker mod.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **05.03.19:** - Added apprise python package.
* **22.02.19:** - Rebasing to alpine 3.9.
* **10.12.18:** - Moved to Pipeline Building
* **16.08.18:** - Rebase to alpine 3.8
* **05.01.18:** - Deprecate cpu_core routine lack of scaling
* **12.12.17:** - Rebase to alpine 3.7
* **21.07.17:** - Internal git pull instead of at runtime
* **25.05.17:** - Rebase to alpine 3.6
* **07.02.17:** - Rebase to alpine 3.5
* **30.01.17:** - Compile libunrar.so to allow reading of .cbr format files
* **12.01.17:** - Add ghostscript package, allows magazine covers to be created etc
* **14.10.16:** - Add version layer information
* **03.10.16:** - Fix non-persistent settings and make log folder
* **28.09.16:** - Inital Release
