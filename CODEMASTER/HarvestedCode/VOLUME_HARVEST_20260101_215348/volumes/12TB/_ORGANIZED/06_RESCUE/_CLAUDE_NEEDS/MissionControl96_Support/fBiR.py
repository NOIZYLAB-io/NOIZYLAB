# rsp_post_render.py
import os, sys, shutil, datetime, json

AUTHOR = "RSP"
EXPORT_ROOT = os.path.expanduser("~/RSP_Planar_Template/Exports")
TARGETS = {
    "wav": "WAV_24bit_48k",
    "mp3": "MP3_320kbps",
    "flac": "FLAC_Archive"
}

def stamp(file_path):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    meta = {"author": AUTHOR, "timestamp": ts, "file": file_path}
    with open(file_path + ".rsp.json", "w") as f:
        json.dump(meta, f)

def route(file_path):
    ext = file_path.split(".")[-1].lower()
    dest_dir = os.path.join(EXPORT_ROOT, TARGETS.get(ext, "WAV_24bit_48k"))
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy2(file_path, dest_dir)
    stamp(os.path.join(dest_dir, os.path.basename(file_path)))

if __name__ == "__main__":
    for p in sys.argv[1:]:
        route(os.path.abspath(p))
    print("RSP post‑render routing complete.")
