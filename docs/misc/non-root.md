# Running Containers As A Non-Root User

!!! warning
    Running containers as a non-root user is an advanced topic and should not be undertaken without a full understanding of everything documented below.

## What?

If you run one of our typical images in a standard Docker setup, the container itself will run as `root`. After init we then drop to an unprivileged user, `abc` to run the actual application service(s). We do this because at the time we designed our architecture the alternative - setting a fixed unprivileged user at build time - would have prevented us from offering the range of options that wanted to. While it is now possible to use the `--user` parameter to run any container as an arbitrary user, it hasn't been something we've been able to support before now.

The other approach is to run [Docker itself rootless](https://docs.docker.com/engine/security/rootless/). This creates a separate user and network namespace for your containers and means that even containers nominally running as `root` don't have root permissions on your host. Running a container as a non-root user and running it rootless are **not** the same, but are commonly conflated.

## Why?

Running containers in rootless mode provides defense in depth: even if a container is fully compromised *and* an attacker manages to escape the container, the attacker will still only be acting as an unprivileged user on the host system.

Like many security enhancements, running some or all of your containers in rootless mode comes with potential usability downsides, which are described below.

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

* The PUID & PGID variables will not have any effect, the container will instead run applications with the UID & GID of the user you have specified via the `--user` parameter
* You will need to manually manage the permissions of any mounted volumes or paths
* Docker Mods will not be run
* Custom Services will not be run
* Custom Scripts will be limited in their functionality
* You cannot set `no-new-privileges=true` unless you additionally set permissions on /run to match your `user` UID and GID
    * This is because s6 needs `/run` to be owned by the user running the container

For all of these reasons, we recommend you *do not* switch existing container instances to run with a non-root user without careful testing.

For example:

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/radarr:latest
    container_name: radarr
    environment:
      - TZ=Europe/London
    volumes:
      - /path/to/radarr/data:/config
      - /path/to/movies:/movies
      - /path/to/downloadclient-downloads:/downloads
    ports:
      - 7878:7878
    restart: unless-stopped
    user: 1000:1000
```

or

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/radarr:latest
    container_name: radarr
    environment:
      - TZ=Europe/London
    volumes:
      - /path/to/radarr/data:/config
      - /path/to/movies:/movies
      - /path/to/downloadclient-downloads:/downloads
    ports:
      - 7878:7878
    restart: unless-stopped
    user: 1000:1000
    tmpfs:
      - /run:uid=1000,gid=1000,exec
    security_opt:
      - no-new-privileges=true
```

## Support Policy

Operation of our images with a non-root user is supported on a Reasonable Endeavours basis and *only* for images which we have specifically tested. These images will have their ability to be run with a non-root user noted in the readme, along with any additional caveats. Please see our [Support Policy](https://linuxserver.io/supportpolicy) for more details.

## Change History

* 2025-08-13 - Add notes about `no-new-privileges=true`
* 2024-12-17 - Initial release
