#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scan Audiobro LA Scoring Strings & Legato Sordino for .nki and .ncw files.
Exports results to audiobro_index.csv.
"""

from pathlib import Path
import csv
import sys

search_paths = [
    Path("/Libraries/Instruments/Audiobro/LA_Scoring_Strings"),
    Path("/Libraries/Instruments/Audiobro/Legato_Sordino"),
    Path("/Libraries/Instruments/Audiobro/LA_Scoring_Strings/Samples"),
]

exts = {".nki", ".ncw"}
results = []

# Check if the script is run with the correct parameters
if len(sys.argv) < 4 or sys.argv[1] != "ignite" or sys.argv[2] != "--base":
    print("Usage: python noizyfish_omnifinder.py ignite --base <base_path> --pdf-keywords <keyword1> <keyword2> ...")
    sys.exit(1)

# Get the base path and keywords from the command line arguments
base_path = Path(sys.argv[3])
keywords = sys.argv[4:]

# Update the search paths to include the base path
search_paths = [base_path]

for base in search_paths:
    if base.exists():
        for f in base.glob("*.nki"):
            if f.is_file():
                results.append({
                    "library": base.name,
                    "name": f.name,
                    "ext": f.suffix.lower(),
                    "size_bytes": f.stat().st_size,
                    "path": str(f),
                })
        for f in base.glob("*.ncw"):
            if f.is_file():
                results.append({
                    "library": base.name,
                    "name": f.name,
                    "ext": f.suffix.lower(),
                    "size_bytes": f.stat().st_size,
                    "path": str(f),
                })

with open("audiobro_index.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["library","name","ext","size_bytes","path"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"Indexed {len(results)} files to audiobro_index.csv")

pip install PyYAML rich PyPDF2 click