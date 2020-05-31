# [linuxserver/dokuwiki](https://github.com/linuxserver/docker-dokuwiki)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-dokuwiki.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-dokuwiki)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-dokuwiki.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-dokuwiki/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-dokuwiki/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-dokuwiki/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/dokuwiki.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/dokuwiki "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/dokuwiki.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/dokuwiki)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/dokuwiki.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/dokuwiki)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-dokuwiki%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-dokuwiki/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flspipepr%2Fdokuwiki%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/dokuwiki/latest/index.html)

[Dokuwiki](https://www.dokuwiki.org/dokuwiki/) is a simple to use and highly versatile Open Source wiki software that doesn't require a database. It is loved by users for its clean and readable syntax. The ease of maintenance, backup and integration makes it an administrator's favorite. Built in access controls and authentication connectors make DokuWiki especially useful in the enterprise context and the large number of plugins contributed by its vibrant community allow for a broad range of use cases beyond a traditional wiki.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/dokuwiki` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=dokuwiki \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e APP_URL=/dokuwiki `#optional` \
  -p 80:80 \
  -p 443:443 `#optional` \
  -v </path/to/appdata/config>:/config \
  --restart unless-stopped \
  linuxserver/dokuwiki
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  dokuwiki:
    image: linuxserver/dokuwiki
    container_name: dokuwiki
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - APP_URL=/dokuwiki #optional
    volumes:
      - </path/to/appdata/config>:/config
    ports:
      - 80:80
    ports:
      - 443:443 #optional
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | Application HTTP Port |
| `443` | #optional Application HTTPS Port |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `APP_URL=/dokuwiki` | Specify an APP_URL to append to your root location, helpful for subfolder reverse proxy setups.  Does not take effect until after first restart following setup. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Configuration files. |



## Environment variables from files (Docker secrets)

You can set any environment variable from a file by using a special prepend `FILE__`.

As an example:

```
-e FILE__PASSWORD=/run/secrets/mysecretpassword
```

Will set the environment variable `PASSWORD` based on the contents of the `/run/secrets/mysecretpassword` file.

## Umask for running applications

For all of our images we provide the ability to override the default umask settings for services started within the containers using the optional `-e UMASK=022` setting.
Keep in mind umask is not chmod it subtracts from permissions based on it's value it does not add. Please read up [here](https://en.wikipedia.org/wiki/Umask) before asking for support.


## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Upon first install go to `http://$IP:$PORT/install.php` once you have completed the setup, restart the container, login as admin and set "Use nice URLs" in the `admin/Configuration Settings` panel to `.htaccess` and tick `Use slash as namespace separator in URLs` to enable [nice URLs](https://www.dokuwiki.org/rewrite) you will find the webui at `http://$IP:$PORT/`, for more info see [Dokuwiki](https://www.dokuwiki.org/dokuwiki/)


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27dokuwiki%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=dokuwiki "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it dokuwiki /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f dokuwiki`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' dokuwiki`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/dokuwiki`

## Versions

* **19.12.19:** - Rebasing to alpine 3.11.
* **01.12.19:** - Add php7-ldap package to support LDAP authentication.
* **28.05.19:** - Initial Release.
