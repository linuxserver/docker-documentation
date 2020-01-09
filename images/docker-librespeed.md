# [linuxserver/librespeed](https://github.com/linuxserver/docker-librespeed)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-librespeed.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-librespeed)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-librespeed.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-librespeed/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-librespeed/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-librespeed/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/librespeed)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/librespeed.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/librespeed "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/librespeed.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/librespeed)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/librespeed.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/librespeed)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-librespeed/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-librespeed/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/librespeed/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/librespeed/latest/index.html)

[Librespeed](https://github.com/librespeed/speedtest) is a very lightweight Speedtest implemented in Javascript, using XMLHttpRequest and Web Workers.
No Flash, No Java, No Websocket, No Bullshit.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/librespeed` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=librespeed \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e PASSWORD=PASSWORD \
  -e DB_TYPE=sqlite `#optional` \
  -e DB_NAME=DB_NAME `#optional` \
  -e DB_HOSTNAME=DB_HOSTNAME `#optional` \
  -e DB_USERNAME=DB_USERNAME `#optional` \
  -e DB_PASSWORD=DB_PASSWORD `#optional` \
  -p 80:80 \
  -v /path/to/appdata/config:/config \
  --restart unless-stopped \
  linuxserver/librespeed
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  librespeed:
    image: linuxserver/librespeed
    container_name: librespeed
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - PASSWORD=PASSWORD
      - DB_TYPE=sqlite #optional
      - DB_NAME=DB_NAME #optional
      - DB_HOSTNAME=DB_HOSTNAME #optional
      - DB_USERNAME=DB_USERNAME #optional
      - DB_PASSWORD=DB_PASSWORD #optional
    volumes:
      - /path/to/appdata/config:/config
    ports:
      - 80:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | web gui |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `PASSWORD=PASSWORD` | Set the password for the results database. |
| `DB_TYPE=sqlite` | Defaults to `sqlite`, can also be set to `mysql` or `postgresql`. |
| `DB_NAME=DB_NAME` | Database name. Required for mysql and pgsql. |
| `DB_HOSTNAME=DB_HOSTNAME` | Database address. Required for mysql and pgsql. |
| `DB_USERNAME=DB_USERNAME` | Database username. Required for mysql and pgsql. |
| `DB_PASSWORD=DB_PASSWORD` | Database password. Required for mysql and pgsql. |

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

Access the speedtest webui at `http://SERVERIP`. The results database can be accessed at `http://SERVERIP/results/stats.php` with the password set.  
The default template used is based on `example-singleServer-full.html`. However, all templates are provided for reference at `/config/www/`. Feel free to customize `/config/www/index.html` as you like. Delete the file and restart to go back to the image default.  

You can optionally place customized `speedtest.js` and `speedtest_worker.js` files under `/config/www` and they will supersede the defaults after a container start. Keep in mind that once you do so, they will no longer be updated. You can delete them and recreate the container to go back to the image defaults.  

If you are setting up a mysql or postgresql database, you first need to import the tables into your database as described at the following link  
https://github.com/librespeed/speedtest/blob/master/doc.md#creating-the-database



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it librespeed /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f librespeed`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' librespeed`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/librespeed`

## Versions

* **09.01.20:** - Initial Release.
