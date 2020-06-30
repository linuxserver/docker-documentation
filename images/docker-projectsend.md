# [linuxserver/projectsend](https://github.com/linuxserver/docker-projectsend)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-projectsend.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-projectsend)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-projectsend.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-projectsend/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-projectsend/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-projectsend/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/projectsend.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/projectsend "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/projectsend.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/projectsend)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/projectsend.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/projectsend)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-projectsend%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-projectsend/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fprojectsend%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/projectsend/latest/index.html)

[Projectsend](http://www.projectsend.org) is a self-hosted application that lets you upload files and assign them to specific clients that you create yourself. Secure, private and easy. No more depending on external services or e-mail to send those files.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/projectsend` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=projectsend \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e MAX_UPLOAD=<5000> \
  -p 80:80 \
  -v <path to data>:/config \
  -v <path to data>:/data \
  --restart unless-stopped \
  linuxserver/projectsend
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  projectsend:
    image: linuxserver/projectsend
    container_name: projectsend
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - MAX_UPLOAD=<5000>
    volumes:
      - <path to data>:/config
      - <path to data>:/data
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
| `MAX_UPLOAD=<5000>` | To set maximum upload size (in MB), default if unset is 5000. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where to store projectsend config files. |
| `/data` | Where to store files to share. |



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

*IMPORTANT* This image no longer supports MSSQL since being migrated to PHP7, if you want MSSQL support please use the tag `linuxserver/projectsend:r1053-ls27`

Requires a user and database in either mysql or mariadb.

More info at [ProjectSend](http://www.projectsend.org).


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27projectsend%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=projectsend "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it projectsend /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f projectsend`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' projectsend`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/projectsend`

## Versions

* **31.12.19:** - Rebase to Alpine 3.11 and upgrade to PHP7.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **11.02.19:** - Add pipeline logic and multi arch.
* **11.06.17:** - Fetch version from github.
* **09.12.17:** - Rebase to alpine 3.7.
* **13.06.17:** - Initial Release.
