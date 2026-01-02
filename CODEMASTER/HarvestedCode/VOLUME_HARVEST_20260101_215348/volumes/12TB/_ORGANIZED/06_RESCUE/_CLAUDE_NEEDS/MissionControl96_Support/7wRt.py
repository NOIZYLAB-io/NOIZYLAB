#!/usr/bin/env python3
"""
NoizyFish Library/Product Name Extractor & Hierarchy Builder
- Loads the full volume index (from the scan script)
- Extracts likely library/product names from file/folder names
- Groups files by detected product/library
- Outputs a structured JSON of product/library hierarchies and contents
"""

import json
import re
from pathlib import Path
from collections import defaultdict

# Load the latest index file (update path as needed)
index_files = sorted(Path.home().glob("NoizyFish_Volume_Index_*.json"), reverse=True)
if not index_files:
    print("No index file found. Run the volume scan first.")
    exit(1)

INDEX_FILE = index_files[0]
print(f"Loading index: {INDEX_FILE}")
with open(INDEX_FILE) as f:
    index = json.load(f)

# Heuristics for library/product name extraction
PRODUCT_PATTERNS = [
    r"(?i)(library|collection|pack|bundle|archive|kit|expansion|soundset|bank|sample|preset|patch|instrument|plugin|suite|volume|vol\.?\d+|v\d+)",
    r"(?i)[A-Z][a-z]+[A-Z][a-z]+",  # CamelCase
    r"(?i)[A-Z0-9_\-]{6,}",        # ALLCAPS or long alphanum
]

# Group files by top-level folder or detected product/library name
products = defaultdict(list)

for entry in index:
    path = Path(entry["path"])
    # Try to extract product/library name from path parts
    name = None
    for part in path.parts[::-1]:
        for pat in PRODUCT_PATTERNS:
            m = re.search(pat, part)
            if m:
                name = m.group(0)
                break
        if name:
            break
    # Fallback: use top-level folder
    if not name and len(path.parts) > 2:
        name = path.parts[1]
    if name:
        products[name].append(entry)

# Build hierarchy: {product: {dirs: [...], files: [...]}}
hierarchy = {}
for name, entries in products.items():
    dirs = [e for e in entries if e["type"] == "dir"]
    files = [e for e in entries if e["type"] == "file"]
    hierarchy[name] = {
        "dirs": [d["path"] for d in dirs],
        "files": [f["path"] for f in files],
        "file_count": len(files),
        "dir_count": len(dirs),
    }

# Output structured hierarchy
out_file = Path.home() / f"NoizyFish_Library_Hierarchy_{INDEX_FILE.stem.split('_')[-1]}.json"
with open(out_file, "w") as f:
    json.dump(hierarchy, f, indent=2)
print(f"Library/Product hierarchy written to: {out_file}")
