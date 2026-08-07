# SealSkin Apps Registry

**Repository:** [linuxserver/sealskin-apps](https://github.com/linuxserver/sealskin-apps)

The apps registry is the data that powers the [SealSkin](sealskin.md) app store: a single YAML manifest describing every launchable application, plus the autostart scripts that wire file and URL handoff into each app. It is intentionally just text files on GitHub, no database, no packaging format, which means **anyone can host their own store** by publishing two things: an `apps.yml` and an `autostart/` directory next to it.

The default store consumed by every SealSkin server is:

```
https://raw.githubusercontent.com/linuxserver/sealskin-apps/refs/heads/master/apps.yml
```

Admins can add any number of additional stores by URL, so an organization, university, or community can curate its own catalog while still layering on the official one.

## apps.yml structure

The manifest has two root keys. First, `extension_groups`: reusable YAML anchors grouping file extensions (common images, RAW images, vectors, audio, video, MS Office, OpenDocument, ebooks, CAD and 3D, disc images, archives, code). Second, `apps`: the list itself, currently just over one hundred entries. A representative record:

```yaml
- id: "zotero"
  name: "Zotero"
  logo: "https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/zotero-icon.png"
  url: "https://github.com/linuxserver/docker-zotero"
  provider: "docker"
  provider_config:
    image: "lscr.io/linuxserver/zotero:latest"
    port: 3000
    nvidia_support: true
    dri3_support: true
    type: "app"
    autostart: true
    url_support: false
    open_support: true
    extensions: [ris, bib, rdf]
```

Field meanings:

| Field | Meaning |
| --- | --- |
| `id`, `name`, `logo`, `url` | Identity, display name, icon URL, upstream project link |
| `provider` | Launch backend, `docker` today |
| `provider_config.image` | The container image, always a Selkies based `lscr.io/linuxserver/*` image |
| `provider_config.port` | The internal web port SealSkin proxies to (3000 for nearly everything) |
| `nvidia_support` / `dri3_support` | Which GPU types the app can use, gates the GPU picker in the launcher |
| `type` | `app`, `browser`, or `desktop`, drives client behavior (browsers get URL handoff, desktops skip autostart) |
| `autostart` | Whether an autostart script exists for this app |
| `url_support` / `open_support` | Whether the app can receive a URL or an opened file at launch |
| `extensions` | File extensions this app volunteers to handle, referencing the extension groups |
| `docker_overrides` | Optional raw Docker options an app needs (for example Steam ships `security_opt: [seccomp=unconfined, apparmor=unconfined]`) |

The catalog spans the whole [application fleet](../user-guide/apps.md): a dozen browsers, 24 full desktops (Kali plus the Webtop matrix of distro and desktop combinations), creative tools, office suites, development environments, and a deep emulation and gaming shelf.

## The autostart scripts

For every app with `autostart: true`, the `autostart/` directory holds two scripts: `<id>` for X11 sessions and `<id>-wayland` for Wayland sessions. Before launching a container, the SealSkin server writes the appropriate script into the session's home directory as the window manager autostart file.

This is the mechanism behind "click a link, it opens isolated" and "download a file, it opens in the right app": SealSkin passes `SEALSKIN_URL` or `SEALSKIN_FILE` as environment variables, and the scripts consume them:

```bash
/usr/bin/firefox ${FIREFOX_CLI} ${SEALSKIN_FILE:+"$SEALSKIN_FILE"} ${SEALSKIN_URL:+"$SEALSKIN_URL"}
```

Scripts can also do first run setup, seeding emulator configs, installing desktop entries, starting helper panels, whatever the app needs to feel ready the moment the stream appears.

## Hosting your own store

1. Write an `apps.yml` following the schema above (a bare list or an `apps:` keyed document both work).
2. Put autostart scripts in an `autostart/` directory *next to* the manifest; SealSkin derives their URLs from the manifest URL (`<base>/autostart/<id>` and `<id>-wayland`).
3. Host both anywhere that serves raw files over HTTPS (a GitHub repository is perfect).
4. Add the manifest URL as a store in the SealSkin admin UI.

Stores are cached server side with ETag revalidation and refreshed hourly, so updates propagate automatically. Custom store apps can point at any image, including your own images built with the [Developer Guide](../developer-guide/building-images.md), which makes the registry the natural distribution channel for in house apps on a SealSkin deployment.

## Related lists

The website app showcase at [sealskin.app](https://sealskin.app) maintains a compact JavaScript list of the fleet (`apps.js`) for display purposes; the YAML manifest in this repository is the operational source of truth that servers actually consume.
