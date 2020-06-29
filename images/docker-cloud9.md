# linuxserver/cloud9

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-cloud9.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-cloud9) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-cloud9.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-cloud9/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-cloud9/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-cloud9/container_registry) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/cloud9.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/cloud9) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/cloud9.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/cloud9) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/cloud9.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/cloud9) [![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-cloud9%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-cloud9/job/master/) [![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fcloud9%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/cloud9/latest/index.html)

[Cloud9](https://github.com/c9/core) Cloud9 is a complete web based IDE with terminal access. This container is for running their core SDK locally and developing plugins.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/cloud9` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
| latest | Docker and Compose environment pre-installed |
| go | Basic Golang environment pre-installed |
| nodejs | Current stable NodeJS/NPM environment pre-installed |
| python | Current Python3 environment pre-installed |
| ruby | Current Ruby environment pre-installed |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=cloud9 \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e GITURL=https://github.com/linuxserver/docker-cloud9.git `#optional` \
  -e USERNAME= `#optional` \
  -e PASSWORD= `#optional` \
  -p 8000:8000 \
  -v /path/to/your/code:/code `#optional` \
  -v /var/run/docker.sock:/var/run/docker.sock `#optional` \
  --restart unless-stopped \
  linuxserver/cloud9
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  cloud9:
    image: linuxserver/cloud9
    container_name: cloud9
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - GITURL=https://github.com/linuxserver/docker-cloud9.git #optional
      - USERNAME= #optional
      - PASSWORD= #optional
    volumes:
    volumes:
      - /path/to/your/code:/code #optional
      - /var/run/docker.sock:/var/run/docker.sock #optional
    ports:
      - 8000:8000
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `8000` | The port for the Cloud9 web interface |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `GITURL=https://github.com/linuxserver/docker-cloud9.git` | Specify a git repo to checkout on first startup |
| `USERNAME=` | Optionally specify a username for http auth |
| `PASSWORD=` | Optionally specify a password for http auth \(if USERNAME and PASSWORD are not set, there will be no http auth\) |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/code` | Optionally if you want to mount up a local folder of code instead of checking out |
| `/var/run/docker.sock` | Needed if you plan to use Docker or compose commands |

## Environment variables from files \(Docker secrets\)

You can set any environment variable from a file by using a special prepend `FILE__`.

As an example:

```text
-e FILE__PASSWORD=/run/secrets/mysecretpassword
```

Will set the environment variable `PASSWORD` based on the contents of the `/run/secrets/mysecretpassword` file.

## Umask for running applications

For all of our images we provide the ability to override the default umask settings for services started within the containers using the optional `-e UMASK=022` setting. Keep in mind umask is not chmod it subtracts from permissions based on it's value it does not add. Please read up [here](https://en.wikipedia.org/wiki/Umask) before asking for support.

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at [http://your-ip:8000](http://your-ip:8000), for more information check out [here](https://docs.c9.io/docs).

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27cloud9%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=cloud9)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it cloud9 /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f cloud9`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' cloud9`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/cloud9`

## Versions

* **07.02.20:** - Add optional http auth.
* **02.06.19:** - Initial Release.

