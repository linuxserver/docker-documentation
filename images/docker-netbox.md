---
title: netbox
---
# [linuxserver/netbox](https://github.com/linuxserver/docker-netbox)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-netbox.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-netbox)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-netbox.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-netbox/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-netbox/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-netbox/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/netbox.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/netbox "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/netbox.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/netbox)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/netbox.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/netbox)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-netbox%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-netbox/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fnetbox%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/netbox/latest/index.html)

[Netbox](https://github.com/netbox-community/netbox) is an IP address management (IPAM) and data center infrastructure management (DCIM) tool. Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically to address the needs of network and infrastructure engineers. It is intended to function as a domain-specific source of truth for network operations.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `ghcr.io/linuxserver/netbox` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker-compose ([recommended](https://docs.linuxserver.io/general/docker-compose))

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  netbox:
    image: ghcr.io/linuxserver/netbox
    container_name: netbox
    environment:
      - PUID=1000
      - PGID=1000
      - SUPERUSER_EMAIL=<SUPERUSER_EMAIL>
      - SUPERUSER_PASSWORD=<SUPERUSER_PASSWORD>
      - ALLOWED_HOST=<ALLOWED_HOST>
      - BASE_PATH=<BASE_PATH>
      - DB_NAME=<DB_NAME>
      - DB_USER=<DB_USER>
      - DB_PASSWORD=<DB_PASSWORD>
      - DB_HOST=<DB_HOST>
      - DB_PORT=<DB_PORT>
      - REDIS_HOST=<REDIS_HOST>
      - REDIS_PORT=<REDIS_PORT>
      - REDIS_PASSWORD=<REDIS_PASSWORD>
      - REMOTE_AUTH_ENABLED=<REMOTE_AUTH_ENABLED>
      - REMOTE_AUTH_BACKEND=<REMOTE_AUTH_BACKEND>
      - REMOTE_AUTH_HEADER=<REMOTE_AUTH_HEADER>
      - REMOTE_AUTH_AUTO_CREATE_USER=<REMOTE_AUTH_AUTO_CREATE_USER>
      - REMOTE_AUTH_DEFAULT_GROUPS=<REMOTE_AUTH_DEFAULT_GROUPS>
      - REMOTE_AUTH_DEFAULT_PERMISSIONS=<REMOTE_AUTH_DEFAULT_PERMISSIONS>
      - TZ=<TZ>
    volumes:
      - <path to data on host>:/config
    ports:
      - 8000:8000
    restart: unless-stopped
```

### docker cli

```
docker run -d \
  --name=netbox \
  -e PUID=1000 \
  -e PGID=1000 \
  -e SUPERUSER_EMAIL=<SUPERUSER_EMAIL> \
  -e SUPERUSER_PASSWORD=<SUPERUSER_PASSWORD> \
  -e ALLOWED_HOST=<ALLOWED_HOST> \
  -e BASE_PATH=<BASE_PATH> \
  -e DB_NAME=<DB_NAME> \
  -e DB_USER=<DB_USER> \
  -e DB_PASSWORD=<DB_PASSWORD> \
  -e DB_HOST=<DB_HOST> \
  -e DB_PORT=<DB_PORT> \
  -e REDIS_HOST=<REDIS_HOST> \
  -e REDIS_PORT=<REDIS_PORT> \
  -e REDIS_PASSWORD=<REDIS_PASSWORD> \
  -e REMOTE_AUTH_ENABLED=<REMOTE_AUTH_ENABLED> \
  -e REMOTE_AUTH_BACKEND=<REMOTE_AUTH_BACKEND> \
  -e REMOTE_AUTH_HEADER=<REMOTE_AUTH_HEADER> \
  -e REMOTE_AUTH_AUTO_CREATE_USER=<REMOTE_AUTH_AUTO_CREATE_USER> \
  -e REMOTE_AUTH_DEFAULT_GROUPS=<REMOTE_AUTH_DEFAULT_GROUPS> \
  -e REMOTE_AUTH_DEFAULT_PERMISSIONS=<REMOTE_AUTH_DEFAULT_PERMISSIONS> \
  -e TZ=<TZ> \
  -p 8000:8000 \
  -v <path to data on host>:/config \
  --restart unless-stopped \
  ghcr.io/linuxserver/netbox
```


## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8000` | will map the container's port 8000 to port 8000 on the host |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `SUPERUSER_EMAIL=<SUPERUSER_EMAIL>` | Username for admin account |
| `SUPERUSER_PASSWORD=<SUPERUSER_PASSWORD>` | Password for admin account |
| `ALLOWED_HOST=<ALLOWED_HOST>` | The hostname you will use to access the app (i.e., netbox.example.com) |
| `BASE_PATH=<BASE_PATH>` | The path you will use to access the app (i.e., /netbox, optional, default: none) |
| `DB_NAME=<DB_NAME>` | Database name (optional, default: netbox) |
| `DB_USER=<DB_USER>` | Database user |
| `DB_PASSWORD=<DB_PASSWORD>` | Database password |
| `DB_HOST=<DB_HOST>` | Database host (optional, default: postgres) |
| `DB_PORT=<DB_PORT>` | Database port (optional) |
| `REDIS_HOST=<REDIS_HOST>` | Redis host (optional, default: redis) |
| `REDIS_PORT=<REDIS_PORT>` | Redis port number (optional, default: 6379) |
| `REDIS_PASSWORD=<REDIS_PASSWORD>` | Redis password (optional, default: none) |
| `REMOTE_AUTH_ENABLED=<REMOTE_AUTH_ENABLED>` | Enable remote authentication (optional, default: False |
| `REMOTE_AUTH_BACKEND=<REMOTE_AUTH_BACKEND>` | Python path to the custom Django authentication backend to use for external user authentication (optional, default: netbox.authentication.RemoteUserBackend |
| `REMOTE_AUTH_HEADER=<REMOTE_AUTH_HEADER>` | Name of the HTTP header which informs NetBox of the currently authenticated user. (optional, default: HTTP_REMOTE_USER |
| `REMOTE_AUTH_AUTO_CREATE_USER=<REMOTE_AUTH_AUTO_CREATE_USER>` | If true, NetBox will automatically create local accounts for users authenticated via a remote service (optional, default: False |
| `REMOTE_AUTH_DEFAULT_GROUPS=<REMOTE_AUTH_DEFAULT_GROUPS>` | The list of groups to assign a new user account when created using remote authentication (optional, default: [] |
| `REMOTE_AUTH_DEFAULT_PERMISSIONS=<REMOTE_AUTH_DEFAULT_PERMISSIONS>` | A mapping of permissions to assign a new user account when created using remote authentication (optional, default: {} |
| `TZ=<TZ>` | Timezone (i.e., America/New_York) |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | config directory volume mapping |



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

Access the WebUI at <your-ip>:8000. For more information, check out [NetBox](https://github.com/netbox-community/netbox).


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=netbox&query=%24.mods%5B%27netbox%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=netbox "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it netbox /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f netbox`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' netbox`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ghcr.io/linuxserver/netbox`

## Versions

* **03.02.21:** - Added remote authentication environment variables.
* **02.01.21:** - Added BASE_PATH environment variable.
* **23.08.20:** - Initial Release.
