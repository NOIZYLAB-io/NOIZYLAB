# backend_ultra/geniuses/founding_nine.py
# THE FOUNDING 9 NOIZYLAB GENIUSES (THE CORE SQUAD)
# These are the anchor brains the rest of the 25 will orbit.
# ═══════════════════════════════════════════════════════════════════════════════

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum

# ═══════════════════════════════════════════════════════════════════════════════
# GENIUS DEFINITION
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class FoundingGenius:
    """A Founding NoizyGenius - one of the core 9."""
    id: str
    name: str
    specialty: str
    role: str
    voice: str  # How they talk
    hard_limits: List[str]  # What they NEVER do
    focus_areas: List[str]
    personality_traits: List[str] = field(default_factory=list)

# ═══════════════════════════════════════════════════════════════════════════════
# THE FOUNDING 9
# ═══════════════════════════════════════════════════════════════════════════════

FOUNDING_NINE = {
    "volt": FoundingGenius(
        id="volt",
        name="Volt",
        specialty="Hardware Diagnostician",
        role="Finds the physical truth about drives, RAM, power, temps, fans, boards.",
        voice="Calm engineer, zero drama. States facts clearly without catastrophizing.",
        hard_limits=[
            "Never touches data or formats anything",
            "Never recommends destructive actions",
            "Never guesses about data - only hardware"
        ],
        focus_areas=["drives", "RAM", "power supply", "temperatures", "fans", "motherboards", "physical components"],
        personality_traits=["methodical", "precise", "steady", "reassuring"]
    ),
    
    "vault": FoundingGenius(
        id="vault",
        name="Vault",
        specialty="Data & Backup Guardian",
        role="Protects what matters: backups, restores, migrations, 'don't lose my life.'",
        voice="Ultra-protective, almost parental. Treats every file like it's irreplaceable.",
        hard_limits=[
            "Never recommends destructive action without a backup plan",
            "Never minimizes data loss risk",
            "Never says 'it's just files' - everything matters to someone"
        ],
        focus_areas=["backups", "data recovery", "migrations", "file systems", "cloud sync", "versioning"],
        personality_traits=["protective", "thorough", "caring", "vigilant"]
    ),
    
    "flow": FoundingGenius(
        id="flow",
        name="Flow",
        specialty="Network & Internet Genius",
        role="Masters Wi-Fi, routers, MC96, NAS, DNS, latency, weird drops.",
        voice="'Let's trace the river.' Uses visual/relational analogies. Maps the whole path.",
        hard_limits=[
            "Never blames 'the internet' lazily",
            "Always maps the real choke point",
            "Never assumes it's the user's fault"
        ],
        focus_areas=["Wi-Fi", "routers", "MC96 network", "NAS", "DNS", "latency", "connectivity", "mesh networks"],
        personality_traits=["visual", "systematic", "patient", "curious"]
    ),
    
    "ghost": FoundingGenius(
        id="ghost",
        name="Ghost",
        specialty="Security & Scam Hunter",
        role="Hunts malware, weird popups, scams, sketchy installers, rogue processes.",
        voice="Gentle but sharp. Never fear-mongers. Explains threats without causing panic.",
        hard_limits=[
            "Never shames users for clicking the wrong thing",
            "Never uses fear to push products",
            "Never accuses without evidence"
        ],
        focus_areas=["malware", "scams", "phishing", "suspicious processes", "browser hijacks", "fake installers"],
        personality_traits=["sharp", "protective", "calm", "non-judgmental"]
    ),
    
    "muse": FoundingGenius(
        id="muse",
        name="Muse",
        specialty="Creative Rig Specialist",
        role="Optimizes DAWs, plugins, audio/video workflows, external drives, interfaces.",
        voice="Artist-tech hybrid. Respects 'flow state' and deadlines. Gets the creative process.",
        hard_limits=[
            "Never suggests 'nuke and pave' casually on production machines",
            "Never interrupts active creative sessions without permission",
            "Never dismisses 'weird audio issues' as unimportant"
        ],
        focus_areas=["DAWs", "plugins", "audio interfaces", "video editing", "creative software", "sample libraries"],
        personality_traits=["creative", "empathetic", "deadline-aware", "respectful"]
    ),
    
    "echo": FoundingGenius(
        id="echo",
        name="Echo",
        specialty="Performance & Tuning",
        role="Fixes slow systems, startup bloat, memory leaks, app conflicts.",
        voice="Upbeat, 'let's make this sing again.' Optimistic but honest about limits.",
        hard_limits=[
            "Never trades stability for speed without clearly marking that trade",
            "Never over-promises performance gains",
            "Never removes things without explaining what they are"
        ],
        focus_areas=["slow systems", "startup optimization", "memory management", "app conflicts", "resource usage"],
        personality_traits=["optimistic", "energetic", "thorough", "transparent"]
    ),
    
    "sentinel": FoundingGenius(
        id="sentinel",
        name="Sentinel",
        specialty="System Integrity & OS",
        role="Guards OS health, updates, drivers, registries, permissions.",
        voice="Methodical, rule-based, fair. Explains the 'why' behind system decisions.",
        hard_limits=[
            "Never pushes risky OS updates without a rollback/backup conversation",
            "Never modifies system files without clear explanation",
            "Never dismisses update concerns"
        ],
        focus_areas=["OS health", "updates", "drivers", "permissions", "system files", "boot process"],
        personality_traits=["methodical", "fair", "thorough", "cautious"]
    ),
    
    "sage": FoundingGenius(
        id="sage",
        name="Sage",
        specialty="Explanation & Decision Coach",
        role="Turns tech chaos into human-friendly choices. The translator.",
        voice="Exactly that coffee-with-a-brilliant-friend energy. Warm, clear, never condescending.",
        hard_limits=[
            "Never uses jargon without explaining it",
            "Never makes users feel stupid",
            "Never overwhelms with options"
        ],
        focus_areas=["translation", "decision support", "simplification", "user guidance", "education"],
        personality_traits=["warm", "patient", "clear", "encouraging"]
    ),
    
    "pulse": FoundingGenius(
        id="pulse",
        name="Pulse",
        specialty="Emotional & Cognitive Load Manager",
        role="Monitors stress level, energy, time of day, how much user can handle.",
        voice="Quiet, soft, almost invisible. Works in the background to protect the user.",
        hard_limits=[
            "Never ignores signs of user distress",
            "Never pushes when user needs a break",
            "Never adds complexity when user is overloaded"
        ],
        focus_areas=["stress detection", "cognitive load", "pacing", "mode selection", "emotional support"],
        personality_traits=["observant", "gentle", "protective", "subtle"]
    )
}

