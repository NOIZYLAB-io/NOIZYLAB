#!/usr/bin/env python3
import os
from pathlib import Path

HAND_OF_GOD = Path.home() / "Desktop" / "Hand of God"
SUBFOLDER = HAND_OF_GOD / "Volume_Aliases"
VOLUMES = Path("/Volumes")
SUBFOLDER.mkdir(parents=True, exist_ok=True)

for vol in VOLUMES.iterdir():
    # Skip hidden/system volumes and non-directories
    if vol.name.startswith('.') or not vol.is_dir():
        continue
    alias_path = SUBFOLDER / vol.name
    if alias_path.exists():
        # Check if the existing alias is a symlink and points to the correct volume
        if alias_path.is_symlink() and os.readlink(str(alias_path)) == str(vol):
            print(f"Alias already exists and is correct: {alias_path}")
        else:
            print(f"Alias already exists but may be incorrect: {alias_path}")
        continue  # Skip to next volume if alias exists
    try:
        os.symlink(str(vol), str(alias_path))
        print(f"Created alias for {vol} -> {alias_path}")
    except PermissionError:
        print(f"Permission denied: Failed to create alias for {vol}")
    except Exception as e:
        print(f"Failed to create alias for {vol}: {e}")

print("All volume aliases created in Hand of God's Volume_Aliases subfolder.")
