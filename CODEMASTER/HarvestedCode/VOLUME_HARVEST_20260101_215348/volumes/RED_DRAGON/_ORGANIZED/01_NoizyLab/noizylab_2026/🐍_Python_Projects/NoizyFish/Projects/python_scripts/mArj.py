import os
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime

SAVE_DIR = "VS_Buddy_Setup/Saved_Notes"
PARALLELS_DIR = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace" / "Parallels"
AGENTS_TOTAL = 96

def save_output(text):
    os.makedirs(SAVE_DIR, exist_ok=True)
    fname = datetime.datetime.now().strftime("%Y-%m-%d_%H%M") + ".txt"
    fpath = os.path.join(SAVE_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\n💾 Saved output to {fpath}")

def process_file(file):
    # Replace this with your Super Brain logic or cleaning/organizing function
    # Example: just print file for now
    print(f"Processing: {file}")
    # You can add code cleaning, linting, moving, etc. here

def main():
    if not PARALLELS_DIR.exists():
        print(f"❌ Parallels directory not found: {PARALLELS_DIR}")
        sys.exit(1)

    files = [f for f in PARALLELS_DIR.rglob("*") if f.is_file()]
    print(f"🧠 Super Brain: Scanning {len(files)} files in Parallels with {AGENTS_TOTAL} agents...")

    with ThreadPoolExecutor(max_workers=AGENTS_TOTAL) as pool:
        futures = [pool.submit(process_file, file) for file in files]
        for f in as_completed(futures):
            f.result()

    print("✅ All files in Parallels processed.")

if __name__ == "__main__":
    main()
    if "--save" in sys.argv:
        summary = f"Processed files in Parallels on {datetime.datetime.now()}\n"
        save_output(summary)