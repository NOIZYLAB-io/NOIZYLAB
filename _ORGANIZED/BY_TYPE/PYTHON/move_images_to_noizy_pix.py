import os
import shutil

# Set the root and target folder
ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(ROOT, '_NOIZY_PIX')
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

for foldername, subfolders, filenames in os.walk(ROOT):
    # Skip the _NOIZY_PIX folder itself
    if os.path.abspath(foldername) == os.path.abspath(TARGET):
        continue
    for filename in filenames:
        ext = os.path.splitext(filename)[1].lower()
        if ext in IMAGE_EXTENSIONS:
            src_path = os.path.join(foldername, filename)
            dst_path = os.path.join(TARGET, filename)
            # Avoid overwriting files with the same name
            if os.path.exists(dst_path):
                base, ext = os.path.splitext(filename)
                i = 1
                while True:
                    new_name = f"{base}_{i}{ext}"
                    dst_path = os.path.join(TARGET, new_name)
                    if not os.path.exists(dst_path):
                        break
                    i += 1
            shutil.move(src_path, dst_path)
            print(f"Moved: {src_path} -> {dst_path}")
