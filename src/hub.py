"""Simple BAN Hub skeleton."""

import logging

try:
    import bluetooth
except ImportError:
    bluetooth = None

try:
    import wifi
except ImportError:
    wifi = None


def scan_bluetooth_devices():
    if not bluetooth:
        logging.warning(
            "PyBluez is not installed. Bluetooth scanning unavailable."
        )
        return []
    logging.info("Scanning for Bluetooth devices...")
    return bluetooth.discover_devices(duration=8, lookup_names=True)


def scan_wifi_networks():
    if not wifi:
        logging.warning(
            "wifi library is not installed. Wi-Fi scanning unavailable."
        )
        return []
    logging.info("Scanning for Wi-Fi networks...")
    cells = wifi.Cell.all('wlan0')
    return [(cell.ssid, cell.address) for cell in cells]


def main():
    logging.basicConfig(level=logging.INFO)
    bt_devices = scan_bluetooth_devices()
    for addr, name in bt_devices:
        logging.info("Found Bluetooth device %s at %s", name, addr)

    wifi_networks = scan_wifi_networks()
    for ssid, bssid in wifi_networks:
        logging.info("Found Wi-Fi network %s at %s", ssid, bssid)


if __name__ == "__main__":
    main()
