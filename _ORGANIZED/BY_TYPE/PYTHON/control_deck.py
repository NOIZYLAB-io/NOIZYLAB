# backend_ultra/mc96/control_deck.py
# MC96 CONTROL DECK - YOUR MISSION CONTROL VIEW
# "Walk into the bridge of the ship" moment
# ═══════════════════════════════════════════════════════════════════════════════

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json

# ═══════════════════════════════════════════════════════════════════════════════
# DEVICE STATUS DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════════

class DeviceStatus(Enum):
    STABLE = "stable"       # 🟢 All good
    WATCH = "watch"         # 🟡 Needs attention soon
    CRITICAL = "critical"   # 🔴 Immediate attention
    OFFLINE = "offline"     # ⚪ Not connected
    RETIRE_SOON = "retire"  # 🟤 End of life approaching

class PerformanceLevel(Enum):
    SMOOTH = "smooth"
    STRAINED = "strained"
    CHOKING = "choking"

class BackupStatus(Enum):
    UP_TO_DATE = "up_to_date"
    STALE = "stale"
    NONE = "none"

class ThermalStatus(Enum):
    NORMAL = "normal"
    WARM = "warm"
    HOT = "hot"

# ═══════════════════════════════════════════════════════════════════════════════
# DEVICE TILE (What orbits the hologram)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class DeviceTile:
    """A device tile that orbits the NOIZY hologram."""
    id: str
    name: str
    role: str  # e.g., "Main Workstation", "Backup Node", "Creative Rig"
    device_type: str  # e.g., "M2 Ultra Mac", "Windows Laptop", "NAS"
    os: str
    status: DeviceStatus = DeviceStatus.STABLE
    last_check: datetime = None
    risk_badges: List[str] = field(default_factory=list)  # e.g., ["Aging HDD", "No backup"]
    
    # Snapshot data
    performance: PerformanceLevel = PerformanceLevel.SMOOTH
    storage_percent: float = 0.0
    thermals: ThermalStatus = ThermalStatus.NORMAL
    backup_status: BackupStatus = BackupStatus.UP_TO_DATE
    
    # Top insights
    insights: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if self.last_check is None:
            self.last_check = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "device_type": self.device_type,
            "os": self.os,
            "status": self.status.value,
            "status_emoji": self._get_status_emoji(),
            "last_check": self.last_check.isoformat() if self.last_check else None,
            "last_check_human": self._humanize_time(),
            "risk_badges": self.risk_badges,
            "snapshot": {
                "performance": self.performance.value,
                "storage_percent": self.storage_percent,
                "storage_status": self._get_storage_status(),
                "thermals": self.thermals.value,
                "backup_status": self.backup_status.value
            },
            "insights": self.insights[:3]  # Top 3 only
        }
    
    def _get_status_emoji(self) -> str:
        emoji_map = {
            DeviceStatus.STABLE: "🟢",
            DeviceStatus.WATCH: "🟡",
            DeviceStatus.CRITICAL: "🔴",
            DeviceStatus.OFFLINE: "⚪",
            DeviceStatus.RETIRE_SOON: "🟤"
        }
        return emoji_map.get(self.status, "⚪")
    
    def _get_storage_status(self) -> str:
        if self.storage_percent < 70:
            return "Good"
        elif self.storage_percent < 85:
            return "Getting full"
        else:
            return "Critical"
    
    def _humanize_time(self) -> str:
        if not self.last_check:
            return "Never"
        delta = datetime.now() - self.last_check
        if delta.seconds < 3600:
            return f"{delta.seconds // 60} minutes ago"
        elif delta.seconds < 86400:
            return f"{delta.seconds // 3600} hours ago"
        else:
            return f"{delta.days} days ago"

# ═══════════════════════════════════════════════════════════════════════════════
# GLOBAL STATUS (Top bar)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class GlobalStatus:
    """The top bar status pill."""
    critical_count: int = 0
    watch_count: int = 0
    stable_count: int = 0
    offline_count: int = 0
    
    @property
    def status_text(self) -> str:
        if self.critical_count > 0:
            parts = []
            if self.critical_count > 0:
                parts.append(f"{self.critical_count} CRITICAL")
            if self.watch_count > 0:
                parts.append(f"{self.watch_count} WATCH")
            return f"ATTENTION: {' • '.join(parts)}"
        elif self.watch_count > 0:
            return f"WATCH: {self.watch_count} item{'s' if self.watch_count > 1 else ''} need attention"
        else:
            return "ALL SYSTEMS STABLE"
    
    @property
    def status_color(self) -> str:
        if self.critical_count > 0:
            return "red"
        elif self.watch_count > 0:
            return "yellow"
        else:
            return "green"

