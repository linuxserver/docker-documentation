# [linuxserver/nextcloud](https://github.com/linuxserver/docker-nextcloud)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/nextcloud.svg)](https://microbadger.com/images/linuxserver/nextcloud "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/nextcloud.svg)](https://microbadger.com/images/linuxserver/nextcloud "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/nextcloud.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/nextcloud.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-nextcloud/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-nextcloud/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nextcloud/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nextcloud/latest/index.html)

[Nextcloud](https://nextcloud.com/) gives you access to all your files wherever you are.

Where are your photos and documents? With Nextcloud you pick a server of your choice, at home, in a data center or at a provider. And that is where your files will be. Nextcloud runs on that server, protecting your data and giving you access from your desktop or mobile devices. Through Nextcloud you also access, sync and share your existing data on that FTP drive at the office, a Dropbox or a NAS you have at home.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/nextcloud` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=nextcloud \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 443:443 \
  -v </path/to/appdata>:/config \
  -v <path/to/data>:/data \
  --restart unless-stopped \
  linuxserver/nextcloud
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  nextcloud:
    image: linuxserver/nextcloud
    container_name: nextcloud
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/appdata>:/config
      - <path/to/data>:/data
    ports:
      - 443:443
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `443` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Nextcloud configs. |
| `/data` | Your personal data. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `<your-ip>:443`, for more information check out [Nextcloud](https://nextcloud.com/).

If you are updating our container along with the in app updater and you are not customizing our default nginx configuration you will need to remove the file:
```
/config/nginx/site-confs/default
```
Then restart the container to replace it with the latest one. 



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it nextcloud /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f nextcloud`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' nextcloud`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/nextcloud`

## Versions

* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **27.02.19:** - Updating base nginx config to sync up with v15 requirements.
* **22.02.19:** - Rebasing to alpine 3.9.
* **28.01.19:** - Add pipeline logic and multi arch.
* **25.01.19:** - Add php7-phar for occ upgrades.
* **05.09.18:** - Rebase to alpine 3.8.
* **11.06.18:** - Use latest rather than specific version for initial install.
* **26.04.18:** - Bump default install to 13.0.1.
* **06.02.18:** - Bump default install to 13.0.0.
* **26.01.18:** - Rebase to alpine 3.7, bump default install to 12.0.5.
* **12.12.17:** - Bump default install to 12.0.4, fix continuation lines.
* **15.10.17:** - Sed php.ini for opcache requirements in newer nextcloud versions.
* **20.09.17:** - Bump default install to 12.0.3.
* **19.08.17:** - Bump default install to 12.0.2.
* **25.05.17:** - Rebase to alpine 3.6.
* **22.05.17:** - Update to nextcloud 12.0, adding required dependecies and note about commenting out SAMEORIGIN; line.
* **03.05.17:** - Use community repo of memcache.
* **07.03.17:** - Release into main repository and upgrade to php7 and Alpine 3.5.
