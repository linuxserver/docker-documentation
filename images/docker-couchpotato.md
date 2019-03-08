# [linuxserver/couchpotato](https://github.com/linuxserver/docker-couchpotato)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/couchpotato.svg)](https://microbadger.com/images/linuxserver/couchpotato "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/couchpotato.svg)](https://microbadger.com/images/linuxserver/couchpotato "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/couchpotato.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/couchpotato.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-couchpotato/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-couchpotato/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/couchpotato/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/couchpotato/latest/index.html)

[Couchpotato](https://couchpota.to/) is an automatic NZB and torrent downloader. You can keep a `movies I want` list and it will search for NZBs/torrents of these movies every X hours. Once a movie is found, it will send it to SABnzbd or download the torrent to a specified directory.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/couchpotato` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=couchpotato \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e UMASK_SET=022 \
  -p 5050:5050 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/downloads>:/downloads \
  -v </path/to/movies>:/movies \
  --restart unless-stopped \
  linuxserver/couchpotato
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  couchpotato:
    image: linuxserver/couchpotato
    container_name: couchpotato
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - UMASK_SET=022
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/downloads>:/downloads
      - </path/to/movies>:/movies
    ports:
      - 5050:5050
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `5050` | http gui |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `UMASK_SET=022` | for umask setting of couchpotato, optional , default if left unset is 022 |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Couchpotato Application Data. |
| `/downloads` | Downloads Folder. |
| `/movies` | Movie Share. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `<your-ip>:5050`, for more information check out [CouchPotato](https://couchpota.to).



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it couchpotato /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f couchpotato`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' couchpotato`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/couchpotato`

## Versions

* **22.02.19:** - Rebasing to alpine 3.9.
* **14.01.19:** - Multi-arch builds.
* **16.08.18:** - Rebase to alpine 3.8.
* **06.11.17:** - Rebase to alpine 3.7.
* **20.07.17:** - Internal git pull instead of at runtime, add UMASK_SET variable.
* **12.07.17:** - Add inspect commands to README, move to jenkins build and push
* **25.05.17:** - Rebase to alpine 3.6
* **07.02.17:** - Rebase to alpine 3.5.
* **11.11.16:** - Stop cp logging to docker log (they are accessible in the webui and the config folder).
* **30.09.16:** - Fix umask.
* **09.09.16:** - Add layer badges to README.
* **27.08.16:** - Add badges to README.
* **08.08.16:** - Rebase to alpine linux.
* **12.11.15:** - Misc Code Cleanup.
* **02.10.15:** - Change to python baseimage.
* **28.07.15:** - Updated to latest baseimage (for testing), and a fix to autoupdate.
