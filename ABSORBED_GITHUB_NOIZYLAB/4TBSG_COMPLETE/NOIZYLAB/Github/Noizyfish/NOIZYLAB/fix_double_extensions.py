import os
import re

# List all external drives except Mission Control
DRIVES = ['/Volumes/' + d for d in os.listdir('/Volumes/') if d != 'Mission Control']

# Pattern to match double/repeated extensions (e.g., .wav.wav, .WAV.wav, .mp3.mp3)
double_ext_pattern = re.compile(r'(\.[a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)$')

for drive in DRIVES:
    for root, dirs, files in os.walk(drive):
        for file in files:
            match = double_ext_pattern.search(file)
            if match and match.group(1).lower() == match.group(2).lower():
                base = file[:file.rfind(match.group(1))]
                ext = match.group(1).lower()
                new_name = base + ext
                src = os.path.join(root, file)
                dst = os.path.join(root, new_name)
                try:
                    os.rename(src, dst)
                    print(f"Renamed file: {src} -> {dst}")
                except Exception as e:
                    print(f"Error renaming file {src}: {e}")

print("Double/repeated extension scan and fix complete.")
