import os
import json
import csv
from mutagen import File
from datetime import timedelta

AUDIO_EXTENSIONS = {'.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg', '.wma', '.aiff', '.alac'}

REPORT_CSV = '/Users/m2ultra/joe_audio_report.csv'
REPORT_JSON = '/Users/m2ultra/joe_audio_report.json'
SCAN_ROOT = '/Volumes/JOE'

def is_audio_file(filename):
    return any(filename.lower().endswith(ext) for ext in AUDIO_EXTENSIONS)

def scan_audio_files(root):
    audio_files = []
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if is_audio_file(fname):
                full_path = os.path.join(dirpath, fname)
                try:
                    audio = File(full_path)
                    duration = float(audio.info.length) if audio and audio.info and hasattr(audio.info, 'length') else 0.0
                except Exception:
                    duration = 0.0
                audio_files.append({
                    'path': full_path,
                    'duration_seconds': duration
                })
    return audio_files

def write_csv(audio_files, csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['path', 'duration_seconds', 'duration_hms'])
        writer.writeheader()
        for entry in audio_files:
            hms = str(timedelta(seconds=int(entry['duration_seconds'])))
            writer.writerow({'path': entry['path'], 'duration_seconds': entry['duration_seconds'], 'duration_hms': hms})

def write_json(audio_files, json_path):
    for entry in audio_files:
        entry['duration_hms'] = str(timedelta(seconds=int(entry['duration_seconds'])))
    with open(json_path, 'w') as f:
        json.dump(audio_files, f, indent=2)

def main():
    print(f'Scanning {SCAN_ROOT} for audio files...')
    audio_files = scan_audio_files(SCAN_ROOT)
    print(f'Found {len(audio_files)} audio files. Writing reports...')
    write_csv(audio_files, REPORT_CSV)
    write_json(audio_files, REPORT_JSON)
    print(f'Reports written to {REPORT_CSV} and {REPORT_JSON}')

if __name__ == '__main__':
    main()
