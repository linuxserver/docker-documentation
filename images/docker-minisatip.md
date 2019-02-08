[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: https://github.com/catalinii/minisatip
[hub]: https://hub.docker.com/r/linuxserver/minisatip/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# linuxserver/minisatip
[![](https://images.microbadger.com/badges/version/linuxserver/minisatip.svg)](https://microbadger.com/images/linuxserver/minisatip "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/linuxserver/minisatip.svg)](https://microbadger.com/images/linuxserver/minisatip "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/minisatip.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/linuxserver/minisatip.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/x86-64/x86-64-minisatip)](https://ci.linuxserver.io/job/Docker-Builders/job/x86-64/job/x86-64-minisatip/)

[Minisatip][appurl] is a multi-threaded satip server version 1.2 that runs under Linux and it was tested with DVB-S, DVB-S2, DVB-T, DVB-T2, DVB-C, DVB-C2, ATSC and ISDB-T cards.

[![minisatip](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/minisatip-icon.png)][appurl]

## Usage

```
docker create \
--name=minisatip \
-e PGID=<gid> -e PUID=<uid> \
-e TZ=<timezone> \
-e RUN_OPTS=<parameter> \
-p 8875:8875 -p 554:554 \
-p 1900:1900/udp
--device=/dev/dvb \
linuxserver/minisatip
```

## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side.
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`


* `-p 8875` - the port(s)
* `-p 554` - the port(s)
* `-p 1900/udp` - the port(s)
* `-v /config` -
* `-e PGID` for GroupID - see below for explanation
* `-e PUID` for UserID - see below for explanation
* `-e RUN_OPTS` additional runtime parameters - see below for explanation
* `--device=/dev/dvb` - for passing through Tv-cards.
* `-e TZ` for timezone information, eg Europe/London

It is based on alpine with s6 overlay, for shell access whilst the container is running do `docker exec -it minisatip /bin/bash`.

### User / Group Identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" ™.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

### Additional runtime parameters

In some cases it might be necessary to start minisatip with additional parameters, for example to configure a unicable LNB. Add the parameters you need and restart the container. Be sure to have the right parameters set as adding the wrong once might lead to the container not starting correctly.
For a list of minisatip parameters visit [minisatip][appurl] page.

## Setting up the application
Best used in conjunction with [tvheadend](https://github.com/linuxserver/docker-tvheadend)

There is no setup per se, other than adding your cards for passthrough.

You can then use your cards as DVB inputs in apps such as tvheadend.

## Info

* To monitor the logs of the container in realtime `docker logs -f minisatip`.

* container version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' minisatip`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/minisatip`

## Versions

+ **28.08.18:** Rebase to Alpine 3.8.
+ **13.12.17:** Rebase to Alpine 3.7.
+ **28.05.17:** Rebase to Alpine 3.6.
+ **08.02.17:** Rebase to Alpine 3.5 and only compile libs in dvb-apps.
+ **14.10.16:** Add version layer information.
+ **18.09.16:** Add support for Common Interface.
+ **11.09.16:** Add layer badges to README.
+ **28.08.16:** Add badges to README.
+ **15.08.16:** Initial Release.
