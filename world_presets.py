# ROB OS - LAYER 2: WORLD PRESETS
# ================================
# Concrete sound worlds ready to implement
# Each world: name + vibe + default sliders

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum

class WorldCategory(Enum):
    NATURE = "nature"
    STUDIO = "studio"
    AMBIENT = "ambient"
    MINIMAL = "minimal"
    URBAN = "urban"
    ASMR = "asmr"

@dataclass
class WorldPreset:
    id: str
    name: str
    tagline: str
    description: str
    category: WorldCategory
    
    # Default slider values (0-100)
    music_level: int
    ambience_level: int
    voice_level: int
    
    # Voice mode suggestion
    suggested_voice_mode: str  # "sanctuary", "guide", "spark", "off"
    
    # Safety settings
    has_sudden_sounds: bool = False
    has_thunder: bool = False
    has_animal_sounds: bool = False
    brightness_level: str = "low"  # "low", "medium", "high"
    
    # Use case suggestions
    good_for: List[str] = None
    
    # Audio asset hints (for implementation)
    music_hints: List[str] = None
    ambience_hints: List[str] = None

# ============================================
# THE 10 CORE NOIZY WORLDS (v1 Set)
# ============================================

WORLD_PRESETS: Dict[str, WorldPreset] = {
    
    "fish_forest": WorldPreset(
        id="fish_forest",
        name="Fish Forest",
        tagline="Warm summer trees, gentle leaves, soft birds.",
        description="Summer trees, soft light, life but not busy. The sound of being safe in nature without the overwhelm.",
        category=WorldCategory.NATURE,
        music_level=35,
        ambience_level=65,
        voice_level=30,
        suggested_voice_mode="sanctuary",
        has_sudden_sounds=False,
        has_thunder=False,
        has_animal_sounds=True,  # Soft birds only
        brightness_level="medium",
        good_for=["crisis", "overwhelm", "gentle_start", "autistic_friendly"],
        music_hints=["soft_pads", "gentle_piano", "ambient_guitar"],
        ambience_hints=["leaves_rustling", "soft_birds", "gentle_wind", "distant_stream"]
    ),
    
    "noizy_coast": WorldPreset(
        id="noizy_coast",
        name="NOIZY Coast",
        tagline="Soft waves, distant birds, late-afternoon light.",
        description="Gentle late-afternoon shoreline. The sun is setting, the day is ending, everything is okay.",
        category=WorldCategory.NATURE,
        music_level=40,
        ambience_level=70,
        voice_level=20,
        suggested_voice_mode="sanctuary",
        has_sudden_sounds=False,
        has_thunder=False,
        has_animal_sounds=True,  # Far gulls
        brightness_level="medium",
        good_for=["burnout", "end_of_day", "tired", "recovery"],
        music_hints=["slow_pad", "bass_swells", "ambient_wash"],
        ambience_hints=["small_waves", "distant_gulls", "beach_air", "soft_wind"]
    ),
    
    "rain_on_the_roof": WorldPreset(
        id="rain_on_the_roof",
        name="Rain on the Roof",
        tagline="Safe inside, rain outside, piano in the other room.",
        description="You're inside, warm and dry. The storm is out there, but you're protected. Someone is playing piano somewhere in the house.",
        category=WorldCategory.AMBIENT,
        music_level=30,
        ambience_level=80,
        voice_level=40,
        suggested_voice_mode="sanctuary",
        has_sudden_sounds=False,
        has_thunder=False,  # Distant, very soft if any
        has_animal_sounds=False,
        brightness_level="low",
        good_for=["crisis", "2am_parent", "anxiety", "autistic_friendly", "sleep_prep"],
        music_hints=["piano", "rhodes", "slow_chords", "ambient_keys"],
        ambience_hints=["rain_on_roof", "distant_thunder_very_soft", "indoor_warmth", "crackling_optional"]
    ),
    
    "mc96_midnight": WorldPreset(
        id="mc96_midnight",
        name="MC96 Midnight",
        tagline="Quiet studio at 3am, gear humming, world asleep.",
        description="Deep studio, everyone else asleep. Just you and the machines. The hum of gear, the glow of screens, the peace of focused work.",
        category=WorldCategory.STUDIO,
        music_level=45,
        ambience_level=35,
        voice_level=15,
        suggested_voice_mode="guide",  # For focus work
        has_sudden_sounds=False,
        has_thunder=False,
        has_animal_sounds=False,
        brightness_level="low",
        good_for=["focus", "work", "creative_flow", "late_night", "builder_mode"],
        music_hints=["low_groove", "fish_music_3am", "ambient_electronic", "subtle_beat"],
        ambience_hints=["room_tone", "tape_hiss", "gear_hum", "keyboard_distant", "fan_very_soft"]
    ),
    
    "silent_shore": WorldPreset(
        id="silent_shore",
        name="Silent Shore",
        tagline="Almost no sound. Just enough to feel the room.",
        description="For when you need near-silence. Barely-there room tone. Maximum sensory rest.",
        category=WorldCategory.MINIMAL,
        music_level=0,
        ambience_level=10,
        voice_level=0,
        suggested_voice_mode="off",
        has_sudden_sounds=False,
        has_thunder=False,
        has_animal_sounds=False,
        brightness_level="low",
        good_for=["sensory_overload", "autistic_meltdown", "migraine", "maximum_quiet"],
        music_hints=[],
        ambience_hints=["barely_there_room_tone", "air_movement", "subtle_presence"]
    ),
    
    "soft_tide": WorldPreset(
        id="soft_tide",
        name="Soft Tide",
        tagline="Floating ambient cloud, nothing sharp or sudden.",
        description="Pure ambient float. No beat, no edges. Just lush, slow, enveloping sound.",
        category=WorldCategory.AMBIENT,
        music_level=60,
        ambience_level=40,
        voice_level=0,
        suggested_voice_mode="off",
        has_sudden_sounds=False,
        has_thunder=False,
        has_animal_sounds=False,
        brightness_level="low",
        good_for=["floating", "meditation", "deep_rest", "dissociation_recovery"],
        music_hints=["lush_pads", "slow_ambient", "no_beat", "evolving_textures"],
        ambience_hints=["gentle_water", "air", "soft_movement"]
    ),
    
    "asmr_cove": WorldPreset(
        id="asmr_cove",
        name="ASMR Cove",
        tagline="Soft little sounds like pages, light taps. For texture lovers.",
        description="For people who like ASMR textures. Soft pages, light taps, gentle rustles. Close Rob voice optional.",
        category=WorldCategory.ASMR,
        music_level=25,
        ambience_level=50,
        voice_level=50,
        suggested_voice_mode="sanctuary",  # Close whisper optional
        has_sudden_sounds=False,
        has_thunder=False,
        has_animal_sounds=False,
        brightness_level="low",
        good_for=["asmr_fans", "texture_seekers", "gentle_stimulation"],
        music_hints=["very_soft_ambient", "minimal_texture"],
        ambience_hints=["soft_pages", "light_taps", "rustles", "fabric", "close_mic_textures"]
    ),
    
    "city_glow": WorldPreset(
        id="city_glow",
        name="City Glow",
        tagline="Night city far away, you're in a quiet room.",
        description="The city is out there, alive and distant. You're in a quiet room looking out. Urban peace.",
        category=WorldCategory.URBAN,
        music_level=35,
        ambience_level=55,
        voice_level=20,
        suggested_voice_mode="guide",
        has_sudden_sounds=False,
        has_thunder=False,
        has_animal_sounds=False,
        brightness_level="low",
        good_for=["urban_comfort", "night_owl", "apartment_dweller"],
        music_hints=["muted_synths", "soft_chords", "lo_fi_ambient"],
        ambience_hints=["distant_traffic", "no_sirens", "city_hum", "window_air"]
    ),
    
    "analog_dream": WorldPreset(
        id="analog_dream",
        name="Analog Dream",
        tagline="Lo-fi tape loops, warm warble. 2NDLIFE homage.",
        description="Homage to the analog era. Tape loops, warm warble, the sound of imperfect machines making beautiful mistakes.",
        category=WorldCategory.STUDIO,
        music_level=50,
        ambience_level=30,
        voice_level=20,
        suggested_voice_mode="guide",
        has_sudden_sounds=False,
        has_thunder=False,
        has_animal_sounds=False,
        brightness_level="low",
        good_for=["nostalgia", "creative_work", "music_lovers", "fish_music_fans"],
        music_hints=["lo_fi_tape_loops", "warm_warble", "vintage_synths", "subtle_crackle"],
        ambience_hints=["tape_hiss", "subtle_clunks", "machine_warmth", "vinyl_surface"]
    ),
    
    "skyroom": WorldPreset(
        id="skyroom",
        name="Skyroom",
        tagline="Light, open, airy. Good for hopeful planning.",
        description="High up, windows everywhere, light streaming in. For when you need hope and clarity.",
        category=WorldCategory.AMBIENT,
        music_level=55,
        ambience_level=30,
        voice_level=25,
        suggested_voice_mode="guide",
        has_sudden_sounds=False,
        has_thunder=False,
        has_animal_sounds=False,
        brightness_level="medium",
        good_for=["planning", "hope", "morning", "fresh_start", "recovery"],
        music_hints=["airy_pads", "light_piano", "uplifting_ambient"],
        ambience_hints=["gentle_wind", "high_air", "open_space", "light_movement"]
    )
}


