import logging
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import hub  # noqa: E402


def test_scan_functions_no_dependencies(monkeypatch, caplog):
    monkeypatch.setattr(hub, "bluetooth", None)
    monkeypatch.setattr(hub, "wifi", None)
    caplog.set_level(logging.WARNING)
    assert hub.scan_bluetooth_devices() == []
    assert "Bluetooth scanning unavailable" in caplog.text
    caplog.clear()
    assert hub.scan_wifi_networks("wlan0") == []
    assert "Wi-Fi scanning unavailable" in caplog.text


def test_main_scans(monkeypatch, caplog):
    monkeypatch.setattr(
        hub,
        "scan_bluetooth_devices",
        lambda: [("addr", "name")],
    )
    monkeypatch.setattr(
        hub,
        "scan_wifi_networks",
        lambda iface: [("ssid", "bssid")],
    )
    caplog.set_level(logging.INFO)
    hub.main([])
    assert "Found Bluetooth device" in caplog.text
    assert "Found Wi-Fi network" in caplog.text
