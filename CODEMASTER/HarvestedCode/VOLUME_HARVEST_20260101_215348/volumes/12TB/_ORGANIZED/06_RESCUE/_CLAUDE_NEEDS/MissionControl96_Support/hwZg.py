import os
import sys
from PIL import Image
import subprocess

# Set your source and output folders
SOURCE_FOLDER = os.path.expanduser('~/Pictures/iCons/MUS_01/Source JPG\'s')
OUTPUT_FOLDER = os.path.expanduser('~/Desktop/NoizyFish/Utils/ConvertedIcons')
ICONSET_SIZES = {
    'icon_16x16.png': (16, 16),
    'icon_16x16@2x.png': (32, 32),
    'icon_32x32.png': (32, 32),
    'icon_32x32@2x.png': (64, 64),
    'icon_128x128.png': (128, 128),
    'icon_128x128@2x.png': (256, 256),
    'icon_256x256.png': (256, 256),
    'icon_256x256@2x.png': (512, 512),
    'icon_512x512.png': (512, 512),
    'icon_512x512@2x.png': (1024, 1024),
}

def create_iconset(image_path, iconset_path):
    img = Image.open(image_path)
    for name, size in ICONSET_SIZES.items():
        resized = img.resize(size, Image.LANCZOS)
        resized.save(os.path.join(iconset_path, name))

def convert_to_icns(iconset_path, icns_path):
    subprocess.run(['iconutil', '-c', 'icns', iconset_path, '-o', icns_path], check=True)

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    for filename in os.listdir(SOURCE_FOLDER):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            name, _ = os.path.splitext(filename)
            iconset_dir = os.path.join(OUTPUT_FOLDER, f'{name}.iconset')
            icns_file = os.path.join(OUTPUT_FOLDER, f'{name}.icns')
            os.makedirs(iconset_dir, exist_ok=True)
            create_iconset(os.path.join(SOURCE_FOLDER, filename), iconset_dir)
            convert_to_icns(iconset_dir, icns_file)
            print(f'Converted {filename} to {icns_file}')

if __name__ == '__main__':
    main()
