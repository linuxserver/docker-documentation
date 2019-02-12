[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: https://github.com/rembo10/headphones
[hub]: https://hub.docker.com/r/linuxserver/headphones/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# linuxserver/headphones
[![](https://images.microbadger.com/badges/version/linuxserver/headphones.svg)](https://microbadger.com/images/linuxserver/headphones "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/linuxserver/headphones.svg)](https://microbadger.com/images/linuxserver/headphones "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/headphones.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/linuxserver/headphones.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/x86-64/x86-64-headphones)](https://ci.linuxserver.io/job/Docker-Builders/job/x86-64/job/x86-64-headphones/)

[headphones](https://hub.docker.com/r/linuxserver/headphones/) is an automated music downloader for NZB and Torrent, written in Python. It supports SABnzbd, NZBget, Transmission, µTorrent and Blackhole.

[![headphones](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/headphones-banner.png)][appurl]

## Usage

```
docker create \
    --name="headphones" \
    -v /path/to/headphones/data:/config \
    -v /path/to/downloads:/downloads \
    -v /path/to/music:/music \
    -e PGID=<gid> -e PUID=<uid> \
    -e TZ=<timezone> \
    -p 8181:8181 \
    linuxserver/headphones
```

## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side.
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`


* `-p 8181` - the port(s)
* `-v /config` - Configuration file location
* `-v /music` - Location of music. (i.e. /opt/downloads/music or /var/music)
* `-v /downloads` - Location of downloads folder
* `-e PGID` for for GroupID - see below for explanation - *optional*
* `-e PUID` for for UserID - see below for explanation - *optional*
* `-e TZ` for setting timezone information, eg Europe/London

It is based on alpine linux with s6 overlay, for shell access whilst the container is running do `docker exec -it headphones /bin/bash`.

### User / Group Identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" ™.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Setting up the application

Access WebUI at `<your-ip>:8181` and walk through the wizard.

## Info

* To monitor the logs of the container in realtime `docker logs -f headphones`.

* container version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' headphones`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/headphones`

## Versions

+ **16.01.19:** Add pipeline logic and multi arch.
+ **18.08.18:** Rebase to alpine 3.8.
+ **03.04.18:** Remove forced port and update README.
+ **05.01.18:** Deprecate cpu_core routine lack of scaling.
+ **12.12.17:** Rebase to alpine 3.7.
+ **20.07.17:** Internal git pull instead of at runtime.
+ **12.07.17:** Add inspect commands to README, move to jenkins build and push.
+ **28.05.17:** Add flac package to handle FLAC based .cue.
+ **25.05.17:** Rebase to alpine 3.6.
+ **03.05.17:** Reduce layer, replace broken source for shntool.
+ **07.02.17:** Rebase to alpine 3.5.
+ **23.12.16:** Fix capitalisation in README.
+ **09.09.16:** Add layer badges to README.
+ **27.08.16:** Add badges to README, compile shntool.
+ **08.08.16:** Rebase to alpine linux.
+ **18.07.15:** Inital Release
