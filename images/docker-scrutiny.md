# [linuxserver/scrutiny](https://github.com/linuxserver/docker-scrutiny)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-scrutiny.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-scrutiny)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-scrutiny.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-scrutiny/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-scrutiny/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-scrutiny/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/scrutiny.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/scrutiny "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/scrutiny.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/scrutiny)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/scrutiny.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/scrutiny)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-scrutiny%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-scrutiny/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fscrutiny%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/scrutiny/latest/index.html)

[Scrutiny](https://github.com/AnalogJ/scrutiny) WebUI for smartd S.M.A.R.T monitoring. Scrutiny is a Hard Drive Health Dashboard & Monitoring solution, merging manufacturer provided S.M.A.R.T metrics with real-world failure rates from Backblaze.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `ghcr.io/linuxserver/scrutiny` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  scrutiny:
    image: ghcr.io/linuxserver/scrutiny
    container_name: scrutiny
    cap_add:
      - SYS_RAWIO
      - SYS_ADMIN #optional
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - SCRUTINY_API_ENDPOINT=http://localhost:8080
      - SCRUTINY_WEB=true
      - SCRUTINY_COLLECTOR=true
    volumes:
      - /path/to/config:/config
      - /run/udev:/run/udev:ro
    ports:
      - 8080:8080
    devices:
      - /dev/sda:/dev/sda
      - /dev/sdb:/dev/sdb
      - /dev/nvme1n1:/dev/nvme1n1
    restart: unless-stopped
```

### docker cli

```
docker run -d \
  --name=scrutiny \
  --cap-add=SYS_RAWIO \
  --cap-add=SYS_ADMIN `#optional` \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e SCRUTINY_API_ENDPOINT=http://localhost:8080 \
  -e SCRUTINY_WEB=true \
  -e SCRUTINY_COLLECTOR=true \
  -p 8080:8080 \
  -v /path/to/config:/config \
  -v /run/udev:/run/udev:ro \
  --device /dev/sda:/dev/sda \
  --device /dev/sdb:/dev/sdb \
  --device /dev/nvme1n1:/dev/nvme1n1 \
  --restart unless-stopped \
  ghcr.io/linuxserver/scrutiny
```


## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8080` | Port for scrutiny's web interface and API. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `SCRUTINY_API_ENDPOINT=http://localhost:8080` | # optional - API endpoint of the scrutiny UI. Do not change unless using as a remote collector |
| `SCRUTINY_WEB=true` | # optional - Run the web service. |
| `SCRUTINY_COLLECTOR=true` | # optional - Run the metrics collector. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where config is stored. |
| `/run/udev:ro` | Provides necessary metadata to Scrutiny. |

#### Device Mappings (`--device`)
| Parameter | Function |
| :-----:   | --- |
| `/dev/sda` | This is how Scrutiny accesses drives. Optionally supply `/dev:/dev` instead for all devices. |
| `/dev/sdb` | A second drive. |
| `/dev/nvme1n1` | An NVMe drive. NVMe requires `--cap-add=SYS_ADMIN`. |


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

This container can be run as an 'all-in-one' deployment or as a hub / spoke deployment. Use the environment variables `SCRUTINY_WEB` and `SCRUTINY_COLLECTOR` to control the mode of the container. Setting both to `true` will deploy the container as both a collector and the web UI - this is the simplest and most straightforward deployment approach. To make use of the hub and spoke model, run this container in "collector" mode by specifying `SCRUTINY_API_ENDPOINT`. Set this to the host that is running the API. For this to work, you will need to expose the API port directly from the container (by default this is `8080`).

You may need to manually enter the container to run `scrutiny-collector-metrics run` for your first job or wait until around midnight for it to kick off.

A fully commented example configuration yaml file can be found in the original project repository [here](https://github.com/AnalogJ/scrutiny/blob/master/example.scrutiny.yaml). Place this file in the location mounted to `/config`.

A note on `--cap-add` for this container: 
  * `SYS_RAWIO` is necessary to allow smartctl permission to query your device SMART data.
  * `SYS_ADMIN` is required for NVMe drives as per upstream issue [#26](https://github.com/AnalogJ/scrutiny/issues/26#issuecomment-696817130). 


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=scrutiny&query=%24.mods%5B%27scrutiny%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=scrutiny "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it scrutiny /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f scrutiny`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' scrutiny`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ghcr.io/linuxserver/scrutiny`

## Versions

* **17.09.20:** - Initial Release.
