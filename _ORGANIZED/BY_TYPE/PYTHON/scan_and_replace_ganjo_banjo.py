import os
import re

# Target directory
TARGET_DIR = '/Volumes/RED DRAGON/ BFA Libraries'

# Patterns to replace
replacements = [
    (r'ganjo', 'AG'),
    (r'banjo', 'AB')
]

# Walk through all files and folders
for root, dirs, files in os.walk(TARGET_DIR):
    # Rename files
    for file in files:
        new_name = file
        for pattern, repl in replacements:
            new_name = re.sub(pattern, repl, new_name, flags=re.IGNORECASE)
        if new_name != file:
            src = os.path.join(root, file)
            dst = os.path.join(root, new_name)
            os.rename(src, dst)
            print(f"Renamed file: {src} -> {dst}")
    # Rename directories
    for dir in dirs:
        new_name = dir
        for pattern, repl in replacements:
            new_name = re.sub(pattern, repl, new_name, flags=re.IGNORECASE)
        if new_name != dir:
            src = os.path.join(root, dir)
            dst = os.path.join(root, new_name)
            os.rename(src, dst)
            print(f"Renamed folder: {src} -> {dst}")

print("Scan and replace complete.")