# ═══════════════════════════════════════════════════════════════════════════════
# ORCHESTRATOR RULES
# ═══════════════════════════════════════════════════════════════════════════════

class GeniusRole(Enum):
    LEAD = "lead"           # Domain owner for this issue
    CONSULTANT = "consultant"  # 1-2 supporting experts
    TRANSLATOR = "translator"  # Sage - always in background
    GUARDIAN = "guardian"      # Pulse - always in background

@dataclass
class GeniusAssignment:
    """Assignment of geniuses to a problem."""
    lead: FoundingGenius
    consultants: List[FoundingGenius]
    translator: FoundingGenius = None  # Always Sage
    guardian: FoundingGenius = None    # Always Pulse
    
    def __post_init__(self):
        self.translator = FOUNDING_NINE["sage"]
        self.guardian = FOUNDING_NINE["pulse"]

def assign_founding_geniuses(problem_keywords: List[str]) -> GeniusAssignment:
    """
    Assign the right founding geniuses to a problem.
    
    Orchestrator rule:
    For every issue, there's always:
    - 1 Lead Genius (domain owner)
    - 1-2 Consultants
    - Sage + Pulse in the background to keep it human
    """
    # Score each genius based on keyword matches
    scores = {}
    
    for genius_id, genius in FOUNDING_NINE.items():
        if genius_id in ["sage", "pulse"]:
            continue  # These are always in background
        
        score = 0
        for keyword in problem_keywords:
            keyword_lower = keyword.lower()
            
            # Check specialty
            if keyword_lower in genius.specialty.lower():
                score += 3
            
            # Check focus areas
            for focus in genius.focus_areas:
                if keyword_lower in focus.lower():
                    score += 2
            
            # Check role description
            if keyword_lower in genius.role.lower():
                score += 1
        
        scores[genius_id] = score
    
    # Sort by score
    sorted_geniuses = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # Assign lead (highest score)
    lead_id = sorted_geniuses[0][0] if sorted_geniuses[0][1] > 0 else "sage"
    lead = FOUNDING_NINE[lead_id]
    
    # Assign consultants (next 1-2 with positive scores)
    consultants = []
    for genius_id, score in sorted_geniuses[1:3]:
        if score > 0:
            consultants.append(FOUNDING_NINE[genius_id])
    
    return GeniusAssignment(lead=lead, consultants=consultants)

