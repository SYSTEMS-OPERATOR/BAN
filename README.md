# Body Area Network Hub (BAN Hub)
[![CI](https://github.com/yourorg/BAN/actions/workflows/python.yml/badge.svg)](https://github.com/yourorg/BAN/actions/workflows/python.yml)
[![codecov](https://codecov.io/gh/yourorg/BAN/branch/main/graph/badge.svg)](https://codecov.io/gh/yourorg/BAN)

This project aims to provide a universal hub for managing personal devices such as wearables and sensors. It supports Bluetooth (via the `bleak` library) and Wi-Fi communication with optional USB connectivity.

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
   ```
3. Run the hub:
   ```bash
   python hub.py
   ```

Refer to `docs/setup.md` for more details.

## Running Tests

Run the test suite with `pytest`. Ensure the required testing
dependencies are installed first:

```bash
pip install -r src/requirements.txt
pip install pytest pytest-asyncio pytest-cov
pytest
```

