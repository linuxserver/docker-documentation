# linuxserver/heimdall

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-heimdall.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-heimdall/releases) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/heimdall.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/heimdall) [![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/heimdall.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/heimdall) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/heimdall.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/heimdall) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/heimdall.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/heimdall) [![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-heimdall/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-heimdall/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/heimdall/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/heimdall/latest/index.html)

[Heimdall](https://heimdall.site) is a way to organise all those links to your most used web sites and web applications in a simple way. Simplicity is the key to Heimdall. Why not use it as your browser start page? It even has the ability to include a search bar using either Google, Bing or DuckDuckGo.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/heimdall` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :---: | :--- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :---: | :--- |
| latest | Stable Heimdall releases. |
| development | Latest commit from the github master branch. |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=heimdall \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 80:80 \
  -p 443:443 \
  -v </path/to/appdata/config>:/config \
  --restart unless-stopped \
  linuxserver/heimdall
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  heimdall:
    image: linuxserver/heimdall
    container_name: heimdall
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/appdata/config>:/config
    ports:
      - 80:80
      - 443:443
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `80` | http gui |
| `443` | https gui |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Contains all relevant configuration files. |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the web gui at [http://SERVERIP:PORT](http://SERVERIP:PORT)

### Adding password protection

This image now supports password protection through htpasswd. Run the following command on your host to generate the htpasswd file `docker exec -it heimdall htpasswd -c /config/nginx/.htpasswd <username>`. Replace  with a username of your choice and you will be asked to enter a password. New installs will automatically pick it up and implement password protected access. Existing users updating their image can delete their site config at `/config/nginx/site-confs/default` and restart the container after updating the image. A new site config with htpasswd support will be created in its place.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it heimdall /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f heimdall`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' heimdall`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/heimdall`

## Versions

* **16.07.19:** - Save laravel.log to /config/log/heimdall.
* **28.06.19:** - Rebasing to alpine 3.10.
* **01.04.19:** - Fix permission detect logic.
* **26.03.19:** - Install Heimdall during container start to prevent delayed start due to overlayfs bug with recursive chown.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **15.03.19:** - Clarify docker image tags in readme.
* **22.02.19:** - Rebasing to alpine 3.9.
* **16.01.18:** - Generate random app key in .env for new installs.
* **20.11.18:** - Upgrade baseimage packages during build.
* **04.11.18:** - Add php7-zip.
* **31.10.18:** - Add queue service.
* **17.10.18:** - Symlink avatars folder.
* **16.10.18:** - Updated fastcgi\_params for user login support.
* **07.10.18:** - Symlink `.env` rather than copy. It now resides under `/config/www`
* **30.09.18:** - Multi-arch image. Move `.env` to `/config`.
* **05.09.18:** - Rebase to alpine linux 3.8.
* **06.03.18:** - Use password protection if htpasswd is set. Existing users can delete their default site config at /config/nginx/site-confs/default and restart the container, a new default site config with htpasswd support will be created in its place
* **12.02.18:** - Initial Release.

