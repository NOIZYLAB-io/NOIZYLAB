from pathlib import Path
import csv

paths = [
    "/Libraries/Instruments/Audiobro/LA_Scoring_Strings/Instruments",
    "/Libraries/Instruments/Audiobro/LA_Scoring_Strings/Samples",
    "/Libraries/Instruments/Audiobro/Legato_Sordino/Instruments",
    "/Libraries/Instruments/Audiobro/Legato_Sordino/Samples",
]

exts = {".nki", ".ncw"}
results = []

for base in paths:
    p = Path(base)
    if p.exists():
        for f in p.glob("*"):
            if f.suffix.lower() in exts and f.is_file():
                results.append({
                    "library": p.parent.parent.name,
                    "folder": p.name,
                    "name": f.name,
                    "ext": f.suffix.lower(),
                    "size_bytes": f.stat().st_size,
                    "path": str(f),
                })

# Export to CSV
with open("audiobro_index.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["library","folder","name","ext","size_bytes","path"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"Indexed {len(results)} files to audiobro_index.csv")