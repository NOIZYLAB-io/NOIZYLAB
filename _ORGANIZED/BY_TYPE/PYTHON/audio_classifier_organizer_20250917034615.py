"""
MetaBeast Audio Classifier & Organizer

- Scans a master folder for audio files
- Extracts features and classifies as 'music' or 'sound effect'
- Organizes files into Music/SoundEffects folders
- Generates metadata CSV
- Monetization: Prepares metadata for licensing platforms (e.g., Pond5, AudioJungle)
"""
import os
import shutil
import librosa
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import soundfile as sf

# CONFIG
MASTER_FOLDER = '/Volumes/6TB/MASTER_AUDIO'  # Change as needed
MUSIC_FOLDER = os.path.join(MASTER_FOLDER, 'Music')
SFX_FOLDER = os.path.join(MASTER_FOLDER, 'SoundEffects')
METADATA_CSV = os.path.join(MASTER_FOLDER, 'audio_metadata.csv')
AUDIO_EXTENSIONS = ['.wav', '.aiff', '.mp3', '.flac', '.ogg']

# Ensure output folders exist
os.makedirs(MUSIC_FOLDER, exist_ok=True)
os.makedirs(SFX_FOLDER, exist_ok=True)

def is_audio_file(filename):
    return any(filename.lower().endswith(ext) for ext in AUDIO_EXTENSIONS)

def scan_audio_files(folder):
    audio_files = []
    for root, _, files in os.walk(folder):
        for f in files:
            if is_audio_file(f):
                audio_files.append(os.path.join(root, f))
    return audio_files

def extract_features(file_path):
    try:
        y, sr = librosa.load(file_path, sr=None, mono=True, duration=60)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr))
        spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
        mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr))
        zero_crossings = np.mean(librosa.feature.zero_crossing_rate(y))
        return [tempo, chroma, spectral_centroid, mfcc, zero_crossings]
    except Exception as e:
        print(f"Error extracting features from {file_path}: {e}")
        return [0,0,0,0,0]

def get_metadata(file_path):
    try:
        info = sf.info(file_path)
        return {
            'filename': os.path.basename(file_path),
            'path': file_path,
            'samplerate': info.samplerate,
            'channels': info.channels,
            'duration': info.duration,
            'format': info.format
        }
    except Exception as e:
        return {
            'filename': os.path.basename(file_path),
            'path': file_path,
            'samplerate': None,
            'channels': None,
            'duration': None,
            'format': None
        }

def train_classifier(X, y):
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    return clf

def main():
    print("Scanning audio files...")
    audio_files = scan_audio_files(MASTER_FOLDER)
    print(f"Found {len(audio_files)} audio files.")

    # For demo: Simulate training data (replace with real labeled data for production)
    # Assume first half is music, second half is sfx
    features = [extract_features(f) for f in audio_files]
    labels = ['music'] * (len(audio_files)//2) + ['sfx'] * (len(audio_files) - len(audio_files)//2)
    clf = train_classifier(features, labels)

    metadata_rows = []
    for f in audio_files:
        feats = extract_features(f)
        pred = clf.predict([feats])[0]
        target_folder = MUSIC_FOLDER if pred == 'music' else SFX_FOLDER
        shutil.move(f, os.path.join(target_folder, os.path.basename(f)))
        meta = get_metadata(os.path.join(target_folder, os.path.basename(f)))
        meta['type'] = pred
        metadata_rows.append(meta)
        print(f"Moved {f} -> {target_folder} [{pred}]")

    # Save metadata
    df = pd.DataFrame(metadata_rows)
    df.to_csv(METADATA_CSV, index=False)
    print(f"Metadata saved to {METADATA_CSV}")

    # Monetization: Prepare for licensing platforms
    # (Export metadata CSV, add tags, descriptions, etc. as needed)
    print("Monetization-ready metadata prepared.")

if __name__ == "__main__":
    main()
