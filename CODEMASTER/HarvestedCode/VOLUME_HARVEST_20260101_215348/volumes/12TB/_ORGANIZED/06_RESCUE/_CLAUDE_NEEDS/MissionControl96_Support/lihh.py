import os
import shutil
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

SRC_DIR = '/Users/rsp_ms/Pictures/iCons'
DST_DIR = '/Users/rsp_ms/Pictures/iCons/Source_All_iCons_CLEANED'
ICON_EXTS = ('.png', '.jpg', '.jpeg', '.icns')

def organize_icons():
    files_moved = 0
    for root, dirs, files in os.walk(SRC_DIR):
        # Skip destination folder if inside source
        if Path(root).resolve() == Path(DST_DIR).resolve():
            continue
        for file in files:
            if file == '.DS_Store':
                continue
            src_file = Path(root) / file
            if src_file.suffix.lower() in ICON_EXTS or not src_file.suffix:
                dst_file = Path(DST_DIR) / file
                # Avoid overwriting files
                if dst_file.exists():
                    dst_file = Path(DST_DIR) / f"{src_file.stem}_{files_moved}{src_file.suffix}"
                try:
                    shutil.move(str(src_file), str(dst_file))
                    files_moved += 1
                except Exception as e:
                    print(f"Failed to move {src_file}: {e}")
    # Remove empty folders except destination
    for root, dirs, files in os.walk(SRC_DIR, topdown=False):
        if Path(root).resolve() == Path(DST_DIR).resolve():
            continue
        if not os.listdir(root):
            try:
                os.rmdir(root)
            except Exception:
                pass
    messagebox.showinfo("Done", f"Moved {files_moved} icon files to {DST_DIR}")

def run_widget():
    root = tk.Tk()
    root.title("Icon Organizer Widget")
    root.geometry("320x160")
    label = tk.Label(root, text="Organize your icons!", font=("Arial", 14))
    label.pack(pady=10)
    btn = tk.Button(root, text="Organize Now", command=organize_icons, font=("Arial", 12))
    btn.pack(pady=20)
    root.mainloop()

if __name__ == '__main__':
    # Ensure destination exists
    os.makedirs(DST_DIR, exist_ok=True)
    run_widget()
    os.system('python3 /Users/rsp_ms/The_Aquarium/NoizyWorkspace/iCon_CVTR/icon_widget.py')