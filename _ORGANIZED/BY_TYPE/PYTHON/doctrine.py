"""
═══════════════════════════════════════════════════════════════════════════════
NOIZYLAB GENIUS DOCTRINE
═══════════════════════════════════════════════════════════════════════════════

THE LAW. THE WAY. NON-NEGOTIABLE.

Every interaction MUST end in one of four outcomes.
If the user ends thinking "idk what to do" — WE FAILED.

TRUST IS THE PRODUCT. Fixes are the bonus.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Dict
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# SESSION OUTCOMES — Every session MUST end in one of these
# ═══════════════════════════════════════════════════════════════════════════════

class SessionOutcome(Enum):
    FIXED = "fixed"              # Issue solved, logged, and verified
    STABILIZED = "stabilized"    # Damage stopped, safe until full repair
    ESCALATED = "escalated"      # Clear next steps provided
    DECISION_HELP = "decision"   # Repair vs replace with cost/risk/time
    INCOMPLETE = "incomplete"    # WE FAILED - user left confused


@dataclass
class OutcomeReport:
    """Every session generates an outcome report"""
    outcome: SessionOutcome
    summary: str
    actions_taken: List[str]
    next_steps: List[str]
    cost_estimate: Optional[str]
    time_estimate: Optional[str]
    risk_assessment: Optional[str]
    backup_verified: bool
    audit_trail: List[Dict]
    timestamp: datetime


# ═══════════════════════════════════════════════════════════════════════════════
# SAFETY PROTOCOLS — Trauma-proofing layer
# ═══════════════════════════════════════════════════════════════════════════════

class SafetyLevel(Enum):
    SAFE = "safe"                    # No risk of data loss
    CAUTION = "caution"              # Minor risk, reversible
    WARNING = "warning"              # Moderate risk, backup recommended
    RED_LINE = "red_line"            # High risk, requires double-confirm


# Actions that require RED_LINE protection
RED_LINE_OPERATIONS = [
    "disk_format",
    "partition_change",
    "partition_delete",
    "partition_resize",
    "firmware_flash",
    "bios_update",
    "registry_edit",
    "system_restore",
    "factory_reset",
    "os_reinstall",
    "bootloader_modify",
    "encryption_change",
    "secure_erase",
    "raid_rebuild",
    "driver_rollback_critical",
    "kernel_modification"
]

# Actions that require WARNING level
WARNING_OPERATIONS = [
    "driver_update",
    "system_update",
    "app_uninstall_system",
    "cache_clear_system",
    "temp_clean_aggressive",
    "startup_modify",
    "service_disable",
    "firewall_modify",
    "permission_change"
]


def get_safety_level(operation: str) -> SafetyLevel:
    """Determine safety level for an operation"""
    if operation in RED_LINE_OPERATIONS:
        return SafetyLevel.RED_LINE
    if operation in WARNING_OPERATIONS:
        return SafetyLevel.WARNING
    return SafetyLevel.SAFE


def generate_safety_warning(operation: str, safety_level: SafetyLevel) -> Dict:
    """Generate appropriate warning for operation"""
    warnings = {
        SafetyLevel.RED_LINE: {
            "level": "🚨 RED LINE OPERATION",
            "message": f"This operation ({operation}) could cause permanent data loss.",
            "requirements": [
                "Backup verification REQUIRED",
                "Double confirmation REQUIRED",
                "Dry-run option available",
                "Full audit trail will be recorded"
            ],
            "recommendation": "We strongly recommend creating a full backup before proceeding.",
            "can_undo": False
        },
        SafetyLevel.WARNING: {
            "level": "⚠️ CAUTION",
            "message": f"This operation ({operation}) carries some risk.",
            "requirements": [
                "Backup recommended",
                "Confirmation required"
            ],
            "recommendation": "Consider backing up important data first.",
            "can_undo": "Possibly"
        },
        SafetyLevel.CAUTION: {
            "level": "ℹ️ NOTICE",
            "message": f"This operation ({operation}) is generally safe.",
            "requirements": [],
            "recommendation": None,
            "can_undo": True
        },
        SafetyLevel.SAFE: {
            "level": "✅ SAFE",
            "message": "This operation carries no risk of data loss.",
            "requirements": [],
            "recommendation": None,
            "can_undo": True
        }
    }
    return warnings.get(safety_level, warnings[SafetyLevel.SAFE])


# ═══════════════════════════════════════════════════════════════════════════════
# ESCALATION PATHS — When Geniuses hit a wall
# ═══════════════════════════════════════════════════════════════════════════════

ESCALATION_PATHS = {
    "board_repair": {
        "name": "Board-Level Repair",
        "description": "Requires component-level soldering and diagnostics",
        "skill_level": "Specialized technician",
        "typical_cost": "$150-500+",
        "typical_time": "3-7 business days",
        "examples": ["Logic board failure", "GPU resoldering", "Power circuit repair"]
    },
    "data_recovery_pro": {
        "name": "Professional Data Recovery",
        "description": "Clean room recovery for failed drives",
        "skill_level": "Data recovery specialist",
        "typical_cost": "$300-2000+",
        "typical_time": "5-14 business days",
        "examples": ["Failed SSD", "Clicking HDD", "Physical damage"]
    },
    "manufacturer_rma": {
        "name": "Manufacturer RMA/Warranty",
        "description": "Return to manufacturer for repair/replacement",
        "skill_level": "N/A - manufacturer handles",
        "typical_cost": "Free if under warranty, varies if not",
        "typical_time": "7-21 business days",
        "examples": ["Manufacturing defect", "Warranty repair", "Recall"]
    },
    "authorized_service": {
        "name": "Authorized Service Provider",
        "description": "Official repair through manufacturer's network",
        "skill_level": "Certified technician",
        "typical_cost": "Varies by repair",
        "typical_time": "3-10 business days",
        "examples": ["Apple Authorized", "Microsoft Authorized", "Dell ProSupport"]
    },
    "local_shop": {
        "name": "Local Repair Shop",
        "description": "Third-party repair shop",
        "skill_level": "Varies - verify credentials",
        "typical_cost": "Usually 20-40% less than authorized",
        "typical_time": "1-5 business days",
        "examples": ["Screen replacement", "Battery swap", "General repair"]
    },
    "replace_device": {
        "name": "Device Replacement",
        "description": "Repair cost exceeds value - recommend replacement",
        "skill_level": "N/A",
        "typical_cost": "New device cost",
        "typical_time": "Immediate with data migration",
        "examples": ["Old device", "Multiple failures", "Cost prohibitive repair"]
    },
    "specialist_consult": {
        "name": "Specialist Consultation",
        "description": "Requires expert in specific domain",
        "skill_level": "Domain specialist",
        "typical_cost": "Consultation fee varies",
        "typical_time": "1-3 business days",
        "examples": ["Enterprise network", "Server infrastructure", "Custom hardware"]
    }
}


def get_escalation_recommendation(issue_type: str, device_age: int, repair_cost_estimate: float, device_value: float) -> Dict:
    """Generate escalation recommendation with full context"""
    
    # Calculate repair-to-value ratio
    repair_ratio = repair_cost_estimate / device_value if device_value > 0 else 1.0
    
    recommendation = {
        "should_repair": repair_ratio < 0.5,
        "repair_ratio": f"{repair_ratio * 100:.0f}%",
        "analysis": []
    }
    
    if repair_ratio >= 0.5:
        recommendation["analysis"].append(
            f"Repair cost ({repair_cost_estimate:.0f}) is {repair_ratio * 100:.0f}% of device value ({device_value:.0f})"
        )
        recommendation["analysis"].append("Replacement may be more cost-effective")
    
    if device_age > 5:
        recommendation["analysis"].append(
            f"Device is {device_age} years old - consider future reliability"
        )
    
    # Add specific escalation path
    if "board" in issue_type.lower() or "logic" in issue_type.lower():
        recommendation["escalation"] = ESCALATION_PATHS["board_repair"]
    elif "data" in issue_type.lower() or "recovery" in issue_type.lower():
        recommendation["escalation"] = ESCALATION_PATHS["data_recovery_pro"]
    elif repair_ratio >= 0.7:
        recommendation["escalation"] = ESCALATION_PATHS["replace_device"]
    else:
        recommendation["escalation"] = ESCALATION_PATHS["local_shop"]
    
    return recommendation


# ═══════════════════════════════════════════════════════════════════════════════
# AUDIT TRAIL — Every action logged
# ═══════════════════════════════════════════════════════════════════════════════

class AuditTrail:
    """Complete audit trail for every session"""
    
    def __init__(self, session_id: str, device_id: str):
        self.session_id = session_id
        self.device_id = device_id
        self.entries = []
        self.start_time = datetime.now()
    
    def log(self, action: str, genius_id: str, result: str, details: Dict = None):
        """Log an action to the audit trail"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "genius": genius_id,
            "result": result,
            "details": details or {},
            "safety_level": get_safety_level(action).value
        }
        self.entries.append(entry)
        return entry
    
    def log_warning_shown(self, operation: str, user_response: str):
        """Log that a warning was shown and user's response"""
        self.log(
            action=f"warning_shown:{operation}",
            genius_id="SYSTEM",
            result=user_response,
            details={"operation": operation, "user_acknowledged": user_response == "confirmed"}
        )
    
    def log_backup_check(self, backup_exists: bool, backup_date: Optional[str]):
        """Log backup verification"""
        self.log(
            action="backup_verification",
            genius_id="SYSTEM",
            result="verified" if backup_exists else "not_found",
            details={"backup_exists": backup_exists, "backup_date": backup_date}
        )
    
    def get_summary(self) -> Dict:
        """Get audit trail summary"""
        return {
            "session_id": self.session_id,
            "device_id": self.device_id,
            "start_time": self.start_time.isoformat(),
            "end_time": datetime.now().isoformat(),
            "total_actions": len(self.entries),
            "red_line_operations": sum(1 for e in self.entries if e["safety_level"] == "red_line"),
            "entries": self.entries
        }


