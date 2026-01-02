#!/usr/bin/env python3
"""
Audio Car Wash: Advanced Audio File Cleaner and Organizer
- Moves files from source to destination
- Checks format, sample rate, bit depth, duration
- Detects silence, clipping, corruption
- Normalizes loudness and trims silence
- Converts to consistent format (WAV, 48kHz, 24-bit)
- Logs all actions and generates a summary report

Requirements:
  pip install soundfile numpy pydub SpeechRecognition
  brew install ffmpeg
"""
import shutil
from pathlib import Path
import soundfile as sf
import numpy as np
from pydub import AudioSegment, effects, silence
import amazon_q
import speech_recognition as sr
import os

SOURCE = Path("/Volumes/4TB Utility/2026_SFX_MASTER")
DEST = Path("/Volumes/4TB Utility/SFX_FLAT")
LOG = DEST / "car_wash_log.txt"
REPORT = DEST / "car_wash_report.txt"
TARGET_SR = 48000
TARGET_BIT_DEPTH = 24
TARGET_FORMAT = "wav"
TARGET_CHANNELS = 1  # mono

DEST.mkdir(parents=True, exist_ok=True)

# --- Utility functions ---
def analyze_audio(file_path):
    try:
        with sf.SoundFile(file_path) as f:
            sr = f.samplerate
            channels = f.channels
            frames = f.frames
            duration = frames / sr
            subtype = f.subtype
            data = f.read(dtype='float32')
            rms = np.sqrt(np.mean(data**2))
            peak = np.max(np.abs(data))
            silence_ratio = np.sum(np.abs(data) < 0.001) / data.size
            clipped = np.sum(np.abs(data) >= 0.99) > 0
            return {
                "sample_rate": sr,
                "channels": channels,
                "duration": duration,
                "bit_depth": subtype,
                "rms": rms,
                "peak": peak,
                "silence_ratio": silence_ratio,
                "clipped": clipped,
                "ok": sr >= 22050 and duration > 0.1 and silence_ratio < 0.8 and not clipped
            }
    except Exception as e:
        return {"ok": False, "error": str(e)}


def clean_and_convert(file_path, dest_path):
    try:
        audio = AudioSegment.from_file(file_path)
        # Trim silence
        trimmed = silence.detect_nonsilent(audio, min_silence_len=100, silence_thresh=audio.dBFS-20)
        if trimmed:
            start, end = trimmed[0][0], trimmed[-1][1]
            audio = audio[start:end]
        # Normalize loudness
        audio = effects.normalize(audio)
        # Convert to mono
        if audio.channels > 1:
            audio = audio.set_channels(TARGET_CHANNELS)
        # Set frame rate
        audio = audio.set_frame_rate(TARGET_SR)
        # Export as WAV 24-bit
        audio.export(dest_path, format=TARGET_FORMAT, bitrate="24k")
        return True, "Cleaned and converted"
    except Exception as e:
        return False, f"Error cleaning: {e}"

def get_voice_path():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("🎤 Please say the folder path or keyword to search for audio files:")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
        return None
    except sr.RequestError as e:
        print(f"Recognition error: {e}")
        return None

def get_voice_folder():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("🎤 Please say the drive or folder name to open in Finder:")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        # Try to match to mounted volumes
        volumes = [str(p) for p in Path("/Volumes").iterdir()]
        match = next((v for v in volumes if text.lower() in v.lower()), None)
        if match:
            print(f"Opening: {match}")
            os.system(f'open "{match}"')
        else:
            print("Drive or folder not found. Please try again.")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
    except sr.RequestError as e:
        print(f"Recognition error: {e}")

# Example usage:
search_path = get_voice_path()
if search_path:
    # You can now use search_path as a folder or keyword
    folder = Path(search_path)
    if folder.exists():
        print(f"Searching in: {folder}")
        SOURCE = folder
    else:
        print("Folder not found. Please try again.")

with open(LOG, "w") as log, open(REPORT, "w") as report:
    for file in SOURCE.iterdir():
        if file.is_file():
            info = analyze_audio(file)
            if info.get("ok"):
                dest_file = DEST / (file.stem + ".wav")
                ok, reason = clean_and_convert(file, dest_file)
                if ok:
                    shutil.move(str(file), str(dest_file))
                    log.write(f"Moved and cleaned: {file} -> {dest_file}\n")
                    report.write(f"{file.name}: OK | {info}\n")
                    print(f"✅ Washed: {file.name}")
                else:
                    report.write(f"{file.name}: FAIL | {reason}\n")
                    print(f"❌ Failed to clean: {file.name} ({reason})")
            else:
                report.write(f"{file.name}: SKIPPED | {info}\n")
                print(f"🚫 Skipped: {file.name} (quality issue)")

print("Audio Car Wash complete! Log saved to", LOG)
print("Summary report saved to", REPORT)





    print(item)for item in drive_path.iterdir():drive_path = Path("/Volumes/4TB Utility")  # Change to your drive nameimport os
drive_path = "/Volumes/4TB Utility"  # Change to your drive name
os.system(f'open "{drive_path}"')
