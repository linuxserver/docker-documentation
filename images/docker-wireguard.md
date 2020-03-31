# [linuxserver/wireguard](https://github.com/linuxserver/docker-wireguard)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-wireguard.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-wireguard)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-wireguard.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-wireguard/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-wireguard/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-wireguard/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/wireguard)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/wireguard.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/wireguard "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/wireguard.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/wireguard)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/wireguard.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/wireguard)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-wireguard/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-wireguard/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/wireguard/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/wireguard/latest/index.html)

[WireGuard®](https://www.wireguard.com/) is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPsec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform (Windows, macOS, BSD, iOS, Android) and widely deployable. It is currently under heavy development, but already it might be regarded as the most secure, easiest to use, and simplest VPN solution in the industry.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/wireguard` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=wireguard \
  --cap-add=NET_ADMIN \
  --cap-add=SYS_MODULE \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e SERVERURL=wireguard.domain.com `#optional` \
  -e SERVERPORT=51820 `#optional` \
  -e PEERS=1 `#optional` \
  -e PEERDNS=8.8.8.8 `#optional` \
  -p 51820:51820/udp \
  -v /path/to/appdata/config:/config \
  -v /lib/modules:/lib/modules \
  --restart unless-stopped \
  linuxserver/wireguard
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
version: "2.1"
services:
  wireguard:
    image: linuxserver/wireguard
    container_name: wireguard
    cap_add:
      - NET_ADMIN
      - SYS_MODULE
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - SERVERURL=wireguard.domain.com #optional
      - SERVERPORT=51820 #optional
      - PEERS=1 #optional
      - PEERDNS=8.8.8.8 #optional
    volumes:
      - /path/to/appdata/config:/config
      - /lib/modules:/lib/modules
    ports:
      - 51820:51820/udp
    sysctls:
      - net.ipv4.conf.all.src_valid_mark=1
    restart: unless-stopped

```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `51820/udp` | wireguard port |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `SERVERURL=wireguard.domain.com` | External IP or domain name for docker host. Required for server mode. |
| `SERVERPORT=51820` | External port for docker host. Required for server mode. |
| `PEERS=1` | Number of peers to create confs for. Required for server mode. |
| `PEERDNS=8.8.8.8` | DNS server set in peer/client configs. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains all relevant configuration files. |
| `/lib/modules` | Maps host's modules folder. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

This image is designed for Ubuntu and Debian x86_64 systems only. During container start, it will download the necessary kernel headers and build the kernel module (until kernel 5.6, which has the module built-in, goes mainstream).

This can be run as a server or a client, based on the parameters used. 

## Server Mode
Pass the environment variables `SERVERURL`, `SERVERPORT`, `PEERS` and `PEERDNS`, and the container will generate all necessary confs for both the server and the clients. The client config qr codes will be output in the docker log. They will also be saved in text and png format under `/config/peerX`.

If there is an existing `/config/wg0.conf`, the above environment variables won't have any affect. To add more peers/clients later on, you can run `docker exec -it wireguard /app/add-peer` while the container is running.

To recreate all serer and client confs, set the above env vars, delete `/config/wg0.conf` and restart the container. Client confs will be recreated with existing private/public keys. Delete the peer folders for the keys to be recreated along with the confs.

## Client Mode
Drop your client conf into the config folder as `/config/wg0.conf` and start the container. 



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it wireguard /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f wireguard`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' wireguard`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/wireguard`

## Versions

* **31.03.20:** - Initial Release.
