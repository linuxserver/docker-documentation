---
title: radarr
---
# [linuxserver/radarr](https://github.com/linuxserver/docker-radarr)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-radarr.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-radarr)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-radarr.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-radarr/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-radarr/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-radarr/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/radarr.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/radarr "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/radarr.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/radarr)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/radarr.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/radarr)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-radarr%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-radarr/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fradarr%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/radarr/latest/index.html)

[Radarr](https://github.com/Radarr/Radarr) - A fork of Sonarr to work with movies à la Couchpotato.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `ghcr.io/linuxserver/radarr` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :----: | --- |
| latest | Stable Radarr releases |
| develop | Radarr releases from their develop branch |
| nightly | Radarr releases from their nightly branch |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker-compose ([recommended](https://docs.linuxserver.io/general/docker-compose))

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  radarr:
    image: ghcr.io/linuxserver/radarr
    container_name: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /path/to/data:/config
      - /path/to/movies:/movies
      - /path/to/downloadclient-downloads:/downloads
    ports:
      - 7878:7878
    restart: unless-stopped
```

### docker cli

```
docker run -d \
  --name=radarr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 7878:7878 \
  -v /path/to/data:/config \
  -v /path/to/movies:/movies \
  -v /path/to/downloadclient-downloads:/downloads \
  --restart unless-stopped \
  ghcr.io/linuxserver/radarr
```


## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `7878` | The port for the Radarr webinterface |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London, this is required for Radarr |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Database and Radarr configs |
| `/movies` | Location of Movie library on disk (See note in Application setup) |
| `/downloads` | Location of download managers output directory (See note in Application setup) |



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

Access the webui at `<your-ip>:7878`, for more information check out [Radarr](https://github.com/Radarr/Radarr).

**Special Note**: Following our current folder structure will result in an inability to hardlink from your downloads to your movies folder because they are on seperate volumes. To support hardlinking, ensure that the movies and downloads data are on a single volume. For example, if you have `/mnt/storage/Movies` and `/mnt/storage/downloads/completed/Movies`, you would want something like `/mnt/storage:/media` for your volume. Then you can hardlink from `/media/downloads/completed` to `/media/Movies`.

Another item to keep in mind, is that within Radarr itself, you should map your download client folder to your radarr folder. Navigate to **Settings -> Download Client -> Advanced Settings -> Remote Path Mappings**. Add a new mapping, and set: the Host as the same entry of the Host in your download client (for example its IP address), the Remote Path as `/downloads/Movies` (relative to the internal container path), and Local Path as `/media/downloads/completed/Movies`, assuming you have folders to separate your downloaded data types.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=radarr&query=%24.mods%5B%27radarr%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=radarr "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it radarr /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f radarr`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' radarr`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ghcr.io/linuxserver/radarr`

## Versions

* **17.01.21:** - Deprecate `UMASK_SET` in favor of UMASK in baseimage, see above for more information.
* **11.30.20:** - Publish `develop` tag.
* **11.28.20:** - Switch to v3 .NET CORE builds (no more mono, `5.14` tag is deprecated). Rebase to Focal (for issues on arm32v7, [see here](https://docs.linuxserver.io/faq#my-host-is-incompatible-with-images-based-on-ubuntu-focal)).
* **05.04.20:** - Move app to /app.
* **01.08.19:** - Rebase to Linuxserver LTS mono version.
* **13.06.19:** - Add env variable for setting umask.
* **10.05.19:** - Rebase to Bionic.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **09.09.18:** - Add pipeline build process.
* **24.02.18:** - Add nightly branch.
* **06.02.18:** - Radarr repo changed owner.
* **15.12.17:** - Fix continuation lines.
* **17.04.17:** - Switch to using inhouse mono baseimage, adds python also.
* **13.04.17:** - Switch to official mono repository.
* **10.01.17:** - Initial Release.
