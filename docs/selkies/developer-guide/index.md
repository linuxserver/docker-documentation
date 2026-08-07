# Developer Guide

This guide is for people who build on the platform rather than just run it: packaging your own application or desktop as a Selkies container, customizing the runtime, integrating the underlying libraries, or contributing to the stack itself.

## Which page do you need?

- **"I want to ship my app in a browser."** Read [Building Custom Images](building-images.md). It is a Dockerfile of a dozen lines, and the page dissects two real production examples (Chromium and Webtop KDE).
- **"I need to understand how it all fits together first."** [Platform Architecture](architecture.md) is the technical deep dive: compositors, encoding paths, transport, and process supervision.
- **"I need to know what happens inside the container at boot."** [Baseimage Internals](baseimage-internals.md) documents the s6 service tree, the init scripts, Nginx, and every file in the downstream contract.
- **"I want to tweak a stock container without building an image."** [Customizing Containers](customization.md): Docker mods, custom scripts, custom services, and the persistent config surface.
- **"I am implementing a client or debugging the wire."** [The Streaming Protocol](protocol.md) documents the WebSocket message formats, binary frame headers, and the settings handshake.
- **"I want to hack on Selkies, pixelflux, or the dashboards."** [Development Environment](development.md) covers dev mode, live reload, and building each component from source.

## The mental model

Three ideas carry the entire developer story:

1. **The baseimage does everything generic.** TLS, auth, supervision, GPU detection, audio, input, the client. Your image adds packages and, at minimum, one line in an autostart file. Resist the urge to re solve problems the base already solves.
2. **Configuration is environment variables all the way down.** The same `SELKIES_*` settings that users tweak are your deployment API, including the `|locked` mechanism that turns a general purpose image into a locked kiosk without rebuilding.
3. **Session persistence is exactly `/config`.** Design your image so state the user cares about lands in the home directory, and image updates become free.
