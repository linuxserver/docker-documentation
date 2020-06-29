# [linuxserver/boinc](https://github.com/linuxserver/docker-boinc)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-boinc.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-boinc)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-boinc.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-boinc/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-boinc/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-boinc/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/boinc.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/boinc "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/boinc.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/boinc)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/boinc.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/boinc)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-boinc%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-boinc/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fboinc%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/boinc/latest/index.html)

[BOINC](https://boinc.berkeley.edu/) is a platform for high-throughput computing on a large scale (thousands or millions of computers). It can be used for volunteer computing (using consumer devices) or grid computing (using organizational resources). It supports virtualized, parallel, and GPU-based applications.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/boinc` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=boinc \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e GUAC_USER=abc `#optional` \
  -e GUAC_PASS=900150983cd24fb0d6963f7d28e17f72 `#optional` \
  -p 8080:8080 \
  -v /path/to/data:/config \
  --device /dev/dri:/dev/dri `#optional` \
  --restart unless-stopped \
  linuxserver/boinc
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  boinc:
    image: linuxserver/boinc
    container_name: boinc
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - GUAC_USER=abc #optional
      - GUAC_PASS=900150983cd24fb0d6963f7d28e17f72 #optional
    volumes:
      - /path/to/data:/config
    ports:
      - 8080:8080
    devices:
      - /dev/dri:/dev/dri #optional
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8080` | Boinc desktop gui. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `GUAC_USER=abc` | Username for the BOINC desktop gui. |
| `GUAC_PASS=900150983cd24fb0d6963f7d28e17f72` | Password's md5 hash for the BOINC desktop gui. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where BOINC should store its database and config. |

#### Device Mappings (`--device`)
| Parameter | Function |
| :-----:   | --- |
| `/dev/dri` | Only needed if you want to use your Intel GPU (vaapi). |


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

This image sets up the BOINC client and manager and makes its interface available via Guacamole server in the browser. The interface is available at `http://your-ip:8080`.

By default, there is no username or password set. Custom usernames and passwords can be set via optional docker environment variables. Keep in mind that the `GUACPASS` variable accepts the `md5 hash` of the desired password (the sample above is the hash for `abc`). The md5 hash can be generated by either of the following commands:

```
echo -n password | openssl md5
```

```
printf '%s' password | md5sum
```

You can access advanced features of the Guacamole remote desktop using `ctrl`+`alt`+`shift` enabling you to use remote copy/paste and different languages.

It is recommended to switch to `Advanced View` in the top menu, because the `Computing Preferences` don't seem to be displayed in `Simple View`.

Sometimes, the pop-up windows may open in a tiny box in the upper left corner of the screen. When that happens, you can find the corner and resize them.

## GPU Hardware Acceleration

### Intel

Hardware acceleration users for Intel Quicksync will need to mount their /dev/dri video device inside of the container by passing the following command when running or creating the container:
```--device=/dev/dri:/dev/dri```
We will automatically ensure the abc user inside of the container has the proper permissions to access this device.

### Nvidia

Hardware acceleration users for Nvidia will need to install the container runtime provided by Nvidia on their host, instructions can be found here:
https://github.com/NVIDIA/nvidia-docker
We automatically add the necessary environment variable that will utilise all the features available on a GPU on the host. Once nvidia-docker is installed on your host you will need to re/create the docker container with the nvidia container runtime `--runtime=nvidia` and add an environment variable `-e NVIDIA_VISIBLE_DEVICES=all` (can also be set to a specific gpu's UUID, this can be discovered by running `nvidia-smi --query-gpu=gpu_name,gpu_uuid --format=csv` ). NVIDIA automatically mounts the GPU and drivers from your host into the BOINC docker container.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27boinc%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=boinc "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it boinc /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f boinc`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' boinc`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/boinc`

## Versions

* **01.04.20:** - Install boinc from ppa.
* **17.03.20:** - Add armhf and aarch64 builds and switch to multi-arch image.
* **16.03.20:** - Clean up old pid files.
* **15.03.20:** - Initial release.
