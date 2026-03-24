"""BAN hub routines for Bluetooth and Wi-Fi discovery.

Dev Agent Breadcrumbs
---------------------
1. ``main`` orchestrates startup and scan execution.
2. ``scan_bluetooth_devices`` returns normalized Bluetooth records.
3. ``scan_wifi_networks`` returns normalized Wi-Fi records.
"""

from __future__ import annotations

import asyncio
import logging
from typing import List, Tuple

LOGGER = logging.getLogger(__name__)
WIFI_INTERFACE = "wlan0"

try:
    from bleak import BleakScanner
except ImportError:  # pragma: no cover - environment dependent import
    BleakScanner = None

try:
    import wifi
except ImportError:  # pragma: no cover - environment dependent import
    wifi = None


def configure_logging() -> None:
    """Configure application logging for the BAN hub runtime."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


async def scan_bluetooth_devices() -> List[Tuple[str, str]]:
    """Scan for Bluetooth devices and return ``(address, name)`` pairs."""
    if BleakScanner is None:
        LOGGER.warning(
            "bleak is not installed. Bluetooth scanning unavailable."
        )
        return []

    LOGGER.info("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()
    return [(device.address, device.name or "Unknown") for device in devices]


def scan_wifi_networks(
    interface: str = WIFI_INTERFACE,
) -> List[Tuple[str, str]]:
    """Scan for Wi-Fi networks and return ``(ssid, bssid)`` pairs."""
    if wifi is None:
        LOGGER.warning(
            "wifi library is not installed. Wi-Fi scanning unavailable."
        )
        return []

    LOGGER.info("Scanning for Wi-Fi networks on interface %s...", interface)
    cells = wifi.Cell.all(interface)
    return [(cell.ssid, cell.address) for cell in cells]


async def main() -> None:
    """Run the BAN hub startup sequence and emit discovery results."""
    configure_logging()

    bluetooth_devices = await scan_bluetooth_devices()
    for address, name in bluetooth_devices:
        LOGGER.info("Found Bluetooth device %s at %s", name, address)

    wifi_networks = scan_wifi_networks()
    for ssid, bssid in wifi_networks:
        LOGGER.info("Found Wi-Fi network %s at %s", ssid, bssid)


if __name__ == "__main__":
    asyncio.run(main())
