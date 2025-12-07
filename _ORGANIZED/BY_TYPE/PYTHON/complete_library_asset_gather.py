import os
import shutil
from pathlib import Path

# Main library root
LIB_ROOT = Path("/Volumes/4TB Blue Fish/Native Instruments")
# Add 6TB as a search root
SEARCH_ROOTS = [
    Path("/Volumes/4TB Blue Fish"),
    Path("/Volumes/6TB/NI_2026"),
    Path("/Users/rsp_ms/Desktop"),
    Path("/Users/rsp_ms/Downloads"),
]
DEST_ROOT = Path("/Users/rsp_ms/Desktop/KTK_Rebuilds_Complete")

ASSET_EXTS = [".nki", ".nkm", ".nkc", ".ncw", ".wav", ".aiff", ".sf2", ".sfz", ".rex", ".rx2", ".mp3", ".flac"]

def get_manufacturer_and_library(folder: Path):
    parts = folder.parts
    if len(parts) >= 2:
        manufacturer = parts[-2]
        library = parts[-1]
    else:
        manufacturer = "Unknown"
        library = folder.name
    return manufacturer, library

def list_library_assets(lib_folder):
    assets = []
    for dirpath, _, filenames in os.walk(lib_folder):
        for fname in filenames:
            ext = Path(fname).suffix.lower()
            if ext in ASSET_EXTS:
                assets.append(Path(dirpath) / fname)
    return assets

def find_missing_assets(asset_names, search_roots, exclude_root):
    found = {}
    for root in search_roots:
        for dirpath, _, filenames in os.walk(root):
            for fname in filenames:
                if fname in asset_names and not str(Path(dirpath)).startswith(str(exclude_root)):
                    found[fname] = Path(dirpath) / fname
    return found

def gather_complete_library(lib_folder, dest_root, search_roots):
    manufacturer, library = get_manufacturer_and_library(lib_folder)
    print(f"\n🔎 Manufacturer: {manufacturer} | Library: {library}")
    assets = list_library_assets(lib_folder)
    asset_names = set(f.name for f in assets)
    print(f"   Found {len(assets)} assets in library folder.")

    dest_lib = dest_root / manufacturer / library
    dest_lib.mkdir(parents=True, exist_ok=True)
    for asset in assets:
        dest_path = dest_lib / asset.name
        if not dest_path.exists():
            shutil.copy2(asset, dest_path)
            print(f"   Copied: {asset} -> {dest_path}")

    # Search for missing asset types
    for ext in ASSET_EXTS:
        if not any(str(a).lower().endswith(ext) for a in assets):
            print(f"   Missing asset type: {ext} -- searching...")
            found = find_missing_assets([f for f in asset_names if f.endswith(ext)], search_roots, lib_folder)
            for fname, found_path in found.items():
                dest_path = dest_lib / fname
                if not dest_path.exists():
                    shutil.copy2(found_path, dest_path)
                    print(f"   Recovered: {found_path} -> {dest_path}")

if __name__ == "__main__":
    DEST_ROOT.mkdir(parents=True, exist_ok=True)
    for lib_folder in LIB_ROOT.iterdir():
        if lib_folder.is_dir():
            gather_complete_library(lib_folder, DEST_ROOT, SEARCH_ROOTS)
    print("\n🏁 Complete asset gathering finished.")