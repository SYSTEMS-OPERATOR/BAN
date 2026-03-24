## Overview
Catalog of all agent-like entities in the codebase (workers, daemons, bots, async routines, etc).  
Purpose: Clarity, maintainability, zero confusion.

---

### BluetoothScanRoutine
- **Purpose:** Asynchronously discovers nearby Bluetooth devices using bleak.
- **Location:** `src/hub.py` (`scan_bluetooth_devices` coroutine)
- **Interface:** `async def scan_bluetooth_devices()` returns a list of `(address, name)` tuples.
- **Triggers:** Invoked by `main()` or any caller needing a Bluetooth scan.
- **Behaviors:** Logs a warning if bleak is unavailable, otherwise performs a discovery scan.
- **Tests:** `tests/test_hub.py`

### WiFiScanRoutine
- **Purpose:** Discovers nearby Wi-Fi networks using the optional `wifi` package.
- **Location:** `src/hub.py` (`scan_wifi_networks` function)
- **Interface:** `def scan_wifi_networks(interface: str = "wlan0")` returns a list of `(ssid, bssid)` tuples.
- **Triggers:** Invoked by `main()` or any caller needing a Wi-Fi scan.
- **Behaviors:** Logs a warning if `wifi` is unavailable, otherwise scans the requested interface.
- **Tests:** `tests/test_hub.py`

### LoggingConfigRoutine
- **Purpose:** Defines consistent runtime logging configuration for hub execution.
- **Location:** `src/hub.py` (`configure_logging` function)
- **Interface:** `def configure_logging() -> None`
- **Triggers:** Called by `main()` during startup.
- **Behaviors:** Sets INFO logging level and unified formatter for hub logs.
- **Tests:** covered indirectly by runtime execution paths.

### HubMainLoop
- **Purpose:** Coordinates Bluetooth and Wi-Fi scans when the hub starts.
- **Location:** `src/hub.py` (`main` coroutine)
- **Interface:** `async def main()`
- **Triggers:** Executed when running `python hub.py` or via the example script.
- **Behaviors:** Logs discovered Bluetooth devices and Wi-Fi networks.
- **Tests:** covered indirectly via unit tests of scan routines.
