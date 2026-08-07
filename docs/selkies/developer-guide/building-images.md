# Building Custom Images

Packaging your own application or desktop on the Selkies baseimage is deliberately boring. This page goes from the minimal case to the two production patterns, a single app (Chromium) and a full desktop (Webtop KDE).

## The minimal single app image

```dockerfile
FROM ghcr.io/linuxserver/baseimage-selkies:debiantrixie

ENV TITLE="My App"
ENV PIXELFLUX_WAYLAND=true

RUN apt-get update && \
    apt-get install -y --no-install-recommends my-app && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*

COPY /root /

EXPOSE 3001
VOLUME /config
```

with a repository layout of:

```
root/
└── defaults/
    ├── autostart_wayland    # what to run in Wayland mode
    └── autostart            # what to run in X11 fallback mode
```

and `root/defaults/autostart_wayland` containing, in the simplest case, one line:

```bash
#!/bin/bash
my-app
```

Build it, run it with `--shm-size=1gb -p 3001:3001`, and your app is streaming. Everything else on this page is refinement.

## The downstream contract

The baseimage looks for these files. All are optional, sane defaults exist for each:

| File | Role |
| --- | --- |
| `/defaults/autostart_wayland` | Command launched inside labwc (Wayland). Runs as the `abc` user. Copied to `/config/.config/labwc/autostart` on first run only, so users can edit it and their edits persist |
| `/defaults/autostart` | Same for Openbox (X11 fallback) |
| `/defaults/menu_wayland.xml`, `/defaults/menu.xml` | Right click root menu (Openbox menu XML schema, shared by labwc) |
| `/defaults/startwm_wayland.sh`, `/defaults/startwm.sh` | Replace the *entire* session startup. This is the full desktop hook, override these and you own the session |
| `/usr/share/selkies/www/icon.png` | App icon: favicon, PWA icon, and the Selkies Desktop wallpaper mark |

Also set `ENV TITLE` (browser tab title) and keep `VOLUME /config`.

!!! tip "First run copy semantics"
    Autostart and menu files are copied into `/config` only if they do not already exist there. That makes them user editable and persistent, but it also means testing changes to them requires a fresh `/config` volume, a classic gotcha.

## Case study: docker-chromium (single app)

