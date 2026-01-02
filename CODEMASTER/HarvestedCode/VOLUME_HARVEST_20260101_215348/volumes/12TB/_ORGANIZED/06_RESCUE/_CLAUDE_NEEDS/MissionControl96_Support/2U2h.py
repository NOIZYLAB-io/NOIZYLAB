#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iCon — Universal Icon Generator
Converts any image into icons for iOS, iPadOS, macOS, Windows, Android, and Web.
Follows current platform standards for icon sizes and formats.
"""

import os
from pathlib import Path
from PIL import Image
from icnsutil import IcnsFile

# --- Icon Specs ---
ICON_SPECS = {
    "ios": [
        (20, "AppIcon-20.png"), (29, "AppIcon-29.png"), (40, "AppIcon-40.png"),
        (60, "AppIcon-60.png"), (76, "AppIcon-76.png"), (83.5, "AppIcon-83.5.png"),
        (1024, "AppIcon-1024.png"),
    ],
    "macos": [
        (16, "icon_16x16.png"), (32, "icon_32x32.png"), (64, "icon_64x64.png"),
        (128, "icon_128x128.png"), (256, "icon_256x256.png"),
        (512, "icon_512x512.png"), (1024, "icon_1024x1024.png"),
    ],
    "windows": [
        (16, None), (24, None), (32, None), (48, None), (64, None), (128, None), (256, None)
    ],
    "android": [
        (48, "ic_launcher_mdpi.png"), (72, "ic_launcher_hdpi.png"),
        (96, "ic_launcher_xhdpi.png"), (144, "ic_launcher_xxhdpi.png"),
        (192, "ic_launcher_xxxhdpi.png"), (512, "play_store.png"),
    ],
    "web": [
        (16, "favicon-16.png"), (32, "favicon-32.png"), (48, "favicon-48.png"),
        (64, "favicon-64.png"), (128, "favicon-128.png"), (256, "favicon-256.png"),
        (512, "favicon-512.png"),
    ]
}

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def save_png(img, size, out_path):
    icon = img.resize((int(size), int(size)), Image.LANCZOS)
    icon.save(out_path, format="PNG")

def generate_ios_icons(img, out_dir):
    ensure_dir(out_dir)
    for size, name in ICON_SPECS["ios"]:
        save_png(img, size, Path(out_dir) / name)

def generate_macos_icons(img, out_dir):
    ensure_dir(out_dir)
    for size, name in ICON_SPECS["macos"]:
        save_png(img, size, Path(out_dir) / name)
    # ICNS file
    icns = IcnsFile()
    for size, _ in ICON_SPECS["macos"]:
        icon = img.resize((int(size), int(size)), Image.LANCZOS)
        icns.add_icon(int(size), icon)
    icns.write(Path(out_dir) / "icon.icns")

def generate_windows_icon(img, out_dir):
    ensure_dir(out_dir)
    sizes = [size for size, _ in ICON_SPECS["windows"]]
    out_path = Path(out_dir) / "icon.ico"
    img.save(out_path, format="ICO", sizes=[(size, size) for size in sizes])

def generate_android_icons(img, out_dir):
    ensure_dir(out_dir)
    for size, name in ICON_SPECS["android"]:
        save_png(img, size, Path(out_dir) / name)

def generate_web_icons(img, out_dir):
    ensure_dir(out_dir)
    for size, name in ICON_SPECS["web"]:
        save_png(img, size, Path(out_dir) / name)
    # Favicon.ico
    sizes = [size for size, _ in ICON_SPECS["web"] if size <= 256]
    img.save(Path(out_dir) / "favicon.ico", format="ICO", sizes=[(size, size) for size in sizes])

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 icon.py <input_image>")
        sys.exit(1)
    input_image = Path(sys.argv[1])
    if not input_image.exists():
        print("Input image not found.")
        sys.exit(1)
    img = Image.open(input_image).convert("RGBA")
    out_base = Path("icon_output")
    print("Generating icons for all platforms...")
    generate_ios_icons(img, out_base / "ios")
    generate_macos_icons(img, out_base / "macos")
    generate_windows_icon(img, out_base / "windows")
    generate_android_icons(img, out_base / "android")
    generate_web_icons(img, out_base / "web")
    print(f"All icons generated in: {out_base.resolve()}")

if __name__ == "__main__":
    main()

# Install required packages with:
# pip install pillow icnsutil tk