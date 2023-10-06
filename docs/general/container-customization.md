# Customizing LinuxServer Containers

One of the challenges we face as an organization is making everyone happy with the functionality we provide for the software we package in Docker containers. As the projects that we package and distribute grow, conventionally so do the use cases along with large communities of power users. As it has become very difficult for us to support Swiss Army Knife style images we are looking to the community of users to start customizing our base image layer themselves.

Something we provide and pride ourselves on is keeping our containers up to date with not only the latest external software releases, but also with the latest distribution level packages. Conventionally when people needed some form of custom functionality they would fork our source and build something once that suited their needs leaving this dangling fork without updates or basic maintenance.

Behind the scenes we have been working to provide the community with the ability to customize our images not only for themselves but also for other users. This comes in the form of 3 different tools:

- [**Private Custom Scripts**](#custom-scripts): Run once when the container is started before services (including the main service/app) are started
- [**Private Custom Services**](#custom-services): Run at the same time as other services. Service get restarted on exit
- **Public Facing [Docker Mods](https://github.com/linuxserver/docker-mods)**: Provide extensions to the containers filesystem. Scripts/services can be implemented as s6 services

All of the functionality described in this post is live on every one of the containers we currently maintain:

<https://fleet.linuxserver.io>

**NOTE:** While the following support has been added to our containers, we will not give support to any custom scripts, services, or mods. If you are having an issue with one of our containers, be sure to disable all custom scripts/services/mods before seeking support.

## Custom Scripts

The first part of this update is the support for a user's custom scripts to run at startup. In every container, simply create a new folder located at `/custom-cont-init.d` and add any scripts you want. These scripts can contain logic for installing packages, copying over custom files to other locations, or installing plugins.

Because this location is outside of `/config` you will need to mount it like any other volume if you wish to make use of it. e.g. `-v /home/foo/appdata/my-custom-files:/custom-cont-init.d` if using the Docker CLI or

```yaml
services:
  bar:
    volumes:
      - /home/foo/appdata/bar:/config
      - /home/foo/appdata/my-custom-files:/custom-cont-init.d:ro
```

if using compose. Where possible, to improve security, we recommend mounting them read-only (`:ro`) so that container processes cannot write to the location.

One example use case is our Piwigo container has a plugin that supports video, but requires ffmpeg to be installed. No problem. Add this bad boy into a script file (can be named anything) and you're good to go.

```shell
#!/bin/bash

echo "**** installing ffmpeg ****"
apk add --no-cache ffmpeg
```

**NOTE:** The folder `/custom-cont-init.d` needs to be owned by root! If this is not the case, this folder will be renamed and a new (empty) folder will be created. This is to prevent remote code execution by putting scripts in the aforementioned folder.

## Custom Services

There might also be a need to run an additional service in a container alongside what we already package. Similarly to the custom scripts, just create a new directory at `/custom-services.d`. The files in this directory should be named after the service they will be running. Similar to with custom scripts you will need to mount this folder like any other volume if you wish to make use of it. e.g. `-v /home/foo/appdata/my-custom-services:/custom-services.d` if using the Docker CLI or

```yaml
services:
  bar:
    volumes:
      - /home/foo/appdata/bar:/config
      - /home/foo/appdata/my-custom-services:/custom-services.d:ro
```

if using compose. Where possible, to improve security, we recommend mounting them read-only (`:ro`) so that container processes cannot write to the location.

Running cron in our containers is now as simple as a single file. Drop this script in `/custom-services.d/cron` and it will run automatically in the container:

```shell
#!/usr/bin/with-contenv bash

/usr/sbin/crond -f -S -l 0 -c /etc/crontabs
```

**NOTE:** With this example, you will most likely need to have cron installed via a custom script using the technique in the previous section, and will need to populate the crontab.

**NOTE:** The folder `/custom-services.d` needs to be owned by root! If this is not the case, this folder will be renamed and a new (empty) folder will be created. This is to prevent remote code execution by putting scripts in the aforementioned folder.

## Docker Mods

In most cases if you needed to write some kind of custom logic to get a plugin to work or to use some kind of popular external service you will not be the only one that finds this logic useful.

If you would like to publish and support your hard work we provide a system for a user to pass a single environment variable to the container to ingest your custom modifications.

We consume Mods from Dockerhub and in order to publish one following our guide, you only need a Github Account and a Dockerhub account. [(Our guide and example code can be found here)](https://github.com/linuxserver/docker-mods)

Essentially it is a system that stashes a tarball of scripts and any other files you need in an image layer on Dockerhub. When we spin up the container we will download this tarball and extract it to /.

This allows community members to publish a relatively static pile of logic that will always be applied to an end user's up to date Linuxserver.io container.

An example of how this logic can be used to greatly expand the functionality of our base containers would be to add VPN support to a Transmission container:

```shell
docker create \
  --name=transmission \
  --cap-add=NET_ADMIN \
  -e PUID=1000 \
  -e PGID=1000 \
  -e DOCKER_MODS=taisun/config-mods:pia \
  -e PIAUSER=pmyuser \
  -e PIAPASS=mypassword \
  -e PIAENDPOINT="US New York City" \
  -e TZ=US/Eastern \
  -p 9091:9091 \
  -p 51413:51413 \
  -p 51413:51413/udp \
  -v path to data:/config \
  -v path to downloads:/downloads \
  -v path to watch folder:/watch \
  --restart unless-stopped \
  linuxserver/transmission
```

The source code for this mod can be found [here](https://github.com/Taisun-Docker/config-mods/tree/master/pia).

**NOTE:** When pulling in logic from external sources practice caution and trust the sources/community you get them from, as there are extreme security implications to consuming files from sources outside of our control.

## We are here to help

If you are interested in writing custom logic and possibly sharing it with the community in the form of a [Docker Mod](https://github.com/linuxserver/docker-mods) we are always available to help you out.

Our [Discord server](https://discord.gg/YWrKVTn) is best for quick direct contact and our [Forum](https://discourse.linuxserver.io/) for a longer running project.

There is zero barrier to entry for these levels of container customization and you are in complete control.

We are looking forward to your next creation.
