# linuxserver/photoshow

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-photoshow.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-photoshow) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-photoshow.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-photoshow/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-photoshow/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-photoshow/container_registry) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/photoshow.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/photoshow) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/photoshow.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/photoshow) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/photoshow.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/photoshow) [![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-photoshow%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-photoshow/job/master/) [![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fphotoshow%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/photoshow/latest/index.html)

[Photoshow](https://github.com/thibaud-rohmer/PhotoShow) is gallery software at its easiest, it doesn't even require a database.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/photoshow` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :---: | :--- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=photoshow \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 80:80 \
  -v <path to data>:/config \
  -v <path to pictures>:/Pictures:ro \
  -v <path to store thumbs>:/Thumbs \
  --restart unless-stopped \
  linuxserver/photoshow
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  photoshow:
    image: linuxserver/photoshow
    container_name: photoshow
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
      - <path to pictures>:/Pictures:ro
      - <path to store thumbs>:/Thumbs
    ports:
      - 80:80
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `80` | WebUI |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Stores config and logs for nginx base. |
| `/Pictures:ro` | Your local folder of photos you wish to share. |
| `/Thumbs` | Local folder to store thumbnails of your images. |

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

On first run create an admin account, any folder and its subfolders that you map to /Pictures will be presented as a webgallery. Config settings are persistent and stored as a subfolder of the /Thumbs mapping.

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27photoshow%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=photoshow)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it photoshow /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f photoshow`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' photoshow`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/photoshow`

## Versions

* **01.06.20:** - Rebasing to alpine 3.12.
* **19.12.19:** - Rebasing to alpine 3.11.
* **23.09.19:** - Adding PHP-Exif for image metadata and processing.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **16.01.19:** - Add pipeline logic and multi arch.
* **05.09.18:** - Rebase to alpine 3.8.
* **07.01.18:** - Rebase to alpine 3.7.
* **25.05.17:** - Rebase to alpine 3.6.
* **03.05.17:** - Use repo pinning to better solve dependencies, use repo version of php7-imagick.
* **14.02.17:** - Rebase to alpine 3.5.
* **14.10.16:** - Add version layer information.
* **30.09.16:** - Rebase to alpine linux.
* **11.09.16:** - Add layer badges to README.
* **21.08.15:** - Use patched keybaord js from fork of photoshow.
* **21.08.15:** - Initial Release.

