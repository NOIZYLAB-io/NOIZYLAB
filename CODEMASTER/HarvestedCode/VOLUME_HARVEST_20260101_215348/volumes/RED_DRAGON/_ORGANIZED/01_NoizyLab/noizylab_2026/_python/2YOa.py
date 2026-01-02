#!/usr/bin/env python3
"""
Bubba Hand of God Big House (v4)
Trusted zone + Cha-Cha voice navigation
Always announces chosen menu option
"""

import os, shutil, time, subprocess, concurrent.futures
from pathlib import Path

# ---------- Config ----------
WORKSPACE = Path.home() / "Documents/Noizyfish_Aquarium/Noizy_Workspace"
LOGS = WORKSPACE / "Saved_Notes"
LOGS.mkdir(parents=True, exist_ok=True)

VOICE = "Siri Voice 1"  # Cha-Cha's system voice
TRUSTED_ZONE = WORKSPACE

# ---------- Helpers ----------
def say_nav(text: str):
    """Cha-Cha announces only navigation/status items."""
    print(f"**{text}**")
    try:
        subprocess.run(["say", "-v", VOICE, text])
    except Exception:
        pass

def save_log(name: str, content: str):
    f = LOGS / f"{name}_{int(time.time())}.txt"
    f.write_text(content)
    return str(f)

def in_trusted_zone(path: Path) -> bool:
    try:
        return TRUSTED_ZONE in path.resolve().parents or path.resolve() == TRUSTED_ZONE
    except Exception:
        return False

# ---------- Cleanup ----------
def clean_big_house(copy_mode=True):
    say_nav("Cleanup Big House initiated")
    drives = [d for d in Path("/Volumes").iterdir()
              if d.is_dir() and d.name not in ("Macintosh HD", "Macintosh HD - Data")]
    if not drives:
        return "No external drives found."

    categories = {
        "Audio_Project": [".wav", ".aiff", ".mp3", ".flac"],
        "Code_Project": [".py", ".sh", ".js", ".ts", ".cpp", ".c", ".h"],
        "Docs_Project": [".txt", ".md", ".rtf", ".docx", ".pdf"],
        "Images_Project": [".png", ".jpg", ".jpeg", ".gif", ".svg"]
    }

    def process_file(item: Path):
        try:
            if not item.is_file():
                return None
            for project, exts in categories.items():
                if item.suffix.lower() in exts:
                    dest_dir = WORKSPACE / project
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    dest = dest_dir / item.name
                    if in_trusted_zone(dest_dir):
                        if copy_mode:
                            shutil.copy2(item, dest)
                        else:
                            shutil.move(str(item), str(dest))
                        return f"{item} → {project}"
            # fallback
            dest_dir = WORKSPACE / "Misc_Project"
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = dest_dir / item.name
            if in_trusted_zone(dest_dir):
                if copy_mode:
                    shutil.copy2(item, dest)
                else:
                    shutil.move(str(item), str(dest))
                return f"{item} → Misc_Project"
        except Exception as e:
            return f"Error {item}: {e}"

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(drives)*2) as pool:
        futures = []
        for drive in drives:
            for item in drive.rglob("*"):
                futures.append(pool.submit(process_file, item))
        for f in concurrent.futures.as_completed(futures):
            _ = f.result()

    say_nav("All drives scanned. Comfort zone re-established.")
    return "Cleanup finished."

# ---------- Benchmark ----------
def benchmark_drives(workers_per_drive=1):
    say_nav(f"Benchmark drives with {workers_per_drive} worker per drive initiated")
    drives = [d for d in Path("/Volumes").iterdir()
              if d.is_dir() and d.name not in ("Macintosh HD", "Macintosh HD - Data")]
    if not drives:
        return "No external drives found."

    def iter_files(root: Path):
        for dirpath, _, filenames in os.walk(root):
            for fn in filenames:
                yield Path(dirpath) / fn

    def scan_drive(root: Path):
        count = 0
        t0 = time.perf_counter()
        for _ in iter_files(root):
            count += 1
        dt = time.perf_counter() - t0
        return f"{root.name}: {count} files in {dt:.1f}s ({(count/dt)*60:.0f} files/min)"

    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(drives)*workers_per_drive) as pool:
        for d in drives:
            for _ in range(workers_per_drive):
                futures.append(pool.submit(scan_drive, d))
        results = [f.result() for f in concurrent.futures.as_completed(futures)]

    say_nav("Benchmark complete")
    return "\n".join(results)

# ---------- Menu ----------
def menu():
    print("\n=== Bubba Hand of God Menu ===")
    print("a) Cleanup Big House")
    print("x) Benchmark Drives (1 worker/drive)")
    print("y) Benchmark Drives (2 workers/drive)")
    print("q) Quit")
    return input("Choose: ").lower()

# ---------- Entry ----------
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        command = " ".join(sys.argv[1:]).lower()
        if "benchmark 1" in command:
            print(benchmark_drives(1))
        elif "benchmark 2" in command:
            print(benchmark_drives(2))
        elif "cleanup" in command:
            print(clean_big_house())
        else:
            print("Unknown command")
    else:
        say_nav("Good evening Mr. Plowman. Are we ready to get started?")
        while True:
            choice = menu()
            if choice == "a":
                print(clean_big_house())
            elif choice == "x":
                print(benchmark_drives(1))
            elif choice == "y":
                print(benchmark_drives(2))
            elif choice == "q":
                say_nav("Exiting Bubba Hand of God. Rest well, Mr. Plowman.")
                break
