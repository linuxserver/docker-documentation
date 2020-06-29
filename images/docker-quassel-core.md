# [linuxserver/quassel-core](https://github.com/linuxserver/docker-quassel-core)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-quassel-core.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-quassel-core)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-quassel-core.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-quassel-core/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-quassel-core/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-quassel-core/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/quassel-core.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/quassel-core "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/quassel-core.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/quassel-core)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/quassel-core.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/quassel-core)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-quassel-core%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-quassel-core/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fquassel-core%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/quassel-core/latest/index.html)

[Quassel-core](http://quassel-irc.org/) is a modern, cross-platform, distributed IRC client, meaning that one (or multiple) client(s) can attach to and detach from a central core.

This container handles the IRC connection (quasselcore) and requires a desktop client (quasselclient) to be used and configured. It is designed to be always on and will keep your identity present in IRC even when your clients cannot be online. Backlog (history) is downloaded by your client upon reconnection allowing infinite scrollback through time.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/quassel-core` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=quassel-core \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e RUN_OPTS=--config-from-environment `#optional` \
  -p 4242:4242 \
  -p 113:10113 `#optional` \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/quassel-core
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  quassel-core:
    image: linuxserver/quassel-core
    container_name: quassel-core
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - RUN_OPTS=--config-from-environment #optional
    volumes:
      - <path to data>:/config
    ports:
      - 4242:4242
    ports:
      - 113:10113 #optional
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `4242` | The port quassel-core listens for connections on. |
| `10113` | Optional Ident Port |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `RUN_OPTS=--config-from-environment` | Custom CLI options for Quassel |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Database and quassel-core configuration storage. |



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

Quassel wiki: [quassel](http://bugs.quassel-irc.org/projects/quassel-irc/wiki)

A great place to host a quassel instance is a VPS, such as [DigitalOcean](https://www.digitalocean.com/?refcode=501c48b34b8c). For $5 a month you can have a 24/7 IRC connection and be up and running in under 55 seconds (or so they claim).

Once you have the container running, fire up a quassel desktop client and connect to your new core instance using your droplets public IP address and the port you specified in your `docker run` command *default: 4242*. Create an admin user, select SQLite as your storage backend (Quassel limitation). Setup your real name and nick, then press `Save & Connect`.

You're now connected to IRC. Let's add you to our [IRC](http://www.linuxserver.io/index.php/irc/) `#linuxserver.io` room on Freenode. Click 'File' > 'Networks' > 'Configure Networks' > 'Add' (under Networks section, not Servers) > 'Use preset' > Select 'Freenode' and then configure your identity using the tabs in the 'Network details' section. Once connected to Freenode, click `#join` and enter `#linuxserver.io`. That's it, you're done.

## Stateless usage

To use Quassel in stateless mode, where it needs to be configured through
environment arguments, run it with the `--config-from-environment` RUN_OPTS environment setting.

| Env | Usage |
| :----: | --- |
| DB_BACKEND | `SQLite` or `PostgreSQL` |
| DB_PGSQL_USERNAME | PostgreSQL User |
| DB_PGSQL_PASSWORD | PostgreSQL Password |
| DB_PGSQL_HOSTNAME | PostgreSQL Host |
| DB_PGSQL_PORT | PostgreSQL Port |
| AUTH_AUTHENTICATOR | `Database` or `LDAP` |
| AUTH_LDAP_HOSTNAME | LDAP Host |
| AUTH_LDAP_PORT | LDAP Port |
| AUTH_LDAP_BIND_DN | LDAP Bind Domain |
| AUTH_LDAP_BIND_PASSWORD | LDAP Password |
| AUTH_LDAP_FILTER | LDAP Authentication Filters |
| AUTH_LDAP_UID_ATTRIBUTE | LDAP UID |

Additionally you have RUN_OPTS that can be used to customize pathing and behvior.

| Option | Example |
| :----: | --- |
| --strict-ident | strictly bool `--strict-ident` |
| --ident-daemon | strictly bool `--ident-daemon` |
| --ident-port | `--ident-port "10113"` |
| --ident-listen | `--ident-listen "::,0.0.0.0"` |
| --ssl-cert | `--ssl-cert /config/keys/cert.crt` |
| --ssl-key | `--ssl-key /config/keys/cert.key` |
| --require-ssl | strictly bool `--require-ssl` |

Minimal example with SQLite:

```
docker create \
  --name=quassel-core \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e RUN_OPTS='--config-from-environment' \
  -e DB_BACKEND=SQLite \
  -e AUTH_AUTHENTICATOR=Database \
  -p 4242:4242 \
  -v <path to data>:/config \
  --restart unless-stopped \
  linuxserver/quassel-core
```


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27quassel-core%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=quassel-core "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it quassel-core /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f quassel-core`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' quassel-core`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/quassel-core`

## Versions

* **19.12.19:** - Rebasing to alpine 3.11.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **20.03.19:** - Make stateless operation an option, with input from one of the quassel team.
* **26.01.19:** - Add pipeline logic and multi arch.
* **08.01.19:** - Rebase to Ubuntu Bionic and upgrade to Quassel`0.13.0` See [here.](https://quassel-irc.org/node/134).
* **30.07.18:** - Rebase to alpine:3.8 and use buildstage.
* **03.01.18:** - Deprecate cpu_core routine lack of scaling.
* **09.12.17:** - Rebase to alpine:3.7.
* **26.11.17:** - Use cpu core counting routine to speed up build time.
* **12.07.17:** - Add inspect commands to README, move to jenkins build and push.
* **27.05.17:** - Rebase to alpine:3.6.
* **13.05.17:** - Switch to git source.
* **28.12.16:** - Rebase to alpine:3.5.
* **23.11.16:** - Rebase to alpine:edge.
* **23.09.16:** - Use QT5 dependencies (thanks bauerj).
* **10.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README.
* **10.08.16:** - Rebase to xenial.
* **14.10.15:** - Removed the webui, turned out to be to unstable for most usecases.
* **01.09.15:** - Fixed mistake in README.
* **30.07.15:** - Switched to internal baseimage, and fixed a bug with updating the webinterface.
* **06.07.15:** - Enabled BLOWFISH encryption and added a (optional) webinterface, for the times you dont have access to your client.
