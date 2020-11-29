# FAQ

Here will some Frequently Asked Questions reside

## My host is incompatible with images based on Ubuntu Focal

This seems to only affect armhf.

This is due to a bug in the libseccomp2 library (dependency of docker itself), which is fixed. However it's not pushed to all the repositories.

[A GitHub issue tracking this](https://github.com/moby/moby/issues/40734)

You have a few options, some are short-term.

1. Use another tag, not based on Focal. At the time of writing we currently offer a `bionic` tag for [Plex](https://github.com/linuxserver/docker-plex) and [Jellyfin](https://github.com/linuxserver/docker-jellyfin) that will receive the same care as latest for the foreseeable future.

2. Add the backports repo for DebianBuster. As seen [here](https://github.com/linuxserver/docker-jellyfin/issues/71#issuecomment-733621693).

    ```bash
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 04EE7237B7D453EC 648ACFD622F3D138
    echo "deb http://deb.debian.org/debian buster-backports main" | sudo tee -a /etc/apt/sources.list.d/buster-backports.list
    sudo apt update
    sudo apt install -t buster-backports libseccomp2
    ```

3. Manually install an updated version of the library with dpkg.

    ```bash
    wget http://ftp.us.debian.org/debian/pool/main/libs/libseccomp/libseccomp2_2.4.4-1~bpo10+1_armhf.deb
    sudo dpkg -i libseccomp2_2.4.4-1~bpo10+1_armhf.deb
    ```

    Note this url may have been updated. Find the latest by browsing [here](http://ftp.us.debian.org/debian/pool/main/libs/libseccomp/).

4. Reinstall/update your OS to a version that still gets updates.
    * Any distro based on DebianStretch does not seem to have this package available
    * DebianBuster based distros can get the package trough backports, as outlined in point 2.

    RaspberryPI OS (formerly Raspbian) Can be upgraded to run with a 64bit

Symptoms of this can be:

* 502 errors in __Jellyfin__ as seen in [linuxserver/docker-jellyfin#71](https://github.com/linuxserver/docker-jellyfin/issues/71)
* `Error starting framework core` messages in the docker log for __Plex__. [linuxserver/docker-plex#247](https://github.com/linuxserver/docker-plex/issues/247)
* `docker exec <container-name> date` returns 1970
