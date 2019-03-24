# [linuxserver/lychee](https://github.com/linuxserver/docker-lychee)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/lychee.svg)](https://microbadger.com/images/linuxserver/lychee "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/lychee.svg)](https://microbadger.com/images/linuxserver/lychee "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/lychee.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/lychee.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-lychee/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-lychee/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/lychee/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/lychee/latest/index.html)

[Lychee](https://lychee.electerious.com/) is a free photo-management tool, which runs on your server or web-space. Installing is a matter of seconds. Upload, manage and share photos like from a native application. Lychee comes with everything you need and all your photos are stored securely.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/lychee` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=lychee \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 80:80 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/pictures>:/pictures \
  --restart unless-stopped \
  linuxserver/lychee
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  lychee:
    image: linuxserver/lychee
    container_name: lychee
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/pictures>:/pictures
    ports:
      - 80:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | http gui |


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
| `/pictures` | Where lychee will store uploaded data. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Set up mysql/mariadb and account via the webui, accessible at http://SERVERIP:PORT  
You can change the php upload limits by editing the file `/config/lychee/user.ini` and restarting the container.  
More info at [lychee](https://lychee.electerious.com/).  



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it lychee /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f lychee`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' lychee`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/lychee`

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **21.02.19:** - Add info on changing php upload limits to readme.
* **21.01.18:** - Added ffmpeg for video thumbnail creation, switched to installing zip release instead of source tarball, created small thumbnails folder, switched to dynamic readme.
* **14.01.19:** - Adding pipeline logic and multi arch..
* **04.09.18:** - Rebase to alpine 3.8, switch to LycheeOrg repository.
* **08.01.18:** - Rebase to alpine 3.7.
* **25.05.17:** - Rebase to alpine 3.6.
* **03.05.17:** - Use repo pinning to better solve dependencies, use repo version of php7-imagick.
* **12.02.17:** - Initial Release.
