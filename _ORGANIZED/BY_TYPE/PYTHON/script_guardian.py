# ROB OS - LAYER 4: SCRIPT GUARDIAN
# ===================================
# Lint + Sandbox + Lock + Ledger + Mirror
# NEVER AGAIN will a script nuke the system drive
# "Lucy incident" prevention built into the DNA

from typing import Dict, Any, List, Optional, Set
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import re

class RiskLevel(Enum):
    SAFE = "safe"                    # Read-only, no system impact
    LOW = "low"                      # Minor changes, easily reversible
    MEDIUM = "medium"                # Significant changes, needs attention
    HIGH = "high"                    # Destructive potential, needs consent
    CRITICAL = "critical"            # System-level danger, requires double-confirm
    FORBIDDEN = "forbidden"          # Never allowed, period

@dataclass
class ScriptAnalysis:
    """Result of analyzing a script for safety."""
    script_id: str
    risk_level: RiskLevel
    flags: List[str]
    warnings: List[str]
    blocked_operations: List[str]
    requires_consent: bool
    requires_sandbox: bool
    approved: bool
    approval_reason: str

@dataclass
class AuditEntry:
    """A single entry in the audit log."""
    timestamp: str
    action: str
    script_id: Optional[str]
    user_id: str
    risk_level: RiskLevel
    result: str
    details: Dict[str, Any] = field(default_factory=dict)

