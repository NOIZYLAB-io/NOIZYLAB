from pathlib import Path
import os

VOLUMES = Path("/Volumes")
SUBFOLDER = Path("/Users/rsp_ms/Desktop/Hand of God/Volume_Aliases")
SUBFOLDER.mkdir(parents=True, exist_ok=True)

SKIP_VOLUMES = {"Macintosh HD", "Recovery", "Preboot"}  # Add any volume names to skip

for vol in VOLUMES.iterdir():
    # Skip hidden/system volumes, non-directories, or volumes in SKIP_VOLUMES
    if vol.name.startswith('.') or not vol.is_dir() or vol.name in SKIP_VOLUMES:
        continue
    alias_path = SUBFOLDER / vol.name
    if alias_path.exists():
        if alias_path.is_symlink() and os.readlink(str(alias_path)) == str(vol):
            print(f"Alias already exists and is correct: {alias_path}")
        else:
            print(f"Alias already exists but may be incorrect: {alias_path}")
        continue
    try:
        os.symlink(str(vol), str(alias_path))
        print(f"Created alias for {vol} -> {alias_path}")
    except PermissionError:
        print(f"Permission denied: Failed to create alias for {vol}")
    except Exception as e:
        print(f"Failed to create alias for {vol}: {e}")

print("All volume aliases created in Hand of God's Volume_Aliases subfolder.")
