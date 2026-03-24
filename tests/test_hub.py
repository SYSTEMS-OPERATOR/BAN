"""Unit tests for BAN hub discovery routines."""

import asyncio
from types import SimpleNamespace

from src import hub


class DummyDevice:
    """Simple BLE device fixture for tests."""

    def __init__(self, address: str, name: str | None) -> None:
        self.address = address
        self.name = name


def test_scan_bluetooth_devices_returns_normalized_devices(monkeypatch):
    """Bluetooth scan returns address/name tuples and fills unknown names."""

    class DummyScanner:
        """Stub scanner with deterministic device list."""

        @staticmethod
        async def discover():
            return [
                DummyDevice("AA:BB:CC:DD:EE:FF", "Tester"),
                DummyDevice("11:22:33:44:55:66", None),
            ]

    monkeypatch.setattr(hub, "BleakScanner", DummyScanner)

    devices = asyncio.run(hub.scan_bluetooth_devices())

    assert devices == [
        ("AA:BB:CC:DD:EE:FF", "Tester"),
        ("11:22:33:44:55:66", "Unknown"),
    ]


def test_scan_bluetooth_devices_without_bleak(monkeypatch):
    """Bluetooth scan safely degrades when bleak is unavailable."""
    monkeypatch.setattr(hub, "BleakScanner", None)

    devices = asyncio.run(hub.scan_bluetooth_devices())

    assert devices == []


def test_scan_wifi_networks_returns_normalized_cells(monkeypatch):
    """Wi-Fi scan returns SSID/BSSID pairs from the selected interface."""

    called = {}

    def fake_all(interface):
        called["interface"] = interface
        return [
            SimpleNamespace(ssid="BAN-NET", address="00:11:22:33:44:55"),
            SimpleNamespace(ssid="Guest", address="AA:AA:AA:AA:AA:AA"),
        ]

    dummy_wifi = SimpleNamespace(Cell=SimpleNamespace(all=fake_all))
    monkeypatch.setattr(hub, "wifi", dummy_wifi)

    networks = hub.scan_wifi_networks(interface="test0")

    assert called["interface"] == "test0"
    assert networks == [
        ("BAN-NET", "00:11:22:33:44:55"),
        ("Guest", "AA:AA:AA:AA:AA:AA"),
    ]


def test_scan_wifi_networks_without_wifi(monkeypatch):
    """Wi-Fi scan safely degrades when wifi dependency is unavailable."""
    monkeypatch.setattr(hub, "wifi", None)

    networks = hub.scan_wifi_networks()

    assert networks == []
