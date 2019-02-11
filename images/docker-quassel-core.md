[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: http://quassel-irc.org/
[hub]: https://hub.docker.com/r/linuxserver/quassel-core/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# linuxserver/quassel-core
[![](https://images.microbadger.com/badges/version/linuxserver/quassel-core.svg)](https://microbadger.com/images/linuxserver/quassel-core "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/linuxserver/quassel-core.svg)](https://microbadger.com/images/linuxserver/quassel-core "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/quassel-core.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/linuxserver/quassel-core.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/x86-64/x86-64-quassel-core)](https://ci.linuxserver.io/job/Docker-Builders/job/x86-64/job/x86-64-quassel-core/)

[Quassel IRC][appurl] is a modern, cross-platform, distributed IRC client, meaning that one (or multiple) client(s) can attach to and detach from a central core.

This container handles the IRC connection (quasselcore) and requires a desktop client (quasselclient) to be used and configured. It is designed to be always on and will keep your identity present in IRC even when your clients cannot be online. Backlog (history) is downloaded by your client upon reconnection allowing infinite scrollback through time.

[![quassel](http://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Apps-quassel-icon.png)][appurl]

## Usage

```
docker create \
	--name=quassel-core \
	-v /etc/localtime:/etc/localtime:ro \
	-v <path to data>:/config \
	-e PGID=<gid> -e PUID=<uid> \
	-p 4242:4242 \
	linuxserver/quassel-core
```

## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side.
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`


* `-p 4242` - the port quassel-core listens for connections on
* `-v /etc/localtime` for timesync - *optional*
* `-v /config` - database and quassel-core configuration storage
* `-e PGID` for for GroupID - see below for explanation
* `-e PUID` for for UserID - see below for explanation

It is based on alpine linux with s6 overlay, for shell access whilst the container is running do `docker exec -it quassel-core /bin/bash`.

### User / Group Identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" ™.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Setting up the application
Quassel wiki: [quassel](http://bugs.quassel-irc.org/projects/quassel-irc/wiki)

A great place to host a quassel instance is a VPS, such as [DigitalOcean](https://www.digitalocean.com/?refcode=501c48b34b8c). For $5 a month you can have a 24/7 IRC connection and be up and running in under 55 seconds (or so they claim).

Once you have the container running, fire up a quassel desktop client and connect to your new core instance using your droplets public IP address and the port you specified in your `docker run` command *default: 4242*. Create an admin user, select SQLite as your storage backend (Quassel limitation). Setup your real name and nick, then press `Save & Connect`.

You're now connected to IRC. Let's add you to our [IRC](http://www.linuxserver.io/index.php/irc/) `#linuxserver.io` room on Freenode. Click 'File' > 'Networks' > 'Configure Networks' > 'Add' (under Networks section, not Servers) > 'Use preset' > Select 'Freenode' and then configure your identity using the tabs in the 'Network details' section. Once connected to Freenode, click `#join` and enter `#linuxserver.io`. That's it, you're done.

## Info

Monitor the logs of the container in realtime `docker logs -f quassel-core`.

* container version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' quassel-core`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/quassel-core`

## Versions

+ **26.01.19:** Add pipeline logic and multi arch.
+ **08.01.19:** Rebase to Ubuntu Bionic and upgrade to Quassel`0.13.0` See [here.](https://quassel-irc.org/node/134)
+ **30.07.18:** Rebase to alpine:3.8 and use buildstage.
+ **03.01.18:** Deprecate cpu_core routine lack of scaling.
+ **09.12.17:** Rebase to alpine:3.7.
+ **26.11.17:** Use cpu core counting routine to speed up build time.
+ **12.07.17:** Add inspect commands to README, move to jenkins build and push.
+ **27.05.17:** Rebase to alpine:3.6.
+ **13.05.17:** Switch to git source.
+ **28.12.16:** Rebase to alpine:3.5.
+ **23.11.16:** Rebase to alpine:edge.
+ **23.09.16:** Use QT5 dependencies (thanks bauerj).
+ **10.09.16:** Add layer badges to README.
+ **28.08.16:** Add badges to README.
+ **10.08.16:** Rebase to xenial
+ **14.10.15:** Removed the webui, turned out to be to unstable for most usecases.
+ **01.09.15:** Fixed mistake in README
+ **30.07.15:** Switched to internal baseimage, and fixed a bug with updating the webinterface.
+ **06.07.15:** Enabled BLOWFISH encryption and added a (optional) webinterface, for the times you dont have access to your client.
