# [linuxserver/foldingathome](https://github.com/linuxserver/docker-foldingathome)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-foldingathome.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-foldingathome)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-foldingathome.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-foldingathome/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-foldingathome/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-foldingathome/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/foldingathome)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/foldingathome.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/foldingathome "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/foldingathome.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/foldingathome)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/foldingathome.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/foldingathome)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-foldingathome/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-foldingathome/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/foldingathome/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/foldingathome/latest/index.html)

[Folding@home](https://foldingathome.org/) is a distributed computing project for simulating protein dynamics, including the process of protein folding and the movements of proteins implicated in a variety of diseases. It brings together citizen scientists who volunteer to run simulations of protein dynamics on their personal computers. Insights from this data are helping scientists to better understand biology, and providing new opportunities for developing therapeutics.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/foldingathome` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=foldingathome \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 7396:7396 \
  -p 36330:36330 `#optional` \
  -v /path/to/data:/config \
  --restart unless-stopped \
  linuxserver/foldingathome
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  foldingathome:
    image: linuxserver/foldingathome
    container_name: foldingathome
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /path/to/data:/config
    ports:
      - 7396:7396
    ports:
      - 36330:36330 #optional
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `7396` | Folding@home web gui. |
| `36330` | Optional port for connecting remotely via FAHControl app (no password). |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where Folding@home should store its database and config. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

This image sets up the Folding@home client. The interface is available at `http://your-ip:7396`.

The built-in webserver provides very basic control (ie. GPUs are only active when set to `Medium` or higher). For more fine grained control of individual devices, you can use the FAHControl app on a different device and connect remotely via port `36330` (no password).

## GPU Hardware Acceleration

### Nvidia

Hardware acceleration users for Nvidia will need to install the container runtime provided by Nvidia on their host, instructions can be found here:
https://github.com/NVIDIA/nvidia-docker
We automatically add the necessary environment variable that will utilise all the features available on a GPU on the host. Once nvidia-docker is installed on your host you will need to re/create the docker container with the nvidia container runtime `--runtime=nvidia` and add an environment variable `-e NVIDIA_VISIBLE_DEVICES=all` (can also be set to a specific gpu's UUID, this can be discovered by running `nvidia-smi --query-gpu=gpu_name,gpu_uuid --format=csv` ). NVIDIA automatically mounts the GPU and drivers from your host into the foldingathome docker container.



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it foldingathome /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f foldingathome`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' foldingathome`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/foldingathome`

## Versions

* **20.03.20:** - Initial release.
