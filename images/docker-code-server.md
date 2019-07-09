# [linuxserver/code-server](https://github.com/linuxserver/docker-code-server)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/code-server.svg)](https://microbadger.com/images/linuxserver/code-server "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/code-server.svg)](https://microbadger.com/images/linuxserver/code-server "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/code-server.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/code-server.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-code-server/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-code-server/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/code-server/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/code-server/latest/index.html)

[Code-server](https://coder.com) is VS Code running on a remote server, accessible through the browser.
- Code on your Chromebook, tablet, and laptop with a consistent dev environment.
- If you have a Windows or Mac workstation, more easily develop for Linux.
- Take advantage of large cloud servers to speed up tests, compilations, downloads, and more.
- Preserve battery life when you're on the go.
- All intensive computation runs on your server.
- You're no longer running excess instances of Chrome.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/code-server` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```
docker create \
  --name=code-server \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e PASSWORD=password `#optional` \
  -e SUDO_PASSWORD=password `#optional` \
  -p 8443:8443 \
  -v /path/to/appdata/config:/config \
  --restart unless-stopped \
  linuxserver/code-server
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  code-server:
    image: linuxserver/code-server
    container_name: code-server
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - PASSWORD=password #optional
      - SUDO_PASSWORD=password #optional
    volumes:
      - /path/to/appdata/config:/config
    ports:
      - 8443:8443
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8443` | web gui |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `PASSWORD=password` | Optional web gui password, if not provided, there will be no auth. |
| `SUDO_PASSWORD=password` | If this optional variable is set, user will have sudo access in the code-server terminal with the specified password. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains all relevant configuration files. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `http://<your-ip>:8443`.  
For github integration, drop your ssh key in to `/config/.ssh`.  
Then open a terminal from the top menu and set your github username and email via the following commands  
```
git config --global user.name "username"
git config --global user.email "email address"
```



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it code-server /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f code-server`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' code-server`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/code-server`

## Versions

* **09.07.19:** - Add optional sudo access.
* **01.07.19:** - Add nano.
* **24.06.19:** - Initial Release.
