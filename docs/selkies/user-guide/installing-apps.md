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

## Steam (built in, reinstalls itself)

Every glibc based image carries a Steam installer. Nothing is installed until you ask for it, and this specialized installer can run steam in any docker environment without any additional container permissions (seccomp/apparmor):

```bash
steam
```

The first run opens a terminal that installs the Steam launcher and its 32 bit dependencies with the distro package manager, then wraps the launcher so gamepads work through the [joystick interposer](web-client.md#gamepads), including inside Proton. Steam then appears in the menus and in the sidebar Apps section, and later runs of `steam` start it normally. You can also install or remove it from the Apps section, or with `selkies-proot install steam` and `selkies-proot remove steam`.

The install lives in the container layer, so a recreation or upgrade drops it. Your game data in `$HOME/.steam` and `$HOME/.local/share/Steam` persists. Running `steam` again, or double clicking a Steam desktop icon you kept in `~/Desktop`, triggers the minimal installer again. After the reinstall your library is where you left it.

Limits:

- x86_64 only, and it needs passwordless sudo, so `HARDEN_DESKTOP` and `DISABLE_SUDO` block it.
- Alpine images ship a `steam` stub that reports it is unsupported.
- `NO_STEAM=true` removes the installer at startup, so `steam` is not a command in the container.

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
