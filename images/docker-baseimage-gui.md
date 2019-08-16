[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[appurl]: https://cloud-images.ubuntu.com
[dockerfileurl]: https://github.com/linuxserver/docker-baseimage-gui/blob/master/Dockerfile



[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png?v=4&s=4000)][linuxserverurl]


## Contact information:

| Type | Address/Details |
| :---: | --- |
| Discord | [Discord](https://discord.gg/YWrKVTn) |
| IRC | freenode at `#linuxserver.io` more information at:- [IRC][ircurl]
| Forum | [LinuxServer.io forum][forumurl] |

&nbsp;

# [linuxserver/docker-baseimage-gui](https://github.com/linuxserver/docker-baseimage-gui)
[![](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/Dockerfile-Bionic-green.png)](https://github.com/linuxserver/docker-baseimage-gui/blob/master/Dockerfile)

A custom graphical base image built with:
  * [Ubuntu cloud image][appurl]
  * [S6 overlay](https://github.com/just-containers/s6-overlay)
  * [xrdp](https://github.com/neutrinolabs/xrdp)
  * [xorgxrdp](https://github.com/neutrinolabs/xorgxrdp)
  * [openbox](http://openbox.org/wiki/Main_Page)

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lsiobase/nginx` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Usage

Here is an example to help you get started creating a graphical container.

### Dockerfile
```
#Firefox via RDP
FROM lsiobase/ubuntu-gui:amd64-latest

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################
# Set correct environment variables
ENV TERM="xterm" APPNAME="firefox"
ARG DEBIAN_FRONTEND=noninteractive

#########################################
##         INSTALL DEPENDENCIES        ##
#########################################
RUN apt-get update \
&& apt-get -y upgrade \
&& apt-get install -qy --no-install-recommends \
   firefox \
&& apt-get clean -y \
&& apt-get autoremove -y \
&& rm -rf /tmp/* /var/tmp/* \
&& rm -rf /var/lib/apt/lists/*

COPY root /
```

### servicefile
```
#!/bin/execlineb -P
# ./root/etc/service.d/firefox/run

# Redirect stderr to stdout.
fdmove -c 2 1

# Wait until openbox is running
if { s6-svwait -t 10000 -U /var/run/s6/services/openbox/ }

# Drop privileges and set env
s6-setuidgid abc
s6-env DISPLAY=:1 HOME=/config

# Execute Firefox
/usr/bin/firefox
```

## Access the Graphical Interface

Use an RDP client such as:
  * Remmina
  * Microsoft Remote Deskotp Client

The following line is only in this repo for loop testing:
- { date: "01.01.50:", desc: "I am the release message for this internal repo." }
