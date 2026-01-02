import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from pathlib import Path
from PIL import Image
from icnsutil import IcnsFile
import shutil

ICON_SPECS = {
    "iOS": [20, 29, 40, 60, 76, 83.5, 1024],
    "macOS": [16, 32, 64, 128, 256, 512, 1024],
    "Windows": [16, 24, 32, 48, 64, 128, 256],
    "Android": [48, 72, 96, 144, 192, 512],
    "Web": [16, 32, 48, 64, 128, 256, 512]
}

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def save_png(img, size, out_path):
    icon = img.resize((int(size), int(size)), Image.LANCZOS)
    icon.save(out_path, format="PNG")

def generate_icons(img_path, platform, out_dir):
    img = Image.open(img_path).convert("RGBA")
    ensure_dir(out_dir)
    sizes = ICON_SPECS[platform]
    for size in sizes:
        save_png(img, size, Path(out_dir) / f"icon_{size}.png")
    if platform == "macOS":
        icns = IcnsFile()
        for size in sizes:
            icon = img.resize((int(size), int(size)), Image.LANCZOS)
            icns.add_icon(int(size), icon)
        icns.write(Path(out_dir) / "icon.icns")
    if platform == "Windows":
        img.save(Path(out_dir) / "icon.ico", format="ICO", sizes=[(size, size) for size in sizes])
    if platform == "Web":
        img.save(Path(out_dir) / "favicon.ico", format="ICO", sizes=[(size, size) for size in sizes if size <= 256])

def process_input(input_path, platform):
    input_path = Path(input_path)
    out_base = input_path.parent / f"{input_path.stem}_icons_{platform}"
    ensure_dir(out_base)
    if input_path.is_file():
        generate_icons(input_path, platform, out_base)
    elif input_path.is_dir():
        for file in input_path.glob("*"):
            if file.suffix.lower() in [".png", ".jpg", ".jpeg"]:
                generate_icons(file, platform, out_base / file.stem)
    messagebox.showinfo("Done", f"Icons generated in:\n{out_base}")

def ask_platform():
    return simpledialog.askstring("Choose Platform", "Enter platform (iOS, macOS, Windows, Android, Web):")

def on_drop(event):
    files = root.tk.splitlist(event.data)
    platform = ask_platform()
    if platform not in ICON_SPECS:
        messagebox.showerror("Error", "Unknown platform!")
        return
    for f in files:
        process_input(f, platform)

root = tk.Tk()
root.title("iCon Widget")
root.geometry("400x200")
label = tk.Label(root, text="Drag & Drop Files or Folders Here", font=("Arial", 16))
label.pack(expand=True, fill="both")

# Drag-and-drop support (tkinterDnD2 required for full drag-and-drop)
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    root = TkinterDnD.Tk()
    label = tk.Label(root, text="Drag & Drop Files or Folders Here", font=("Arial", 16))
    label.pack(expand=True, fill="both")
    label.drop_target_register(DND_FILES)
    label.dnd_bind('<<Drop>>', on_drop)
except ImportError:
    label.config(text="Drag-and-drop requires tkinterDnD2.\nOr use the button below.")
    def browse():
        path = filedialog.askopenfilename() or filedialog.askdirectory()
        if path:
            platform = ask_platform()
            if platform in ICON_SPECS:
                process_input(path, platform)
            else:
                messagebox.showerror("Error", "Unknown platform!")
    btn = tk.Button(root, text="Choose File/Folder", command=browse)
    btn.pack()

root.mainloop()

pip install tkinterdnd2

python3 /Users/rsp_ms/Documents/five_sorry_five_associates_2026/icon_widget.py