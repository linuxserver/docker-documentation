# [linuxserver/nano-discord-bot](https://github.com/linuxserver/docker-nano-discord-bot)

[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-nano-discord-bot.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nano-discord-bot)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-nano-discord-bot.svg?style=flat-square&color=E68523&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nano-discord-bot/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitHub%20Package&logo=github&logoColor=FFFFFF)](https://github.com/linuxserver/docker-nano-discord-bot/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab&logoColor=FFFFFF)](https://gitlab.com/Linuxserver.io/docker-nano-discord-bot/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?style=flat-square&color=E68523&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/nano-discord-bot)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/linuxserver/nano-discord-bot.svg?style=flat-square&color=E68523)](https://microbadger.com/images/linuxserver/nano-discord-bot "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/nano-discord-bot.svg?style=flat-square&color=E68523&label=pulls&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/nano-discord-bot)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/nano-discord-bot.svg?style=flat-square&color=E68523&label=stars&logo=docker&logoColor=FFFFFF)](https://hub.docker.com/r/linuxserver/nano-discord-bot)
[![Build Status](https://ci.linuxserver.io/view/all/job/Docker-Pipeline-Builders/job/docker-nano-discord-bot/job/master/badge/icon?style=flat-square)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-nano-discord-bot/job/master/)
[![](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nano-discord-bot/latest/badge.svg)](https://lsio-ci.ams3.digitaloceanspaces.com/linuxserver/nano-discord-bot/latest/index.html)

[Nano-discord-bot](https://discord.com/developers/docs/intro) - A bot used to hook into a [self hosted Nano RPC endpoint](https://hub.docker.com/r/linuxserver/nano) and discord server to Distribute funds from a faucet account.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `linuxserver/nano-discord-bot` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=nano-discord-bot \
  -e PUID=1000 \
  -e PGID=1000 \
  -e WALLET_URL=https://wallet.linuxserver.io/#/nano.linuxserver.io/ \
  -e RPC_URL=https://nano.linuxserver.io:7077 \
  -e FAUCET_KEY=XXXXXXXXXXXXX \
  -e DISCORD_KEY=XXXXXXXXXXXXX \
  -e FAUCET_AMOUNT="1000" \
  -v /path/to/data:/config \
  --restart unless-stopped \
  linuxserver/nano-discord-bot
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  nano-discord-bot:
    image: linuxserver/nano-discord-bot
    container_name: nano-discord-bot
    environment:
      - PUID=1000
      - PGID=1000
      - WALLET_URL=https://wallet.linuxserver.io/#/nano.linuxserver.io/
      - RPC_URL=https://nano.linuxserver.io:7077
      - FAUCET_KEY=XXXXXXXXXXXXX
      - DISCORD_KEY=XXXXXXXXXXXXX
      - FAUCET_AMOUNT="1000"
    volumes:
      - /path/to/data:/config
    restart: unless-stopped
```

## Parameters

Docker images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

### Ports (`-p`)

| Parameter | Function |
| :----: | --- |


### Environment Variables (`-e`)

| Env | Function |
| :----: | --- |
| `PUID=1000` | for UserID - see below for explanation |
| `PGID=1000` | for GroupID - see below for explanation |
| `WALLET_URL=https://wallet.linuxserver.io/#/nano.linuxserver.io/` | Hosted wallet endpoint to use. |
| `RPC_URL=https://nano.linuxserver.io:7077` | RPC endpoint to publish blocks to and ingest account information. |
| `FAUCET_KEY=XXXXXXXXXXXXX` | The private key for your faucet account. |
| `DISCORD_KEY=XXXXXXXXXXXXX` | Discord api key for the bot. |
| `FAUCET_AMOUNT="1000"` | Amount to distribute to individual Discord users in Nano. |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Database and Radarr configs |




## User / Group Identifiers

When using volumes (`-v` flags), permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Application Setup

With the proper environment variables passed to this container it will automatically reach out to your Nano RPC server and Discord Server.
More about setting up a hosted Nano network [here](https://hub.docker.com/r/linuxserver/nano) .


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?style=for-the-badge&color=E68523&label=mods&query=%24.mods%5B%27nano-discord-bot%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=nano-discord-bot "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it nano-discord-bot /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f nano-discord-bot`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' nano-discord-bot`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/nano-discord-bot`

## Versions

* **25.05.20:** - Initial Release.
