"""
NoizyVoice Emotion Detection
============================
Detect emotions from voice characteristics.
"""

from typing import Dict, List, Tuple
import numpy as np
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class VoiceEmotion:
    """
    Detected emotion from voice.
    """
    primary: str = "neutral"
    confidence: float = 0.0
    valence: float = 0.5  # Negative to positive (0-1)
    arousal: float = 0.5  # Calm to excited (0-1)
    energy: float = 0.5   # Low to high energy (0-1)
    stress: float = 0.0   # Stress level (0-1)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict:
        return {
            "primary": self.primary,
            "confidence": self.confidence,
            "valence": self.valence,
            "arousal": self.arousal,
            "energy": self.energy,
            "stress": self.stress,
            "timestamp": self.timestamp,
        }


# Emotion categories
EMOTIONS = [
    "neutral",
    "happy",
    "sad",
    "angry",
    "fearful",
    "surprised",
    "disgusted",
    "calm",
    "excited",
    "tired",
    "stressed",
    "focused",
]


def detect_emotion(audio_bytes: bytes) -> VoiceEmotion:
    """
    Detect emotion from voice audio.
    Placeholder - replace with real emotion model.
    """
    result = VoiceEmotion()
    
    try:
        audio = np.frombuffer(audio_bytes, dtype=np.float32)
        
        # Extract simple features
        energy = np.mean(np.abs(audio))
        variance = np.var(audio)
        max_amp = np.max(np.abs(audio))
        
        # Simple heuristic classification
        result.energy = min(1.0, energy * 10)
        result.arousal = min(1.0, variance * 100)
        
        # Estimate stress from variance and energy
        result.stress = min(1.0, (variance * 50 + energy * 5) / 2)
        
        # Classify primary emotion
        if result.energy < 0.2:
            result.primary = "tired"
            result.valence = 0.4
        elif result.stress > 0.7:
            result.primary = "stressed"
            result.valence = 0.3
        elif result.arousal > 0.7 and result.energy > 0.6:
            result.primary = "excited"
            result.valence = 0.7
        elif result.arousal < 0.3 and result.energy < 0.4:
            result.primary = "calm"
            result.valence = 0.6
        elif result.energy > 0.5:
            result.primary = "focused"
            result.valence = 0.5
        else:
            result.primary = "neutral"
            result.valence = 0.5
        
        result.confidence = 0.6  # Placeholder confidence
        
    except Exception:
        pass
    
    return result


def detect_emotion_from_text(text: str) -> VoiceEmotion:
    """
    Detect emotion from transcribed text.
    Complements audio-based detection.
    """
    result = VoiceEmotion()
    text_lower = text.lower()
    
    # Keyword-based detection
    emotion_keywords = {
        "happy": ["happy", "great", "awesome", "love", "excited", "wonderful", "fantastic"],
        "sad": ["sad", "sorry", "unfortunately", "miss", "upset", "disappointed"],
        "angry": ["angry", "frustrated", "annoyed", "hate", "stupid", "damn"],
        "stressed": ["stressed", "overwhelmed", "too much", "can't handle", "pressure"],
        "tired": ["tired", "exhausted", "sleepy", "drained", "worn out"],
        "calm": ["calm", "relaxed", "peaceful", "okay", "fine", "good"],
        "excited": ["excited", "can't wait", "amazing", "incredible", "wow"],
        "fearful": ["scared", "afraid", "worried", "nervous", "anxious"],
    }
    
    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            if keyword in text_lower:
                result.primary = emotion
                result.confidence = 0.7
                
                # Set valence based on emotion
                if emotion in ["happy", "excited", "calm"]:
                    result.valence = 0.8
                elif emotion in ["sad", "angry", "stressed", "fearful"]:
                    result.valence = 0.2
                else:
                    result.valence = 0.5
                
                return result
    
    result.primary = "neutral"
    result.confidence = 0.5
    result.valence = 0.5
    
    return result


def combine_emotions(audio_emotion: VoiceEmotion, text_emotion: VoiceEmotion) -> VoiceEmotion:
    """
    Combine audio and text emotion detection.
    """
    # Weight audio more heavily
    audio_weight = 0.6
    text_weight = 0.4
    
    combined = VoiceEmotion()
    
    # Use higher confidence emotion as primary
    if audio_emotion.confidence >= text_emotion.confidence:
        combined.primary = audio_emotion.primary
    else:
        combined.primary = text_emotion.primary
    
    # Average the metrics
    combined.confidence = (audio_emotion.confidence * audio_weight + 
                          text_emotion.confidence * text_weight)
    combined.valence = (audio_emotion.valence * audio_weight + 
                       text_emotion.valence * text_weight)
    combined.arousal = audio_emotion.arousal  # Only from audio
    combined.energy = audio_emotion.energy    # Only from audio
    combined.stress = audio_emotion.stress    # Only from audio
    
    return combined


def get_recommended_response_tone(emotion: VoiceEmotion) -> str:
    """
    Get recommended AI response tone based on detected emotion.
    """
    if emotion.stress > 0.7:
        return "calm_supportive"
    elif emotion.primary == "angry":
        return "calm_patient"
    elif emotion.primary == "sad":
        return "empathetic_warm"
    elif emotion.primary == "excited":
        return "enthusiastic"
    elif emotion.primary == "tired":
        return "gentle_brief"
    elif emotion.primary == "happy":
        return "friendly_upbeat"
    else:
        return "neutral_helpful"


def should_activate_calm_mode(emotion: VoiceEmotion) -> bool:
    """
    Determine if calm mode should be activated.
    """
    return (
        emotion.stress > 0.7 or
        emotion.primary in ["stressed", "angry", "fearful"] or
        emotion.valence < 0.3
    )

