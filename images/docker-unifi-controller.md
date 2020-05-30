# [linuxserver/unifi-controller](https://github.com/linuxserver/docker-unifi-controller)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-unifi-controller.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-unifi-controller)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-unifi-controller.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-unifi-controller/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-unifi-controller/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-unifi-controller/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/unifi-controller.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/unifi-controller "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/unifi-controller.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/unifi-controller)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/unifi-controller.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/unifi-controller)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-unifi-controller%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-unifi-controller/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flspipepr%2Funifi-controller%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/unifi-controller/latest/index.html)

The [Unifi-controller](https://www.ubnt.com/enterprise/#unifi) Controller software is a powerful, enterprise wireless software engine ideal for high-density client deployments requiring low latency and high uptime performance.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/unifi-controller` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=unifi-controller \
  -e PUID=1000 \
  -e PGID=1000 \
  -e MEM_LIMIT=1024M `#optional` \
  -p 3478:3478/udp \
  -p 10001:10001/udp \
  -p 8080:8080 \
  -p 8081:8081 \
  -p 8443:8443 \
  -p 8843:8843 \
  -p 8880:8880 \
  -p 6789:6789 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/unifi-controller
```

### Version Tags

This image provides various versions that are available via tags. `latest` tag provides the latest stable build from Unifi, but if this is a permanent setup you might consider using the LTS tag.

| Tag    | Description                                  |
| :----: | -------------------------------------------- |
| latest | releases from the latest stable branch.      |
| LTS    | releases from the 5.6.x "LTS Stable" branch. |
| 5.9    | releases from the now EOL 5.9.x branch.      |
| 5.8    | releases from the now EOL 5.8.x branch.      |
| 5.7    | releases from the now EOL 5.7.x branch.      |

## Common problems
When using a Security Gateway (router) it could be that network connected devices are unable to obtain an ip address. This can be fixed by setting "DHCP Gateway IP", under Settings > Networks > network_name, to a correct (and accessable) ip address.


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  unifi-controller:
    image: linuxserver/unifi-controller
    container_name: unifi-controller
    environment:
      - PUID=1000
      - PGID=1000
      - MEM_LIMIT=1024M #optional
    volumes:
      - <path to data>:/config
    ports:
      - 3478:3478/udp
      - 10001:10001/udp
      - 8080:8080
      - 8081:8081
      - 8443:8443
      - 8843:8843
      - 8880:8880
      - 6789:6789
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3478/udp` | Unifi communication port |
| `10001/udp` | required for AP discovery |
| `8080` | required for Unifi to function |
| `8081` | Unifi communication port |
| `8443` | Unifi communication port |
| `8843` | Unifi communication port |
| `8880` | Unifi communication port |
| `6789` | For throughput test |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `MEM_LIMIT=1024M` | Optionally change the Java memory limit (-Xmx) (default is 1024M). |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | All Unifi data stored here |



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

The webui is at https://ip:8443, setup with the first run wizard.

For Unifi to adopt other devices, e.g. an Access Point, it is required to change the inform ip address. Because Unifi runs inside Docker by default it uses an ip address not accessable by other devices. To change this go to Settings > Controller > Controller Settings and set the Controller Hostname/IP to an ip address accessable by other devices.

Alternatively to manually adopt a device take these steps:

```
ssh ubnt@$AP-IP
mca-cli
set-inform http://$address:8080/inform
```

Use `ubnt` as the password to login and `$address` is the IP address of the host you are running this container on and `$AP-IP` is the Access Point IP address.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27unifi-controller%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=unifi-controller "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it unifi-controller /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f unifi-controller`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' unifi-controller`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/unifi-controller`

## Versions

* **14.11.19:** - Changed url for deb package to match new Ubiquity domain.
* **29.07.19:** - Allow for changing Java mem limit via new optional environment variable.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **10.02.19:** - Initial release of new unifi-controller image with new tags and pipeline logic
