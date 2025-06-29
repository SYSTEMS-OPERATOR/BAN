# Setup Guide

This document provides an overview of how to set up the BAN Hub.

1. Assemble the hardware following the instructions in the `hardware` directory.
2. Navigate to the `src` directory and install dependencies:
   ```bash
   pip install -r requirements.txt
   # Bluetooth support requires PyBluez, but it may not
   # compile on newer Python versions. Skip this step if
   # installation fails or you do not need Bluetooth.
   pip install pybluez || true
   ```
3. Run the hub to scan nearby devices:
   ```bash
   python hub.py
   ```
   See `python hub.py --help` for more options such as scanning only Wi-Fi or
   specifying a different interface.
