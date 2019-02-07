[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: http://booksonic.org
[hub]: https://hub.docker.com/r/linuxserver/booksonic/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# linuxserver/booksonic
[![](https://images.microbadger.com/badges/version/linuxserver/booksonic.svg)](https://microbadger.com/images/linuxserver/booksonic "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/linuxserver/booksonic.svg)](https://microbadger.com/images/linuxserver/booksonic "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/booksonic.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/linuxserver/booksonic.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/x86-64/x86-64-booksonic)](https://ci.linuxserver.io/job/Docker-Builders/job/x86-64/job/x86-64-booksonic/)

[Booksonic][appurl] is a server and an app for streaming your audiobooks to any pc or android phone. Most of the functionality is also availiable on other platforms that have apps for subsonic.

[![booksonic](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/booksonic.png)][appurl]

## Usage

```
docker create \
  --name=booksonic \
-v </path/to/config>:/config \
-v </path/to/audiobooks>:/books \
-v </path/to/podcasts>:/podcasts \
-v </path/to/other media>:/media \
-e PGID=<gid> -e PUID=<uid> \
-e CONTEXT_PATH=<url-base> \
-e TZ=<timezone> \
-p 4040:4040 \
  linuxserver/booksonic
```

## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side.
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`



* `-p 4040` - the port(s)
* `-v /config` - Configuration file location
* `-v /books` - Location of audiobooks.
* `-v /podcasts` - Location of podcasts.
* `-v /media` - Location of other media - *optional*
* `-e PGID` for for GroupID - see below for explanation - *optional*
* `-e PUID` for for UserID - see below for explanation - *optional*
* `-e CONTEXT_PATH` for setting url-base in reverse proxy setups - *optional*
* `-e TZ` for setting timezone information, eg Europe/London

It is based on ubuntu bionic with s6 overlay, for shell access whilst the container is running do `docker exec -it booksonic /bin/bash`.

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

* Shell access whilst the container is running: `docker exec -it booksonic /bin/bash`
* To monitor the logs of the container in realtime: `docker logs -f booksonic`

* container version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' booksonic`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/booksonic`

## Versions

+ **16.01.19:** Adding pipeline logic and multi arch.
+ **05.01.19:** Linting fixes.
+ **27.08.18:** Rebase to ubuntu bionic.
+ **06.12.17:** Rebase to alpine 3.7.
+ **11.07.17:** Rebase to alpine 3.6.
+ **07.02.17:** Rebase to alpine 3.5.
+ **13.12.16:** Initial Release.
