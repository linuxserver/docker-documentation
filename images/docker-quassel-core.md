# [linuxserver/quassel-core](https://github.com/linuxserver/docker-quassel-core)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/quassel-core.svg)](https://microbadger.com/images/linuxserver/quassel-core "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/quassel-core.svg)](https://microbadger.com/images/linuxserver/quassel-core "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/quassel-core.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/quassel-core.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-quassel-core/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-quassel-core/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/quassel-core/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/quassel-core/latest/index.html)

[Quassel-core](http://quassel-irc.org/) is a modern, cross-platform, distributed IRC client, meaning that one (or multiple) client(s) can attach to and detach from a central core.

This container handles the IRC connection (quasselcore) and requires a desktop client (quasselclient) to be used and configured. It is designed to be always on and will keep your identity present in IRC even when your clients cannot be online. Backlog (history) is downloaded by your client upon reconnection allowing infinite scrollback through time.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/quassel-core` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=quassel-core \
  -e PUID=1001 \
  -e PGID=1001 \
  -e TZ=Europe/London \
  -p 4242:4242 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/quassel-core
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  quassel-core:
    image: linuxserver/quassel-core
    container_name: quassel-core
    environment:
      - PUID=1001
      - PGID=1001
      - TZ=Europe/London
    volumes:
      - <path to data>:/config
    ports:
      - 4242:4242
    mem_limit: 4096m
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `4242` | The port quassel-core listens for connections on. |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1001` | for UserID - see below for explanation |
| `PGID=1001` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Database and quassel-core configuration storage. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1001` and `PGID=1001`, to find yours use `id user` as below:

```
  $ id username
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Application Setup

Quassel wiki: [quassel](http://bugs.quassel-irc.org/projects/quassel-irc/wiki)

A great place to host a quassel instance is a VPS, such as [DigitalOcean](https://www.digitalocean.com/?refcode=501c48b34b8c). For $5 a month you can have a 24/7 IRC connection and be up and running in under 55 seconds (or so they claim).

Once you have the container running, fire up a quassel desktop client and connect to your new core instance using your droplets public IP address and the port you specified in your `docker run` command *default: 4242*. Create an admin user, select SQLite as your storage backend (Quassel limitation). Setup your real name and nick, then press `Save & Connect`.

You're now connected to IRC. Let's add you to our [IRC](http://www.linuxserver.io/index.php/irc/) `#linuxserver.io` room on Freenode. Click 'File' > 'Networks' > 'Configure Networks' > 'Add' (under Networks section, not Servers) > 'Use preset' > Select 'Freenode' and then configure your identity using the tabs in the 'Network details' section. Once connected to Freenode, click `#join` and enter `#linuxserver.io`. That's it, you're done.



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it quassel-core /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f quassel-core`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' quassel-core`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/quassel-core`

## Versions

* **26.01.19:** - Add pipeline logic and multi arch.
* **08.01.19:** - Rebase to Ubuntu Bionic and upgrade to Quassel`0.13.0` See [here.](https://quassel-irc.org/node/134).
* **30.07.18:** - Rebase to alpine:3.8 and use buildstage.
* **03.01.18:** - Deprecate cpu_core routine lack of scaling.
* **09.12.17:** - Rebase to alpine:3.7.
* **26.11.17:** - Use cpu core counting routine to speed up build time.
* **12.07.17:** - Add inspect commands to README, move to jenkins build and push.
* **27.05.17:** - Rebase to alpine:3.6.
* **13.05.17:** - Switch to git source.
* **28.12.16:** - Rebase to alpine:3.5.
* **23.11.16:** - Rebase to alpine:edge.
* **23.09.16:** - Use QT5 dependencies (thanks bauerj).
* **10.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README.
* **10.08.16:** - Rebase to xenial.
* **14.10.15:** - Removed the webui, turned out to be to unstable for most usecases.
* **01.09.15:** - Fixed mistake in README.
* **30.07.15:** - Switched to internal baseimage, and fixed a bug with updating the webinterface.
* **06.07.15:** - Enabled BLOWFISH encryption and added a (optional) webinterface, for the times you dont have access to your client.
