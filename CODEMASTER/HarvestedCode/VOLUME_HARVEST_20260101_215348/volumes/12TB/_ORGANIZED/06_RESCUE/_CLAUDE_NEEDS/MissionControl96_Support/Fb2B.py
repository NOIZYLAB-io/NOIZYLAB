import os
from datetime import datetime

SEARCH_ROOTS = [
    "/Users/rsp_ms/NoizyFish_Aquarium",
    "/Users/rsp_ms/Desktop/Native_Instruments_Central/Native Instruments/_3rd_Party_Libraries"
]
KEYWORD = "Cct Chant"
OUTPUT_FILE = "/Users/rsp_ms/NoizyFish_Aquarium/hand_of_god_cct_chant_results.txt"

# Add a timestamped log file for autosave
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE = f"/Users/rsp_ms/NoizyFish_Aquarium/hand_of_god_cct_chant_results_{timestamp}.txt"

results = []

for SEARCH_ROOT in SEARCH_ROOTS:
    for root, dirs, files in os.walk(SEARCH_ROOT):
        for name in files + dirs:
            if KEYWORD.lower() in name.lower():
                path = os.path.join(root, name)
                size = os.path.getsize(path) if os.path.isfile(path) else "-"
                results.append(f"{path} | Size: {size}")

with open(OUTPUT_FILE, "w") as f:
    f.write(f"Results for '{KEYWORD}':\n")
    for line in results:
        f.write(line + "\n")

# Also save to the autosave log
with open(LOG_FILE, "w") as f:
    f.write(f"Results for '{KEYWORD}' ({timestamp}):\n")
    for line in results:
        f.write(line + "\n")

print(f"Saved {len(results)} results to {OUTPUT_FILE} and {LOG_FILE}")
