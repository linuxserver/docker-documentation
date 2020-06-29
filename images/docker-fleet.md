# linuxserver/fleet

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-fleet.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-fleet) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-fleet.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-fleet/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-fleet/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-fleet/container_registry) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/fleet.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/fleet) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/fleet.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/fleet) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/fleet.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/fleet) [![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-fleet%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-fleet/job/master/) [![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Ffleet%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/fleet/latest/index.html)

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
  -e fleet_admin_secret=randomstring `#optional` \
  -p 8080:8080 \
  -v </path/to/appdata/config>:/config \
  --restart unless-stopped \
  linuxserver/fleet
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
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
      - fleet_admin_secret=randomstring #optional
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
| `fleet_admin_secret=randomstring` | A string used as part of the password key derivation process. |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | The primary config file and rolling log files. |

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

Navigate to `http://your_ip_here:8080` to display the home page. If `DATABASE` is selected as the preferred authentication process, ensure that you set up an initial user via `http://your_ip_here:8080/setup`. Once done, that page will no longer be available. A restart is preferable as it will remove the page altogether. Once complete, you can log into the app via `http://your_ip_here:8080/login` to manage your repositories.

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27fleet%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=fleet)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

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

* **26.04.20:** - Updated to keep in line with v2.0.0 branch of Fleet
* **19.12.19:** - Rebasing to alpine 3.11.
* **02.07.19:** - Rebasing to alpine 3.10.
* **02.07.19:** - Stop container if fleet fails.
* **19.05.19:** - Use new base images for arm versions.
* **01.04.19:** - Initial Release

