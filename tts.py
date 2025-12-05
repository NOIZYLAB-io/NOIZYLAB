"""
NoizyVoice TTS (Text-to-Speech)
===============================
AI voice output with personality-infused voices.
"""

from typing import Dict, Optional, List
from dataclasses import dataclass
from datetime import datetime
import base64


@dataclass
class TTSResult:
    """
    Result from TTS synthesis.
    """
    audio_base64: str = ""
    duration_seconds: float = 0.0
    voice_id: str = "default"
    text: str = ""
    success: bool = False
    error: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            "audio_base64": self.audio_base64,
            "duration_seconds": self.duration_seconds,
            "voice_id": self.voice_id,
            "text": self.text,
            "success": self.success,
            "error": self.error,
        }


# Voice personalities for AI Geniuses
VOICE_PROFILES = {
    "default": {
        "name": "Noizy Default",
        "pitch": 1.0,
        "speed": 1.0,
        "style": "neutral",
    },
    "assistant": {
        "name": "Noizy Assistant",
        "pitch": 1.0,
        "speed": 1.0,
        "style": "helpful",
    },
    "technician": {
        "name": "Noizy Tech",
        "pitch": 0.95,
        "speed": 1.1,
        "style": "professional",
    },
    "calm": {
        "name": "Noizy Calm",
        "pitch": 0.9,
        "speed": 0.85,
        "style": "soothing",
    },
    "friendly": {
        "name": "Noizy Friend",
        "pitch": 1.05,
        "speed": 1.0,
        "style": "casual",
    },
    "coach": {
        "name": "Noizy Coach",
        "pitch": 1.0,
        "speed": 1.05,
        "style": "motivational",
    },
    "gabriel": {
        "name": "Gabriel",
        "pitch": 0.95,
        "speed": 0.95,
        "style": "wise",
    },
}


def synthesize_speech(text: str, voice_id: str = "default") -> TTSResult:
    """
    Synthesize speech from text.
    Placeholder - integrate with real TTS engine.
    """
    result = TTSResult(text=text, voice_id=voice_id)
    
    # Get voice profile
    profile = VOICE_PROFILES.get(voice_id, VOICE_PROFILES["default"])
    
    # Try system TTS
    try:
        audio_data = synthesize_system_tts(text, profile)
        if audio_data:
            result.audio_base64 = base64.b64encode(audio_data).decode()
            result.duration_seconds = estimate_duration(text, profile["speed"])
            result.success = True
            return result
    except Exception as e:
        result.error = str(e)
    
    # Fallback: return placeholder
    result.success = False
    result.error = "TTS not available - text only"
    
    return result


def synthesize_system_tts(text: str, profile: Dict) -> Optional[bytes]:
    """
    Use system TTS (macOS say command or similar).
    """
    import subprocess
    import tempfile
    import os
    
    try:
        # Create temp file for audio
        with tempfile.NamedTemporaryFile(suffix=".aiff", delete=False) as f:
            temp_path = f.name
        
        # Use macOS say command
        rate = int(200 * profile.get("speed", 1.0))
        subprocess.run([
            "say",
            "-o", temp_path,
            "-r", str(rate),
            text
        ], check=True, capture_output=True)
        
        # Read audio file
        with open(temp_path, "rb") as f:
            audio_data = f.read()
        
        # Cleanup
        os.unlink(temp_path)
        
        return audio_data
    except Exception:
        return None


def estimate_duration(text: str, speed: float = 1.0) -> float:
    """
    Estimate speech duration based on text length.
    """
    # Average speaking rate: ~150 words per minute
    words = len(text.split())
    base_duration = (words / 150) * 60  # seconds
    return base_duration / speed


def get_voice_profile(voice_id: str) -> Dict:
    """
    Get voice profile by ID.
    """
    return VOICE_PROFILES.get(voice_id, VOICE_PROFILES["default"])


def list_voices() -> List[Dict]:
    """
    List all available voice profiles.
    """
    return [
        {"id": voice_id, **profile}
        for voice_id, profile in VOICE_PROFILES.items()
    ]


def register_voice(voice_id: str, name: str, pitch: float = 1.0, 
                   speed: float = 1.0, style: str = "neutral") -> bool:
    """
    Register a new voice profile.
    """
    VOICE_PROFILES[voice_id] = {
        "name": name,
        "pitch": pitch,
        "speed": speed,
        "style": style,
    }
    return True


def adjust_for_emotion(voice_id: str, emotion: str) -> Dict:
    """
    Adjust voice parameters based on emotion context.
    """
    profile = get_voice_profile(voice_id).copy()
    
    emotion_adjustments = {
        "stressed": {"speed": 0.9, "pitch": 0.95},
        "excited": {"speed": 1.1, "pitch": 1.05},
        "sad": {"speed": 0.85, "pitch": 0.9},
        "calm": {"speed": 0.9, "pitch": 0.95},
        "angry": {"speed": 0.95, "pitch": 0.9},
    }
    
    if emotion in emotion_adjustments:
        adj = emotion_adjustments[emotion]
        profile["speed"] *= adj.get("speed", 1.0)
        profile["pitch"] *= adj.get("pitch", 1.0)
    
    return profile