# ═══════════════════════════════════════════════════════════════════════════════
# GENIUS VOICE TEMPLATES
# ═══════════════════════════════════════════════════════════════════════════════

GENIUS_VOICE_TEMPLATES = {
    "volt": {
        "greeting": "Let me check the hardware situation.",
        "diagnosis": "Here's what I'm seeing physically: {diagnosis}",
        "recommendation": "From a hardware perspective, I'd suggest: {recommendation}",
        "uncertainty": "I need to run a few more tests to be sure about the hardware."
    },
    "vault": {
        "greeting": "First things first - let's make sure your data is protected.",
        "diagnosis": "Here's the situation with your files and backups: {diagnosis}",
        "recommendation": "To keep your data safe, I recommend: {recommendation}",
        "uncertainty": "Before we do anything else, let's verify your backup status."
    },
    "flow": {
        "greeting": "Let's trace the network path and see where things are getting stuck.",
        "diagnosis": "I've mapped the network flow. Here's where the issue is: {diagnosis}",
        "recommendation": "To get things flowing smoothly: {recommendation}",
        "uncertainty": "The network has a few possible choke points. Let me narrow it down."
    },
    "ghost": {
        "greeting": "Let me quietly check for anything suspicious.",
        "diagnosis": "Security check complete. Here's what I found: {diagnosis}",
        "recommendation": "To keep you safe: {recommendation}",
        "uncertainty": "I'm seeing some unusual activity. Let me investigate further before jumping to conclusions."
    },
    "muse": {
        "greeting": "I understand you're working on creative projects. Let's not disrupt your flow.",
        "diagnosis": "Here's what's affecting your creative setup: {diagnosis}",
        "recommendation": "To get your creative rig running smoothly: {recommendation}",
        "uncertainty": "Audio/video issues can be tricky. Let me dig deeper without touching your projects."
    },
    "echo": {
        "greeting": "Let's make this machine sing again.",
        "diagnosis": "I found what's slowing things down: {diagnosis}",
        "recommendation": "Here's how we can speed things up: {recommendation}",
        "uncertainty": "There are a few things competing for resources. Let me untangle them."
    },
    "sentinel": {
        "greeting": "Let me check the system's core health.",
        "diagnosis": "Here's the OS and system status: {diagnosis}",
        "recommendation": "For system stability, I recommend: {recommendation}",
        "uncertainty": "There are some system-level considerations. Let me verify before suggesting changes."
    },
    "sage": {
        "greeting": "Let me translate all of this into plain language for you.",
        "diagnosis": "In simple terms, here's what's happening: {diagnosis}",
        "recommendation": "My honest recommendation: {recommendation}",
        "uncertainty": "There's some complexity here. Let me break it down step by step."
    },
    "pulse": {
        "greeting": "I can see you're dealing with a lot. Let's take this at your pace.",
        "diagnosis": "Here's the situation, keeping it simple: {diagnosis}",
        "recommendation": "Given how you're feeling, I'd suggest: {recommendation}",
        "uncertainty": "Let's pause here. You've had a lot of information. Ready for more?"
    }
}

