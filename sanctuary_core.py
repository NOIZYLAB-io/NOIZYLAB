# backend_ultra/sanctuary/sanctuary_core.py
# NOIZYLAB SANCTUARY SYSTEM
# Science-backed calming layer for nervous system regulation
# ═══════════════════════════════════════════════════════════════════════════════
#
# RESEARCH FOUNDATION:
# - Music & rhythm for autism: emotional regulation, sensory organization
# - Music therapy: reduces anxiety/stress in medical & mental health settings
# - ASMR: reduces heart rate, improves relaxation, feeling of being cared for
# - Binaural beats: statistically real nudges toward calm
# - Slow sound + gentle voice + guided breathing = moves people out of fight/flight
#
# THE PATTERN:
# Slow, predictable sound + Gentle, non-threatening voice + Guided breathing
# → Rest/digest / social connection mode
# ═══════════════════════════════════════════════════════════════════════════════

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum
import time

# ═══════════════════════════════════════════════════════════════════════════════
# SANCTUARY PHILOSOPHY
# ═══════════════════════════════════════════════════════════════════════════════

SANCTUARY_PHILOSOPHY = """
NOIZYLAB SANCTUARY: WHERE NERVOUS SYSTEMS COME TO REST

"Every single person is essential to this world's happiness & joy."

WHAT SANCTUARY IS:
• A space where sound is on YOUR side — structured, safe, inviting
• A place to slow down, breathe, feel seen, and not be judged
• A reminder that you actually matter

WHAT SANCTUARY IS NOT:
• A replacement for serious medical treatment
• A claim to "fix" autism (autistic people aren't broken)
• One frequency away from curing all disease

WHAT SCIENCE TELLS US:
• Sound, music, and intentional breath CAN reduce anxiety, pain, and stress
• For autistic people, rhythm and music CAN support sensory regulation
• ASMR / calming soundscapes give many people a felt sense of care and safety
• These are real, measurable physiological shifts — not just vibes

THE POWER:
As part of a humane, AI-powered, compassion-driven space where people can:
• Slow down
• Breathe
• Feel seen and not judged
• Be reminded they actually matter
...it's powerful as hell.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SENSORY PROFILES (Extreme respect for individual needs)
# ═══════════════════════════════════════════════════════════════════════════════

class SensoryProfile(Enum):
    SOUND_SEEKING = "sound_seeking"      # Loves rich soundscapes, ASMR, textures
    SOUND_NEUTRAL = "sound_neutral"      # Comfortable with moderate sound
    SOUND_SENSITIVE = "sound_sensitive"  # Needs almost-silent, super-gentle audio
    VOICE_PREFERRED = "voice_preferred"  # Finds voice calming
    VOICE_OPTIONAL = "voice_optional"    # Can take or leave voice
    VOICE_AVOIDED = "voice_avoided"      # Prefers no voice, just ambient

@dataclass
class UserSensoryPreferences:
    """Individual sensory preferences for sanctuary experience."""
    profile: SensoryProfile = SensoryProfile.SOUND_NEUTRAL
    
    # Volume preferences (0.0 - 1.0)
    preferred_volume: float = 0.5
    max_comfortable_volume: float = 0.7
    
    # Texture preferences
    prefers_pure_tones: bool = False
    prefers_ambient: bool = True
    prefers_quiet_piano: bool = False
    prefers_nature_sounds: bool = True
    
    # Voice preferences
    wants_voice: bool = True
    voice_speed: str = "slow"  # "normal", "slow", "very_slow"
    
    # Specific sensitivities
    avoid_high_frequencies: bool = False
    avoid_sudden_changes: bool = True
    avoid_stereo_movement: bool = False
    
    def to_sonic_config(self) -> Dict[str, Any]:
        """Convert preferences to sonic bed configuration."""
        return {
            "volume": self.preferred_volume,
            "max_volume": self.max_comfortable_volume,
            "textures": {
                "pure_tones": self.prefers_pure_tones,
                "ambient": self.prefers_ambient,
                "piano": self.prefers_quiet_piano,
                "nature": self.prefers_nature_sounds
            },
            "voice": {
                "enabled": self.wants_voice,
                "speed": self.voice_speed
            },
            "safety": {
                "filter_high_freq": self.avoid_high_frequencies,
                "smooth_transitions": self.avoid_sudden_changes,
                "static_stereo": self.avoid_stereo_movement
            }
        }

# ═══════════════════════════════════════════════════════════════════════════════
# SONIC BED (The foundation layer)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class SonicBedConfig:
    """
    Configuration for the sonic bed — the ambient sound foundation.
    
    Research-aligned design:
    - Tempo: slow or non-metric, avoid sudden changes
    - Timbre: soft, warm, no harsh high-frequency spikes
    - Movement: very gentle stereo motion, nothing dizzying
    """
    tempo: str = "non_metric"  # "slow", "non_metric", "none"
    bpm: Optional[int] = None  # Only if tempo is "slow"
    
    # Timbre
    warmth: float = 0.8  # 0.0 = cold, 1.0 = very warm
    brightness: float = 0.3  # 0.0 = dark, 1.0 = bright (keep low)
    high_freq_filter: float = 0.7  # Cut harsh highs
    
    # Movement
    stereo_width: float = 0.3  # 0.0 = mono, 1.0 = wide (keep gentle)
    stereo_movement_speed: float = 0.1  # Very slow panning
    
    # Layers
    layers: List[str] = field(default_factory=lambda: ["pad", "nature"])
    
    # Transitions
    fade_time_seconds: float = 3.0  # Slow, gentle transitions
    
    def get_safe_config(self, preferences: UserSensoryPreferences) -> Dict[str, Any]:
        """Get a safe configuration respecting user preferences."""
        config = {
            "tempo": self.tempo,
            "bpm": self.bpm,
            "warmth": self.warmth,
            "brightness": min(self.brightness, 0.4) if preferences.avoid_high_frequencies else self.brightness,
            "high_freq_filter": max(self.high_freq_filter, 0.8) if preferences.avoid_high_frequencies else self.high_freq_filter,
            "stereo_width": 0.0 if preferences.avoid_stereo_movement else self.stereo_width,
            "stereo_movement_speed": 0.0 if preferences.avoid_stereo_movement else self.stereo_movement_speed,
            "layers": self.layers,
            "fade_time_seconds": max(self.fade_time_seconds, 5.0) if preferences.avoid_sudden_changes else self.fade_time_seconds,
            "volume": preferences.preferred_volume
        }
        return config

# ═══════════════════════════════════════════════════════════════════════════════
# VOICE LAYER (AI Rob modes)
# ═══════════════════════════════════════════════════════════════════════════════

class VoiceMode(Enum):
    GUIDE = "guide"           # "Here's what's happening, here's the plan."
    SANCTUARY = "sanctuary"   # Slower, softer, breathing & reassurance
    SILENT = "silent"         # No voice, just ambient

@dataclass
class VoiceLayerConfig:
    """
    Configuration for the voice layer.
    
    Modes:
    - Guide Rob: "Here's what's happening, here's the plan."
    - Sanctuary Rob: slower, softer, breathing & reassurance
    """
    mode: VoiceMode = VoiceMode.GUIDE
    
    # Speed (words per minute equivalent)
    speed: str = "normal"  # "normal", "slow", "very_slow"
    speed_values = {"normal": 1.0, "slow": 0.8, "very_slow": 0.6}
    
    # Tone
    warmth: float = 0.8  # Higher = warmer voice
    pitch_variance: float = 0.3  # Lower = more monotone/calming
    
    # Pauses
    pause_between_sentences: float = 1.5  # seconds
    pause_for_breath_cue: float = 3.0  # seconds
    
    # Content style
    acknowledge_stress: bool = True
    invite_breath: bool = True
    recenter_agency: bool = True

SANCTUARY_VOICE_TEMPLATES = {
    "acknowledge_stress": [
        "This is a lot. It's okay to feel that.",
        "I can tell this is overwhelming. That's completely valid.",
        "Your nervous system is working hard right now. Let's help it settle.",
        "It makes sense that you're stressed. This situation is stressful."
    ],
    "invite_breath": [
        "Let's take one slow breath together.",
        "If you'd like, take a breath with me. In... and out.",
        "Just one breath. That's all we need right now.",
        "Breathe in slowly... and let it go."
    ],
    "recenter_agency": [
        "You're not broken. Your nervous system is just overloaded. We can help it settle.",
        "You are safe in this moment.",
        "Nothing needs to happen right now except this breath.",
        "You're doing better than you think.",
        "You matter. Your wellbeing matters. The computer can wait."
    ],
    "grounding": [
        "Feel your feet on the floor. Feel the chair supporting you.",
        "Notice three things you can see right now.",
        "You are here. You are safe. We'll figure this out together.",
        "Right now, in this moment, you have everything you need."
    ]
}

def get_sanctuary_voice_script(
    acknowledge: bool = True,
    breath: bool = True,
    recenter: bool = True,
    grounding: bool = False
) -> List[str]:
    """Generate a sanctuary voice script."""
    script = []
    
    if acknowledge:
        import random
        script.append(random.choice(SANCTUARY_VOICE_TEMPLATES["acknowledge_stress"]))
    
    if breath:
        script.append(random.choice(SANCTUARY_VOICE_TEMPLATES["invite_breath"]))
    
    if recenter:
        script.append(random.choice(SANCTUARY_VOICE_TEMPLATES["recenter_agency"]))
    
    if grounding:
        script.append(random.choice(SANCTUARY_VOICE_TEMPLATES["grounding"]))
    
    return script

# ═══════════════════════════════════════════════════════════════════════════════
# MICRO-RITUALS (30-60 second calming interventions)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class MicroRitual:
    """
    A 30-60 second calming micro-ritual.
    
    Structure:
    1. 1-2 slow breaths paced by voice
    2. One grounding line
    3. Stop — don't lecture, let silence + music do the work
    """
    id: str
    name: str
    duration_seconds: int
    breath_count: int
    grounding_line: str
    sonic_bed: str  # Reference to sonic bed preset
    voice_enabled: bool = True

MICRO_RITUALS = {
    "noizy_breath": MicroRitual(
        id="noizy_breath",
        name="NOIZY Breath",
        duration_seconds=45,
        breath_count=2,
        grounding_line="You are safe in this moment.",
        sonic_bed="gentle_pad",
        voice_enabled=True
    ),
    "silent_reset": MicroRitual(
        id="silent_reset",
        name="Silent Reset",
        duration_seconds=30,
        breath_count=1,
        grounding_line="",  # No voice
        sonic_bed="nature_ambient",
        voice_enabled=False
    ),
    "agency_restore": MicroRitual(
        id="agency_restore",
        name="Agency Restore",
        duration_seconds=60,
        breath_count=3,
        grounding_line="You're not broken. Your nervous system is just overloaded. We can help it settle.",
        sonic_bed="warm_drone",
        voice_enabled=True
    ),
    "tech_pause": MicroRitual(
        id="tech_pause",
        name="Tech Pause",
        duration_seconds=45,
        breath_count=2,
        grounding_line="The computer can wait. You matter more than any machine.",
        sonic_bed="gentle_pad",
        voice_enabled=True
    )
}

def execute_micro_ritual(ritual_id: str, preferences: UserSensoryPreferences) -> Dict[str, Any]:
    """Execute a micro-ritual with user preferences."""
    ritual = MICRO_RITUALS.get(ritual_id)
    if not ritual:
        return {"error": f"Ritual '{ritual_id}' not found"}
    
    # Build the ritual sequence
    sequence = []
    
    # 1. Fade in sonic bed
    sequence.append({
        "type": "sonic_bed",
        "action": "fade_in",
        "preset": ritual.sonic_bed,
        "duration": 2.0,
        "volume": preferences.preferred_volume
    })
    
    # 2. Breaths (if voice enabled and user wants voice)
    if ritual.voice_enabled and preferences.wants_voice:
        for i in range(ritual.breath_count):
            sequence.append({
                "type": "voice",
                "text": "Breathe in slowly..." if i == 0 else "And again...",
                "pause_after": 3.0
            })
            sequence.append({
                "type": "voice",
                "text": "And let it go.",
                "pause_after": 2.0
            })
    else:
        # Silent breaths - just timing
        sequence.append({
            "type": "pause",
            "duration": ritual.breath_count * 5.0
        })
    
    # 3. Grounding line (if provided and voice enabled)
    if ritual.grounding_line and ritual.voice_enabled and preferences.wants_voice:
        sequence.append({
            "type": "voice",
            "text": ritual.grounding_line,
            "pause_after": 3.0
        })
    
    # 4. Let silence + music do the work
    remaining_time = ritual.duration_seconds - sum([
        s.get("duration", 0) + s.get("pause_after", 0) 
        for s in sequence
    ])
    if remaining_time > 0:
        sequence.append({
            "type": "pause",
            "duration": max(remaining_time, 5.0)
        })
    
    # 5. Gentle fade out
    sequence.append({
        "type": "sonic_bed",
        "action": "fade_out",
        "duration": 3.0
    })
    
    return {
        "ritual": ritual,
        "sequence": sequence,
        "total_duration": ritual.duration_seconds,
        "voice_enabled": ritual.voice_enabled and preferences.wants_voice
    }

# ═══════════════════════════════════════════════════════════════════════════════
# SANCTUARY MODES (Full experience presets)
# ═══════════════════════════════════════════════════════════════════════════════

class SanctuaryMode(Enum):
    QUICK_CALM = "quick_calm"      # 30-60 seconds, just breathe
    DEEP_REST = "deep_rest"        # 5-15 minutes, full immersion
    CRISIS_ANCHOR = "crisis_anchor"  # For panic/meltdown moments
    BACKGROUND_PEACE = "background_peace"  # Ongoing ambient support

@dataclass
class SanctuaryModeConfig:
    """Configuration for a full sanctuary mode."""
    id: str
    name: str
    description: str
    duration_range: str  # e.g., "30-60 seconds"
    sonic_bed: SonicBedConfig
    voice_mode: VoiceMode
    micro_rituals: List[str]  # Which rituals are available
    intensity: float  # 0.0 = very subtle, 1.0 = full immersion

SANCTUARY_MODES = {
    SanctuaryMode.QUICK_CALM: SanctuaryModeConfig(
        id="quick_calm",
        name="Quick Calm",
        description="30-60 seconds. Just breathe. Reset your nervous system.",
        duration_range="30-60 seconds",
        sonic_bed=SonicBedConfig(tempo="non_metric", warmth=0.8, brightness=0.2),
        voice_mode=VoiceMode.SANCTUARY,
        micro_rituals=["noizy_breath", "silent_reset"],
        intensity=0.5
    ),
    SanctuaryMode.DEEP_REST: SanctuaryModeConfig(
        id="deep_rest",
        name="Deep Rest",
        description="5-15 minutes. Full immersion. Let everything else go.",
        duration_range="5-15 minutes",
        sonic_bed=SonicBedConfig(tempo="non_metric", warmth=0.9, brightness=0.1, stereo_width=0.4),
        voice_mode=VoiceMode.SANCTUARY,
        micro_rituals=["noizy_breath", "agency_restore"],
        intensity=0.8
    ),
    SanctuaryMode.CRISIS_ANCHOR: SanctuaryModeConfig(
        id="crisis_anchor",
        name="Crisis Anchor",
        description="For panic or meltdown moments. Ultra-simple. Ultra-safe.",
        duration_range="As long as needed",
        sonic_bed=SonicBedConfig(tempo="none", warmth=1.0, brightness=0.0, stereo_width=0.0),
        voice_mode=VoiceMode.SANCTUARY,
        micro_rituals=["noizy_breath", "agency_restore", "tech_pause"],
        intensity=0.3  # Very gentle, not overwhelming
    ),
    SanctuaryMode.BACKGROUND_PEACE: SanctuaryModeConfig(
        id="background_peace",
        name="Background Peace",
        description="Ongoing ambient support while you work or rest.",
        duration_range="Ongoing",
        sonic_bed=SonicBedConfig(tempo="non_metric", warmth=0.7, brightness=0.3, stereo_width=0.2),
        voice_mode=VoiceMode.SILENT,
        micro_rituals=[],
        intensity=0.2  # Very subtle
    )
}

# ═══════════════════════════════════════════════════════════════════════════════
# SANCTUARY ENGINE (Main orchestrator)
# ═══════════════════════════════════════════════════════════════════════════════

class SanctuaryEngine:
    """
    The main Sanctuary Engine that orchestrates calming experiences.
    
    "As part of a humane, AI-powered, compassion-driven space where people can:
    • Slow down
    • Breathe
    • Feel seen and not judged
    • Be reminded they actually matter
    ...it's powerful as hell."
    """
    
    def __init__(self):
        self.active_mode: Optional[SanctuaryMode] = None
        self.user_preferences: UserSensoryPreferences = UserSensoryPreferences()
        self.session_start: Optional[float] = None
    
    def set_preferences(self, preferences: UserSensoryPreferences):
        """Set user sensory preferences."""
        self.user_preferences = preferences
    
    def start_sanctuary(self, mode: SanctuaryMode) -> Dict[str, Any]:
        """Start a sanctuary session."""
        self.active_mode = mode
        self.session_start = time.time()
        
        mode_config = SANCTUARY_MODES[mode]
        sonic_config = mode_config.sonic_bed.get_safe_config(self.user_preferences)
        
        return {
            "status": "started",
            "mode": mode.value,
            "mode_name": mode_config.name,
            "description": mode_config.description,
            "sonic_config": sonic_config,
            "voice_mode": mode_config.voice_mode.value,
            "available_rituals": mode_config.micro_rituals,
            "message": self._get_welcome_message(mode)
        }
    
    def _get_welcome_message(self, mode: SanctuaryMode) -> str:
        """Get a welcome message for the sanctuary mode."""
        messages = {
            SanctuaryMode.QUICK_CALM: "Let's take a moment. Just breathe.",
            SanctuaryMode.DEEP_REST: "You're safe here. Let everything else go for a while.",
            SanctuaryMode.CRISIS_ANCHOR: "I'm here. You're not alone. Let's just breathe together.",
            SanctuaryMode.BACKGROUND_PEACE: "Gentle sounds in the background. You do your thing."
        }
        return messages.get(mode, "Welcome to Sanctuary.")
    
    def trigger_ritual(self, ritual_id: str) -> Dict[str, Any]:
        """Trigger a micro-ritual."""
        return execute_micro_ritual(ritual_id, self.user_preferences)
    
    def get_voice_script(self, context: str = "general") -> List[str]:
        """Get an appropriate voice script for the current context."""
        if context == "crisis":
            return get_sanctuary_voice_script(acknowledge=True, breath=True, recenter=True, grounding=True)
        elif context == "stressed":
            return get_sanctuary_voice_script(acknowledge=True, breath=True, recenter=True, grounding=False)
        else:
            return get_sanctuary_voice_script(acknowledge=False, breath=True, recenter=False, grounding=False)
    
    def end_sanctuary(self) -> Dict[str, Any]:
        """End the sanctuary session."""
        duration = time.time() - self.session_start if self.session_start else 0
        
        result = {
            "status": "ended",
            "mode": self.active_mode.value if self.active_mode else None,
            "duration_seconds": duration,
            "closing_message": "You did well. Take this calm with you."
        }
        
        self.active_mode = None
        self.session_start = None
        
        return result
    
    def get_crisis_response(self) -> Dict[str, Any]:
        """
        Immediate crisis response — for panic/meltdown moments.
        Ultra-simple. Ultra-safe. No complexity.
        """
        return {
            "mode": "crisis_anchor",
            "immediate_actions": [
                {"type": "voice", "text": "I'm here. You're not alone."},
                {"type": "pause", "duration": 2.0},
                {"type": "voice", "text": "Let's just breathe together."},
                {"type": "breath_cue", "inhale": 4.0, "exhale": 6.0},
                {"type": "voice", "text": "You are safe in this moment."},
                {"type": "pause", "duration": 3.0},
                {"type": "voice", "text": "Nothing needs to happen right now except this breath."}
            ],
            "sonic_bed": {
                "preset": "crisis_safe",
                "volume": 0.3,
                "warmth": 1.0,
                "no_sudden_changes": True
            },
            "reminder": "The computer can wait. You matter more than any machine."
        }

# ═══════════════════════════════════════════════════════════════════════════════
# AUTISM-AWARE FEATURES
# ═══════════════════════════════════════════════════════════════════════════════

AUTISM_AWARE_DESIGN = """
SANCTUARY: AUTISM-AWARE DESIGN PRINCIPLES

