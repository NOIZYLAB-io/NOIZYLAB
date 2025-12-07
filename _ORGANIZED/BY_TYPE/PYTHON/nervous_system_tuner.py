# ROB OS - LAYER 3: NERVOUS SYSTEM TUNER
# ========================================
# Echo - Personal sanctuary profiler
# Learns what calms THIS specific nervous system

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

class NervousSystemType(Enum):
    """General nervous system profiles (not diagnoses, just patterns)."""
    STANDARD = "standard"
    SENSITIVE = "sensitive"          # HSP, easily overwhelmed
    AUTISTIC = "autistic"            # Specific sensory needs
    ADHD = "adhd"                    # Needs engagement, not just calm
    TRAUMA_AWARE = "trauma_aware"    # Needs predictability, safety
    CHRONIC_PAIN = "chronic_pain"    # Needs distraction, gentle
    UNKNOWN = "unknown"              # Haven't learned yet

@dataclass
class NervousSystemProfile:
    """A complete profile of what works for one nervous system."""
    user_id: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    
    # Self-identified type (optional, never required)
    self_identified_type: NervousSystemType = NervousSystemType.UNKNOWN
    
    # Sound preferences
    preferred_frequency_range: str = "full"  # "low", "mid", "high", "full"
    max_comfortable_volume: int = 75
    prefers_predictable_sounds: bool = True
    tolerates_sudden_sounds: bool = False
    
    # Specific sound preferences
    likes_nature_sounds: bool = True
    likes_music: bool = True
    likes_voice: bool = True
    likes_asmr: bool = False
    likes_binaural: bool = False
    
    # Specific sound aversions
    dislikes_high_frequencies: bool = False
    dislikes_bass: bool = False
    dislikes_voices: bool = False
    dislikes_animal_sounds: bool = False
    dislikes_mechanical_sounds: bool = False
    
    # Worlds that work
    effective_worlds: List[str] = field(default_factory=list)
    ineffective_worlds: List[str] = field(default_factory=list)
    
    # Breath/rhythm
    responds_to_guided_breath: bool = True
    preferred_breath_pace: str = "slow"  # "very_slow", "slow", "moderate"
    
    # Voice preferences
    preferred_voice_mode: str = "sanctuary"
    prefers_whisper: bool = False
    prefers_silence: bool = False
    
    # Learned patterns
    best_time_of_day: str = "any"  # "morning", "afternoon", "evening", "night", "any"
    average_session_duration: int = 300  # seconds
    
    # Notes
    special_notes: List[str] = field(default_factory=list)


