---
title: nextcloud
---
# [linuxserver/nextcloud](https://github.com/linuxserver/docker-nextcloud)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-nextcloud.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-nextcloud)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-nextcloud.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-nextcloud/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-nextcloud/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-nextcloud/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/nextcloud.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/nextcloud "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/nextcloud.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/nextcloud)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/nextcloud.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/nextcloud)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-nextcloud%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-nextcloud/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fnextcloud%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/nextcloud/latest/index.html)

[Nextcloud](https://nextcloud.com/) gives you access to all your files wherever you are.

Where are your photos and documents? With Nextcloud you pick a server of your choice, at home, in a data center or at a provider. And that is where your files will be. Nextcloud runs on that server, protecting your data and giving you access from your desktop or mobile devices. Through Nextcloud you also access, sync and share your existing data on that FTP drive at the office, a Dropbox or a NAS you have at home.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `ghcr.io/linuxserver/nextcloud` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :----: | --- |
| latest | Stable Nextcloud releases (currently php7) |
| php8 | Experimental php8 based Nextcloud releases |

## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker-compose ([recommended](https://docs.linuxserver.io/general/docker-compose))

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  nextcloud:
    image: ghcr.io/linuxserver/nextcloud
    container_name: nextcloud
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /path/to/appdata:/config
      - /path/to/data:/data
    ports:
      - 443:443
    restart: unless-stopped
```

### docker cli

```
docker run -d \
  --name=nextcloud \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 443:443 \
  -v /path/to/appdata:/config \
  -v /path/to/data:/data \
  --restart unless-stopped \
  ghcr.io/linuxserver/nextcloud
```


## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `443` | WebUI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Nextcloud configs. |
| `/data` | Your personal data. |



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

Access the webui at `https://<your-ip>:443`, for more information check out [Nextcloud](https://nextcloud.com/).

Docker image update and recreation of container alone won't update nextcloud version. 

In order to update nextcloud version, you have two options, firstly make sure you are using the latest docker image,then either 

1.  Perform the in app gui update. 
2.  Use the CLI version by running `docker exec -it nextcloud updater.phar`
 (Both of these are described [here](https://docs.nextcloud.com/server/latest/admin_manual/maintenance/update.html))

Note:  Both `occ` and `updater.phar` can be run without prepending with `sudo -u abc php` or `sudo -u www-data php`

If you are not customizing our default nginx configuration you will need to remove the file:
```
/config/nginx/site-confs/default
```
Then restart the container to replace it with the latest one. 

### Collaborative Editing

Nextcloud's built-in collaborative editing packages (Collabora/CODE and OnlyOffice) only work on x86_64 systems with glibc, and therefore they are not compatible with our images. You should create separate containers for them and set them up in Nextcloud with their respective connector addons.

If (auto) installed, those built-in packages may cause instability and should be removed.


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=nextcloud&query=%24.mods%5B%27nextcloud%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=nextcloud "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it nextcloud /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f nextcloud`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' nextcloud`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ghcr.io/linuxserver/nextcloud`

## Versions

* **21.03.21:** - Publish `php8` tag for testing.
* **25.02.21:** - Nginx default site config updated for v21 (existing users should delete `/config/nginx/site-confs/default` and restart the container).
* **21.01.21:** - Fix php iconv (was breaking the mail addon). If installed, attempt to remove broken CODE Server app during startup.
* **20.01.21:** - Increase php fcgi timeout to prevent 504 Gateway timeout errors (existing users should delete `/config/nginx/site-confs/default` and restart the container).
* **16.01.21:** - Rebasing to alpine 3.13. Users with issues on 32-bit arm, [see this article](https://docs.linuxserver.io/faq#my-host-is-incompatible-with-images-based-on-ubuntu-focal-and-alpine-3-13).
* **12.08.20:** - Various updates to default site config, including added support for webfinger (existing users should delete `/config/nginx/site-confs/default` and restart the container).
* **03.06.20:** - Rebasing to alpine 3.12
* **03.06.20:** - Add php7-bcmath and php7-fileinfo
* **31.05.20:** - Add aliases for occ and updater.phar
* **31.03.20:** - Allow crontab to be user customized, fix logrotate.
* **17.01.20:** - Updated php.ini defaults and site config, including an optional HSTS directive (existing users should delete `/config/nginx/site-confs/default` and restart the container).
* **19.12.19:** - Rebasing to alpine 3.11.
* **18.11.19:** - Nginx default site config updated for v17 (existing users should delete `/config/nginx/site-confs/default` and restart the container).
* **28.10.19:** - Change cronjob to run every 5 minutes.
* **24.10.19:** - Nginx default site config updated due to CVE-2019-11043 (existing users should delete `/config/nginx/site-confs/default` and restart the container).
* **14.07.19:** - Download nextcloud during build time.
* **28.06.19:** - Rebasing to alpine 3.10.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **27.02.19:** - Updating base nginx config to sync up with v15 requirements.
* **22.02.19:** - Rebasing to alpine 3.9.
* **28.01.19:** - Add pipeline logic and multi arch.
* **25.01.19:** - Add php7-phar for occ upgrades.
* **05.09.18:** - Rebase to alpine 3.8.
* **11.06.18:** - Use latest rather than specific version for initial install.
* **26.04.18:** - Bump default install to 13.0.1.
* **06.02.18:** - Bump default install to 13.0.0.
* **26.01.18:** - Rebase to alpine 3.7, bump default install to 12.0.5.
* **12.12.17:** - Bump default install to 12.0.4, fix continuation lines.
* **15.10.17:** - Sed php.ini for opcache requirements in newer nextcloud versions.
* **20.09.17:** - Bump default install to 12.0.3.
* **19.08.17:** - Bump default install to 12.0.2.
* **25.05.17:** - Rebase to alpine 3.6.
* **22.05.17:** - Update to nextcloud 12.0, adding required dependecies and note about commenting out SAMEORIGIN; line.
* **03.05.17:** - Use community repo of memcache.
* **07.03.17:** - Release into main repository and upgrade to php7 and Alpine 3.5.
