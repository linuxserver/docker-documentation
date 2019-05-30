# [linuxserver/nntp2nntp](https://github.com/linuxserver/docker-nntp2nntp)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/nntp2nntp.svg)](https://microbadger.com/images/linuxserver/nntp2nntp "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/nntp2nntp.svg)](https://microbadger.com/images/linuxserver/nntp2nntp "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/nntp2nntp.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/nntp2nntp.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-nntp2nntp/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-nntp2nntp/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nntp2nntp/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nntp2nntp/latest/index.html)

[Nntp2nntp](https://github.com/linuxserver/nntp2nntp) proxy allow you to use your NNTP Account from multiple systems, each with own user name and password. It fully supports SSL and you can also limit the access to proxy with SSL certificates. nntp2nntp proxy is very simple and pretty fast.
## Warning

Whilst we know of no nntp2nntp security issues the [upstream code](https://github.com/linuxserver/nntp2nntp) for this project has received no changes since 06.08.15 and is likely abandoned permanently.  For this reason we strongly recommend you do not make this application public facing and if you must do so other layers of security and SSL should be considered an absolute bare minimum requirement.  We see this proxy being used primarily on a LAN so that all the users NNTP applications can share a common set of internal credentials allowing for central managment of the upstream account e.g change provider, server, thread limits for all applications with one global config change.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/nntp2nntp` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=nntp2nntp \
  -e PUID=1000 \
  -e PGID=1000 \
  -e PUID=<yourUID> \
  -e PGID=<yourGID> \
  -e TZ=Europe/London \
  -p 1563:1563 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/nntp2nntp
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  nntp2nntp:
    image: linuxserver/nntp2nntp
    container_name: nntp2nntp
    environment:
      - PUID=1000
      - PGID=1000
      - PUID=<yourUID>
      - PGID=<yourGID>
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
    ports:
      - 1563:1563
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `1563` | will map the container's port 1563 to port 1563 on the host |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `PUID=<yourUID>` | specify your UID |
| `PGID=<yourGID>` | specify your GID |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | this will store config on the docker host |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Edit sample config file `config/nntp2nntp.conf` with upstream provider details and rename the local users.

New user passwords can be created by running the password hash generator
```
docker exec -it nntp2nntp /usr/bin/nntp2nntp.py pass
```
entering the desired password and copying the resulting string to the relevant user line in `/config/nntp2nntp.conf`

Example with a user called `Dave` and with a password of `password`
```
Dave    = 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
```



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it nntp2nntp /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f nntp2nntp`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' nntp2nntp`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/nntp2nntp`

## Versions

* **23.04.19:** - Multiarch builds and build from Github fork.
* **15.05.18:** - Initial Release.
