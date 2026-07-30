# Selkies Desktop

**Repository:** [selkies-project/selkies-desktop](https://github.com/selkies-project/selkies-desktop) · **License:** MPL-2.0 · **Enable with:** `-e SELKIES_DESKTOP=true`

Selkies Desktop is a deliberately tiny desktop shell for single application containers. It is a single C program (one source file, no toolkit, drawing with Cairo over Wayland) that turns a bare labwc session into something that feels like a traditional desktop, without dragging in a full desktop environment.

## What it provides

- A categorized **application launcher** (start menu) built from the standard `.desktop` files on the system
- A persistent **bottom panel with a taskbar** for switching, minimizing, and restoring windows
- A **wallpaper layer** with the Selkies icon
- **Desktop icons** mapped from `~/Desktop`, launched with a double click

## The philosophy

The upstream README is explicit: this is **not** a general purpose desktop environment. Paths are hardcoded, sizes are fixed, and styling is baked in. The goal is narrow: expand on labwc's default right click menu so a single app container gets light multi window capability, a start menu, and a taskbar, at a cost of one small binary with no dependencies beyond Cairo and wayland-client.

If you need a real desktop, use a [Webtop](../user-guide/apps.md). Selkies Desktop fills the gap between "one maximized app" and "full KDE Plasma".

## How to enable it

In any Selkies baseimage derived container running in Wayland mode:

```bash
docker run --rm -it \
  --shm-size=1gb \
  -p 3001:3001 \
  -e SELKIES_DESKTOP=true \
  lscr.io/linuxserver/firefox:latest bash
```

Wayland mode (`PIXELFLUX_WAYLAND=true`) is a prerequisite, it is the default on the current images. The variable is labwc only: Webtop KDE images ignore it since they ship their own shell.

## How it works

The binary is prebuilt into every Selkies baseimage at `/usr/bin/selkies-desktop`. When `SELKIES_DESKTOP=true`, the session launcher starts labwc, waits a moment, then runs `selkies-desktop` as the foreground session process connected to labwc's `wayland-0` socket (with `DISPLAY=:0` for XWayland apps). When it exits the session ends.

Under the hood it uses two wlroots protocols:

- **wlr layer shell** for its two surfaces: the panel (bottom anchored, 30px exclusive zone, dynamically raised above windows while the start menu is open) and the background layer (full screen, input passing through everywhere except desktop icon cells).
- **wlr foreign toplevel management** to track open windows for the taskbar: titles, app IDs, icons, minimize and activate actions.

Other implementation notes worth knowing:

- Application entries come from scanning `/usr/share/applications` and `~/.local/share/applications`, with freedesktop categories folded into a small fixed set (Internet, Multimedia, Development, Games, Office, System, Utilities, and so on).
- Icons resolve from hicolor, Adwaita, Papirus, and pixmaps, with SVG rasterization handled by a vendored nanosvg, no icon library dependency.
- Apps launch through `dex`, `gio launch`, or `gtk-launch`, whichever exists.
- The panel watches `~/.config/panel-reload` with inotify. Touch that file to force a rescan of applications and desktop icons:

```bash
touch ~/.config/panel-reload
```

## Building from source

```bash
sudo apt install libcairo2-dev libwayland-dev wayland-protocols curl build-essential
make
```

The Makefile generates the Wayland protocol bindings with `wayland-scanner` from vendored XML files (`make fetch-deps` refreshes them). Output is a single `selkies-desktop` binary. The baseimage builds it in a dedicated Docker stage and copies the binary in, a nice reference for how small a stack component can be.
