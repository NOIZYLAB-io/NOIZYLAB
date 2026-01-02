#!/usr/bin/env python3
import os
from pathlib import Path
import subprocess
import time

HAND_OF_GOD = Path.home() / "Desktop" / "Hand of God"
VOLUMES = Path("/Volumes")
HAND_OF_GOD.mkdir(parents=True, exist_ok=True)

def create_volume_aliases():
    for vol in VOLUMES.iterdir():
        alias_path = HAND_OF_GOD / vol.name
        if not alias_path.exists():
            try:
                os.symlink(str(vol), str(alias_path))
                print(f"Created alias for {vol} -> {alias_path}")
            except Exception as e:
                print(f"Failed to create alias for {vol}: {e}")
        else:
            print(f"Alias already exists: {alias_path}")
    print("All volume aliases created in Hand of God.")

def notify_completion():
    message = "Volume aliases are ready! You can close this tab."
    subprocess.run([
        "osascript",
        "-e",
        f'display notification "{message}" with title "VS Code Task Complete"'
    ])

if __name__ == "__main__":
    create_volume_aliases()
    time.sleep(2)
    notify_completion()

"workbench.colorCustomizations": {
    "chat.background": "#4B2E19"
}
