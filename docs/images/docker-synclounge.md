---
title: synclounge
---
<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-synclounge/blob/master/.github/CONTRIBUTING.md -->
# [linuxserver/synclounge](https://github.com/linuxserver/docker-synclounge)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Fsynclounge?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh/gateway/linuxserver-ci/docker/linuxserver%2Fsynclounge)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-synclounge.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-synclounge)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-synclounge.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-synclounge/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-synclounge/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-synclounge/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/synclounge)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/synclounge.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/synclounge)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/synclounge.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/synclounge)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-synclounge%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-synclounge/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fsynclounge%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/synclounge/latest/index.html)

[Synclounge](https://github.com/samcm/synclounge) is a third party tool that allows you to watch Plex in sync with your friends/family, wherever you are.

[![synclounge](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/synclounge-banner.png)](https://github.com/samcm/synclounge)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://distribution.github.io/distribution/spec/manifest-v2-2/#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/synclounge:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64v8-\<version tag\> |
| armhf | ❌ | |

## Application Setup

The web app and the server are both accessible at `http://SERVERIP:8088`.

Note: It is recommended to use `http` as the external proto with a reverse proxy due to `https` not working with external plex clients.

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
---
version: "2.1"
services:
  synclounge:
    image: lscr.io/linuxserver/synclounge:latest
    container_name: synclounge
    environment:
      - AUTH_LIST=plexuser1,plexuser2,email1,machineid1 #optional
      - AUTOJOIN_ENABLED=false #optional
      - AUTOJOIN_ROOM=roomname #optional
    ports:
      - 8088:8088
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=synclounge \
  -e AUTH_LIST=plexuser1,plexuser2,email1,machineid1 `#optional` \
  -e AUTOJOIN_ENABLED=false `#optional` \
  -e AUTOJOIN_ROOM=roomname `#optional` \
  -p 8088:8088 \
  --restart unless-stopped \
  lscr.io/linuxserver/synclounge:latest
```

## Parameters

Containers are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `8088` | Web app and server port |

### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `AUTH_LIST=plexuser1,plexuser2,email1,machineid1` | If set, only the users defined here and the users of the plex servers defined here will be able to access the server. Use e-mails, plex usernames and/or plex server machine ids, comma separated, no spaces. |
| `AUTOJOIN_ENABLED=false` | DEPRECATED - (Still works but will be removed in the future in favor of the built-in var `autojoin__room`) - Set to `true` to let users autojoin the server and a room (specified by the `AUTOJOIN_ROOM` var). |
| `AUTOJOIN_ROOM=roomname` | DEPRECATED - (Still works but will be removed in the future in favor of the built-in var `autojoin__room`) - Set the room name for auto joining (requires `AUTOJOIN_ENABLED` set to `true`). |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |

#### Miscellaneous Options

| Parameter | Function |
| :-----:   | --- |

## Environment variables from files (Docker secrets)

You can set any environment variable from a file by using a special prepend `FILE__`.

As an example:

```bash
-e FILE__MYVAR=/run/secrets/mysecretvariable
```

Will set the environment variable `MYVAR` based on the contents of the `/run/secrets/mysecretvariable` file.

## Umask for running applications

For all of our images we provide the ability to override the default umask settings for services started within the containers using the optional `-e UMASK=022` setting.
Keep in mind umask is not chmod it subtracts from permissions based on it's value it does not add. Please read up [here](https://en.wikipedia.org/wiki/Umask) before asking for support.

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=synclounge&query=%24.mods%5B%27synclounge%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=synclounge "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running:

    ```bash
    docker exec -it synclounge /bin/bash
    ```

* To monitor the logs of the container in realtime:

    ```bash
    docker logs -f synclounge
    ```

* Container version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' synclounge
    ```

* Image version number:

    ```bash
    docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/synclounge:latest
    ```

## Updating Info

Most of our images are static, versioned, and require an image update and container recreation to update the app inside. With some exceptions (ie. nextcloud, plex), we do not recommend or support updating apps inside the container. Please consult the [Application Setup](#application-setup) section above to see if it is recommended for the image.

Below are the instructions for updating containers:

### Via Docker Compose

* Update images:
    * All images:

        ```bash
        docker-compose pull
        ```

    * Single image:

        ```bash
        docker-compose pull synclounge
        ```

* Update containers:
    * All containers:

        ```bash
        docker-compose up -d
        ```

    * Single container:

        ```bash
        docker-compose up -d synclounge
        ```

* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Docker Run

* Update the image:

    ```bash
    docker pull lscr.io/linuxserver/synclounge:latest
    ```

* Stop the running container:

    ```bash
    docker stop synclounge
    ```

* Delete the container:

    ```bash
    docker rm synclounge
    ```

* Recreate a new container with the same docker run parameters as instructed above (if mapped correctly to a host folder, your `/config` folder and settings will be preserved)
* You can also remove the old dangling images:

    ```bash
    docker image prune
    ```

### Via Watchtower auto-updater (only use if you don't remember the original parameters)

* Pull the latest image at its tag and replace it with the same env variables in one run:

    ```bash
    docker run --rm \
      -v /var/run/docker.sock:/var/run/docker.sock \
      containrrr/watchtower \
      --run-once synclounge
    ```

* You can also remove the old dangling images: `docker image prune`

!!! warning 

    We do not endorse the use of Watchtower as a solution to automated updates of existing Docker containers. In fact we generally discourage automated updates. However, this is a useful tool for one-time manual updates of containers where you have forgotten the original parameters. In the long term, we highly recommend using [Docker Compose](https://docs.linuxserver.io/general/docker-compose).

### Image Update Notifications - Diun (Docker Image Update Notifier)

!!! tip 

    We recommend [Diun](https://crazymax.dev/diun/) for update notifications. Other tools that automatically update containers unattended are not recommended or supported.

## Building locally

If you want to make local modifications to these images for development purposes or just to customize the logic:

```bash
git clone https://github.com/linuxserver/docker-synclounge.git
cd docker-synclounge
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/synclounge:latest .
```

The ARM variants can be built on x86_64 hardware using `multiarch/qemu-user-static`

```bash
docker run --rm --privileged multiarch/qemu-user-static:register --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

## Versions

* **26.08.23:** - Rebase to Alpine 3.18.
* **04.07.23:** - Deprecate armhf. As announced [here](https://www.linuxserver.io/blog/a-farewell-to-arm-hf)
* **29.11.22:** - Rebase to alpine 3.17, upgrade to s6v3.
* **19.09.22:** - Rebase to alpine 3.15.
* **12.02.21:** - Fix optional dependency builds in aarch64 image.
* **12.02.21:** - Rebasing to alpine 3.13.
* **28.10.20:** - Update to v4. Env vars `EXTERNAL_URL`, `EXTERNAL_SERVER_PORT` and `AUTOJOIN_PASSWORD` are deprecated and no longer have any effect. Env vars `AUTOJOIN_ENABLED` and `AUTOJOIN_ROOM` are still working but will be removed in the future in favor of synclounge's built-in var `autojoin__room`. If you are reverse proxying, do not forget to update your proxy settings ([here](https://github.com/linuxserver/reverse-proxy-confs/blob/master/synclounge.subdomain.conf.sample) and [here](https://github.com/linuxserver/reverse-proxy-confs/blob/master/synclounge.subfolder.conf.sample)) as the server port and addresses are changed.
* **11.10.20:** - Pin builds to upstream commit `6aecc9bd` while evaluating the breaking changes upstream.
* **27.09.20:** - Updating the external repo endpoint.
* **01.06.20:** - Rebasing to alpine 3.12.
* **11.05.20:** - Initial Release.