# airctl

`airctl` is a gesture-driven “system control” tool (think `systemctl`, but for air/hand gestures).

It uses real-time hand tracking to recognize gestures and triggers OS-level actions such as:

- switching workspaces / Spaces
- showing an overview of all open windows (GNOME Overview / macOS Mission Control)
- (optionally) minimizing / maximizing the currently focused window

> Target platforms (current): **GNOME (Linux)** and **macOS 15**  
> Language (current): **Python** (planned migration to Rust later)

---

## Why airctl?

Building hand tracking from scratch is a deep research problem (datasets, models, latency, stability, edge cases).
`airctl` focuses on the part that _is_ fun and practical to build:

- a clean gesture-to-action engine
- robust gesture state handling (debounce / hold / cooldown)
- platform backends (GNOME, macOS) for reliable “window manager” actions
- a CLI workflow that feels like a system tool

---

## Features

### Hand tracking (input)

- Real-time webcam capture
- Hand landmarks extraction (e.g. MediaPipe-based)

### Gesture recognition (logic)

- Rule-based gestures (fast iteration for MVP)
- Smoothing / stabilization (planned)
- Gesture state machine (planned)

### Actions (output)

**GNOME (Linux)**

- Show Overview
- Workspace next/previous (configurable)
- Window actions via hotkeys / backend (WIP)

**macOS 15**

- Mission Control
- Space left/right
- Minimize focused window (Cmd+M)
- Fullscreen toggle (Ctrl+Cmd+F) (optional)

> Note: on Linux, action implementation depends on whether you are on **Wayland** or **Xorg**, and on your GNOME keybindings.

---

## Project structure (planned)

- `airctl/`
  - `src/` - Source codes
    - `capture/` - webcam capture
    - `tracker/` - hand landmarks provider
    - `gestures/` - gesture detection from landmarks
    - `actions/` - OS backends (gnome / macos)
    - `config/` - gesture → action mapping
  - `configs/` - sample configs
  - `docs/` - development notes
  - `cli.py` - `airctl` command entrypoint
  - `README.md` - You're here

---

## CLI (planned)

The CLI is intentionally `systemctl`-like.

- `airctl run`  
  Start the gesture loop (camera → gestures → actions)

- `airctl status`  
  Show basic runtime status (backend, fps, last gesture)

- `airctl actions list`  
  List actions supported by the current platform backend

- `airctl actions test <action>`  
  Trigger an action without gestures (for debugging)

- `airctl config show`  
  Print the active gesture bindings

- `airctl config edit`  
  Open the config in your editor

---

## Gesture set (MVP idea)

These are **examples** (final mapping will be configurable):

- **Open palm (hold)** → Overview / Mission Control
- **Swipe** → Workspace/Space next/prev
- **Fist (hold)** → Minimize focused window
- **Pinch in/out** → (optional) resize / zoom bindings

---

## Configuration

`airctl` is designed to be configurable:

- define gestures (with thresholds / hold time / cooldown)
- map gestures to actions per OS backend
- keep the “gesture engine” portable (future Rust migration)

---

## Roadmap

### MVP (Python)

- [ ] Webcam capture + landmarks
- [ ] Minimal gesture detection (palm / swipe / fist)
- [ ] macOS backend (hotkeys / AppleScript where needed)
- [ ] GNOME backend (start with hotkeys; Wayland/Xorg notes)
- [ ] Config file for bindings

### Hardening

- [ ] Debounce/cooldown to avoid repeated triggers
- [ ] Better gesture state machine
- [ ] On-screen debug overlay

### Rust migration (later)

- [ ] Keep gesture/action interfaces stable
- [ ] Move action engine + daemon to Rust
- [ ] Optionally move inference to ONNX Runtime in Rust

---

## Requirements (expected)

- Python 3.10+
- A working webcam
- OS permissions:
  - **macOS**: Accessibility permission (to send hotkeys / control UI)
  - **GNOME**: depends on Wayland vs Xorg and chosen backend

(Exact dependencies will be listed once the first working prototype is committed.)

---

## Development notes

### Platform limitations

- On **Wayland**, synthetic input/hotkey injection is more restricted than on Xorg.
  `airctl` may provide different backends or require user-side keybinding setup.

### Safety

This tool can generate system input events. Treat it like automation software:
review configs and test actions with `airctl actions test` before enabling always-on mode.

---

## License

TBD (MIT is a good default for an experiment/tool like this).

---

## Name

**airctl** - control your system “in the air”.
