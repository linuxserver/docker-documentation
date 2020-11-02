# [linuxserver/ipfs](https://github.com/linuxserver/docker-ipfs)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-ipfs.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-ipfs)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-ipfs.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-ipfs/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-ipfs/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-ipfs/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/ipfs.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/linuxserver/ipfs "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/ipfs.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/ipfs)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/ipfs.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/ipfs)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-ipfs%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-ipfs/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Fipfs%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/ipfs/latest/index.html)

[Ipfs](https://ipfs.io/) - A peer-to-peer hypermedia protocol designed to make the web faster, safer, and more open.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `ghcr.io/linuxserver/ipfs` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |


## Usage

Here are some example snippets to help you get started creating a container from this image.

### docker-compose ([recommended](https://docs.linuxserver.io/general/docker-compose))

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  ipfs:
    image: ghcr.io/linuxserver/ipfs
    container_name: ipfs
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /path/to/data:/config
    ports:
      - 80:80
      - 4001:4001
      - 5001:5001
      - 8080:8080
      - 443:443 #optional
    restart: unless-stopped
```

### docker cli

```
docker run -d \
  --name=ipfs \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 80:80 \
  -p 4001:4001 \
  -p 5001:5001 \
  -p 8080:8080 \
  -p 443:443 `#optional` \
  -v /path/to/data:/config \
  --restart unless-stopped \
  ghcr.io/linuxserver/ipfs
```


## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |
| `80` | The port for the IPFS web UI |
| `4001` | Peering port, this is the only port you should expose to the internet |
| `5001` | API port, the clientside webUI needs to be able to talk to this from whatever machine your web browser is on |
| `8080` | Gateway Port, actually serves IPFS content |
| `443` | HTTPS port for web UI |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `TZ=Europe/London` | Specify a timezone to use EG Europe/London |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | IPFS storage and config files/logs |



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

In order to push files beyond your local gateway you have to make sure port 4001 is forwarded to the internet. This is required for IPFS peers to reach in and grab your files so public gateways can serve them.

Access the webui at http://localhost , if not using localhost scroll to the bottom of the page and set the API Address setting to IE http://192.168.1.10:5001 , from there you can upload and manage files you push to IPFS. Your gateway to access IPFS files is http://localhost:8080/ipfs/YOUR-FILE-HASH-HERE . You can also simply use public IPFS gateways like: 
* Cloudflare - https://cloudflare-ipfs.com/ipfs/YOUR-FILE-HASH-HERE
* IPFS.io - https://ipfs.io/ipfs/YOUR-FILE-HASH-HERE
* Eternum.io - https://ipfs.eternum.io/ipfs/YOUR-FILE-HASH-HERE

Cloudflare is a solid option as they actually edge cache the files on their CDN so even if your node pinning the item goes down for periods of time their cache will last up to a month. 

For more on using IPFS please read the docs [here](https://docs.ipfs.io/)
 


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=ipfs&query=%24.mods%5B%27ipfs%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=ipfs "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it ipfs /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f ipfs`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ipfs`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' ghcr.io/linuxserver/ipfs`

## Versions

* **09.07.19:** - Initial version.
