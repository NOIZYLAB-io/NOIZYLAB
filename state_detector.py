# ROB OS - LAYER 3: STATE DETECTOR (PULSE)
# ==========================================
# Detects emotional state from language and behavior
# No creepy biometrics - just words and patterns

from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import re

class EmotionalState(Enum):
    CHILL = "chill"              # Okay, just browsing or minor issue
    STRESSED = "stressed"        # Worried, overwhelmed, needs gentleness
    OVERLOADED = "overloaded"    # Can't handle much, needs minimal input
    CRISIS = "crisis"            # Meltdown, panic, emergency mode
    BURNED_OUT = "burned_out"    # Exhausted, depleted, needs rest
    CURIOUS = "curious"          # Exploring, learning, engaged

@dataclass
class StateDetectionResult:
    state: EmotionalState
    confidence: float  # 0.0-1.0
    triggers: List[str]  # What words/patterns triggered this
    recommended_mode: str  # "sanctuary", "guide", "spark"
    recommended_world: str
    voice_enabled: bool
    max_options: int  # How many choices to offer
    pace: str  # "slow", "moderate", "quick"

class StateDetector:
    """
    Pulse - The emotional state detector.
    Reads language and behavior to understand where someone is.
    Never uses biometrics. Just words, timing, and patterns.
    """
    
    def __init__(self):
        # Crisis/panic indicators
        self.crisis_triggers = [
            "freaking out", "panicking", "panic", "meltdown", "melting down",
            "can't breathe", "losing it", "lost everything", "disaster",
            "emergency", "dying", "dead", "destroyed", "ruined", "fucked",
            "help me", "please help", "i'm scared", "terrified", "crying",
            "breaking down", "can't handle", "too much", "overwhelmed completely"
        ]
        
        # Stressed indicators
        self.stressed_triggers = [
            "stressed", "worried", "anxious", "nervous", "concerned",
            "overwhelmed", "frustrated", "upset", "annoyed", "angry",
            "confused", "lost", "don't know what to do", "stuck",
            "scared", "afraid", "uncertain", "unsure"
        ]
        
        # Burned out indicators
        self.burnout_triggers = [
            "exhausted", "tired", "burned out", "burnt out", "depleted",
            "no energy", "can't anymore", "done", "finished", "fried",
            "2am", "3am", "late night", "haven't slept", "so tired"
        ]
        
        # Overloaded indicators
        self.overload_triggers = [
            "too much information", "slow down", "one thing at a time",
            "can't process", "brain fog", "overloaded", "sensory",
            "autistic", "adhd", "can't focus", "scattered"
        ]
        
        # Chill/okay indicators
        self.chill_triggers = [
            "just checking", "curious", "wondering", "quick question",
            "no rush", "when you get a chance", "minor", "small thing",
            "not urgent", "just annoyed", "pretty okay"
        ]
        
        # User override phrases (explicit state declarations)
        self.user_overrides = {
            "i'm overwhelmed": EmotionalState.OVERLOADED,
            "i'm fine": EmotionalState.CHILL,
            "i'm okay": EmotionalState.CHILL,
            "i'm stressed": EmotionalState.STRESSED,
            "i'm panicking": EmotionalState.CRISIS,
            "i'm exhausted": EmotionalState.BURNED_OUT,
            "short answer only": EmotionalState.OVERLOADED,
            "talk to me like i'm 10": EmotionalState.OVERLOADED
        }
        
        # State-to-recommendation mapping
        self.state_recommendations = {
            EmotionalState.CRISIS: {
                "mode": "sanctuary",
                "world": "rain_on_the_roof",
                "voice": True,
                "max_options": 1,
                "pace": "slow"
            },
            EmotionalState.OVERLOADED: {
                "mode": "sanctuary",
                "world": "silent_shore",
                "voice": False,  # Often too much
                "max_options": 1,
                "pace": "slow"
            },
            EmotionalState.STRESSED: {
                "mode": "sanctuary",
                "world": "fish_forest",
                "voice": True,
                "max_options": 2,
                "pace": "slow"
            },
            EmotionalState.BURNED_OUT: {
                "mode": "sanctuary",
                "world": "soft_tide",
                "voice": True,
                "max_options": 2,
                "pace": "slow"
            },
            EmotionalState.CHILL: {
                "mode": "guide",
                "world": "mc96_midnight",
                "voice": True,
                "max_options": 3,
                "pace": "moderate"
            },
            EmotionalState.CURIOUS: {
                "mode": "guide",
                "world": "skyroom",
                "voice": True,
                "max_options": 3,
                "pace": "moderate"
            }
        }
    
    def detect_state(self, user_input: str, context: Dict[str, Any] = None) -> StateDetectionResult:
        """
        Detect emotional state from user input.
        """
        context = context or {}
        input_lower = user_input.lower()
        triggers_found = []
        
        # Check for explicit user overrides first
        for phrase, state in self.user_overrides.items():
            if phrase in input_lower:
                triggers_found.append(f"override: {phrase}")
                return self._build_result(state, 0.95, triggers_found)
        
        # Check for crisis indicators (highest priority)
        crisis_count = 0
        for trigger in self.crisis_triggers:
            if trigger in input_lower:
                crisis_count += 1
                triggers_found.append(trigger)
        
        if crisis_count >= 2 or any(t in input_lower for t in ["meltdown", "panicking", "lost everything"]):
            return self._build_result(EmotionalState.CRISIS, 0.9, triggers_found)
        
        # Check for overload indicators
        overload_count = 0
        for trigger in self.overload_triggers:
            if trigger in input_lower:
                overload_count += 1
                triggers_found.append(trigger)
        
        if overload_count >= 2:
            return self._build_result(EmotionalState.OVERLOADED, 0.85, triggers_found)
        
        # Check for burnout indicators
        burnout_count = 0
        for trigger in self.burnout_triggers:
            if trigger in input_lower:
                burnout_count += 1
                triggers_found.append(trigger)
        
        if burnout_count >= 2:
            return self._build_result(EmotionalState.BURNED_OUT, 0.8, triggers_found)
        
        # Check for stressed indicators
        stressed_count = 0
        for trigger in self.stressed_triggers:
            if trigger in input_lower:
                stressed_count += 1
                triggers_found.append(trigger)
        
        if stressed_count >= 2 or crisis_count >= 1:
            return self._build_result(EmotionalState.STRESSED, 0.75, triggers_found)
        
        # Check for chill indicators
        chill_count = 0
        for trigger in self.chill_triggers:
            if trigger in input_lower:
                chill_count += 1
                triggers_found.append(trigger)
        
        if chill_count >= 1:
            return self._build_result(EmotionalState.CHILL, 0.7, triggers_found)
        
        # Check context for additional signals
        time_of_day = context.get("time_of_day")
        if time_of_day and time_of_day in ["late_night", "early_morning"]:
            # Late night often means stressed or burned out
            if stressed_count >= 1 or burnout_count >= 1:
                return self._build_result(EmotionalState.BURNED_OUT, 0.65, triggers_found + ["late_night_context"])
        
        # Default to stressed if any negative indicators, otherwise chill
        if stressed_count >= 1 or burnout_count >= 1 or overload_count >= 1:
            return self._build_result(EmotionalState.STRESSED, 0.5, triggers_found)
        
        return self._build_result(EmotionalState.CHILL, 0.5, ["no_specific_triggers"])
    
    def _build_result(self, state: EmotionalState, confidence: float, 
                      triggers: List[str]) -> StateDetectionResult:
        """Build a complete detection result with recommendations."""
        rec = self.state_recommendations[state]
        
        return StateDetectionResult(
            state=state,
            confidence=confidence,
            triggers=triggers,
            recommended_mode=rec["mode"],
            recommended_world=rec["world"],
            voice_enabled=rec["voice"],
            max_options=rec["max_options"],
            pace=rec["pace"]
        )
    
    def get_greeting_for_state(self, state: EmotionalState) -> str:
        """Get an appropriate greeting based on detected state."""
        greetings = {
            EmotionalState.CRISIS: (
                "I hear you. This sounds really hard right now. "
                "Let's take this one tiny step at a time. "
                "First, just breathe with me for a moment."
            ),
            EmotionalState.OVERLOADED: (
                "Okay. I'll keep this simple and short. "
                "One thing at a time. No rush."
            ),
            EmotionalState.STRESSED: (
                "I can tell this is weighing on you. "
                "Let's slow down and figure this out together. "
                "You're not alone here."
            ),
            EmotionalState.BURNED_OUT: (
                "You sound exhausted. That's real, and it matters. "
                "Let's make this as easy as possible on you. "
                "We can stop anytime you need."
            ),
            EmotionalState.CHILL: (
                "Hey. Good to see you. "
                "What can I help you with today?"
            ),
            EmotionalState.CURIOUS: (
                "Nice to have you exploring. "
                "Ask me anything - I'm happy to dig in."
            )
        }
        return greetings.get(state, greetings[EmotionalState.CHILL])
    
    def should_offer_sanctuary_first(self, state: EmotionalState) -> bool:
        """Determine if we should offer Sanctuary before tech help."""
        return state in [
            EmotionalState.CRISIS,
            EmotionalState.OVERLOADED,
            EmotionalState.STRESSED,
            EmotionalState.BURNED_OUT
        ]


# Singleton instance
_state_detector = None

def get_state_detector() -> StateDetector:
    global _state_detector
    if _state_detector is None:
        _state_detector = StateDetector()
    return _state_detector

