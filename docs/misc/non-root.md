# Running Containers As A Non-Root User

!!! warning
    Running containers as a non-root user is an advanced topic and should not be undertaken without a full understanding of everything documented below.

## What?

If you run one of our typical images in a standard Docker setup, the container itself will run as `root`. After init we then drop to an unprivileged user, `abc` to run the actual application service(s). We do this because at the time we designed our architecture the alternative - setting a fixed unprivileged user at build time - would have prevented us from offering the range of options that wanted to. While it is now possible to use the `--user` parameter to run any container as an arbitrary user, it hasn't been something we've been able to support before now.

The other approach is to run [Docker itself rootless](https://docs.docker.com/engine/security/rootless/). This creates a separate user and network namespace for your containers that separates them from the host and means that even containers nominally running as `root` don't have root permissions on your host.

## Why?

Some people take the position that a container running as root *at any point* is an unacceptable security risk. Those people typically misunderstand the attack surface of containers and where the risks actually lie. Having said that, there *are* some risks with having containers running as root; generally, a better solution to running every container as an unprivileged user is to run Docker itself rootless, but that's not always desirable. In these situations, being able to run a single container as a unprivileged user has its benefits.

To give you some sense of a potential risk, let's take our SABnzbd image and let's imagine you've exposed it to the internet and for some reason allowed unauthenticated access. Now let's assume a user were to discover a Remote Code Execution vulnerability in SABnzbd, and were able to exploit it to get a shell in the container (not a simple task, but let's be generous). At this point you have a shell running as the unprivileged `abc` account, which heavily limits what you can do. There's no sudo/doas in the container so you'd likely need to chain a Privilege Escalation vulnerability (within the limited set of packages installed) to get root. Even at that point, with root access inside the container, you would then need a further Container Escape vulnerability in order to do anything meaningful to the host beyond simply deleting or modifying data in a mounted path (which you could do as a non-root user anyway). That said, some of our containers do require additional Capabilities to run, and these *could* be exploited by a user with root to affect the host in various ways.

## How?

Creating a container with `--user <uid>:<gid>` or:

```yaml
services:
  somecontainer:
    image: someimage
    user: <uid>:<gid>
```

Will run the container as that user, and that cannot then be changed without recreating it. It's never quite that simple, however.

Our images use s6 as a supervisor and that needs to be able to write its service files to `/run`; many applications expect to be able to write to their working directory, changing UIDs and GIDs requires writing to `/etc/passwd` & `/etc/group`, installing new packages requires writing to numerous locations, and mods need to be extracted to the container filesystem. In short, there are some heavy limitations around operation of our images with a non-root user:

* The PUID & PGID variables will not have any effect, the container will instead run applications with the UID & GID of the user you have specified
* You will need to manually manage the permissions of any mounted volumes or paths
* Docker Mods will not be run
* Custom Services will not be run
* Custom Scripts will be limited in their functionality

For all of these reasons, we recommend you *do not* switch existing container instances to run with a non-root user without careful testing.

For example:

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - TZ=Europe/London
    volumes:
      - /path/to/sonarr/data:/config
      - /path/to/tvseries:/tv
      - /path/to/downloadclient-downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
    user: 1000:1000
```

## Support Policy

Operation of our images with a non-root user is supported on a Reasonable Endeavours basis and *only* for images which we have specifically tested. These images will have their ability to be run with a non-root user noted in the readme, along with any additional caveats. Please see our [Support Policy](https://linuxserver.io/supportpolicy) for more details.
