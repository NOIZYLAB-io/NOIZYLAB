"""
═══════════════════════════════════════════════════════════════════════════════
                         CALM BY DESIGN
═══════════════════════════════════════════════════════════════════════════════

NOIZYLAB never accidentally stresses people out.

Hard rules:
• No blinking red unless data loss is IMMEDIATE
• Every scary message paired with a calm plan
• Always supportive, never shaming

"You're not stupid for not knowing this; this is literally my job."
"""

from typing import Dict, List, Optional
from enum import Enum


class ToneMode(Enum):
    """Communication tone modes"""
    STANDARD = "standard"
    KIDS = "kids"
    ELDER = "elder"
    CRISIS = "crisis"
    CELEBRATION = "celebration"


class AlertLevel(Enum):
    """Alert severity levels"""
    INFO = "info"              # 💡 Blue - Just information
    SUCCESS = "success"        # ✅ Green - Good news
    NOTICE = "notice"          # 📝 Yellow - Worth knowing
    CAUTION = "caution"        # ⚠️ Amber - Be careful
    WARNING = "warning"        # 🔶 Orange - Take action
    CRITICAL = "critical"      # 🔴 Red - Immediate attention


# ═══════════════════════════════════════════════════════════════════════════════
# CALM LANGUAGE RULES
# ═══════════════════════════════════════════════════════════════════════════════

CALM_RULES = {
    "never_say": [
        "You should have",
        "Why didn't you",
        "That was a mistake",
        "You broke it",
        "This is your fault",
        "Obviously",
        "Everyone knows",
        "It's simple",
        "Just do",
        "You need to understand"
    ],
    
    "always_pair_scary_with_calm": True,
    
    "red_only_when": [
        "Immediate data loss risk",
        "Active security threat",
        "Hardware failure in progress",
        "Time-critical action needed"
    ],
    
    "supportive_phrases": [
        "You're not stupid for not knowing this; this is literally my job.",
        "This happens more often than you'd think.",
        "You did the right thing by asking for help.",
        "Let's figure this out together.",
        "I've seen this before — it's fixable.",
        "Take your time. There's no rush here.",
        "Good question. Here's what's happening...",
        "You're handling this well.",
        "This isn't as bad as it might feel right now."
    ]
}


# ═══════════════════════════════════════════════════════════════════════════════
# TONE TRANSLATIONS
# ═══════════════════════════════════════════════════════════════════════════════

def translate_to_kids(message: str) -> str:
    """Translate message to kid-friendly language"""
    
    translations = {
        "malware": "some sneaky bad software",
        "virus": "a computer bug",
        "crashed": "got confused and needed a rest",
        "failed": "had a little trouble",
        "error": "got a bit mixed up",
        "corrupted": "got a bit scrambled",
        "dead": "very tired",
        "dying": "getting sleepy",
        "broken": "not feeling well",
        "slow": "tired and sluggish",
        "overheating": "too warm and needs to cool down",
        "backup": "making a copy to keep safe",
        "delete": "put away",
        "warning": "heads up",
        "critical": "important",
        "disk": "the part that remembers things",
        "RAM": "the thinking part",
        "CPU": "the brain",
        "reboot": "take a nap and wake up fresh",
        "reinstall": "learn everything again from scratch"
    }
    
    result = message
    for tech, friendly in translations.items():
        result = result.replace(tech, friendly)
        result = result.replace(tech.capitalize(), friendly.capitalize())
    
    return result


def translate_to_elder(message: str) -> str:
    """Translate message to elder-friendly language"""
    
    # Remove jargon, add reassurance
    clarifications = {
        "backup": "backup (a safety copy of your files)",
        "cloud": "cloud (files stored safely on the internet)",
        "browser": "browser (the program you use to go on the internet)",
        "download": "download (copy from the internet to your computer)",
        "upload": "upload (copy from your computer to the internet)",
        "restart": "restart (turn off and turn on again)",
        "update": "update (get the latest improvements)",
        "settings": "settings (the options to control how things work)",
        "icon": "icon (the small picture you click on)",
        "click": "click (press the button on your mouse once)",
        "double-click": "double-click (press the mouse button twice quickly)",
        "right-click": "right-click (press the RIGHT button on your mouse)"
    }
    
    result = message
    for tech, clear in clarifications.items():
        if tech in result.lower() and clear not in result:
            result = result.replace(tech, clear)
    
    return result


# ═══════════════════════════════════════════════════════════════════════════════
# ALERT FORMATTING
# ═══════════════════════════════════════════════════════════════════════════════

def format_alert(level: AlertLevel, message: str, calm_plan: str = None) -> Dict:
    """Format an alert with appropriate styling and calm plan"""
    
    icons = {
        AlertLevel.INFO: "💡",
        AlertLevel.SUCCESS: "✅",
        AlertLevel.NOTICE: "📝",
        AlertLevel.CAUTION: "⚠️",
        AlertLevel.WARNING: "🔶",
        AlertLevel.CRITICAL: "🔴"
    }
    
    colors = {
        AlertLevel.INFO: "#3B82F6",      # Blue
        AlertLevel.SUCCESS: "#10B981",    # Green
        AlertLevel.NOTICE: "#F59E0B",     # Yellow
        AlertLevel.CAUTION: "#F97316",    # Amber
        AlertLevel.WARNING: "#EA580C",    # Orange
        AlertLevel.CRITICAL: "#DC2626"    # Red
    }
    
    # CRITICAL alerts MUST have a calm plan
    if level == AlertLevel.CRITICAL and not calm_plan:
        calm_plan = "We'll work through this together. Here's what to do next..."
    
    alert = {
        "level": level.value,
        "icon": icons[level],
        "color": colors[level],
        "message": message,
        "calm_plan": calm_plan,
        "show_breathing_room": level in [AlertLevel.WARNING, AlertLevel.CRITICAL]
    }
    
    # Add supportive phrase for scary alerts
    if level in [AlertLevel.CAUTION, AlertLevel.WARNING, AlertLevel.CRITICAL]:
        import random
        alert["supportive"] = random.choice(CALM_RULES["supportive_phrases"])
    
    return alert


