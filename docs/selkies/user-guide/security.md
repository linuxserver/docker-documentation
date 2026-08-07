# Security and Hardening

Read this page before exposing any Selkies container beyond your local machine.

## The threat model in one paragraph

!!! warning "This container provides privileged access to the host system"
    The web interface includes a terminal with **passwordless sudo**. Any user who can reach the GUI can gain root inside the container, install arbitrary software, and probe your local network. Do not expose it to the internet unless you have secured it properly.

Treat a Selkies session like an SSH login to a machine on your network, because functionally that is what it is.

## HTTPS is required

Modern browser features the client depends on, WebCodecs for video and audio in particular, only work in a secure context. That is why:

- Port `3001` serves HTTPS with a self signed certificate and is the port you browse to directly.
- Port `3000` serves plain HTTP and exists **only** to sit behind a reverse proxy that terminates TLS.

## Authentication layers

**By default there is no authentication.** Your options, from weakest to strongest:

1. **HTTP basic auth**: set `CUSTOM_USER` and `PASSWORD`. Adequate for a trusted home LAN, nothing more.
2. **Reverse proxy with real auth**: for anything internet facing, put the container behind a reverse proxy such as [SWAG](https://github.com/linuxserver/docker-swag) with a robust authentication mechanism (Authelia, Authentik, OAuth2 proxy, client certificates). See [Reverse Proxy](reverse-proxy.md).
3. **SealSkin**: if you are serving multiple users or apps, [SealSkin](../components/sealskin.md) handles authentication with public key cryptography and only proxies sessions to their owners.

## Container isolation options

- Avoid `--privileged` unless you specifically want the Docker in Docker feature. It dramatically widens the blast radius.
- Mounting `/var/run/docker.sock` hands the container control of the host Docker daemon, which is root on the host in practical terms. Only do this deliberately.
- `--security-opt seccomp=unconfined` disables a key Docker security layer. Use it only when a legacy host kernel or old libseccomp genuinely requires it, and treat it as a temporary workaround.

## Hardening variables

For kiosk deployments, single app terminals, classrooms, or any situation where the person at the keyboard is not the administrator, the baseimage ships lockdown variables.

Note that the window manager level switches (`HARDEN_OPENBOX`, `DISABLE_CLOSE_BUTTON`, `DISABLE_MOUSE_BUTTONS`, `HARDEN_KEYBINDS`) only apply to **single application containers**, which run under labwc or Openbox. Full desktop Webtops manage their own windows, so only the desktop wide switches (`HARDEN_DESKTOP` and the `SELKIES_*` locks) matter there. The mechanics are documented in depth in [the developer guide](../developer-guide/building-images.md#the-window-manager-layer-labwc-and-openbox).

### Umbrella switches

| Variable | Description |
| --- | --- |
| `HARDEN_DESKTOP` | Enables `DISABLE_OPEN_TOOLS`, `DISABLE_SUDO`, and `DISABLE_TERMINALS`. Also sets the related client settings (`SELKIES_FILE_TRANSFERS`, `SELKIES_COMMAND_ENABLED`, `SELKIES_UI_SIDEBAR_SHOW_FILES`, `SELKIES_UI_SIDEBAR_SHOW_APPS`) unless you set them explicitly yourself |
| `HARDEN_OPENBOX` | Window manager lockdown for single app containers. Enables `DISABLE_CLOSE_BUTTON`, `DISABLE_MOUSE_BUTTONS`, and `HARDEN_KEYBINDS`, and flags `RESTART_APP` unless you set it, so the primary application restarts automatically if closed |

### Individual switches

| Variable | Description |
| --- | --- |
| `DISABLE_OPEN_TOOLS` | Disables the `xdg-open` and `exo-open` binaries by removing their execute permissions, so apps cannot spawn arbitrary helpers |
| `DISABLE_SUDO` | Disables `sudo` by removing execute permissions and invalidating the passwordless sudo configuration |
| `DISABLE_TERMINALS` | Disables common terminal emulators and hides them from the right click menu |
| `DISABLE_CLOSE_BUTTON` | Removes the close button from window title bars |
| `DISABLE_MOUSE_BUTTONS` | Disables right click and middle click context menus and actions in the window manager |
| `HARDEN_KEYBINDS` | Disables window manager keybinds that could bypass the other options, such as `alt+f4` to close windows or `alt+escape` for the root menu |
| `RESTART_APP` | Watchdog that restarts the main application if it is closed. The user's autostart script is made read only and root owned to prevent tampering |

### Locking client settings

Any boolean `SELKIES_*` setting can be pinned so the user cannot change it in the sidebar by appending `|locked`:

```bash
-e SELKIES_CLIPBOARD_ENABLED="false|locked"
-e SELKIES_FILE_TRANSFERS="none"
-e SELKIES_UI_SHOW_SIDEBAR="false|locked"
```

See the [Configuration Reference](configuration.md) for the full list and value syntax.

### Example: locked down kiosk browser

```yaml
---
services:
  kiosk:
    image: lscr.io/linuxserver/chromium:latest
    shm_size: 1gb
    environment:
      - HARDEN_DESKTOP=true
      - HARDEN_OPENBOX=true
      - "SELKIES_CLIPBOARD_ENABLED=false|locked"
      - SELKIES_FILE_TRANSFERS=none
      - "SELKIES_UI_SHOW_SIDEBAR=false|locked"
      - NO_DECOR=true
      - "CHROME_CLI=--kiosk https://youtube.com"
    ports:
      - 3001:3001
    restart: unless-stopped
```

Locking the sidebar off entirely (`SELKIES_UI_SHOW_SIDEBAR=false|locked`) is the finishing touch for a true kiosk, the visitor sees nothing but the app.

## Sharing links

The sharing feature generates links that grant access to the running session: full collaboration, view only, or gamepad only for players 2 through 4. The built in links are a **demo of the multi user protocol**, they carry no authentication of their own. Proper shared sessions need the token based access control an orchestrator like [SealSkin](../components/sealskin.md) wires up. Remember that anyone with a collaboration link has the same power as the primary user, including that passwordless sudo terminal. Disable what you do not need:

```bash
-e SELKIES_ENABLE_SHARING=false        # master switch
-e SELKIES_ENABLE_COLLAB=false         # or individually
```

## Pelorus and the computer use API

Enabling `PELORUS=true` starts an agent control API inside the container and forces the accessibility bridge on for all applications, which means any process in the session can read the full UI text of every app. The Pelorus API itself has no authentication and relies on the container's Nginx and network isolation. Treat a Pelorus enabled container as fully readable and controllable by anything that can reach it on its internal port, and never publish its ports directly. Details on the [Pelorus](../components/pelorus.md) page.