# ═══════════════════════════════════════════════════════════════════════════════
# DEVICE MEMORY — Persistent knowledge about each device
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class DeviceProfile:
    """Persistent memory for each device"""
    device_id: str
    device_type: str  # mac, windows_pc, iphone, android, etc.
    make: str
    model: str
    year: Optional[int]
    specs: Dict  # CPU, RAM, storage, etc.
    os_version: str
    
    # History
    first_seen: datetime
    last_seen: datetime
    total_sessions: int
    
    # Repair history
    past_issues: List[Dict]  # [{issue, date, resolution, genius}]
    known_problems: List[str]  # Recurring issues
    
    # Environment
    network_info: Dict  # Router, ISP, typical speeds
    power_info: Dict  # UPS, surge protector, power quality
    
    # Risk factors
    risk_notes: List[str]  # "Flaky power", "Dusty environment", etc.
    
    def add_issue(self, issue: str, resolution: str, genius_id: str):
        """Add an issue to device history"""
        self.past_issues.append({
            "issue": issue,
            "date": datetime.now().isoformat(),
            "resolution": resolution,
            "genius": genius_id
        })
        self.total_sessions += 1
        self.last_seen = datetime.now()
    
    def get_context_for_genius(self) -> str:
        """Generate context string for genius consultation"""
        context = f"{self.make} {self.model}"
        if self.year:
            context += f" ({self.year})"
        context += f" running {self.os_version}"
        
        if self.past_issues:
            recent = self.past_issues[-3:]
            context += f". Recent issues: {', '.join(i['issue'] for i in recent)}"
        
        if self.risk_notes:
            context += f". Risk factors: {', '.join(self.risk_notes)}"
        
        return context


