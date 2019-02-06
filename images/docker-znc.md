[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: http://wiki.znc.in/ZNC
[hub]: https://hub.docker.com/r/linuxserver/znc/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# linuxserver/znc
[![](https://images.microbadger.com/badges/version/linuxserver/znc.svg)](https://microbadger.com/images/linuxserver/znc "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/linuxserver/znc.svg)](https://microbadger.com/images/linuxserver/znc "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/znc.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/linuxserver/znc.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/x86-64/x86-64-znc)](https://ci.linuxserver.io/job/Docker-Builders/job/x86-64/job/x86-64-znc/)

[ZNC][appurl] is an IRC network bouncer or BNC. It can detach the client from the actual IRC server, and also from selected channels. Multiple clients from different locations can connect to a single ZNC account simultaneously and therefore appear under the same nickname on IRC.

[![znc](http://wiki.znc.in/resources/assets/wiki.png)][appurl]

## Usage

```
docker create \
  --name=znc \
  -v <path to data>:/config \
  -e PGID=<gid> -e PUID=<uid>  \
  -e TZ=<timezone> \
  -p 6501:6501 \
  linuxserver/znc
```

## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side.
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`


* `-p 6501` - the port(s)
* `-v /config` -
* `-e PGID` for GroupID - see below for explanation
* `-e PUID` for UserID - see below for explanation
* `-e TZ` for timezone EG. Europe/London

It is based on alpine linux with s6 overlay, for shell access whilst the container is running do `docker exec -it znc /bin/bash`.


### User / Group Identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" ™.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Setting up the application

To log in to the application, browse to https://<hostip>:6501.

* Default User: admin
* Default Password: admin
`change password ASAP.`

## Info

* Shell access whilst the container is running: `docker exec -it znc /bin/bash`
* To monitor the logs of the container in realtime: `docker logs -f znc`


* container version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' znc`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/znc`

## Versions

+ **31.01.19:** Add pipeline logic and multi arch.
+ **30.01.19:** Add push and clientbuffer modules.
+ **17.08.18:** Rebase to alpine 3.8, use buildstage.
+ **03.01.18:** Deprecate cpu_core routine lack of scaling.
+ **07.12.17:** Rebase alpine linux 3.7.
+ **25.10.17:** Remove debug switch from run command.
+ **26.05.17:** Rebase alpine linux 3.6.
+ **06.02.17:** Rebase alpine linux 3.5.
+ **19.01.17:** Add playback module.
+ **07.01.17:** Add ca-certificates package, resolve sasl issues.
+ **07.12.16:** Use scanelf to determine runtime dependencies.
fix error with `\` instead of `&&\`.
+ **14.10.16:** Add version layer information.
+ **30.09.16:** Fix umask.
+ **11.09.16:** Add layer badges to README.
+ **28.08.16:** Add badges to README.
+ **20.08.16:** Rebase to alpine linux,
move to main repository.
+ **11.12.15:** Initial Release.
