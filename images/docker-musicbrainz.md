---
title: musicbrainz
---
# IMPORTANT NOTICE: THIS IMAGE HAS BEEN DEPRECATED
[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)](https://linuxserver.io)

[![Blog](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Blog)](https://blog.linuxserver.io "all the things you can do with our containers including How-To guides, opinions and much more!")
[![Discord](https://img.shields.io/discord/354974912613449730.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Discord&logo=discord)](https://discord.gg/YWrKVTn "realtime support / chat with the community and the team.")
[![Discourse](https://img.shields.io/discourse/https/discourse.linuxserver.io/topics.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=discourse)](https://discourse.linuxserver.io "post on our community forum.")
[![Fleet](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Fleet)](https://fleet.linuxserver.io "an online web interface which displays all of our maintained images.")
[![GitHub](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub&logo=github)](https://github.com/linuxserver "view the source for all of our repositories.")
[![Open Collective](https://img.shields.io/opencollective/all/linuxserver.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Supporters&logo=open%20collective)](https://opencollective.com/linuxserver "please consider helping us by either donating or contributing to our budget")

The [LinuxServer.io](https://linuxserver.io) team brings you another container release featuring:

* regular and timely application updates
* easy user mappings (PGID, PUID)
* custom base image with s6 overlay
* weekly base OS updates with common layers across the entire LinuxServer.io ecosystem to minimise space usage, down time and bandwidth
* regular security updates

Find us at:
* [Blog](https://blog.linuxserver.io) - all the things you can do with our containers including How-To guides, opinions and much more!
* [Discord](https://discord.gg/YWrKVTn) - realtime support / chat with the community and the team.
* [Discourse](https://discourse.linuxserver.io) - post on our community forum.
* [Fleet](https://fleet.linuxserver.io) - an online web interface which displays all of our maintained images.
* [GitHub](https://github.com/linuxserver) - view the source for all of our repositories.
* [Open Collective](https://opencollective.com/linuxserver) - please consider helping us by either donating or contributing to our budget

# [linuxserver/musicbrainz](https://github.com/linuxserver/docker-musicbrainz)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-musicbrainz.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-musicbrainz)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-musicbrainz.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-musicbrainz/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-musicbrainz/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-musicbrainz/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/musicbrainz.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/musicbrainz "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/musicbrainz.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/musicbrainz)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/musicbrainz.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/musicbrainz)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-musicbrainz%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-musicbrainz/job/master/)

[MusicBrainz](https://musicbrainz.org/) is an open music encyclopedia that collects music metadata and makes it available to the public.

[![musicbrainz](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/musicbrainz-icon.png)](https://musicbrainz.org/)

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/musicbrainz` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container.

### docker-compose ([recommended](https://docs.linuxserver.io/general/docker-compose))

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  musicbrainz:
    image: lscr.io/linuxserver/musicbrainz
    container_name: musicbrainz
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - BRAINZCODE=<code from MusicBrainz>
      - WEBADDRESS=<ip of host>
      - NPROC=<parameter> #optional
    volumes:
      - </path/to/appdata/config>:/config
      - </path/to/appdata/config>:/data
    ports:
      - 5000:5000
    restart: unless-stopped
```

### docker cli

```
docker run -d \
  --name=musicbrainz \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e BRAINZCODE=<code from MusicBrainz> \
  -e WEBADDRESS=<ip of host> \
  -e NPROC=<parameter> `#optional` \
  -p 5000:5000 \
  -v </path/to/appdata/config>:/config \
  -v </path/to/appdata/config>:/data \
  --restart unless-stopped \
  lscr.io/linuxserver/musicbrainz
```


## Parameters

Container images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

| Parameter | Function |
| :----: | --- |
| `-p 5000` | WebUI |
| `-e PUID=1000` | for UserID - see below for explanation |
| `-e PGID=1000` | for GroupID - see below for explanation |
| `-e TZ=Europe/London` | Specify a timezone to use EG Europe/London |
| `-e BRAINZCODE=<code from MusicBrainz>` | To enter MusicBrainz code. See Setting up the application |
| `-e WEBADDRESS=<ip of host>` | To set ip for host to allow css to render properly, DO NOT ENTER PORT NUMBER. |
| `-e NPROC=<parameter>` | To set number of proceses, defaults to 5 if unset. |
| `-v /config` | Config files for musicbrainz. |
| `-v /data` | Data files for musicbrainz. |

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

When using volumes (`-v` flags) permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```


&nbsp;
## Application Setup

+ For all updates you should pull the latest image, clear all files and folders in /config and /data and reinitiate the database import by (re)starting the docker. We do not officially support upgrading this container in place with existing data sets. 

+ **If you did not set WEBADDRESS env variable, then AFTER iniatilisation is complete you will need to edit the line `sub WEB_SERVER { "localhost:5000" }` in file /config/DBDefs.pm changing localhost to the ip of your host, this is to allow css to display properly**

* You must register here to receive a MusicBrainz code to allow you to receive database updates, it is free. [Get Code here](https://metabrainz.org/supporters/account-type).
* The initial import and setup of the database can take quite a long time, dependant on your download speed etc, be patient and don't restart the container before it's complete.
* It appears there are issues with unraid and using /mnt/user/cache/appdata instead of /mnt/cache/appdata, use /mnt/cache/appdata.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=musicbrainz&query=%24.mods%5B%27musicbrainz%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=musicbrainz "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.


## Support Info

* Shell access whilst the container is running: `docker exec -it musicbrainz /bin/bash`
* To monitor the logs of the container in realtime: `docker logs -f musicbrainz`
* container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' musicbrainz`
* image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/musicbrainz`

## Updating Info

Most of our images are static, versioned, and require an image update and container recreation to update the app inside. With some exceptions (ie. nextcloud, plex), we do not recommend or support updating apps inside the container. Please consult the [Application Setup](#application-setup) section above to see if it is recommended for the image.

Below are the instructions for updating containers:

### Via Docker Compose
* Update all images: `docker-compose pull`
  * or update a single image: `docker-compose pull musicbrainz`
* Let compose update all containers as necessary: `docker-compose up -d`
  * or update a single container: `docker-compose up -d musicbrainz`
* You can also remove the old dangling images: `docker image prune`

### Via Docker Run
* Update the image: `docker pull lscr.io/linuxserver/musicbrainz`
* Stop the running container: `docker stop musicbrainz`
* Delete the container: `docker rm musicbrainz`
* Recreate a new container with the same docker run parameters as instructed above (if mapped correctly to a host folder, your `/config` folder and settings will be preserved)
* You can also remove the old dangling images: `docker image prune`

### Via Watchtower auto-updater (only use if you don't remember the original parameters)
* Pull the latest image at its tag and replace it with the same env variables in one run:
  ```
  docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  containrrr/watchtower \
  --run-once musicbrainz
  ```
* You can also remove the old dangling images: `docker image prune`

**Note:** We do not endorse the use of Watchtower as a solution to automated updates of existing Docker containers. In fact we generally discourage automated updates. However, this is a useful tool for one-time manual updates of containers where you have forgotten the original parameters. In the long term, we highly recommend using [Docker Compose](https://docs.linuxserver.io/general/docker-compose).

### Image Update Notifications - Diun (Docker Image Update Notifier)
* We recommend [Diun](https://crazymax.dev/diun/) for update notifications. Other tools that automatically update containers unattended are not recommended or supported.

## Building locally

If you want to make local modifications to these images for development purposes or just to customize the logic:
```
git clone https://github.com/linuxserver/docker-musicbrainz.git
cd docker-musicbrainz
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/musicbrainz:latest .
```

The ARM variants can be built on x86_64 hardware using `multiarch/qemu-user-static`
```
docker run --rm --privileged multiarch/qemu-user-static:register --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

## Versions

* **23.02.21:** - Deprecate image as no one stepped up to take over as maintainer.
* **03.10.20:** - Rebase to alpine 3.12, add gettext and move to nodejs-current.
* **17.05.19:** - Update DBDefs.pm to schema 25 database.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **02.03.19:** - Revert to alpine 3.8 to fix incompatibilities with frontend build tools.
* **19.02.19:** - Multi Arch and add pipeline logic, rebase to Alpine 3.9
* **22.08.18:** - Bump server version 2018-08-14.
* **30.06.18:** - Bump server version 2018-06-30.
* **01.06.18:** - Bump server version 2018-05-30 , simplify sed and use yarn instead of npm.
* **14.05.18:** - Bump server version 2018-05-09.
* **26.04.18:** - Bump server version 2018-04-23.
* **09.02.18:** - Bump server version 2018-02-09.
* **24.01.18:** - Bump server version 2018-01-24.
* **10.01.18:** - Bump server version 2018-01-10.
* **31.11.17:** - Bump server version 2017-12-21.
* **30.11.17:** - Add NPROC variable  to allow number of processes to be set.
* **30.11.17:** - Fix linting recommendations.
* **30.11.17:** - Remove socket on startup if exists (thanks wtf911) [re](https://tickets.metabrainz.org/browse/MBS-9370).
* **24.11.17:** - Remove catalyst side bar on new installs.
* **31.10.17:** - Bump server version 2017-10-31.
* **20.09.17:** - Bump server version 2017-09-18.
* **06.09.17:** - Bump server version 2017-09-04.
* **19.07.17:** - Bump server version 2017-07-17.
* **21.06.17:** - Bump server version 2017-06-19.
* **26.05.17:** - Fix later build of postgres using /run instead of /var/run.
* **26.05.17:** - Rebase to alpine 3.6.
* **15.05.17:** - Schema 24 update, recommend full rebuild with new config.
* **15.04.17:** - Bump server version 2017-04-10.
* **04.04.17:** - Bump server version 2017-03-27.
* **15.03.17:** - Bump server version 2017-03-13.
* **04.03.17:** - Bump server version and use nginx to serve web pages.
* **06.02.17:** - Rebase to alpine 3.5.
* **16.12.16:** - Rebase to alpine linux, entailing almost complete rewrite.
* **14.10.16:** - Add version layer information.
* **30.09.16:** - Fix umask.
* **10.09.16:** - Add layer badges to README.
* **28.08.16:** - Add badges to README, move to main repository.
* **20.07.16:** - Restructure of docker file for clarity, add maxworkers variable in conjunction with starlet, for parallel requests in multi-core setups, thanks to user baoshan.
* **03.06.16:** - Complete rewrite due to schema change. Rebased back to 14.04 direct Using S6 overaly.
* **21.03.16:** - Bump to latest server release.
* **16.03.16:** - Bump to latest server release.
* **26.02.16:** - Bump to latest server release.
* **08.02.16:** - Switch to PPA version for redis.
* **03.01.16:** - Remove d/l of sitemaps file, missing from last 2 db dumps, move fetch of db/dump higher up initialise routine to allow easier resume of broken downloads.
* **15.12.15:** - Per latest musicbrainz blog, switched to production branch,latest stable code is now production branch in place of master.
* **10.12.15:** - Initial release date.
