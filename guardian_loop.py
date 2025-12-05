# ROB OS - LAYER 4: GUARDIAN LOOP
# =================================
# Ongoing health checks, proactive protection, scheduled care
# "We adopted your tech" - lifetime guardian philosophy

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum

class DeviceStatus(Enum):
    STABLE = "stable"       # All good
    WATCH = "watch"         # Minor concerns, monitoring
    CRITICAL = "critical"   # Needs attention now
    OFFLINE = "offline"     # Can't reach
    RETIRING = "retiring"   # End of life, plan replacement

class CheckType(Enum):
    QUICK = "quick"         # Fast health check (< 1 min)
    STANDARD = "standard"   # Normal check (5-10 min)
    DEEP = "deep"           # Thorough scan (30+ min)

@dataclass
class Device:
    """A device under NOIZYLAB guardianship."""
    device_id: str
    name: str
    device_type: str  # "desktop", "laptop", "nas", "router", "mobile"
    role: str         # "Main Studio", "Archive", "Client Loaner"
    os: str
    status: DeviceStatus
    
    # Health metrics
    last_check: Optional[str] = None
    health_score: int = 100  # 0-100
    
    # Backup status
    backup_status: str = "unknown"  # "up_to_date", "stale", "none", "unknown"
    last_backup: Optional[str] = None
    
    # Issues
    active_issues: List[str] = field(default_factory=list)
    
    # Metadata
    notes: str = ""
    adopted_date: Optional[str] = None
    
    # Guardian settings
    autopilot_enabled: bool = True
    check_frequency: str = "daily"  # "hourly", "daily", "weekly", "manual"

@dataclass
class HealthCheck:
    """Result of a health check."""
    device_id: str
    check_type: CheckType
    timestamp: str
    
    # Results
    status: DeviceStatus
    health_score: int
    
    # Findings
    findings: List[Dict[str, Any]] = field(default_factory=list)
    issues_found: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    
    # Backup check
    backup_current: bool = True
    backup_age_days: int = 0

@dataclass
class Issue:
    """An issue detected on a device."""
    issue_id: str
    device_id: str
    severity: str  # "low", "medium", "high", "critical"
    title: str
    description: str
    detected_at: str
    
    # Status
    status: str = "open"  # "open", "acknowledged", "in_progress", "resolved", "snoozed"
    snoozed_until: Optional[str] = None
    
    # Resolution
    resolved_at: Optional[str] = None
    resolution_notes: str = ""

