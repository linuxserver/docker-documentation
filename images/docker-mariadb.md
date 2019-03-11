# [linuxserver/mariadb](https://github.com/linuxserver/docker-mariadb)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/mariadb.svg)](https://microbadger.com/images/linuxserver/mariadb "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/mariadb.svg)](https://microbadger.com/images/linuxserver/mariadb "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/mariadb.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/mariadb.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-mariadb/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-mariadb/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/mariadb/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/mariadb/latest/index.html)

[Mariadb](https://mariadb.org/) is one of the most popular database servers. Made by the original developers of MySQL.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/mariadb` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=mariadb \
  -e PUID=1000 \
  -e PGID=1000 \
  -e MYSQL_ROOT_PASSWORD=<DATABASE PASSWORD> \
  -e TZ=Europe/London \
  -e MYSQL_DATABASE=<USER DB NAME> `#optional` \
  -e MYSQL_USER=<MYSQL USER> `#optional` \
  -e MYSQL_PASSWORD=<DATABASE PASSWORD> `#optional` \
  -p 3306:3306 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/mariadb
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  mariadb:
    image: linuxserver/mariadb
    container_name: mariadb
    environment:
      - PUID=1000
      - PGID=1000
      - MYSQL_ROOT_PASSWORD=<DATABASE PASSWORD>
      - TZ=Europe/London
      - MYSQL_DATABASE=<USER DB NAME> #optional
      - MYSQL_USER=<MYSQL USER> #optional
      - MYSQL_PASSWORD=<DATABASE PASSWORD> #optional
    volumes:
      - <path to data>:/config
    ports:
      - 3306:3306
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3306` | Mariadb listens on this port. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `MYSQL_ROOT_PASSWORD=<DATABASE PASSWORD>` | Set this to root password for installation (minimum 4 characters). |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `MYSQL_DATABASE=<USER DB NAME>` | Specify the name of a database to be created on image startup. |
| `MYSQL_USER=<MYSQL USER>` | This user will have superuser access to the database specified by MYSQL_DATABASE. |
| `MYSQL_PASSWORD=<DATABASE PASSWORD>` | Set this to the password you want to use for you MYSQL_USER (minimum 4 characters). |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains the db itself and all assorted settings. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

If you didn't set a password during installation, (see logs for warning) use
`mysqladmin -u root password <PASSWORD>`
to set one at the docker prompt...

NOTE changing the MYSQL_ROOT_PASSWORD variable after the container has set up the initial databases has no effect, use the mysqladmin tool to change your mariadb password.

NOTE if you want to use (MYSQL_DATABASE MYSQL_USER MYSQL_PASSWORD) **all three** of these variables need to be set you cannot pick and choose.

Unraid users, it is advisable to edit the template/webui after setup and remove reference to this variable.

Find custom.cnf in /config for config changes (restart container for them to take effect)
, the databases in /config/databases and the log in /config/log/myqsl



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it mariadb /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f mariadb`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' mariadb`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/mariadb`

## Versions

* **07.03.19:** - Add ability to setup a database and default user on first spinup.
* **26.01.19:** - Add pipeline logic and multi arch.
* **10.09.18:** - Rebase to ubuntu bionic and use 10.3 mariadb repository.
* **09.12.17:** - Fix continuation lines.
* **12.09.17:** - Gracefully shut down mariadb.
* **27.10.16:** - Implement linting suggestions on database init script.
* **11.10.16:** - Rebase to ubuntu xenial, add version labelling.
* **09.03.16:** - Update to mariadb 10.1. Change to use custom.cnf over my.cnf in /config. Restructured init files to change config options on startup, rather than in the dockerfile.
* **26.01.16:** - Change user of mysqld_safe script to abc, better unclean shutdown handling on restart.
* **23.12.15:** - Remove autoupdating, between some version updates the container breaks.
* **12.08.15:** - Initial Release.
