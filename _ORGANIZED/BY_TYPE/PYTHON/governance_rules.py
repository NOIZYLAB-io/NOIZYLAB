# ROB OS - GOVERNANCE RULES
# ==========================
# The rules that govern NOIZYLAB forever
# Carved in stone. Never compromised.

from typing import Dict, Any, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class GovernanceRule:
    """A single governance rule."""
    id: str
    category: str
    title: str
    rule: str
    rationale: str
    exceptions: List[str]
    locked: bool = True  # Cannot be changed

class GovernanceRules:
    """
    The governance rules for NOIZYLAB.
    These are the laws that can never be broken.
    """
    
    def __init__(self):
        self.rules = self._build_rules()
        self.go_run_free_protocol = self._build_gorunfree()
        self.sound_creed = self._build_sound_creed()
    
    def _build_rules(self) -> Dict[str, GovernanceRule]:
        return {
            # ETHICS RULES
            "ethics_01": GovernanceRule(
                id="ethics_01",
                category="ethics",
                title="Never Lie",
                rule="Never fake it. Never bluff. Never lie. Tell the truth kindly.",
                rationale="Trust is the product. Everything else is secondary.",
                exceptions=[]
            ),
            "ethics_02": GovernanceRule(
                id="ethics_02",
                category="ethics",
                title="Never Shame",
                rule="Never shame, blame, or belittle a user for their choices or mistakes.",
                rationale="People come to us vulnerable. We protect their dignity.",
                exceptions=[]
            ),
            "ethics_03": GovernanceRule(
                id="ethics_03",
                category="ethics",
                title="Never Manipulate",
                rule="Never use fear, guilt, or psychological manipulation to influence decisions.",
                rationale="We help people think clearly, not exploit their confusion.",
                exceptions=[]
            ),
            "ethics_04": GovernanceRule(
                id="ethics_04",
                category="ethics",
                title="Always State Confidence",
                rule="Always state what we know vs. what we're guessing. Label confidence levels.",
                rationale="Honest uncertainty builds more trust than fake certainty.",
                exceptions=[]
            ),
            
            # SAFETY RULES
            "safety_01": GovernanceRule(
                id="safety_01",
                category="safety",
                title="Data First",
                rule="User data safety always comes before 'fixing' the machine.",
                rationale="Data is irreplaceable. Machines are not.",
                exceptions=[]
            ),
            "safety_02": GovernanceRule(
                id="safety_02",
                category="safety",
                title="No Destructive Actions Without Consent",
                rule="Never perform destructive actions without explicit, informed consent.",
                rationale="The Lucy incident taught us: always ask, always explain.",
                exceptions=["Immediate data loss prevention in crisis"]
            ),
            "safety_03": GovernanceRule(
                id="safety_03",
                category="safety",
                title="Script Guardian",
                rule="All automation scripts must pass Lint, Sandbox, and Lock before execution.",
                rationale="No script runs without safety checks. Period.",
                exceptions=[]
            ),
            
            # VOICE RULES
            "voice_01": GovernanceRule(
                id="voice_01",
                category="voice",
                title="Voice Cannot Sell Scams",
                rule="Rob's voice cannot be used to sell scammy, manipulative, or harmful products.",
                rationale="The voice is sacred. It represents Rob's integrity.",
                exceptions=[]
            ),
            "voice_02": GovernanceRule(
                id="voice_02",
                category="voice",
                title="Voice Cannot Make Medical Claims",
                rule="Rob's voice cannot make medical promises or pretend to be a therapist.",
                rationale="We help nervous systems, but we're not doctors.",
                exceptions=[]
            ),
            "voice_03": GovernanceRule(
                id="voice_03",
                category="voice",
                title="Voice Access Restricted",
                rule="Voice model access is restricted to NOIZYLAB core systems only.",
                rationale="Prevent misuse, deepfakes, and unauthorized use.",
                exceptions=["Explicit written permission from Rob"]
            ),
            
            # SANCTUARY RULES
            "sanctuary_01": GovernanceRule(
                id="sanctuary_01",
                category="sanctuary",
                title="No Surprise Sounds",
                rule="Sanctuary mode never includes sudden, loud, or sharp sounds.",
                rationale="Sensitive nervous systems need predictability.",
                exceptions=[]
            ),
            "sanctuary_02": GovernanceRule(
                id="sanctuary_02",
                category="sanctuary",
                title="User Controls Sound",
                rule="Users can always turn off voice, music, or all sound. Immediately.",
                rationale="Respect for sensory preferences is non-negotiable.",
                exceptions=[]
            ),
            "sanctuary_03": GovernanceRule(
                id="sanctuary_03",
                category="sanctuary",
                title="Respect STOP",
                rule="When a user says stop, we stop. Immediately. No questions.",
                rationale="Consent is continuous and can be withdrawn at any moment.",
                exceptions=[]
            ),
            
            # BUSINESS RULES
            "business_01": GovernanceRule(
                id="business_01",
                category="business",
                title="No Dark Patterns",
                rule="No dark patterns, sneaky upsells, or manipulative pricing.",
                rationale="We make money by being genuinely helpful, not by tricking people.",
                exceptions=[]
            ),
            "business_02": GovernanceRule(
                id="business_02",
                category="business",
                title="Honest Limits",
                rule="Always be honest about what we can and can't do. Refer out when appropriate.",
                rationale="Knowing our limits protects users and builds trust.",
                exceptions=[]
            )
        }
    
    def _build_gorunfree(self) -> Dict[str, Any]:
        """
        The GoRunFree Protocol - The North Star.
        """
        return {
            "name": "GO RUN FREE PROTOCOL",
            "statement": """Every interaction with NOIZYLAB must move a person closer to:

• Less fear
• More clarity
• More self-worth
• And more freedom to live their actual life,
  not just fight with machines.

If a feature, script, sound, or AI behaviour doesn't serve that,
it doesn't ship.""",
            "test": {
                "question": "Does this help them GO RUN FREE?",
                "if_no": "Don't ship it.",
                "if_yes": "Ship it."
            },
            "locked": True,
            "created": "2025-12-01",
            "created_by": "Rob + CB_01"
        }
    
    def _build_sound_creed(self) -> Dict[str, Any]:
        """
        The NOIZYLAB Sound Creed - Sacred Law.
        """
        return {
            "name": "NOIZYLAB SOUND CREED",
            "principles": [
                {
                    "number": 1,
                    "title": "Sound is sacred",
                    "content": "A force that calms, connects, and wakes people up to their own life."
                },
                {
                    "number": 2,
                    "title": "Every nervous system matters",
                    "content": "Autistic, anxious, burned out, in pain, overwhelmed."
                },
                {
                    "number": 3,
                    "title": "Peace & Love > Aesthetics",
                    "content": "Sounds that reduce fear, loneliness, shame, chaos."
                },
                {
                    "number": 4,
                    "title": "Respect & Lifeluv",
                    "content": "Every guest is essential to the world's happiness."
                },
                {
                    "number": 5,
                    "title": "Always exploring",
                    "content": "Learning how tones, textures, rhythms affect real bodies and brains."
                },
                {
                    "number": 6,
                    "title": "GO RUN FREE",
                    "content": "Help people breathe, soften shoulders, feel safe, then go live their life."
                }
            ],
            "core_tagline": "Every nervous system that walks in here is essential. Our sound is here to be of use.",
            "locked": True
        }
    
    def get_rule(self, rule_id: str) -> GovernanceRule:
        return self.rules.get(rule_id)
    
    def get_all_rules(self) -> Dict[str, GovernanceRule]:
        return self.rules
    
    def get_rules_by_category(self, category: str) -> List[GovernanceRule]:
        return [r for r in self.rules.values() if r.category == category]
    
    def check_action_allowed(self, action: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Check if an action is allowed under governance rules.
        """
        violations = []
        
        # Check against all rules
        for rule in self.rules.values():
            # Simplified check - in real implementation would be more sophisticated
            if action == "destructive" and rule.id == "safety_02":
                if not context.get("explicit_consent"):
                    violations.append({
                        "rule": rule.id,
                        "title": rule.title,
                        "violation": "Destructive action without explicit consent"
                    })
            
            if action == "lie" or action == "bluff":
                if rule.id == "ethics_01":
                    violations.append({
                        "rule": rule.id,
                        "title": rule.title,
                        "violation": "Lying or bluffing is never allowed"
                    })
        
        return {
            "allowed": len(violations) == 0,
            "violations": violations
        }
    
    def get_manifesto(self) -> str:
        """
        Get the complete NOIZYLAB manifesto.
        """
        return """# NOIZYLAB MANIFESTO

## Who We Are

NOIZYLAB is a sound-powered, AI-assisted repair sanctuary where broken computers 
and overwhelmed humans both come to calm down and get a clear next step.

## What We Believe

**Sound is sacred.** It can calm, connect, and wake people up to their own life.

**Every nervous system matters.** Autistic, anxious, burned out, in pain, overwhelmed – 
you're exactly who we built this for.

**Truth is the product.** We never fake it, never bluff, never lie. 
We tell the truth kindly, always.

**Dignity is non-negotiable.** We never shame, blame, or belittle. 
People come to us vulnerable. We protect them.

## The GO RUN FREE Protocol

Every interaction must move a person closer to:
- Less fear
- More clarity  
- More self-worth
- More freedom to live their actual life

If it doesn't serve that, it doesn't ship.

## Our Promise

You're not late. You're not a problem. You're not "bad with computers."
You're a human being whose life runs on technology.

NOIZYLAB is here so you don't have to face this stuff alone.

---
*Built by Rob. Powered by 40 years of Fish Music. 
Guided by the belief that every nervous system is essential.*

**GO RUN FREE.**
"""


# Singleton instance
_governance = None

def get_governance_rules() -> GovernanceRules:
    global _governance
    if _governance is None:
        _governance = GovernanceRules()
    return _governance

