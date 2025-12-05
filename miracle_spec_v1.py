# backend_ultra/miracle/miracle_spec_v1.py
# NOIZYLAB: MIRACLE SPEC V1.0
# THE "THIS IS HOW IT MUST BEHAVE" HANDBOOK
# ═══════════════════════════════════════════════════════════════════════════════

from typing import Dict, Any, List, Optional
from enum import Enum
from dataclasses import dataclass, field
import time
import json

# ═══════════════════════════════════════════════════════════════════════════════
# NON-NEGOTIABLE PILLARS (Every agent. Every screen. Every answer.)
# ═══════════════════════════════════════════════════════════════════════════════

class Pillar(Enum):
    TRUTH = "truth"       # Never fake, never bluff, never overstate
    CARE = "care"         # Always on the user's side, emotionally and practically
    SAFETY = "safety"     # Data and sanity before speed and cleverness
    SIMPLICITY = "simplicity"  # Miraculously simple experience, no chaos

PILLARS = [Pillar.TRUTH, Pillar.CARE, Pillar.SAFETY, Pillar.SIMPLICITY]

def check_pillar_violation(response: Dict[str, Any]) -> List[str]:
    """If anything violates a pillar → it's wrong, full stop."""
    violations = []
    if response.get("fakes_or_bluffs"):
        violations.append("PILLAR VIOLATION: TRUTH - Faked or bluffed")
    if response.get("ignores_user_emotions"):
        violations.append("PILLAR VIOLATION: CARE - Ignored user's emotional state")
    if response.get("risks_data_for_speed"):
        violations.append("PILLAR VIOLATION: SAFETY - Risked data for speed")
    if response.get("creates_chaos"):
        violations.append("PILLAR VIOLATION: SIMPLICITY - Created unnecessary complexity")
    return violations

# ═══════════════════════════════════════════════════════════════════════════════
# THE 3-BRAIN CORE ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════════

