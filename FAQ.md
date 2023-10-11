# FAQ

Here resides some Frequently Asked Questions.

## My host is incompatible with images based on Ubuntu Jammy {#jammy}

Some x86_64 hosts running older versions of the Docker engine are not compatible with some images based on Ubuntu Jammy.

- Symptoms

    If your host is affected you may see errors in your containers such as:

    ```text
    ERROR - Unable to determine java version; make sure Java is installed and callable
    ```

    Or

    ```text
    Failed to create CoreCLR, HRESULT: 0x80070008
    ```

    Or

    ```text
    WARNING :: MAIN : webStart.py:initialize:249 : can't start new thread
    ```

- Resolution

  - Option 1 (Long-Term Fix)

    Upgrade your Docker engine to at least version `20.10.10`. [Refer to the official Docker docs for installation/update details.](https://docs.docker.com/engine/install)

  - Option 2 (Short-Term Fix)

    For Docker CLI, run your container with:

    `--security-opt seccomp=unconfined`

    For Docker Compose, run your container with:

    ```yaml
      security_opt:
        - seccomp=unconfined
    ```

## My host is incompatible with images based on rdesktop {#rdesktop}

Some x86_64 hosts have issues running rdesktop based images even with the latest Docker version due to syscalls that are unknown to Docker.

- Symptoms

    If your host is affected you may see errors in your containers such as:

    ```text
    Failed to close file descriptor for child process (Operation not permitted)
    ```

- Resolution

    For Docker CLI, run your container with:

    `--security-opt seccomp=unconfined`

    For Docker Compose, run your container with:

    ```yaml
      security_opt:
        - seccomp=unconfined
    ```

## My host is incompatible with images based on Ubuntu Focal and Alpine 3.13 and later {#libseccomp}

This only affects 32 bit installs of distros based on Debian Buster.

This is due to a bug in the libseccomp2 library (dependency of Docker itself), which is fixed. However, it's not pushed to all the repositories.

[A GitHub issue tracking this](https://github.com/moby/moby/issues/40734)

You have a few options as noted below. Options 1 is short-term, while option 2 is considered the best option if you don't plan to reinstall the device (option 3).

- Resolution

    If you decide to do option 1 or 2, you should just need to restart the container after confirming you have libseccomp2.4.4 installed.

    If 1 or 2 did not work, ensure your Docker install is at least version 20.10.0, [refer to the official Docker docs for installation.](https://docs.docker.com/engine/install/debian/)

  - Option 1

    Manually install an updated version of the library with dpkg.

    ```shell
    wget http://ftp.us.debian.org/debian/pool/main/libs/libseccomp/libseccomp2_2.4.4-1~bpo10+1_armhf.deb
    sudo dpkg -i libseccomp2_2.4.4-1~bpo10+1_armhf.deb
    ```

    {% hint style="info" %}
    This url may have been updated. Find the latest by browsing [here](http://ftp.us.debian.org/debian/pool/main/libs/libseccomp/).
    {% endhint %}

  - Option 2

    Add the backports repo for DebianBuster. As seen [here](https://github.com/linuxserver/docker-jellyfin/issues/71#issuecomment-733621693).

    ```shell
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 04EE7237B7D453EC 648ACFD622F3D138
    echo "deb http://deb.debian.org/debian buster-backports main" | sudo tee -a /etc/apt/sources.list.d/buster-backports.list
    sudo apt update
    sudo apt install -t buster-backports libseccomp2
    ```

  - Option 3

    Reinstall/update your OS to a version that still gets updates.

    - Any distro based on DebianStretch does not seem to have this package available
    - DebianBuster based distros can get the package trough backports, as outlined in point 2.

    {% hint style="info" %}
    RaspberryPI OS (formerly Raspbian) Can be upgraded to run with a 64bit kernel
    {% endhint %}

- Symptoms

  - 502 errors in __Jellyfin__ as seen in [linuxserver/docker-jellyfin#71](https://github.com/linuxserver/docker-jellyfin/issues/71)
  - `Error starting framework core` messages in the docker log for __Plex__. [linuxserver/docker-plex#247](https://github.com/linuxserver/docker-plex/issues/247)
  - No WebUI for __Radarr__, even though the container is running. [linuxserver/docker-radarr#118](https://github.com/linuxserver/docker-radarr/issues/118)
  - Images based on our Nginx base-image(Nextcloud, SWAG, Nginx, etc.) fails to generate a certificate, with a message similar to `error getting time:crypto/asn1/a_time.c:330`
  - `docker exec <container-name> date` returns 1970

## My host filesystem is incompatible with my docker storage driver {#storage}

Some host file systems types are not compatible with the default storage driver of docker (overlay2)

- Symptoms

    If your host is affected you may see errors in your containers such as:

    ```text
    ERROR Found no accessible config files
    ```
    or
    ```text
    Directory not empty. This directory contains an empty ignorecommands sub-directory
    ```

- Resolution

    As shown in [Docker docs](https://docs.docker.com/storage/storagedriver/select-storage-driver/#supported-backing-filesystems)

    A host filesystem of zfs requires a docker storage driver of zfs and a host file system of btrfs requires a docker storage driver of btrfs.
    Correcting this oversight will resolve the issue. This is not something that a container change will resolve. 

## What is lscr.io {#lscr}

LSCR is a vanity url for our images, this is provided to us in collaboration with [scarf.sh](https://about.scarf.sh/). It is not a dedicated docker registry, rather a redirection service. As of writing it redirects to GitHub Container Registry (ghcr.io). 

Aside from giving us the ability to redirect to another backend, if necessary, it also exposes telemetry about pulls, historically only available to the backend provider. We base some decisions on this data, as it gives us a somewhat realistic usage overview (relative to just looking at pulls on DockerHub).

We have some blog posts related to how we utilize Scarf:

- [End of an Arch](https://www.linuxserver.io/blog/end-of-an-arch)
- [Unravelling Some Stats](https://www.linuxserver.io/blog/unravelling-some-stats)
- [Wrap Up Warm For Winter](https://www.linuxserver.io/blog/wrap-up-warm-for-the-winter)

### I cannot connect to lscr.io {#lscr-no-connect}

Due to the nature of Scarf as a Docker gateway which gathers usage metrics, some overzealous privacy-focused blocklists will include its domains.

If you want to help us in getting a better overview of how people use our containers, you should add `gateway.scarf.sh` to the allowlist in your blocklist solution.

Alternatively, you can use Docker Hub or GHCR directly to pull your images, although be aware that all public registries gather user metrics, so this doesn't provide you with any real benefit in that area.

If Scarf is on the blocklist, you will get an error message like this when trying to pull an image:

```
Error response from daemon: Get "https://lscr.io/v2/": dial tcp: lookup lscr.io: no such host
```

This is, however, a generic message. To rule out a service-interruption, you should also see if you can resolve the backend provider.

Using dig:

```shell
dig ghcr.io +short
dig lscr.io +short
```

Using nslookup:

```shell
nslookup ghcr.io
nslookup lscr.io
```

If you only got a response from ghcr, chances are that Scarf is on the blocklist.

## I want to reverse proxy an application which defaults to https with a self-signed certificate {#strict-proxy}

### Traefik {#strict-proxy-traefik}

In this example, we will configure a serverTransport rule we can apply to a service, as well as telling Traefik to use https on the backend for the service.

Create a [ServerTransport](https://doc.traefik.io/traefik/routing/services/#serverstransport_1) in your dynamic Traefik configuration; we are calling ours `ignorecert`.

```yml
    http:
      serversTransports:
        ignorecert:
          insecureSkipVerify: true
```

Then on our `foo` service we tell it to use this rule, as well as telling Traefik the backend is running on https.

```yml
    - traefik.http.services.foo.loadbalancer.serverstransport=ignorecert
    - traefik.http.services.foo.loadbalancer.server.scheme=https
```
