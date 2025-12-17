import os
from mutagen import File

AUDIO_EXTS = ('.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg', '.wma', '.aiff')

def scan_audio(root_dir):
    total_seconds = 0
    file_count = 0
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            if name.lower().endswith(AUDIO_EXTS):
                try:
                    audio = File(os.path.join(root, name))
                    if audio and audio.info and hasattr(audio.info, 'length'):
                        total_seconds += audio.info.length
                        file_count += 1
                except Exception:
                    continue
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    print(f"Scanned {file_count} audio files.")
    print(f"Total audio duration: {hours}h {minutes}m {seconds}s")

if __name__ == '__main__':
    scan_audio('/Volumes/JOE')
