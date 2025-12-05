# backend_ultra/business/service_tiers.py
# NOIZYLAB SERVICE TIERS (ETHICAL, CLEAR, NON-SCAMMY)
# ═══════════════════════════════════════════════════════════════════════════════

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# SERVICE TIER DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════════

class ServiceTier(Enum):
    QUICK_TUNEUP = "quick_tuneup"
    DEEP_REPAIR = "deep_repair"
    DATA_RESCUE = "data_rescue"
    MIGRATION = "migration"
    GUARDIAN = "guardian"

@dataclass
class ServiceTierConfig:
    """Configuration for a service tier."""
    id: str
    name: str
    emoji: str
    tagline: str
    use_when: List[str]
    what_it_is: List[str]
    what_it_is_not: List[str]
    duration: str
    deliverable: str
    price_range: str = None  # Optional, can be set later

SERVICE_TIERS = {
    ServiceTier.QUICK_TUNEUP: ServiceTierConfig(
        id="quick_tuneup",
        name="Quick Tune-Up Session",
        emoji="☕",
        tagline="Feel better in 10-15 minutes",
        use_when=[
            "Slow, annoying, fans loud, but not a crisis",
            "Things are frustrating but not on fire",
            "You want a quick win without deep diving"
        ],
        what_it_is=[
            "30-45 min remote session",
            "Clean safe junk & temp files",
            "Reduce startup bloat",
            "Tame obvious CPU hogs",
            "Check basic health (drive, temps, OS sanity)"
        ],
        what_it_is_not=[
            "Deep hardware diagnostics",
            "Data recovery",
            "Full reinstall / migration"
        ],
        duration="30-45 minutes",
        deliverable="Simple summary: what changed, how it improved, what to watch."
    ),
    
    ServiceTier.DEEP_REPAIR: ServiceTierConfig(
        id="deep_repair",
        name="Deep Repair Session",
        emoji="🛠",
        tagline="Really understand and fix a stubborn problem",
        use_when=[
            "Repeated crashes, weird behaviour, mystery slowness",
            "You suspect something is actually wrong",
            "Quick fixes haven't worked"
        ],
        what_it_is=[
            "60-120 min session (remote or hybrid)",
            "Run deeper diagnostics (logs, SMART, thermals, RAM stress)",
            "Untangle conflicting software, drivers, odd behaviours",
            "Stabilize system and plan any needed hardware / OS moves"
        ],
        what_it_is_not=[
            "Physical board-level repair",
            "Full lab-grade data recovery",
            "'We'll hack it until something breaks'"
        ],
        duration="60-120 minutes",
        deliverable="Clear diagnosis: what's likely wrong, what we did, recommended next move."
    ),
    
    ServiceTier.DATA_RESCUE: ServiceTierConfig(
        id="data_rescue",
        name="Data-First Rescue Strategy",
        emoji="🧯",
        tagline="Stabilize, protect data, map rescue options",
        use_when=[
            "Won't boot, clicking drive, scary noises, black screens",
            "'My life is on this'",
            "You're scared you lost everything"
        ],
        what_it_is=[
            "Focused session that does NOT brute-force the machine",
            "Assesses risk level honestly",
            "Helps choose between: Pro lab / Careful DIY / Accept loss & rebuild",
            "Helps you talk to recovery labs like a pro",
            "Plans best chance strategy, not wishful thinking"
        ],
        what_it_is_not=[
            "A guarantee of getting data back",
            "A replacement for a real lab when physical failure is severe"
        ],
        duration="Variable (depends on situation)",
        deliverable="Rescue brief you can show any shop/lab: symptoms, tests, suspected failure, do's & don'ts."
    ),
    
    ServiceTier.MIGRATION: ServiceTierConfig(
        id="migration",
        name="Migration & New-Machine Setup",
        emoji="🧭",
        tagline="Gracefully move your life to a new machine",
        use_when=[
            "Old machine is limping",
            "You want a clean, future-proofed setup",
            "You're ready to retire an old soldier"
        ],
        what_it_is=[
            "Planning: which machine should be your main one",
            "Defining what moves over (and what doesn't)",
            "Setting up: accounts, apps, email",
            "Backup system setup",
            "Basic security & maintenance rules"
        ],
        what_it_is_not=[
            "'Copy every mess from old to new'",
            "Infinite tweak marathon"
        ],
        duration="2-4 hours (can be split)",
        deliverable="A new machine that feels intentional + 'Tech Passport' doc."
    ),
    
    ServiceTier.GUARDIAN: ServiceTierConfig(
        id="guardian",
        name="Guardian Plan (Membership)",
        emoji="🛡",
        tagline="Ongoing peace of mind, not just one-off rescue",
        use_when=[
            "You want ongoing peace of mind",
            "You'd rather prevent disasters than react to them",
            "You value priority response when things go weird"
        ],
        what_it_is=[
            "Scheduled health checks",
            "Backup & drive health monitoring",
            "Priority response when things go weird",
            "One or two Quick Tune-Ups included per period",
            "Discount on Deep Repair/Migration"
        ],
        what_it_is_not=[
            "Fake 'must subscribe to be safe' messaging",
            "Hostage-taking (one-off sessions still fully supported)",
            "Subscription trap"
        ],
        duration="Monthly or Annual",
        deliverable="Peace of mind + priority access + regular health reports."
    )
}

