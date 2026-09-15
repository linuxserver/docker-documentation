# Running Containers As A Non-Root User

!!! warning
    Running containers as a non-root user is an advanced topic and should not be undertaken without a full understanding of everything documented below.

## What?

If you run one of our typical images in a standard Docker setup, the container itself will run as `root`. After init we then drop to an unprivileged user, `abc` to run the actual application service(s). We do this because at the time we designed our architecture the alternative - setting a fixed unprivileged user at build time - would have prevented us from offering the range of options that wanted to. While it is now possible to use the `--user` parameter to start any container as an arbitrary user, it hasn't been something we've been able to support before now.

The other approach is to run [Docker itself rootless](https://docs.docker.com/engine/security/rootless/). This creates a separate user and network namespace for your containers and means that even containers nominally running as `root` don't have root permissions on your host. Running a container as a non-root user and running it rootless are **not** the same, but are commonly conflated.

## Why?

Some people take the position that a container running as root *at any point in any configuration* is an unacceptable security risk, this is typically driven by a misunderstanding of the security boundaries of containers and the likely paths an attacker has access to. Having said that, there are risks with having containers running as root, depending on the environment; generally, rather than starting containers as an unprivileged user, a better approach is to run Docker itself rootless, but that's not always practical. In these situations, being able to start individual containers as an unprivileged user has its benefits.

To give you some sense of the scope of potential risk, let's take a look at possible configurations:

### Container starts as root, application runs as root

If the application is compromised, an attacker could gain root access to the container without any further action. However, without a further container escape vulnerability, they cannot affect the host unless the container has additional capabilities, runs privileged, or is configured with shared namespaces, mounted devices, or other advanced options that expand its attack surface.

### Container starts as root, application runs as unprivileged user

This is the configuration for most LSIO images. If the application is compromised, an attacker has access to the container as an unprivileged user. Our images do not typically include tools such as su/sudo/doas, or other suid binaries, and so without a further local privilege escalation vulnerability they cannot gain root access inside the container. If they were able to find a container escape vulnerability that could be exploited without root access, they may be able to gain access to the host as either an unprivileged or root user, depending on the exploit.

### Container starts as unprivileged user, application runs as unprivileged user

This is the "non-root" configuration for LSIO images. This is identical to the previous scenario *except* that the container init runs as an unprivileged user as well as the application, so if an attacker were to compromise that process - such as via custom scripts or a supply chain exploit in an included package - they would not have root access inside the container. The root user still exists in the image, and can still be accessed, it just isn't used by the running container.

### Docker runs rootless, container and application run in any of the above configurations

Docker runs itself and the entire container in a user namespace, separate from the rest of the host. Even if the application in the container is running as root, and the container is running privileged, an attacker is limited to that user namespace and cannot access the rest of the host. They could however access other containers in that namespace, or data mounted into containers from outside the namespace. There is also the possibility of vulnerabilities that would allow namespace escape, so even with a rootless environment you should still follow good security practices.

### A note on no-new-privileges=true

Docker provides an option to restrict privilege escalation - via suid binary, exploit, or other route - that can be set via CLI or compose:

```shell
--security-opt=no-new-privileges:true
```

```yaml
    security_opt:
      - no-new-privileges=true
```

This will prevent any process in the container from gaining more privileges than its parent. This can be used in combination with any of the above configurations, subject to the caveats listed below, and with the understanding that it will prevent the use of tools such as `sudo`, or any other suid binary such as `passwd`.

## How?

Creating a container with `--user <uid>:<gid>` or:

```yaml
services:
  somecontainer:
    image: someimage
    user: <uid>:<gid>
```

Will start the container as that user, and that cannot then be changed without recreating the container. It's never quite that simple, however.

Our images use s6 as a supervisor and that needs to be able to write its service files to `/run`; many applications expect to be able to write to their working directory, changing UIDs and GIDs requires writing to `/etc/passwd` & `/etc/group`, installing new packages requires writing to numerous locations, and mods need to be extracted to the container filesystem. In short, there are some heavy limitations around operation of our images with a non-root user:

* The PUID & PGID variables will not have any effect, the container will instead run applications with the UID & GID of the user you have specified via the `--user` parameter
* You will need to manually manage the permissions of any mounted volumes or paths
* Docker Mods will not be run
* Custom Services will not be run
* Custom Scripts will be limited in their functionality
* You cannot set `no-new-privileges=true` unless you additionally set permissions on /run to match your `user` UID and GID
    * This is because s6 needs `/run` to be owned by the user running the container

For all of these reasons, we recommend you *do not* switch existing container instances to use a non-root user without careful testing.

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

Operation of our images with a non-root user is supported on a Reasonable Endeavours basis and *only* for images which we have specifically tested. These images will have their ability to use a non-root user noted in the readme, along with any additional caveats. Please see our [Support Policy](https://linuxserver.io/supportpolicy) for more details.

## Change History

* 2026-09-15 - Update "Why" section to clarify configuration options
* 2025-08-13 - Add notes about `no-new-privileges=true`
* 2024-12-17 - Initial release
