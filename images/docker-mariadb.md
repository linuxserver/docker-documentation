# linuxserver/mariadb

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-mariadb.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-mariadb) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-mariadb.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-mariadb/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-mariadb/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-mariadb/container_registry) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/mariadb.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/mariadb) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/mariadb.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/mariadb) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/mariadb.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/mariadb) [![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-mariadb%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-mariadb/job/master/) [![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fmariadb%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/mariadb/latest/index.html)

[Mariadb](https://mariadb.org/) is one of the most popular database servers. Made by the original developers of MySQL.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/mariadb` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=mariadb \
  -e PUID=1000 \
  -e PGID=1000 \
  -e MYSQL_ROOT_PASSWORD=ROOT_ACCESS_PASSWORD \
  -e TZ=Europe/London \
  -e MYSQL_DATABASE=USER_DB_NAME `#optional` \
  -e MYSQL_USER=MYSQL_USER `#optional` \
  -e MYSQL_PASSWORD=DATABASE_PASSWORD `#optional` \
  -e REMOTE_SQL=http://URL1/your.sql,https://URL2/your.sql `#optional` \
  -p 3306:3306 \
  -v path_to_data:/config \
  --restart unless-stopped \
  linuxserver/mariadb
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  mariadb:
    image: linuxserver/mariadb
    container_name: mariadb
    environment:
      - PUID=1000
      - PGID=1000
      - MYSQL_ROOT_PASSWORD=ROOT_ACCESS_PASSWORD
      - TZ=Europe/London
      - MYSQL_DATABASE=USER_DB_NAME #optional
      - MYSQL_USER=MYSQL_USER #optional
      - MYSQL_PASSWORD=DATABASE_PASSWORD #optional
      - REMOTE_SQL=http://URL1/your.sql,https://URL2/your.sql #optional
    volumes:
      - path_to_data:/config
    ports:
      - 3306:3306
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |
| `3306` | Mariadb listens on this port. |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `MYSQL_ROOT_PASSWORD=ROOT_ACCESS_PASSWORD` | Set this to root password for installation \(minimum 4 characters\). |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `MYSQL_DATABASE=USER_DB_NAME` | Specify the name of a database to be created on image startup. |
| `MYSQL_USER=MYSQL_USER` | This user will have superuser access to the database specified by MYSQL\_DATABASE \(do not use root here\). |
| `MYSQL_PASSWORD=DATABASE_PASSWORD` | Set this to the password you want to use for you MYSQL\_USER \(minimum 4 characters\). |
| `REMOTE_SQL=http://URL1/your.sql,https://URL2/your.sql` | Set this to ingest sql files from an http/https endpoint \(comma seperated array\). |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Contains the db itself and all assorted settings. |

## Environment variables from files \(Docker secrets\)

You can set any environment variable from a file by using a special prepend `FILE__`.

As an example:

```text
-e FILE__PASSWORD=/run/secrets/mysecretpassword
```

Will set the environment variable `PASSWORD` based on the contents of the `/run/secrets/mysecretpassword` file.

## Umask for running applications

For all of our images we provide the ability to override the default umask settings for services started within the containers using the optional `-e UMASK=022` setting. Keep in mind umask is not chmod it subtracts from permissions based on it's value it does not add. Please read up [here](https://en.wikipedia.org/wiki/Umask) before asking for support.

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

If you didn't set a password during installation, \(see logs for warning\) use `mysqladmin -u root password <PASSWORD>` to set one at the docker prompt...

NOTE changing the MYSQL\_ROOT\_PASSWORD variable after the container has set up the initial databases has no effect, use the mysqladmin tool to change your mariadb password.

NOTE if you want to use \(MYSQL\_DATABASE MYSQL\_USER MYSQL\_PASSWORD\) **all three** of these variables need to be set you cannot pick and choose.

Unraid users, it is advisable to edit the template/webui after setup and remove reference to this variable.

Find custom.cnf in /config for config changes \(restart container for them to take effect\) , the databases in /config/databases and the log in /config/log/myqsl

### Loading passwords and users from files

The `MYSQL_ROOT_PASSWORD MYSQL_DATABASE MYSQL_USER MYSQL_PASSWORD REMOTE_SQL` env values can be set in a file:

```text
/config/env
```

Using the following format:

```text
MYSQL_ROOT_PASSWORD="ROOT_ACCESS_PASSWORD"
MYSQL_DATABASE="USER_DB_NAME"
MYSQL_USER="MYSQL_USER"
MYSQL_PASSWORD="DATABASE_PASSWORD"
REMOTE_SQL="http://URL1/your.sql,https://URL2/your.sql"
```

These settings can be mixed and matched with Docker ENV settings as you require, but the settings in the file will always take precedence.

### Bootstrapping a new instance

We support a one time run of custom sql files on init. In order to use this place `*.sql` files in:

```text
/config/initdb.d/
```

This will have the same effect as setting the `REMOTE_SQL` environment variable. The sql will only be run on the containers first boot and setup.

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27mariadb%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=mariadb)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it mariadb /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f mariadb`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' mariadb`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/mariadb`

## Versions

* **27.10.19:** - Bump to 10.4, ability use custom sql on initial init ,defining root passwords via file.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **07.03.19:** - Add ability to setup a database and default user on first spinup.
* **26.01.19:** - Add pipeline logic and multi arch.
* **10.09.18:** - Rebase to ubuntu bionic and use 10.3 mariadb repository.
* **09.12.17:** - Fix continuation lines.
* **12.09.17:** - Gracefully shut down mariadb.
* **27.10.16:** - Implement linting suggestions on database init script.
* **11.10.16:** - Rebase to ubuntu xenial, add version labelling.
* **09.03.16:** - Update to mariadb 10.1. Change to use custom.cnf over my.cnf in /config. Restructured init files to change config options on startup, rather than in the dockerfile.
* **26.01.16:** - Change user of mysqld\_safe script to abc, better unclean shutdown handling on restart.
* **23.12.15:** - Remove autoupdating, between some version updates the container breaks.
* **12.08.15:** - Initial Release.

