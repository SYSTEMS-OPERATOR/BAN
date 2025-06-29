# Body Area Network Hub (BAN Hub)

This project aims to provide a universal hub for managing personal devices such as wearables and sensors. It supports Bluetooth and Wi-Fi communication with optional USB connectivity.

## Directory Structure

- `docs/` — Documentation and setup guides.
- `hardware/` — Schematics and hardware assembly instructions.
- `src/` — Source code for the hub software.
- `examples/` — Sample scripts demonstrating hub usage.

## Quick Start

1. Assemble the hardware using the instructions in `hardware/`.
2. Install Python dependencies:
   ```bash
   cd src
   pip install -r requirements.txt
   # Bluetooth support requires PyBluez which may not
   # compile on Python versions newer than 3.10.
   # Skip this if installation fails or you don't need Bluetooth.
   pip install pybluez || true
   ```
3. Run the hub:
   ```bash
   python hub.py
   ```
4. Run lint and tests:
   ```bash
   flake8 src tests
   pytest -q
   ```

Refer to `docs/setup.md` for more details.