# ═══════════════════════════════════════════════════════════════════════════════
# SESSION FLOW — Repair Intake, not "chat"
# ═══════════════════════════════════════════════════════════════════════════════

INTAKE_QUESTIONS = [
    {
        "id": "what_broke",
        "question": "What's the problem you're experiencing?",
        "type": "text",
        "required": True
    },
    {
        "id": "when_started",
        "question": "When did this issue first start?",
        "type": "choice",
        "options": ["Just now", "Today", "This week", "Longer"],
        "required": True
    },
    {
        "id": "what_changed",
        "question": "Did anything change recently? (updates, new software, drops, spills)",
        "type": "text",
        "required": False
    },
    {
        "id": "symptoms",
        "question": "Any unusual sounds, smells, or visual symptoms?",
        "type": "multi_choice",
        "options": ["Clicking sounds", "Burning smell", "Screen flickering", "Overheating", "None"],
        "required": False
    },
    {
        "id": "backup_status",
        "question": "Do you have a recent backup of your important data?",
        "type": "choice",
        "options": ["Yes, within last week", "Yes, but older", "No backup", "Not sure"],
        "required": True,
        "critical": True
    },
    {
        "id": "urgency",
        "question": "How urgent is this?",
        "type": "choice",
        "options": ["Critical - can't work", "Important - need soon", "When convenient"],
        "required": True
    }
]


def generate_intake_form(device_profile: Optional[DeviceProfile] = None) -> List[Dict]:
    """Generate intake form, auto-filling from device profile where possible"""
    form = INTAKE_QUESTIONS.copy()
    
    if device_profile:
        # Add device context
        form.insert(0, {
            "id": "device_confirm",
            "question": f"Is this about your {device_profile.make} {device_profile.model}?",
            "type": "choice",
            "options": ["Yes", "No, different device"],
            "prefilled": True
        })
        
        # Add history context if relevant
        if device_profile.past_issues:
            recent_issue = device_profile.past_issues[-1]
            form.insert(2, {
                "id": "related_to_previous",
                "question": f"Is this related to the previous issue ({recent_issue['issue']})?",
                "type": "choice",
                "options": ["Yes, same issue", "No, different problem", "Not sure"],
                "prefilled": False
            })
    
    return form