class DiagBrain:
    """
    BRAIN 1 - DIAG BRAIN: Fixes the tech
    Symptom → hypotheses → tests → conclusion → confidence
    Always: "What I think, why I think it, how sure I am."
    """
    
    def __init__(self):
        self.current_hypotheses = []
        self.tests_run = []
        self.conclusion = None
        self.confidence = 0.0
    
    def analyze(self, symptoms: List[str], system_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate hypotheses from symptoms."""
        hypotheses = []
        
        # Pattern matching for common issues
        symptom_text = " ".join(symptoms).lower()
        
        if "clicking" in symptom_text and "not booting" in symptom_text:
            hypotheses.append({
                "cause": "Mechanical hard drive failure",
                "confidence": 0.85,
                "severity": "critical",
                "data_risk": "high"
            })
        
        if "slow" in symptom_text and "boot" in symptom_text:
            hypotheses.append({
                "cause": "Too many startup items",
                "confidence": 0.7,
                "severity": "low",
                "data_risk": "none"
            })
            hypotheses.append({
                "cause": "Old HDD (not SSD)",
                "confidence": 0.6,
                "severity": "medium",
                "data_risk": "low"
            })
        
        if "fans" in symptom_text and ("loud" in symptom_text or "100%" in symptom_text):
            hypotheses.append({
                "cause": "High CPU load from background processes",
                "confidence": 0.65,
                "severity": "low",
                "data_risk": "none"
            })
            hypotheses.append({
                "cause": "Thermal paste degradation",
                "confidence": 0.4,
                "severity": "medium",
                "data_risk": "none"
            })
        
        self.current_hypotheses = sorted(hypotheses, key=lambda x: x["confidence"], reverse=True)
        return {
            "hypotheses": self.current_hypotheses,
            "top_suspect": self.current_hypotheses[0] if self.current_hypotheses else None,
            "tests_recommended": self._recommend_tests()
        }
    
    def _recommend_tests(self) -> List[str]:
        """Recommend tests based on hypotheses."""
        tests = []
        for h in self.current_hypotheses:
            if "hard drive" in h["cause"].lower():
                tests.append("SMART disk health check")
                tests.append("Listen for clicking/grinding sounds")
            if "startup" in h["cause"].lower():
                tests.append("Audit startup items")
            if "CPU" in h["cause"]:
                tests.append("Check Activity Monitor / Task Manager")
        return list(set(tests))
    
    def form_conclusion(self, test_results: Dict[str, Any]) -> Dict[str, Any]:
        """Form conclusion from test results."""
        # Adjust confidence based on test results
        self.conclusion = {
            "diagnosis": self.current_hypotheses[0]["cause"] if self.current_hypotheses else "Unknown",
            "confidence": self.current_hypotheses[0]["confidence"] if self.current_hypotheses else 0.0,
            "reasoning": "Based on symptoms and test results",
            "data_risk": self.current_hypotheses[0].get("data_risk", "unknown") if self.current_hypotheses else "unknown"
        }
        return self.conclusion


class HumanBrain:
    """
    BRAIN 2 - HUMAN BRAIN: Cares for the person
    Detects: chill / stressed / overloaded / crisis
    Chooses tone, length, complexity, speed
    """
    
    class EmotionalState(Enum):
        CHILL = "chill"
        STRESSED = "stressed"
        OVERLOADED = "overloaded"
        CRISIS = "crisis"
    
    CRISIS_TRIGGERS = [
        "freaking out", "panic", "lost everything", "total panic",
        "i'm dying", "help me", "urgent", "emergency", "oh god",
        "i think i lost", "please help", "i'm scared"
    ]
    
    OVERLOAD_TRIGGERS = [
        "overwhelmed", "too much", "can't handle", "exhausted",
        "confused", "i don't understand", "this is too hard"
    ]
    
    STRESS_TRIGGERS = [
        "frustrated", "annoyed", "pissed", "angry", "done with this",
        "stupid", "hate this", "sick of"
    ]
    
    def __init__(self):
        self.current_state = self.EmotionalState.CHILL
        self.stress_level = 0.0
    
    def detect_state(self, user_input: str, session_context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Detect user's emotional state from input."""
        input_lower = user_input.lower()
        
        # Check for crisis first (highest priority)
        for trigger in self.CRISIS_TRIGGERS:
            if trigger in input_lower:
                self.current_state = self.EmotionalState.CRISIS
                self.stress_level = 1.0
                return self._get_state_config()
        
        # Check for overload
        for trigger in self.OVERLOAD_TRIGGERS:
            if trigger in input_lower:
                self.current_state = self.EmotionalState.OVERLOADED
                self.stress_level = 0.8
                return self._get_state_config()
        
        # Check for stress
        for trigger in self.STRESS_TRIGGERS:
            if trigger in input_lower:
                self.current_state = self.EmotionalState.STRESSED
                self.stress_level = 0.6
                return self._get_state_config()
        
        # Default to chill
        self.current_state = self.EmotionalState.CHILL
        self.stress_level = 0.2
        return self._get_state_config()
    
    def _get_state_config(self) -> Dict[str, Any]:
        """Get configuration for current emotional state."""
        configs = {
            self.EmotionalState.CHILL: {
                "state": "chill",
                "max_options": 3,
                "detail_level": "full",
                "humor_allowed": True,
                "reassurance_first": False,
                "sentence_length": "normal",
                "tone": "friendly_expert"
            },
            self.EmotionalState.STRESSED: {
                "state": "stressed",
                "max_options": 2,
                "detail_level": "moderate",
                "humor_allowed": False,
                "reassurance_first": True,
                "sentence_length": "shorter",
                "tone": "calm_supportive"
            },
            self.EmotionalState.OVERLOADED: {
                "state": "overloaded",
                "max_options": 1,
                "detail_level": "minimal",
                "humor_allowed": False,
                "reassurance_first": True,
                "sentence_length": "very_short",
                "tone": "gentle_guiding",
                "offer_pause": True
            },
            self.EmotionalState.CRISIS: {
                "state": "crisis",
                "max_options": 1,
                "detail_level": "essential_only",
                "humor_allowed": False,
                "reassurance_first": True,
                "sentence_length": "ultra_short",
                "tone": "calm_anchor",
                "crisis_mode": True,
                "repeat_safety_message": True
            }
        }
        return configs[self.current_state]


class StoryBrain:
    """
    BRAIN 3 - STORY BRAIN: Makes it make sense
    Outputs: One-line summary, Human metaphor, Optional nerd deep-dive
    """
    
    def __init__(self):
        pass
    
    def generate_summary(self, diagnosis: Dict[str, Any], detail_level: str = "full") -> Dict[str, Any]:
        """Generate human-readable summaries at different detail levels."""
        cause = diagnosis.get("diagnosis", "Unknown issue")
        confidence = diagnosis.get("confidence", 0.0)
        data_risk = diagnosis.get("data_risk", "unknown")
        
        # One-line summary (always generated)
        one_liner = self._generate_one_liner(cause, confidence, data_risk)
        
        # Simple metaphor
        metaphor = self._generate_metaphor(cause)
        
        # Technical breakdown (optional based on detail_level)
        technical = None
        if detail_level in ["full", "moderate"]:
            technical = self._generate_technical(diagnosis)
        
        return {
            "one_liner": one_liner,
            "metaphor": metaphor,
            "technical": technical,
            "confidence_statement": self._confidence_to_words(confidence)
        }
    
    def _generate_one_liner(self, cause: str, confidence: float, data_risk: str) -> str:
        """Generate a single-sentence summary."""
        risk_phrase = ""
        if data_risk == "high":
            risk_phrase = " Your data is at risk."
        elif data_risk == "medium":
            risk_phrase = " Some data risk exists."
        
        conf_phrase = "I'm fairly confident" if confidence > 0.7 else "I suspect"
        return f"{conf_phrase} the issue is: {cause}.{risk_phrase}"
    
    def _generate_metaphor(self, cause: str) -> str:
        """Generate a relatable metaphor for the technical issue."""
        metaphors = {
            "hard drive failure": "Think of your hard drive like an old record player. The needle is scratching the disc instead of reading it smoothly. We need to rescue the music before the disc gets too damaged.",
            "startup items": "Your laptop is like someone trying to carry 20 bags of groceries at once. We need to put some of those bags down so they can actually walk.",
            "HDD": "Your hard drive is like a librarian who has to physically walk to every book. An SSD is like having all the books instantly appear in your hands.",
            "CPU load": "Your computer is like a chef trying to cook 50 dishes at once. We need to close some of those orders so they can focus on what matters.",
            "thermal": "Your laptop is running hot, like a car engine that needs a coolant flush. The fans are working overtime to compensate."
        }
        
        cause_lower = cause.lower()
        for key, metaphor in metaphors.items():
            if key in cause_lower:
                return metaphor
        return "Think of it like a machine that's working harder than it should. We can help it work smarter."
    
    def _generate_technical(self, diagnosis: Dict[str, Any]) -> str:
        """Generate technical breakdown for those who want it."""
        return f"Technical analysis: {diagnosis.get('reasoning', 'Based on observed symptoms and diagnostic tests.')} Confidence level: {int(diagnosis.get('confidence', 0) * 100)}%."
    
    def _confidence_to_words(self, confidence: float) -> str:
        """Convert confidence score to human-readable statement."""
        if confidence >= 0.9:
            return "I'm highly confident about this."
        elif confidence >= 0.7:
            return "I'm reasonably confident, but there's some uncertainty."
        elif confidence >= 0.5:
            return "This is my best guess, but we should verify."
        else:
            return "I'm not very sure yet. We need more information."


# ═══════════════════════════════════════════════════════════════════════════════
# THE 25 GENIUSES ORCHESTRATOR
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Genius:
    """A single NoizyGenius specialist."""
    id: str
    name: str
    domain: str
    specialties: List[str]
    personality_traits: List[str] = field(default_factory=list)

class GeniusOrchestrator:
    """
    Orchestrates the 25 NoizyGeniuses.
    Picks a Lead Genius per issue.
    Assigns 1-2 Consultants.
    Shows disagreements + merged plan, never hides conflict.
    """
    
    GENIUSES = {
        "volt": Genius("volt", "Volt", "Hardware", ["motherboards", "power", "components", "physical repair"]),
        "vault": Genius("vault", "Vault", "Data & Backup", ["data recovery", "backup strategies", "file systems"]),
        "ghost": Genius("ghost", "Ghost", "Security", ["malware", "threats", "privacy", "encryption"]),
        "flow": Genius("flow", "Flow", "Network & Routing", ["wifi", "ethernet", "dns", "connectivity"]),
        "muse": Genius("muse", "Muse", "Creative Rigs", ["audio", "video", "DAWs", "creative software"]),
        "spark": Genius("spark", "Spark", "Performance", ["optimization", "speed", "resources", "tuning"]),
        "atlas": Genius("atlas", "Atlas", "Storage", ["drives", "SSDs", "NAS", "RAID"]),
        "echo": Genius("echo", "Echo", "OS & Software", ["operating systems", "drivers", "updates"]),
        "shield": Genius("shield", "Shield", "Defense", ["firewalls", "antivirus", "protection"]),
        "pulse": Genius("pulse", "Pulse", "Monitoring", ["health checks", "diagnostics", "logging"]),
        "bridge": Genius("bridge", "Bridge", "Connectivity", ["peripherals", "bluetooth", "USB"]),
        "core": Genius("core", "Core", "System", ["boot", "BIOS", "firmware", "kernel"]),
        "wave": Genius("wave", "Wave", "Audio", ["sound cards", "audio interfaces", "speakers"]),
        "pixel": Genius("pixel", "Pixel", "Display", ["monitors", "graphics", "resolution"]),
        "cloud": Genius("cloud", "Cloud", "Cloud Services", ["sync", "cloud storage", "remote"]),
        "mobile": Genius("mobile", "Mobile", "Mobile Devices", ["phones", "tablets", "iOS", "Android"]),
        "legacy": Genius("legacy", "Legacy", "Vintage Tech", ["old systems", "compatibility", "migration"]),
        "thermal": Genius("thermal", "Thermal", "Cooling", ["fans", "temps", "thermal paste"]),
        "power": Genius("power", "Power", "Power Systems", ["batteries", "charging", "PSU"]),
        "memory": Genius("memory", "Memory", "RAM & Memory", ["RAM", "virtual memory", "swap"]),
        "input": Genius("input", "Input", "Input Devices", ["keyboards", "mice", "trackpads"]),
        "print": Genius("print", "Print", "Printing", ["printers", "scanners", "imaging"]),
        "sync": Genius("sync", "Sync", "Synchronization", ["device sync", "handoff", "continuity"]),
        "home": Genius("home", "Home", "Smart Home", ["IoT", "home automation", "smart devices"]),
        "elder": Genius("elder", "Elder", "Accessibility", ["accessibility", "elder care", "simplified UX"])
    }
    
    def __init__(self):
        self.current_lead = None
        self.current_consultants = []
    
    def assign_team(self, problem_keywords: List[str]) -> Dict[str, Any]:
        """Assign Lead Genius and Consultants based on problem."""
        scores = {}
        
        for genius_id, genius in self.GENIUSES.items():
            score = 0
            for keyword in problem_keywords:
                keyword_lower = keyword.lower()
                if keyword_lower in genius.domain.lower():
                    score += 3
                for specialty in genius.specialties:
                    if keyword_lower in specialty.lower():
                        score += 2
            scores[genius_id] = score
        
        # Sort by score
        sorted_geniuses = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        # Assign lead and consultants
        self.current_lead = self.GENIUSES[sorted_geniuses[0][0]] if sorted_geniuses[0][1] > 0 else self.GENIUSES["pulse"]
        self.current_consultants = [
            self.GENIUSES[sorted_geniuses[i][0]] 
            for i in range(1, min(3, len(sorted_geniuses))) 
            if sorted_geniuses[i][1] > 0
        ]
        
        return {
            "lead": self.current_lead,
            "consultants": self.current_consultants,
            "team_summary": f"Lead: {self.current_lead.name} ({self.current_lead.domain}). Consulting: {', '.join([c.name for c in self.current_consultants]) or 'None needed'}."
        }
    
    def get_merged_opinion(self, opinions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Merge opinions from multiple geniuses, showing disagreements."""
        if len(opinions) <= 1:
            return {"merged": opinions[0] if opinions else {}, "disagreements": []}
        
        # Check for disagreements
        unique_diagnoses = set([o.get("diagnosis") for o in opinions])
        
        if len(unique_diagnoses) == 1:
            return {"merged": opinions[0], "disagreements": [], "consensus": True}
        
        # Build disagreement report
        disagreements = []
        for op in opinions:
            disagreements.append({
                "genius": op.get("genius_name"),
                "opinion": op.get("diagnosis"),
                "confidence": op.get("confidence")
            })
        
        # Merge: take highest confidence opinion as primary
        primary = max(opinions, key=lambda x: x.get("confidence", 0))
        
        return {
            "merged": primary,
            "disagreements": disagreements,
            "consensus": False,
            "transparency_message": f"Our specialists have different views. {primary.get('genius_name')} is most confident, but we'll address all concerns."
        }


# ═══════════════════════════════════════════════════════════════════════════════
# COGNITIVE LOAD MANAGER
# ═══════════════════════════════════════════════════════════════════════════════

class CognitiveLoadManager:
    """
    Dynamic "don't-fry-the-user" system.
    Tracks steps, complexity, time, stress signals.
    """
    
    def __init__(self):
        self.steps_taken = 0
        self.complexity_score = 0.0
        self.session_start = time.time()
        self.stress_signals = []
    
    def track_step(self, step_complexity: float = 0.5):
        """Track a step taken in the session."""
        self.steps_taken += 1
        self.complexity_score += step_complexity
    
    def add_stress_signal(self, signal: str):
        """Add a detected stress signal."""
        self.stress_signals.append({
            "signal": signal,
            "timestamp": time.time()
        })
    
    def get_load_assessment(self) -> Dict[str, Any]:
        """Assess current cognitive load."""
        session_duration = (time.time() - self.session_start) / 60  # minutes
        
        load_score = (
            (self.steps_taken * 0.1) +
            (self.complexity_score * 0.3) +
            (len(self.stress_signals) * 0.2) +
            (session_duration / 30 * 0.2)  # 30 min = 0.2 load
        )
        
        if load_score > 0.8:
            return {
                "load": "high",
                "recommendation": "collapse_to_one_recommendation",
                "offer_pause": True,
                "message": "You've been working hard on this. Want to pause and save our progress for later?"
            }
        elif load_score > 0.5:
            return {
                "load": "medium",
                "recommendation": "reduce_options",
                "offer_pause": False,
                "message": "Let's keep this simple. Here's the one thing I'd focus on."
            }
        else:
            return {
                "load": "low",
                "recommendation": "full_options",
                "offer_pause": False,
                "message": None
            }


# ═══════════════════════════════════════════════════════════════════════════════
# CRISIS PROTOCOL (MIRACLE MODE)
# ═══════════════════════════════════════════════════════════════════════════════

class CrisisProtocol:
    """
    Hardwired emergency flow.
    Triggered by: "I'm freaking out", "Total panic", "I think I lost everything"
    """
    
    CRISIS_PHRASES = [
        "freaking out", "total panic", "lost everything",
        "i'm dying here", "emergency", "please help", "oh god"
    ]
    
    def __init__(self):
        self.is_active = False
        self.crisis_start = None
    
    def check_trigger(self, user_input: str) -> bool:
        """Check if crisis mode should be triggered."""
        input_lower = user_input.lower()
        for phrase in self.CRISIS_PHRASES:
            if phrase in input_lower:
                self.activate()
                return True
        return False
    
    def activate(self):
        """Activate crisis mode."""
        self.is_active = True
        self.crisis_start = time.time()
    
    def deactivate(self):
        """Deactivate crisis mode."""
        self.is_active = False
        self.crisis_start = None
    
    def get_crisis_response(self, stage: str = "initial") -> Dict[str, Any]:
        """Get the appropriate crisis response for the current stage."""
        responses = {
            "initial": {
                "tone": "calm_anchor",
                "message": "Okay. I hear you. This is one of those horrible moments.\n\nWe're going to slow this down and protect you and your files as much as possible.\n\nFirst:\n• I'm on your side.\n• Your data is priority #1.\n• We'll go one step at a time. No pressure, no blame.",
                "next_action": "assess_damage",
                "repeat_phrase": "Your files and safety are priority one."
            },
            "assess_damage": {
                "tone": "calm_anchor",
                "message": "Before we do anything else, I need to understand what we're protecting.\n\nAre there irreplaceable things on there? (Old photos, work, kid's stuff, etc.)",
                "next_action": "present_paths",
                "repeat_phrase": "Your files and safety are priority one."
            },
            "present_paths": {
                "tone": "calm_anchor",
                "message": "You've got three realistic paths:",
                "paths": [
                    {
                        "name": "Maximize chance of recovery",
                        "description": "Take the drive to a professional data recovery lab. Best chance to save everything. Usually most expensive.",
                        "risk": "lowest",
                        "cost": "highest"
                    },
                    {
                        "name": "Careful DIY / local tech attempt",
                        "description": "Remove drive, connect externally, try to copy data once. Cheaper but more risk.",
                        "risk": "medium",
                        "cost": "medium"
                    },
                    {
                        "name": "Give up on data, fix the machine",
                        "description": "Replace drive, reinstall OS. You keep the machine, lose unbackup data. NOT recommended if data matters.",
                        "risk": "data_loss",
                        "cost": "lowest"
                    }
                ],
                "recommendation": "If this were my machine and those were my family photos, I would lean strongly toward Option 1 or a very careful Option 2, never Option 3 first.",
                "next_action": "execute_chosen_path"
            },
            "closing": {
                "tone": "supportive",
                "message": "When you're through this (and you will be, one way or another), I want to help you set up a system where this never feels this scary again:\n\n• Automatic backups for important stuff\n• Safer drives for long-term memories\n• Early-warning checks so we catch failing drives months earlier\n\nBut for today, you only need to remember this:\n• Stop powering it on.\n• Treat it as a data rescue case.\n• Talk to a real lab or careful tech.\n\nYou're not alone in this.",
                "next_action": None
            }
        }
        return responses.get(stage, responses["initial"])


# ═══════════════════════════════════════════════════════════════════════════════
# ALIGNMENT LINTER (ETHICS CHECK ON EVERY ANSWER)
# ═══════════════════════════════════════════════════════════════════════════════

class AlignmentLinter:
    """
    AI that checks the AI.
    Every response passes through an internal "linter" that scores:
    ✅ Truthfulness, ✅ Clarity, ✅ Kindness, ✅ User-first
    """
    
    def __init__(self):
        self.threshold = 0.7  # Minimum score to pass
    
    def lint(self, response_text: str, response_metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Lint a response for ethics compliance."""
        scores = {
            "truthfulness": self._check_truthfulness(response_text, response_metadata),
            "clarity": self._check_clarity(response_text),
            "kindness": self._check_kindness(response_text),
            "user_first": self._check_user_first(response_text, response_metadata)
        }
        
        overall = sum(scores.values()) / len(scores)
        passed = all(s >= self.threshold for s in scores.values())
        
        result = {
            "scores": scores,
            "overall": overall,
            "passed": passed,
            "issues": []
        }
        
        if not passed:
            for metric, score in scores.items():
                if score < self.threshold:
                    result["issues"].append(f"{metric.upper()}: Score {score:.2f} below threshold {self.threshold}")
            result["action"] = "REWRITE_REQUIRED"
        else:
            result["action"] = "APPROVED"
        
        return result
    
    def _check_truthfulness(self, text: str, metadata: Dict[str, Any]) -> float:
        """Check for truthfulness indicators."""
        score = 1.0
        
        # Penalize fake certainty
        fake_certainty_phrases = ["definitely", "absolutely", "100%", "guaranteed", "for sure"]
        for phrase in fake_certainty_phrases:
            if phrase in text.lower() and not metadata.get("high_confidence", False):
                score -= 0.2
        
        # Reward uncertainty markers
        uncertainty_markers = ["I think", "likely", "probably", "I suspect", "my best guess"]
        for marker in uncertainty_markers:
            if marker.lower() in text.lower():
                score += 0.1
        
        return max(0, min(1, score))
    
    def _check_clarity(self, text: str) -> float:
        """Check for clarity."""
        score = 1.0
        
        # Penalize jargon without explanation
        jargon = ["BIOS", "kernel", "daemon", "registry", "firmware", "driver", "cache"]
        jargon_count = sum(1 for j in jargon if j.lower() in text.lower())
        if jargon_count > 2:
            score -= 0.1 * (jargon_count - 2)
        
        # Penalize very long sentences
        sentences = text.split('.')
        long_sentences = sum(1 for s in sentences if len(s.split()) > 30)
        if long_sentences > 2:
            score -= 0.1 * long_sentences
        
        return max(0, min(1, score))
    
    def _check_kindness(self, text: str) -> float:
        """Check for kindness."""
        score = 1.0
        
        # Penalize blame/shame language
        blame_phrases = ["you should have", "why didn't you", "that was dumb", "your fault", "you broke"]
        for phrase in blame_phrases:
            if phrase in text.lower():
                score -= 0.3
        
        # Reward supportive language
        supportive_phrases = ["not your fault", "this is normal", "don't worry", "we'll figure this out", "I'm here"]
        for phrase in supportive_phrases:
            if phrase in text.lower():
                score += 0.1
        
        return max(0, min(1, score))
    
    def _check_user_first(self, text: str, metadata: Dict[str, Any]) -> float:
        """Check if response puts user first."""
        score = 1.0
        
        # Penalize upselling language
        upsell_phrases = ["upgrade now", "buy our", "premium", "subscribe"]
        for phrase in upsell_phrases:
            if phrase in text.lower():
                score -= 0.2
        
        # Reward user-benefit language
        benefit_phrases = ["save you", "protect your", "for your safety", "your choice", "your data"]
        for phrase in benefit_phrases:
            if phrase in text.lower():
                score += 0.1
        
        return max(0, min(1, score))


# ═══════════════════════════════════════════════════════════════════════════════
# "WHAT WOULD ROB SAY?" FILTER
# ═══════════════════════════════════════════════════════════════════════════════

class RobFilter:
    """
    Hard alignment to Rob's voice & values.
    "Is this how Rob would want a genius friend to talk to someone in pain?"
    """
    
    ROB_VALUES = [
        "honest_not_harsh",
        "kind_not_patronizing",
        "technical_not_jargony",
        "helpful_not_pushy",
        "calm_not_robotic",
        "empathetic_not_sappy"
    ]
    
    def __init__(self):
        pass
    
    def filter(self, response_text: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Apply the Rob filter to a response."""
        issues = []
        suggestions = []
        
        # Check for cold/robotic phrasing
        robotic_phrases = ["as per", "please be advised", "it is recommended that", "the system indicates"]
        for phrase in robotic_phrases:
            if phrase in response_text.lower():
                issues.append(f"Robotic phrasing detected: '{phrase}'")
                suggestions.append("Use warmer, more conversational language")
        
        # Check for condescension
        condescending = ["obviously", "simply", "just", "as you should know", "clearly"]
        for phrase in condescending:
            # "just" is okay in some contexts
            if phrase in response_text.lower() and phrase != "just":
                issues.append(f"Potentially condescending: '{phrase}'")
                suggestions.append("Remove assumptions about what user should know")
        
        # Check for missing empathy in crisis context
        if context.get("emotional_state") == "crisis":
            empathy_markers = ["i understand", "this is hard", "i'm here", "we'll get through", "not your fault"]
            has_empathy = any(marker in response_text.lower() for marker in empathy_markers)
            if not has_empathy:
                issues.append("Missing empathy markers in crisis context")
                suggestions.append("Add acknowledgment of user's emotional state")
        
        passed = len(issues) == 0
        
        return {
            "passed": passed,
            "issues": issues,
            "suggestions": suggestions,
            "rob_would_approve": passed,
            "golden_question": "Is this how Rob would want a genius friend to talk to someone in pain?"
        }


# ═══════════════════════════════════════════════════════════════════════════════
# STANDARD SESSION FLOW ("COFFEE WITH A GENIUS" SCRIPT)
# ═══════════════════════════════════════════════════════════════════════════════

class SessionFlow:
    """
    The "Coffee With a Genius" session flow.
    1. ARRIVE → 2. SCAN → 3. REPORT → 4. OPTIONS → 5. EXECUTE → 6. CLOSE
    """
    
    class Stage(Enum):
        ARRIVE = "arrive"
        SCAN = "scan"
        REPORT = "report"
        OPTIONS = "options"
        EXECUTE = "execute"
        CLOSE = "close"
    
    STAGE_SCRIPTS = {
        Stage.ARRIVE: {
            "message": "Hey. You're safe here. Let's calm your machine down and make a plan.",
            "actions": ["greet", "set_tone", "detect_mood"]
        },
        Stage.SCAN: {
            "message": "Let me take a quick look at what's going on...",
            "actions": ["read_logs", "check_health", "check_os", "check_storage", "check_network"]
        },
        Stage.REPORT: {
            "structure": [
                "Good news first",
                "Here's what I found",
                "Top 1-2 likely causes",
                "How sure I am"
            ]
        },
        Stage.OPTIONS: {
            "structure": [
                "Option A – Best balance",
                "Option B – Safer / more cautious",
                "Option C – Cheaper / more DIY (if sensible)",
                "What I'd do if this were my machine"
            ]
        },
        Stage.EXECUTE: {
            "pre_checks": [
                "Show what will be touched",
                "Label risk level",
                "Get explicit consent"
            ],
            "risk_labels": {
                "safe_reversible": "✅ Safe & reversible",
                "safe_permanent": "⚠️ Safe but permanent",
                "risky": "🔶 Risky: backup strongly recommended first"
            }
        },
        Stage.CLOSE: {
            "structure": [
                "What we did",
                "How things improved / stabilized",
                "What to watch for next"
            ],
            "offers": [
                "Want the nerdy breakdown?",
                "Want a simple summary PDF/email?"
            ]
        }
    }
    
    def __init__(self):
        self.current_stage = self.Stage.ARRIVE
        self.stage_history = []
    
    def advance(self) -> Dict[str, Any]:
        """Advance to the next stage."""
        stages = list(self.Stage)
        current_idx = stages.index(self.current_stage)
        
        if current_idx < len(stages) - 1:
            self.stage_history.append(self.current_stage)
            self.current_stage = stages[current_idx + 1]
        
        return self.get_current_stage_info()
    
    def get_current_stage_info(self) -> Dict[str, Any]:
        """Get information about the current stage."""
        return {
            "stage": self.current_stage.value,
            "script": self.STAGE_SCRIPTS.get(self.current_stage, {}),
            "progress": f"{list(self.Stage).index(self.current_stage) + 1}/{len(self.Stage)}"
        }


# ═══════════════════════════════════════════════════════════════════════════════
# MASTER MIRACLE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class MiracleEngine:
    """
    The complete Miracle Engine that orchestrates all components.
    "The miracle isn't that NOIZYLAB is magic.
    The miracle is that it's relentlessly on your side:
    smart, safe, kind, and clear, every single time."
    """
    
    def __init__(self):
        self.diag_brain = DiagBrain()
        self.human_brain = HumanBrain()
        self.story_brain = StoryBrain()
        self.orchestrator = GeniusOrchestrator()
        self.load_manager = CognitiveLoadManager()
        self.crisis_protocol = CrisisProtocol()
        self.alignment_linter = AlignmentLinter()
        self.rob_filter = RobFilter()
        self.session_flow = SessionFlow()
    
    def process_input(self, user_input: str, system_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process user input through the complete Miracle Engine."""
        system_data = system_data or {}
        
        # 1. Check for crisis trigger
        if self.crisis_protocol.check_trigger(user_input):
            return self._handle_crisis(user_input)
        
        # 2. Detect emotional state (Human Brain)
        emotional_state = self.human_brain.detect_state(user_input)
        
        # 3. Extract problem keywords and assign genius team
        keywords = self._extract_keywords(user_input)
        team = self.orchestrator.assign_team(keywords)
        
        # 4. Run diagnostics (Diag Brain)
        symptoms = self._extract_symptoms(user_input)
        diagnosis = self.diag_brain.analyze(symptoms, system_data)
        
        # 5. Generate human-readable summary (Story Brain)
        summary = self.story_brain.generate_summary(
            diagnosis.get("top_suspect", {}),
            emotional_state.get("detail_level", "full")
        )
        
        # 6. Check cognitive load
        load_assessment = self.load_manager.get_load_assessment()
        
        # 7. Build response
        response = self._build_response(
            emotional_state=emotional_state,
            team=team,
            diagnosis=diagnosis,
            summary=summary,
            load_assessment=load_assessment
        )
        
        # 8. Lint the response
        lint_result = self.alignment_linter.lint(response["text"], response)
        
        # 9. Apply Rob filter
        rob_result = self.rob_filter.filter(response["text"], {"emotional_state": emotional_state["state"]})
        
        # 10. Final output
        return {
            "response": response,
            "emotional_state": emotional_state,
            "team": team,
            "diagnosis": diagnosis,
            "summary": summary,
            "lint_result": lint_result,
            "rob_filter": rob_result,
            "session_stage": self.session_flow.get_current_stage_info()
        }
    
    def _handle_crisis(self, user_input: str) -> Dict[str, Any]:
        """Handle crisis mode input."""
        crisis_response = self.crisis_protocol.get_crisis_response("initial")
        
        return {
            "response": {
                "text": crisis_response["message"],
                "tone": crisis_response["tone"],
                "is_crisis": True
            },
            "emotional_state": {"state": "crisis", "stress_level": 1.0},
            "crisis_protocol": crisis_response,
            "session_stage": {"stage": "crisis_mode", "progress": "1/?"}
        }
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract problem-related keywords from text."""
        keywords = []
        keyword_map = {
            "slow": ["performance", "speed"],
            "boot": ["startup", "boot"],
            "click": ["hardware", "drive"],
            "fan": ["thermal", "cooling"],
            "wifi": ["network", "connectivity"],
            "crash": ["stability", "software"],
            "data": ["data", "backup"],
            "virus": ["security", "malware"]
        }
        
        text_lower = text.lower()
        for trigger, kws in keyword_map.items():
            if trigger in text_lower:
                keywords.extend(kws)
        
        return list(set(keywords)) or ["general"]
    
    def _extract_symptoms(self, text: str) -> List[str]:
        """Extract symptoms from user description."""
        symptoms = []
        
        symptom_patterns = [
            "slow", "clicking", "not booting", "won't boot", "fans loud",
            "overheating", "freezing", "crashing", "blue screen", "error",
            "won't start", "dead", "no power", "no display"
        ]
        
        text_lower = text.lower()
        for pattern in symptom_patterns:
            if pattern in text_lower:
                symptoms.append(pattern)
        
        return symptoms or ["unspecified issue"]
    
    def _build_response(self, **kwargs) -> Dict[str, Any]:
        """Build the final response based on all inputs."""
        emotional_state = kwargs.get("emotional_state", {})
        summary = kwargs.get("summary", {})
        load_assessment = kwargs.get("load_assessment", {})
        
        # Adjust based on emotional state
        if emotional_state.get("state") == "crisis":
            text = self.crisis_protocol.get_crisis_response()["message"]
        elif emotional_state.get("state") == "overloaded":
            text = f"{summary.get('one_liner', 'Let me help.')}\n\nWant to pause and come back to this later?"
        elif emotional_state.get("state") == "stressed":
            text = f"First, don't worry. We'll figure this out together.\n\n{summary.get('one_liner', '')}\n\n{summary.get('metaphor', '')}"
        else:
            text = f"{summary.get('one_liner', '')}\n\n{summary.get('metaphor', '')}\n\n{summary.get('confidence_statement', '')}"
        
        return {
            "text": text,
            "tone": emotional_state.get("tone", "friendly_expert"),
            "detail_level": emotional_state.get("detail_level", "full")
        }


# ═══════════════════════════════════════════════════════════════════════════════
# INSTANTIATE THE MIRACLE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

MIRACLE_ENGINE = MiracleEngine()

