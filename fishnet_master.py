#!/usr/bin/env python3
import os
from pathlib import Path

FISHNET_MASTER = Path.home() / "Desktop" / "Hand of God" / "Fishnet_Master"
VOLUMES = Path("/Volumes")
FISHNET_MASTER.mkdir(parents=True, exist_ok=True)

# Add aliases for all volumes
for vol in VOLUMES.iterdir():
    alias_path = FISHNET_MASTER / vol.name
    if not alias_path.exists():
        try:
            os.symlink(str(vol), str(alias_path))
            print(f"Created alias for {vol} -> {alias_path}")
        except Exception as e:
            print(f"Failed to create alias for {vol}: {e}")
    else:
        print(f"Alias already exists: {alias_path}")

# Add aliases for key folders/scripts
key_items = [
    Path.home() / "Desktop" / "NoizyFish",
    Path.home() / "Desktop" / "Hand of God",
    Path.home() / "Desktop" / "NoizyFish" / "Projects",
    Path.home() / "Desktop" / "NoizyFish" / "noizyfish_full_organizer.py",
    Path.home() / "Desktop" / "Hand of God" / "create_and_move_volume_aliases.py"
]
for item in key_items:
    alias_path = FISHNET_MASTER / item.name
    if item.exists() and not alias_path.exists():
        try:
            os.symlink(str(item), str(alias_path))
            print(f"Created alias for {item} -> {alias_path}")
        except Exception as e:
            print(f"Failed to create alias for {item}: {e}")
    elif alias_path.exists():
        print(f"Alias already exists: {alias_path}")

print("Fishnet Master setup complete in Hand of God.")
