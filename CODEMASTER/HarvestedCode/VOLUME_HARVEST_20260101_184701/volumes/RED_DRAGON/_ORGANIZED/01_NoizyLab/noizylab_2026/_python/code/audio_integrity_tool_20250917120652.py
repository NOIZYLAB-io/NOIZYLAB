import os
import shutil
from pydub import AudioSegment
import librosa
import soundfile as sf

# Configurable paths
AUDIO_ROOT = '/Volumes/JOE/DUPES FROM 12TB'
REPAIR_FOLDER = os.path.join(AUDIO_ROOT, 'needs_repair')
READY_FOLDER = os.path.join(AUDIO_ROOT, 'ready_to_go')
os.makedirs(REPAIR_FOLDER, exist_ok=True)
os.makedirs(READY_FOLDER, exist_ok=True)

# Supported formats
AUDIO_EXTS = ['.wav', '.mp3', '.flac', '.aiff', '.ogg', '.m4a', '.aac', '.wma', '.mp4']

def is_audio_file(filename):
    return any(filename.lower().endswith(ext) for ext in AUDIO_EXTS)

def check_integrity(filepath):
    try:
        # Try loading with pydub
        audio = AudioSegment.from_file(filepath)
        # Check duration
        if len(audio) < 1000:  # less than 1 second
            return False, 'Too short'
        # Check for silence
        if audio.dBFS < -50:
            return False, 'Mostly silence'
        # Try loading with librosa for more checks
        y, sr = librosa.load(filepath, sr=None)
        if librosa.get_duration(y=y, sr=sr) < 1:
            return False, 'Librosa: too short'
        if max(abs(y)) < 0.01:
            return False, 'Librosa: too quiet'
        return True, 'OK'
    except Exception as e:
        return False, f'Error: {e}'

def attempt_repair(filepath):
    # Example: try re-exporting with pydub
    try:
        audio = AudioSegment.from_file(filepath)
        repaired_path = os.path.join(READY_FOLDER, os.path.basename(filepath))
        audio.export(repaired_path, format='wav')
        return repaired_path, 'Repaired with pydub'
    except Exception as e:
        return None, f'Repair failed: {e}'

def process_audio_files():
    for fname in os.listdir(AUDIO_ROOT):
        fpath = os.path.join(AUDIO_ROOT, fname)
        if os.path.isfile(fpath) and is_audio_file(fname):
            ok, reason = check_integrity(fpath)
            if ok:
                shutil.copy2(fpath, READY_FOLDER)
                print(f'{fname}: OK')
            else:
                print(f'{fname}: Damaged ({reason})')
                shutil.move(fpath, REPAIR_FOLDER)
                repaired, rep_reason = attempt_repair(os.path.join(REPAIR_FOLDER, fname))
                if repaired:
                    print(f'{fname}: {rep_reason}')
                else:
                    print(f'{fname}: Could not repair ({rep_reason})')

if __name__ == '__main__':
    process_audio_files()
    print('Audio integrity check complete.')
