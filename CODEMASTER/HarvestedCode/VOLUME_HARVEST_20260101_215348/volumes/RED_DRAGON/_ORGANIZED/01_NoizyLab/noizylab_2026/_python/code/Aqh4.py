#!/usr/bin/env python3
"""
noizy_car_wash.py
One giant self-contained bootstrapper + advanced audio car wash:
 - Ensures ~/noizyvenv exists
 - Installs all required packages
 - Warns if libsndfile (system dependency) is missing
 - Runs advanced audio car wash logic inline
"""
import os
import sys
import subprocess
import venv
from pathlib import Path
import shutil

# Where to build the venv
VENV_PATH = Path.home() / "noizyvenv"

# Python deps we always want
REQUIREMENTS = [
    "speechrecognition",
    "sounddevice",
    "numpy",
    "soundfile",
    "pydub"
]

def ensure_venv():
    if not VENV_PATH.exists():
        print(f"[NOIZY] Creating virtual environment at {VENV_PATH}")
        venv.create(VENV_PATH, with_pip=True)
    else:
        print(f"[NOIZY] Using existing virtual environment at {VENV_PATH}")

def run_pip_install():
    pip_path = VENV_PATH / "bin" / "pip"
    if not pip_path.exists():
        sys.exit("[ERROR] pip not found inside venv – creation failed")

    print(f"[NOIZY] Installing/Updating: {', '.join(REQUIREMENTS)}")
    try:
        subprocess.check_call([str(pip_path), "install", "--upgrade"] + REQUIREMENTS)
    except subprocess.CalledProcessError as e:
        sys.exit(f"[ERROR] pip install failed: {e}")

def check_libsndfile():
    brew = shutil.which("brew")
    if brew:
        try:
            subprocess.check_call([brew, "--prefix", "libsndfile"],
                                  stdout=subprocess.DEVNULL,
                                  stderr=subprocess.DEVNULL)
            print("[NOIZY] libsndfile is installed ✔️")
        except subprocess.CalledProcessError:
            print("[WARN] libsndfile not found. Install it with:")
            print("       brew install libsndfile")
    else:
        print("[WARN] Could not check libsndfile (Homebrew not found). "
              "If you hit errors with soundfile, install libsndfile manually.")

def run_main(args):
    # --- Advanced Audio Car Wash Logic ---
    import soundfile as sf
    import numpy as np
    from pydub import AudioSegment, effects, silence
    from pathlib import Path
    import shutil

    SOURCE = Path("/Volumes/4TB Utility/2026_SFX_MASTER")
    DEST = Path("/Volumes/4TB Utility/SFX_FLAT")
    LOG = DEST / "car_wash_log.txt"
    REPORT = DEST / "car_wash_report.txt"
    TARGET_SR = 48000
    TARGET_BIT_DEPTH = 24
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

    with open(LOG, "w", encoding="utf-8") as log, open(REPORT, "w", encoding="utf-8") as report:
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

if __name__ == "__main__":
    ensure_venv()
    run_pip_install()
    check_libsndfile()
    run_main(sys.argv[1:])
