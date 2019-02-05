[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: https://github.com/thibaud-rohmer/PhotoShow
[hub]: https://hub.docker.com/r/linuxserver/photoshow/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# linuxserver/photoshow
[![](https://images.microbadger.com/badges/version/linuxserver/photoshow.svg)](https://microbadger.com/images/linuxserver/photoshow "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/linuxserver/photoshow.svg)](https://microbadger.com/images/linuxserver/photoshow "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/photoshow.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/linuxserver/photoshow.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/x86-64/x86-64-photoshow)](https://ci.linuxserver.io/job/Docker-Builders/job/x86-64/job/x86-64-photoshow/)

[Photoshow][appurl] is gallery software at its easiest, it doesn't even require a database.

[![photoshow](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/photoshow-icon.png)][appurl]

## Usage

```
docker create \
--name=photoshow \
-v <path to data>:/config \
-v <path to pictures>:/Pictures:ro \
-v <path to store thumbs>:/Thumbs \
-e PGID=<gid> -e PUID=<uid> \
-e TZ=<timezone> \
-p 80:80 \
linuxserver/photoshow
```

## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side.
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`


* `-p 80` - port for the webui
* `-v /config` - stores config and logs for nginx base
* `-v /Pictures` - your local folder of photos you wish to share
* `-v /Thumbs` - local folder to store thumbnails of your images
* `-e PGID` for GroupID - see below for explanation
* `-e PUID` for UserID - see below for explanation
* `-e TZ` - for timezone information *eg Europe/London, etc*

It is based on alpine linux with s6 overlay, for shell access whilst the container is running do `docker exec -it photoshow /bin/bash`.

### User / Group Identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" ™.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Setting up the application

On first run create an admin account, any folder and its subfolders that you map to /Pictures will be presented as a webgallery. Config settings are persistent and stored as a subfolder of the /Thumbs mapping.


## Info

* To monitor the logs of the container in realtime `docker logs -f photoshow`.


* container version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' photoshow`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/photoshow`

## Versions

+ **16.01.19:** Add pipeline logic and multi arch.
+ **05.09.18:** Rebase to alpine 3.8.
+ **07.01.18:** Rebase to alpine 3.7.
+ **25.05.17:** Rebase to alpine 3.6.
+ **03.05.17:** Use repo pinning to better solve dependencies, use repo version of php7-imagick.
+ **14.02.17:** Rebase to alpine 3.5.
+ **14.10.16:** Add version layer information.
+ **30.09.16:** Rebase to alpine linux.
+ **11.09.16:** Add layer badges to README.
+ **21.08.15:** Use patched keybaord js from fork of photoshow
+ **21.08.15:** Initial Release.
