import os
import re

# List all drives except Mission Control
DRIVES = ['/Volumes/' + d for d in os.listdir('/Volumes/') if d != 'Mission Control']

# Prompt user for word to replace and replacement
word = input('Enter the word to replace: ')
replacement = input('Enter the replacement word: ')

pattern = re.compile(re.escape(word), re.IGNORECASE)

for drive in DRIVES:
    for root, dirs, files in os.walk(drive):
        # Rename files
        for file in files:
            new_name = pattern.sub(replacement, file)
            if new_name != file:
                src = os.path.join(root, file)
                dst = os.path.join(root, new_name)
                try:
                    os.rename(src, dst)
                    print(f"Renamed file: {src} -> {dst}")
                except Exception as e:
                    print(f"Error renaming file {src}: {e}")
        # Rename directories
        for dir in dirs:
            new_name = pattern.sub(replacement, dir)
            if new_name != dir:
                src = os.path.join(root, dir)
                dst = os.path.join(root, new_name)
                try:
                    os.rename(src, dst)
                    print(f"Renamed folder: {src} -> {dst}")
                except Exception as e:
                    print(f"Error renaming folder {src}: {e}")

print("Scan and replace complete.")
