# ROB OS - LAYER 1: VOICE SUITE
# ==============================
# The Master Voice System - Rob // GUIDE, SANCTUARY, SPARK
# "Your voice makes this feel like a place built by a human being"

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum

class VoiceMode(Enum):
    GUIDE = "guide"           # Clear tech explanations, warm authority
    SANCTUARY = "sanctuary"   # Soft, calming, healing
    SPARK = "spark"           # Short energetic hits, celebration
    OFF = "off"               # No voice, just text + ambience

@dataclass
class VoiceSettings:
    mode: VoiceMode
    tempo: str          # "slow", "moderate", "quick"
    energy: int         # 1-10
    breathiness: float  # 0.0-1.0
    pause_weight: float # 0.0-1.0 (how much space between thoughts)

class VoiceBible:
    """
    The Voice Bible - Style sheet for AI Rob.
    Ensures any model knows how Rob should sound.
    """
    
    def __init__(self):
        # Core identity
        self.accent = "Canadian / North American neutral"
        self.vibe = "Warm, grounded, a bit wry, never slick or fake"
        self.identity = "Rob - the guy who built NOIZYLAB from pain and love"
        
        # Mode definitions
        self.modes = {
            VoiceMode.GUIDE: VoiceSettings(
                mode=VoiceMode.GUIDE,
                tempo="moderate",
                energy=7,
                breathiness=0.2,
                pause_weight=0.3
            ),
            VoiceMode.SANCTUARY: VoiceSettings(
                mode=VoiceMode.SANCTUARY,
                tempo="slow",
                energy=3,
                breathiness=0.5,
                pause_weight=0.7
            ),
            VoiceMode.SPARK: VoiceSettings(
                mode=VoiceMode.SPARK,
                tempo="quick",
                energy=8,
                breathiness=0.1,
                pause_weight=0.1
            )
        }
        
        # Signature phrases by mode
        self.signature_phrases = {
            VoiceMode.GUIDE: [
                "straight up",
                "honestly",
                "here's the deal",
                "let me break this down",
                "the truth is",
                "what I'd do if it were my machine"
            ],
            VoiceMode.SANCTUARY: [
                "you're not broken",
                "this is a lot",
                "you're allowed to be here as you are",
                "take your time",
                "there's no rush",
                "I've got you"
            ],
            VoiceMode.SPARK: [
                "nice",
                "we did it",
                "you're good to go",
                "system clear",
                "that's one less thing on your plate",
                "welcome back"
            ]
        }
        
        # Voice safety rules
        self.safety_rules = [
            "Voice cannot sell scammy products",
            "Voice cannot threaten, shame, or manipulate",
            "Voice cannot make medical promises",
            "Voice cannot pretend to be a doctor or therapist",
            "Voice must always label speculation vs fact",
            "Voice must default to compassion",
            "Voice must offer options, not commands"
        ]
    
    def get_mode_settings(self, mode: VoiceMode) -> VoiceSettings:
        return self.modes.get(mode, self.modes[VoiceMode.GUIDE])
    
    def get_signature_phrases(self, mode: VoiceMode) -> List[str]:
        return self.signature_phrases.get(mode, [])


class VoiceModeSelector:
    """
    Automatically selects the right Rob voice based on context.
    """
    
    def __init__(self):
        self.voice_bible = VoiceBible()
        
        # Context triggers for each mode
        self.sanctuary_triggers = [
            "freaking out", "panicking", "meltdown", "overwhelmed",
            "can't handle", "too much", "breaking down", "crying",
            "scared", "terrified", "lost everything", "disaster"
        ]
        
        self.spark_triggers = [
            "fixed", "working", "success", "done", "complete",
            "thank you", "amazing", "perfect", "love it"
        ]
        
        # User override phrases
        self.user_overrides = {
            "I'm overwhelmed": VoiceMode.SANCTUARY,
            "short answer only": VoiceMode.GUIDE,  # But brief
            "talk to me like I'm 10": VoiceMode.GUIDE,  # Simple
            "give me the full nerd": VoiceMode.GUIDE,  # Detailed
            "no voice": VoiceMode.OFF,
            "just text": VoiceMode.OFF,
            "mute": VoiceMode.OFF
        }
    
    def select_mode(self, user_input: str, context: Dict[str, Any]) -> VoiceMode:
        """
        Select the appropriate voice mode based on user state.
        """
        input_lower = user_input.lower()
        
        # Check for explicit user overrides first
        for phrase, mode in self.user_overrides.items():
            if phrase in input_lower:
                return mode
        
        # Check for sanctuary triggers (crisis/overwhelm)
        for trigger in self.sanctuary_triggers:
            if trigger in input_lower:
                return VoiceMode.SANCTUARY
        
        # Check for spark triggers (success/celebration)
        for trigger in self.spark_triggers:
            if trigger in input_lower:
                return VoiceMode.SPARK
        
        # Check context-based selection
        emotional_state = context.get("emotional_state", "stable")
        if emotional_state in ["crisis", "overloaded", "meltdown"]:
            return VoiceMode.SANCTUARY
        elif emotional_state in ["celebrating", "relieved", "happy"]:
            return VoiceMode.SPARK
        
        # Default to GUIDE for normal tech interactions
        return VoiceMode.GUIDE
    
    def get_emotional_throttle(self, mode: VoiceMode, intensity: str) -> Dict[str, Any]:
        """
        Adjust voice parameters based on emotional intensity.
        """
        settings = self.voice_bible.get_mode_settings(mode)
        
        if intensity == "high_stress":
            # Make everything softer, slower
            return {
                "tempo": "slow",
                "energy": max(1, settings.energy - 3),
                "pause_weight": min(1.0, settings.pause_weight + 0.3)
            }
        elif intensity == "curious":
            # Bit more energy and detail
            return {
                "tempo": "moderate",
                "energy": min(10, settings.energy + 1),
                "pause_weight": settings.pause_weight
            }
        
        return {
            "tempo": settings.tempo,
            "energy": settings.energy,
            "pause_weight": settings.pause_weight
        }


class MasterVoice:
    """
    The Master Voice controller.
    Coordinates voice mode, settings, and output.
    """
    
    def __init__(self):
        self.bible = VoiceBible()
        self.selector = VoiceModeSelector()
        self.current_mode = VoiceMode.GUIDE
        self.voice_enabled = True
    
    def speak(self, text: str, mode: Optional[VoiceMode] = None, 
              context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generate speech output with appropriate mode and settings.
        """
        if not self.voice_enabled:
            return {"mode": VoiceMode.OFF, "text": text, "audio": None}
        
        # Select mode if not specified
        if mode is None:
            mode = self.selector.select_mode(text, context or {})
        
        self.current_mode = mode
        settings = self.bible.get_mode_settings(mode)
        
        return {
            "mode": mode,
            "text": text,
            "settings": {
                "tempo": settings.tempo,
                "energy": settings.energy,
                "breathiness": settings.breathiness,
                "pause_weight": settings.pause_weight
            },
            "signature_phrases": self.bible.get_signature_phrases(mode)
        }
    
    def set_voice_enabled(self, enabled: bool):
        self.voice_enabled = enabled
    
    def get_current_mode(self) -> VoiceMode:
        return self.current_mode


# Singleton instance
_master_voice = None

def get_master_voice() -> MasterVoice:
    global _master_voice
    if _master_voice is None:
        _master_voice = MasterVoice()
    return _master_voice

