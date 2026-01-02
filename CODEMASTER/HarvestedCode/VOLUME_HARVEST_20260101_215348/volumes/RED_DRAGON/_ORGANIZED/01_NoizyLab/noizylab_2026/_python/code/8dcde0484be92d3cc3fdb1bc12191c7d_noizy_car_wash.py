�7#!/usr/bin/env python3
"""
noizy_car_wash.py

One-file bootstrapper + audio tool for audio cleaning and OSC streaming.

USAGE:
    python3 noizy_car_wash.py
    python3 noizy_car_wash.py --osc_host <host> --osc_port <port>
"""

import sys
import subprocess
import venv
from pathlib import Path
import shutil
import os
import time
import argparse

VENV_PATH = Path.home() / "noizyvenv"
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

def run_main(osc_host=None, osc_port=None):
    import soundfile as sf
    import numpy as np
    from pydub import AudioSegment, effects, silence

    SOURCE = Path("/Users/rsp_ms/Documents/Noizyfish_Aquarium/Noizy_Workspace/waves_test_sort")
    DEST = Path("/Users/rsp_ms/Documents/Noizyfish_Aquarium/Noizy_Workspace/sort")
    LOG = DEST / "car_wash_log.txt"
    REPORT = DEST / "car_wash_report.txt"
    TARGET_SR = 48000
    TARGET_FORMAT = "wav"
    TARGET_CHANNELS = 1  # mono

    DEST.mkdir(parents=True, exist_ok=True)

    # Permissions check
    if not os.access(DEST, os.W_OK):
        print(f"[ERROR] No write permission for {DEST}")
        sys.exit(1)

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
            # Export as WAV (lossless)
            audio.export(dest_path, format=TARGET_FORMAT)
            return True, "Cleaned and converted"
        except Exception as e:
            return False, f"Error cleaning: {e}"

    processed = 0
    skipped = 0
    failed = 0

    with open(LOG, "w", encoding="utf-8") as log, open(REPORT, "w", encoding="utf-8") as report:
        for file in SOURCE.rglob("*"):
            if file.is_file() and file.suffix.lower() in {".wav", ".mp3"}:
                info = analyze_audio(file)
                dest_file = DEST / (file.stem + ".wav")
                # Avoid overwriting
                if dest_file.exists():
                    dest_file = DEST / (file.stem + f"_{int(time.time())}.wav")
                if info.get("ok"):
                    ok, reason = clean_and_convert(file, dest_file)
                    if ok:
                        shutil.move(str(file), str(dest_file))
                        log.write(f"Moved and cleaned: {file} -> {dest_file}\n")
                        report.write(f"{file.name}: OK | {info}\n")
                        print(f"✅ Washed: {file.name}")
                        processed += 1
                    else:
                        report.write(f"{file.name}: FAIL | {reason}\n")
                        print(f"❌ Failed to clean: {file.name} ({reason})")
                        failed += 1
                else:
                    report.write(f"{file.name}: SKIPPED | {info}\n")
                    print(f"🚫 Skipped: {file.name} (quality issue)")
                    skipped += 1

    print(f"Audio Car Wash complete! {processed} processed, {skipped} skipped, {failed} failed.")
    print("Log saved to", LOG)
    print("Summary report saved to", REPORT)

    # Automatically open the log file (macOS)
    try:
        subprocess.run(["open", str(LOG)], check=True)
    except Exception as e:
        print(f"[WARN] Could not open log file automatically: {e}")

    # Example OSC usage (requires python-osc)
    if osc_host and osc_port:
        try:
            from pythonosc import udp_client
            osc_client = udp_client.SimpleUDPClient(osc_host, osc_port)
            osc_client.send_message("/carwash/complete", "done")
            print(f"[OSC] Sent completion message to {osc_host}:{osc_port}")
        except ImportError:
            print("[WARN] python-osc not installed. OSC message not sent.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--osc_host", type=str, default=None)
    parser.add_argument("--osc_port", type=int, default=None)
    args = parser.parse_args()

    ensure_venv()
    run_pip_install()
    check_libsndfile()
    run_main(args.osc_host, args.osc_port)

start_dir = os.path.expanduser("~/Documents/Noizyfish_Aquarium/Noizy_Workspace")
pattern = "noizy_car_wash.py"  # or "*.wav" for audio files

�72&file:///Users/rsp_ms/noizy_car_wash.py