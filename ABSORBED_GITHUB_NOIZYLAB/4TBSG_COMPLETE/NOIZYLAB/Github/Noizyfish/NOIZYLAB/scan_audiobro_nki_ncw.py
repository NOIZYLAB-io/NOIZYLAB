#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scan Audiobro LA Scoring Strings & Legato Sordino for .nki and .ncw files.
Exports results to audiobro_index.csv.
"""

from pathlib import Path
import csv

search_paths = [
    Path("/Libraries/Instruments/Audiobro/LA_Scoring_Strings/Instruments"),
    Path("/Libraries/Instruments/Audiobro/LA_Scoring_Strings/Samples"),
    Path("/Libraries/Instruments/Audiobro/Legato_Sordino/Instruments"),
    Path("/Libraries/Instruments/Audiobro/Legato_Sordino/Samples"),
]

exts = {".nki", ".ncw"}
results = []

for base in search_paths:
    if base.exists():
        for f in base.glob("*"):
            if f.suffix.lower() in exts and f.is_file():
                results.append({
                    "library": base.parent.parent.name,
                    "folder": base.name,
                    "name": f.name,
                    "ext": f.suffix.lower(),
                    "size_bytes": f.stat().st_size,
                    "path": str(f),
                })

with open("audiobro_index.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["library","folder","name","ext","size_bytes","path"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"Indexed {len(results)} files to audiobro_index.csv")