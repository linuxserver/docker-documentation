# [linuxserver/oscam](https://github.com/linuxserver/docker-oscam)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/oscam.svg)](https://microbadger.com/images/linuxserver/oscam "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/oscam.svg)](https://microbadger.com/images/linuxserver/oscam "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/oscam.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/oscam.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-oscam/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-oscam/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/oscam/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/oscam/latest/index.html)

[Oscam](http://www.streamboard.tv/oscam/) is an Open Source Conditional Access Module software used for descrambling DVB transmissions using smart cards. It's both a server and a client.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/oscam` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=oscam \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=Europe/London \
  -p 8888:8888 \
  -v <path to data>:/config \
  --device /dev/ttyUSB0:/dev/ttyUSB0 \
  --restart unless-stopped \
  linuxserver/oscam
```

### Passing through Smart Card Readers

If you want to pass through a smart card reader, you need to specify the reader with the `--device=` tag. The method used depends on how the reader is recognized.
The first is /dev/ttyUSBX. To find the correct device, connect the reader and run `dmesg | tail` on the host. In the output you will find /dev/ttyUSBX, where X is the number of the device. If this is the first reader you connect to your host, it will be /dev/ttyUSB0. If you add one more it will be /dev/ttyUSB1.

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
version: "2"
services:
  oscam:
    image: linuxserver/oscam
    container_name: oscam
    environment:
      - PUID=1001
      - PGID=1001
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
    ports:
      - 8888:8888
    devices:
      - /dev/ttyUSB0:/dev/ttyUSB0
    mem_limit: 4096m
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8888` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1001` | for UserID - see below for explanation |
| `PGID=1001` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where oscam should store config files and logs. |

#### Device Mappings (`--device`)
| Parameter | Function |
| :-----:   | --- |
| `/dev/ttyUSB0` | For passing through smart card readers. |


## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1001` and `PGID=1001`, to find yours use `id user` as below:

```
  $ id username
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Application Setup

To set up oscam there are numerous guides on the internet. There are too many scenarios to make a quick guide.
The web interface is at port 8888.



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

* **19.02.19:** - Add pipeline logic and multi arch, rebase to Alpine 3.8.
* **03.01.18:** - Deprecate cpu_core routine lack of scaling.
* **13.12.17:** - Rebase to alpine 3.7.
* **19.10.17:** - Add ccid package for usb card readers.
* **17.10.17:** - Switch to using bzr for source code, streamboard awol.
* **28.05.17:** - Rebase to alpine 3.6.
* **09.02.17:** - Rebase to alpine 3.5.
* **14.10.16:** - Add version layer information.
* **02.10.16:** - Add info on passing through devices to README.
* **25.09.16:** - Initial release.
