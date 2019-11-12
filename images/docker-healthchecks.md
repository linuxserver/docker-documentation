# [linuxserver/healthchecks](https://github.com/linuxserver/docker-healthchecks)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-healthchecks.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-healthchecks)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-healthchecks.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-healthchecks/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-healthchecks/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-healthchecks/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/healthchecks)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/healthchecks.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/healthchecks "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/healthchecks.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/healthchecks)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/healthchecks.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/healthchecks)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-healthchecks/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-healthchecks/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/healthchecks/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/healthchecks/latest/index.html)

[Healthchecks](https://github.com/healthchecks/healthchecks) is a watchdog for your cron jobs. It's a web server that listens for pings from your cron jobs, plus a web interface.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/healthchecks` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=healthchecks \
  -e PUID=1000 \
  -e PGID=1000 \
  -e SITE_ROOT=<SITE_ROOT> \
  -e SITE_NAME=<SITE_NAME> \
  -e DEFAULT_FROM_EMAIL=<DEFAULT_FROM_EMAIL> \
  -e EMAIL_HOST=<EMAIL_HOST> \
  -e EMAIL_PORT=<EMAIL_PORT> \
  -e EMAIL_HOST_USER=<EMAIL_HOST_USER> \
  -e EMAIL_HOST_PASSWORD=<EMAIL_HOST_PASSWORD> \
  -e EMAIL_USE_TLS=<EMAIL_USE_TLS> \
  -e ALLOWED_HOSTS=<ALLOWED_HOSTS> \
  -e SUPERUSER_EMAIL=<SUPERUSER_EMAIL> \
  -e SUPERUSER_PASSWORD=<SUPERUSER_PASSWORD> \
  -p 8000:8000 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/healthchecks
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  healthchecks:
    image: linuxserver/healthchecks
    container_name: healthchecks
    environment:
      - PUID=1000
      - PGID=1000
      - SITE_ROOT=<SITE_ROOT>
      - SITE_NAME=<SITE_NAME>
      - DEFAULT_FROM_EMAIL=<DEFAULT_FROM_EMAIL>
      - EMAIL_HOST=<EMAIL_HOST>
      - EMAIL_PORT=<EMAIL_PORT>
      - EMAIL_HOST_USER=<EMAIL_HOST_USER>
      - EMAIL_HOST_PASSWORD=<EMAIL_HOST_PASSWORD>
      - EMAIL_USE_TLS=<EMAIL_USE_TLS>
      - ALLOWED_HOSTS=<ALLOWED_HOSTS>
      - SUPERUSER_EMAIL=<SUPERUSER_EMAIL>
      - SUPERUSER_PASSWORD=<SUPERUSER_PASSWORD>
    volumes:
      - <path to data>:/config
    ports:
      - 8000:8000
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8000` | will map the container's port 8000 to port 8000 on the host |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `SITE_ROOT=<SITE_ROOT>` | The site's domain (i.e., example.com) |
| `SITE_NAME=<SITE_NAME>` | The site's name |
| `DEFAULT_FROM_EMAIL=<DEFAULT_FROM_EMAIL>` | From email for alerts |
| `EMAIL_HOST=<EMAIL_HOST>` | SMTP host |
| `EMAIL_PORT=<EMAIL_PORT>` | SMTP port |
| `EMAIL_HOST_USER=<EMAIL_HOST_USER>` | SMTP user |
| `EMAIL_HOST_PASSWORD=<EMAIL_HOST_PASSWORD>` | SMTP password |
| `EMAIL_USE_TLS=<EMAIL_USE_TLS>` | Use TLS for SMTP |
| `ALLOWED_HOSTS=<ALLOWED_HOSTS>` | array of valid hostnames for the server ["test.com","test2.com"] |
| `SUPERUSER_EMAIL=<SUPERUSER_EMAIL>` | Superuser emai |
| `SUPERUSER_PASSWORD=<SUPERUSER_PASSWORD>` | Superuser password |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | database and healthchecks config |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the WebUI at <your-ip>:8000. For more information, check out [Healthchecks](https://github.com/healthchecks/healthchecks).



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it healthchecks /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f healthchecks`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' healthchecks`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/healthchecks`

## Versions

* **31.10.19:** - Add postgres client and fix config for CSRF.
* **23.10.19:** - Allow to create superuser
* **28.06.19:** - Rebasing to alpine 3.10.
* **12.04.19:** - Rebase to Alpine 3.9.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **14.02.19:** - Adding mysql libs needed for using a database.
* **11.10.18:** - adding pipeline logic and multi arching release
* **15.11.17:** - `git pull` is now in Dockerfile so each tagged container contains the same code version
* **17.10.17:** - Fixed `local_settings.py` output
* **27.09.17:** - Initial Release.
