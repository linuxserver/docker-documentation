# [linuxserver/rsnapshot](https://github.com/linuxserver/docker-rsnapshot)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-rsnapshot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-rsnapshot)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-rsnapshot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-rsnapshot/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-rsnapshot/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-rsnapshot/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/rsnapshot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/rsnapshot "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/rsnapshot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/rsnapshot)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/rsnapshot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/rsnapshot)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-rsnapshot%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-rsnapshot/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Frsnapshot%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/rsnapshot/latest/index.html)

[Rsnapshot](http://www.rsnapshot.org/) is a filesystem snapshot utility based on rsync. rsnapshot makes it easy to make periodic snapshots of local machines, and remote machines over ssh. The code makes extensive use of hard links whenever possible, to greatly reduce the disk space required."


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `ghcr.io/linuxserver/rsnapshot` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker-compose ([recommended](https://docs.linuxserver.io/general/docker-compose))

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  rsnapshot:
    image: ghcr.io/linuxserver/rsnapshot
    container_name: rsnapshot
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/New_York
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/snapshots>:/.snapshots #optional
      - </path/to/data>:/data #optional
    restart: unless-stopped
```

### docker cli

```
docker run -d \
  --name=rsnapshot \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=America/New_York \
  -v </path/to/appdata/config>:/config \
  -v </path/to/snapshots>:/.snapshots `#optional` \
  -v </path/to/data>:/data `#optional` \
  --restart unless-stopped \
  ghcr.io/linuxserver/rsnapshot
```


## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=America/New_York` | Specify a timezone to use EG America/New_York |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains all relevant configuration files. |
| `/.snapshots` | Storage location for all snapshots. |
| `/data` | Storage location for data to be backed up. |



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

### IMPORTANT NOTES:
After starting the container you will need to edit `/config/rsnapshot.conf`.

#### SNAPSHOT ROOT DIRECTORY

rsnapshot is configured to backup data to the `/.snapshots` volume by default.
This can be changed in the config, but be sure you mount a volume to the container to match.

#### BACKUP LEVELS / INTERVALS

rsnapshot retains backups based on configurations in this section.
Please see the [rsnapshot readme](https://github.com/rsnapshot/rsnapshot/blob/master/README.md#configuration) for more information.

#### BACKUP POINTS

rsnapshot is configured to backup data from the `/data` volume by default.
This can be changed in the config, but be sure you mount a volume to the container to match.

### cron

You will then need to edit `/config/crontabs/root` to set cron jobs to run rsnapshot.
By default no cron jobs are enabled. Examples are includes based on information from the [rsnapshot readme](https://github.com/rsnapshot/rsnapshot/blob/master/README.md#configuration).


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=rsnapshot&query=%24.mods%5B%27rsnapshot%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=rsnapshot "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it rsnapshot /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f rsnapshot`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' rsnapshot`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ghcr.io/linuxserver/rsnapshot`

## Versions

* **20.08.20:** - Initial Release.
