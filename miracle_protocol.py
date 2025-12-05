"""
═══════════════════════════════════════════════════════════════════════════════
                         THE MIRACLE PROTOCOL
═══════════════════════════════════════════════════════════════════════════════

For the WORST days of their tech life.
When everything is on fire.

"My computer just died and I'm freaking out."
"I think I lost everything."
"This is for my business / school / family photos."

We give them something LEGENDARY.

No guesses. No false hope. Just the real playbook.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class CrisisLevel(Enum):
    """How severe is the crisis"""
    PANIC = "panic"              # User is freaking out
    URGENT = "urgent"            # Time-sensitive, high stakes
    SERIOUS = "serious"          # Bad situation, needs help
    CONCERNING = "concerning"    # Problems, but manageable


class StakeType(Enum):
    """What's at stake"""
    MEMORIES = "memories"        # Photos, videos, irreplaceable
    BUSINESS = "business"        # Work, income, clients
    SCHOOL = "school"            # Assignments, deadlines
    CREATIVE = "creative"        # Music, art, projects
    FINANCIAL = "financial"      # Tax records, banking
    MEDICAL = "medical"          # Health records
    LEGAL = "legal"              # Legal documents
    GENERAL = "general"          # General data


class FailureType(Enum):
    """What kind of failure"""
    DRIVE_DEAD = "drive_dead"
    DRIVE_DYING = "drive_dying"
    OS_CORRUPT = "os_corrupt"
    MALWARE = "malware"
    RANSOMWARE = "ransomware"
    PHYSICAL_DAMAGE = "physical"
    LIQUID_DAMAGE = "liquid"
    WONT_BOOT = "no_boot"
    DATA_DELETED = "deleted"
    UNKNOWN = "unknown"


@dataclass
class MiracleOption:
    """One possible path forward"""
    name: str
    description: str
    success_chance: str          # "High", "Moderate", "Low", "Unknown"
    cost_range: str
    time_range: str
    preserves_data: bool
    requires_professional: bool
    risk_level: str              # "Low", "Moderate", "High"
    steps: List[str]
    why_this_option: str


@dataclass
class MiraclePlan:
    """The complete miracle plan"""
    crisis_level: CrisisLevel
    stakes: List[StakeType]
    failure_type: FailureType
    
    # Stabilization
    immediate_actions: List[str]
    what_not_to_do: List[str]
    
    # Options
    best_chance: MiracleOption
    best_balance: MiracleOption
    budget_option: MiracleOption
    
    # Support
    emotional_message: str
    realistic_expectations: str
    next_step: str


