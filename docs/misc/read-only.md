# Running Containers Read-Only

!!! warning
    Running containers read-only is an advanced topic and should not be undertaken without a full understanding of everything documented below.

## What?

Docker containers have an internal filesystem, which is shipped as part of the image. Everything you're *not* mounting to the host, or tmpfs (RAM), is part of this filesystem. It operates on the basis of Copy-On-Write, which means that only files which are created or modified are actually written to disk, and these will persist until you destroy or recreate the container, at which point it will revert all changes. Typically the only things written to the container filesystem would be temporary data like pidfiles, lockfiles, sockets, etc. but it can be anything. For example, if you use Docker Mods, we download and extract the mods to the container filesystem at runtime, which is why they have to be redownloaded when you update (and thus recreate) the container. The mods themselves may then make further changes to the filesystem such as installing new packages or changing config files, etc.

If you're curious, you can run `docker diff <container name>` to see which files have been added (A), changed (C), or deleted (D) compared to the filesystem that shipped with the image (note this *won't* show anything in mounted paths).

Docker provides the capability to run containers with a read-only internal filesystem. This prevents any changes from being made to any part of the running container that isn't mounted to your host or tmpfs.

## Why?

From a security perspective, preventing any changes to the container filesystem is a good idea. It means if someone somehow compromises the container they can't install new packages, change permissions, create new user accounts, copy executables, or do anything else persistent outside of your host-mounted paths. Now in the case of the vast majority of our images, if a malicious actor were to compromise the running application they wouldn't have root access anyway, which already limits their ability to act, but if chained with a Local Privilege Escalation (LPE) vulnerability for example, they could acquire it. Running read-only isn't a security silver bullet (they don't exist) but it is an additional mitigation step you can take.

## How?

Creating a container with `--read-only=true` or:

```yaml
services:
  somecontainer:
    image: someimage
    read_only: true
```

Will mount its filesystem as read-only, and that cannot then be changed without recreating it. It's never quite that simple, however.

Our images use s6 as a supervisor and that needs to be able to write its service files to `/run`; many applications expect to be able to write to their working directory, changing UIDs and GIDs requires writing to `/etc/passwd` & `/etc/group`, installing new packages requires writing to numerous locations, and as discussed above, mods need to be extracted to the container filesystem. In short, there are some heavy limitations around read-only operation of our images:

* The PUID & PGID variables will not have any effect, the container will run applications as 911:911, and will apply those permissions to `/config`.
* The UMASK variable will not have any effect
* Docker Mods will not be run
* Custom Services will not be run
* Custom Scripts will be limited in their functionality
* Any application that requires writing to its working directory will be unable to run read-only

In addition, in order to successfully run read-only, you must also mount `/run` to tmpfs with the `exec` flag set. This can be achieved with either `--tmpfs /run:exec` or:

```yaml
services:
  somecontainer:
    image: someimage
    tmpfs:
      - /run:exec
```

For example:

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /path/to/sonarr/data:/config
      - /path/to/tvseries:/tv
      - /path/to/downloadclient-downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
    tmpfs:
      - /run:exec
    read_only: true
```

## Support Policy

Read-only operation of our images is supported on a Reasonable Endeavours basis and *only* for images which we have specifically tested. These images will have their ability to be run read-only noted in the readme, along with any additional caveats. Please see our [Support Policy](https://linuxserver.io/supportpolicy) for more details.
