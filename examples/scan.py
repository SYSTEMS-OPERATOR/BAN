"""Example script that scans for nearby Bluetooth and Wi-Fi devices using the hub."""
from pathlib import Path
import sys

# Ensure src directory is on path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from hub import main
import asyncio

if __name__ == '__main__':
    asyncio.run(main())

