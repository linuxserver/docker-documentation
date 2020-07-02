# [linuxserver/sickgear](https://github.com/linuxserver/docker-sickgear)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-sickgear.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-sickgear)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-sickgear.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-sickgear/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-sickgear/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-sickgear/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/sickgear.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/sickgear "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/sickgear.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/sickgear)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/sickgear.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/sickgear)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-sickgear%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-sickgear/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fsickgear%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/sickgear/latest/index.html)

[SickGear](https://github.com/sickgear/sickgear) provides management of TV shows and/or Anime, it detects new episodes, links downloader apps, and more.. 

For more information on SickGear visit their website and check it out: https://github.com/SickGear/SickGear


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/sickgear` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=sickgear \
  -e PUID=1000 \
  -e PGID=1000 \
  -p 8081:8081 \
  -v /path/to/data:/config \
  -v /path/to/data:/tv \
  -v /path/to/data:/downloads \
  --restart unless-stopped \
  linuxserver/sickgear
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  sickgear:
    image: linuxserver/sickgear
    container_name: sickgear
    environment:
      - PUID=1000
      - PGID=1000
    volumes:
      - /path/to/data:/config
      - /path/to/data:/tv
      - /path/to/data:/downloads
    ports:
      - 8081:8081
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8081` | will map the container's port 8081 to port 8081 on the host |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | this will store any uploaded data on the docker host |
| `/tv` | where you store your tv shows |
| `/downloads` | your downloads folder for post processing (must not be download in progress) |



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

## Setting up the application

Access the webui at `<your-ip>:8081`, for more information check out [SickGear](https://github.com/sickgear/sickgear).

## Migration

Non linuxserver.io containers are known to have the following configuration differences and may need SickGear or docker changes to migrate an existing setup

* The post processing directory which is volume mounted as `downloads` within this container may be `incoming` in other versions.

* The permissions environmental variables which are defined as `PGID` and `PUID` within this container may have been `APP_UID` and `APP_UID` in other versions.

* The configuration file directory which is volume mounted as `config` within this container may be set as the environmetal variable `APP_DATA` in other versions.

* The cache directory which is set in `config.ini` may be configured as a fixed path `cache_dir = /data/cache`. 
Symptoms of this issue include port usage problems and a failure to start the web server log entries. 
Whilst the container is stopped alter this directive to `cache_dir = cache` which will allow SickGear to look for the folder relative to the volume mounted `/config` directory.

It is recommended that a clean install be completed, rather than a migration, however if migration is necessary:

* start a new instance of this image

* compare and align SickGear version numbers bewteen old and new. Ideally they should match but at a minumum the old vesion should be a lower version number to allow SickGear itself to try and migrate

* stop both containers

* notice the configuration difference and migrate copies of the old settings into the new app

* start the new container and test


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27sickgear%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=sickgear "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it sickgear /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f sickgear`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' sickgear`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/sickgear`

## Versions

* **03.06.20:** - Rebasing to alpine 3.12, switch to python3.
* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **07.11.18:** - Pipeline prep
* **07.07.18:** - Initial draft release
