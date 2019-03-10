# [linuxserver/jackett](https://github.com/linuxserver/docker-jackett)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/jackett.svg)](https://microbadger.com/images/linuxserver/jackett "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/jackett.svg)](https://microbadger.com/images/linuxserver/jackett "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/jackett.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/jackett.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-jackett/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-jackett/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/jackett/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/jackett/latest/index.html)

[Jackett](https://github.com/Jackett/Jackett) works as a proxy server: it translates queries from apps (Sonarr, SickRage, CouchPotato, Mylar, etc) into tracker-site-specific http queries, parses the html response, then sends results back to the requesting software. This allows for getting recent uploads (like RSS) and performing searches. Jackett is a single repository of maintained indexer scraping & translation logic - removing the burden from other apps.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/jackett` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=jackett \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e RUN_OPTS=<run options here> `#optional` \
  -p 9117:9117 \
  -v <path to data>:/config \
  -v <path to blackhole>:/downloads \
  --restart unless-stopped \
  linuxserver/jackett
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  jackett:
    image: linuxserver/jackett
    container_name: jackett
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - RUN_OPTS=<run options here> #optional
    volumes:
      - <path to data>:/config
      - <path to blackhole>:/downloads
    ports:
      - 9117:9117
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `9117` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `RUN_OPTS=<run options here>` | Optionally specify additional arguments to be passed. EG. `--ProxyConnection=10.0.0.100:1234`. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where Jackett should store its config file. |
| `/downloads` | Path to torrent blackhole. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

The web interface is at `<your-ip>:9117` , configure various trackers and connections to other apps there.
More info at [Jackett](https://github.com/Jackett/Jackett).

Disable autoupdates in the webui to prevent jackett crashing, the image is refreshed when new versions are released.



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it jackett /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f jackett`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' jackett`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/jackett`

## Versions

* **10.03.19:** - Switch to net-core builds of jackett, not dependant on mono and smaller images.
* **11.02.19:** - Add pipeline logic and multi arch.
* **11.06.18:** - Ensure root ownership of Jackett files.
* **13.12.17:** - Fix continuation lines.
* **17.04.17:** - Switch to using inhouse mono baseimage, ubuntu xenial based.
* **09.02.17:** - Rebase to alpine 3.5.
* **29.10.16:** - Call python2 from edge main to satisfy new mono dependency.
* **14.10.16:** - Add version layer information.
* **22.09.16:** - Remove autoupdate, tidy up Dockerfile.
* **10.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README.
* **06.08.16:** - Rebase to alpine linux for smaller image.
* **25.01.16:** - Initial Release.
