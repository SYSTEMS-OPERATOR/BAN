# Body Area Network Hub (BAN Hub)

BAN Hub is a lightweight Python project for discovering nearby wearable/sensor connectivity endpoints over Bluetooth and Wi-Fi.

## Core Capabilities
- Asynchronous Bluetooth scanning via `bleak` (when installed).
- Wi-Fi network scanning via `wifi` (when installed).
- Safe fallback behavior when optional dependencies are unavailable.
- Simple tuple outputs that are easy to integrate downstream.

## Directory Structure
- `docs/` — setup and contribution documentation.
- `hardware/` — hardware notes and assembly guidance.
- `src/` — runtime source code.
- `tests/` — unit tests for core logic.
- `examples/` — runnable usage example.

## Quick Start
1. Install dependencies:
   ```bash
   pip install -r src/requirements.txt
   ```
2. Run the hub:
   ```bash
   python src/hub.py
   ```

## Running Tests
```bash
pip install pytest
pytest -q
```

## Dev Agent Breadcrumbs
See logic breadcrumbs in:
- `src/hub.py`
- `examples/scan.py`
- `MIND.md`, `BODY.md`, `SOUL.md`
