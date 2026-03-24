# BODY.md — BAN Physical/Runtime Surface

## Runtime Components
- **BluetoothScanRoutine**: async BLE scanner backed by `bleak`.
- **WiFiScanRoutine**: sync Wi-Fi scanner backed by `wifi`.
- **HubMainLoop**: orchestration entrypoint that executes scan routines.

## Inputs and Outputs
- **Bluetooth output:** list of `(address, name)` tuples.
- **Wi-Fi output:** list of `(ssid, bssid)` tuples.
- **Logging output:** informational and warning logs for scan state and results.

## Operational Constraints
- Bluetooth and Wi-Fi dependencies are optional and can be missing in minimal environments.
- Default Wi-Fi interface is `wlan0`; callers may pass a different interface name.
- Tests are deterministic through dependency monkeypatching.

## Validation Surface
- Unit tests in `tests/test_hub.py` cover:
  - successful Bluetooth normalization,
  - Bluetooth dependency-missing fallback,
  - successful Wi-Fi normalization,
  - Wi-Fi dependency-missing fallback.