# ═══════════════════════════════════════════════════════════════════════════════
# ISSUE ITEM (For the Issues Drawer)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class IssueItem:
    """An issue in the global issues drawer."""
    id: str
    device_id: str
    device_name: str
    severity: str  # "critical", "watch"
    title: str
    description: str
    recommendation: str
    snoozed_until: datetime = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "device_id": self.device_id,
            "device_name": self.device_name,
            "severity": self.severity,
            "severity_emoji": "🔴" if self.severity == "critical" else "🟡",
            "title": self.title,
            "description": self.description,
            "recommendation": self.recommendation,
            "is_snoozed": self.snoozed_until is not None and self.snoozed_until > datetime.now(),
            "snoozed_until": self.snoozed_until.isoformat() if self.snoozed_until else None
        }

# ═══════════════════════════════════════════════════════════════════════════════
# MC96 CONTROL DECK
# ═══════════════════════════════════════════════════════════════════════════════

class MC96ControlDeck:
    """
    The MC96 Mission Control - your "walk into the bridge" moment.
    
    Layout:
    - Top Bar: Status pill + navigation
    - Center: Hologram + orbiting device tiles
    - Left: Issues drawer
    - Right: Side panel (device detail)
    """
    
    def __init__(self):
        self.devices: Dict[str, DeviceTile] = {}
        self.issues: List[IssueItem] = []
        self.global_status = GlobalStatus()
        self.last_autopilot_summary: str = None
        self.last_autopilot_time: datetime = None
    
    def add_device(self, device: DeviceTile):
        """Add a device to the control deck."""
        self.devices[device.id] = device
        self._recalculate_global_status()
    
    def remove_device(self, device_id: str):
        """Remove a device from the control deck."""
        if device_id in self.devices:
            del self.devices[device_id]
            self._recalculate_global_status()
    
    def update_device_status(self, device_id: str, status: DeviceStatus, insights: List[str] = None):
        """Update a device's status."""
        if device_id in self.devices:
            self.devices[device_id].status = status
            if insights:
                self.devices[device_id].insights = insights
            self.devices[device_id].last_check = datetime.now()
            self._recalculate_global_status()
    
    def add_issue(self, issue: IssueItem):
        """Add an issue to the issues drawer."""
        self.issues.append(issue)
        self._recalculate_global_status()
    
    def snooze_issue(self, issue_id: str, snooze_days: int = 1):
        """Snooze an issue for a number of days."""
        for issue in self.issues:
            if issue.id == issue_id:
                issue.snoozed_until = datetime.now() + timedelta(days=snooze_days)
                break
    
    def resolve_issue(self, issue_id: str):
        """Mark an issue as resolved."""
        self.issues = [i for i in self.issues if i.id != issue_id]
        self._recalculate_global_status()
    
    def _recalculate_global_status(self):
        """Recalculate the global status based on all devices and issues."""
        self.global_status = GlobalStatus(
            critical_count=sum(1 for d in self.devices.values() if d.status == DeviceStatus.CRITICAL),
            watch_count=sum(1 for d in self.devices.values() if d.status == DeviceStatus.WATCH),
            stable_count=sum(1 for d in self.devices.values() if d.status == DeviceStatus.STABLE),
            offline_count=sum(1 for d in self.devices.values() if d.status == DeviceStatus.OFFLINE)
        )
    
    def get_dashboard_state(self) -> Dict[str, Any]:
        """Get the complete dashboard state for rendering."""
        active_issues = [i for i in self.issues if not i.snoozed_until or i.snoozed_until <= datetime.now()]
        
        return {
            "global_status": {
                "text": self.global_status.status_text,
                "color": self.global_status.status_color,
                "counts": {
                    "critical": self.global_status.critical_count,
                    "watch": self.global_status.watch_count,
                    "stable": self.global_status.stable_count,
                    "offline": self.global_status.offline_count
                }
            },
            "devices": [d.to_dict() for d in self.devices.values()],
            "issues": [i.to_dict() for i in active_issues],
            "issue_count": len(active_issues),
            "hologram_state": self._get_hologram_state(),
            "autopilot": {
                "last_summary": self.last_autopilot_summary,
                "last_time": self.last_autopilot_time.isoformat() if self.last_autopilot_time else None
            }
        }
    
    def _get_hologram_state(self) -> Dict[str, Any]:
        """Get the state for the NOIZY hologram."""
        if self.global_status.critical_count > 0:
            return {
                "mode": "alert",
                "animation": "pulse_red",
                "message": "Critical issues need attention"
            }
        elif self.global_status.watch_count > 0:
            return {
                "mode": "attention",
                "animation": "pulse_amber",
                "message": "Some items to review when you have time"
            }
        else:
            return {
                "mode": "calm",
                "animation": "slow_spin",
                "message": "All systems stable. Go make cool stuff."
            }
    
    def get_device_detail(self, device_id: str) -> Dict[str, Any]:
        """Get detailed information for a specific device (side panel)."""
        if device_id not in self.devices:
            return None
        
        device = self.devices[device_id]
        device_issues = [i for i in self.issues if i.device_id == device_id]
        
        return {
            "device": device.to_dict(),
            "issues": [i.to_dict() for i in device_issues],
            "actions": [
                {"id": "quick_fix", "label": "☕ Quick Espresso Fix", "type": "primary"},
                {"id": "deep_dive", "label": "🛠 Deep Dive Repair", "type": "secondary"},
                {"id": "crisis", "label": "🧯 Crisis / Not Booting", "type": "danger"},
                {"id": "plan", "label": "🧭 Plan Upgrades & Future", "type": "tertiary"}
            ],
            "history_available": True,
            "autopilot_rules_available": True
        }
    
    def get_morning_summary(self) -> str:
        """Get the calm morning summary - what you see when you sit down."""
        if self.global_status.critical_count > 0:
            return f"Heads up: {self.global_status.critical_count} critical issue{'s' if self.global_status.critical_count > 1 else ''} need your attention."
        elif self.global_status.watch_count > 0:
            return f"Things are mostly good. {self.global_status.watch_count} item{'s' if self.global_status.watch_count > 1 else ''} to review when you have time."
        else:
            return "ALL SYSTEMS STABLE – NOTHING NEEDS YOU TODAY.\n\nLast night I checked backups on all devices. All good. You're clear."