The [Chromium image](https://github.com/linuxserver/docker-chromium) is the canonical single app pattern. Its Dockerfile is four steps: replace the icon, `apt-get install chromium chromium-l10n`, clean up, `COPY /root /`. The interesting engineering is in the overlay:

**A wrapper script**, `/usr/bin/wrapped-chromium`, instead of launching the browser directly:

```bash
#!/bin/bash
# Cleanup stale singleton locks so a recreated container does not
# hit the "profile in use" dialog
if ! pgrep chromium > /dev/null; then
  rm -f $HOME/.config/chromium/Singleton*
fi

# Use native Wayland when a GPU is present and labwc is running
if ls -l /dev/dri/* > /dev/null 2>&1 && pgrep labwc > /dev/null; then
  WAYLAND="--ozone-platform=wayland"
fi

# Accessibility for the Pelorus agent layer
if [ "${PELORUS,,}" == "true" ]; then
  ACCESSIBILITY="--force-renderer-accessibility"
fi

exec /usr/bin/chromium \
  --no-sandbox \
  --test-type \
  --password-store=basic \
  --start-maximized \
  ${WAYLAND} ${ACCESSIBILITY} "$@"
```

Notes on those flags: `--no-sandbox` is required because the container itself is the sandbox boundary and Chromium's own sandbox needs privileges the container deliberately lacks; `--password-store=basic` avoids keyring prompts; a symlink at `/usr/bin/chromium-browser` catches anything invoking the standard name.

**The autostart passes user flags through an env var:**

```bash
#!/bin/bash
wrapped-chromium ${CHROME_CLI}
```

That `${CHROME_CLI}` convention (each browser image has its equivalent, `FIREFOX_CLI`, `VIVALDI_CLI`, and so on) is how end users add flags or a start URL without rebuilding, document your own equivalent if your app takes arguments.

**A menu.xml** offering the app and a terminal (`foot` on Wayland, `xterm` on X11) on right click, so the session is recoverable if the app is closed.

```bash
<?xml version="1.0" encoding="utf-8"?>
<openbox_menu xmlns="http://openbox.org/3.4/menu">
<menu id="root-menu" label="MENU">
<item label="foot" icon="/usr/share/icons/hicolor/48x48/apps/foot.png"><action name="Execute"><command>/usr/bin/foot</command></action></item>
<item label="Chromium" icon="/usr/share/icons/hicolor/48x48/apps/chromium.png"><action name="Execute"><command>/usr/bin/wrapped-chromium --enable-features=UseOzonePlatform --ozone-platform=wayland</command></action></item>
</menu>
</openbox_menu>
```

## Case study: docker-webtop ubuntu-kde (full desktop)

The [Webtop KDE image](https://github.com/linuxserver/docker-webtop/tree/ubuntu-kde) shows the desktop pattern. Instead of autostart files (its `/defaults/autostart` is literally `exit 0`), it overrides the session scripts:

- **`/defaults/startwm_wayland.sh`** owns the whole session: it seeds KDE config on first run (disable compositing, disable the lock screen), exports the KDE session environment (`QT_QPA_PLATFORM=wayland`, `XDG_CURRENT_DESKTOP=KDE`), then inside a dbus session starts `kwin_wayland` **nested on the pixelflux socket** (`WAYLAND_DISPLAY=wayland-1`) with XWayland, waits, starts the polkit agent, and runs `plasmashell` on `wayland-0` as the foreground process. A small Python shim pre binds the X11 socket so XWayland lands on a predictable display number.
- **`/defaults/startwm.sh`** (the X11 path) is a deliberate stub that displays an unsupported platform message, this flavor is Wayland only.
- It bridges the platform's autostart convention into KDE by dropping a `.desktop` file in `~/.config/autostart` that executes the user's persistent autostart script, so features like SealSkin's autostart injection work identically on desktops.
- Build steps worth stealing: `setcap -r /usr/bin/kwin_wayland` (strip file capabilities so KWin runs unprivileged in a container), rewriting the Chromium `.desktop` Exec to the wrapper script, and swapping in `wl-clipboard-rs` for clipboard tooling.

The other Webtop flavors are lighter: Alpine XFCE's entire session script is essentially `WAYLAND_DISPLAY=wayland-1 startxfce4 --wayland`, some desktops can talk to the pixelflux compositor directly without a nested compositor.

## The window manager layer: labwc and Openbox

Single application containers run [labwc](https://github.com/labwc/labwc) on Wayland, which is a **1:1 replacement for Openbox**: it consumes the same menu XML schema and an rc.xml with the same concepts, so everything below applies to both stacks, with the X11 fallback simply using Openbox itself. Full desktop Webtops (KDE, XFCE, and friends) bring their own window management and ignore this layer entirely.

### The right click menu: menu.xml

The root menu users get by right clicking the desktop is plain Openbox menu XML. The baseimage default (`/defaults/menu_wayland.xml` for labwc, `/defaults/menu.xml` for Openbox) is just a terminal entry:

```xml
<?xml version="1.0" encoding="utf-8"?>
<openbox_menu xmlns="http://openbox.org/3.4/menu">
<menu id="root-menu" label="MENU">
<item label="foot" icon="/usr/share/pixmaps/xterm-color_48x48.xpm">
  <action name="Execute"><command>/usr/bin/foot</command></action>
</item>
</menu>
</openbox_menu>
```

Downstream images override these files to add their application, so the session is recoverable if the app is closed. Like the autostart scripts, menu files are copied to `/config/.config/labwc/` (or `.../openbox/`) on first run only, after which the user's copy wins.

### Our rc.xml defaults

The labwc config ships as `/defaults/labwc.xml` and is copied to `/config/.config/labwc/rc.xml` on first run (Openbox uses the system `/etc/xdg/openbox/rc.xml`, regenerated from a backup at each start). The notable defaults, identical in intent on both platforms:

- **Server side decorations** with a titlebar layout of `icon:iconify,max,close`, and a **window rule maximizing every window** on launch so the app fills the stream.
- **Per app decoration overrides**: browsers that draw their own tab bar (Chromium, Firefox, Brave, Vivaldi, and the rest) get `serverDecoration="no"` rules so they render edge to edge.
- **Mouse bindings on the desktop**: right click shows the root menu, middle click shows the combined client list (how users restore minimized windows).
- **Keybinds**: `alt+f4` and `alt+escape` close windows, `alt+space` opens the window menu, and Super+E launches a terminal.

### How the hardening variables rewrite it

At container init, `init-selkies-config` rewrites the rc.xml based on environment variables, which is exactly how the [hardening family](../user-guide/security.md#hardening-variables) works under the hood:

| Variable | rc.xml edit |
| --- | --- |
| `NO_DECOR` | Flips the decoration rules to `serverDecoration="no"` (Openbox: injects `<decor>no</decor>`) |
| `NO_FULL` | Deletes the maximize on launch window rule |
| `DISABLE_CLOSE_BUTTON` | Strips `close` from the titlebar button layout |
| `DISABLE_MOUSE_BUTTONS` | Deletes the right and middle click mousebinds, removing the root menu and client list |
| `HARDEN_KEYBINDS` | Comments out the escape hatch keybinds (`alt+f4`, `alt+escape`, `alt+space`, Super+E) |

When `DISABLE_MOUSE_BUTTONS` or `HARDEN_KEYBINDS` is active, the resulting rc.xml is chowned to root and made read only (mode 444) so the session user cannot undo the lockdown from inside.

**Scope**: because all of this operates on labwc and Openbox configuration, the window manager hardening only affects **single application containers**. On full desktop Webtops these variables have nothing to rewrite; the desktop environment's own policies apply there.

## Hardening and kiosk builds

You rarely need image changes for lockdown, the [hardening variables](../user-guide/security.md#hardening-variables) (`HARDEN_DESKTOP`, `HARDEN_OPENBOX`, `RESTART_APP`, and the `SELKIES_*|locked` syntax) do it at runtime through the rc.xml rewrites above plus binary permission changes, which keeps one image serving both open and kiosk deployments. Bake `ENV` defaults into your Dockerfile if you want them locked by default.

## Testing your image

```bash
docker build -t my-selkies-app .
docker run --rm -it --shm-size=1gb -p 3001:3001 -v /tmp/testconfig:/config my-selkies-app bash
```

Checklist:

- App launches maximized and undecorated (or as intended) in the browser
- Audio plays, clipboard syncs both ways
- Kill the app inside the session: can you relaunch from the right click menu? Does `RESTART_APP=true` bring it back?
- Recreate the container against the same `/config`: settings persist, no first run dialogs
- Try `SELKIES_DESKTOP=true` and `PELORUS=true` if you intend to support them
- Run the X11 fallback (`-e PIXELFLUX_WAYLAND=false`) unless you are deliberately Wayland only, in which case ship the explanatory stub `startwm.sh`

## Multi arch and CI

LinuxServer images ship x86_64 and aarch64 from near identical Dockerfiles (`Dockerfile` and `Dockerfile.aarch64` differing only in the FROM tag). If you publish your own, the same pattern with `docker buildx` covers both. For distribution through SealSkin, add your image to a custom [apps registry](../components/sealskin-apps.md) with an autostart script and it becomes installable in any SealSkin deployment.