# ═══════════════════════════════════════════════════════════════════════════════
# KIDS MODE MESSAGES
# ═══════════════════════════════════════════════════════════════════════════════

KIDS_MODE = {
    "welcome": "Hi there! I'm here to help your computer feel better. 🌟",
    
    "scanning": "I'm taking a look at your computer... like a doctor's checkup! 🩺",
    
    "found_problem": "I found something that's making your computer feel a bit sick. Don't worry — we can fix it!",
    
    "fixing": "I'm helping your computer feel better now. This might take a few minutes... ⏳",
    
    "done": "All done! Your computer should be feeling much better now. Great job being patient! 🎉",
    
    "needs_help": "This is a tricky one! We might need a grown-up's help with this part.",
    
    "restart_needed": "Your computer needs to take a little nap and wake up fresh. Can you help restart it?",
    
    "backup_reminder": "Let's make a copy of your important stuff — like making a backup of your favorite toy, just in case!",
    
    "goodbye": "You did great! Your computer says thank you. 💙"
}


# ═══════════════════════════════════════════════════════════════════════════════
# ELDER MODE MESSAGES
# ═══════════════════════════════════════════════════════════════════════════════

ELDER_MODE = {
    "welcome": """
Hello! I'm here to help you with your computer.

I'll explain everything clearly, step by step.
You can't break anything by clicking here — I'll always warn you first if something is risky.

Take your time. There's no rush.
    """.strip(),
    
    "before_action": """
Before we do this, let me explain what will happen:
{explanation}

This will NOT delete your photos or documents.
Would you like to continue?
    """.strip(),
    
    "step_by_step": """
Let's do this together, one step at a time:

Step {number}: {instruction}

Take your time. Let me know when you're ready for the next step.
    """.strip(),
    
    "reassurance": """
You're doing great. This is exactly right.

If you ever feel unsure, just ask me to explain again.
There's no such thing as a silly question.
    """.strip(),
    
    "completion": """
All done! Here's what we accomplished:
{summary}

Your computer is working well now.
If you have any questions later, I'm always here to help.
    """.strip()
}


# ═══════════════════════════════════════════════════════════════════════════════
# CRISIS MODE MESSAGES
# ═══════════════════════════════════════════════════════════════════════════════

CRISIS_MODE = {
    "opening": """
I hear you. This is stressful, and I'm here to help.

First, let's make sure we don't make anything worse.
Then we'll figure out the best path forward together.
    """.strip(),
    
    "stabilizing": """
Good. We're stabilizing the situation.

Right now, the most important thing is: {priority}

Don't worry about anything else yet.
    """.strip(),
    
    "options_intro": """
Okay, here's where we stand:

I'm going to give you three clear options.
No pressure — just information so you can decide what's right for you.
    """.strip(),
    
    "honest_assessment": """
I want to be honest with you:

{assessment}

That said, here's what we CAN do...
    """.strip(),
    
    "closing": """
You handled this really well.

Whatever you decide, you're making an informed choice.
That's the best anyone can do.

I'm here if you need anything else.
    """.strip()
}


# ═══════════════════════════════════════════════════════════════════════════════
# MESSAGE GENERATOR
# ═══════════════════════════════════════════════════════════════════════════════

class CalmMessenger:
    """Generates calm, supportive messages"""
    
    def __init__(self):
        self.mode = ToneMode.STANDARD
    
    def set_mode(self, mode: ToneMode):
        """Set the communication mode"""
        self.mode = mode
    
    def say(self, message: str, **kwargs) -> str:
        """Say something in the appropriate tone"""
        
        if self.mode == ToneMode.KIDS:
            message = translate_to_kids(message)
        elif self.mode == ToneMode.ELDER:
            message = translate_to_elder(message)
        
        # Fill in any placeholders
        for key, value in kwargs.items():
            message = message.replace(f"{{{key}}}", str(value))
        
        return message
    
    def alert(self, level: AlertLevel, message: str, calm_plan: str = None) -> Dict:
        """Create an alert"""
        
        if self.mode == ToneMode.KIDS:
            message = translate_to_kids(message)
            if calm_plan:
                calm_plan = translate_to_kids(calm_plan)
        elif self.mode == ToneMode.ELDER:
            message = translate_to_elder(message)
            if calm_plan:
                calm_plan = translate_to_elder(calm_plan)
        
        return format_alert(level, message, calm_plan)
    
    def supportive(self) -> str:
        """Get a random supportive phrase"""
        import random
        phrase = random.choice(CALM_RULES["supportive_phrases"])
        
        if self.mode == ToneMode.KIDS:
            phrase = translate_to_kids(phrase)
        
        return phrase
    
    def get_template(self, template_name: str) -> str:
        """Get a template for the current mode"""
        
        if self.mode == ToneMode.KIDS and template_name in KIDS_MODE:
            return KIDS_MODE[template_name]
        elif self.mode == ToneMode.ELDER and template_name in ELDER_MODE:
            return ELDER_MODE[template_name]
        elif self.mode == ToneMode.CRISIS and template_name in CRISIS_MODE:
            return CRISIS_MODE[template_name]
        
        return ""


# Singleton
calm = CalmMessenger()

