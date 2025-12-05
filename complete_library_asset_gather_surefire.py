import os
import shutil
from pathlib import Path
import subprocess

LIB_ROOT = Path("/Volumes/4TB Blue Fish/Native Instruments")
SEARCH_ROOTS = [
    Path("/Volumes/4TB Blue Fish"),
    Path("/Volumes/6TB/NI_2026"),
    Path("/Users/rsp_ms/Desktop"),
    Path("/Users/rsp_ms/Downloads"),
]
DEST_ROOT = Path("/Users/rsp_ms/Desktop/KTK_Rebuilds_Complete")

# All known NI extensions (add more as needed)
ASSET_EXTS = [
    ".nki", ".nkm", ".nkc", ".nkr", ".nkx", ".ncw", ".nks", ".nka", ".nkb", ".nkt", ".nksf", ".nksr",
    ".wav", ".aiff", ".flac", ".mp3", ".ogg", ".rex", ".rx2", ".sf2", ".sfz",
    ".ens", ".ism", ".kit",
    ".nbkt", ".nbkt2", ".nbkt3", ".nbkt4", ".nbkt5", ".nbkt6", ".nbkt7", ".nbkt8", ".nbkt9", ".nbkt10",
    ".nbkt11", ".nbkt12", ".nbkt13", ".nbkt14", ".nbkt15", ".nbkt16", ".nbkt17", ".nbkt18", ".nbkt19", ".nbkt20",
    ".nbkt21", ".nbkt22", ".nbkt23", ".nbkt24", ".nbkt25", ".nbkt26", ".nbkt27", ".nbkt28", ".nbkt29", ".nbkt30",
    ".nbkt31", ".nbkt32", ".nbkt33", ".nbkt34", ".nbkt35", ".nbkt36", ".nbkt37", ".nbkt38", ".nbkt39", ".nbkt40",
    ".nbkt41", ".nbkt42", ".nbkt43", ".nbkt44", ".nbkt45", ".nbkt46", ".nbkt47", ".nbkt48", ".nbkt49", ".nbkt50",
    ".nbkt51", ".nbkt52", ".nbkt53", ".nbkt54", ".nbkt55", ".nbkt56", ".nbkt57", ".nbkt58", ".nbkt59", ".nbkt60",
    ".nbkt61", ".nbkt62", ".nbkt63", ".nbkt64"
]

# List all your 96Agent scripts here
AGENT96_SCRIPTS = [
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "agent96_duplicate_detector.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "agent96_simple.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "agent96_wave_analyzer.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "bulletproof_deep96.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "deep_agent96.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "duplicate_detector.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "exs24_repair.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "exs24_resurrection.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "multi_volume_duplicate_detector.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "neural_ultra_deep96.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "ultra_deep_96_agent_analyzer.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "wave_detective.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "wave_relevance_analyzer.sh",
    Path.home() / "Desktop" / "CLEANED_SCRIPTS" / "wave_simple.sh",
]

def call_all_agents(scripts, target_folder):
    for script_path in scripts:
        if script_path.exists():
            print(f"🕵️‍♂️ Calling 96Agent: {script_path.name} on {target_folder}")
            try:
                result = subprocess.run(
                    ["bash", str(script_path), str(target_folder)],
                    capture_output=True, text=True
                )
                print(result.stdout)
                if result.stderr:
                    print("Agent96 Error:", result.stderr)
            except Exception as e:
                print(f"Failed to run {script_path.name}: {e}")
        else:
            print(f"Agent script not found: {script_path}")

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

    # Call all 96Agent scripts on the destination library folder
    call_all_agents(AGENT96_SCRIPTS, dest_lib)

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
    print("\n🏁 Surefire asset gathering (with all 96Agents) finished.")