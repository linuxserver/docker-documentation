[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: https://github.com/hubbcaps/gazee
[hub]: https://hub.docker.com/r/linuxserver/gazee/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# linuxserver/gazee
[![](https://images.microbadger.com/badges/version/linuxserver/gazee.svg)](https://microbadger.com/images/linuxserver/gazee "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/linuxserver/gazee.svg)](https://microbadger.com/images/linuxserver/gazee "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/gazee.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/linuxserver/gazee.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/x86-64/x86-64-gazee)](https://ci.linuxserver.io/job/Docker-Builders/job/x86-64/job/x86-64-gazee/)

A WebApp Comic Reader for your favorite digital comics. Reach and read your comic library from any web connected device with a modern web browser.

[![gazee](https://raw.githubusercontent.com/hubbcaps/gazee/master/public/images/logos/red/logo-red-yellow.png)][appurl]

## Usage

```
docker create \
  --name=gazee \
  -v <path to data>:/config \
  -v <path to comics>:/comics \
  -v <path to mylar data>:/mylar \
  -v <path to SSL certs>:/certs \
  -e PGID=<gid> -e PUID=<uid>  \
  -p 4242:4242 \
  linuxserver/gazee
```

## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side.
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`



* `-p 4242` - the port(s)
* `-v /config` - Where Gazee should store config files.
* `-v /comics` - Path to comics folder.
* `-v /mylar` - Path to Mylar DB
* `-v /certs` - Where SSL certs should be stored.
* `-e PGID` for GroupID - see below for explanation
* `-e PUID` for UserID - see below for explanation

It is based on alpine linux with s6 overlay, for shell access whilst the container is running do `docker exec -it gazee /bin/bash`.

### User / Group Identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" &trade;.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Setting up the application

Webui can be found at `your-ip:4242`

  Default username and password for the web interface:

  * **Username:** `admin`
  * **Password:** `gazee`

Click the gear icon to go to the settings page.

Change the default admin password or add a new admin and remove the admin user altogether.

Comic path should be set to `/comics`

*Optional* Mylar DB path should be set to `/mylar`

*Optional* path for certificates and keys should be set to `/certs`

After you update the settings, Gazee will restart and begin an intial scan of your comic library.

Happy Reading!

## Info

* Shell access whilst the container is running: `docker exec -it gazee /bin/bash`
* To monitor the logs of the container in realtime: `docker logs -f gazee`

* container version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' gazee`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/gazee`

## Versions

+ **17.08.18:** Rebase to alpine 3.8.
+ **30.12.17:** Ensure version 11 of cherrypy.
+ **07.12.17:** Initial Release.
