# {PROJECT_NAME}

## Project Type
Audio Processing / Music Production Project

## Tech Stack
- **Python**: 3.12+
- **Audio Libraries**: librosa, soundfile, pydub
- **ML/AI**: PyTorch, torchaudio
- **CLI**: Click / Typer
- **Processing**: NumPy, SciPy

## Project Structure
```
src/
├── {package_name}/
│   ├── __init__.py
│   ├── main.py
│   ├── audio/
│   │   ├── io.py           # File I/O
│   │   ├── effects.py      # Audio effects
│   │   ├── analysis.py     # Audio analysis
│   │   └── synthesis.py    # Sound synthesis
│   ├── dsp/
│   │   ├── filters.py      # Digital filters
│   │   ├── transforms.py   # FFT, STFT, etc.
│   │   └── dynamics.py     # Compressors, limiters
│   ├── ml/
│   │   ├── models/         # ML models
│   │   ├── train.py        # Training
│   │   └── inference.py    # Inference
│   └── utils/
│       ├── time.py         # Time/sample conversions
│       └── visualization.py # Waveforms, spectrograms
├── tests/
├── notebooks/              # Jupyter experiments
├── samples/                # Test audio files
└── models/                 # Trained models
```

## Audio Conventions

### Sample Rates
- **44100 Hz**: CD quality, general audio
- **48000 Hz**: Video standard
- **96000 Hz**: High-res audio
- **22050 Hz**: Speech/ML models

### Bit Depths
- **16-bit**: Standard quality
- **24-bit**: Professional quality
- **32-bit float**: Processing headroom

### Channel Layout
- Mono: 1 channel
- Stereo: 2 channels (L, R)
- 5.1: 6 channels

## Key Libraries

### librosa (Analysis)
```python
import librosa

# Load audio
y, sr = librosa.load("audio.wav", sr=None)

# Analysis
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
```

### soundfile (I/O)
```python
import soundfile as sf

# Read
data, sr = sf.read("input.wav")

# Write
sf.write("output.wav", data, sr, subtype='PCM_24')
```

### torchaudio (ML)
```python
import torchaudio

waveform, sr = torchaudio.load("audio.wav")
spectrogram = torchaudio.transforms.Spectrogram()(waveform)
mel_spec = torchaudio.transforms.MelSpectrogram()(waveform)
```

## DSP Patterns

### Basic Processing
```python
import numpy as np
from scipy import signal

def apply_gain(audio: np.ndarray, db: float) -> np.ndarray:
    """Apply gain in decibels."""
    return audio * (10 ** (db / 20))

def normalize(audio: np.ndarray, peak_db: float = -1.0) -> np.ndarray:
    """Normalize audio to peak level."""
    peak = np.max(np.abs(audio))
    target = 10 ** (peak_db / 20)
    return audio * (target / peak)
```

### Filtering
```python
def lowpass_filter(audio: np.ndarray, cutoff: float, sr: int) -> np.ndarray:
    """Apply lowpass filter."""
    nyquist = sr / 2
    normalized_cutoff = cutoff / nyquist
    b, a = signal.butter(4, normalized_cutoff, btype='low')
    return signal.filtfilt(b, a, audio)
```

### Time-Frequency
```python
def stft(audio: np.ndarray, n_fft: int = 2048, hop_length: int = 512):
    """Short-time Fourier transform."""
    return librosa.stft(audio, n_fft=n_fft, hop_length=hop_length)

def istft(stft_matrix: np.ndarray, hop_length: int = 512):
    """Inverse STFT."""
    return librosa.istft(stft_matrix, hop_length=hop_length)
```

## Commands

### FFmpeg
```bash
# Convert format
ffmpeg -i input.wav output.mp3

# Extract audio from video
ffmpeg -i video.mp4 -vn -acodec pcm_s16le audio.wav

# Resample
ffmpeg -i input.wav -ar 44100 output.wav

# Normalize
ffmpeg -i input.wav -af loudnorm output.wav
```

### SoX
```bash
# Convert sample rate
sox input.wav output.wav rate 44100

# Mix to mono
sox input.wav output.wav channels 1

# Apply effects
sox input.wav output.wav reverb 50 50 100
```

## ML/AI Audio

### Whisper (Speech-to-Text)
```python
import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.wav")
print(result["text"])
```

### Music Generation
- AudioCraft (Meta)
- Stable Audio
- MusicGen

### Voice
- Coqui TTS
- Bark
- Tortoise-TTS

## Performance Tips
- Use `librosa.stream` for large files
- Process in blocks for memory efficiency
- Use float32 for processing, convert on export
- Parallelize with multiprocessing

## Testing Audio
```python
@pytest.fixture
def sine_wave():
    """Generate test sine wave."""
    sr = 44100
    duration = 1.0
    freq = 440.0
    t = np.linspace(0, duration, int(sr * duration))
    return np.sin(2 * np.pi * freq * t), sr
```

## File Formats
- **WAV**: Uncompressed, lossless
- **FLAC**: Compressed, lossless
- **MP3**: Compressed, lossy (good compatibility)
- **OGG**: Compressed, lossy (better quality)
- **M4A/AAC**: Compressed, lossy (Apple)
