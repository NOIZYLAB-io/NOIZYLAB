import librosa
import pandas as pd
import os

# Map chroma index to pitch classes
PITCH_CLASSES = ['C', 'C#', 'D', 'D#', 'E', 'F',
                 'F#', 'G', 'G#', 'A', 'A#', 'B']

def detect_key(y, sr):
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_mean = chroma.mean(axis=1)
    pitch_index = chroma_mean.argmax()
    pitch_name = PITCH_CLASSES[pitch_index]

    # crude heuristic: assume major if mean energy > average, else minor
    if chroma_mean[pitch_index] > chroma_mean.mean():
        scale = "major"
    else:
        scale = "minor"
    return f"{pitch_name} {scale}"

def analyze_track(file_path):
    try:
        y, sr = librosa.load(file_path)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        key = detect_key(y, sr)
        duration = librosa.get_duration(y=y, sr=sr)
        return tempo, key, duration
    except Exception as e:
        print(f"⚠️ Error analyzing {file_path}: {e}")
        return None, None, None

folder = "Tracks"
data = []

for file in os.listdir(folder):
    if file.lower().endswith((".wav", ".mp3", ".aiff", ".flac")):
        filepath = os.path.join(folder, file)
        tempo, key, duration = analyze_track(filepath)
        data.append([file, tempo, key, duration])

df = pd.DataFrame(data, columns=["Filename", "BPM", "Key", "Duration (sec)"])
df.to_csv("music_metadata.csv", index=False)
print("✅ Metadata exported to music_metadata.csv")
