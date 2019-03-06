# [linuxserver/ldap-auth](https://github.com/linuxserver/docker-ldap-auth)

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn)
[![](https://images.microbadger.com/badges/version/linuxserver/ldap-auth.svg)](https://microbadger.com/images/linuxserver/ldap-auth "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/linuxserver/ldap-auth.svg)](https://microbadger.com/images/linuxserver/ldap-auth "Get your own version badge on microbadger.com")
![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/ldap-auth.svg)
![Docker Stars](https://img.shields.io/docker/stars/linuxserver/ldap-auth.svg)
[![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-ldap-auth/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-ldap-auth/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ldap-auth/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ldap-auth/latest/index.html)

[Ldap-auth](https://github.com/nginxinc/nginx-ldap-auth) software is for authenticating users who request protected resources from servers proxied by nginx. It includes a daemon (ldap-auth) that communicates with an authentication server, and a webserver daemon that generates an authentication cookie based on the user’s credentials. The daemons are written in Python for use with a Lightweight Directory Access Protocol (LDAP) authentication server (OpenLDAP or Microsoft Windows Active Directory 2003 and 2012).

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/). 

Simply pulling `linuxserver/ldap-auth` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=ldap-auth \
  -e TZ=Europe/London \
  -p 8888:8888 \
  -p 9000:9000 \
  --restart unless-stopped \
  linuxserver/ldap-auth
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  ldap-auth:
    image: linuxserver/ldap-auth
    container_name: ldap-auth
    environment:
      - TZ=Europe/London
    ports:
      - 8888:8888
      - 9000:9000
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8888` | the port for ldap auth daemon |
| `9000` | the port for ldap login page |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |



## Application Setup

- This container itself does not have any settings and it relies on the pertinent information passed through in http headers of incoming requests. Make sure that your webserver is set up with the right config.
- Here's a sample config: [nginx-ldap-auth.conf](https://github.com/nginxinc/nginx-ldap-auth/blob/master/nginx-ldap-auth.conf).



## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it ldap-auth /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f ldap-auth`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ldap-auth`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/ldap-auth`

## Versions

* **22.02.19:** - Rebasing to alpine 3.9.
* **18.09.18:** - Update pip
* **14.09.18:** - Add TZ parameter, remove unnecessary PUID/PGID params
* **11.08.18:** - Initial release.
