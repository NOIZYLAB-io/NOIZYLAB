import os
import hashlib
import json
import mimetypes
import datetime

# === CONFIG ===
ROOT_DIR = r"D:\FishMusicVault"   # Change to your 12TB root
LOG_DIR  = r"D:\RitualLogs"
os.makedirs(LOG_DIR, exist_ok=True)

# === HELPERS ===
def hash_file(path, block_size=65536):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(block_size), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        return f"ERROR:{e}"

def log_event(logfile, data):
    with open(os.path.join(LOG_DIR, logfile), "a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")

# === SCAN ===
def full_scan():
    seen_hashes = {}
    dupes, empties, bad_ext, errors = [], [], [], []

    for root, dirs, files in os.walk(ROOT_DIR):
        # Empty folder check
        if not files and not dirs:
            empties.append(root)
            continue

        for file in files:
            path = os.path.join(root, file)
            # Hash for dupes
            h = hash_file(path)
            if h.startswith("ERROR"):
                errors.append({"file": path, "error": h})
                continue
            if h in seen_hashes:
                dupes.append({"file": path, "dupe_of": seen_hashes[h]})
                try: os.remove(path)
                except: pass
            else:
                seen_hashes[h] = path

            # Extension validation
            mime, _ = mimetypes.guess_type(path)
            ext = os.path.splitext(file)[1].lower()
            if mime and not mime.endswith(ext.replace(".", "")):
                bad_ext.append({"file": path, "ext": ext, "mime": mime})

    # Purge empties
    for folder in empties:
        try: os.rmdir(folder)
        except: pass

    # Save logs
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    log_event(f"autosave_{ts}.json", {
        "timestamp": ts,
        "dupes_removed": dupes,
        "empties_removed": empties,
        "bad_extensions": bad_ext,
        "errors": errors
    })

    print(f"Scan complete. Logs saved to {LOG_DIR}")

if __name__ == "__main__":
    full_scan()