class GuardianLoop:
    """
    The Guardian Loop - Ongoing protection for all devices.
    "We adopted your tech."
    """
    
    def __init__(self):
        self.devices: Dict[str, Device] = {}
        self.issues: Dict[str, Issue] = {}
        self.check_history: List[HealthCheck] = []
        
        # Default check schedules
        self.check_schedules = {
            "hourly": timedelta(hours=1),
            "daily": timedelta(days=1),
            "weekly": timedelta(weeks=1),
            "manual": None
        }
        
        # Health score thresholds
        self.health_thresholds = {
            "stable": 80,
            "watch": 60,
            "critical": 40
        }
    
    def adopt_device(self, device_id: str, name: str, device_type: str,
                     role: str, os: str, notes: str = "") -> Device:
        """
        Adopt a new device into the Guardian Loop.
        This is the start of a lifetime relationship.
        """
        device = Device(
            device_id=device_id,
            name=name,
            device_type=device_type,
            role=role,
            os=os,
            status=DeviceStatus.STABLE,
            notes=notes,
            adopted_date=datetime.now().isoformat()
        )
        
        self.devices[device_id] = device
        return device
    
    def get_device(self, device_id: str) -> Optional[Device]:
        return self.devices.get(device_id)
    
    def get_all_devices(self) -> List[Device]:
        return list(self.devices.values())
    
    def run_health_check(self, device_id: str, 
                          check_type: CheckType = CheckType.STANDARD) -> HealthCheck:
        """
        Run a health check on a device.
        """
        device = self.devices.get(device_id)
        if not device:
            raise ValueError(f"Device {device_id} not found")
        
        # In real implementation, this would run actual diagnostics
        # For now, simulate a check
        
        findings = []
        issues_found = []
        recommendations = []
        health_score = 100
        
        # Simulate findings based on device status
        if device.backup_status == "stale":
            findings.append({
                "category": "backup",
                "finding": "Backup is stale",
                "severity": "medium"
            })
            issues_found.append("Backup has not run recently")
            recommendations.append("Run a full backup soon")
            health_score -= 15
        
        if device.backup_status == "none":
            findings.append({
                "category": "backup",
                "finding": "No backup configured",
                "severity": "high"
            })
            issues_found.append("No backup system in place")
            recommendations.append("Set up backup immediately")
            health_score -= 30
        
        # Determine status from health score
        if health_score >= self.health_thresholds["stable"]:
            status = DeviceStatus.STABLE
        elif health_score >= self.health_thresholds["watch"]:
            status = DeviceStatus.WATCH
        else:
            status = DeviceStatus.CRITICAL
        
        # Create check record
        check = HealthCheck(
            device_id=device_id,
            check_type=check_type,
            timestamp=datetime.now().isoformat(),
            status=status,
            health_score=health_score,
            findings=findings,
            issues_found=issues_found,
            recommendations=recommendations,
            backup_current=device.backup_status == "up_to_date",
            backup_age_days=0 if device.backup_status == "up_to_date" else 7
        )
        
        # Update device
        device.last_check = check.timestamp
        device.health_score = health_score
        device.status = status
        device.active_issues = issues_found
        
        # Create issues for any problems found
        for issue_desc in issues_found:
            self._create_issue(device_id, issue_desc, findings)
        
        # Store check history
        self.check_history.append(check)
        
        return check
    
    def _create_issue(self, device_id: str, description: str,
                       findings: List[Dict[str, Any]]) -> Issue:
        """Create an issue from a finding."""
        # Determine severity from findings
        severity = "low"
        for finding in findings:
            if finding.get("severity") == "critical":
                severity = "critical"
                break
            elif finding.get("severity") == "high" and severity != "critical":
                severity = "high"
            elif finding.get("severity") == "medium" and severity in ["low"]:
                severity = "medium"
        
        issue_id = f"{device_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        issue = Issue(
            issue_id=issue_id,
            device_id=device_id,
            severity=severity,
            title=description[:50],
            description=description,
            detected_at=datetime.now().isoformat()
        )
        
        self.issues[issue_id] = issue
        return issue
    
    def get_open_issues(self) -> List[Issue]:
        """Get all open issues across all devices."""
        return [i for i in self.issues.values() if i.status == "open"]
    
    def get_device_issues(self, device_id: str) -> List[Issue]:
        """Get all issues for a specific device."""
        return [i for i in self.issues.values() if i.device_id == device_id]
    
    def acknowledge_issue(self, issue_id: str) -> Issue:
        """Acknowledge an issue (user has seen it)."""
        issue = self.issues.get(issue_id)
        if issue:
            issue.status = "acknowledged"
        return issue
    
    def snooze_issue(self, issue_id: str, days: int = 7) -> Issue:
        """Snooze an issue for a number of days."""
        issue = self.issues.get(issue_id)
        if issue:
            issue.status = "snoozed"
            issue.snoozed_until = (datetime.now() + timedelta(days=days)).isoformat()
        return issue
    
    def resolve_issue(self, issue_id: str, notes: str = "") -> Issue:
        """Mark an issue as resolved."""
        issue = self.issues.get(issue_id)
        if issue:
            issue.status = "resolved"
            issue.resolved_at = datetime.now().isoformat()
            issue.resolution_notes = notes
        return issue
    
    def get_dashboard_summary(self) -> Dict[str, Any]:
        """
        Get a summary for the MC96 dashboard.
        """
        devices = self.get_all_devices()
        issues = self.get_open_issues()
        
        stable_count = sum(1 for d in devices if d.status == DeviceStatus.STABLE)
        watch_count = sum(1 for d in devices if d.status == DeviceStatus.WATCH)
        critical_count = sum(1 for d in devices if d.status == DeviceStatus.CRITICAL)
        
        # Determine overall status
        if critical_count > 0:
            overall_status = "critical"
            status_message = f"CRITICAL – {critical_count} device(s) need attention"
        elif watch_count > 0:
            overall_status = "watch"
            status_message = f"ATTENTION NEEDED – {watch_count} issue(s) to review"
        else:
            overall_status = "stable"
            status_message = "ALL SYSTEMS STABLE"
        
        return {
            "overall_status": overall_status,
            "status_message": status_message,
            "device_counts": {
                "total": len(devices),
                "stable": stable_count,
                "watch": watch_count,
                "critical": critical_count
            },
            "open_issues": len(issues),
            "critical_issues": sum(1 for i in issues if i.severity == "critical"),
            "devices": [
                {
                    "id": d.device_id,
                    "name": d.name,
                    "status": d.status.value,
                    "health_score": d.health_score,
                    "last_check": d.last_check
                }
                for d in devices
            ]
        }
    
    def get_autopilot_status(self) -> Dict[str, Any]:
        """Get the current autopilot configuration."""
        devices = self.get_all_devices()
        
        return {
            "global_enabled": True,
            "devices": [
                {
                    "id": d.device_id,
                    "name": d.name,
                    "autopilot_enabled": d.autopilot_enabled,
                    "check_frequency": d.check_frequency
                }
                for d in devices
            ],
            "safety_note": (
                "Autopilot will never erase your files or reformat drives. "
                "For anything destructive, it will always ask you first."
            )
        }


# Singleton instance
_guardian_loop = None

def get_guardian_loop() -> GuardianLoop:
    global _guardian_loop
    if _guardian_loop is None:
        _guardian_loop = GuardianLoop()
    return _guardian_loop

