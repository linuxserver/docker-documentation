# [linuxserver/ldap-auth](https://github.com/linuxserver/docker-ldap-auth)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-ldap-auth.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-ldap-auth)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-ldap-auth.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-ldap-auth/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-ldap-auth/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-ldap-auth/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/ldap-auth.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/ldap-auth "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/ldap-auth.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/ldap-auth)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/ldap-auth.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/ldap-auth)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-ldap-auth%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-ldap-auth/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fldap-auth%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/ldap-auth/latest/index.html)

[Ldap-auth](https://github.com/nginxinc/nginx-ldap-auth) software is for authenticating users who request protected resources from servers proxied by nginx. It includes a daemon (ldap-auth) that communicates with an authentication server, and a webserver daemon that generates an authentication cookie based on the user’s credentials. The daemons are written in Python for use with a Lightweight Directory Access Protocol (LDAP) authentication server (OpenLDAP or Microsoft Windows Active Directory 2003 and 2012).

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/ldap-auth` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=ldap-auth \
  -e TZ=Europe/London \
  -e FERNETKEY= `#optional` \
  -e CERTFILE= `#optional` \
  -e KEYFILE= `#optional` \
  -p 8888:8888 \
  -p 9000:9000 \
  --restart unless-stopped \
  linuxserver/ldap-auth
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  ldap-auth:
    image: linuxserver/ldap-auth
    container_name: ldap-auth
    environment:
      - TZ=Europe/London
      - FERNETKEY= #optional
      - CERTFILE= #optional
      - KEYFILE= #optional
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
| `FERNETKEY=` | Optionally define a custom fernet key, has to be base64-encoded 32-byte (only needed if container is frequently recreated, or if using multi-node setups, invalidating previous authentications) |
| `CERTFILE=` | Point this to a certificate file to enable HTTP over SSL (HTTPS) for the ldap auth daemon |
| `KEYFILE=` | Point this to the private key file, matching the certificate file referred to in CERTFILE |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |



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


## Application Setup

- This container itself does not have any settings and it relies on the pertinent information passed through in http headers of incoming requests. Make sure that your webserver is set up with the right config.
- Here's a sample config: [nginx-ldap-auth.conf](https://github.com/nginxinc/nginx-ldap-auth/blob/master/nginx-ldap-auth.conf).
- Unlike the upstream project, this image encodes the cookie information with fernet, using a randomly generated key during container creation (or optionally user defined).
- Also unlike the upstream project, this image serves the login page at `/ldaplogin` (as well as `/login`) to prevent clashes with reverse proxied apps that may also use `/login` for their internal auth.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27ldap-auth%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=ldap-auth "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


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

* **08.09.20:** - Set form action correctly.
* **30.07.20:** - Fix bug related to unset optional `CERTFILE` and `KEYFILE` vars.
* **27.07.20:** - Add support for HTTP over SSL (HTTPS).
* **21.07.20:** - Add support for optional user defined fernet key.
* **02.06.20:** - Rebasing to alpine 3.12, serve login page at `/ldaplogin` as well as `/login`, to prevent clashes with reverese proxied apps.
* **17.05.20:** - Add support for self-signed CA certs.
* **20.02.20:** - Switch to python3.
* **19.12.19:** - Rebasing to alpine 3.11.
* **01.07.19:** - Fall back to base64 encoding when basic http auth is used.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **18.09.18:** - Update pip
* **14.09.18:** - Add TZ parameter, remove unnecessary PUID/PGID params
* **11.08.18:** - Initial release.
