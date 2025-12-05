import os
import csv
import soundfile as sf
import re

# Supported audio/sample extensions
AUDIO_EXTS = ['.wav', '.ncw', '.nki']

# Root Big Fish Audio Libraries folder
ROOT = '/Volumes/RED DRAGON/ BFA Libraries'
REPORT = os.path.join(ROOT, 'BFA_metadata_by_instrument.csv')

# Helper: extract instrument name from filename or folder

def get_instrument(path):
    # Try to extract instrument from folder or filename
    parts = re.split(r'[\/]', path)
    for part in reversed(parts):
        if any(inst in part.lower() for inst in ['guitar', 'banjo', 'mandolin', 'bass', 'drum', 'fiddle', 'resonator', 'horn', 'string', 'piano', 'organ', 'tambo', 'acoustic', 'electric']):
            return part
    return 'Unknown'

# Helper: get master library name

def get_master_library(path):
    parts = re.split(r'[\/]', path)
    for part in parts:
        if part.startswith('BFA -'):
            return part
    return 'Unknown'

# Scan and collect metadata
rows = []
for root, dirs, files in os.walk(ROOT):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in AUDIO_EXTS:
            fpath = os.path.join(root, file)
            instrument = get_instrument(fpath)
            master_lib = get_master_library(fpath)
            # Try to get audio metadata
            try:
                info = sf.info(fpath)
                samplerate = info.samplerate
                channels = info.channels
                duration = info.duration
            except Exception:
                samplerate = channels = duration = 'N/A'
            rows.append([file, instrument, master_lib, samplerate, channels, duration, fpath])

# Group by instrument and master library
rows.sort(key=lambda x: (x[2], x[1]))

# Write CSV report
with open(REPORT, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Filename', 'Instrument', 'Master Library', 'Sample Rate', 'Channels', 'Duration', 'Path'])
    writer.writerows(rows)

print(f"Metadata scan complete. Report saved to {REPORT}")
