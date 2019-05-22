[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[appurl]: https://cloud-images.ubuntu.com
[dockerfileurl]: https://github.com/linuxserver/docker-baseimage-guacgui/blob/master/Dockerfile


[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png?v=4&s=4000)][linuxserverurl]


## Contact information:

| Type | Address/Details |
| :---: | --- |
| Discord | [Discord](https://discord.gg/YWrKVTn) |
| IRC | freenode at `#linuxserver.io` more information at:- [IRC][ircurl]
| Forum | [Linuserver.io forum][forumurl] |

&nbsp;

# [linuxserver/docker-baseimage-guacgui](https://github.com/linuxserver/docker-baseimage-guacgui)
[![](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/Dockerfile-Bionic-green.png)](https://github.com/linuxserver/docker-baseimage-gui/blob/master/Dockerfile)

A custom graphical base image built with:
  * [Ubuntu cloud image][appurl]
  * [S6 overlay](https://github.com/just-containers/s6-overlay)
  * [xrdp](https://github.com/neutrinolabs/xrdp)
  * [xorgxrdp](https://github.com/neutrinolabs/xorgxrdp)
  * [openbox](http://openbox.org/wiki/Main_Page)
  * [guacamole](https://guacamole.apache.org/)
## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/docker-baseimage-guacgui` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container.

### docker

```
docker create \
  --name=docker-baseimage-guacgui \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e APPNAME=xclock \
  -e GUAC_USER=abc \
  -e GUAC_PASS=900150983cd24fb0d6963f7d28e17f72 \
  -p 8080:8080 \
  -p 3389:3389 \
  -v </path/to/appdata>:/config \
  --restart unless-stopped \
  linuxserver/docker-baseimage-guacgui
```


### docker-compose

Compatible with docker-compose v2 schemas.

```
---
version: "2"
services:
  docker-baseimage-guacgui:
    image: linuxserver/docker-baseimage-guacgui
    container_name: docker-baseimage-guacgui
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - APPNAME=xclock
      - GUAC_USER=abc
      - GUAC_PASS=900150983cd24fb0d6963f7d28e17f72
    volumes:
      - </path/to/appdata>:/config
    ports:
      - 8080:8080
      - 3389:3389
    restart: unless-stopped
```

## Parameters

Container images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

| Parameter | Function |
| :----: | --- |
| `-p 8080` | Allows HTTP access to the internal X server. |
| `-p 3389` | Allows RDP access to the internal X server. |
| `-e PUID=1000` | for UserID - see below for explanation |
| `-e PGID=1000` | for GroupID - see below for explanation |
| `-e TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `-e APPNAME=xclock` | Specify the graphical application name shown on RDP access. |
| `-e GUAC_USER=abc` | Specify the username for guacamole's web interface. |
| `-e GUAC_PASS=900150983cd24fb0d6963f7d28e17f72` | Specify the password's md5 hash for guacamole's web interface. |
| `-v /config` | Contains X user's home directory contents. |

&nbsp;
## Application Setup

This is baseimage meant to be used as base for graphical applications. Please
refer to the example folder for usage.
&nbsp;
Passwords can be generate via the following:
```
echo -n password | openssl md5
```
```
printf '%s' password | md5sum
```
Please beware this image is not hardened for internet usage. Use
a reverse ssl proxy to increase security.

The following line is only in this repo for loop testing:
  - { date: "01.01.50:", desc: "I am the release message for this internal repo." }
