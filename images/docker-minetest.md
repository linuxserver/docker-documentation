[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: http://www.minetest.net/
[hub]: https://hub.docker.com/r/linuxserver/minetest/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# linuxserver/minetest
[![](https://images.microbadger.com/badges/version/linuxserver/minetest.svg)](https://microbadger.com/images/linuxserver/minetest "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/linuxserver/minetest.svg)](https://microbadger.com/images/linuxserver/minetest "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/minetest.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/linuxserver/minetest.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/x86-64/x86-64-minetest)](https://ci.linuxserver.io/job/Docker-Builders/job/x86-64/job/x86-64-minetest/)

[Minetest][appurl] (server) is a near-infinite-world block sandbox game and a game engine, inspired by InfiniMiner, Minecraft, and the like.

[![minetest](https://raw.githubusercontent.com/linuxserver/beta-templates/master/lsiodev/img/minetest-icon.png)][appurl]

## Usage

```
docker create \
  --name=minetest \
  -v <path to data>:/config/.minetest \
  -e PGID=<gid> -e PUID=<uid>  \
  -p 30000:30000/udp
  linuxserver/minetest
```

## Tags
Client and server must be the same version and to allow this you can choose one of the following tags in the following format

linuxserver/minetest:0.4.16

+ **0.4.13**
+ **0.4.14**
+ **0.4.15**
+ **0.4.16**

The default aka :latest builds whatever is the latest release at build time, from here. https://github.com/minetest/minetest/releases


## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side.
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`



* `-p 30000/udp` - the port(s)
* `-v /config/.minetest` - where minetest stores config files and maps etc.
* `-e PGID` for GroupID - see below for explanation
* `-e PUID` for UserID - see below for explanation

It is based on alpine linux with s6 overlay, for shell access whilst the container is running do `docker exec -it minetest /bin/bash`.

### User / Group Identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" ™.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Setting up the application

You can find the world maps, mods folder and config files in /config/.minetest.

## Info

* Shell access whilst the container is running: `docker exec -it minetest /bin/bash`
* To monitor the logs of the container in realtime: `docker logs -f minetest`

* container version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' minetest`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/minetest`

## Versions

+ **14.01.19:** Add pipeline logic and multi arch.
+ **08.08.18:** Rebase to alpine 3.8, build from latest release tag instead of master.
+ **03.01.18:** Deprecate cpu_core routine lack of scaling.
+ **08.12.17:** Rebase to alpine 3.7.
+ **30.11.17:** Use cpu core counting routine to speed up build time.
+ **26.05.17:** Rebase to alpine 3.6.
+ **14.02.17:** Rebase to alpine 3.5.
+ **25.11.16:** Rebase to alpine linux, move to main repo.
+ **27.02.16:** Bump to latest version.
+ **19.02.16:** Change port to UDP, thanks to slashopt for pointing this out.
+ **15.02.16:** Make minetest app a service.
+ **01.02.16:** Add lua-socket dependency.
+ **06.11.15:** Initial Release.
