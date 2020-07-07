# [lsiodev/nano-discord-bot](https://github.com/linuxserver/docker-nano-discord-bot)

[![GitHub Stars](https://img.shields.io/github/stars/lsiodev/docker-nano-discord-bot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-nano-discord-bot)
[![GitHub Release](https://img.shields.io/github/release/lsiodev/docker-nano-discord-bot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-nano-discord-bot/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-nano-discord-bot/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-nano-discord-bot/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/lsiodev/nano-discord-bot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/lsiodev/nano-discord-bot "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/lsiodev/nano-discord-bot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/lsiodev/nano-discord-bot)
[![Docker Stars](https://img.shields.io/docker/stars/lsiodev/nano-discord-bot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/lsiodev/nano-discord-bot)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-nano-discord-bot%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-nano-discord-bot/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fnano-discord-bot%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/lsiodev/nano-discord-bot/latest/index.html)

[Nano-discord-bot](https://discord.com/developers/docs/intro) - A bot used to hook into a [self hosted Nano RPC endpoint](https://hub.docker.com/r/linuxserver/nano) and discord server to Distribute funds from a faucet account.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lsiodev/nano-discord-bot` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  lsiodev/nano-discord-bot
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  nano-discord-bot:
    image: lsiodev/nano-discord-bot
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

With the proper environment variables passed to this container it will automatically reach out to your Nano RPC server and Discord Server.
More about setting up a hosted Nano network [here](https://hub.docker.com/r/linuxserver/nano) .


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27nano-discord-bot%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=nano-discord-bot "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it nano-discord-bot /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f nano-discord-bot`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' nano-discord-bot`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' lsiodev/nano-discord-bot`

## Versions

* **25.05.20:** - Initial Release.
