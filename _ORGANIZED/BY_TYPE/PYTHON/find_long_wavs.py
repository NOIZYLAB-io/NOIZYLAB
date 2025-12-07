import os
from pydub import AudioSegment

def find_long_wavs(root_path, min_seconds=20):
    results = []
    for dirpath, _, filenames in os.walk(root_path):
        for f in filenames:
            if f.lower().endswith(".wav"):
                full_path = os.path.join(dirpath, f)
                try:
                    audio = AudioSegment.from_wav(full_path)
                    duration_sec = len(audio) / 1000.0  # ms → seconds
                    if duration_sec >= min_seconds:
                        results.append((full_path, duration_sec))
                except Exception as e:
                    print(f"Skipping {full_path}: {e}")
    return results

if __name__ == "__main__":
    drive_path = "/Volumes/YourDriveName"  # change this
    long_wavs = find_long_wavs(drive_path)

    for path, duration in long_wavs:
        print(f"{path} — {duration:.1f} sec")