Based on research showing:
• Many autistic people have equal or stronger musical processing skills
• Rhythm/music can support sensory and motor regulation
• Predictable rhythm helps organize sensory input and movement
• Safe, controllable sound lets the brain "practice" regulation

KEY DESIGN CHOICES:

1. PREDICTABILITY
   - No sudden changes in volume, tempo, or texture
   - Transitions are always slow and telegraphed
   - User controls everything — nothing happens by surprise

2. PERSONALIZATION
   - Some autistic folks LOVE sound and ASMR
   - Some are sound-sensitive and need almost-silent, super-gentle audio
   - We ask, we remember, we respect

3. SAFE SOUND
   - Controllable (user sets volume, texture, voice)
   - Predictable (no random changes)
   - Inviting (warm, not harsh)

4. RHYTHM AS STRENGTH
   - Use rhythm to support regulation, not demand it
   - Breathing cues are invitations, not commands
   - "If you'd like" not "You must"

5. RESPECT FOR AUTONOMY
   - Autistic people aren't broken — we're not "fixing" anyone
   - We're offering a tool that some nervous systems find helpful
   - Take it or leave it, no judgment
"""

# ═══════════════════════════════════════════════════════════════════════════════
# INSTANTIATE SANCTUARY ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

SANCTUARY_ENGINE = SanctuaryEngine()

