import os
import soundfile as sf
import traceback

# List all external drives except Mission Control
DRIVES = ['/Volumes/' + d for d in os.listdir('/Volumes/') if d != 'Mission Control']
AUDIO_EXTS = ['.wav', '.mp3', '.flac', '.aiff', '.ogg', '.m4a', '.wma', '.aac', '.ncw']
LOG_PATH = '/Volumes/RED DRAGON/Projects/python_scripts/audio_integrity_log.txt'

bad_files = []

for drive in DRIVES:
    for root, dirs, files in os.walk(drive):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in AUDIO_EXTS:
                fpath = os.path.join(root, file)
                try:
                    # Try to open with soundfile (works for most formats)
                    sf.info(fpath)
                except Exception as e:
                    bad_files.append(f"{fpath}: {e}")

with open(LOG_PATH, 'w') as log:
    for line in bad_files:
        log.write(line + '\n')

print(f"Audio integrity check complete. Log saved to {LOG_PATH}")
