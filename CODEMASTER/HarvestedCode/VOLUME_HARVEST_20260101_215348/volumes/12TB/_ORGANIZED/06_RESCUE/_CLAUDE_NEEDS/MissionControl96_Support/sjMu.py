import os
import shutil
import time
from collections import defaultdict

# Source and destination root directories
SOURCE_ROOT = "/Volumes/6TB"
DEST_ROOT = "/Volumes/6TB/noisy fish"

def scan_and_copy_folder(src, dst, brand=None, library=None, steps=[0], max_steps=5000, stats=None, level=0):
    if steps[0] >= max_steps:
        return
    if not os.path.exists(dst):
        os.makedirs(dst, exist_ok=True)
    try:
        items = os.listdir(src)
    except Exception as e:
        print(" " * level + f"[ERROR] Could not list {src}: {e}")
        return
    for item in items:
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            print(" " * level + f"[DIR] {s}")
            scan_and_copy_folder(s, d, brand, library, steps, max_steps, stats, level+2)
        else:
            try:
                shutil.copy2(s, d)
                steps[0] += 1
                if stats is not None and brand and library:
                    size = os.path.getsize(d)
                    stats[(brand, library)]['files'] += 1
                    stats[(brand, library)]['size'] += size
                print(" " * level + f"[FILE] {s} -> {d}")
                if steps[0] % 100 == 0:
                    print(f"-- Progress: {steps[0]} files copied...")
                if steps[0] >= max_steps:
                    print(f"-- Reached max steps ({max_steps}). Stopping.")
                    return
            except Exception as e:
                print(" " * level + f"[ERROR] Could not copy {s}: {e}")

def main():
    # Scan all top-level folders in SOURCE_ROOT
    top_folders = [f for f in os.listdir(SOURCE_ROOT) if os.path.isdir(os.path.join(SOURCE_ROOT, f))]
    steps = [0]
    max_steps = 5000
    stats = defaultdict(lambda: {'files': 0, 'size': 0})
    for brand in top_folders:
        brand_src = os.path.join(SOURCE_ROOT, brand)
        brand_dst = os.path.join(DEST_ROOT, brand)
        print(f"\n=== Scanning brand: {brand} ===")
        if not os.path.exists(brand_src):
            continue
        for library in os.listdir(brand_src):
            lib_src = os.path.join(brand_src, library)
            lib_dst = os.path.join(brand_dst, library)
            if os.path.isdir(lib_src):
                print(f"-- Scanning library: {library}")
                scan_and_copy_folder(lib_src, lib_dst, brand, library, steps, max_steps, stats)
            else:
                if not os.path.exists(brand_dst):
                    os.makedirs(brand_dst, exist_ok=True)
                try:
                    shutil.copy2(lib_src, lib_dst)
                    steps[0] += 1
                    stats[(brand, library)]['files'] += 1
                    stats[(brand, library)]['size'] += os.path.getsize(lib_dst)
                    print(f"[FILE] {lib_src} -> {lib_dst}")
                except Exception as e:
                    print(f"[ERROR] Could not copy {lib_src}: {e}")
                if steps[0] >= max_steps:
                    print(f"-- Reached max steps ({max_steps}). Stopping.")
                    break
        if steps[0] >= max_steps:
            break
    # Print top 10 libraries by file count
    top10 = sorted(stats.items(), key=lambda x: x[1]['files'], reverse=True)[:10]
    print("\nTop 10 Libraries (by file count):")
    for (brand, library), s in top10:
        print(f"{brand}/{library}: {s['files']} files, {s['size']/1024/1024:.2f} MB")

if __name__ == "__main__":
    main()
            break
