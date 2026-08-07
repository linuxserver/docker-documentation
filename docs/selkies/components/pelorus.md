# Pelorus

**Repository:** [linuxserver/pelorus](https://github.com/linuxserver/pelorus) · **Enable with:** `-e PELORUS=true` · **UI at:** `https://<host>:3001/pelorus/`

Pelorus is the agentic interface for Selkies desktops: an AI navigator that lets a chat LLM drive a real Linux desktop. It works with labwc sessions (single application containers) and full KDE Plasma desktops, and it is preinstalled in every Selkies baseimage, activated with a single environment variable.

The key idea that separates Pelorus from screenshot driven "computer use" agents: **the desktop is represented as text.** Window lists with exact geometry, accessibility trees with precise click coordinates for every button and menu item, taskbar and start menu contents, all delivered as structured text. A model never has to guess pixel coordinates from an image, which means even small quantized local models can operate the desktop reliably. Screenshots exist as a fallback for content that has no accessibility representation (games, canvases, some Electron apps).

## Enabling it

```bash
docker run --rm -it \
  --shm-size=1gb \
  -p 3001:3001 \
  -e PELORUS=true \
  lscr.io/linuxserver/chromium:latest bash
```

`PELORUS=true` in Wayland mode does all of this automatically:

- Starts the Pelorus FastAPI server (port 5100 internally, proxied by the container's Nginx at `/pelorus/`)
- Enables the pixelflux **Computer Use API** on port 5000 internally (`PIXELFLUX_CU=5000`), the raw input injection and screenshot layer
- Starts the AT-SPI accessibility registry and forces the accessibility bridge on for GTK and Qt applications so their UI trees are readable
- On labwc, starts the compositor with its IPC socket (`labwc -i`) so windows can be enumerated; on KDE, window data comes from KWin over D-Bus

Open `https://<host>:3001/pelorus/` for the built in chat UI, or `.../pelorus/docs` for the OpenAPI reference.

## How the agent loop works

1. **Observe:** capture desktop state as text, the environment header, desktop icons, taskbar buttons, one line per window with PID, title, and geometry, plus any open start menu contents.
2. **Infer:** send state, system prompt, and the task to the configured model. Supported providers: **Ollama**, any **OpenAI compatible** endpoint, and **Gemini**.
3. **Act:** dispatch the model's tool calls, input actions go to the Computer Use backend, introspection actions are answered locally.
4. Repeat until the task completes or the step budget runs out.

The model gets three tools:

- **`computer`**: the workhorse. Actions include `desktop_state`, `explore_window` (dump a window's full accessibility tree with exact screen coordinates for every element), `key`, `type`, the click family, `scroll`, `left_click_drag`, `hold_key`, `wait`, and `close_window`. `explore_window` is the primary inspection tool; a vision screenshot of the window region is the fallback when a tree is unavailable.
- **`create_task`** and **`set_task_status`**: a small task queue so the agent can decompose work.

## Using Pelorus from your own code

You do not have to use the built in agent. The REST API exposes the desktop primitives directly, so an external agent (or your own orchestration) can be the brain. The full API reference with request and response schemas lives in [API.md in the Pelorus repository](https://github.com/linuxserver/pelorus/blob/master/API.md); the highlights:

| Endpoint | Purpose |
| --- | --- |
| `POST /api/run` | Run the built in agent on a task, optionally streaming steps over SSE |
| `GET /api/state` | The text based desktop state |
| `GET /api/windows` | Window list with geometry |
| `GET /api/desktop/explore/{pid}` | Accessibility tree for a window, coordinates enriched to absolute screen positions |
| `POST /api/desktop/control` | Raw input: clicks, typing, keys, scrolling, drags, screenshots, region zoom |
| `GET /api/desktop/screenshot` | Full desktop screenshot, base64 PNG |
| `POST /api/desktop/close/{pid}` | Close a window |
| `WS /ws` | Streaming agent protocol used by the chat UI |

Provider configuration lives at `/config/agent/config.toml` (auto created, seeded from `PELORUS_PROVIDER`, `PELORUS_ENDPOINT`, `PELORUS_MODEL`, and `PELORUS_API_KEY` environment variables), and can be managed at runtime through `/api/servers`.

## Configuration reference

| Variable | Default | Description |
| --- | --- | --- |
| `PELORUS` | unset | Set `true` in a baseimage container to enable the whole stack |
| `PELORUS_PORT` | `5100` | Internal API port |
| `PELORUS_PROVIDER` | `ollama` | `ollama`, an OpenAI compatible provider, or `gemini` |
| `PELORUS_ENDPOINT` | `http://localhost:11434` | Model endpoint URL |
| `PELORUS_MODEL` | `gemma4:12b` | Model name |
| `PELORUS_API_KEY` | empty | API key where the provider needs one |
| `PIXELFLUX_CU` | `5000` when `PELORUS=true` | Computer Use API port, set automatically |

## Security

Treat Pelorus as an unauthenticated root of control over the session:

- The API has **no authentication of its own**. In the containers it is reachable only through Nginx (which can carry the container's basic auth) and is not published directly. Never expose port 5100 or 5000 yourself.
- Configured provider API keys are stored in `/config/agent/config.toml` and are readable through the server management API, anyone who can reach the API can read them.
- Enabling the accessibility bridge means every process in the session can read the full UI text of every application. That is inherent to how AT-SPI works and is the price of text based desktop state.

The [Security and Hardening](../user-guide/security.md) page covers the container level mitigations.

## How it fits the stack

Pelorus is a consumer of two lower layers documented elsewhere: the pixelflux [Computer Use API](pixelflux.md) for input and pixels, and the compositor's window enumeration (the labwc IPC patch shipped in the [baseimages](baseimages.md), or KWin D-Bus on KDE). It adds the accessibility layer, the state formatting, the LLM providers, and the agent loop on top. If you are building your own agentic system, that layering is the map: you can plug in at any level.
