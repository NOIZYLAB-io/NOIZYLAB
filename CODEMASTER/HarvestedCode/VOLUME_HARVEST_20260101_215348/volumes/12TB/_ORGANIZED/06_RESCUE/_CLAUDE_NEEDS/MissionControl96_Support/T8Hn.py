import os
import shutil
from collections import defaultdict

# Source and destination root directories
SOURCE_ROOT = "/Volumes/6TB"
DEST_ROOT = "/Volumes/6TB/noisy fish"

# List of top-level brands to scan (add more as needed)
BRANDS = [
    "Native Instruments",
    "Garritan",
    "XLN Audio",
    "reFX",
    "iZotope",
    "Toontrack",
    "Superior Drummer",
    "Sugar-Bytes",
    "Kompose Audio",
    "SampleTank 3",
    "Steven Slate",
    "Impulse Responses",
    "IR Presets",
    "Nexus library",
    "NucleusSoundlab",
    "SYLENTH 1 PRESETS",
    "SYNTH PRESETS",
    "BigKick",
    "M-Tron Pro Library",
    "Liquid Instruments",
    "Reason",
    "STEAM",
    "XLN Audio",
    "_AVID Samples",
    "iZotope Stutter Edit Presets"
]

# Limit for steps
MAX_STEPS = 5000

# Track stats
library_stats = defaultdict(lambda: {'files': 0, 'size': 0})
steps = 0

def copytree_limited(src, dst, brand, library):
    global steps
    if steps >= MAX_STEPS:
        return
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree_limited(s, d, brand, library)
        else:
            try:
                shutil.copy2(s, d)
                steps += 1
                size = os.path.getsize(d)
                library_stats[(brand, library)]['files'] += 1
                library_stats[(brand, library)]['size'] += size
                if steps >= MAX_STEPS:
                    return
            except Exception as e:
                pass  # Ignore errors for now

def main():
    for brand in BRANDS:
        brand_src = os.path.join(SOURCE_ROOT, brand)
        brand_dst = os.path.join(DEST_ROOT, brand)
        if not os.path.exists(brand_src):
            continue
        for library in os.listdir(brand_src):
            lib_src = os.path.join(brand_src, library)
            lib_dst = os.path.join(brand_dst, library)
            if os.path.isdir(lib_src):
                copytree_limited(lib_src, lib_dst, brand, library)
            else:
                # Single file at brand root
                if not os.path.exists(brand_dst):
                    os.makedirs(brand_dst)
                shutil.copy2(lib_src, lib_dst)
                steps += 1
                size = os.path.getsize(lib_dst)
                library_stats[(brand, library)]['files'] += 1
                library_stats[(brand, library)]['size'] += size
                if steps >= MAX_STEPS:
                    break
        if steps >= MAX_STEPS:
            break
    # Print top 10 libraries by file count
    top10 = sorted(library_stats.items(), key=lambda x: x[1]['files'], reverse=True)[:10]
    print("Top 10 Libraries (by file count):")
    for (brand, library), stats in top10:
        print(f"{brand}/{library}: {stats['files']} files, {stats['size']/1024/1024:.2f} MB")

if __name__ == "__main__":
    main()
