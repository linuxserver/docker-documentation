# [linuxserver/transmission](https://github.com/linuxserver/docker-transmission)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-transmission.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-transmission)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-transmission.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-transmission/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-transmission/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-transmission/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/transmission)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/transmission.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/transmission "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/transmission.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/transmission)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/transmission.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/transmission)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-transmission/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-transmission/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/transmission/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/transmission/latest/index.html)

[Transmission](https://www.transmissionbt.com/) is designed for easy, powerful use. Transmission has the features you want from a BitTorrent client: encryption, a web interface, peer exchange, magnet links, DHT, µTP, UPnP and NAT-PMP port forwarding, webseed support, watch directories, tracker editing, global and per-torrent speed limits, and more.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/transmission` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=transmission \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e TRANSMISSION_WEB_HOME=/combustion-release/ `#optional` \
  -e USER=username `#optional` \
  -e PASS=password `#optional` \
  -p 9091:9091 \
  -p 51413:51413 \
  -p 51413:51413/udp \
  -v <path to data>:/config \
  -v <path to downloads>:/downloads \
  -v <path to watch folder>:/watch \
  --restart unless-stopped \
  linuxserver/transmission
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  transmission:
    image: linuxserver/transmission
    container_name: transmission
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - TRANSMISSION_WEB_HOME=/combustion-release/ #optional
      - USER=username #optional
      - PASS=password #optional
    volumes:
      - <path to data>:/config
      - <path to downloads>:/downloads
      - <path to watch folder>:/watch
    ports:
      - 9091:9091
      - 51413:51413
      - 51413:51413/udp
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `9091` | WebUI |
| `51413` | Torrent Port TCP |
| `51413/udp` | Torrent Port UDP |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `TRANSMISSION_WEB_HOME=/combustion-release/` | Specify an alternative UI options are `/combustion-release/`, `/transmission-web-control/`, and `/kettu/` . |
| `USER=username` | Specify an optional username for the interface |
| `PASS=password` | Specify an optional password for the interface |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Where transmission should store config files and logs. |
| `/downloads` | Local path for downloads. |
| `/watch` | Watch folder for torrent files. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Webui is on port 9091, the settings.json file in /config has extra settings not available in the webui. Stop the container before editing it or any changes won't be saved.

For users pulling an update and unable to access the webui setting you may need to set "rpc-host-whitelist-enabled": false, in /config/settings.json`

If you choose to use transmission-web-control as your default UI, just note that the origional Web UI will not be available to you despite the button being present.

## Securing the webui with a username/password.

this requires 3 settings to be changed in the settings.json file.

`Make sure the container is stopped before editing these settings.`

`"rpc-authentication-required": true,` - check this, the default is false, change to true.

`"rpc-username": "transmission",` substitute transmission for your chosen user name, this is just an example.

`rpc-password` will be a hash starting with {, replace everything including the { with your chosen password, keeping the quotes.

Transmission will convert it to a hash when you restart the container after making the above edits.

## Updating Blocklists Automatically

This requires `"blocklist-enabled": true,` to be set. By setting this to true, it is assumed you have also populated `blocklist-url` with a valid block list.

The automatic update is a shell script that downloads a blocklist from the url stored in the settings.json, gunzips it, and restarts the transmission daemon.

The automatic update will run once a day at 3am local server time.



## Support Info

* Shell access whilst the container is running:
  * `docker exec -it transmission /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f transmission`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' transmission`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/transmission`

## Versions

* **04.10.19:** - Update package label.
* **21.08.19:** - Add optional user/pass environment variables, fix transmission shut down if user/pass are set.
* **19.07.19:** - Send SIGTERM in blocklist update to properly close pid.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebase to Alpine 3.9, add themes to baseimage, add python and findutils.
* **22.02.19:** - Catch term and clean exit.
* **07.02.19:** - Add pipeline logic and multi arch.
* **15.08.18:** - Rebase to alpine linux 3.8.
* **12.02.18:** - Pull transmission from edge repo.
* **10.01.18:** - Rebase to alpine linux 3.7.
* **25.07.17:** - Add rsync package.
* **27.05.17:** - Rebase to alpine linux 3.6.
* **06.02.17:** - Rebase to alpine linux 3.5.
* **15.01.17:** - Add p7zip, tar , unrar and unzip packages.
* **16.10.16:** - Blocklist autoupdate with optional authentication.
* **14.10.16:** - Add version layer informationE.
* **23.09.16:** - Add information about securing the webui to README.
* **21.09.16:** - Add curl package.
* **09.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README.
* **09.08.16:** - Rebase to alpine linux.
* **06.12.15:** - Separate mapping for watch folder.
* **16.11.15:** - Initial Release.
