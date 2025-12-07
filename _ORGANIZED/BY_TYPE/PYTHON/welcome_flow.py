# ROB OS - WELCOME FLOW
# ======================
# The complete first-time experience for new users
# From arrival to first session

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum

class WelcomeStep(Enum):
    ARRIVAL = "arrival"
    EMOTIONAL_CHECK = "emotional_check"
    SANCTUARY_SETUP = "sanctuary_setup"
    DEVICE_INTAKE = "device_intake"
    READBACK = "readback"
    SESSION_TYPE = "session_type"
    CONFIRMATION = "confirmation"
    SESSION_START = "session_start"

@dataclass
class WelcomeScreen:
    """A single screen in the welcome flow."""
    step: WelcomeStep
    title: str
    content: str
    voice_script: Optional[str]
    voice_mode: str  # "guide", "sanctuary", "spark"
    options: List[Dict[str, Any]]
    world: Optional[str]
    next_step: Optional[WelcomeStep]

class WelcomeFlow:
    """
    The complete welcome flow for new NOIZYLAB users.
    """
    
    def __init__(self):
        self.screens = self._build_screens()
        self.current_step = WelcomeStep.ARRIVAL
        self.user_choices: Dict[str, Any] = {}
    
    def _build_screens(self) -> Dict[WelcomeStep, WelcomeScreen]:
        return {
            WelcomeStep.ARRIVAL: WelcomeScreen(
                step=WelcomeStep.ARRIVAL,
                title="Welcome to NOIZYLAB",
                content="This is the place where broken computers and overwhelmed humans both come to calm down and figure out the next step.",
                voice_script="""Hey. I'm Rob.

You found NOIZYLAB.

This is the place where broken computers and overwhelmed humans 
both come to calm down and figure out the next step.

You're not late. You're not a problem.
You're just here. And that's enough to start.""",
                voice_mode="sanctuary",
                options=[
                    {"id": "need_help", "label": "I need help, I'm stressed", "emoji": "😰"},
                    {"id": "curious", "label": "I'm curious, show me around", "emoji": "🔍"}
                ],
                world="fish_forest",
                next_step=WelcomeStep.EMOTIONAL_CHECK
            ),
            
            WelcomeStep.EMOTIONAL_CHECK: WelcomeScreen(
                step=WelcomeStep.EMOTIONAL_CHECK,
                title="How are you doing right now?",
                content="No wrong answer. This just helps me pick a starting point for you.",
                voice_script="Before we look at any tech, tell me: how are you doing right now?",
                voice_mode="sanctuary",
                options=[
                    {"id": "okay", "label": "Pretty okay, just want to relax", "emoji": "😌", "state": "chill"},
                    {"id": "stressed", "label": "Stressed / Overwhelmed", "emoji": "😣", "state": "stressed"},
                    {"id": "panic", "label": "Meltdown / Panic", "emoji": "🧨", "state": "crisis"},
                    {"id": "tired", "label": "Tired / Burned out", "emoji": "🥱", "state": "burned_out"},
                    {"id": "focus", "label": "Need to focus", "emoji": "🧠", "state": "focus"}
                ],
                world=None,  # Keeps current
                next_step=WelcomeStep.SANCTUARY_SETUP
            ),
            
            WelcomeStep.SANCTUARY_SETUP: WelcomeScreen(
                step=WelcomeStep.SANCTUARY_SETUP,
                title="Where do you want to be for a bit?",
                content="Pick a sound world. You can change this anytime.",
                voice_script="Let's pick a place to be while we talk. Where sounds good to you?",
                voice_mode="sanctuary",
                options=[
                    {"id": "fish_forest", "label": "Fish Forest", "description": "Warm summer trees, gentle leaves, soft birds.", "emoji": "🌲"},
                    {"id": "rain_on_the_roof", "label": "Rain on the Roof", "description": "Safe inside, rain outside, piano in the other room.", "emoji": "🌧️"},
                    {"id": "mc96_midnight", "label": "MC96 Midnight", "description": "Quiet studio at 3am, gear humming, world asleep.", "emoji": "🌙"},
                    {"id": "silent_shore", "label": "Silent Shore", "description": "Almost no sound. Just enough to feel the room.", "emoji": "🤫"},
                    {"id": "soft_tide", "label": "Soft Tide", "description": "Floating ambient cloud, nothing sharp or sudden.", "emoji": "🌊"}
                ],
                world=None,  # User picks
                next_step=WelcomeStep.DEVICE_INTAKE
            ),
            
            WelcomeStep.DEVICE_INTAKE: WelcomeScreen(
                step=WelcomeStep.DEVICE_INTAKE,
                title="Tell me about your device",
                content="Just the basics. We'll dig deeper together.",
                voice_script="Alright. Let's talk about what's going on with your machine. Just the basics for now.",
                voice_mode="guide",
                options=[
                    {"id": "device_type", "type": "select", "label": "What kind of device?", 
                     "choices": ["Laptop", "Desktop", "Phone/Tablet", "Something else"]},
                    {"id": "os", "type": "select", "label": "What system?",
                     "choices": ["Mac", "Windows", "Not sure"]},
                    {"id": "problem", "type": "text", "label": "In your own words, what's it doing?",
                     "placeholder": "It's slow, it crashes, it won't start..."},
                    {"id": "critical_data", "type": "toggle", "label": "Is there anything on it you absolutely can't lose?"}
                ],
                world=None,
                next_step=WelcomeStep.READBACK
            ),
            
            WelcomeStep.READBACK: WelcomeScreen(
                step=WelcomeStep.READBACK,
                title="Here's what I'm hearing",
                content="Let me make sure I understand before we go further.",
                voice_script="""Here's what I'm hearing:

[Device summary]
[Symptom summary]
[Critical data: yes/no]

That sounds like it could be [likely issue] with [risk level] to your files.
I'm not 100% sure yet, but that's our starting point.""",
                voice_mode="guide",
                options=[
                    {"id": "correct", "label": "That's right", "emoji": "✅"},
                    {"id": "adjust", "label": "Let me clarify something", "emoji": "✏️"}
                ],
                world=None,
                next_step=WelcomeStep.SESSION_TYPE
            ),
            
            WelcomeStep.SESSION_TYPE: WelcomeScreen(
                step=WelcomeStep.SESSION_TYPE,
                title="What kind of session?",
                content="Pick what feels right. We can always adjust.",
                voice_script="Based on what you've told me, here are your options. What feels right?",
                voice_mode="guide",
                options=[
                    {"id": "espresso", "label": "☕ Espresso Tune-Up", 
                     "description": "Quick, safe clean & check. 30-45 min."},
                    {"id": "deep_dive", "label": "🛠 Deep Dive Repair", 
                     "description": "Thorough investigation and fixes. 2-3 hours."},
                    {"id": "data_rescue", "label": "🧯 Data-First Rescue", 
                     "description": "Protect your files above all else."},
                    {"id": "recommend", "label": "🤔 Recommend for me", 
                     "description": "I'll suggest based on what you told me."}
                ],
                world=None,
                next_step=WelcomeStep.CONFIRMATION
            ),
            
            WelcomeStep.CONFIRMATION: WelcomeScreen(
                step=WelcomeStep.CONFIRMATION,
                title="Before we start",
                content="Here's what we'll do and what we won't do without asking.",
                voice_script="""Here's what we're going to do in this session:

[Session plan]

Here's what we won't do without asking you:
- Wipe drives
- Reinstall the OS
- Run anything that could risk your files

Ready when you are.""",
                voice_mode="guide",
                options=[
                    {"id": "start", "label": "Start Session", "emoji": "▶️", "primary": True},
                    {"id": "wait", "label": "I need a minute", "emoji": "⏸️"}
                ],
                world=None,
                next_step=WelcomeStep.SESSION_START
            ),
            
            WelcomeStep.SESSION_START: WelcomeScreen(
                step=WelcomeStep.SESSION_START,
                title="Session Active",
                content="We're working together now. I've got you.",
                voice_script="Alright, we're in. Let's take care of this together.",
                voice_mode="guide",
                options=[],
                world=None,
                next_step=None
            )
        }
    
    def get_current_screen(self) -> WelcomeScreen:
        return self.screens[self.current_step]
    
    def advance(self, choice: Dict[str, Any]) -> WelcomeScreen:
        """
        Record choice and advance to next screen.
        """
        self.user_choices[self.current_step.value] = choice
        
        current = self.screens[self.current_step]
        if current.next_step:
            self.current_step = current.next_step
        
        return self.get_current_screen()
    
    def go_back(self) -> WelcomeScreen:
        """
        Go back to previous screen.
        """
        steps = list(WelcomeStep)
        current_idx = steps.index(self.current_step)
        if current_idx > 0:
            self.current_step = steps[current_idx - 1]
        return self.get_current_screen()
    
    def get_crisis_flow(self) -> Dict[str, Any]:
        """
        Get the crisis-specific flow for panicking users.
        """
        return {
            "immediate_world": "rain_on_the_roof",
            "voice_mode": "sanctuary",
            "first_message": """I hear you. This sounds really hard right now.

Before we touch anything on the computer,
let's just take one breath together.""",
            "breath_sequence": {
                "duration": 20,
                "script": [
                    "Breathe in slowly...",
                    "Hold gently...",
                    "And let it go...",
                    "That's it. You're here."
                ]
            },
            "after_breath": """Okay. Now let's take this one tiny step at a time.
Nothing we do in the next few minutes will make anything worse.
I promise.""",
            "simplified_intake": True,
            "max_questions": 3
        }
    
    def get_tour_flow(self) -> Dict[str, Any]:
        """
        Get the tour flow for curious users.
        """
        return {
            "world": "mc96_midnight",
            "voice_mode": "guide",
            "intro": """Nice. I'll give you the quick tour.

NOIZYLAB has three big pieces:

Sanctuary – where we calm your nerves.
Worlds – where we build sound and scenes out of my old FishMusic and SFX.
MC96 – where we actually look after your machines.

You can use one, two, or all three.
You're in charge.""",
            "tour_stops": [
                {"name": "Sanctuary", "description": "Sound-powered calm for your nervous system."},
                {"name": "Worlds", "description": "10 handcrafted soundscapes from 40 years of audio."},
                {"name": "MC96 Mission Control", "description": "Your devices, their health, all in one place."}
            ]
        }


# Singleton instance
_welcome_flow = None

def get_welcome_flow() -> WelcomeFlow:
    global _welcome_flow
    if _welcome_flow is None:
        _welcome_flow = WelcomeFlow()
    return _welcome_flow

