# MIND.md — BAN Cognitive Map

## Intent
BAN is designed as a lightweight hub that discovers nearby Bluetooth and Wi-Fi devices with safe fallbacks when optional dependencies are unavailable.

## Logic Flow (Dev Agent Breadcrumbs)
1. Start in `src/hub.py::main`.
2. Configure logging once.
3. Run Bluetooth discovery asynchronously.
4. Run Wi-Fi discovery synchronously.
5. Normalize findings into simple tuples for portability.

## Decision Rules
- If `bleak` is not installed, return an empty Bluetooth result and emit a warning.
- If `wifi` is not installed, return an empty Wi-Fi result and emit a warning.
- Device names missing from Bluetooth scans are normalized to `"Unknown"`.

## Near-Term Improvements
- Make Wi-Fi interface configurable via environment variables or CLI flags.
- Add retry policies and scan timeout controls.
- Add structured output mode for integration with external services.