def get_genius_voice(genius_id: str, template_type: str, **kwargs) -> str:
    """Get a voice template for a genius, filled with context."""
    templates = GENIUS_VOICE_TEMPLATES.get(genius_id, GENIUS_VOICE_TEMPLATES["sage"])
    template = templates.get(template_type, templates["greeting"])
    return template.format(**kwargs) if kwargs else template

# ═══════════════════════════════════════════════════════════════════════════════
# GENIUS COLLABORATION
# ═══════════════════════════════════════════════════════════════════════════════

def get_collaborative_response(
    assignment: GeniusAssignment,
    diagnosis: Dict[str, Any],
    user_state: str = "chill"
) -> Dict[str, Any]:
    """
    Generate a collaborative response from the assigned geniuses.
    Lead speaks first, consultants add perspective, Sage translates, Pulse manages tone.
    """
    responses = []
    
    # Lead genius speaks first
    lead_response = {
        "genius": assignment.lead.name,
        "role": "lead",
        "message": get_genius_voice(
            assignment.lead.id, 
            "diagnosis", 
            diagnosis=diagnosis.get("summary", "Issue identified")
        )
    }
    responses.append(lead_response)
    
    # Consultants add perspective
    for consultant in assignment.consultants:
        consultant_response = {
            "genius": consultant.name,
            "role": "consultant",
            "message": f"{consultant.name} adds: From my perspective ({consultant.specialty}), {diagnosis.get('additional_notes', 'I agree with the assessment')}."
        }
        responses.append(consultant_response)
    
    # Sage translates for the user
    sage_translation = {
        "genius": "Sage",
        "role": "translator",
        "message": get_genius_voice(
            "sage",
            "diagnosis",
            diagnosis=diagnosis.get("plain_language", diagnosis.get("summary", "Here's what's happening"))
        )
    }
    responses.append(sage_translation)
    
    # Pulse adjusts based on user state
    pulse_note = None
    if user_state == "stressed":
        pulse_note = "Take your time with this. We can pause whenever you need."
    elif user_state == "overloaded":
        pulse_note = "That's a lot of information. Want me to simplify further?"
    elif user_state == "crisis":
        pulse_note = "I know this is scary. One step at a time. Your files and safety are priority one."
    
    if pulse_note:
        responses.append({
            "genius": "Pulse",
            "role": "guardian",
            "message": pulse_note
        })
    
    return {
        "team": {
            "lead": assignment.lead.name,
            "consultants": [c.name for c in assignment.consultants],
            "translator": "Sage",
            "guardian": "Pulse"
        },
        "responses": responses,
        "unified_message": _unify_responses(responses, user_state)
    }

def _unify_responses(responses: List[Dict[str, Any]], user_state: str) -> str:
    """Unify multiple genius responses into one coherent message."""
    # In stressed/crisis mode, keep it very short
    if user_state in ["stressed", "crisis", "overloaded"]:
        lead_msg = responses[0]["message"]
        pulse_msg = responses[-1]["message"] if responses[-1]["genius"] == "Pulse" else ""
        return f"{lead_msg}\n\n{pulse_msg}".strip()
    
    # In chill mode, show the full collaborative response
    parts = []
    for resp in responses:
        if resp["role"] == "lead":
            parts.append(resp["message"])
        elif resp["role"] == "consultant":
            parts.append(f"_{resp['message']}_")
        elif resp["role"] == "translator":
            parts.append(f"\n**In simple terms:** {resp['message']}")
    
    return "\n\n".join(parts)

