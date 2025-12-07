#!/usr/bin/env python3
import os
from pathlib import Path

HAND_OF_GOD = Path.home() / "Desktop" / "Hand of God"
SUBFOLDER = HAND_OF_GOD / "Volume_Aliases"
VOLUMES = Path("/Volumes")
SUBFOLDER.mkdir(parents=True, exist_ok=True)

for vol in VOLUMES.iterdir():
    alias_path = SUBFOLDER / vol.name
    if not alias_path.exists():
        try:
            os.symlink(str(vol), str(alias_path))
            print(f"Created alias for {vol} -> {alias_path}")
        except Exception as e:
            print(f"Failed to create alias for {vol}: {e}")
    else:
        print(f"Alias already exists: {alias_path}")

print("All volume aliases created in Hand of God's Volume_Aliases subfolder.")
