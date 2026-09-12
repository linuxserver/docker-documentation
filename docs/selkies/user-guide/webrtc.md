# WebRTC Transport

Selkies streams over WebSockets by default, and for most people that is the right choice: one TCP connection, works through any reverse proxy, no firewall rules beyond the web port. An opt in WebRTC transport carries the same H.264 video, Opus audio, and input over UDP instead. This page explains when it is worth turning on, how the containers enable it, and the networking it needs.

!!! note "WebSockets stays the default"
    Nothing on this page applies until you deliberately switch a container to WebRTC. If your desktop streams fine today, you do not need any of it.

## When to use it

WebRTC helps when the path between the browser and the container is lossy or has variable latency, typically a mobile network, a long haul link, or a wireless client on a congested network. UDP does not stall on a lost packet the way TCP does, the audio pacer keeps sound and input responsive while video is squeezed, and congestion control can adapt the bitrate to what the link actually delivers.

The trade offs:

- **Only `h264enc` streams over WebRTC.** The striped H.264 and JPEG encoders are WebSocket only, and the encoder menu is narrowed to what WebRTC can carry while it is the active transport. The previous choice is restored when switching back.
- **Rate control defaults to CBR.** A congestion controlled transport needs the encoder holding a bandwidth target, so `SELKIES_VIDEO_BITRATE` becomes the setting you tune rather than CRF. Pin `SELKIES_RATE_CONTROL_MODE` if you want otherwise.
- **UDP has to get through.** A reverse proxy alone is not enough. Media takes a direct path from the container to the browser, and something has to make that path reachable: forwarded ports, a public address, or a TURN relay.
- **Turbo mode and paint over still apply.** Damage tracking and paint over work on both transports.

## Enabling it in the containers

