"""
NoizyVoice ASR (Automatic Speech Recognition)
=============================================
Speech-to-text engine using Whisper or custom models.
"""

from typing import Dict, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import numpy as np


@dataclass
class TranscriptionResult:
    """
    Result from speech recognition.
    """
    text: str = ""
    confidence: float = 0.0
    language: str = "en"
    duration_seconds: float = 0.0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    segments: list = field(default_factory=list)
    device_id: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            "text": self.text,
            "confidence": self.confidence,
            "language": self.language,
            "duration_seconds": self.duration_seconds,
            "timestamp": self.timestamp,
            "segments": self.segments,
            "device_id": self.device_id,
        }


# Whisper model instance (lazy loaded)
_whisper_model = None


def load_whisper_model(model_size: str = "base"):
    """
    Load Whisper model for transcription.
    """
    global _whisper_model
    
    try:
        import whisper
        _whisper_model = whisper.load_model(model_size)
        return True
    except ImportError:
        print("Whisper not installed. Using placeholder ASR.")
        return False
    except Exception as e:
        print(f"Failed to load Whisper: {e}")
        return False


def transcribe_audio(audio_bytes: bytes, device_id: str = None) -> TranscriptionResult:
    """
    Transcribe audio bytes to text.
    """
    global _whisper_model
    
    result = TranscriptionResult(device_id=device_id)
    
    # Try Whisper first
    if _whisper_model is not None:
        try:
            # Convert bytes to numpy array
            audio_array = np.frombuffer(audio_bytes, dtype=np.float32)
            
            # Transcribe
            whisper_result = _whisper_model.transcribe(audio_array)
            
            result.text = whisper_result.get("text", "").strip()
            result.language = whisper_result.get("language", "en")
            result.segments = whisper_result.get("segments", [])
            result.confidence = 0.9  # Whisper doesn't provide confidence
            
            return result
        except Exception as e:
            print(f"Whisper transcription failed: {e}")
    
    # Fallback placeholder
    result.text = transcribe_placeholder(audio_bytes)
    result.confidence = 0.5
    
    return result


def transcribe_file(file_path: str, device_id: str = None) -> TranscriptionResult:
    """
    Transcribe audio from a file.
    """
    global _whisper_model
    
    result = TranscriptionResult(device_id=device_id)
    
    if _whisper_model is not None:
        try:
            whisper_result = _whisper_model.transcribe(file_path)
            
            result.text = whisper_result.get("text", "").strip()
            result.language = whisper_result.get("language", "en")
            result.segments = whisper_result.get("segments", [])
            result.confidence = 0.9
            
            return result
        except Exception as e:
            print(f"Whisper file transcription failed: {e}")
    
    result.text = "[File transcription placeholder]"
    result.confidence = 0.3
    
    return result


def transcribe_placeholder(audio_bytes: bytes) -> str:
    """
    Placeholder transcription when Whisper is not available.
    """
    # Simple placeholder based on audio length
    audio_length = len(audio_bytes)
    
    if audio_length < 1000:
        return "[Short audio - no speech detected]"
    elif audio_length < 10000:
        return "[Audio received - placeholder transcription]"
    else:
        return "[Long audio received - placeholder transcription]"


def get_audio_duration(audio_bytes: bytes, sample_rate: int = 16000) -> float:
    """
    Calculate audio duration in seconds.
    """
    try:
        samples = len(audio_bytes) // 4  # Assuming float32
        return samples / sample_rate
    except Exception:
        return 0.0


def preprocess_audio(audio_bytes: bytes, sample_rate: int = 16000) -> np.ndarray:
    """
    Preprocess audio for ASR.
    """
    try:
        audio = np.frombuffer(audio_bytes, dtype=np.float32)
        
        # Normalize
        max_val = np.max(np.abs(audio))
        if max_val > 0:
            audio = audio / max_val
        
        return audio
    except Exception:
        return np.array([])


def detect_speech_activity(audio_bytes: bytes, threshold: float = 0.01) -> bool:
    """
    Detect if audio contains speech.
    """
    try:
        audio = np.frombuffer(audio_bytes, dtype=np.float32)
        energy = np.mean(np.abs(audio))
        return energy > threshold
    except Exception:
        return False


def is_model_loaded() -> bool:
    """
    Check if ASR model is loaded.
    """
    return _whisper_model is not None

