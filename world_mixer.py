# ROB OS - LAYER 2: WORLD MIXER
# ==============================
# The control surface for Music / Ambience / Voice
# "Tune it for your nervous system."

from typing import Dict, Any, Optional
from dataclasses import dataclass, field
from .world_presets import WorldPreset, get_world_selector

@dataclass
class MixerState:
    """Current state of the world mixer."""
    world_id: str
    music_level: int = 50      # 0-100
    ambience_level: int = 50   # 0-100
    voice_level: int = 30      # 0-100
    
    # Safety toggles
    soft_highs_only: bool = False      # Reduces hiss/brightness
    no_sudden_sounds: bool = True      # Locks to safest SFX set
    
    # Extras
    guided_breath: bool = False
    asmr_textures: bool = False
    binaural_layer: bool = False
    
    # Voice mode
    voice_mode: str = "sanctuary"  # "guide", "sanctuary", "spark", "off"

@dataclass
class SanctuaryProfile:
    """Saved user sanctuary preferences."""
    profile_id: str
    user_id: str
    name: str = "My Sanctuary"
    
    # Preferred world
    default_world_id: str = "rain_on_the_roof"
    
    # Preferred levels
    music_level: int = 35
    ambience_level: int = 65
    voice_level: int = 30
    
    # Safety preferences
    soft_highs_only: bool = False
    no_sudden_sounds: bool = True
    
    # Extras
    guided_breath: bool = False
    asmr_textures: bool = False
    binaural_layer: bool = False
    
    # Learned preferences
    avoided_sounds: list = field(default_factory=list)  # ["thunder", "animal_sounds"]
    preferred_voice_mode: str = "sanctuary"


