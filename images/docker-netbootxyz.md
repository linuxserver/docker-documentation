# [linuxserver/netbootxyz](https://github.com/linuxserver/docker-netbootxyz)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-netbootxyz.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-netbootxyz)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-netbootxyz.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-netbootxyz/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-netbootxyz/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-netbootxyz/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/netbootxyz.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/netbootxyz "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/netbootxyz.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/netbootxyz)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/netbootxyz.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/netbootxyz)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-netbootxyz%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-netbootxyz/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fnetbootxyz%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/netbootxyz/latest/index.html)

[Netbootxyz](https://netboot.xyz) is a way to PXE boot various operating system installers or utilities from one place within the BIOS without the need of having to go retrieve the media to run the tool. iPXE is used to provide a user friendly menu from within the BIOS that lets you easily choose the operating system you want along with any specific types of versions or bootable flags.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/netbootxyz` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :----: | --- |
| latest | Web application for full self hosting |
| tftp | TFTP server only with NETBOOT.XYZ boot files |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=netbootxyz \
  -e PUID=1000 \
  -e PGID=1000 \
  -e MENU_VERSION=1.9.9 `#optional` \
  -p 3000:3000 \
  -p 69:69/udp \
  -p 8080:80 `#optional` \
  -v /path/to/config:/config \
  -v /path/to/assets:/assets `#optional` \
  --restart unless-stopped \
  linuxserver/netbootxyz
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  netbootxyz:
    image: linuxserver/netbootxyz
    container_name: netbootxyz
    environment:
      - PUID=1000
      - PGID=1000
      - MENU_VERSION=1.9.9 #optional
    volumes:
      - /path/to/config:/config
    volumes:
      - /path/to/assets:/assets #optional
    ports:
      - 3000:3000
      - 69:69/udp
    ports:
      - 8080:80 #optional
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `3000` | Web configuration interface. |
| `69/udp` | TFTP Port. |
| `80` | NGINX server for hosting assets. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `MENU_VERSION=1.9.9` | Specify a specific version of boot files you want to use from NETBOOT.XYZ (unset pulls latest) |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Storage for boot menu files and web application config |
| `/assets` | Storage for NETBOOT.XYZ bootable assets (live CDs and other files) |



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

To use this image you need an existing DHCP server where you can set this TFTP server as your DHCP boot destination. This image does not contain a DHCP server nor do we aim to support one in the future. This is simply a TFTP server hosting the latest IPXE kernel builds from [netboot.xyz](https://netboot.xyz). If you are interested in their project and lack the ability to setup a DHCP server to boot this payload they also have USB stick images you can use available on their [downloads page](https://netboot.xyz/downloads/).

### Router Setup Examples

#### PFSense
Services -> DHCP Server

Set both the option for "TFTP Server" and the options under the Advanced "Network Booting" section. 
* check enable
* Next server- IP used for TFTP Server
* Default BIOS file name- `netboot.xyz.kpxe`
* UEFI 32 bit file name- `netboot.xyz.efi`
* UEFI 64 bit file name- `netboot.xyz.efi`

#### OPNsense
Services -> DHCP Server

Under the Advanced "Network Booting" section. 
* check enable
* Next server- IP of docker host
* Default BIOS file name- `netboot.xyz.kpxe`
* UEFI 32 bit file name- `netboot.xyz.efi`
* UEFI 64 bit file name- `netboot.xyz.efi`

#### Unifi Security Gateway (with the controller)
Networks -> LAN (or the network you want to boot from) -> ADVANCED DHCP OPTIONS
* tick Enable network boot
* Server-  YOURSERVERIP
* Filename- `netboot.xyz.kpxe`

#### DD-WRT
Administration -> Services -> Additional DNSMasq Options
Set the following lines: 
```
dhcp-match=set:bios,60,PXEClient:Arch:00000
dhcp-boot=tag:bios,netboot.xyz.kpxe,,YOURSERVERIP
dhcp-match=set:efi32,60,PXEClient:Arch:00002
dhcp-boot=tag:efi32,netboot.xyz.efi,,YOURSERVERIP
dhcp-match=set:efi32-1,60,PXEClient:Arch:00006
dhcp-boot=tag:efi32-1,netboot.xyz.efi,,YOURSERVERIP
dhcp-match=set:efi64,60,PXEClient:Arch:00007
dhcp-boot=tag:efi64,netboot.xyz.efi,,YOURSERVERIP
dhcp-match=set:efi64-1,60,PXEClient:Arch:00008
dhcp-boot=tag:efi64-1,netboot.xyz.efi,,YOURSERVERIP
dhcp-match=set:efi64-2,60,PXEClient:Arch:00009
dhcp-boot=tag:efi64-2,netboot.xyz.efi,,YOURSERVERIP
```

#### Tomato
Advanced -> DHCP/DNS -> Dnsmasq Custom configuration
Set the following lines: 
```
dhcp-match=set:bios,60,PXEClient:Arch:00000
dhcp-boot=tag:bios,netboot.xyz.kpxe,,YOURSERVERIP
dhcp-match=set:efi32,60,PXEClient:Arch:00002
dhcp-boot=tag:efi32,netboot.xyz.efi,,YOURSERVERIP
dhcp-match=set:efi32-1,60,PXEClient:Arch:00006
dhcp-boot=tag:efi32-1,netboot.xyz.efi,,YOURSERVERIP
dhcp-match=set:efi64,60,PXEClient:Arch:00007
dhcp-boot=tag:efi64,netboot.xyz.efi,,YOURSERVERIP
dhcp-match=set:efi64-1,60,PXEClient:Arch:00008
dhcp-boot=tag:efi64-1,netboot.xyz.efi,,YOURSERVERIP
dhcp-match=set:efi64-2,60,PXEClient:Arch:00009
dhcp-boot=tag:efi64-2,netboot.xyz.efi,,YOURSERVERIP
```

#### OpenWRT
```
uci set dhcp.@dnsmasq[0].dhcp_match=set:bios,60,PXEClient:Arch:00000
uci set dhcp.@dnsmasq[0].dhcp_boot=tag:bios,netboot.xyz.kpxe,,YOURSERVERIP
uci set dhcp.@dnsmasq[0].dhcp_match=set:efi32,60,PXEClient:Arch:00002
uci set dhcp.@dnsmasq[0].dhcp_boot=tag:efi32,netboot.xyz.efi,,YOURSERVERIP
uci set dhcp.@dnsmasq[0].dhcp_match=set:efi32-1,60,PXEClient:Arch:00006
uci set dhcp.@dnsmasq[0].dhcp_boot=tag:efi32-1,netboot.xyz.efi,,YOURSERVERIP
uci set dhcp.@dnsmasq[0].dhcp_match=set:efi64,60,PXEClient:Arch:00007
uci set dhcp.@dnsmasq[0].dhcp_boot=tag:efi64,netboot.xyz.efi,,YOURSERVERIP
uci set dhcp.@dnsmasq[0].dhcp_match=set:efi64-1,60,PXEClient:Arch:00008
uci set dhcp.@dnsmasq[0].dhcp_boot=tag:efi64-1,netboot.xyz.efi,,YOURSERVERIP
uci set dhcp.@dnsmasq[0].dhcp_match=set:efi64-2,60,PXEClient:Arch:00009
uci set dhcp.@dnsmasq[0].dhcp_boot=tag:efi64-2,netboot.xyz.efi,,YOURSERVERIP
uci commit
/etc/init.d/dnsmasq restart
```
#### Microsoft Server DHCP

* Run the DHCP program
* Under Scope/Scope Options
* check option 066 and enter the FQDN or IP of your TFTP boot server
* check option 067 and enter one of the following bootfile names:
   * Default BIOS file name- netboot.xyz.kpxe
   * UEFI 32 bit file name- netboot.xyz.efi
   * UEFI 64 bit file name- netboot.xyz.efi

Anything else from a router standpoint is a crapshoot for supporting Dnsmasq options or proprietary PXE boot options, check Google for support (try your exact router model number with 'pxe boot') or look into setting up your own DHCP server in Linux.

This image also contains `netboot.xyz.efi` which can be used to boot using UEFI network boot. The UEFI boot and menu will have limited functionality if you choose to use it. 


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27netbootxyz%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=netbootxyz "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it netbootxyz /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f netbootxyz`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' netbootxyz`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/netbootxyz`

## Versions

* **01.06.20:** - Rebasing to alpine 3.12.
* **19.12.19:** - Rebasing to alpine 3.11.
* **13.12.19:** - Swapping latest tag over to webapp stack for management.
* **10.12.19:** - Adding tftp branch to provide tftp only option to latest users.
* **22.10.19:** - Initial release.
