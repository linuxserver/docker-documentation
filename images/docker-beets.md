# [linuxserver/beets](https://github.com/linuxserver/docker-beets)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-beets.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-beets)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-beets.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-beets/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-beets/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-beets/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/beets.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/beets "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/beets.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/beets)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/beets.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/beets)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-beets%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-beets/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flspipepr%2Fbeets%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/beets/latest/index.html)

[Beets](http://beets.io/) is a music library manager and not, for the most part, a music player. It does include a simple player plugin and an experimental Web-based player, but it generally leaves actual sound-reproduction to specialized tools.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/beets` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | Stable Beets Releases |
| nightly | Built against head of Beets git, generally considered unstable but a likely choice for power users of the application. |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=beets \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8337:8337 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/music/library>:/music \
  -v </path/to/ingest>:/downloads \
  --restart unless-stopped \
  linuxserver/beets
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  beets:
    image: linuxserver/beets
    container_name: beets
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/music/library>:/music
      - </path/to/ingest>:/downloads
    ports:
      - 8337:8337
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8337` | Application WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Configuration files. |
| `/music` | Music library |
| `/downloads` | Non processed music |



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


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27beets%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=beets "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it beets /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f beets`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' beets`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/beets`

## Versions

* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **12.05.19:** - Add flac and mp3val binaries required for badfiles plugin.
* **12.04.19:** - Rebase to Alpine 3.9.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **11.03.19:** - Swap copyartifacts for extrafiles, update endpoints with nightly tag.
* **01.03.19:** - Switch to python3.
* **07.02.19:** - Add fftw-dev build dependency for chromaprint.
* **28.01.19:** - Add pipeline logic and multi arch.
* **15.08.18:** - Rebase to alpine 3.8, use alpine repo version of pylast.
* **12.08.18:** - Add requests pip package.
* **04.03.18:** - Upgrade mp3gain to 1.6.1.
* **02.01.18:** - Deprecate cpu_core routine lack of scaling.
* **27.12.17:** - Add beautifulsoup4 pip package.
* **06.12.17:** - Rebase to alpine linux 3.7.
* **25.05.17:** - Rebase to alpine linux 3.6.
* **06.02.17:** - Rebase to alpine linux 3.5.
* **16.01.17:** - Add packages required for replaygain.
* **24.12.16:** - Add [beets-copyartifacts](https://github.com/sbarakat/beets-copyartifacts) plugin.
* **07.12.16:** - Edit cmake options for chromaprint, should now build and install fpcalc, add gstreamer lib
* **14.10.16:** - Add version layer information.
* **01.10.16:** - Add nano and editor variable to allow editing of the config from the container command line.
* **30.09.16:** - Fix umask.
* **24.09.16:** - Rebase to alpine linux.
* **10.09.16:** - Add layer badges to README.
* **05.01.16:** - Change ffpmeg repository, other version crashes container
* **06.11.15:** - Initial Release
* **29.11.15:** - Take out term setting, causing issues with key entry for some users
