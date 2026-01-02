import os
import librosa
import soundfile as sf
from pydub import AudioSegment, effects

# Directory containing audio files
AUDIO_DIR = '/Volumes/4TBSG/2025_NOIZYFISH/wav/'
OUTPUT_DIR = os.path.join(AUDIO_DIR, 'processed')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Helper: Check integrity and get info
def check_integrity(filepath):
    try:
        y, sr = librosa.load(filepath, sr=None, mono=False)
        info = sf.info(filepath)
        print(f"{filepath}: OK | Format: {info.format}, SR: {info.samplerate}, Channels: {info.channels}, Bit Depth: {info.subtype}")
        return True, info
    except Exception as e:
        print(f"{filepath}: ERROR - {e}")
        return False, None

# Helper: Clean up, normalize, EQ, balance
def process_audio(filepath, output_dir):
    try:
        audio = AudioSegment.from_file(filepath)
        # Remove silence (leading/trailing)
        trimmed = effects.strip_silence(audio, silence_len=100, silence_thresh=-40)
        # Normalize volume
        normalized = effects.normalize(trimmed)
        # Simple EQ: boost mids, cut lows/highs
        eq_audio = normalized.low_pass_filter(12000).high_pass_filter(100)
        # Balance: make stereo if mono
        if eq_audio.channels == 1:
            eq_audio = AudioSegment.from_mono_audiosegments(eq_audio, eq_audio)
        # Export
        out_path = os.path.join(output_dir, os.path.basename(filepath))
        eq_audio.export(out_path, format="wav")
        print(f"Processed: {filepath} -> {out_path}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")

# Main loop
for file in os.listdir(AUDIO_DIR):
    if file.lower().endswith('.wav'):
        path = os.path.join(AUDIO_DIR, file)
        ok, info = check_integrity(path)
        if ok:
            process_audio(path, OUTPUT_DIR)

print("Audio integrity check and processing complete.")
