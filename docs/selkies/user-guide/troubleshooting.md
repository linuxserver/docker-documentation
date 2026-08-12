# Troubleshooting

## Step zero: the minimal command

Before anything else, reduce to the minimal command for your image:

```bash
docker run --rm -it --shm-size=1gb -p 3001:3001 lscr.io/linuxserver/<app>:latest bash
```

The trailing `bash` gives you a shell in the container for poking around, `ctrl+d` exits and cleans up.

and browse to `https://localhost:3001` from the Docker host if possible.

- **Works?** Your problem is in your added options. Re-add them one at a time: volume, env vars, GPU flags, proxy. The last addition before it breaks is your culprit.
- **Still broken?** You now have a one line reproduction. Grab the container logs and open an issue on the app's repository, this is exactly the report maintainers want.

This loop resolves the majority of reports, particularly GPU and reverse proxy issues.

## Quick reference table

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Page loads, no video, or "insecure context" errors | Browsing plain HTTP | Use `https://host:3001`, or fix TLS at your proxy. WebCodecs requires a secure context |
| Black screen behind the UI | WebSocket blocked | Check reverse proxy `Upgrade` headers and timeouts, see [Reverse Proxy](reverse-proxy.md) |
| Applications crash inside the session | Shared memory too small | `--shm-size=1gb` |
| Container restarts or app crashes on old hardware or NAS | Old kernel or libseccomp blocking syscalls | Try `--security-opt seccomp=unconfined` (understand the [security cost](security.md#container-isolation-options)) |
| Blurry colored text | 4:2:0 chroma subsampling | Enable FullColor 4:4:4 in the sidebar or use the JPEG encoder, note the [Intel and AMD caveat](gpu.md#fullcolor-444-and-hardware-encoders) |
| Choppy video during motion | CPU limited or bandwidth limited | Check the Stats section, lower FPS or raise CRF, try Turbo mode off, consider a [GPU](gpu.md) |
| Cursor feels laggy in games | Absolute pointer mode | Use Gaming mode (pointer lock) |
| Gamepad not detected in app | App does not use the joystick API path | Some apps are incompatible with the userspace interposer; try another input mode in app, or file an issue |
| Files will not upload | Proxy body size limit | Raise `client_max_body_size` at your proxy |
| Auth prompt not appearing | `PASSWORD` unset | Both `CUSTOM_USER` and `PASSWORD` behavior: no password means no auth |
| Volume permission errors in `/config` | PUID and PGID mismatch | Set them to your host user's `id` values |

## GPU problems

Work through the ladder in [GPU Acceleration](gpu.md#debugging-gpu-problems). Summary:

1. Confirm the container works with no GPU flags at all.
2. Add only the device mount and watch the startup logs for detection messages.
3. Verify inside the container: run `vkcube` in a session terminal, a smoothly spinning cube and the GPU listed in the terminal means the GPU path works. `vainfo` for Intel and AMD and `nvidia-smi` for Nvidia confirm device visibility.
4. Nvidia specifics: driver installed from the `.run` file, `--device /dev/nvidia-modeset` for Vulkan (drivers 595.80 and newer need nothing else), kernel parameters `nvidia-drm.modeset=1 nvidia_drm.fbdev=1` on drivers below 595.80, and no Nvidia support on Alpine images.
5. Multi GPU: pin `DRINODE` and `DRI_NODE` explicitly, remember they must match for zero copy.

## Reading the logs

```bash
docker logs -f <container>
```

The startup sequence prints the s6 service initialization, GPU detection results, and the mode selection (Wayland vs X11). The pixelflux layer logs its encoding decision, look for lines telling you whether the zero copy path or a readback path was chosen, and which encoder is active.

For deeper debugging set `-e SELKIES_DEBUG=true`.

## Performance expectations

Calibrate before assuming a bug: a CPU only x86_64 host from the last decade comfortably serves a 1080p60 desktop session, and a budget N97 class mini PC has demonstrated eight simultaneous Firefox sessions running youtube. If you are far from that, the Stats sidebar (bandwidth, latency, FPS) will point at the bottleneck: network jitter shows up as latency spikes, CPU saturation as low server FPS, decode issues as low client FPS with fine server FPS.

## Getting help

- Each app image has its own issue tracker at `github.com/linuxserver/docker-<app>`.
- Platform wide discussion happens on the [LinuxServer.io Discord](https://linuxserver.io/discord) and forums.
- Include: the minimal command you tested, full container logs, host OS and kernel, browser and version, and GPU details if relevant.
