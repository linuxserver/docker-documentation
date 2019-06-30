# [linuxserver/duckdns](https://github.com/linuxserver/docker-duckdns)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/duckdns.svg)](https://microbadger.com/images/linuxserver/duckdns "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/duckdns.svg)](https://microbadger.com/images/linuxserver/duckdns "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/duckdns.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/duckdns.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-duckdns/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-duckdns/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/duckdns/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/duckdns/latest/index.html)

[Duckdns](https://duckdns.org/) is a free service which will point a DNS (sub domains of duckdns.org) to an IP of your choice. The service is completely free, and doesn't require reactivation or forum posts to maintain its existence.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/duckdns` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=duckdns \
  -e PUID=1000 `#optional` \
  -e PGID=1000 `#optional` \
  -e TZ=Europe/London \
  -e SUBDOMAINS=subdomain1,subdomain2 \
  -e TOKEN=token \
  -e LOG_FILE=false `#optional` \
  -v </path/to/appdata/config>:/config `#optional` \
  --restart unless-stopped \
  linuxserver/duckdns
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  duckdns:
    image: linuxserver/duckdns
    container_name: duckdns
    environment:
      - PUID=1000 #optional
      - PGID=1000 #optional
      - TZ=Europe/London
      - SUBDOMAINS=subdomain1,subdomain2
      - TOKEN=token
      - LOG_FILE=false #optional
    volumes:
    volumes:
      - </path/to/appdata/config>:/config #optional
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `SUBDOMAINS=subdomain1,subdomain2` | multiple subdomains allowed, comma separated, no spaces |
| `TOKEN=token` | DuckDNS token |
| `LOG_FILE=false` | Set to `true` to log to file (also need to map /config). |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Used in conjunction with logging to file. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

- Go to the [duckdns website](https://duckdns.org/), register your subdomain(s) and retrieve your token
- Create a container with your subdomain(s) and token
- It will update your IP with the DuckDNS service every 5 minutes



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it duckdns /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f duckdns`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' duckdns`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/duckdns`

## Versions

* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **08.02.19:** - Update readme with optional parameters.
* **10.12.18:** - Fix docker compose example.
* **15.10.18:** - Multi-arch image.
* **22.08.18:** - Rebase to alpine 3.8.
* **08.12.17:** - Rebase to alpine 3.7.
* **28.05.17:** - Rebase to alpine 3.6.
* **09.02.17:** - Rebase to alpine 3.5.
* **17.11.16:** - Initial release.