# ============================================
# WORLD SELECTOR LOGIC
# ============================================

class WorldSelector:
    """
    Selects appropriate world based on user state and context.
    """
    
    def __init__(self):
        self.presets = WORLD_PRESETS
        
        # State-to-world mapping
        self.state_recommendations = {
            "crisis": ["rain_on_the_roof", "fish_forest", "silent_shore"],
            "meltdown": ["silent_shore", "rain_on_the_roof"],
            "overwhelmed": ["rain_on_the_roof", "fish_forest", "soft_tide"],
            "stressed": ["noizy_coast", "rain_on_the_roof", "fish_forest"],
            "burned_out": ["soft_tide", "noizy_coast", "rain_on_the_roof"],
            "tired": ["soft_tide", "rain_on_the_roof", "noizy_coast"],
            "focus": ["mc96_midnight", "analog_dream", "city_glow"],
            "creative": ["mc96_midnight", "analog_dream", "skyroom"],
            "hopeful": ["skyroom", "fish_forest", "noizy_coast"],
            "okay": ["fish_forest", "noizy_coast", "mc96_midnight"],
            "sensory_overload": ["silent_shore", "soft_tide"]
        }
    
    def get_world(self, world_id: str) -> Optional[WorldPreset]:
        return self.presets.get(world_id)
    
    def get_all_worlds(self) -> Dict[str, WorldPreset]:
        return self.presets
    
    def recommend_for_state(self, state: str) -> List[WorldPreset]:
        """
        Recommend worlds based on emotional state.
        """
        world_ids = self.state_recommendations.get(state.lower(), ["fish_forest"])
        return [self.presets[wid] for wid in world_ids if wid in self.presets]
    
    def get_autistic_safe_worlds(self) -> List[WorldPreset]:
        """
        Get worlds specifically safe for autistic/sensory-sensitive users.
        """
        safe_worlds = []
        for world in self.presets.values():
            if (not world.has_sudden_sounds and 
                not world.has_thunder and 
                world.brightness_level == "low"):
                safe_worlds.append(world)
        return safe_worlds
    
    def get_worlds_by_category(self, category: WorldCategory) -> List[WorldPreset]:
        return [w for w in self.presets.values() if w.category == category]


# Singleton instance
_world_selector = None

def get_world_selector() -> WorldSelector:
    global _world_selector
    if _world_selector is None:
        _world_selector = WorldSelector()
    return _world_selector

