# linuxserver/oscam

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-oscam.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-oscam) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-oscam.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-oscam/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-oscam/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-oscam/container_registry) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/oscam.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/oscam) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/oscam.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/oscam) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/oscam.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/oscam) [![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-oscam%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-oscam/job/master/) [![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Foscam%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/oscam/latest/index.html)

[Oscam](http://www.streamboard.tv/oscam/) is an Open Source Conditional Access Module software used for descrambling DVB transmissions using smart cards. It's both a server and a client.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/oscam` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=oscam \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8888:8888 \
  -v <path to data>:/config \
  --device /dev/ttyUSB0:/dev/ttyUSB0 \
  --restart unless-stopped \
  linuxserver/oscam
```

### Passing through Smart Card Readers

If you want to pass through a smart card reader, you need to specify the reader with the `--device=` tag. The method used depends on how the reader is recognized. The first is /dev/ttyUSBX. To find the correct device, connect the reader and run `dmesg | tail` on the host. In the output you will find /dev/ttyUSBX, where X is the number of the device. If this is the first reader you connect to your host, it will be /dev/ttyUSB0. If you add one more it will be /dev/ttyUSB1.

If there are no /dev/ttyUSBX device in `dmesg | tail`, you have to use the USB bus path. It will look similar to the below.

`/dev/bus/usb/001/001`

The important parts are the two numbers in the end. The first one is the Bus number, the second is the Device number. To find the Bus and Device number you have to run `lsusb` on the host, then find your USB device in the list and note the Bus and Device numbers.

Here is an example of how to find the Bus and Device. The output of the lsusb command is below.

`Bus 002 Device 005: ID 076b:6622 OmniKey AG CardMan 6121`

The first number, the Bus, is 002. The second number, the Device, is 005. This will look like below in the `--device=` tag.

`--device=/dev/bus/usb/002/005`

If you have multiple smart card readers, you add one `--device=` tag for each reader.

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  oscam:
    image: linuxserver/oscam
    container_name: oscam
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
    ports:
      - 8888:8888
    devices:
      - /dev/ttyUSB0:/dev/ttyUSB0
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `8888` | WebUI |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Where oscam should store config files and logs. |

#### Device Mappings \(`--device`\)

| Parameter | Function |
| :---: | :--- |
| `/dev/ttyUSB0` | For passing through smart card readers. |

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

To set up oscam there are numerous guides on the internet. There are too many scenarios to make a quick guide. The web interface is at port 8888.

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27oscam%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=oscam)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it oscam /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f oscam`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' oscam`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/oscam`

## Versions

* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **29.04.19:** - Add revision check, so pipeline can build new revisions.
* **28.04.19:** - Switch back to streamboard svn to fix version not showing in UI.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **19.02.19:** - Add pipeline logic and multi arch, rebase to Alpine 3.8.
* **03.01.18:** - Deprecate cpu\_core routine lack of scaling.
* **13.12.17:** - Rebase to alpine 3.7.
* **19.10.17:** - Add ccid package for usb card readers.
* **17.10.17:** - Switch to using bzr for source code, streamboard awol.
* **28.05.17:** - Rebase to alpine 3.6.
* **09.02.17:** - Rebase to alpine 3.5.
* **14.10.16:** - Add version layer information.
* **02.10.16:** - Add info on passing through devices to README.
* **25.09.16:** - Initial release.