def get_tier_recommendation(symptoms: List[str], stress_level: str, has_critical_data: bool) -> ServiceTier:
    """Recommend the best service tier based on symptoms and situation."""
    
    # Crisis indicators
    crisis_keywords = ["won't boot", "clicking", "dead", "lost everything", "black screen", "freaking out"]
    is_crisis = any(kw in " ".join(symptoms).lower() for kw in crisis_keywords) or stress_level == "crisis"
    
    if is_crisis and has_critical_data:
        return ServiceTier.DATA_RESCUE
    
    # Deep repair indicators
    deep_keywords = ["crashes", "repeated", "keeps", "mystery", "weird", "random"]
    needs_deep = any(kw in " ".join(symptoms).lower() for kw in deep_keywords)
    
    if needs_deep:
        return ServiceTier.DEEP_REPAIR
    
    # Migration indicators
    migration_keywords = ["old", "new machine", "upgrade", "replace", "migrate"]
    needs_migration = any(kw in " ".join(symptoms).lower() for kw in migration_keywords)
    
    if needs_migration:
        return ServiceTier.MIGRATION
    
    # Default to quick tune-up
    return ServiceTier.QUICK_TUNEUP

# ═══════════════════════════════════════════════════════════════════════════════
# SESSION TYPES (FROM USER'S POV)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class SessionType:
    """A session type as presented to the user."""
    id: str
    name: str
    emoji: str
    description: str
    time_estimate: str
    best_for: str

SESSION_TYPES = [
    SessionType(
        id="espresso",
        name="Quick Espresso Fix",
        emoji="☕",
        description="Feel better in 10-15 minutes. Startup cleanup, junk removal, obvious CPU hogs.",
        time_estimate="30-45 min",
        best_for="Slow, annoying, but not on fire"
    ),
    SessionType(
        id="deep_dive",
        name="Deep Dive Repair",
        emoji="🛠",
        description="Really understand and fix a stubborn problem. Multi-step diagnosis, hardware checks.",
        time_estimate="60-120 min",
        best_for="Repeated problems, mystery crashes, suspected trouble"
    ),
    SessionType(
        id="crisis",
        name="Crisis Rescue",
        emoji="🧯",
        description="Stabilize, protect data, map rescue options. One step at a time, emotions first.",
        time_estimate="Variable",
        best_for="Won't boot, dying drives, 'my life is on this'"
    ),
    SessionType(
        id="autopilot_review",
        name="Autopilot Review",
        emoji="🧭",
        description="See what NOIZY did for you in the background, and what's next.",
        time_estimate="15-30 min",
        best_for="Weekly/monthly overview, peace of mind"
    )
]

# ═══════════════════════════════════════════════════════════════════════════════
# GUARDIAN PLAN TIERS
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class GuardianTier:
    """A Guardian Plan membership tier."""
    id: str
    name: str
    tagline: str
    includes: List[str]
    price_monthly: float = None
    price_annual: float = None

GUARDIAN_TIERS = [
    GuardianTier(
        id="starter",
        name="Starter Guardian",
        tagline="Basic peace of mind",
        includes=[
            "Monthly health check",
            "Backup status monitoring",
            "Priority email response",
            "1 Quick Tune-Up per quarter"
        ]
    ),
    GuardianTier(
        id="guardian",
        name="Full Guardian",
        tagline="Complete protection",
        includes=[
            "Weekly health checks",
            "Real-time backup & drive monitoring",
            "Priority response (same-day)",
            "2 Quick Tune-Ups per month",
            "1 Deep Repair per quarter (included)",
            "10% off all other services"
        ]
    ),
    GuardianTier(
        id="legacy",
        name="Legacy Guardian",
        tagline="Your tech heritage, protected",
        includes=[
            "Everything in Full Guardian",
            "Quarterly 'Tech Passport' update",
            "Annual migration planning session",
            "Priority crisis response (within 2 hours)",
            "Family device coverage (up to 5 devices)",
            "20% off all services"
        ]
    )
]

# ═══════════════════════════════════════════════════════════════════════════════
# ETHICAL PRICING RULES
# ═══════════════════════════════════════════════════════════════════════════════

ETHICAL_PRICING_RULES = """
NOIZYLAB PRICING ETHICS (HARD RULES)

1. NO FAKE URGENCY
   - Never say "subscribe or you're at risk"
   - One-off sessions are always available
   - Membership = extra stability, not hostage-taking

2. NO HIDDEN FEES
   - Price quoted = price paid
   - If scope expands, we discuss BEFORE billing

3. HONEST RECOMMENDATIONS
   - If repair cost > device value, we say so
   - If a local shop is better for this job, we say so
   - If DIY is reasonable, we help you do it yourself

4. CONFLICT OF INTEREST RULE
   - When user's best interest vs our revenue conflict:
   - ALWAYS pick user's best interest
   - Even if it loses NOIZYLAB money

5. VALUE TRANSPARENCY
   - We explain what you're paying for
   - We explain what you're NOT getting
   - No mystery bundles or confusing tiers
"""

def check_pricing_ethics(recommendation: Dict[str, Any]) -> Dict[str, Any]:
    """Check if a pricing/service recommendation follows ethical rules."""
    issues = []
    
    # Check for fake urgency
    if recommendation.get("urgency_language") and not recommendation.get("is_genuinely_urgent"):
        issues.append("Fake urgency detected - remove urgency language")
    
    # Check for hidden scope
    if recommendation.get("has_hidden_scope"):
        issues.append("Hidden scope detected - disclose all potential costs upfront")
    
    # Check conflict of interest
    if recommendation.get("benefits_noizylab_over_user"):
        issues.append("Conflict of interest - recommendation benefits NOIZYLAB over user")
    
    # Check if repair > value
    repair_cost = recommendation.get("repair_cost", 0)
    device_value = recommendation.get("device_value", float('inf'))
    if repair_cost > device_value * 0.7:
        issues.append(f"Repair cost ({repair_cost}) may exceed device value ({device_value}) - discuss replacement option")
    
    return {
        "ethical": len(issues) == 0,
        "issues": issues,
        "recommendation": "Proceed" if len(issues) == 0 else "Review and adjust"
    }

