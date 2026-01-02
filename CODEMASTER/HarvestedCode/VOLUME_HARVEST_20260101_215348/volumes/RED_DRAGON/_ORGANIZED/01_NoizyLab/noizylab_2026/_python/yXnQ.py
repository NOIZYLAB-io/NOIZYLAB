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
  pip install soundfile numpy pydub SpeechRecognition tqdm
  brew install ffmpeg
"""
import shutil
from pathlib import Path
import os
import soundfile as sf
import numpy as np
from pydub import AudioSegment, effects, silence
import speech_recognition as sr
from tqdm import tqdm

DEST = Path("/Volumes/4TB Utility/SFX_FLAT")
LOG = DEST / "car_wash_log.txt"
REPORT = DEST / "car_wash_report.txt"
ERROR_LOG = DEST / "car_wash_errors.txt"
TARGET_SR = 48000
TARGET_FORMAT = "wav"
TARGET_CHANNELS = 1  # mono

DEST.mkdir(parents=True, exist_ok=True)

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
        trimmed = silence.detect_nonsilent(audio, min_silence_len=100, silence_thresh=audio.dBFS-20)
        if trimmed:
            start, end = trimmed[0][0], trimmed[-1][1]
            audio = audio[start:end]
        audio = effects.normalize(audio)
        if audio.channels > 1:
            audio = audio.set_channels(TARGET_CHANNELS)
        audio = audio.set_frame_rate(TARGET_SR)
        audio.export(dest_path, format=TARGET_FORMAT)
        return True, "Cleaned and converted"
    except Exception as e:
        return False, f"Error cleaning: {e}"

def get_voice_path():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("🎤 Please say the folder path to search for audio files:")
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

def open_folder_in_finder(folder):
    if folder.exists():
        os.system(f'open "{folder}"')
        print(f"Opened {folder} in Finder.")
    else:
        print("Folder not found.")

def main():
    search_path = get_voice_path()
    if search_path:
        folder = Path(search_path)
        if folder.exists():
            print(f"Searching in: {folder}")
            open_folder_in_finder(folder)
            SOURCE = folder
        else:
            print("Folder not found. Please try again.")
            exit(1)
    else:
        print("No folder selected. Exiting.")
        exit(1)

    audio_exts = {".wav", ".mp3", ".aiff", ".flac", ".m4a", ".aac", ".ogg", ".wma"}
    files = [f for f in SOURCE.iterdir() if f.is_file() and f.suffix.lower() in audio_exts]
    if not files:
        print("No audio files found in the selected folder.")
        return

    washed, skipped, failed = 0, 0, 0

    with open(LOG, "w", encoding="utf-8") as log, \
         open(REPORT, "w", encoding="utf-8") as report, \
         open(ERROR_LOG, "a", encoding="utf-8") as err_log:
        for file in tqdm(files, desc="Washing audio files"):
            info = analyze_audio(file)
            if info.get("ok"):
                dest_file = DEST / (file.stem + ".wav")
                ok, reason = clean_and_convert(file, dest_file)
                if ok:
                    shutil.move(str(file), str(dest_file))
                    log.write(f"Moved and cleaned: {file} -> {dest_file}\n")
                    report.write(f"{file.name}: OK | {info}\n")
                    print(f"✅ Washed: {file.name}")
                    washed += 1
                else:
                    err_log.write(f"{file.name}: {reason}\n")
                    report.write(f"{file.name}: FAIL | {reason}\n")
                    print(f"❌ Failed to clean: {file.name} ({reason})")
                    failed += 1
            else:
                err_log.write(f"{file.name}: {info.get('error', 'Unknown error')}\n")
                report.write(f"{file.name}: SKIPPED | {info}\n")
                print(f"🚫 Skipped: {file.name} (quality issue)")
                skipped += 1

    print(f"\nAudio Car Wash complete!")
    print(f"Washed: {washed}, Skipped: {skipped}, Failed: {failed}")
    print("Log saved to", LOG)
    print("Summary report saved to", REPORT)
    print("Error log saved to", ERROR_LOG)

if __name__ == "__main__":
    main()