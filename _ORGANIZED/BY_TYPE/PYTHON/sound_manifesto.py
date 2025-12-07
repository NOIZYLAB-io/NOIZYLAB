# backend_ultra/sanctuary/sound_manifesto.py
# NOIZYLAB SOUND MANIFESTO & DOCTRINE
# "Every nervous system that walks in here is essential. Our sound is here to be of use."
# ═══════════════════════════════════════════════════════════════════════════════
#
# UNTIL ROB'S LAST DAY, NOIZYLAB WILL KEEP LEARNING
# HOW SOUND CAN HELP HUMANS SUFFER LESS AND LOVE MORE.
#
# PEACE & LOVE, RESPECT & LIFELUV!!!
# ═══════════════════════════════════════════════════════════════════════════════

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum

# ═══════════════════════════════════════════════════════════════════════════════
# THE NOIZYLAB SOUND MANIFESTO (FINAL, DROP-IN)
# ═══════════════════════════════════════════════════════════════════════════════

SOUND_MANIFESTO = """
═══════════════════════════════════════════════════════════════════════════════
                    THE NOIZYLAB SOUND MANIFESTO
═══════════════════════════════════════════════════════════════════════════════

1. SOUND IS HOW WE SAY "YOU MATTER."
   Every tone, track, and breath cue is a way of telling you:
   You're alive. You're important. You're not alone in this.

2. WE DESIGN FOR NERVOUS SYSTEMS, NOT PLAYLISTS.
   We care how your chest feels, how your shoulders drop, how your pulse slows—
   more than we care about genre, fashion, or cool points.

3. AUTISM, ANXIETY, PAIN, BURNOUT: ALL WELCOME.
   Some people need silence. Some need rhythm. Some need a soft voice in their ear.
   We don't force one "healing sound" on everyone. We give you choices.

4. NOTHING FAKE, NOTHING PROMISED WE CAN'T KEEP.
   Sound can calm, comfort, focus, and soothe.
   It can't cure every illness or "fix" who you are.
   We use it as support, not as a lie.

5. RESPECT, ALWAYS.
   No shaming for meltdowns, shutdowns, overload, or "not coping well."
   You're not a problem to solve. You're a person to protect.

6. FLOW OVER FORCE.
   We don't shove you into "relax."
   We make space—slow tempos, gentle textures, kind words—
   and let your system arrive there at its own pace.

7. GO RUN FREE.
   The point isn't to keep you here forever.
   The point is to help you breathe, reset, remember your worth—
   and then go live your life with a lighter heart.

═══════════════════════════════════════════════════════════════════════════════

Until Rob's last day, NOIZYLAB will keep learning
how sound can help humans suffer less and love more.

PEACE & LOVE, RESPECT & LIFELUV!!!

═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# NOIZYLAB SOUND CREED (THE LAW)
# ═══════════════════════════════════════════════════════════════════════════════

SOUND_CREED = {
    "sound_is_sacred": {
        "statement": "Sound is sacred.",
        "meaning": "We treat sound as a force that can calm, connect, and wake people back up to their own life."
    },
    "every_nervous_system_matters": {
        "statement": "Every nervous system matters.",
        "meaning": "Autistic, anxious, burned out, in pain, overwhelmed—everyone is worth the effort to tune the world a little kinder for them."
    },
    "peace_and_love_over_aesthetics": {
        "statement": "Peace & Love > Aesthetics.",
        "meaning": "We don't just make cool sounds. We make sounds that reduce fear, loneliness, shame, and chaos."
    },
    "respect_and_lifeluv": {
        "statement": "Respect & Lifeluv.",
        "meaning": "No person is 'extra.' Every single guest is essential to the world's happiness and joy. We design audio that reminds them of that."
    },
    "always_exploring": {
        "statement": "Always exploring.",
        "meaning": "Until your last day: We keep learning how tones, textures, rhythms, voices affect real bodies and brains. We test, listen, refine—never pretending magic, always chasing real relief."
    },
    "go_run_free": {
        "statement": "GO RUN FREE.",
        "meaning": "The goal of every sound in NOIZYLAB: Help people breathe, soften their shoulders, feel safe enough to think again, and then go run free in their own life."
    }
}

CORE_TAGLINE = "Every nervous system that walks in here is essential. Our sound is here to be of use."

# ═══════════════════════════════════════════════════════════════════════════════
# SANCTUARY MODE MATRIX
# ═══════════════════════════════════════════════════════════════════════════════

class UserState(Enum):
    OVERLOADED = "overloaded"           # Autistic meltdown risk, sensory overwhelm
    ANXIOUS_IN_PAIN = "anxious_in_pain" # Anxious, in pain
    TIRED_BURNT_OUT = "tired_burnt_out" # Tired, burnt out
    CALM_CURIOUS = "calm_curious"       # Calm, curious

class SanctuaryGoal(Enum):
    DOWNSHIFT = "downshift"     # De-escalate
    STABILIZE = "stabilize"     # Stay regulated
    FOCUS = "focus"             # Gentle concentration
    CONNECT = "connect"         # Feel cared for

@dataclass
class SanctuaryModeV2:
    """A Sanctuary mode with full specification."""
    id: str
    name: str
    tagline: str
    for_who: List[str]
    sound_description: str
    options: List[str]
    goal: str
    ui_notes: str
    voice_enabled: bool = False
    asmr_available: bool = False
    consent_required: bool = False

SANCTUARY_MODES_V2 = {
    "silent_shore": SanctuaryModeV2(
        id="silent_shore",
        name="Silent Shore",
        tagline="Near-silence for sensitive systems",
        for_who=[
            "Sound-sensitive autistic users",
            "Migraine",
            "Sensory overload"
        ],
        sound_description="Near-silence, faint room tone only",
        options=["Room tone on/off", "Visual breathing indicator"],
        goal="Zero additional load",
        ui_notes="Soft visuals, simple breathing indicator, text prompts only",
        voice_enabled=False,
        asmr_available=False
    ),
    
    "soft_tide": SanctuaryModeV2(
        id="soft_tide",
        name="Soft Tide",
        tagline="Gentle ambient for nervous system downshift",
        for_who=[
            "General anxiety",
            "Pain",
            "Cognitive fatigue"
        ],
        sound_description="Slow ambient (≤60 BPM or free-time), minimal high-freq content",
        options=["Darker/warmer", "Brighter/airier", "Volume control"],
        goal="Nervous system downshift + gentle safety",
        ui_notes="Warm colors, slow visual movement, clear exit button",
        voice_enabled=False,
        asmr_available=False
    ),
    
    "rob_sanctuary": SanctuaryModeV2(
        id="rob_sanctuary",
        name="Rob Sanctuary",
        tagline="Voice + pad for when you're scared or overwhelmed",
        for_who=[
            "\"I'm scared / overwhelmed / melting\"",
            "Panic moments",
            "Need to feel held"
        ],
        sound_description="Ambient bed from Soft Tide + Rob // Sanctuary speaking few, slow lines",
        options=["Voice on/off", "Breath pacing", "Grounding prompts"],
        goal="Feel held + guided, not alone",
        ui_notes="Rob's voice is slow, warm, with generous pauses. Content: breath pacing, grounding, permission to pause.",
        voice_enabled=True,
        asmr_available=False
    ),
    
    "asmr_cove": SanctuaryModeV2(
        id="asmr_cove",
        name="ASMR Cove",
        tagline="Tingles and whispers (only if you like ASMR)",
        for_who=[
            "ASMR-responsive users who like tingles/whispers"
        ],
        sound_description="Quiet textures + optional Rob whisper",
        options=["Textures on/off", "Whisper voice on/off", "Intensity control"],
        goal="Deep personal comfort, but never forced",
        ui_notes="MASSIVE consent language: 'Only if you like ASMR. Some people find this uncomfortable. That's okay.'",
        voice_enabled=True,
        asmr_available=True,
        consent_required=True
    ),
    
    "steady_flow": SanctuaryModeV2(
        id="steady_flow",
        name="Steady Flow",
        tagline="Gentle focus for working, coding, creating",
        for_who=[
            "Working, coding, writing",
            "Therapy homework",
            "Need soft focus without hypnotizing"
        ],
        sound_description="Light, consistent, low-distractibility textures",
        options=["Texture type", "Occasional gentle reminders on/off"],
        goal="Soft channel toward flow without hypnotizing",
        ui_notes="Minimal voice; maybe occasional gentle reminders. Never intrusive.",
        voice_enabled=False,  # Minimal
        asmr_available=False
    )
}

def get_recommended_mode(user_state: UserState, goal: SanctuaryGoal) -> str:
    """Recommend a sanctuary mode based on user state and goal."""
    recommendations = {
        (UserState.OVERLOADED, SanctuaryGoal.DOWNSHIFT): "silent_shore",
        (UserState.OVERLOADED, SanctuaryGoal.STABILIZE): "silent_shore",
        (UserState.ANXIOUS_IN_PAIN, SanctuaryGoal.DOWNSHIFT): "soft_tide",
        (UserState.ANXIOUS_IN_PAIN, SanctuaryGoal.CONNECT): "rob_sanctuary",
        (UserState.TIRED_BURNT_OUT, SanctuaryGoal.STABILIZE): "soft_tide",
        (UserState.TIRED_BURNT_OUT, SanctuaryGoal.FOCUS): "steady_flow",
        (UserState.CALM_CURIOUS, SanctuaryGoal.FOCUS): "steady_flow",
        (UserState.CALM_CURIOUS, SanctuaryGoal.CONNECT): "rob_sanctuary"
    }
    return recommendations.get((user_state, goal), "soft_tide")

# ═══════════════════════════════════════════════════════════════════════════════
# ROB'S VOICE SYSTEM - FINAL SPEC
# ═══════════════════════════════════════════════════════════════════════════════

class RobVoicePersona(Enum):
    GUIDE = "guide"           # Explanations, walkthroughs, tech sessions
    SANCTUARY = "sanctuary"   # Stress, overload, autistic regulation, grief, fear
    SPARK = "spark"           # Intros, brand stingers, non-crisis hype

@dataclass
class RobVoiceConfig:
    """Configuration for a Rob voice persona."""
    persona: RobVoicePersona
    use_for: List[str]
    pace: str
    tone: str
    content_style: List[str]
    key_behaviours: List[str]
    never_use_in: List[str] = field(default_factory=list)

ROB_VOICE_PERSONAS = {
    RobVoicePersona.GUIDE: RobVoiceConfig(
        persona=RobVoicePersona.GUIDE,
        use_for=[
            "Explanations",
            "NOIZYLAB walkthroughs",
            "Tech sessions"
        ],
        pace="Normal, conversational",
        tone="Confident, friendly, straight-talking",
        content_style=[
            "\"Here's what's going on.\"",
            "\"Here's what I'd do if it were my machine.\"",
            "\"Here are your options.\""
        ],
        key_behaviours=[
            "Labels certainty: 'I'm pretty sure…' / 'I'm not sure yet…'",
            "No jargon without a quick translation",
            "Ends with one clear next step"
        ]
    ),
    
    RobVoicePersona.SANCTUARY: RobVoiceConfig(
        persona=RobVoicePersona.SANCTUARY,
        use_for=[
            "Stress",
            "Overload",
            "Autistic regulation",
            "Grief",
            "Fear"
        ],
        pace="Slow",
        tone="Warm, soft, never urgent. Generous pauses, let silence work.",
        content_style=[
            "\"You're not broken.\"",
            "\"This is a lot. It's okay.\"",
            "\"Let's just take one breath.\""
        ],
        key_behaviours=[
            "Generous pauses between sentences",
            "Let silence work",
            "Never rush",
            "Acknowledge feelings before offering solutions"
        ]
    ),
    
    RobVoicePersona.SPARK: RobVoiceConfig(
        persona=RobVoicePersona.SPARK,
        use_for=[
            "Intros",
            "Brand stingers",
            "Non-crisis hype",
            "Celebrating successful repairs",
            "Marketing"
        ],
        pace="Energetic, but not manic",
        tone="Fun, playful, 'Fish/Fuel Rob'",
        content_style=[
            "\"Let's go!\"",
            "\"That's what I'm talking about!\"",
            "\"NOIZYLAB, baby!\""
        ],
        key_behaviours=[
            "High energy but controlled",
            "Celebratory",
            "Never used in crisis or Sanctuary spaces"
        ],
        never_use_in=[
            "Crisis situations",
            "Sanctuary modes",
            "When user is stressed or overwhelmed",
            "Data rescue scenarios"
        ]
    )
}

# ═══════════════════════════════════════════════════════════════════════════════
# ROB // SANCTUARY MICRO-SCRIPTS
# ═══════════════════════════════════════════════════════════════════════════════

SANCTUARY_MICRO_SCRIPTS = {
    "breath": {
        "name": "NOIZY Breath",
        "duration": "20-40 seconds",
        "script": [
            "Hey. This is a lot. Let's take one slow breath together.",
            "",
            "Inhale… two… three…",
            "Hold… one… two…",
            "Exhale… two… three… four…",
            "",
            "There you go. You're doing enough right now."
        ]
    },
    
    "worth": {
        "name": "Worth Reminder",
        "duration": "15-25 seconds",
        "script": [
            "You are not a malfunction.",
            "You're a human being having a hard moment.",
            "That's allowed here."
        ]
    },
    
    "permission": {
        "name": "Permission",
        "duration": "10-20 seconds",
        "script": [
            "You don't have to solve your whole life in this minute.",
            "Just stay. Breathe.",
            "We'll pick one small next step together."
        ]
    },
    
    "grounding": {
        "name": "Grounding",
        "duration": "30-60 seconds",
        "script": [
            "Notice one thing you can see…",
            "One thing you can feel…",
            "One thing you can hear in this room besides me.",
            "",
            "You're here. You're alive. You matter more than this machine."
        ]
    },
    
    "crisis_anchor": {
        "name": "Crisis Anchor",
        "duration": "45-60 seconds",
        "script": [
            "I'm here. You're not alone.",
            "",
            "Let's just breathe together.",
            "Inhale… two… three… four…",
            "Exhale… two… three… four… five… six…",
            "",
            "You are safe in this moment.",
            "Nothing needs to happen right now except this breath.",
            "",
            "The computer can wait. You matter more than any machine."
        ]
    }
}

def get_sanctuary_script(script_id: str) -> Dict[str, Any]:
    """Get a sanctuary micro-script."""
    script = SANCTUARY_MICRO_SCRIPTS.get(script_id)
    if not script:
        return {"error": f"Script '{script_id}' not found"}
    return script

# ═══════════════════════════════════════════════════════════════════════════════
# GUARDRAILS (WHAT WE NEVER DO / ALWAYS DO)
# ═══════════════════════════════════════════════════════════════════════════════

HARD_NOS = [
    "No claiming sound 'cures autism'",
    "No claiming specific frequencies 'heal all disease'",
    "No forcing sound on people (especially autistic or sensory-sensitive guests)",
    "No surprise loud elements, stingers, notification pings in Sanctuary",
    "No using SPARK Rob in crisis or Sanctuary spaces",
    "No shaming for meltdowns, shutdowns, overload, or 'not coping well'",
    "No promising what sound cannot honestly deliver"
]

HARD_YESES = [
    "Always offer OFF / QUIET modes",
    "Always explain in plain text what a mode will feel like",
    "Always respect 'STOP' or 'TOO MUCH' immediately",
    "Always frame sound as: 'A tool to help your system'",
    "Always frame sound as: 'Something you can try'",
    "Always frame sound as: 'Not a replacement for medical or mental-health care'",
    "Always give users control over volume, texture, voice",
    "Always show clear exit buttons",
    "Always let users customize their sensory experience"
]

HONEST_BOUNDARIES = {
    "sound_can": [
        "Lower anxiety, heart rate, and subjective stress for many people",
        "Help autistic people with social engagement, emotional regulation, and sensory organization when used in structured, respectful ways",
        "Support pain management, sleep, focus, and recovery as a complement to real medical/psych care",
        "Provide a felt sense of care and safety",
        "Help people breathe, slow down, and feel less alone"
    ],
    "sound_cannot": [
        "Cure autism (and shouldn't try – autistic people aren't broken)",
        "Replace meds, surgery, or evidence-based therapy for serious disease",
        "Guarantee 'healing all ailments' with the right frequency",
        "Fix every problem",
        "Work the same for everyone"
    ]
}

def check_guardrails(action: Dict[str, Any]) -> Dict[str, Any]:
    """Check if an action violates any guardrails."""
    violations = []
    
    # Check for claims we can't make
    if action.get("claims_cure"):
        violations.append("VIOLATION: Cannot claim sound cures conditions")
    
    if action.get("forces_sound"):
        violations.append("VIOLATION: Cannot force sound on users")
    
    if action.get("surprise_loud"):
        violations.append("VIOLATION: No surprise loud elements in Sanctuary")
    
    if action.get("spark_in_crisis"):
        violations.append("VIOLATION: Cannot use SPARK Rob in crisis/Sanctuary")
    
    if action.get("no_exit_option"):
        violations.append("VIOLATION: Must always offer exit/quiet options")
    
    return {
        "compliant": len(violations) == 0,
        "violations": violations,
        "action": "APPROVED" if len(violations) == 0 else "BLOCKED"
    }

# ═══════════════════════════════════════════════════════════════════════════════
# AUDIO DESIGN RULES (FROM RESEARCH)
# ═══════════════════════════════════════════════════════════════════════════════

AUDIO_DESIGN_RULES = {
    "tempo_and_rhythm": {
        "target": "≤ 60 BPM or gentle non-metric ambient",
        "avoid": [
            "Heavy percussion",
            "Sudden rhythm changes",
            "Sharp syncopation"
        ],
        "rationale": "Slow tempo entrains heart rate and breathing toward rest state"
    },
    
    "dynamics_and_spectrum": {
        "avoid": [
            "Big jumps in volume",
            "Harsh high frequencies (spikes above ~5-6 kHz)",
            "Super-boomy bass that rattles sensory systems"
        ],
        "aim_for": [
            "Warm midrange (200 Hz - 2 kHz) for body comfort",
            "Gentle high shimmer (6-8 kHz) very low in level, if at all"
        ],
        "rationale": "Warm, smooth spectrum feels safe; harsh frequencies trigger alertness"
    },
    
    "binaural_tones": {
        "usage": "Optional layer, never the main feature",
        "implementation": [
            "Keep low in the mix",
            "Let users opt in/out easily",
            "Toggle: 'Extra hypnotic layer (binaural beats) – ON/OFF'"
        ],
        "rationale": "Modest anxiety reduction in some people, not magic"
    },
    
    "transitions": {
        "rule": "All transitions must be slow and smooth",
        "fade_time": "Minimum 3 seconds, prefer 5+ seconds",
        "rationale": "Sudden changes trigger startle response, especially in sensitive systems"
    },
    
    "personalization": {
        "required_controls": [
            "Volume",
            "'Brightness' of sound (more highs vs more muffled)",
            "Voice on/off",
            "ASMR textures on/off",
            "Binaural layer on/off"
        ],
        "rationale": "Some autistic folks love sound; some hate it. Personal control is king."
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# AUTISM-AWARE DESIGN PRINCIPLES
# ═══════════════════════════════════════════════════════════════════════════════

AUTISM_AWARE_PRINCIPLES = {
    "predictability": {
        "rule": "No surprise popups, notifications, or sound effects",
        "implementation": "Always show: 'You're in [Mode Name]. This will sound like [short description].'",
        "rationale": "Predictability reduces cognitive load and anxiety"
    },
    
    "respect_differences": {
        "rule": "Make it explicit that autistic people are not all the same",
        "implementation": "Text: 'Some autistic people love sound; some hate it. You get to choose what your nervous system tastes like here.'",
        "rationale": "Autonomy and respect for individual differences"
    },
    
    "control_panel": {
        "required_elements": [
            "Volume slider",
            "'Brightness' slider (more highs vs more muffled)",
            "Voice toggle",
            "ASMR textures toggle",
            "Binaural layer toggle"
        ],
        "rationale": "Maximum user control over sensory input"
    },
    
    "not_fixing": {
        "rule": "We are not 'fixing' autistic people",
        "framing": "We're offering a tool that some nervous systems find helpful. Take it or leave it, no judgment.",
        "rationale": "Autistic people aren't broken"
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# EXPORT FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def get_manifesto() -> str:
    """Get the full sound manifesto."""
    return SOUND_MANIFESTO

def get_creed() -> Dict[str, Any]:
    """Get the sound creed."""
    return SOUND_CREED

def get_tagline() -> str:
    """Get the core tagline."""
    return CORE_TAGLINE

def get_all_modes() -> Dict[str, SanctuaryModeV2]:
    """Get all sanctuary modes."""
    return SANCTUARY_MODES_V2

def get_voice_personas() -> Dict[RobVoicePersona, RobVoiceConfig]:
    """Get all Rob voice personas."""
    return ROB_VOICE_PERSONAS

def get_guardrails() -> Dict[str, List[str]]:
    """Get all guardrails."""
    return {
        "hard_nos": HARD_NOS,
        "hard_yeses": HARD_YESES,
        "honest_boundaries": HONEST_BOUNDARIES
    }

def get_audio_rules() -> Dict[str, Any]:
    """Get audio design rules."""
    return AUDIO_DESIGN_RULES

def get_autism_principles() -> Dict[str, Any]:
    """Get autism-aware design principles."""
    return AUTISM_AWARE_PRINCIPLES

