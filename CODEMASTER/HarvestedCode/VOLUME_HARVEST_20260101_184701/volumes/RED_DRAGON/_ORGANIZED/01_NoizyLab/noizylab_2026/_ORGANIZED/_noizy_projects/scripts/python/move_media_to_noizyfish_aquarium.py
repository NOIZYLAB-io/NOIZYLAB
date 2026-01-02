"""
Move all video and audio files from MissionControl96 into NoizyFish_Aquarium/media for unified management.
"""
import os
import shutil

BASE = '/Users/rsp_ms/Desktop/MissionControl96'
TARGET = os.path.join(BASE, 'NoizyFish_Aquarium', 'media')
VIDEO_EXTS = ['.mp4', '.mov', '.avi', '.mkv', '.webm', '.flv', '.wmv']
AUDIO_EXTS = ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a']

if not os.path.exists(TARGET):
    os.makedirs(TARGET)

for root, dirs, files in os.walk(BASE):
    # Skip NoizyFish_Aquarium itself
    if 'NoizyFish_Aquarium' in root and root != TARGET:
        continue
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in VIDEO_EXTS + AUDIO_EXTS:
            src = os.path.join(root, file)
            dst = os.path.join(TARGET, file)
            if not os.path.exists(dst):
                shutil.move(src, dst)
                print(f"Moved: {src} -> {dst}")
            else:
                print(f"Already exists: {dst}")
print("Media migration to NoizyFish_Aquarium/media complete.")
