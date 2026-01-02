import os
import re
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
MISC_FOLDER = "Misc"

def organize_files():
    files = [f for f in os.listdir(ROOT) if os.path.isfile(os.path.join(ROOT, f))]
    pattern = re.compile(r"^(C\d+)\s?([A-Za-z0-9 ()\-]+)?(\.[a-z0-9]+)$", re.IGNORECASE)

    for filename in files:
        match = pattern.match(filename)
        if match:
            prefix = match.group(1)
            suffix = match.group(2).strip() if match.group(2) else "Other"
            # Replace '140' with '140Bpm' in the suffix
            if "140" in suffix:
                suffix = suffix.replace("140", "140Bpm")
            target_dir = os.path.join(ROOT, prefix, suffix)
        else:
            target_dir = os.path.join(ROOT, MISC_FOLDER)

        os.makedirs(target_dir, exist_ok=True)
        src = os.path.join(ROOT, filename)
        dst = os.path.join(target_dir, filename)
        shutil.move(src, dst)
        print(f"Moved: {filename} -> {target_dir}")

if __name__ == "__main__":
    os.chdir("/Users/rsp_ms/Desktop/Native_Instruments_Central/Native Instruments/_3rd_Party_Libraries")
    organize_files()
python3 organize_samples.py