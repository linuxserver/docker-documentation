# [linuxserver/ombi](https://github.com/linuxserver/docker-ombi)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/ombi.svg)](https://microbadger.com/images/linuxserver/ombi "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/ombi.svg)](https://microbadger.com/images/linuxserver/ombi "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/ombi.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/ombi.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-ombi/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-ombi/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ombi/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ombi/latest/index.html)

[Ombi](https://ombi.io) allows you to host your own Plex Request and user management system.
If you are sharing your Plex server with other users, allow them to request new content using an easy to manage interface!
Manage all your requests for Movies and TV with ease, leave notes for the user and get notification when a user requests something.
Allow your users to post issues against their requests so you know there is a problem with the audio etc.
Even automatically send them weekly newsletters of new content that has been added to your Plex server!

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/ombi` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :----: | --- |
| latest | Stable Ombi releases |
| development | Releases from the `develop` branch of Ombi |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=ombi \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 3579:3579 \
  -v </path/to/appdata/config>:/config \
  --restart unless-stopped \
  linuxserver/ombi
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  ombi:
    image: linuxserver/ombi
    container_name: ombi
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/appdata/config>:/config
    ports:
      - 3579:3579
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3579` | web gui |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains all relevant configuration files. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `<your-ip>:3579`. Follow the setup wizard on initial install.  Then configure the required services.



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it ombi /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f ombi`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ombi`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/ombi`

## Versions

* **22.02.19:** - Clarify info on tags and development builds.
* **25.01.19:** - Add info on tags and development builds.
* **09.01.19:** - Switch to multi-arch builds and add aarch64 image.
* **11.03.18:** - Add HOME env to Dockerfile.
* **05.03.18:** - Switch to Ombi v3 stable based on .net core.
* **26.01.18:** - Fix continuation lines.
* **16.04.17:** - Switch to using inhouse mono baseimage.
* **17.02.17:** - Initial Release.
