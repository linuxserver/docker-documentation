# [linuxserver/snipe-it](https://github.com/linuxserver/docker-snipe-it)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-snipe-it.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-snipe-it)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-snipe-it.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-snipe-it/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-snipe-it/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-snipe-it/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/snipe-it.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/snipe-it "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/snipe-it.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/snipe-it)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/snipe-it.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/snipe-it)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-snipe-it%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-snipe-it/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fsnipe-it%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/snipe-it/latest/index.html)

[Snipe-it](https://github.com/snipe/snipe-it) makes asset management easy. It was built by people solving real-world IT and asset management problems, and a solid UX has always been a top priority. Straightforward design and bulk actions mean getting things done faster.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/snipe-it` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=snipe-it \
  -e PUID=1000 \
  -e PGID=1000 \
  -e APP_URL=<hostname or ip> \
  -e MYSQL_PORT_3306_TCP_ADDR=<mysql host> \
  -e MYSQL_PORT_3306_TCP_PORT=<mysql port> \
  -e MYSQL_DATABASE=<mysql database> \
  -e MYSQL_USER=<mysql pass> \
  -e MYSQL_PASSWORD=changeme \
  -p 8080:80 \
  -v <path to snipe-it data>:/config \
  --restart unless-stopped \
  linuxserver/snipe-it
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
version: "3"
services:
  mysql:
    image: mysql:5
    container_name: snipe_mysql
    restart: always
    volumes:
      - <path to mysql data>:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=<secret password>
      - MYSQL_USER=snipe
      - MYSQL_PASSWORD=<secret user password>
      - MYSQL_DATABASE=snipe
  snipeit:
    image: linuxserver/snipe-it:latest
    container_name: snipe-it
    restart: always
    depends_on:
      - mysql
    volumes:
      - <path to data>:/config
    environment:
      - APP_URL=< your application URL IE 192.168.10.1:8080>
      - MYSQL_PORT_3306_TCP_ADDR=mysql
      - MYSQL_PORT_3306_TCP_PORT=3306
      - MYSQL_DATABASE=snipe
      - MYSQL_USER=snipe
      - MYSQL_PASSWORD=<secret user password>
      - PGID=1000
      - PUID=1000
    ports:
      - "8080:80"

```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | Snipe-IT Web UI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `APP_URL=<hostname or ip>` | Hostname or IP and port if applicable IE <ip or hostname>:8080 |
| `MYSQL_PORT_3306_TCP_ADDR=<mysql host>` | Mysql hostname or IP to use |
| `MYSQL_PORT_3306_TCP_PORT=<mysql port>` | Mysql port to use |
| `MYSQL_DATABASE=<mysql database>` | Mysql database to use |
| `MYSQL_USER=<mysql pass>` | Mysql user to use |
| `MYSQL_PASSWORD=changeme` | Mysql password to use |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Contains your config files and data storage for Snipe-IT |



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

## Optional Parameters

This container also generates an SSL certificate and stores it in
```
/config/keys/cert.crt
/config/keys/key.crt
```
To use your own certificate swap these files with yours. To use SSL forward your port to 443 inside the container IE:

```
-p 443:443
```

The application accepts a series of environment variables to further customize itself on boot:

| Parameter | Function |
| :---: | --- |
| `-e APP_TIMEZONE=` | The timezone the application will use IE US/Pacific|
| `-e APP_ENV=` | Default is production but can use testing or develop|
| `-e APP_DEBUG=` | Set to true to see debugging output in the web UI|
| `-e APP_LOCALE=` | Default is en set to the language preferred full list [here][localesurl]|
| `-e MAIL_PORT_587_TCP_ADDR=` | SMTP mailserver ip or hostname|
| `-e MAIL_PORT_587_TCP_PORT=` | SMTP mailserver port|
| `-e MAIL_ENV_FROM_ADDR=` | The email address mail should be replied to and listed when sent|
| `-e MAIL_ENV_FROM_NAME=` | The name listed on email sent from the default account on the system|
| `-e MAIL_ENV_ENCRYPTION=` | Mail encryption to use IE tls |
| `-e MAIL_ENV_USERNAME=` | SMTP server login username|
| `-e MAIL_ENV_PASSWORD=` | SMTP server login password|



## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Access the webui at `<your-ip>:8080`, for more information check out [Snipe-it](https://github.com/snipe/snipe-it).


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27snipe-it%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=snipe-it "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it snipe-it /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f snipe-it`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' snipe-it`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/snipe-it`

## Versions

* **01.06.20:** - Rebasing to alpine 3.12.
* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **10.04.19:** - Add php deps for V4.7.0, ensure framework directories are available at build time.
* **10.04.19:** - Fix permissions for new bootstrap cache directory.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.02.19:** - Rebasing to alpine 3.9.
* **31.10.18:** - Rebasing to alpine 3.8
* **05.08.18:** - Migration to live build server.
* **13.06.18:** - Initial Release.
