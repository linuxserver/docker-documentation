# Available Apps and Desktops

Every image in this catalog is built on the same [Selkies baseimage](../components/baseimages.md), so everything in this guide, the ports, the environment variables, the GPU flags, the web client, applies to all of them identically. Swap the image name and you are done.

## Webtop: full desktops

[Webtop](https://github.com/linuxserver/docker-webtop) ships complete desktop environments as tags of `lscr.io/linuxserver/webtop`. One branch per flavor, the tag is `<distro>-<desktop>`:

| Tag | Description |
| --- | --- |
| `latest` | XFCE Alpine *Wayland Support |
| `alpine-i3` | i3 Alpine *Wayland Support |
| `alpine-kde` | KDE Alpine *Wayland Only |
| `alpine-mate` | MATE Alpine |
| `arch-i3` | i3 Arch *Wayland Support |
| `arch-kde` | KDE Arch *Wayland Support |
| `arch-mate` | MATE Arch |
| `arch-xfce` | XFCE Arch *Wayland Support |
| `debian-i3` | i3 Debian *Wayland Support |
| `debian-kde` | KDE Debian |
| `debian-mate` | MATE Debian |
| `debian-xfce` | XFCE Debian |
| `fedora-i3` | i3 Fedora *Wayland Support |
| `fedora-kde` | KDE Fedora *Wayland Support |
| `fedora-mate` | MATE Fedora |
| `fedora-xfce` | XFCE Fedora |
| `ubuntu-i3` | i3 Ubuntu *Wayland Support |
| `ubuntu-kde` | KDE Ubuntu *Wayland Only |
| `ubuntu-mate` | MATE Ubuntu |
| `ubuntu-xfce` | XFCE Ubuntu *Wayland Support |

How to read the matrix:

- **Wayland Support** means the flavor can run the modern Wayland stack. XFCE flavors marked this way carry experimental XFCE Wayland support, and the i3 flavors run **Sway** when in Wayland mode.
- **Wayland Only** flavors cannot use X11 at all. All KDE images now run in Wayland mode by default.
- Unmarked flavors run the X11 stack. X11 will die off eventually, the platform is all in on Wayland because of the true zero copy pipeline it unlocks, the performance difference is night and day. Prefer a Wayland capable flavor whenever you can.

```bash
docker run -d \
  --name=webtop \
  --shm-size=1gb \
  -p 3001:3001 \
  -v /path/to/config:/config \
  lscr.io/linuxserver/webtop:ubuntu-kde
```

Notes:

- The **KDE flavors are the flagship experience**, running KDE Plasma natively on Wayland with a nested KWin compositor. `ubuntu-kde` reflects the current state of the project best and is the reference flavor used throughout these docs.
- **Nvidia GPU support is not available on Alpine based images.** GPU users should pick Ubuntu, Debian, Fedora, or Arch flavors.

## Single application images

More than one hundred applications are packaged as dedicated images, each running the app under the lightweight labwc compositor so it feels like a native web app. All follow the pattern `lscr.io/linuxserver/<name>`:

**Browsers and web:** Brave, Chrome, Chromium, Firefox, Helium, Librewolf, Msedge, Mullvad Browser, Opera, Ungoogled Chromium, Vivaldi, Zen, Webstation

**Communication:** Altus, Ferdium, Pidgin, Signal, Telegram, Thunderbird, Webcord, Weixin

**Development:** Github Desktop, Gitqlient, Intellij Idea, Mysql Workbench, Pycharm, Sqlitebrowser, Vscode, Vscodium, Yaak

**Creative and media:** Ardour, Audacity, Blender, Darktable, Digikam, Gimp, Handbrake, Inkscape, Kdenlive, Krita, Lollypop, Rawtherapee, Shotcut, Spotube, Vlc

**Office and productivity:** Calibre, Calligra, Joplin, Libreoffice, Obsidian, Onlyoffice, Wps Office, Zotero

**3D printing and engineering:** Bambustudio, Cura, Freecad, Kicad, Orcaslicer

**Gaming and emulation:** Azahar, Blade of Agony, Dolphin, Dosbox Staging, Duckstation, Eden, Flycast, Gzdoom, Mame, Melonds, Modrinth, Pcsx2, Ppsspp, Retroarch, Rpcs3, shadPS4, Steam, Xemu, Dogwalk

**Utilities and other:** Boinc, Doublecommander, Filezilla, Keepassxc, Kali Linux, Mediaelch, Qdirstat, Remmina, Rustdesk, Wireshark, WineGUI

Each app has its own GitHub repository at `github.com/linuxserver/docker-<name>` with a README covering any app specific options (for example `CHROME_CLI` on the Chromium image to pass command line flags to the browser).

The machine readable list that powers the [SealSkin](../components/sealskin.md) app store lives at [sealskin.app/apps.js](https://sealskin.app/apps.js), and the SealSkin apps registry with full launch metadata is documented on the [SealSkin Apps Registry](../components/sealskin-apps.md) page.

## Which should I pick?

- **You want one app in a browser tab** (a remote browser, a media tool, an IDE): use the dedicated app image. Lower memory, instant focus on the app, kiosk friendly.
- **You want one app but occasionally need a file manager or second window:** use the app image and set `-e SELKIES_DESKTOP=true` for the minimal [Selkies Desktop](../components/selkies-desktop.md) shell.
- **You want a real desktop:** Webtop. Pick `ubuntu-kde` or `debian-kde` if in doubt, or an XFCE or MATE flavor for lower resource usage.
- **You want many apps for many users, launched on demand:** run [SealSkin](../components/sealskin.md) and let it orchestrate all of the above.