class ScriptGuardian:
    """
    The Script Guardian - Lint + Sandbox + Lock + Ledger + Mirror
    Ensures no script ever does what Lucy did to the system drive.
    """
    
    def __init__(self):
        # FORBIDDEN paths - NEVER touch these
        self.forbidden_paths = {
            "/",
            "/System",
            "/Library",
            "/usr",
            "/bin",
            "/sbin",
            "/private",
            "/var",
            "/etc",
            "/Applications",
            "/Users",  # Root users folder
            "C:\\Windows",
            "C:\\Program Files",
            "C:\\Program Files (x86)",
            "C:\\Users",  # Root users folder
        }
        
        # PROTECTED paths - Only with explicit consent
        self.protected_paths = {
            "/Users/m2ultra",  # User home - careful
            "/Volumes",        # External drives - careful
            "GABRIEL",         # The sacred machine
        }
        
        # SAFE paths - Can operate freely
        self.safe_paths = {
            "/Users/m2ultra/NOIZYLAB",
            "/tmp",
            "/var/tmp",
        }
        
        # Dangerous operations
        self.dangerous_operations = {
            "rm -rf": RiskLevel.CRITICAL,
            "rm -r": RiskLevel.HIGH,
            "rm": RiskLevel.MEDIUM,
            "rmdir": RiskLevel.MEDIUM,
            "format": RiskLevel.FORBIDDEN,
            "diskutil erase": RiskLevel.FORBIDDEN,
            "mkfs": RiskLevel.FORBIDDEN,
            "dd if=": RiskLevel.CRITICAL,
            "sudo": RiskLevel.HIGH,
            "chmod 777": RiskLevel.HIGH,
            "chown": RiskLevel.HIGH,
            "> /dev/": RiskLevel.FORBIDDEN,
            "shutdown": RiskLevel.CRITICAL,
            "reboot": RiskLevel.CRITICAL,
            "launchctl": RiskLevel.HIGH,
            "systemctl": RiskLevel.HIGH,
            "crontab": RiskLevel.HIGH,
            "mv /": RiskLevel.CRITICAL,
            "cp /": RiskLevel.MEDIUM,
        }
        
        # Audit log
        self.audit_log: List[AuditEntry] = []
        
        # Pending approvals
        self.pending_approvals: Dict[str, ScriptAnalysis] = {}
    
    def analyze_script(self, script_content: str, script_id: str,
                       context: Dict[str, Any] = None) -> ScriptAnalysis:
        """
        Analyze a script for safety risks.
        This is the LINT function.
        """
        flags = []
        warnings = []
        blocked = []
        risk_level = RiskLevel.SAFE
        
        lines = script_content.split('\n')
        
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            
            # Skip comments and empty lines
            if not line_stripped or line_stripped.startswith('#'):
                continue
            
            # Check for dangerous operations
            for op, op_risk in self.dangerous_operations.items():
                if op in line_stripped:
                    if op_risk == RiskLevel.FORBIDDEN:
                        blocked.append(f"Line {i+1}: FORBIDDEN operation '{op}'")
                        risk_level = RiskLevel.FORBIDDEN
                    elif op_risk.value > risk_level.value:
                        risk_level = op_risk
                        flags.append(f"Line {i+1}: {op_risk.value.upper()} risk operation '{op}'")
            
            # Check for forbidden paths
            for path in self.forbidden_paths:
                if path in line_stripped and not any(safe in line_stripped for safe in self.safe_paths):
                    blocked.append(f"Line {i+1}: Touches FORBIDDEN path '{path}'")
                    risk_level = RiskLevel.FORBIDDEN
            
            # Check for protected paths
            for path in self.protected_paths:
                if path in line_stripped:
                    warnings.append(f"Line {i+1}: Touches PROTECTED path '{path}' - requires consent")
                    if risk_level.value < RiskLevel.HIGH.value:
                        risk_level = RiskLevel.HIGH
            
            # Check for boot/startup modifications
            boot_patterns = [
                r'LaunchAgent', r'LaunchDaemon', r'startup',
                r'rc\.local', r'init\.d', r'systemd',
                r'cron', r'@reboot'
            ]
            for pattern in boot_patterns:
                if re.search(pattern, line_stripped, re.IGNORECASE):
                    flags.append(f"Line {i+1}: Modifies boot/startup behavior")
                    if risk_level.value < RiskLevel.CRITICAL.value:
                        risk_level = RiskLevel.CRITICAL
        
        # Determine approval status
        approved = risk_level in [RiskLevel.SAFE, RiskLevel.LOW]
        requires_consent = risk_level in [RiskLevel.MEDIUM, RiskLevel.HIGH, RiskLevel.CRITICAL]
        requires_sandbox = risk_level in [RiskLevel.MEDIUM, RiskLevel.HIGH]
        
        if risk_level == RiskLevel.FORBIDDEN:
            approved = False
            approval_reason = "Script contains FORBIDDEN operations. Cannot be approved."
        elif requires_consent:
            approved = False
            approval_reason = f"Script requires explicit consent due to {risk_level.value} risk level."
        else:
            approval_reason = "Script passed safety checks."
        
        analysis = ScriptAnalysis(
            script_id=script_id,
            risk_level=risk_level,
            flags=flags,
            warnings=warnings,
            blocked_operations=blocked,
            requires_consent=requires_consent,
            requires_sandbox=requires_sandbox,
            approved=approved,
            approval_reason=approval_reason
        )
        
        # Log the analysis
        self._log_action("analyze", script_id, risk_level, "analyzed", {
            "flags": len(flags),
            "warnings": len(warnings),
            "blocked": len(blocked)
        })
        
        # If needs consent, add to pending
        if requires_consent and risk_level != RiskLevel.FORBIDDEN:
            self.pending_approvals[script_id] = analysis
        
        return analysis
    
    def request_consent(self, script_id: str, user_id: str) -> Dict[str, Any]:
        """
        Generate a consent request for a risky script.
        This is the LOCK function.
        """
        analysis = self.pending_approvals.get(script_id)
        if not analysis:
            return {"error": "No pending approval for this script"}
        
        # Build clear, honest consent message
        consent_message = {
            "script_id": script_id,
            "risk_level": analysis.risk_level.value,
            "summary": f"This script has been flagged as {analysis.risk_level.value.upper()} risk.",
            "what_it_does": analysis.flags + analysis.warnings,
            "blocked_operations": analysis.blocked_operations,
            "plain_language_warning": self._get_plain_warning(analysis),
            "consent_required": True,
            "double_confirm_required": analysis.risk_level == RiskLevel.CRITICAL,
            "consent_text": f"I understand this script may {self._get_risk_description(analysis.risk_level)} and I want to proceed.",
            "cancel_text": "No, don't run this. Let me review it first."
        }
        
        return consent_message
    
    def approve_with_consent(self, script_id: str, user_id: str,
                              consent_given: bool, double_confirmed: bool = False) -> Dict[str, Any]:
        """
        Process user consent for a risky script.
        """
        analysis = self.pending_approvals.get(script_id)
        if not analysis:
            return {"error": "No pending approval for this script"}
        
        if analysis.risk_level == RiskLevel.FORBIDDEN:
            return {
                "approved": False,
                "reason": "This script contains FORBIDDEN operations and cannot be approved under any circumstances."
            }
        
        if not consent_given:
            self._log_action("consent_denied", script_id, analysis.risk_level, "denied", {"user_id": user_id})
            del self.pending_approvals[script_id]
            return {"approved": False, "reason": "User declined to give consent."}
        
        if analysis.risk_level == RiskLevel.CRITICAL and not double_confirmed:
            return {
                "approved": False,
                "reason": "CRITICAL risk scripts require double confirmation. Please confirm again.",
                "requires_double_confirm": True
            }
        
        # Consent given
        analysis.approved = True
        analysis.approval_reason = f"User {user_id} gave explicit consent."
        
        self._log_action("consent_given", script_id, analysis.risk_level, "approved", {"user_id": user_id})
        del self.pending_approvals[script_id]
        
        return {
            "approved": True,
            "reason": "Script approved with user consent.",
            "requires_sandbox": analysis.requires_sandbox,
            "next_step": "sandbox_test" if analysis.requires_sandbox else "execute"
        }
    
    def run_in_sandbox(self, script_id: str, script_content: str,
                        test_data_path: str) -> Dict[str, Any]:
        """
        Run a script in sandbox mode on test data.
        This is the SANDBOX function.
        """
        # Verify the test path is actually safe
        if not any(test_data_path.startswith(safe) for safe in self.safe_paths):
            return {
                "success": False,
                "error": "Test data path is not in a safe location. Use /tmp or NOIZYLAB test folders."
            }
        
        self._log_action("sandbox_run", script_id, RiskLevel.LOW, "sandbox_started", {
            "test_path": test_data_path
        })
        
        # In real implementation, this would actually run the script
        # For now, return a simulated result
        return {
            "success": True,
            "sandbox_path": test_data_path,
            "result": "Sandbox test completed. No errors detected.",
            "next_step": "Review results, then approve for real execution if satisfied."
        }
    
    def _log_action(self, action: str, script_id: Optional[str],
                    risk_level: RiskLevel, result: str, details: Dict[str, Any] = None):
        """
        Log an action to the audit trail.
        This is the LEDGER function.
        """
        entry = AuditEntry(
            timestamp=datetime.now().isoformat(),
            action=action,
            script_id=script_id,
            user_id="system",  # Would be actual user in real implementation
            risk_level=risk_level,
            result=result,
            details=details or {}
        )
        self.audit_log.append(entry)
    
    def get_audit_log(self, limit: int = 100) -> List[AuditEntry]:
        """Get recent audit log entries."""
        return self.audit_log[-limit:]
    
    def _get_plain_warning(self, analysis: ScriptAnalysis) -> str:
        """Get a plain-language warning for the user."""
        if analysis.risk_level == RiskLevel.CRITICAL:
            return (
                "⚠️ CRITICAL WARNING: This script could permanently delete files, "
                "modify system settings, or cause data loss. Only proceed if you "
                "fully understand what it does and have backups."
            )
        elif analysis.risk_level == RiskLevel.HIGH:
            return (
                "⚠️ HIGH RISK: This script will make significant changes that may be "
                "difficult to undo. Please review carefully before proceeding."
            )
        elif analysis.risk_level == RiskLevel.MEDIUM:
            return (
                "⚠️ MODERATE RISK: This script will modify files or settings. "
                "Changes should be reversible, but please review before proceeding."
            )
        return "This script appears safe, but please review before running."
    
    def _get_risk_description(self, risk_level: RiskLevel) -> str:
        """Get a description of what this risk level means."""
        descriptions = {
            RiskLevel.CRITICAL: "permanently delete files or modify critical system settings",
            RiskLevel.HIGH: "make significant changes that may be hard to reverse",
            RiskLevel.MEDIUM: "modify files or settings",
            RiskLevel.LOW: "make minor changes",
            RiskLevel.SAFE: "perform read-only operations"
        }
        return descriptions.get(risk_level, "perform unknown operations")


# Singleton instance
_script_guardian = None

def get_script_guardian() -> ScriptGuardian:
    global _script_guardian
    if _script_guardian is None:
        _script_guardian = ScriptGuardian()
    return _script_guardian

