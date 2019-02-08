[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: https://github.com/Libresonic/libresonic
[hub]: https://hub.docker.com/r/linuxserver/libresonic/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# linuxserver/libresonic
[![](https://images.microbadger.com/badges/version/linuxserver/libresonic.svg)](https://microbadger.com/images/linuxserver/libresonic "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/linuxserver/libresonic.svg)](https://microbadger.com/images/linuxserver/libresonic "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/libresonic.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/linuxserver/libresonic.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/x86-64/x86-64-libresonic)](https://ci.linuxserver.io/job/Docker-Builders/job/x86-64/job/x86-64-libresonic/)

[Libresonic][appurl] is a free, web-based media streamer, providing ubiqutious access to your music. Use it to share your music with friends, or to listen to your own music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room.

[![libresonic](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/libresonic.png)][appurl]

## Usage

```
docker create \
--name="libresonic" \
-v </path/to/config>:/config \
-v </path/to/music>:/music \
-v </path/to/playlists>:/playlists \
-v </path/to/podcasts>:/podcasts \
-v </path/to/other media>:/media \
-e PGID=<gid> -e PUID=<uid> \
-e CONTEXT_PATH=<url-base> \
-e TZ=<timezone> \
-p 4040:4040 \
linuxserver/libresonic
```

## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side.
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`


* `-p 4040` - the port(s)
* `-v /config` - Configuration file location
* `-v /music` - Location of music.
* `-v /playlists` - Location for playlists to be saved to.
* `-v /podcasts` - Location of podcasts.
* `-v /media` - Location of other media - *optional*
* `-e PGID` for for GroupID - see below for explanation - *optional*
* `-e PUID` for for UserID - see below for explanation - *optional*
* `-e CONTEXT_PATH` for setting url-base in reverse proxy setups - *optional*
* `-e TZ` for setting timezone information, eg Europe/London

It is based on ubuntu bionic  with s6 overlay, for shell access whilst the container is running do `docker exec -it libresonic /bin/bash`.

### User / Group Identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" ™.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Setting up the application

Access WebUI at `<your-ip>:4040`.

Default user/pass is admin/admin

## Info

* To monitor the logs of the container in realtime `docker logs -f libresonic`.

* container version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' libresonic`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/libresonic`

## Versions

+ **15.01.19:** Pull war from github, adding pipeline multi arch builds.
+ **05.01.19:** Linting fixes.
+ **27.08.18:** Rebase to ubuntu bionic.
+ **12.12.17:** Rebase to alpine 3.7.
+ **11.07.17:** Rebase to alpine 3.6.
+ **12.05.17:** Add annotation timeout (primarily for armhf and lower powered hosts).
+ **08.02.17:** Rebase to alpine 3.5.
+ **04.12.16:** Update jetty runner version.
+ **29.11.16:** Switch to building from release tags following v6.1 stable release.
+ **17.11.16:** Initial Release.
