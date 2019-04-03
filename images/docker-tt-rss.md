# [linuxserver/tt-rss](https://github.com/linuxserver/docker-tt-rss)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/tt-rss.svg)](https://microbadger.com/images/linuxserver/tt-rss "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/tt-rss.svg)](https://microbadger.com/images/linuxserver/tt-rss "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/tt-rss.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/tt-rss.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-tt-rss/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-tt-rss/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/tt-rss/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/tt-rss/latest/index.html)

[Tt-rss](https://tt-rss.org) is an open source web-based news feed (RSS/Atom) reader and aggregator, designed to allow you to read news from any location, while feeling as close to a real desktop application as possible.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/tt-rss` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=tt-rss \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 80:80 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/tt-rss
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  tt-rss:
    image: linuxserver/tt-rss
    container_name: tt-rss
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
    ports:
      - 80:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where tt-rss should store it's config files and data. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

You must create a user and database for tt-rss to use in a mysql/mariadb or postgresql server. A basic nginx configuration file can be found in /config/nginx/site-confs , edit the file to enable ssl (port 443 by default), set servername etc.. Self-signed keys are generated the first time you run the container and can be found in /config/keys , if needed, you can replace them with your own.

**The default username and password after initial configuration is admin/password**

## Power users
The container can configure itself using environment variables, the gaurd for this logic to run is if the variable `DB_TYPE` is set. The most common variables to set are a URL for the application and a database endpoint. IE:
* -e DB_TYPE=mysql
* -e DB_HOST=host
* -e DB_USER=user
* -e DB_NAME=name
* -e DB_PASS=password
* -e DB_PORT=3306
* -e SELF_URL_PATH=http://localhost/

Please note if you use this method you need to have an already initialized database endpoint. We do our best to ensure that anything in the config.php can be set via these environment variables. 



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it tt-rss /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f tt-rss`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' tt-rss`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/tt-rss`

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **26.02.19:** - Install app in container, add php-ldap, allow env vars to generate config, thanks Neraud and Fmstrat.
* **22.02.19:** - Rebasing to alpine 3.9.
* **28.01.19:** - Add pipeline logic and multi arch.
* **21.08.18:** - Rebase to alpine linux 3.8.
* **08.01.18:** - Rebase to alpine linux 3.7.
* **19.07.17:** - Use updated [repository](https://git.tt-rss.org/git/tt-rss) for initial install.
* **25.05.17:** - Rebase to alpine linux 3.6.
* **23.02.17:** - Rebase to alpine linux 3.5 and nginx.
* **14.10.16:** - Add version layer information.
* **10.09.16:** - Add layer badges to README.
* **31.08.15:** - Initial Release.
