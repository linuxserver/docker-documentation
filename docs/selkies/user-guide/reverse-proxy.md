# Reverse Proxy

Putting a Selkies container behind a reverse proxy gets you real TLS certificates, clean hostnames, and a place to hang serious authentication. The containers are designed for it.

## The rules

1. **Proxy to port 3000 (HTTP)**, and let your proxy terminate TLS. The container's port 3001 self signed HTTPS is for direct access; double TLS is pointless.
2. **WebSocket upgrades must pass through.** All streaming rides a WebSocket at `<path>/websocket`. Any proxy that handles `Upgrade` and `Connection` headers works.
3. **Long timeouts.** Sessions are long lived connections. Set read and send timeouts to an hour (the internal Nginx uses 3600s), or idle sessions will drop.
4. **Client must still reach you over HTTPS.** The browser APIs need a secure context, so your proxy must serve HTTPS to the user.

## SWAG

[SWAG](https://github.com/linuxserver/docker-swag) ships preset configs for many of these containers. Enable the relevant proxy conf (for example `chromium.subdomain.conf.sample`), point it at your container, and you are done, including automatic Let's Encrypt certificates. SWAG is the path of least resistance and the one the LinuxServer team supports directly.

## Plain Nginx example (subdomain)

```nginx
server {
    listen 443 ssl;
    server_name desktop.example.org;

    # your ssl_certificate / ssl_certificate_key here

    location / {
        proxy_pass http://<container-host>:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
        proxy_buffering off;
        client_max_body_size 0;
    }
}
```

`client_max_body_size` matters for file uploads into the session.

## Subfolder proxying

To serve a container under a path like `https://example.org/desktop/`, set the `SUBFOLDER` variable on the **container** so its internal routes match:

```yaml
    environment:
      - SUBFOLDER=/desktop/
```

Both slashes are required. Then proxy the location through:

```nginx
    location /desktop/ {
        proxy_pass http://<container-host>:3000/desktop/;
        # same upgrade headers and timeouts as above
    }
```

## Authentication at the proxy

This is where real auth belongs for internet facing deployments. Common patterns:

- **Authelia or Authentik** forward auth in front of the container location.
- **Basic auth at the proxy** as a floor, still better managed there than in the container.
- Keep the container's own `CUSTOM_USER` and `PASSWORD` as an inner layer if you like defense in depth; the proxy can inject the `Authorization` header upstream so users only log in once.

If you are heading toward many users and many apps, that is exactly what [SealSkin](../components/sealskin.md) automates, including per session credentials and path based session routing.

## Known sharp edges

- The container substitutes `SUBFOLDER` and auth settings into its Nginx config with simple string replacement at startup. Exotic characters in passwords or paths can break the substitution, keep them simple.
- Server side events and the streaming WebSocket dislike buffering proxies, always disable response buffering (`proxy_buffering off` or your proxy's equivalent).
- If the client loads but you get a black screen or no video, it is almost always a blocked WebSocket upgrade or an HTTP (not HTTPS) page context.