The baseimage keeps WebRTC hidden until you configure it. Set `SELKIES_MODE=webrtc`, or any WebRTC, STUN, TURN, or Cloudflare variable from the [configuration reference](configuration.md#webrtc-networking-stun-and-turn), and the container:

1. Sets `SELKIES_MODE=webrtc` if you have not set a mode yourself, so new clients start on WebRTC.
2. Sets `SELKIES_ENABLE_DUAL_MODE=true` so the transport switch appears in the sidebar and users can fall back to WebSockets at will.

Without any of those variables the switch is hidden and the container is WebSocket only, exactly as before. Anything you set explicitly wins, so `SELKIES_MODE=websockets` plus a TURN host gives you a WebSocket default with WebRTC available in the menu, and `SELKIES_ENABLE_DUAL_MODE=false` plus `SELKIES_MODE=webrtc` gives you WebRTC with no way back.

The simplest working setup forwards one extra UDP port next to the web port:

```yaml
---
services:
  webtop:
    image: lscr.io/linuxserver/webtop:latest
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - SELKIES_MODE=webrtc
      - SELKIES_WEBRTC_UDP_MUX_PORT=59000
    ports:
      - 3001:3001
      - 59000:59000/udp
    shm_size: 1gb
    restart: unless-stopped
```

That is enough for clients on the same LAN as the Docker host. The rest of this page explains why the extra port is needed and what to add when clients are further away.

## How the connection is built

Two connections are involved, and it helps to keep them apart when something fails:

| Connection | Path | What it carries |
| --- | --- | --- |
| Signaling | The container's normal web port (3000 or 3001, or your reverse proxy), over the same WebSocket path the client already uses | Session description and ICE candidates, then settings, clipboard, files, and stats over the data channel once the peer connection is up |
| Media | Direct UDP (or TCP when muxing is configured) from the container to the browser | Video, audio, microphone, and webcam |

If the web client loads and the sidebar works but the desktop never appears, the media path is what is broken. That is the case every section below is about.

ICE, the negotiation that picks the media path, tries candidates in order of preference: a direct host address, then a server reflexive address discovered through STUN, then a TURN relay. The stats section of the sidebar shows which one won, `relay` means every packet is going through your TURN server.

## Making the media path reachable

Pick the first row that matches your deployment.

| Situation | What to do |
| --- | --- |
| Client and container on the same LAN | Forward one UDP port and tell Selkies about it, see [UDP mux](#one-forwarded-port-udp-mux) |
| Container has a public IP, or sits behind static 1:1 NAT (a cloud instance with an elastic IP) | Forward one UDP port, set `SELKIES_WEBRTC_PUBLIC_IP` to the public address, optionally enable ICE-lite |
| Clients on networks that block UDP | Add a TCP mux port, ideally `443` |
| Container behind NAT you cannot forward through, or many clients on hostile networks | Run or rent a [TURN server](#turn-servers) |

### One forwarded port (UDP mux)

By default every WebRTC session binds its own ephemeral UDP ports, which inside a container means the browser is handed addresses it cannot reach. `SELKIES_WEBRTC_UDP_MUX_PORT` replaces that with one port that all sessions share, sessions are told apart by their ICE credentials. Forward that single port without remapping, as in the example above, and you are done. Always set it, the alternative is publishing the whole 49152 to 65535 range.

`SELKIES_WEBRTC_PORT_RANGE=50000-50100` is the alternative for schedulers that allot each session a small window of ports. Forward the same range with `-p 50000-50100:50000-50100/udp`. A range is ignored when a mux port is set.

A port already in use fails the container at startup rather than the first session, since a session that silently bound elsewhere would be unreachable through the forwarded port.

### Public address and static NAT

On a cloud instance the container gathers its private address as a host candidate, which a remote browser cannot reach, and the connection falls through to TURN or fails. `SELKIES_WEBRTC_PUBLIC_IP` substitutes your public IPv4 and/or IPv6 address into the host candidates. STUN and TURN candidates are left alone, so hole punching and relay fallback still work.

`SELKIES_WEBRTC_ICE_LITE=true` is a good companion here. The server then offers host candidates only and answers the browser's connectivity checks instead of running its own, which is all a server with a reachable address needs. The browser still gets STUN and TURN for candidates of its own.

```yaml
    environment:
      - SELKIES_MODE=webrtc
      - SELKIES_WEBRTC_UDP_MUX_PORT=59000
      - SELKIES_WEBRTC_TCP_MUX_PORT=59000
      - SELKIES_WEBRTC_PUBLIC_IP=203.0.113.5
      - SELKIES_WEBRTC_ICE_LITE=true
    ports:
      - 3001:3001
      - 59000:59000/udp
      - 59000:59000/tcp
```

### Clients that cannot use UDP

`SELKIES_WEBRTC_TCP_MUX_PORT` makes the server accept ICE-TCP on one TCP port and advertise it next to the UDP candidates. Browsers prefer UDP whenever it works and only fall to TCP when it does not. It may share its number with the UDP mux port, and `443` is the usual choice on a public deployment because corporate firewalls pass it. Media over TCP costs latency under loss, so keep UDP reachable where you can.

## STUN and TURN

STUN lets both ends discover their public addresses, TURN relays media when no direct path exists. Selkies ships with working defaults for casual use and you should replace both for anything serious:

- **STUN** defaults to Google's public server. On a private network with no internet access point `SELKIES_STUN_HOST` and `SELKIES_STUN_PORT` at your own STUN or TURN server or connections will hang looking for it.
- **TURN** defaults to the free [Open Relay](https://www.metered.ca/tools/openrelay) service. It has one location and a shared public secret, so any `relay` connection through it adds real latency and stutter. Treat it as a demo.

### Choosing a TURN server

| Option | Fit |
| --- | --- |
| [Cloudflare TURN](https://developers.cloudflare.com/calls/turn/overview/) | Easiest managed option, geodistributed, free for the first 1000 GB a month. Set `SELKIES_ENABLE_CLOUDFLARE_TURN=true`, `SELKIES_CLOUDFLARE_TURN_TOKEN_ID`, and `SELKIES_CLOUDFLARE_TURN_API_TOKEN` |
| [coturn](https://github.com/coturn/coturn) | The standard self hosted server, available as `coturn/coturn` on Docker Hub or from every distro. Place it as close to your clients as you can |
| [eturnal](https://eturnal.net), [Pion TURN](https://github.com/pion/turn), [STUNner](https://github.com/l7mp/stunner) | Alternatives, STUNner is the Kubernetes native one |

### Pointing Selkies at your TURN server

Four authentication methods are supported and they override each other in this order:

1. **RTC config JSON** (`SELKIES_RTC_CONFIG_JSON`): a file with a complete ICE server configuration, re-read periodically so rotated credentials are picked up. When the file exists everything below is ignored.
2. **TURN REST API** (`SELKIES_TURN_REST_URI` and `SELKIES_TURN_REST_API_KEY`): a service that mints time limited credentials on request, the right answer for multi user deployments where users should not hold the TURN secret.
3. **Shared secret** (`SELKIES_TURN_SHARED_SECRET` with `SELKIES_TURN_HOST` and `SELKIES_TURN_PORT`): Selkies generates time limited HMAC credentials itself from coturn's `static-auth-secret`.
4. **Long term credentials** (`SELKIES_TURN_USERNAME` and `SELKIES_TURN_PASSWORD` with host and port): a fixed username and password, coturn's `lt-cred-mech`.

The last two put the TURN secret inside the container, which is fine when you own both ends. `SELKIES_TURN_PROTOCOL=tcp` and `SELKIES_TURN_TLS=true` apply to the shared secret and long term methods and tell the browser how to reach the relay.

A minimal self hosted pairing with coturn on the same host, using a shared secret:

```yaml
---
services:
  coturn:
    image: coturn/coturn:latest
    command: >
      -n --listening-ip=0.0.0.0 --listening-ip=::
      --listening-port=3478 --realm=example.org
      --external-ip=203.0.113.5
      --min-port=65500 --max-port=65535
      --use-auth-secret --static-auth-secret=change-me-to-a-long-random-string
    ports:
      - 3478:3478
      - 3478:3478/udp
      - 65500-65535:65500-65535/udp
    restart: unless-stopped

  webtop:
    image: lscr.io/linuxserver/webtop:latest
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - SELKIES_MODE=webrtc
      - SELKIES_TURN_HOST=turn.example.org
      - SELKIES_TURN_PORT=3478
      - SELKIES_TURN_SHARED_SECRET=change-me-to-a-long-random-string
      - SELKIES_STUN_HOST=turn.example.org
      - SELKIES_STUN_PORT=3478
    ports:
      - 3001:3001
    shm_size: 1gb
    restart: unless-stopped
```

Open `3478` for TCP and UDP plus the relay range `65500-65535` UDP on the coturn host's firewall. Keep the relay range small, Docker publishes each port individually and a wide range slows container startup. coturn also answers STUN, which is why the example points `SELKIES_STUN_HOST` at it too. For TURN over TLS add `--cert` and `--pkey` with a certificate from a real CA and set `SELKIES_TURN_TLS=true`.

The upstream [WebRTC and Firewall Issues](https://docs.selkies.io/firewall) page covers coturn configuration files, Kubernetes deployments, and the TURN REST API in far more depth.

## Reverse proxies

Nothing changes at your reverse proxy. Signaling goes through the container's web port exactly like the WebSocket transport, so a proxy set up per the [Reverse Proxy](reverse-proxy.md) page already handles it, SWAG included. Media never touches the proxy. If your proxy is on a different host than the container, the port forwarding and public IP settings above refer to the container host, not the proxy.

## Troubleshooting

- **Client loads, transport switch shows WebRTC, no picture.** ICE failed. Switch to WebSockets in the sidebar to confirm everything else works, then check the media path: is the UDP mux port forwarded, is `SELKIES_WEBRTC_PUBLIC_IP` set on a NAT host, can the browser reach the TURN server?
- **Works on the LAN, fails from outside.** Host candidates are private addresses. Set `SELKIES_WEBRTC_PUBLIC_IP` or configure TURN.
- **Works but stutters, stats say `relay`.** You are on the default Open Relay TURN or a distant relay. Fix the direct path so the browser never needs the relay, or move the TURN server closer.
- **Fails on one specific network only.** That network blocks UDP. Add a TCP mux port on `443` or set `SELKIES_TURN_PROTOCOL=tcp`.
- **Container will not start after adding a mux port.** The port is taken on the host, pick another.
- **Need more detail.** `SELKIES_DEBUG=true` logs ICE candidate gathering and selection, and `SELKIES_ENABLE_WEBRTC_STATISTICS=true` dumps per session CSVs into `SELKIES_WEBRTC_STATISTICS_DIR`.
