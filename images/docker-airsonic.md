# [linuxserver/airsonic](https://github.com/linuxserver/docker-airsonic)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-airsonic.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-airsonic)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-airsonic.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-airsonic/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-airsonic/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-airsonic/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/airsonic.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/airsonic "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/airsonic.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/airsonic)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/airsonic.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/airsonic)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-airsonic%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-airsonic/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flspipepr%2Fairsonic%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/airsonic/latest/index.html)

[Airsonic](https://github.com/airsonic/airsonic) is a free, web-based media streamer, providing ubiquitious access to your music. Use it to share your music with friends, or to listen to your own music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/airsonic` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=airsonic \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e CONTEXT_PATH=<URL_BASE> `#optional` \
  -e JAVA_OPTS=<options> `#optional` \
  -p 4040:4040 \
  -v </path/to/config>:/config \
  -v </path/to/music>:/music \
  -v </path/to/playlists>:/playlists \
  -v </path/to/podcasts>:/podcasts \
  -v </path/to/other media>:/media `#optional` \
  --device /dev/snd:/dev/snd `#optional` \
  --restart unless-stopped \
  linuxserver/airsonic
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  airsonic:
    image: linuxserver/airsonic
    container_name: airsonic
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - CONTEXT_PATH=<URL_BASE> #optional
      - JAVA_OPTS=<options> #optional
    volumes:
      - </path/to/config>:/config
      - </path/to/music>:/music
      - </path/to/playlists>:/playlists
      - </path/to/podcasts>:/podcasts
    volumes:
      - </path/to/other media>:/media #optional
    ports:
      - 4040:4040
    devices:
      - /dev/snd:/dev/snd #optional
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `4040` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `CONTEXT_PATH=<URL_BASE>` | For setting url-base in reverse proxy setups. |
| `JAVA_OPTS=<options>` | For passing additional java options. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Configuration file location. |
| `/music` | Location of music. |
| `/playlists` | Location for playlists to be saved to. |
| `/podcasts` | Location of podcasts. |
| `/media` | Location of other media. |

#### Device Mappings (`--device`)
| Parameter | Function |
| :-----:   | --- |
| `/dev/snd` | Only needed to pass your host sound device to Airsonic's Java jukebox player. |


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

Access WebUI at `<your-ip>:4040`.

Default user/pass is admin/admin

Extra java options can be passed with the JAVA_OPTS environment variable, eg `-e JAVA_OPTS="-Xmx256m -Xms256m"`. For some reverse proxies, you may need to pass `JAVA_OPTS=-Dserver.use-forward-headers=true` for airsonic to generate the proper URL schemes.

Note that if you want to use [Airsonic's Java jukebox player](https://airsonic.github.io/docs/jukebox/), then `PGID` will need to match the group of your sound device (e.g. `/dev/snd`).


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27airsonic%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=airsonic "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it airsonic /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f airsonic`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' airsonic`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/airsonic`

## Versions

* **24.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **26.01.19:** - Add pipeline logic and multi arch.
* **05.01.19:** - Linting fixes.
* **27.08.18:** - Use new inhouse java baseimage for quicker builds.
* **23.08.18:** - Rebase to ubuntu bionic for increased performance across all arch's.
* **22.04.18:** - Add the forgotten JAVA_OPTS to the run command.
* **29.12.17:** - Initial Release.
