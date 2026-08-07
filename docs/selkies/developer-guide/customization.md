# Customizing Containers

You can go remarkably far customizing a stock container at runtime before a custom image is warranted. These are the layers, from lightest to heaviest.

## 1. Environment variables

The first stop, and often the last. The [Configuration Reference](../user-guide/configuration.md) covers stream tuning, UI visibility, feature gating, and the `|locked` syntax; the [Security page](../user-guide/security.md) covers the hardening family. Between `TITLE`, `DASHBOARD`, watermarks, UI toggles, and locks, most "white label kiosk" requirements are pure configuration.

## 2. The persistent config volume

Because `/config` is the user home, a lot of behavior is just files you can manage there:

- **`/config/.config/labwc/autostart`** (or `.../openbox/autostart` in X11 mode): the session launch script. The image default is copied here on first run and never overwritten, so you can edit what starts, add companion processes, or export app specific environment. Note that with `RESTART_APP=true` this file is locked read only by design.
- **Menus** (`menu.xml`) live alongside and follow the same first run copy rule, and **`rc.xml`** (window manager behavior, keybinds, decorations) lives there too. The schema and our default edits are documented in [the window manager layer](building-images.md#the-window-manager-layer-labwc-and-openbox).
- Application dotfiles, browser policies, desktop settings: seed them into the volume before first boot and the session starts preconfigured. This is exactly how SealSkin's template and App Lab features work.

## 3. Custom scripts and services (LSIO hooks)

Inherited from the LinuxServer base and fully supported here:

- **`/custom-cont-init.d/`**: mount a directory of scripts to run once at container init, as root, before services start. Ideal for installing a package, dropping a config file, or patching something in the image layer.

```yaml
    volumes:
      - ./my-init:/custom-cont-init.d:ro
```

- **`/custom-services.d/`**: mount scripts to run as supervised long running services alongside the stack, a sidecar daemon inside the session container.

## 4. Docker mods

Reusable, shareable customization layers applied at startup via the `DOCKER_MODS` variable, multiple mods separated by `|`. The most useful with these images:

```yaml
    environment:
      - DOCKER_MODS=linuxserver/mods:universal-package-install
      - INSTALL_PACKAGES=fonts-noto-cjk|mpv
```

The [mod catalog](https://mods.linuxserver.io/) has many more, and writing your own mod is a tiny Dockerfile that layers files into the container at start, effectively a runtime `COPY /root /`.

## 5. proot-apps

Persistent, per user application installs into `/config` that survive image updates, covered in [Installing Applications](../user-guide/installing-apps.md). Relevant to developers because it is scriptable: a custom init script can `proot-apps install` a set of tools on first boot to build a standard environment without owning an image.

## 6. Custom dashboards and frontends

The web client separates the streaming engine (`selkies-web-core`) from the UI (the dashboard) with a documented `postMessage` API: the engine handles the socket, decode, render, and input, and emits status events; the dashboard sends control messages (`settings`, `pipelineControl`, `setManualResolution`, clipboard updates, and so on). Ship your own dashboard and select it with the `DASHBOARD` variable, or in a custom image drop your build into `/usr/share/selkies/` alongside the stock ones. See the selkies-web-core README in the [Selkies repository](https://github.com/selkies-project/selkies) for the full message catalog, and [Development Environment](development.md) for live reload while building one.

## When to graduate to a custom image

Rules of thumb:

- Packages needed at boot every time, and start time matters → custom image
- The same customization on more than a couple of deployments → custom image
- Anything touching the session scripts (`startwm*`) → custom image
- One off tweak, user level config, or an experiment → stay with the runtime layers above

The jump is small by design, take your working `custom-cont-init.d` script and it usually translates line for line into a Dockerfile `RUN`, plus a `COPY /root /` for your files. Continue at [Building Custom Images](building-images.md).
