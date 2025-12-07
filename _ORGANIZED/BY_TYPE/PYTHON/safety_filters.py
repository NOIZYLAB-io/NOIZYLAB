# ROB OS - LAYER 2: SAFETY FILTERS
# =================================
# Hush - The guardian of sensitive nervous systems
# "No jump scares. No surprise noise. No sharp animal shrieks."

from typing import Dict, Any, List, Set
from dataclasses import dataclass
from enum import Enum

class SoundSafetyLevel(Enum):
    MAXIMUM_SAFE = "maximum_safe"    # Silent Shore level - almost nothing
    AUTISTIC_SAFE = "autistic_safe"  # No sudden, no sharp, no surprises
    STANDARD_SAFE = "standard_safe"  # Gentle but more variety allowed
    UNRESTRICTED = "unrestricted"    # User explicitly wants everything

@dataclass
class SafetyProfile:
    """User's sound safety preferences."""
    level: SoundSafetyLevel
    blocked_categories: Set[str]
    max_high_frequency: int  # Hz - soft highs only
    max_transient_speed: float  # ms - no sudden attacks
    volume_ceiling: int  # 0-100

class SoundSafetyFilter:
    """
    Hush - The safety filter for all NOIZYLAB audio.
    Ensures no sound ever harms a sensitive nervous system.
    """
    
    def __init__(self):
        # Categories of sounds that can be blocked
        self.blockable_categories = {
            "thunder": "Thunder and lightning sounds",
            "animal_sounds": "Animal vocalizations (birds, dogs, etc.)",
            "sudden_impacts": "Sudden bangs, crashes, hits",
            "sharp_highs": "Bright, hissy, or piercing sounds",
            "alarms": "Alarm sounds, sirens, alerts",
            "voices_unknown": "Voices other than Rob",
            "bass_rumble": "Very low bass rumbles",
            "crowd_noise": "Multiple voices, crowd sounds",
            "mechanical": "Mechanical sounds, motors, machinery"
        }
        
        # Preset safety profiles
        self.presets = {
            SoundSafetyLevel.MAXIMUM_SAFE: SafetyProfile(
                level=SoundSafetyLevel.MAXIMUM_SAFE,
                blocked_categories=set(self.blockable_categories.keys()),
                max_high_frequency=8000,  # Hz
                max_transient_speed=500,  # ms (very slow attacks only)
                volume_ceiling=60
            ),
            SoundSafetyLevel.AUTISTIC_SAFE: SafetyProfile(
                level=SoundSafetyLevel.AUTISTIC_SAFE,
                blocked_categories={"thunder", "sudden_impacts", "alarms", "sharp_highs", "crowd_noise"},
                max_high_frequency=12000,
                max_transient_speed=200,
                volume_ceiling=75
            ),
            SoundSafetyLevel.STANDARD_SAFE: SafetyProfile(
                level=SoundSafetyLevel.STANDARD_SAFE,
                blocked_categories={"sudden_impacts", "alarms"},
                max_high_frequency=16000,
                max_transient_speed=50,
                volume_ceiling=90
            ),
            SoundSafetyLevel.UNRESTRICTED: SafetyProfile(
                level=SoundSafetyLevel.UNRESTRICTED,
                blocked_categories=set(),
                max_high_frequency=20000,
                max_transient_speed=1,
                volume_ceiling=100
            )
        }
        
        # Current active profile
        self.active_profile = self.presets[SoundSafetyLevel.AUTISTIC_SAFE]
    
    def set_safety_level(self, level: SoundSafetyLevel) -> SafetyProfile:
        """Set the overall safety level."""
        self.active_profile = self.presets[level]
        return self.active_profile
    
    def block_category(self, category: str) -> bool:
        """Add a category to the blocked list."""
        if category in self.blockable_categories:
            self.active_profile.blocked_categories.add(category)
            return True
        return False
    
    def unblock_category(self, category: str) -> bool:
        """Remove a category from the blocked list."""
        if category in self.active_profile.blocked_categories:
            self.active_profile.blocked_categories.remove(category)
            return True
        return False
    
    def check_sound_safe(self, sound_metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Check if a sound is safe to play given current settings.
        Returns safety status and any required modifications.
        """
        issues = []
        modifications = []
        
        # Check category
        sound_categories = sound_metadata.get("categories", [])
        for cat in sound_categories:
            if cat in self.active_profile.blocked_categories:
                issues.append(f"Blocked category: {cat}")
        
        # Check frequency content
        max_freq = sound_metadata.get("max_frequency", 20000)
        if max_freq > self.active_profile.max_high_frequency:
            modifications.append({
                "type": "lowpass_filter",
                "cutoff": self.active_profile.max_high_frequency
            })
        
        # Check transient speed
        attack_time = sound_metadata.get("attack_time_ms", 0)
        if attack_time < self.active_profile.max_transient_speed:
            modifications.append({
                "type": "soft_attack",
                "target_attack_ms": self.active_profile.max_transient_speed
            })
        
        # Check volume
        peak_level = sound_metadata.get("peak_level", 100)
        if peak_level > self.active_profile.volume_ceiling:
            modifications.append({
                "type": "volume_limit",
                "max_level": self.active_profile.volume_ceiling
            })
        
        return {
            "safe": len(issues) == 0,
            "issues": issues,
            "modifications_required": modifications,
            "can_play_with_modifications": len(issues) == 0 and len(modifications) > 0
        }
    
    def get_safe_world_flags(self) -> Dict[str, bool]:
        """
        Get the current safety flags for world selection.
        """
        return {
            "safe_for_autistic": self.active_profile.level in [
                SoundSafetyLevel.MAXIMUM_SAFE, 
                SoundSafetyLevel.AUTISTIC_SAFE
            ],
            "no_sudden_sounds": "sudden_impacts" in self.active_profile.blocked_categories,
            "no_thunder": "thunder" in self.active_profile.blocked_categories,
            "no_animal_sounds": "animal_sounds" in self.active_profile.blocked_categories,
            "soft_highs_only": self.active_profile.max_high_frequency <= 12000
        }
    
    def get_ui_config(self) -> Dict[str, Any]:
        """
        Get the safety filter configuration for UI rendering.
        """
        return {
            "current_level": self.active_profile.level.value,
            "level_options": [
                {
                    "id": "maximum_safe",
                    "label": "Maximum Safe",
                    "description": "Almost no sound. For severe sensory overload or migraines."
                },
                {
                    "id": "autistic_safe",
                    "label": "Autistic-Friendly",
                    "description": "No sudden sounds, sharp highs, or surprises. Default for sensitive systems."
                },
                {
                    "id": "standard_safe",
                    "label": "Standard Safe",
                    "description": "Gentle but more variety. Still no alarms or impacts."
                },
                {
                    "id": "unrestricted",
                    "label": "Unrestricted",
                    "description": "All sounds allowed. Only if you're sure."
                }
            ],
            "blockable_categories": [
                {"id": k, "label": v, "blocked": k in self.active_profile.blocked_categories}
                for k, v in self.blockable_categories.items()
            ],
            "note": "You can always turn sounds off. Nothing here is permanent."
        }


# Singleton instance
_safety_filter = None

def get_safety_filter() -> SoundSafetyFilter:
    global _safety_filter
    if _safety_filter is None:
        _safety_filter = SoundSafetyFilter()
    return _safety_filter