# ═══════════════════════════════════════════════════════════════════════════════
# AUTOPILOT CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

class AutopilotMode(Enum):
    CHILL = "chill"        # Monitor + safe cleanups, minimal alerts
    HELPER = "helper"      # Also runs low-risk fixes automatically
    PARANOID = "paranoid"  # Ultra-serious about safety, lots of early warnings

@dataclass
class AutopilotConfig:
    """Configuration for a device's autopilot."""
    device_id: str
    enabled: bool = True
    mode: AutopilotMode = AutopilotMode.HELPER
    
    # What autopilot can do
    can_run_health_checks: bool = True
    can_clean_safe_junk: bool = True
    can_optimize_startup: bool = True
    can_monitor_temps: bool = True
    can_check_backups: bool = True
    
    # What autopilot can NEVER do
    can_delete_files: bool = False  # NEVER
    can_format_drives: bool = False  # NEVER
    can_change_partitions: bool = False  # NEVER
    can_reinstall_os: bool = False  # NEVER

AUTOPILOT_SAFETY_RULES = """
Autopilot will NEVER:
• Erase your files
• Reformat drives
• Change partitions
• Reinstall your operating system

For anything destructive, it will ALWAYS ask you first.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# INSTANTIATE CONTROL DECK
# ═══════════════════════════════════════════════════════════════════════════════

MC96_DECK = MC96ControlDeck()

# Add example devices
from datetime import timedelta

MC96_DECK.add_device(DeviceTile(
    id="gabriel",
    name="GABRIEL",
    role="Main Studio Workstation",
    device_type="M2 Ultra Mac Studio",
    os="macOS Sonoma",
    status=DeviceStatus.STABLE,
    performance=PerformanceLevel.SMOOTH,
    storage_percent=72,
    thermals=ThermalStatus.NORMAL,
    backup_status=BackupStatus.UP_TO_DATE,
    insights=[
        "Drive health normal, no failure patterns detected.",
        "Startup time optimal.",
        "Last full backup: 2 hours ago. ✓"
    ]
))

MC96_DECK.add_device(DeviceTile(
    id="hp_omen",
    name="HP-OMEN",
    role="Windows Gaming/Dev Machine",
    device_type="HP OMEN Desktop",
    os="Windows 11",
    status=DeviceStatus.STABLE,
    performance=PerformanceLevel.SMOOTH,
    storage_percent=45,
    thermals=ThermalStatus.NORMAL,
    backup_status=BackupStatus.UP_TO_DATE,
    insights=[
        "All systems nominal.",
        "GPU temps within safe range.",
        "Last backup: 6 hours ago. ✓"
    ]
))

