# [lsiodev/gmail-order-bot](https://github.com/linuxserver/docker-gmail-order-bot)

[![GitHub Stars](https://img.shields.io/github/stars/lsiodev/docker-gmail-order-bot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-gmail-order-bot)
[![GitHub Release](https://img.shields.io/github/release/lsiodev/docker-gmail-order-bot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-gmail-order-bot/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-gmail-order-bot/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/Linuxserver.io/docker-gmail-order-bot/container_registry)
[![MicroBadger Layers](https://img.shields.io/microbadger/layers/lsiodev/gmail-order-bot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge)](https://microbadger.com/images/lsiodev/gmail-order-bot "Get your own version badge on microbadger.com")
[![Docker Pulls](https://img.shields.io/docker/pulls/lsiodev/gmail-order-bot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/lsiodev/gmail-order-bot)
[![Docker Stars](https://img.shields.io/docker/stars/lsiodev/gmail-order-bot.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/lsiodev/gmail-order-bot)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-gmail-order-bot%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-gmail-order-bot/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Flsio-ci.ams3.digitaloceanspaces.com%2Flinuxserver%2Fgmail-order-bot%2Flatest%2Fci-status.yml)](https://lsio-ci.ams3.digitaloceanspaces.com/lsiodev/gmail-order-bot/latest/index.html)

[Gmail-order-bot](https://developers.google.com/gmail/api) - A bot used to leverage a Gmail account as an order messaging service to consume email orders from [Nano Checkout](https://github.com/linuxserver/nano-checkout) and process them using any custom logic you choose.


## Supported Architectures

Our images support multiple architectures such as `x86-64`, `arm64` and `armhf`. We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lsiodev/gmail-order-bot` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

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
  --name=gmail-order-bot \
  -e PUID=1000 \
  -e PGID=1000 \
  -e BOT_NAME=discord \
  -e LOOP_TIME=60 \
  -v /path/to/data:/config \
  --restart unless-stopped \
  lsiodev/gmail-order-bot
```


### docker-compose

Compatible with docker-compose v2 schemas.

```yaml
---
version: "2.1"
services:
  gmail-order-bot:
    image: lsiodev/gmail-order-bot
    container_name: gmail-order-bot
    environment:
      - PUID=1000
      - PGID=1000
      - BOT_NAME=discord
      - LOOP_TIME=60
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
| `BOT_NAME=discord` | On successful order receive send the order payload to this bot (default bots are located in root/defaults/bots) |
| `LOOP_TIME=60` | Time in seconds to reach into gmail and get new messages to process |

### Volume Mappings (`-v`)

| Volume | Function |
| :----: | --- |
| `/config` | Path to gmail tokens and custom/default bots |



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

This container is for developers only! We make pre-defined bots we use in our workflow, but you have to have an underlying understanding of javascript and some basic Docker skills to use it.

The entire basis of this is to act as middleware between your email address receiving orders from https://checkout.linuxserver.io and send them to some external service. The bot will archive any messages that do not come from orders@nanocheckout.com with valid DKIM signatures, so definetly do not use this on a personal account.

The concept behind this bot and using email as a destination for orders is to serve normal users that simply want an email for an order out of the box and provide a free messaging queue akin to something like RabbitMQ for people that want to automate order ingestion. 

By default we include bots we use that will be copied over on first container run, for example a simple discord ping when an order is received with the order details:
```
const Discord = require('discord.js');
const YAML = require('yaml');
const discordtoken = process.env.DISCORD_TOKEN;
const roomid = process.env.DISCORD_ROOM


exports.orderbot = async function(order) {
  return new Promise(resolve => {
    const client = new Discord.Client();
    client.login(discordtoken);
    client.on('ready', async () => {
      delete order.rawpayload
      await client.channels.cache.get(roomid.toString()).send(YAML.stringify(order));
      client.destroy();
      resolve(true)
    })
  });
}
```

This code will be passed an order object containing all the order details parsed from the email message. Here we use custom env variables to set application settings to connect up to and send a message to discord. 

In order to use this bot you will need to perform the following setup steps: 
1. Create a dedicated gmail account to use for https://checkout.linuxserver.io
2. Enable API access to this Gmail account by clicking on `Enable the Gmail API` here https://developers.google.com/gmail/api/quickstart/nodejs
3. Save your credentials.json file from that action to the folder you will be bind mounting as `/config`
4. Run `docker run --rm -it -u $(id -u ${USER}):$(id -g ${USER}) -v /path/to/data:/config --entrypoint /config.sh lsiodev/gmail-order-bot`
5. Go to the URL prompted and enter the key you get from it.
6. Start the container using the run/compose example in this readme.

When the container starts if you are using a custom bot located in `/config/bots` it will install the node modules included in it's package.json, do not use system level node modules this container is Alpine based and it will cause conflicts. 

From there the bot will loop in for your defined timeout and pull in emails and spit out orders to your destination. 


## Docker Mods
[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=mods&query=%24.mods%5B%27gmail-order-bot%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=gmail-order-bot "view available mods for this container.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) can be accessed via the dynamic badge above.


## Support Info

* Shell access whilst the container is running:
  * `docker exec -it gmail-order-bot /bin/bash`
* To monitor the logs of the container in realtime:
  * `docker logs -f gmail-order-bot`
* Container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' gmail-order-bot`
* Image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' lsiodev/gmail-order-bot`

## Versions

* **06.07.20:** - Initial Release.
