[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: http://shout-irc.com/
[hub]: https://hub.docker.com/r/lsiocommunity/shout-irc/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# lsiocommunity/shout-irc
[![](https://images.microbadger.com/badges/version/lsiocommunity/shout-irc.svg)](https://microbadger.com/images/lsiocommunity/shout-irc "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/lsiocommunity/shout-irc.svg)](http://microbadger.com/images/lsiocommunity/shout-irc "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/lsiocommunity/shout-irc.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/lsiocommunity/shout-irc.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/lsiocommunity/x86-64-shout-irc)](https://ci.linuxserver.io/job/Docker-Builders/job/lsiocommunity/job/x86-64-shout-irc/)

shoutIRC is a web IRC client that you host on your own server.

__What features does it have?__
- Multiple user support
- Stays connected even when you close the browser
- Connect from multiple devices at once
- Responsive layout — works well on your smartphone
- _.. and more!_

[![shoutirc](https://raw.githubusercontent.com/linuxserver/community-templates/master/lsiocommunity/img/shout-icon.png)][appurl]

## Usage

```
docker create \
  --name=shout \
  -v <path to data>:/config \
  -e PGID=<gid> -e PUID=<uid>  \
  -e TZ=<timezone> \
  -p 9000:9000 \
  lsiocommunity/shout-irc
```

## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side.
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`


* `-p 9000` - the port(s)
* `-v /config` -
* `-e PGID` for GroupID - see below for explanation
* `-e PUID` for UserID - see below for explanation
* `-e TZ` for timezone information, eg Europe/London

It is based on alpine linux with s6 overlay, for shell access whilst the container is running do `docker exec -it shout /bin/bash`.

### User / Group Identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" ™.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Setting up the application

To log in to the application, browse to https://<hostip>:9000.

To setup user account(s)

+ edit /config/config.json changing the value `public: true,` to `public: false,`  restart the container and enter the following from the command line of the host.

+ `docker exec -it shout shout --home /config add <user>`

+ Enter a password when prompted, refresh your browser.

+ You should now be prompted for a password on the webinterface.

## Info

* Shell access whilst the container is running: `docker exec -it shout /bin/bash`
* To monitor the logs of the container in realtime: `docker logs -f shout`

* container version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' shout`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' lsiocommnunity/shout`


## Versions

+ **28.01.19:** Add pipeline logic and multi arch.
+ **25.08.18:** Rebase to alpine 3.8.
+ **13.12.17:** Rebase to alpine 3.7.
+ **27.05.17:** Rebase to alpine 3.6.
+ **09.02.17:** Rebase to alpine 3.5.
+ **14.10.16:** Add version layer information.
+ **31.08.16:** Rebase to alpine linux, move to lsiocommunity
