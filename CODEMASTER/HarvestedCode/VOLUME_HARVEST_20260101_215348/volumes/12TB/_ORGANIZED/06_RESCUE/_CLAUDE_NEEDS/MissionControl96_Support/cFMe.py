import os
from datetime import datetime

SEARCH_ROOTS = [
    "/Users/rsp_ms/NoizyFish_Aquarium",
    "/Users/rsp_ms/Desktop/Native_Instruments_Central/Native Instruments/_3rd_Party_Libraries"
]
# Add all mounted volumes except system
for vol in os.listdir("/Volumes"):
    vol_path = os.path.join("/Volumes", vol)
    if os.path.ismount(vol_path) and not vol.startswith("Macintosh HD"):
        SEARCH_ROOTS.append(vol_path)

KEYWORD = "CCT Chant"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = f"/Users/rsp_ms/NoizyFish_Aquarium/hand_of_god_cct_chant_results_{timestamp}.txt"

results = []

for SEARCH_ROOT in SEARCH_ROOTS:
    for root, dirs, files in os.walk(SEARCH_ROOT):
        for name in files:
            path = os.path.join(root, name)
            # Check filename
            if KEYWORD.lower() in name.lower():
                size = os.path.getsize(path)
                results.append(f"{path} | Size: {size} | MATCH: filename")
                continue
            # Check file content (text files only, skip binary)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if KEYWORD.lower() in line.lower():
                            size = os.path.getsize(path)
                            results.append(f"{path} | Size: {size} | MATCH: content")
                            break
            except Exception:
                continue

with open(OUTPUT_FILE, "w") as f:
    f.write(f"Results for '{KEYWORD}' ({timestamp}):\n")
    for line in results:
        f.write(line + "\n")

print(f"Saved {len(results)} results to {OUTPUT_FILE}")