# ═══════════════════════════════════════════════════════════════════════════════
# TRUST LANGUAGE — Calm, direct, non-hype
# ═══════════════════════════════════════════════════════════════════════════════

TRUST_PHRASES = {
    "uncertainty": [
        "Here's what I know. Here's what I don't. Here's what I recommend.",
        "I'm confident about X, but Y needs more investigation.",
        "This could be A or B. Let's run a test to find out."
    ],
    "limitation": [
        "This is beyond what I can fix remotely. Here's your best next step.",
        "I can stabilize this, but full repair needs hands-on work.",
        "I've done what I can. Here's who can take it from here."
    ],
    "cost_honest": [
        "Repair estimate: $X-Y. Replacement would cost around $Z.",
        "At this repair cost, you're at X% of device value. Here's my honest take.",
        "This might not be worth fixing. Let me show you why."
    ],
    "risk_honest": [
        "If we don't address this, here's what could happen.",
        "Doing nothing carries this risk: X.",
        "The safe move is Y. The faster move is Z. Your call."
    ]
}


def get_trust_phrase(category: str) -> str:
    """Get appropriate trust-building phrase"""
    import random
    phrases = TRUST_PHRASES.get(category, TRUST_PHRASES["uncertainty"])
    return random.choice(phrases)


# ═══════════════════════════════════════════════════════════════════════════════
# DOCTRINE ENFORCEMENT
# ═══════════════════════════════════════════════════════════════════════════════

def validate_session_outcome(outcome: SessionOutcome, report: OutcomeReport) -> Dict:
    """Validate that a session meets doctrine requirements"""
    issues = []
    
    # Check for incomplete outcome
    if outcome == SessionOutcome.INCOMPLETE:
        issues.append("❌ DOCTRINE VIOLATION: Session ended without clear outcome")
    
    # Check backup verification for risky operations
    if not report.backup_verified and any("red_line" in str(a) for a in report.audit_trail):
        issues.append("❌ DOCTRINE VIOLATION: Red-line operation without backup verification")
    
    # Check next steps are provided
    if outcome in [SessionOutcome.ESCALATED, SessionOutcome.DECISION_HELP]:
        if not report.next_steps:
            issues.append("❌ DOCTRINE VIOLATION: Escalation/Decision without clear next steps")
    
    # Check cost/time estimates for decision help
    if outcome == SessionOutcome.DECISION_HELP:
        if not report.cost_estimate:
            issues.append("⚠️ Missing cost estimate for decision help")
        if not report.time_estimate:
            issues.append("⚠️ Missing time estimate for decision help")
    
    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "outcome": outcome.value,
        "doctrine_compliant": len([i for i in issues if "VIOLATION" in i]) == 0
    }


# ═══════════════════════════════════════════════════════════════════════════════
# THE DOCTRINE — FINAL WORD
# ═══════════════════════════════════════════════════════════════════════════════

DOCTRINE = """
═══════════════════════════════════════════════════════════════════════════════
                         NOIZYLAB GENIUS DOCTRINE
═══════════════════════════════════════════════════════════════════════════════

                      TRUST IS THE PRODUCT.
                      Fixes are the bonus.

EVERY SESSION MUST END IN ONE OF FOUR OUTCOMES:
  ✅ FIXED      — Issue solved, logged, and verified
  ✅ STABILIZED — Damage stopped, safe until full repair  
  ✅ ESCALATED  — Clear next steps provided
  ✅ DECISION   — Repair vs replace with cost/risk/time

If the user ends thinking "idk what to do" — WE FAILED.

THE 25 GENIUSES ARE A WAR ROOM, NOT A WIDGET:
  • Multi-agent system consulting behind the scenes
  • One voice, many experts thinking
  • Persistent device memory — we never forget
  • Pattern recognition across all repairs
  • Continuous learning from every fix

SAFETY IS NON-NEGOTIABLE:
  • No destructive steps without plain-language warning
  • Backup verification before red-line operations
  • Dry-run option for risky procedures
  • Complete audit trail for every action
  • Double-confirm for red-line operations

WHEN WE HIT A WALL:
  • Clear escalation path with cost/time/risk
  • Honest "repair vs replace" analysis
  • No gaslighting. No pretending.
  • Grown-up, honest tech triage.

THIS IS THE LAW. THIS IS THE WAY.
═══════════════════════════════════════════════════════════════════════════════
"""

print(DOCTRINE)

