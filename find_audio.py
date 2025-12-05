import os
import subprocess
import shutil
import sys

# Debug: confirm script has started
print("Script started…")

# Keywords and duration threshold
KEYWORDS = ["audience", "medium", "live"]
MIN_DURATION = 20.0
SEARCH_ROOT = "/Volumes"  # search external + system drives
RESULTS_FILE = "results.txt"
COLLECTED_DIR = "Collected_Audio"

def get_duration(filepath):
    """Use ffprobe to get audio duration in seconds."""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return float(result.stdout.strip())
    except Exception:
        return 0.0

def main():
    matches = []

    # Gather all candidate files first
    all_files = []
    for root, _, files in os.walk(SEARCH_ROOT):
        for f in files:
            if f.lower().endswith((".wav", ".aiff")):
                all_files.append(os.path.join(root, f))

    total = len(all_files)
    if total == 0:
        print("No WAV or AIFF files found under", SEARCH_ROOT)
        return

    # Process files with a progress indicator
    for i, filepath in enumerate(all_files, start=1):
        percent = (i / total) * 100
        sys.stdout.write(f"\rSearching... {percent:.1f}%")
        sys.stdout.flush()

        filename = os.path.basename(filepath).lower()
        if any(k in filename for k in KEYWORDS):
            dur = get_duration(filepath)
            if dur >= MIN_DURATION:
                matches.append((filepath, dur))

    print("\nSearch complete.")

    if not matches:
        print("No files matched the filters.")
        return

    # Write results file
    with open(RESULTS_FILE, "w") as out:
        for filepath, dur in matches:
            out.write(f"{filepath} | {dur:.1f} sec\n")

    # Copy files into collection folder
    os.makedirs(COLLECTED_DIR, exist_ok=True)
    for filepath, dur in matches:
        try:
            dest = os.path.join(COLLECTED_DIR, os.path.basename(filepath))
            shutil.copy2(filepath, dest)
        except Exception as e:
            print(f"Could not copy {filepath}: {e}")

    print(f"\nDONE! {len(matches)} files saved to '{COLLECTED_DIR}' and listed in '{RESULTS_FILE}'.")

if __name__ == "__main__":
    main()
