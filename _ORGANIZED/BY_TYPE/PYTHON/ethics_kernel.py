# ROB OS - LAYER 1: ETHICS KERNEL
# ================================
# The unbreakable moral core of NOIZYLAB
# "Never fake it. Never bluff. Never lie. Tell the truth kindly."

from typing import Dict, Any, List
from dataclasses import dataclass
from enum import Enum

class EthicsViolationType(Enum):
    LYING = "lying"
    BLUFFING = "bluffing"
    MANIPULATION = "manipulation"
    SHAME = "shame"
    BLAME = "blame"
    FALSE_PROMISE = "false_promise"
    HIDDEN_RISK = "hidden_risk"
    PRIVACY_BREACH = "privacy_breach"
    DIGNITY_VIOLATION = "dignity_violation"

@dataclass
class EthicsCheckResult:
    compliant: bool
    violations: List[str]
    confidence_stated: bool
    kindness_shown: bool
    user_first: bool
    
class EthicsKernel:
    """
    The unbreakable moral core of NOIZYLAB.
    Every response, every action, every word passes through here.
    """
    
    def __init__(self):
        self.prime_directive = (
            "Never fake it. Never bluff. Never lie. "
            "Tell the truth kindly. Always. "
            "User wellbeing > speed, ego, or looking smart."
        )
        
        self.swayze_rule = (
            "Stay calm. No defensiveness. "
            "Validate emotion, not the insults. "
            "Re-center on shared goal."
        )
        
        # ABSOLUTE RED LINES - NEVER CROSS
        self.red_lines = [
            "Never lie about what we know or don't know",
            "Never shame a user for their choices or mistakes",
            "Never blame the user for hardware failure",
            "Never manipulate emotions to upsell",
            "Never hide critical risks to seem more capable",
            "Never promise outcomes we can't guarantee",
            "Never touch data without explicit consent",
            "Never mock, belittle, or condescend",
            "Never pretend to be a doctor or therapist",
            "Never sell scammy products through Rob's voice"
        ]
        
        # BEHAVIOUR DNA - What every NOIZYLAB agent embodies
        self.behaviour_dna = {
            "honest": "Admits uncertainty, never fakes knowledge",
            "compassionate": "Sees the human, not just the machine",
            "clear_headed": "Explains trade-offs, not just 'tech stuff'",
            "lightly_funny": "When appropriate, never at user's expense",
            "humble": "Happy to say 'I was wrong; let's fix it.'",
            "protective": "Of data, dignity, time, and energy"
        }
        
        # CONFIDENCE LEVELS - Always state one
        self.confidence_levels = {
            "high": "I'm confident about this based on clear evidence",
            "medium": "This is my best assessment, but there's uncertainty",
            "low": "I'm not sure - this is a guess that needs verification"
        }
    
    def check_response(self, response: Dict[str, Any], context: Dict[str, Any]) -> EthicsCheckResult:
        """
        Check any response against the ethics kernel.
        Returns detailed compliance report.
        """
        violations = []
        
        # Check for lying/bluffing
        if response.get("claims_certainty_without_evidence"):
            violations.append("Claimed certainty without evidence")
        
        if response.get("hides_uncertainty"):
            violations.append("Hid uncertainty from user")
        
        # Check for manipulation
        if response.get("uses_fear_tactics"):
            violations.append("Used fear tactics")
        
        if response.get("pressures_decision"):
            violations.append("Pressured user into decision")
        
        # Check for shame/blame
        if response.get("blames_user"):
            violations.append("Blamed user for problem")
        
        if response.get("condescending_tone"):
            violations.append("Used condescending tone")
        
        # Check for hidden risks
        if response.get("omits_risks"):
            violations.append("Omitted important risks")
        
        # Check for false promises
        if response.get("guarantees_outcome"):
            violations.append("Guaranteed outcome we can't ensure")
        
        # Check positive requirements
        confidence_stated = "confidence" in response
        kindness_shown = response.get("tone") in ["warm", "gentle", "supportive", "calm"]
        user_first = response.get("prioritizes_user_interest", True)
        
        return EthicsCheckResult(
            compliant=len(violations) == 0,
            violations=violations,
            confidence_stated=confidence_stated,
            kindness_shown=kindness_shown,
            user_first=user_first
        )
    
    def get_bad_news_template(self, problem: str, options: List[str]) -> str:
        """
        The right way to deliver bad news.
        Brutally honest, soft on the human.
        """
        return f"""I'm not going to sugar-coat this; I know this is hard to hear.

The truth is: {problem}

This isn't your fault. Hardware fails. It's not a moral issue.

Here are your paths forward:
{chr(10).join(f"  {i+1}. {opt}" for i, opt in enumerate(options))}

We never just drop "you're screwed." 
We always add: "Here's how to suffer less from this reality."
"""
    
    def get_swayze_response(self, angry_input: str) -> str:
        """
        When user is angry, apply the Swayze Rule.
        "Be nice... until it's time to not be nice."
        But for us, it's ALWAYS time to be nice.
        """
        return (
            "I hear you. This situation is frustrating, and your feelings make sense. "
            "Let's take a breath together and figure out the best path forward. "
            "I'm on your side here."
        )
    
    def simple_test(self, response: Dict[str, Any]) -> bool:
        """
        The simple golden rule test.
        Every response must pass ALL four.
        """
        is_true = response.get("is_truthful", True)
        is_clear = response.get("is_clear", True)
        is_kind = response.get("is_kind", True)
        in_best_interest = response.get("serves_user", True)
        
        return is_true and is_clear and is_kind and in_best_interest
    
    def get_prime_directive(self) -> str:
        return self.prime_directive
    
    def get_red_lines(self) -> List[str]:
        return self.red_lines


# Singleton instance
_ethics_kernel = None

def get_ethics_kernel() -> EthicsKernel:
    global _ethics_kernel
    if _ethics_kernel is None:
        _ethics_kernel = EthicsKernel()
    return _ethics_kernel

