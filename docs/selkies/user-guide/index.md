# User Guide

This guide is for people running the prebuilt Selkies based containers from LinuxServer.io: the Webtop desktops and the single application images like Chromium, Firefox, GIMP, or Steam.

You do not need to know anything about the internals to use these containers. If a page in this guide feels too deep, back up to the [Quickstart](quickstart.md), it is genuinely enough for most people.

## Reading order

1. **[Quickstart](quickstart.md)**: get a desktop or app streaming in one command, and learn the minimal command debugging philosophy.
2. **[Installation](installation.md)**: docker run and compose in full, ports, volumes, PUID and PGID, and the options that actually matter.
3. **[GPU Acceleration](gpu.md)**: Intel, AMD, and Nvidia passthrough, zero copy encoding, and multi GPU setups.
4. **[Using the Web Client](web-client.md)**: the sidebar, clipboard, file transfer, gamepads, mobile controls, and session sharing.
5. **[Configuration Reference](configuration.md)**: every environment variable in one place.
6. **[Available Apps and Desktops](apps.md)**: the Webtop flavors and the full application catalog.
7. **[Installing Applications](installing-apps.md)**: adding software inside a container with proot-apps or Docker mods.
8. **[Security and Hardening](security.md)**: authentication, what the container can do, and lockdown variables for kiosk style deployments.
9. **[Reverse Proxy](reverse-proxy.md)**: putting containers behind SWAG, Nginx, Traefik, or a subfolder.
10. **[Troubleshooting](troubleshooting.md)**: the checklist to run before opening an issue.
