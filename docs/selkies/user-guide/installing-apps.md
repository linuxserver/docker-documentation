# Installing Applications

The containers are immutable by design: anything installed with the system package manager lives in the container layer and disappears when the container is recreated (which happens on every image update). Only `/config`, the user's home directory, persists.

There are two supported ways to add software, one persistent, one baked in at start.

## PRoot Apps (persistent, recommended)

[proot-apps](https://github.com/linuxserver/proot-apps) installs portable applications into the persistent `$HOME` directory, so they survive container upgrades and recreation.

Inside the container (via the web terminal or `docker exec`):

```bash
proot-apps install filezilla
```

The app appears in the session's menus and can be launched like any other application. Update and remove work the same way:

```bash
proot-apps update filezilla
proot-apps remove filezilla
```

The list of supported applications is maintained in the [proot-apps README](https://github.com/linuxserver/proot-apps?tab=readme-ov-file#supported-apps).

Two things to know:

- Applications are mostly ingested from the Alpine repositories for maintainability, so what you get is the Alpine build of an app regardless of the flavor of the container you run it in.
- **Nvidia GPUs are not supported inside proot-apps.** If an app needs Nvidia acceleration, run it as its own dedicated image or bake it into a custom one.

## Native packages via Docker mods (non persistent)

For system packages, use the [universal-package-install](https://github.com/linuxserver/docker-mods/tree/universal-package-install) mod. Packages are installed by the init system every time the container starts:

```yaml
  environment:
    - DOCKER_MODS=linuxserver/mods:universal-package-install
    - INSTALL_PACKAGES=libfuse2|git|gdb
```

Trade offs:

- Increases container start time on every boot.
- Not persistent in the image, but reinstalled automatically, so effectively stable as long as the variable stays set.
- Best for libraries and CLI tools an app needs, less ideal for large GUI applications.

## Building your own image (permanent)

If you always need the same software, the clean solution is a small downstream Dockerfile:

```dockerfile
FROM lscr.io/linuxserver/webtop:ubuntu-kde

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      git \
      build-essential && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*
```

This is the beginning of the whole [Building Custom Images](../developer-guide/building-images.md) story in the Developer Guide.

## A note on the App Lab

If you are running [SealSkin](../components/sealskin.md), there is a fourth option: the App Lab lets you customize a base image interactively through the GUI, then commit the home directory as a reusable template, no Docker knowledge required.