class MiracleProtocol:
    """
    THE MIRACLE PROTOCOL
    
    When everything is on fire, we become their calm in the storm.
    
    Steps:
    1. STABILIZE - Don't make it worse
    2. MAP - What's at stake, what failed
    3. PROTECT - Preserve what remains
    4. OPTIONS - Best chance / Best balance / Budget path
    """
    
    def __init__(self):
        self.active_miracles: Dict[str, MiraclePlan] = {}
    
    def detect_crisis(self, user_message: str) -> Optional[CrisisLevel]:
        """Detect if this is a crisis situation"""
        message = user_message.lower()
        
        panic_triggers = [
            "freaking out", "panicking", "help me", "emergency",
            "lost everything", "all my", "please help", "desperate",
            "crying", "can't breathe", "nightmare"
        ]
        
        urgent_triggers = [
            "deadline", "tomorrow", "tonight", "business",
            "client", "presentation", "exam", "interview"
        ]
        
        serious_triggers = [
            "died", "dead", "won't turn on", "lost",
            "deleted", "gone", "crashed", "broken"
        ]
        
        if any(t in message for t in panic_triggers):
            return CrisisLevel.PANIC
        if any(t in message for t in urgent_triggers):
            return CrisisLevel.URGENT
        if any(t in message for t in serious_triggers):
            return CrisisLevel.SERIOUS
        
        return None
    
    def detect_stakes(self, user_message: str) -> List[StakeType]:
        """Detect what's at stake"""
        message = user_message.lower()
        stakes = []
        
        if any(w in message for w in ["photo", "picture", "video", "memory", "memories", "family"]):
            stakes.append(StakeType.MEMORIES)
        if any(w in message for w in ["work", "business", "client", "job", "income"]):
            stakes.append(StakeType.BUSINESS)
        if any(w in message for w in ["school", "homework", "assignment", "thesis", "exam"]):
            stakes.append(StakeType.SCHOOL)
        if any(w in message for w in ["music", "art", "project", "creative", "design"]):
            stakes.append(StakeType.CREATIVE)
        if any(w in message for w in ["tax", "bank", "financial", "money"]):
            stakes.append(StakeType.FINANCIAL)
        
        if not stakes:
            stakes.append(StakeType.GENERAL)
        
        return stakes
    
    def detect_failure(self, user_message: str) -> FailureType:
        """Detect type of failure"""
        message = user_message.lower()
        
        if any(w in message for w in ["clicking", "grinding", "dead drive", "drive died"]):
            return FailureType.DRIVE_DEAD
        if any(w in message for w in ["slow", "freezing", "bad sectors"]):
            return FailureType.DRIVE_DYING
        if any(w in message for w in ["won't boot", "won't start", "black screen", "no power"]):
            return FailureType.WONT_BOOT
        if any(w in message for w in ["virus", "malware", "infected", "hacked"]):
            return FailureType.MALWARE
        if any(w in message for w in ["ransomware", "encrypted", "pay", "bitcoin"]):
            return FailureType.RANSOMWARE
        if any(w in message for w in ["dropped", "cracked", "broken screen", "physical"]):
            return FailureType.PHYSICAL_DAMAGE
        if any(w in message for w in ["spill", "water", "coffee", "liquid", "wet"]):
            return FailureType.LIQUID_DAMAGE
        if any(w in message for w in ["deleted", "erased", "formatted", "empty"]):
            return FailureType.DATA_DELETED
        if any(w in message for w in ["corrupt", "won't load", "error"]):
            return FailureType.OS_CORRUPT
        
        return FailureType.UNKNOWN
    
    def generate_stabilization(self, failure: FailureType) -> tuple:
        """Generate immediate stabilization steps"""
        
        immediate = ["Take a deep breath. You're not alone in this."]
        dont_do = []
        
        if failure == FailureType.DRIVE_DEAD:
            immediate.extend([
                "STOP using the device immediately",
                "Do NOT keep trying to power it on",
                "Keep it in a safe, dry place"
            ])
            dont_do.extend([
                "Don't shake or move the drive unnecessarily",
                "Don't try DIY recovery software on a clicking drive",
                "Don't put it in the freezer (old myth, doesn't help)"
            ])
        
        elif failure == FailureType.LIQUID_DAMAGE:
            immediate.extend([
                "Power OFF immediately if still on",
                "Unplug from power",
                "Do NOT try to turn it on to 'check if it works'",
                "Place upside down on towel to drain"
            ])
            dont_do.extend([
                "Don't use a hair dryer (can push liquid deeper)",
                "Don't put in rice (doesn't really help, can add debris)",
                "Don't charge it"
            ])
        
        elif failure == FailureType.RANSOMWARE:
            immediate.extend([
                "Disconnect from internet immediately",
                "Do NOT pay the ransom yet",
                "Take photos of any ransom messages",
                "Note exactly what you can and can't access"
            ])
            dont_do.extend([
                "Don't delete anything",
                "Don't run random 'decryption' tools",
                "Don't restart repeatedly"
            ])
        
        elif failure == FailureType.DATA_DELETED:
            immediate.extend([
                "STOP using the device immediately",
                "Do NOT save any new files",
                "Do NOT install recovery software on the same drive"
            ])
            dont_do.extend([
                "Don't empty the trash/recycle bin if you haven't",
                "Don't defragment or optimize the drive",
                "Don't reinstall the OS"
            ])
        
        else:
            immediate.extend([
                "Stop what you're doing on the device",
                "Note any error messages you see",
                "Don't make changes until we understand the situation"
            ])
            dont_do.extend([
                "Don't reinstall the operating system yet",
                "Don't run random fix tools from the internet"
            ])
        
        return immediate, dont_do
    
    def generate_options(self, failure: FailureType, stakes: List[StakeType]) -> tuple:
        """Generate miracle options"""
        
        has_irreplaceable = StakeType.MEMORIES in stakes or StakeType.CREATIVE in stakes
        
        # Best chance option
        if failure in [FailureType.DRIVE_DEAD, FailureType.LIQUID_DAMAGE]:
            best = MiracleOption(
                name="Professional Data Recovery",
                description="Send to a certified data recovery lab with clean room facilities",
                success_chance="60-90% for mechanical failure",
                cost_range="$300 - $1500+",
                time_range="5-14 business days",
                preserves_data=True,
                requires_professional=True,
                risk_level="Low (they're experts)",
                steps=[
                    "We'll help you find a reputable recovery service",
                    "They'll do a free or low-cost evaluation",
                    "You approve the quote before any work",
                    "They recover what's possible"
                ],
                why_this_option="This gives you the best possible chance of getting your data back. Worth it for irreplaceable files."
            )
        elif failure == FailureType.RANSOMWARE:
            best = MiracleOption(
                name="Professional Ransomware Response",
                description="Security specialist assessment and potential decryption",
                success_chance="Varies - some ransomware has known decryptors",
                cost_range="$200 - $500 for assessment",
                time_range="1-7 days",
                preserves_data=True,
                requires_professional=True,
                risk_level="Low",
                steps=[
                    "Identify the exact ransomware variant",
                    "Check if free decryptors exist (many do!)",
                    "If not, assess backup restoration options",
                    "Clean the system completely"
                ],
                why_this_option="Many ransomware variants have been cracked. A pro can check before you consider paying."
            )
        else:
            best = MiracleOption(
                name="Careful Professional Diagnosis",
                description="Let an expert assess before any recovery attempts",
                success_chance="High for diagnosis, varies for recovery",
                cost_range="$50 - $150 for diagnosis",
                time_range="1-3 days",
                preserves_data=True,
                requires_professional=True,
                risk_level="Low",
                steps=[
                    "Don't attempt fixes yourself",
                    "Bring to a trusted technician",
                    "Get diagnosis before approving work",
                    "Prioritize data preservation"
                ],
                why_this_option="Knowing exactly what's wrong prevents making it worse."
            )
        
        # Best balance option
        if failure == FailureType.DATA_DELETED:
            balance = MiracleOption(
                name="Controlled DIY Recovery",
                description="Use recovery software carefully, with guidance",
                success_chance="Good for recently deleted files",
                cost_range="$0 - $100 for software",
                time_range="2-8 hours",
                preserves_data=True,
                requires_professional=False,
                risk_level="Moderate (must follow steps exactly)",
                steps=[
                    "Boot from a different drive or use another computer",
                    "Run recovery software that scans without writing",
                    "Recover to a DIFFERENT drive",
                    "Verify recovered files"
                ],
                why_this_option="If files were just deleted and you act fast, DIY recovery often works."
            )
        elif failure == FailureType.OS_CORRUPT:
            balance = MiracleOption(
                name="Boot from External + Data Extraction",
                description="Boot from USB, copy data, then repair/reinstall",
                success_chance="High if drive is healthy",
                cost_range="$0 - $50",
                time_range="2-4 hours",
                preserves_data=True,
                requires_professional=False,
                risk_level="Low",
                steps=[
                    "Create bootable USB on another computer",
                    "Boot from USB",
                    "Copy all important files to external drive",
                    "Then repair or reinstall OS"
                ],
                why_this_option="Gets your data safe first, then fixes the system."
            )
        else:
            balance = MiracleOption(
                name="Local Repair Shop",
                description="Third-party repair shop assessment",
                success_chance="Good for common issues",
                cost_range="$75 - $250",
                time_range="1-5 days",
                preserves_data=True,
                requires_professional=True,
                risk_level="Low-Moderate (verify their reputation)",
                steps=[
                    "Find a well-reviewed local shop",
                    "Explain data preservation is priority #1",
                    "Get a quote before approving work",
                    "Ask about their data handling policy"
                ],
                why_this_option="Faster and cheaper than manufacturer, usually just as good."
            )
        
        # Budget option
        budget = MiracleOption(
            name="Guided Self-Assessment",
            description="We walk you through safe diagnostic steps",
            success_chance="Helps determine next steps",
            cost_range="$0",
            time_range="30-60 minutes",
            preserves_data=True,
            requires_professional=False,
            risk_level="Low (we guide you safely)",
            steps=[
                "We'll ask specific questions",
                "Guide you through safe checks",
                "Help you understand what's happening",
                "Recommend the right next step for your situation"
            ],
            why_this_option="Free, and helps you make an informed decision about what to do next."
        )
        
        return best, balance, budget
    
    def generate_emotional_support(self, crisis: CrisisLevel, stakes: List[StakeType]) -> str:
        """Generate appropriate emotional support message"""
        
        if crisis == CrisisLevel.PANIC:
            if StakeType.MEMORIES in stakes:
                return """
I hear you. This is scary, especially when memories are involved.

Here's what I want you to know: We're going to give this our absolute best shot.
Not with false hope, but with real expertise and a real plan.

Many situations that feel hopeless have good outcomes. Let's see what we're working with.
                """.strip()
            else:
                return """
I can hear the stress in your message, and I get it.

Take a breath. You found help. We're going to work through this together, step by step.

Let's start by making sure we don't make anything worse, then we'll figure out the best path forward.
                """.strip()
        
        elif crisis == CrisisLevel.URGENT:
            return """
I understand there's time pressure here. Let's be efficient.

We'll prioritize getting you functional as fast as possible while protecting what matters.
If there are trade-offs to make, I'll explain them clearly so you can decide.
            """.strip()
        
        else:
            return """
This is a tough situation, but you're in the right place.

We're going to figure out exactly what's happening and give you clear options.
No jargon, no upselling — just honest guidance.
            """.strip()
    
    def activate_miracle(self, session_id: str, user_message: str) -> MiraclePlan:
        """Activate the Miracle Protocol"""
        
        crisis = self.detect_crisis(user_message) or CrisisLevel.SERIOUS
        stakes = self.detect_stakes(user_message)
        failure = self.detect_failure(user_message)
        
        immediate, dont_do = self.generate_stabilization(failure)
        best, balance, budget = self.generate_options(failure, stakes)
        emotional = self.generate_emotional_support(crisis, stakes)
        
        # Realistic expectations
        if failure in [FailureType.DRIVE_DEAD, FailureType.LIQUID_DAMAGE]:
            expectations = "Some data may not be recoverable, but we'll maximize what we can save."
        elif failure == FailureType.RANSOMWARE:
            expectations = "Recovery depends on the specific ransomware. Many have solutions; some don't."
        else:
            expectations = "Most situations like this have good outcomes when handled carefully."
        
        plan = MiraclePlan(
            crisis_level=crisis,
            stakes=stakes,
            failure_type=failure,
            immediate_actions=immediate,
            what_not_to_do=dont_do,
            best_chance=best,
            best_balance=balance,
            budget_option=budget,
            emotional_message=emotional,
            realistic_expectations=expectations,
            next_step="Let's start with the stabilization steps, then I'll help you choose the right path."
        )
        
        self.active_miracles[session_id] = plan
        return plan
    
    def get_miracle_response(self, plan: MiraclePlan) -> str:
        """Generate the full miracle response"""
        
        response = f"""
{plan.emotional_message}

---

🧯 **FIRST: STABILIZE**

{chr(10).join(f"• {action}" for action in plan.immediate_actions)}

**What NOT to do:**
{chr(10).join(f"• {action}" for action in plan.what_not_to_do)}

---

🧭 **YOUR OPTIONS**

**Option 1: Best Chance of Saving Everything**
{plan.best_chance.name}
• {plan.best_chance.description}
• Success rate: {plan.best_chance.success_chance}
• Cost: {plan.best_chance.cost_range}
• Time: {plan.best_chance.time_range}
• Why: {plan.best_chance.why_this_option}

**Option 2: Best Balance of Cost & Outcome**
{plan.best_balance.name}
• {plan.best_balance.description}
• Success rate: {plan.best_balance.success_chance}
• Cost: {plan.best_balance.cost_range}
• Time: {plan.best_balance.time_range}
• Why: {plan.best_balance.why_this_option}

**Option 3: Budget-Conscious Path**
{plan.budget_option.name}
• {plan.budget_option.description}
• Cost: {plan.budget_option.cost_range}
• Time: {plan.budget_option.time_range}
• Why: {plan.budget_option.why_this_option}

---

📋 **REALISTIC EXPECTATIONS**

{plan.realistic_expectations}

---

{plan.next_step}
        """.strip()
        
        return response


# Singleton
miracle = MiracleProtocol()

