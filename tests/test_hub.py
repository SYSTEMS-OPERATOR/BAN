import pytest
import types
import asyncio

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

import hub

class DummyDevice:
    def __init__(self, address, name):
        self.address = address
        self.name = name

@pytest.mark.asyncio
async def test_scan_bluetooth_devices(monkeypatch):
    async def fake_discover():
        return [DummyDevice("AA:BB:CC:DD:EE:FF", "Tester")]

    class DummyScanner:
        @staticmethod
        async def discover():
            return await fake_discover()

    monkeypatch.setattr(hub, "BleakScanner", DummyScanner)
    devices = await hub.scan_bluetooth_devices()
    assert devices == [("AA:BB:CC:DD:EE:FF", "Tester")]

