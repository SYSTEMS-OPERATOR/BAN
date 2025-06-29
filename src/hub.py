"""Simple BAN Hub skeleton."""

import argparse
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


def scan_wifi_networks(interface: str = "wlan0"):
    if not wifi:
        logging.warning(
            "wifi library is not installed. Wi-Fi scanning unavailable."
        )
        return []
    logging.info("Scanning for Wi-Fi networks on %s...", interface)
    cells = wifi.Cell.all(interface)
    return [(cell.ssid, cell.address) for cell in cells]


def main(argv: list[str] | None = None) -> None:
    """Run the BAN Hub scanner."""
    parser = argparse.ArgumentParser(description="BAN Hub scanner")
    parser.add_argument(
        "-b",
        "--bluetooth",
        action="store_true",
        help="Scan for Bluetooth devices",
    )
    parser.add_argument(
        "-w",
        "--wifi",
        action="store_true",
        help="Scan for Wi-Fi networks",
    )
    parser.add_argument(
        "-i",
        "--interface",
        default="wlan0",
        help="Wi-Fi interface to scan",
    )
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO)

    if not args.bluetooth and not args.wifi:
        args.bluetooth = args.wifi = True

    if args.bluetooth:
        bt_devices = scan_bluetooth_devices()
        for addr, name in bt_devices:
            logging.info("Found Bluetooth device %s at %s", name, addr)

    if args.wifi:
        wifi_networks = scan_wifi_networks(args.interface)
        for ssid, bssid in wifi_networks:
            logging.info("Found Wi-Fi network %s at %s", ssid, bssid)


if __name__ == "__main__":
    main()
