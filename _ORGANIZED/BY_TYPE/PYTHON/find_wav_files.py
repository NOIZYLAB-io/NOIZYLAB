#!/usr/bin/env python3
try:
    import soundfile as sf
except ImportError:
    print("Missing 'soundfile' package. Install with: pip install soundfile")
    exit(1)
import os
import os

def find_audio_files(root_path="/", save_to_file=False, out_name="audio_files.txt", min_duration=30):
    """
    Recursively lists WAV/WAVE/AIFF files >= min_duration seconds starting at root_path.
    - No copying/moving—just prints and (optionally) saves paths.
    - Skips folders you don't have permission to read.
    - Case-insensitive match for .wav/.wave/.aiff.
    """
    audio_files = []

    exts = (".wav", ".wave", ".aiff")
    for dirpath, dirnames, filenames in os.walk(root_path, topdown=True, onerror=lambda e: None, followlinks=False):
        for fname in filenames:
            if fname.lower().endswith(exts):
                full = os.path.join(dirpath, fname)
                try:
                    info = sf.info(full)
                    duration = info.frames / info.samplerate
                    if duration >= min_duration:
                        print(f"{full} ({duration:.1f}s)")
                        audio_files.append(full)
                except Exception as e:
                    print(f"Could not read {full}: {e}")

    if save_to_file:
        with open(out_name, "w") as f:
            f.write("\n".join(audio_files))
        print(f"\n✅ Saved results to {out_name}")

    print(f"\nTotal qualifying audio files found: {len(audio_files)}")
    return audio_files


if __name__ == "__main__":
    import sys
    def list_drives():
        drives = []
        # Root drive
        drives.append("/")
        # On macOS, external drives are in /Volumes
        volumes = "/Volumes"
        if os.path.exists(volumes):
            for v in os.listdir(volumes):
                drive_path = os.path.join(volumes, v)
                if os.path.ismount(drive_path):
                    drives.append(drive_path)
        return drives

    print("Available drives:")
    drives = list_drives()
    for idx, d in enumerate(drives):
        print(f"  {idx+1}. {d}")

    while True:
        choice = input(f"Select a drive by number (1-{len(drives)}), or type a custom path: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(drives):
            root = drives[int(choice)-1]
            break
        elif os.path.exists(choice):
            root = choice
            break
        else:
            print("Invalid selection. Please try again.")

    save_choice = input("Save results to audio_files.txt? (y/n): ").strip().lower()
    min_dur = input("Minimum duration in seconds (default 30): ").strip()
    try:
        min_dur = float(min_dur) if min_dur else 30
    except ValueError:
        min_dur = 30
    find_audio_files(root, save_to_file=(save_choice == "y"), min_duration=min_dur)