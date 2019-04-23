# [linuxserver/kanzi](https://github.com/linuxserver/docker-kanzi)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/kanzi.svg)](https://microbadger.com/images/linuxserver/kanzi "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/kanzi.svg)](https://microbadger.com/images/linuxserver/kanzi "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/kanzi.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/kanzi.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-kanzi/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-kanzi/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/kanzi/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/kanzi/latest/index.html)

[Kanzi](https://lexigr.am/), formerly titled Kodi-Alexa, this custom skill is the ultimate voice remote control for navigating Kodi. It can do anything you can think of (100+ intents).  This container also contains lexigram-cli to setup Kanzi with an Amazon Developer Account and automatically deploy it to Amazon.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/kanzi` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=kanzi \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e INVOCATION_NAME=kanzi \
  -e URL_ENDPOINT=https://server.com/kanzi/ \
  -p 8000:8000 \
  -v </path/to/appdata/config>:/config \
  --restart unless-stopped \
  linuxserver/kanzi
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  kanzi:
    image: linuxserver/kanzi
    container_name: kanzi
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - INVOCATION_NAME=kanzi
      - URL_ENDPOINT=https://server.com/kanzi/
    volumes:
      - </path/to/appdata/config>:/config
    ports:
      - 8000:8000
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8000` | Application Port |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `INVOCATION_NAME=kanzi` | Specify an invocation name for this skill, use either kanzi or kod. |
| `URL_ENDPOINT=https://server.com/kanzi/` | Specify the URL at which the webserver is reachable either `https://kanzi.server.com/` or `https://server.com/kanzi/` Note the trailing slash **MUST** be included. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Configuration files. |



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

### Initial setup
* Once you start the container for the first time, you need to perform some steps before use.
 1.  Create an Amazon Developer Account [here.](https://developer.amazon.com/)
 2.  Open a terminal in the `/config` directory of the docker container `docker exec -itw /config kanzi bash`
 3.  Enter `lexigram login --no-browser true` to setup your AWS credentials and copy the URL into a browser, login to your Amazon Developer Account and copy/paste the resulting authorisation code back into the terminal and press enter.
 4.  Edit the file `kodi.config` according to your local setup and this will be used by the included gunicorn server to respond to requests.  
 5.  Restart the container to automatically deploy the Kanzi skill.
 6.  Reverse proxy this container with our [LetsEncrypt container](https://hub.docker.com/r/linuxserver/letsencrypt/) which contains preconfigured templates for reverse proxying the Kanzi container on either a subdomain or subfolder utilising Docker custom networking.  Alternatively, if you already have an Nginx reverse proxy set up, you can use one of these location blocks to reverse proxy Kanzi to a subfolder or subdomain respectively.
 
 Subfolder
 ```
 location /kanzi {
   rewrite           ^/kanzi/(.*)  /$1  break;
   proxy_pass         https://$IP-ADDRESS:8000;
   proxy_redirect     https://$IP-ADDRESS:8000 /kanzi;
   proxy_set_header   Host $host;
   proxy_set_header   X-Real-IP $remote_addr;
   proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
   proxy_set_header   X-Forwarded-Server $host;
   proxy_set_header   X-Forwarded-Host $server_name;
 }
 ```
 Subdomain
 ```
   location / {
   proxy_pass         https://$IP-ADDRESS:8000;
   proxy_set_header   Host $host;
   proxy_set_header   X-Real-IP $remote_addr;
   proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
   proxy_set_header   X-Forwarded-Server $host;
   proxy_set_header   X-Forwarded-Host $server_name;
 }
 ```



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it kanzi /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f kanzi`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' kanzi`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/kanzi`

## Versions

* **13.04.19:** - Initial Release.
