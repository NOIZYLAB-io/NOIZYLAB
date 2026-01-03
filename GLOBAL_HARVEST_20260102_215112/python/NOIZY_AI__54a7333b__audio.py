"""
NOIZYVOICE Audio Processing Utilities
"""
import io
import numpy as np
from pathlib import Path
from typing import Optional, Tuple, Union
import soundfile as sf
import librosa
from loguru import logger


class AudioProcessor:
    """Audio processing utilities"""

    def __init__(
        self,
        sample_rate: int = 24000,
        output_sample_rate: int = 48000,
        normalize: bool = True,
    ):
        self.sample_rate = sample_rate
        self.output_sample_rate = output_sample_rate
        self.normalize = normalize

    def load_audio(
        self,
        path: Union[str, Path],
        target_sr: Optional[int] = None,
    ) -> Tuple[np.ndarray, int]:
        """Load audio file and resample if needed"""
        target_sr = target_sr or self.sample_rate

        audio, sr = librosa.load(path, sr=target_sr, mono=True)

        if self.normalize:
            audio = self.normalize_audio(audio)

        logger.debug(f"Loaded audio: {path}, duration={len(audio)/sr:.2f}s")
        return audio, sr

    def save_audio(
        self,
        audio: np.ndarray,
        path: Union[str, Path],
        sample_rate: Optional[int] = None,
        format: str = "wav",
    ) -> Path:
        """Save audio to file"""
        sr = sample_rate or self.output_sample_rate
        path = Path(path)

        # Resample if needed
        if sr != self.sample_rate:
            audio = librosa.resample(audio, orig_sr=self.sample_rate, target_sr=sr)

        sf.write(path, audio, sr, format=format)
        logger.debug(f"Saved audio: {path}")
        return path

    def to_bytes(
        self,
        audio: np.ndarray,
        sample_rate: Optional[int] = None,
        format: str = "wav",
    ) -> bytes:
        """Convert audio to bytes"""
        sr = sample_rate or self.output_sample_rate

        # Resample if needed
        if sr != self.sample_rate:
            audio = librosa.resample(audio, orig_sr=self.sample_rate, target_sr=sr)

        buffer = io.BytesIO()
        sf.write(buffer, audio, sr, format=format)
        buffer.seek(0)
        return buffer.read()

    def normalize_audio(self, audio: np.ndarray) -> np.ndarray:
        """Normalize audio to [-1, 1] range"""
        max_val = np.abs(audio).max()
        if max_val > 0:
            audio = audio / max_val * 0.95
        return audio

    def trim_silence(
        self,
        audio: np.ndarray,
        top_db: int = 30,
    ) -> np.ndarray:
        """Trim silence from audio"""
        trimmed, _ = librosa.effects.trim(audio, top_db=top_db)
        return trimmed

    def get_duration(self, audio: np.ndarray, sample_rate: Optional[int] = None) -> float:
        """Get audio duration in seconds"""
        sr = sample_rate or self.sample_rate
        return len(audio) / sr

    def resample(
        self,
        audio: np.ndarray,
        orig_sr: int,
        target_sr: int,
    ) -> np.ndarray:
        """Resample audio"""
        return librosa.resample(audio, orig_sr=orig_sr, target_sr=target_sr)

    def concatenate(self, audio_list: list[np.ndarray]) -> np.ndarray:
        """Concatenate multiple audio arrays"""
        return np.concatenate(audio_list)

    def add_silence(
        self,
        audio: np.ndarray,
        duration: float,
        position: str = "end",
    ) -> np.ndarray:
        """Add silence to audio"""
        silence = np.zeros(int(duration * self.sample_rate))

        if position == "start":
            return np.concatenate([silence, audio])
        elif position == "end":
            return np.concatenate([audio, silence])
        else:
            return np.concatenate([silence, audio, silence])

    def apply_fade(
        self,
        audio: np.ndarray,
        fade_in: float = 0.01,
        fade_out: float = 0.01,
    ) -> np.ndarray:
        """Apply fade in/out to audio"""
        fade_in_samples = int(fade_in * self.sample_rate)
        fade_out_samples = int(fade_out * self.sample_rate)

        # Fade in
        if fade_in_samples > 0:
            fade_in_curve = np.linspace(0, 1, fade_in_samples)
            audio[:fade_in_samples] *= fade_in_curve

        # Fade out
        if fade_out_samples > 0:
            fade_out_curve = np.linspace(1, 0, fade_out_samples)
            audio[-fade_out_samples:] *= fade_out_curve

        return audio

    def extract_mel_spectrogram(
        self,
        audio: np.ndarray,
        n_mels: int = 80,
        n_fft: int = 1024,
        hop_length: int = 256,
    ) -> np.ndarray:
        """Extract mel spectrogram"""
        mel = librosa.feature.melspectrogram(
            y=audio,
            sr=self.sample_rate,
            n_mels=n_mels,
            n_fft=n_fft,
            hop_length=hop_length,
        )
        return librosa.power_to_db(mel, ref=np.max)

    def chunk_audio(
        self,
        audio: np.ndarray,
        chunk_size: int = 1024,
    ) -> list[np.ndarray]:
        """Split audio into chunks for streaming"""
        chunks = []
        for i in range(0, len(audio), chunk_size):
            chunk = audio[i:i + chunk_size]
            if len(chunk) < chunk_size:
                # Pad last chunk
                chunk = np.pad(chunk, (0, chunk_size - len(chunk)))
            chunks.append(chunk)
        return chunks
