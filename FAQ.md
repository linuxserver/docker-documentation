# FAQ

Here will some Frequently Asked Questions reside

## My host is incompatible with images based on Ubuntu Focal and Alpine 3.13 {#libseccomp}

This only affect 32 bit installs of distros based on Debian Buster.

This is due to a bug in the libseccomp2 library (dependency of docker itself), which is fixed. However it's not pushed to all the repositories.

[A GitHub issue tracking this](https://github.com/moby/moby/issues/40734)

You have a few options, 1 and 2 are short-term, 3 is to be considered the best option if you dont plan to reinstall the device.

### Resolution

If you decide to do option 2 or 3, you should just need to restart the container after confirming you have libseccomp2.4.4 installed.

If 2 or 3 did not work, ensure you have an up-to-date install of Docker, [refer to the official Docker docs for installation.](https://docs.docker.com/engine/install/debian/)

1. Use another tag, not based on Focal. At the time of writing we currently offer a `bionic` tag for [Plex](https://github.com/linuxserver/docker-plex) and [Jellyfin](https://github.com/linuxserver/docker-jellyfin) that will receive the same care as latest for the foreseeable future.

2. Manually install an updated version of the library with dpkg.

    ```bash
    wget http://ftp.us.debian.org/debian/pool/main/libs/libseccomp/libseccomp2_2.4.4-1~bpo10+1_armhf.deb
    sudo dpkg -i libseccomp2_2.4.4-1~bpo10+1_armhf.deb
    ```

    Note this url may have been updated. Find the latest by browsing [here](http://ftp.us.debian.org/debian/pool/main/libs/libseccomp/).

3. Add the backports repo for DebianBuster. As seen [here](https://github.com/linuxserver/docker-jellyfin/issues/71#issuecomment-733621693).

    ```bash
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 04EE7237B7D453EC 648ACFD622F3D138
    echo "deb http://deb.debian.org/debian buster-backports main" | sudo tee -a /etc/apt/sources.list.d/buster-backports.list
    sudo apt update
    sudo apt install -t buster-backports libseccomp2
    ```

4. Reinstall/update your OS to a version that still gets updates.
    * Any distro based on DebianStretch does not seem to have this package available
    * DebianBuster based distros can get the package trough backports, as outlined in point 2.

    RaspberryPI OS (formerly Raspbian) Can be upgraded to run with a 64bit kernel

### Symptoms

* 502 errors in __Jellyfin__ as seen in [linuxserver/docker-jellyfin#71](https://github.com/linuxserver/docker-jellyfin/issues/71)
* `Error starting framework core` messages in the docker log for __Plex__. [linuxserver/docker-plex#247](https://github.com/linuxserver/docker-plex/issues/247)
* No WebUI for __Radarr__, even though the container is running. [linuxserver/docker-radarr#118](https://github.com/linuxserver/docker-radarr/issues/118)
* Images based on our Nginx base-image(Nextcloud, SWAG, Nginx, etc.) fails to generate a certificate, with a message similar to `error getting time:crypto/asn1/a_time.c:330`
* `docker exec <container-name> date` returns 1970
