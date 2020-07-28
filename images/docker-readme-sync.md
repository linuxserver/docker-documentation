[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: www.example.com
[hub]: https://hub.docker.com/r/lsiodev/readme-sync/


[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png?v=4&s=4000)][linuxserverurl]


## Contact information:- 

| Type | Address/Details | 
| :---: | --- |
| Discord | [Discord](https://discord.gg/YWrKVTn) |
| Forum | [Linuserver.io forum][forumurl] |
| IRC | freenode at `#linuxserver.io` more information at:- [IRC][ircurl]
| Podcast | Covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation! [Linuxserver.io Podcast][podcasturl] |


The [LinuxServer.io][linuxserverurl] team brings you another image release featuring :-

 + regular and timely application updates
 + easy user mappings
 + custom base image with s6 overlay
 + weekly base OS updates with common layers across the entire LinuxServer.io ecosystem to minimise space usage, down time and bandwidth
 + security updates

# lsiodev/readme-sync

[![](https://images.microbadger.com/badges/version/lsiodev/readme-sync.svg)](https://microbadger.com/images/lsiodev/readme-sync "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/lsiodev/readme-sync.svg)](https://microbadger.com/images/lsiodev/readme-sync "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/lsiodev/readme-sync.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/lsiodev/readme-sync.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/lsiodev/readme-sync-docker)](https://ci.linuxserver.io/job/Docker-Builders/job/lsiodev/job/readme-sync-docker/)

Utility to copy README.md from a given github.com repository to a given dockerhub.com repository.

&nbsp;

## Usage

```
docker run --rm=true \
    -e DOCKERHUB_USERNAME=<USERNAME> \
    -e DOCKERHUB_PASSWORD=<PASSWORD> \
    -e GIT_REPOSITORY=<GITHUB REPO> \
    -e DOCKER_REPOSITORY=<DOCKERHUB REPO> \
    -e GIT_BRANCH=<GITHUB BRANCH> \
    lsiodev/readme-sync bash -c 'node sync'

```

&nbsp;

## Parameters

The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side. 
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.



| Parameter | Function |
| :---: | --- |
| `-e DOCKERHUB_USERNAME` | your dockerhub username |
| `-e DOCKERHUB_PASSWORD` | your dockerhub password |
| `-e GIT_REPOSITORY` | github repository, i.e. linuxserver/docker-readme-sync |
| `-e DOCKER_REPOSITORY` | dockerhub repository, i.e. lsiodev/docker-readme-sync |
| `-e GIT_BRANCH` | github repository branch, optional (default: master) |

&nbsp;
It is based on alpine and is not meant to run as a service. The sync is performed and the command exits.
&nbsp;

## Versions

|  Date | Changes |
| :---: | --- |
| 28.07.20 |  Rebase to alpine 3.12. |
| 20.08.18 |  Rebase to alpine 3.8. |
| 28.02.18 |  convert repo to use node.js implementation. |
| 17.11.17 |  add github branch support. |
| 16.10.16 |  merge ruby app. |
| 11.10.16 |  Initial development release. |