class WorldMixer:
    """
    The World Mixer - controls the soundscape for each session.
    """
    
    def __init__(self):
        self.world_selector = get_world_selector()
        self.current_state: Optional[MixerState] = None
        self.saved_profiles: Dict[str, SanctuaryProfile] = {}
    
    def load_world(self, world_id: str) -> MixerState:
        """
        Load a world preset and initialize the mixer.
        """
        world = self.world_selector.get_world(world_id)
        if not world:
            # Default to rain_on_the_roof if not found
            world = self.world_selector.get_world("rain_on_the_roof")
        
        self.current_state = MixerState(
            world_id=world.id,
            music_level=world.music_level,
            ambience_level=world.ambience_level,
            voice_level=world.voice_level,
            voice_mode=world.suggested_voice_mode,
            no_sudden_sounds=not world.has_sudden_sounds
        )
        
        return self.current_state
    
    def adjust_music(self, level: int) -> MixerState:
        """Adjust music level (0-100)."""
        if self.current_state:
            self.current_state.music_level = max(0, min(100, level))
        return self.current_state
    
    def adjust_ambience(self, level: int) -> MixerState:
        """Adjust ambience/environment level (0-100)."""
        if self.current_state:
            self.current_state.ambience_level = max(0, min(100, level))
        return self.current_state
    
    def adjust_voice(self, level: int) -> MixerState:
        """Adjust voice level (0-100)."""
        if self.current_state:
            self.current_state.voice_level = max(0, min(100, level))
        return self.current_state
    
    def set_voice_mode(self, mode: str) -> MixerState:
        """Set voice mode: guide, sanctuary, spark, or off."""
        if self.current_state and mode in ["guide", "sanctuary", "spark", "off"]:
            self.current_state.voice_mode = mode
        return self.current_state
    
    def toggle_safety(self, setting: str, enabled: bool) -> MixerState:
        """Toggle safety settings."""
        if self.current_state:
            if setting == "soft_highs_only":
                self.current_state.soft_highs_only = enabled
            elif setting == "no_sudden_sounds":
                self.current_state.no_sudden_sounds = enabled
        return self.current_state
    
    def toggle_extra(self, extra: str, enabled: bool) -> MixerState:
        """Toggle extras: guided_breath, asmr_textures, binaural_layer."""
        if self.current_state:
            if extra == "guided_breath":
                self.current_state.guided_breath = enabled
            elif extra == "asmr_textures":
                self.current_state.asmr_textures = enabled
            elif extra == "binaural_layer":
                self.current_state.binaural_layer = enabled
        return self.current_state
    
    def save_as_profile(self, user_id: str, name: str = "My Sanctuary") -> SanctuaryProfile:
        """
        Save current mixer state as a user's sanctuary profile.
        """
        if not self.current_state:
            return None
        
        profile = SanctuaryProfile(
            profile_id=f"{user_id}_sanctuary",
            user_id=user_id,
            name=name,
            default_world_id=self.current_state.world_id,
            music_level=self.current_state.music_level,
            ambience_level=self.current_state.ambience_level,
            voice_level=self.current_state.voice_level,
            soft_highs_only=self.current_state.soft_highs_only,
            no_sudden_sounds=self.current_state.no_sudden_sounds,
            guided_breath=self.current_state.guided_breath,
            asmr_textures=self.current_state.asmr_textures,
            binaural_layer=self.current_state.binaural_layer,
            preferred_voice_mode=self.current_state.voice_mode
        )
        
        self.saved_profiles[user_id] = profile
        return profile
    
    def load_profile(self, user_id: str) -> Optional[MixerState]:
        """
        Load a user's saved sanctuary profile.
        """
        profile = self.saved_profiles.get(user_id)
        if not profile:
            return None
        
        self.current_state = MixerState(
            world_id=profile.default_world_id,
            music_level=profile.music_level,
            ambience_level=profile.ambience_level,
            voice_level=profile.voice_level,
            soft_highs_only=profile.soft_highs_only,
            no_sudden_sounds=profile.no_sudden_sounds,
            guided_breath=profile.guided_breath,
            asmr_textures=profile.asmr_textures,
            binaural_layer=profile.binaural_layer,
            voice_mode=profile.preferred_voice_mode
        )
        
        return self.current_state
    
    def get_state(self) -> Optional[MixerState]:
        return self.current_state
    
    def get_ui_config(self) -> Dict[str, Any]:
        """
        Get the mixer configuration for UI rendering.
        """
        return {
            "header": {
                "title": "NOIZYLAB // Sanctuary",
                "subtitle": "This is your nervous system's living room.",
                "nav_buttons": ["Back to MC96", "Help"]
            },
            "sliders": [
                {
                    "id": "music",
                    "icon": "🎵",
                    "label": "Music",
                    "min": 0, "max": 100,
                    "labels": ["Off", "Deep"]
                },
                {
                    "id": "ambience",
                    "icon": "🌍",
                    "label": "Environment",
                    "min": 0, "max": 100,
                    "labels": ["Off", "Immersive"]
                },
                {
                    "id": "voice",
                    "icon": "🎙",
                    "label": "My Voice (Rob)",
                    "min": 0, "max": 100,
                    "labels": ["Off", "Close"]
                }
            ],
            "safety_toggles": [
                {
                    "id": "soft_highs_only",
                    "label": "Soft high sounds only",
                    "description": "Reduces hiss/brightness"
                },
                {
                    "id": "no_sudden_sounds",
                    "label": "No sudden sounds",
                    "description": "Locks to the safest SFX set"
                }
            ],
            "extras": [
                {
                    "id": "guided_breath",
                    "label": "Guided breath (Rob)",
                    "description": "Short, gentle breathing prompts in my voice."
                },
                {
                    "id": "asmr_textures",
                    "label": "ASMR textures",
                    "description": "Soft little sounds like pages, light taps. Only if you enjoy ASMR."
                },
                {
                    "id": "binaural_layer",
                    "label": "Binaural layer",
                    "description": "Low-level tones some people find calming. Easy to turn off."
                }
            ],
            "tip": "Try starting lower than you think, then bump it up slowly.",
            "boss_note": "You're the boss. If anything feels weird or wrong, switch it off."
        }


# Singleton instance
_world_mixer = None

def get_world_mixer() -> WorldMixer:
    global _world_mixer
    if _world_mixer is None:
        _world_mixer = WorldMixer()
    return _world_mixer

