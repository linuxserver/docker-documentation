# linuxserver/clarkson

[![](https://img.shields.io/discord/354974912613449730.svg?logo=discord&label=LSIO%20Discord&style=flat-square)](https://discord.gg/YWrKVTn) [![](https://images.microbadger.com/badges/version/linuxserver/clarkson.svg)](https://microbadger.com/images/linuxserver/clarkson) [![](https://images.microbadger.com/badges/image/linuxserver/clarkson.svg)](https://microbadger.com/images/linuxserver/clarkson) ![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/clarkson.svg) ![Docker Stars](https://img.shields.io/docker/stars/linuxserver/clarkson.svg) [![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Pipeline-Builders/docker-clarkson/master)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-clarkson/job/master/) [![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/clarkson/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/clarkson/latest/index.html)

[Clarkson](https://github.com/linuxserver/Clarkson) is a web-based dashboard application that gives you a neat and clean interface for logging your fuel fill-ups for all of your vehicles. The application has full multi-user support, as well as multiple vehicles per user. Whenever you fill-up your car or motorcycle, keep the receipt and record the data in Clarkson.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/clarkson` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :---: | :--- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v6-latest |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker

```text
docker create \
  --name=clarkson \
  -e PUID=1000 \
  -e PGID=1000 \
  -e MYSQL_HOST=<mysql_host> \
  -e MYSQL_USERNAME=<mysql_username> \
  -e MYSQL_PASSWORD=<mysql_password> \
  -e ENABLE_REGISTRATIONS=<true|false> \
  -e TZ=Europe/London \
  -p 3000:3000 \
  --restart unless-stopped \
  linuxserver/clarkson
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2"
services:
  clarkson:
    image: linuxserver/clarkson
    container_name: clarkson
    environment:
      - PUID=1000
      - PGID=1000
      - MYSQL_HOST=<mysql_host>
      - MYSQL_USERNAME=<mysql_username>
      - MYSQL_PASSWORD=<mysql_password>
      - ENABLE_REGISTRATIONS=<true|false>
      - TZ=Europe/London
    ports:
      - 3000:3000
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `3000` | WebUI |

### Environment Variables \(`-e`\)

| Env | Function |  |
| :---: | :--- | :--- |
| `PUID=1000` | for UserID - see below for explanation |  |
| `PGID=1000` | for GroupID - see below for explanation |  |
| `MYSQL_HOST=<mysql_host>` | Points the backend to the MySQL database. This can be either a docker hostname or an IP. |  |
| `MYSQL_USERNAME=<mysql_username>` | The user with access to the _clarkson_ schema. |  |
| `MYSQL_PASSWORD=<mysql_password>` | The password for the user. |  |
| \`ENABLE\_REGISTRATIONS=&lt;true | false&gt;\` | **Defaults to** _**false**_. If set to _true_, allows new users to register. |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |  |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |


## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

**Please ensure MySQL is running before starting this container**.

It is preferred if you create the `clarkson` schema before initially running the container, then creating a user with granted permissions for the schema. Creating the schema before running the app is important as the "clarkson" user will not have permission to create the schema on your behalf. You can, of course, use the "root" user, which has the ability to create schemas automatically, but this is not recommended.

```sql
CREATE SCHEMA `clarkson`;
CREATE USER 'clarkson_user' IDENTIFIED BY 'supersecretpassword';
GRANT ALL ON `clarkson`.* TO 'clarkson_user';
```

Once running, the container will run an initial MySQL migration, which populates the schema with all tables and procedures. The application will start immediately afterwards. You will need to register an initial user, of which will be the admin of the application. All subsequent users will be standard users. You can disable registrations after the fact by recreating the container with the `ENABLE_REGISTRATIONS` flag set to `false`. This will not hide the "Register" link, but will disable the functionality.

## Support Info

* Shell access whilst the container is running: 
  * `docker exec -it clarkson /bin/bash`
* To monitor the logs of the container in realtime: 
  * `docker logs -f clarkson`
* Container version number 
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' clarkson`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/clarkson`

## Versions

* **22.02.19:** - Rebasing to alpine 3.9.
* **11.02.19:** - Add pipeline logic and multi arch.
* **22.08.18:** - Rebase to alpine linux 3.8.
* **19.02.18:** - Initial Release.

