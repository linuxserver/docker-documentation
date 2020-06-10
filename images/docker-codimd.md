# [linuxserver/codimd](https://github.com/linuxserver/docker-codimd)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-codimd.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-codimd)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-codimd.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-codimd/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-codimd/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-codimd/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/codimd.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/codimd "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/codimd.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/codimd)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/codimd.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/codimd)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-codimd%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-codimd/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fcodimd%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/codimd/latest/index.html)

[Codimd](https://demo.codimd.org) gives you access to all your files wherever you are.

CodiMD is a real-time, multi-platform collaborative markdown note editor.  This means that you can write notes with other people on your desktop, tablet or even on the phone.  You can sign-in via multiple auth providers like Facebook, Twitter, GitHub and many more on the homepage.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/codimd` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=codimd \
  -e PUID=1000 \
  -e PGID=1000 \
  -e DB_HOST=<hostname or ip> \
  -e DB_PORT=3306 \
  -e DB_USER=codimd \
  -e DB_PASS=<secret password> \
  -e DB_NAME=codimd \
  -e TZ=Europe/London \
  -p 3000:3000 \
  -v </path/to/appdata>:/config \
  --restart unless-stopped \
  linuxserver/codimd
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
version: "3"
services:
  mariadb:
    image: linuxserver/mariadb:latest
    container_name: codimd_mariadb
    restart: always
    volumes:
      - <path to mariadb data>:/config
    environment:
      - MYSQL_ROOT_PASSWORD=<secret password>
      - MYSQL_DATABASE=codimd
      - MYSQL_USER=codimd
      - MYSQL_PASSWORD=<secret password>
      - PGID=1000
      - PUID=1000
      - TZ=Europe/London
  codimd:
    image: linuxserver/codimd:latest
    container_name: codimd
    restart: always
    depends_on:
      - mariadb
    volumes:
      - <path to config>:/config
    environment:
      - DB_HOST=mariadb
      - DB_USER=codimd
      - DB_PASS=<secret password>
      - DB_NAME=codimd
      - DB_PORT=3306
      - PGID=1000
      - PUID=1000
      - TZ=Europe/London
    ports:
      - "3000:3000"

```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3000` | If you wish to access this container from http://{IP}:${PORT}` this *must* be left unchanged. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `DB_HOST=<hostname or ip>` | Host address of mysql database |
| `DB_PORT=3306` | Port to access mysql database default is 3306 |
| `DB_USER=codimd` | Database user |
| `DB_PASS=<secret password>` | Database password |
| `DB_NAME=codimd` | Database name |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | CodiMD config and configurable files |



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

CodiMD web interface can be accessed `http://${IP}:3000/`, if you want to use a custom domain or anything besides port 3000 you will need to leverage their env settings for callbacks: (specifically for CMD_DOMAIN and CMD_URL_ADDPORT)

[Full list of CodiMD options](https://github.com/codimd/server/blob/master/docs/configuration-env-vars.md)

For convience we provide a working example using Mysql as a backend in this document, if you do not wish to use our custom environment values or a Mysql database backend feel free to leverage any of the settings laid out in the link above.

To run behind a reverse proxy we have a [preconfigured config](https://github.com/linuxserver/reverse-proxy-confs/blob/master/codimd.subdomain.conf.sample) using docker networking included in our [LetsEncrypt](https://github.com/linuxserver/docker-letsencrypt) image and you can read how to use this in the [Reverse Proxy Confs repository](https://github.com/linuxserver/reverse-proxy-confs/#how-to-use-these-reverse-proxy-configs)


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27codimd%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=codimd "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it codimd /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f codimd`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' codimd`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/codimd`

## Versions

* **23.05.19:** - Initial release
