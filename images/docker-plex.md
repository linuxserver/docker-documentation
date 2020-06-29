# linuxserver/plex

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-plex.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-plex) [![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-plex.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-plex/releases) [![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-plex/packages) [![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-plex/container_registry) [![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/plex.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/plex) [![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/plex.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/plex) [![Docker Stars](https://img.shields.io/docker/stars/linuxserver/plex.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/plex) [![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-plex%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-plex/job/master/) [![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fplex%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/plex/latest/index.html)

[Plex](https://plex.tv) organizes video, music and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone Plex Media Server. has always been a top priority. Straightforward design and bulk actions mean getting things done faster.

## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/plex` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=plex \
  --net=host \
  -e PUID=1000 \
  -e PGID=1000 \
  -e VERSION=docker \
  -e UMASK_SET=022 `#optional` \
  -e PLEX_CLAIM= `#optional` \
  -v /path/to/library:/config \
  -v /path/to/tvseries:/tv \
  -v /path/to/movies:/movies \
  --restart unless-stopped \
  linuxserver/plex
```

### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  plex:
    image: linuxserver/plex
    container_name: plex
    network_mode: host
    environment:
      - PUID=1000
      - PGID=1000
      - VERSION=docker
      - UMASK_SET=022 #optional
      - PLEX_CLAIM= #optional
    volumes:
      - /path/to/library:/config
      - /path/to/tvseries:/tv
      - /path/to/movies:/movies
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime \(such as those above\). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports \(`-p`\)

| Parameter | Function |
| :---: | :--- |


#### Networking \(`--net`\)

| Parameter | Function |
| :---: | :--- |
| `--net=host` | Use Host Networking |

### Environment Variables \(`-e`\)

| Env | Function |
| :---: | :--- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `VERSION=docker` | Set whether to update plex or not - see Application Setup section. |
| `UMASK_SET=022` | control permissions of files and directories created by Plex |
| `PLEX_CLAIM=` | Optionally you can obtain a claim token from [https://plex.tv/claim](https://plex.tv/claim) and input here. Keep in mind that the claim tokens expire within 4 minutes. |

### Volume Mappings \(`-v`\)

| Volume | Function |
| :---: | :--- |
| `/config` | Plex library location. _This can grow very large, 50gb+ is likely for a large collection._ |
| `/tv` | Media goes here. Add as many as needed e.g. `/movies`, `/tv`, etc. |
| `/movies` | Media goes here. Add as many as needed e.g. `/movies`, `/tv`, etc. |

## Environment variables from files \(Docker secrets\)

You can set any environment variable from a file by using a special prepend `FILE__`.

As an example:

```text
-e FILE__PASSWORD=/run/secrets/mysecretpassword
```

Will set the environment variable `PASSWORD` based on the contents of the `/run/secrets/mysecretpassword` file.

## Umask for running applications

For all of our images we provide the ability to override the default umask settings for services started within the containers using the optional `-e UMASK=022` setting. Keep in mind umask is not chmod it subtracts from permissions based on it's value it does not add. Please read up [here](https://en.wikipedia.org/wiki/Umask) before asking for support.

## Optional Parameters

If you want to run the container in bridge network mode \(instead of the recommended host network mode\) you will need to specify ports. The [official documentation for ports](https://support.plex.tv/articles/201543147-what-network-ports-do-i-need-to-allow-through-my-firewall/) lists 32400 as the only required port. The rest of the ports are optionally used for specific purposes listed in the documentation. If you have not already claimed your server \(first time setup\) you need to set `PLEX_CLAIM` to claim a server set up with bridge networking.

```text
  -p 32400:32400 \
  -p 1900:1900/udp \
  -p 3005:3005 \
  -p 5353:5353/udp \
  -p 8324:8324 \
  -p 32410:32410/udp \
  -p 32412:32412/udp \
  -p 32413:32413/udp \
  -p 32414:32414/udp \
  -p 32469:32469
```

The application accepts a series of environment variables to further customize itself on boot:

| Parameter | Function |
| :---: | :--- |
| `--device=/dev/dri:/dev/dri` | Add this option to your run command if you plan on using Quicksync hardware acceleration - see Application Setup section. |
| `--device=/dev/dvb:/dev/dvb` | Add this option to your run command if you plan on using dvb devices. |

## User / Group Identifiers

When using volumes \(`-v` flags\), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```text
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

Webui can be found at `<your-ip>:32400/web`

 **Note about updates, if there is no value set for the VERSION variable, then no updates will take place.**

 **For new users, no updates will take place on the first run of the container as there is no preferences file to read your token from, to update restart the Docker container after logging in through the webui**

Valid settings for VERSION are:-

`IMPORTANT NOTE:- YOU CANNOT UPDATE TO A PLEXPASS ONLY (BETA) VERSION IF YOU ARE NOT LOGGED IN WITH A PLEXPASS ACCOUNT`

* **`docker`**: Let Docker handle the Plex Version, we keep our Dockerhub Endpoint up to date with the latest public builds. This is the same as leaving this setting out of your create command.
* **`latest`**: will update plex to the latest version available that you are entitled to.
* **`public`**: will update plexpass users to the latest public version, useful for plexpass users that don't want to be on the bleeding edge but still want the latest public updates.
* **`<specific-version>`**: will select a specific version \(eg 0.9.12.4.1192-9a47d21\) of plex to install, note you cannot use this to access plexpass versions if you do not have plexpass.

## Hardware Acceleration

### Intel

Hardware acceleration users for Intel Quicksync will need to mount their /dev/dri video device inside of the container by passing the following command when running or creating the container:

`--device=/dev/dri:/dev/dri`

We will automatically ensure the abc user inside of the container has the proper permissions to access this device.

### Nvidia

Hardware acceleration users for Nvidia will need to install the container runtime provided by Nvidia on their host, instructions can be found here:

[https://github.com/NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker)

We automatically add the necessary environment variable that will utilise all the features available on a GPU on the host. Once nvidia-docker is installed on your host you will need to re/create the docker container with the nvidia container runtime `--runtime=nvidia` and add an environment variable `-e NVIDIA_VISIBLE_DEVICES=all` \(can also be set to a specific gpu's UUID, this can be discovered by running `nvidia-smi --query-gpu=gpu_name,gpu_uuid --format=csv` \). NVIDIA automatically mounts the GPU and drivers from your host into the plex docker.

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27plex%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=plex)

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image \(if any\) can be accessed via the dynamic badge above.

## Support Info

* Shell access whilst the container is running:
  * `docker exec -it plex /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f plex`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' plex`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/plex`

## Versions

* **03.05.20:** - Update exposed ports and example docs for bridge mode.
* **23.03.20:** - Remove udev hack \(no longer needed\), suppress uuid error in log during first start.
* **04.12.19:** - Add variable for setting PLEX\_CLAIM. Remove `/transcode` volume mapping as it is now set via plex gui and defaults to a location under `/config`.
* **06.08.19:** - Add variable for setting UMASK.
* **10.07.19:** - Fix permissions for tuner \(/dev/dvb\) devices.
* **20.05.19:** - Bugfix do not allow Root group for Intel QuickSync ownership rules.
* **23.03.19:** - Switching to new Base images, shift to arm32v7 tag.
* **22.03.19:** - Fix update logic for `VERSION=public`.
* **14.03.19:** - Switch to new api endpoints, enable beta \(plex pass\) updates for armhf and aarch64.
* **15.02.19:** - Clean up plex pid after unclean stop.
* **11.02.19:** - Fix nvidia variables, add device variables.
* **16.01.19:** - Add pipeline logic, multi arch, and HW transcoding configuration; remove avahi service.
* **07.09.18:** - Rebase to ubuntu bionic, add udev package.
* **09.12.17:** - Fix continuation lines.
* **12.07.17:** - Add inspect commands to README, move to jenkins build and push.
* **28.05.17:** - Add unrar package as per requests, for subzero plugin.
* **11.01.17:** - Use Plex environment variables from pms docker, change abc home folder to /app to alleviate usermod chowning library
* **03.01.17:** - Use case insensitive version variable matching rather than export and make lowercase.
* **17.10.16:** - Allow use of uppercase version variable
* **01.10.16:** - Add TZ info to README.
* **09.09.16:** - Add layer badges to README.
* **27.08.16:** - Add badges to README.
* **22.08.16:** - Rebased to xenial and s6 overlay
* **07.04.16:** - removed `/transcode` volume support \(upstream Plex change\) and modified PlexPass download method to prevent unauthorised usage of paid PMS
* **24.09.15:** - added optional support for volume transcoding \(/transcode\), and various typo fixes.
* **17.09.15:** - Changed to run chmod only once
* **19.09.15:** - Plex updated their download servers from http to https
* **28.08.15:** - Removed plexpass from routine, and now uses VERSION as a combination fix.
* **18.07.15:** - Moved autoupdate to be hosted by linuxserver.io and implemented bugfix thanks to ljm42.
* **09.07.15:** - Now with ability to pick static version number.
* **08.07.15:** - Now with autoupdates. \(Hosted by fanart.tv\)
* **03.07.15:** - Fixed a mistake that allowed plex to run as user plex rather than abc \(99:100\). Thanks to double16 for spotting this.

