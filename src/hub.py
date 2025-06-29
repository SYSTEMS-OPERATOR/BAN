"""Simple BAN Hub skeleton using the bleak library for Bluetooth scanning."""

import logging
import asyncio

try:
    from bleak import BleakScanner
except ImportError:
    BleakScanner = None

try:
    import wifi
except ImportError:
    wifi = None


async def scan_bluetooth_devices():
    if not BleakScanner:
        logging.warning("bleak is not installed. Bluetooth scanning unavailable.")
        return []
    logging.info("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()
    return [(d.address, d.name or "Unknown") for d in devices]


def scan_wifi_networks():
    if not wifi:
        logging.warning("wifi library is not installed. Wi-Fi scanning unavailable.")
        return []
    logging.info("Scanning for Wi-Fi networks...")
    cells = wifi.Cell.all('wlan0')
    return [(cell.ssid, cell.address) for cell in cells]


async def main():
    logging.basicConfig(level=logging.INFO)
    bt_devices = await scan_bluetooth_devices()
    for addr, name in bt_devices:
        logging.info("Found Bluetooth device %s at %s", name, addr)

    wifi_networks = scan_wifi_networks()
    for ssid, bssid in wifi_networks:
        logging.info("Found Wi-Fi network %s at %s", ssid, bssid)


if __name__ == "__main__":
    asyncio.run(main())
