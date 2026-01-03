#!/usr/bin/env python3
import os
import librosa
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

# Path to the test folder and file
TEST_DIR = '/Users/rsp_ms/Desktop/Align_Audio_Test'
FILENAME = 'DRUM_TEST.wav'
FILEPATH = os.path.join(TEST_DIR, FILENAME)
OUTPUT_PATH = os.path.join(TEST_DIR, 'DRUM_TEST_aligned.wav')
REPORT_PATH = os.path.join(TEST_DIR, 'DRUM_TEST_report.txt')

# Load audio
try:
    y, sr = librosa.load(FILEPATH, sr=None)
except Exception as e:
    print(f"Error loading file: {e}")
    exit(1)

# Plot waveform and save image
import librosa.display
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 4))
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform')
plt.savefig('/Users/rsp_ms/Desktop/Align_Audio_Test/DRUM_TEST_waveform.png')
plt.close()

# Analyze waveform: Find peaks and valleys
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
onsets = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
peaks = librosa.util.peak_pick(onset_env, pre_max=3, post_max=3, pre_avg=3, post_avg=5, delta=0.5, wait=5)

# Pitch analysis: Estimate tuning
f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
num_voiced = np.sum(voiced_flag)
tuning_percent = 100 * num_voiced / len(voiced_flag)

# Align by shifting so first main peak is at start
if len(peaks) > 0:
    peak_sample = peaks[0]
    shift_samples = int(peak_sample * sr / len(onset_env))
    y_aligned = np.roll(y, -shift_samples)
else:
    y_aligned = y

# Save aligned audio
sf.write(OUTPUT_PATH, y_aligned, sr)

# Save report
with open(REPORT_PATH, 'w') as f:
    f.write(f"File: {FILENAME}\n")
    f.write(f"Sample Rate: {sr}\n")
    f.write(f"Detected Peaks: {peaks.tolist()}\n")
    f.write(f"First Peak Sample: {peaks[0] if len(peaks) > 0 else 'None'}\n")
    f.write(f"Pitch Tuning Percent: {tuning_percent:.2f}%\n")
    f.write(f"Aligned file saved as: {OUTPUT_PATH}\n")

# Optional: Plot waveform and peaks
plt.figure(figsize=(12, 4))
librosa.display.waveshow(y, sr=sr, alpha=0.5)
plt.vlines([peak_sample * sr / len(onset_env) for peak_sample in peaks], -1, 1, color='r', linestyle='--', label='Peaks')
plt.title('Waveform and Detected Peaks')
plt.savefig(os.path.join(TEST_DIR, 'DRUM_TEST_waveform.png'))
plt.close()

print(f"Analysis complete. Report and aligned file saved in {TEST_DIR}")