class NervousSystemTuner:
    """
    Echo - The nervous system profiler.
    Learns what calms each specific person over time.
    """
    
    def __init__(self):
        self.profiles: Dict[str, NervousSystemProfile] = {}
        
        # Preset profiles for self-identified types
        self.type_presets = {
            NervousSystemType.AUTISTIC: {
                "prefers_predictable_sounds": True,
                "tolerates_sudden_sounds": False,
                "dislikes_high_frequencies": True,
                "likes_asmr": False,  # Many autistic people don't like ASMR
                "preferred_breath_pace": "slow",
                "max_comfortable_volume": 60,
                "effective_worlds": ["silent_shore", "rain_on_the_roof", "soft_tide"]
            },
            NervousSystemType.SENSITIVE: {
                "prefers_predictable_sounds": True,
                "tolerates_sudden_sounds": False,
                "max_comfortable_volume": 65,
                "preferred_breath_pace": "slow",
                "effective_worlds": ["fish_forest", "soft_tide", "rain_on_the_roof"]
            },
            NervousSystemType.ADHD: {
                "prefers_predictable_sounds": False,  # May need some variety
                "likes_music": True,
                "preferred_breath_pace": "moderate",
                "max_comfortable_volume": 75,
                "effective_worlds": ["mc96_midnight", "analog_dream", "city_glow"]
            },
            NervousSystemType.TRAUMA_AWARE: {
                "prefers_predictable_sounds": True,
                "tolerates_sudden_sounds": False,
                "dislikes_mechanical_sounds": True,
                "preferred_breath_pace": "very_slow",
                "max_comfortable_volume": 55,
                "effective_worlds": ["rain_on_the_roof", "silent_shore", "fish_forest"]
            },
            NervousSystemType.CHRONIC_PAIN: {
                "likes_music": True,
                "preferred_breath_pace": "slow",
                "max_comfortable_volume": 70,
                "effective_worlds": ["soft_tide", "rain_on_the_roof", "noizy_coast"]
            }
        }
    
    def get_or_create_profile(self, user_id: str) -> NervousSystemProfile:
        """Get existing profile or create a new one."""
        if user_id not in self.profiles:
            self.profiles[user_id] = NervousSystemProfile(user_id=user_id)
        return self.profiles[user_id]
    
    def set_self_identified_type(self, user_id: str, 
                                  ns_type: NervousSystemType) -> NervousSystemProfile:
        """
        Set a self-identified nervous system type and apply presets.
        This is ALWAYS optional and user-controlled.
        """
        profile = self.get_or_create_profile(user_id)
        profile.self_identified_type = ns_type
        
        # Apply presets if available
        if ns_type in self.type_presets:
            preset = self.type_presets[ns_type]
            for key, value in preset.items():
                if hasattr(profile, key):
                    setattr(profile, key, value)
        
        return profile
    
    def learn_from_session(self, user_id: str, session_data: Dict[str, Any]) -> None:
        """
        Learn from a sanctuary session.
        Updates the profile based on what worked or didn't.
        """
        profile = self.get_or_create_profile(user_id)
        
        world_used = session_data.get("world")
        was_effective = session_data.get("effective", False)
        
        if world_used:
            if was_effective and world_used not in profile.effective_worlds:
                profile.effective_worlds.append(world_used)
            elif not was_effective and world_used not in profile.ineffective_worlds:
                profile.ineffective_worlds.append(world_used)
        
        # Learn from adjustments
        if "turned_off_voice" in session_data:
            profile.prefers_silence = True
            profile.likes_voice = False
        
        if "lowered_volume" in session_data:
            new_max = session_data.get("final_volume", profile.max_comfortable_volume)
            profile.max_comfortable_volume = min(profile.max_comfortable_volume, new_max)
        
        if "used_breath" in session_data:
            profile.responds_to_guided_breath = session_data.get("breath_helped", True)
        
        # Update session duration average
        duration = session_data.get("duration_seconds", 0)
        if duration > 0:
            profile.average_session_duration = int(
                (profile.average_session_duration + duration) / 2
            )
    
    def get_personalized_sanctuary(self, user_id: str) -> Dict[str, Any]:
        """
        Get a fully personalized sanctuary setup for a user.
        """
        profile = self.get_or_create_profile(user_id)
        
        # Pick best world
        recommended_world = "rain_on_the_roof"  # Default
        if profile.effective_worlds:
            recommended_world = profile.effective_worlds[0]
        
        # Build personalized settings
        return {
            "world": recommended_world,
            "levels": {
                "music": min(50, profile.max_comfortable_volume),
                "ambience": min(65, profile.max_comfortable_volume),
                "voice": 30 if profile.likes_voice else 0
            },
            "safety": {
                "no_sudden_sounds": not profile.tolerates_sudden_sounds,
                "soft_highs_only": profile.dislikes_high_frequencies,
                "max_volume": profile.max_comfortable_volume
            },
            "extras": {
                "guided_breath": profile.responds_to_guided_breath,
                "asmr": profile.likes_asmr,
                "binaural": profile.likes_binaural
            },
            "voice_mode": profile.preferred_voice_mode if profile.likes_voice else "off",
            "personalization_level": "high" if len(profile.effective_worlds) > 2 else "learning"
        }
    
    def get_autistic_guest_settings(self) -> Dict[str, Any]:
        """
        Get default settings optimized for autistic guests.
        Based on research and the NOIZYLAB Sound Creed.
        """
        return {
            "world": "silent_shore",  # Start minimal
            "levels": {
                "music": 0,
                "ambience": 15,
                "voice": 0  # Voice off by default, user can enable
            },
            "safety": {
                "no_sudden_sounds": True,
                "soft_highs_only": True,
                "max_volume": 60
            },
            "extras": {
                "guided_breath": False,  # Offer, don't assume
                "asmr": False,
                "binaural": False
            },
            "voice_mode": "off",  # User controls this
            "note": "You control everything here. Nothing is forced.",
            "easy_exits": True  # Always show clear way to pause/stop
        }
    
    def get_2am_parent_settings(self) -> Dict[str, Any]:
        """
        Get settings optimized for exhausted late-night users.
        The burned-out parent at 2am scenario.
        """
        return {
            "world": "rain_on_the_roof",
            "levels": {
                "music": 30,
                "ambience": 70,
                "voice": 35
            },
            "safety": {
                "no_sudden_sounds": True,
                "soft_highs_only": False,
                "max_volume": 70
            },
            "extras": {
                "guided_breath": True,
                "asmr": False,
                "binaural": False
            },
            "voice_mode": "sanctuary",
            "message": "It's late. You made it here. Let's keep this small.",
            "offer_defer_tech": True  # "Handle this tomorrow?"
        }


# Singleton instance
_ns_tuner = None

def get_nervous_system_tuner() -> NervousSystemTuner:
    global _ns_tuner
    if _ns_tuner is None:
        _ns_tuner = NervousSystemTuner()
    return _ns_tuner

