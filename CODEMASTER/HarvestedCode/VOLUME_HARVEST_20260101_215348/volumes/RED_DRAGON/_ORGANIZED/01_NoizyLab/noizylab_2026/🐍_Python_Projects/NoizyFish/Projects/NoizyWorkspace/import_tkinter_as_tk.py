import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
from pathlib import Path
import os

SRC_DIR = '/Users/rsp_ms/Pictures/iCons'
DST_DIR = '/Users/rsp_ms/Pictures/iCons/Source_All_iCons_CLEANED'

def organize_icons():
    files_moved = 0
    for root, dirs, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.icns')):
                src_file = Path(root) / file
                dst_file = Path(DST_DIR) / file
                if not dst_file.exists():
                    shutil.move(str(src_file), str(dst_file))
                    files_moved += 1
    messagebox.showinfo("Done", f"Moved {files_moved} icon files to {DST_DIR}")

def run_widget():
    root = tk.Tk()
    root.title("Icon Organizer Widget")
    root.geometry("300x150")
    label = tk.Label(root, text="Organize your icons!", font=("Arial", 14))
    label.pack(pady=10)
    btn = tk.Button(root, text="Organize Now", command=organize_icons)
    btn.pack(pady=20)
    root.mainloop()

if __name__ == '__main__':
    run_widget()