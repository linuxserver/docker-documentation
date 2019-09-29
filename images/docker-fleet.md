# linuxserver/fleet

[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-fleet.svg?style=flat-square&color=E68523)](https://github.com/linuxserver/docker-fleet/releases) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/fleet.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/fleet) [![MicroBadger Size](https://img.shields.io/microbadger/image-size/linuxserver/fleet.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/fleet) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/fleet.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/fleet) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/fleet.svg?style=flat-square&color=E68523)](https://hub.docker.com/r/linuxserver/fleet) [![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-fleet/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-fleet/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/fleet/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/fleet/latest/index.html)

[Fleet](https://github.com/linuxserver/fleet) provides an online web interface which displays a set of maintained images from one or more owned repositories.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/fleet` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :---: | :--- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=fleet \
  -e PUID=1000 \
  -e PGID=1000 \
  -e fleet_admin_authentication_type=DATABASE \
  -e fleet_database_url=jdbc:mariadb://<url>:3306/fleet \
  -e fleet_database_username=fleet_user \
  -e fleet_database_password=dbuserpassword \
  -e fleet_dockerhub_username=dockerhub_user \
  -e fleet_dockerhub_password=password \
  -e fleet_refresh_interval=60 `#optional` \
  -e fleet_admin_secret=randomstring `#optional` \
  -e fleet_admin_username=admin `#optional` \
  -e fleet_admin_password=secretpassword `#optional` \
  -e fleet_skip_sync_on_startup=true `#optional` \
  -p 8080:8080 \
  -v </path/to/appdata/config>:/config \
  --restart unless-stopped \
  linuxserver/fleet
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  fleet:
    image: linuxserver/fleet
    container_name: fleet
    environment:
      - PUID=1000
      - PGID=1000
      - fleet_admin_authentication_type=DATABASE
      - fleet_database_url=jdbc:mariadb://<url>:3306/fleet
      - fleet_database_username=fleet_user
      - fleet_database_password=dbuserpassword
      - fleet_dockerhub_username=dockerhub_user
      - fleet_dockerhub_password=password
      - fleet_refresh_interval=60 #optional
      - fleet_admin_secret=randomstring #optional
      - fleet_admin_username=admin #optional
      - fleet_admin_password=secretpassword #optional
      - fleet_skip_sync_on_startup=true #optional
    volumes:
      - </path/to/appdata/config>:/config
    ports:
      - 8080:8080
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `8080` | Http port |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `fleet_admin_authentication_type=DATABASE` | A switch to define how Fleet manages user logins. If set to DATABASE, see the related optional params. Can be set to either DATABASE or PROPERTIES. |
| `fleet_database_url=jdbc:mariadb://<url>:3306/fleet` | The full JDBC connection string to the Fleet database |
| `fleet_database_username=fleet_user` | The username with the relevant GRANT permissions for the database |
| `fleet_database_password=dbuserpassword` | The database user's password. |
| `fleet_dockerhub_username=dockerhub_user` | The username of a member of your repository's owners team. This is used to get the list of your \(and only your\) namespaces in Docker Hub. |
| `fleet_dockerhub_password=password` | The password for the Docker Hub user. |
| `fleet_refresh_interval=60` | The time in minutes for how often Fleet should scan the Docker Hub repositories. |
| `fleet_admin_secret=randomstring` | A string used as part of the password key derivation process. Not mandatory. Only used if authentication type is set to DATABASE. |
| `fleet_admin_username=admin` | The name of the sole admin user, if authentication type is set to PROPERTIES. |
| `fleet_admin_password=secretpassword` | The password for the sole admin user, if authentication type is set to PROPERTIES. |
| `fleet_skip_sync_on_startup=true` | A flag to tell the app not to run an initial synchronisation process when it starts up |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | The primary config file and rolling log files. |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Navigate to `http://your_ip_here:8080` to display the home page. If `DATABASE` is selected as the preferred authentication process, ensure that you set up an initial user via `http://your_ip_here:8080/setup`. Once done, that page will no longer be available. A restart is preferable as it will remove the page altogether. Once complete, you can log into the app via `http://your_ip_here:8080/login` to manage your repositories.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it fleet /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f fleet`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' fleet`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/fleet`

## Versions

* **02.07.19:** - Rebasing to alpine 3.10.
* **02.07.19:** - Stop container if fleet fails.
* **19.05.19:** - Use new base images for arm versions.
* **01.04.19:** - Initial Release

