# [linuxserver/musicbrainz](https://github.com/linuxserver/docker-musicbrainz)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/musicbrainz.svg)](https://microbadger.com/images/linuxserver/musicbrainz "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/musicbrainz.svg)](https://microbadger.com/images/linuxserver/musicbrainz "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/musicbrainz.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/musicbrainz.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-musicbrainz/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-musicbrainz/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/musicbrainz/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/musicbrainz/latest/index.html)

[Musicbrainz](https://musicbrainz.org/) is an open music encyclopedia that collects music metadata and makes it available to the public.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/musicbrainz` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=musicbrainz \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=Europe/London \
  -e BRAINZCODE=<code from musicbrainz> \
  -e WEBADDRESS=<ip of host> \
  -e NPROC=<parameter> `#optional` \
  -p 5000:5000 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/appdata/config>:/data \
  --restart unless-stopped \
  linuxserver/musicbrainz
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  musicbrainz:
    image: linuxserver/musicbrainz
    container_name: musicbrainz
    environment:
      - PUID=1001
      - PGID=1001
      - TZ=Europe/London
      - BRAINZCODE=<code from musicbrainz>
      - WEBADDRESS=<ip of host>
      - NPROC=<parameter> #optional
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/appdata/config>:/data
    ports:
      - 5000:5000
    mem_limit: 4096m
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `5000` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1001` | for UserID - see below for explanation |
| `PGID=1001` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `BRAINZCODE=<code from musicbrainz>` | To enter musicbrainz code. see Setting up the application |
| `WEBADDRESS=<ip of host>` | To set ip for host to allow css to render properly, DO NOT ENTER PORT NUMBER. |
| `NPROC=<parameter>` | To set number of proceses, defaults to 5 if unset. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Config files for musicbrainz. |
| `/data` | Data files for musicbrainz. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1001` and `PGID=1001`, to find yours use `id user` as below:

```
  $ id username
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Application Setup

+ For schema 24 updates you should pull the latest image, clear all files and folders in /config and /data and reinitiate the database import by (re)starting the docker.

+ **If you did not set WEBADDRESS env variable, then AFTER iniatilisation is complete you will need to edit the line `sub WEB_SERVER { "localhost:5000" }` in file /config/DBDefs.pm changing localhost to the ip of your host, this is to allow css to display properly**

* You must register here to recieve a musicbrainz code to allow you to recieve database updates, it is free. [Get Code here](https://metabrainz.org/supporters/account-type).
* The initial import and setup of the database can take quite a long time, dependant on your download speed etc, be patient and don't restart the container before it's complete.
* It appears there are issues with unraid and using /mnt/user/cache/appdata instead of /mnt/cache/appdata, use /mnt/cache/appdata.



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it musicbrainz /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f musicbrainz`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' musicbrainz`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/musicbrainz`

## Versions

* **19.02.19:** - Multi Arch and add pipeline logic, rebase to Alpine 3.9
* **22.08.18:** - Bump server version 2018-08-14.
* **30.06.18:** - Bump server version 2018-06-30.
* **01.06.18:** - Bump server version 2018-05-30 , simplify sed and use yarn instead of npm.
* **14.05.18:** - Bump server version 2018-05-09.
* **26.04.18:** - Bump server version 2018-04-23.
* **09.02.18:** - Bump server version 2018-02-09.
* **24.01.18:** - Bump server version 2018-01-24.
* **10.01.18:** - Bump server version 2018-01-10.
* **31.11.17:** - Bump server version 2017-12-21.
* **30.11.17:** - Add NPROC variable  to allow number of processes to be set.
* **30.11.17:** - Fix linting recommendations.
* **30.11.17:** - Remove socket on startup if exists (thanks wtf911) [re](https://tickets.metabrainz.org/browse/MBS-9370).
* **24.11.17:** - Remove catalyst side bar on new installs.
* **31.10.17:** - Bump server version 2017-10-31.
* **20.09.17:** - Bump server version 2017-09-18.
* **06.09.17:** - Bump server version 2017-09-04.
* **19.07.17:** - Bump server version 2017-07-17.
* **21.06.17:** - Bump server version 2017-06-19.
* **26.05.17:** - Fix later build of postgres using /run instead of /var/run.
* **26.05.17:** - Rebase to alpine 3.6.
* **15.05.17:** - Schema 24 update, recommend full rebuild with new config.
* **15.04.17:** - Bump server version 2017-04-10.
* **04.04.17:** - Bump server version 2017-03-27.
* **15.03.17:** - Bump server version 2017-03-13.
* **04.03.17:** - Bump server version and use nginx to serve web pages.
* **06.02.17:** - Rebase to alpine 3.5.
* **16.12.16:** - Rebase to alpine linux, entailing almost complete rewrite.
* **14.10.16:** - Add version layer information.
* **30.09.16:** - Fix umask.
* **10.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README, move to main repository.
* **20.07.16:** - Restructure of docker file for clarity, add maxworkers variable in conjunction with starlet, for parallel requests in multi-core setups, thanks to user baoshan.
* **03.06.16:** - Complete rewrite due to schema change. Rebased back to 14.04 direct Using S6 overaly.
* **21.03.16:** - Bump to latest server release.
* **16.03.16:** - Bump to latest server release.
* **26.02.16:** - Bump to latest server release.
* **08.02.16:** - Switch to PPA version for redis.
* **03.01.16:** - Remove d/l of sitemaps file, missing from last 2 db dumps, move fetch of db/dump higher up initialise routine to allow easier resume of broken downloads.
* **15.12.15:** - Per latest musicbrainz blog, switched to production branch,latest stable code is now production branch in place of master.
* **10.12.15:** - Initial release date.
