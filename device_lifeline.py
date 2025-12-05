"""
═══════════════════════════════════════════════════════════════════════════════
                         DEVICE LIFELINE
═══════════════════════════════════════════════════════════════════════════════

Not: "We fixed your laptop."
But: "We adopted your tech."

Each device gets a LIFETIME of care.
Origin. History. Lifeline status.

NOIZYLAB becomes a calm voice over the entire lifespan of their gear.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime, date
from enum import Enum


class LifelineStatus(Enum):
    """The current status of a device's lifeline"""
    THRIVING = "thriving"              # Healthy, well-maintained
    STABLE = "stable"                  # Good condition, minor concerns
    AGING_GRACEFULLY = "aging"         # Old but reliable
    NEEDS_ATTENTION = "attention"      # Issues developing
    KEEP_BUT_WATCH = "watch"           # "Keep but don't trust"
    RETIREMENT_SOON = "retirement"     # Time to plan replacement
    LEGACY_HERO = "legacy"             # Retired with honors


class DeviceRole(Enum):
    """What role does this device play in their life"""
    PRIMARY_WORK = "primary_work"
    SECONDARY_WORK = "secondary_work"
    SCHOOL = "school"
    CREATIVE = "creative"              # Music, art, video
    FAMILY_SHARED = "family_shared"
    KIDS = "kids"
    ELDER_USE = "elder_use"
    BUSINESS_CRITICAL = "business"
    MEMORIES_KEEPER = "memories"       # Photos, videos, legacy
    GAMING = "gaming"
    CASUAL = "casual"


@dataclass
class DeviceOrigin:
    """The origin story of a device"""
    acquired_date: Optional[date]
    acquired_how: str                  # "New", "Refurbished", "Gift", "Inherited"
    original_owner: str
    original_purpose: str              # "School laptop", "Music production", etc.
    purchase_price: Optional[float]
    warranty_end: Optional[date]
    story: str                         # Free-form origin story


@dataclass
class LifeEvent:
    """A significant event in the device's life"""
    date: datetime
    event_type: str                    # "crash", "upgrade", "repair", "move", "owner_change"
    description: str
    severity: str                      # "minor", "moderate", "major", "critical"
    resolved: bool
    resolution: Optional[str]
    genius_involved: Optional[str]
    emotional_impact: str              # "scary", "frustrating", "relief", "neutral"


@dataclass
class DeviceLifeline:
    """
    The complete lifeline of a device.
    
    This is their tech's biography — from birth to retirement.
    """
    
    # Identity
    device_id: str
    nickname: Optional[str]            # "Dad's old MacBook", "The Beast"
    device_type: str
    make: str
    model: str
    year: int
    serial: Optional[str]
    
    # Origin
    origin: DeviceOrigin
    
    # Current state
    current_owner: str
    current_role: DeviceRole
    lifeline_status: LifelineStatus
    health_score: int                  # 0-100
    
    # History
    life_events: List[LifeEvent] = field(default_factory=list)
    owners_history: List[Dict] = field(default_factory=list)
    locations_history: List[str] = field(default_factory=list)
    
    # Care
    last_checkup: Optional[datetime] = None
    next_recommended_checkup: Optional[datetime] = None
    known_quirks: List[str] = field(default_factory=list)
    red_flags: List[str] = field(default_factory=list)
    
    # Emotional context
    sentimental_value: str = "normal"  # "normal", "high", "irreplaceable"
    what_matters_most: List[str] = field(default_factory=list)  # "photos", "music projects", etc.
    
    # NOIZYLAB relationship
    first_seen_by_noizy: Optional[datetime] = None
    total_sessions: int = 0
    total_repairs: int = 0
    relationship_duration_days: int = 0
    
    def add_life_event(
        self, 
        event_type: str, 
        description: str, 
        severity: str = "minor",
        resolved: bool = True,
        resolution: str = None,
        genius: str = None,
        emotional_impact: str = "neutral"
    ):
        """Add a life event to this device's history"""
        event = LifeEvent(
            date=datetime.now(),
            event_type=event_type,
            description=description,
            severity=severity,
            resolved=resolved,
            resolution=resolution,
            genius_involved=genius,
            emotional_impact=emotional_impact
        )
        self.life_events.append(event)
        
        # Update health score based on severity
        if severity == "critical" and not resolved:
            self.health_score = max(0, self.health_score - 30)
        elif severity == "major" and not resolved:
            self.health_score = max(0, self.health_score - 15)
        
        # Update lifeline status
        self._update_lifeline_status()
    
    def _update_lifeline_status(self):
        """Update lifeline status based on current state"""
        age = datetime.now().year - self.year
        
        if self.health_score >= 85 and age < 3:
            self.lifeline_status = LifelineStatus.THRIVING
        elif self.health_score >= 70:
            self.lifeline_status = LifelineStatus.STABLE
        elif self.health_score >= 50 and age >= 5:
            self.lifeline_status = LifelineStatus.AGING_GRACEFULLY
        elif self.health_score >= 50:
            self.lifeline_status = LifelineStatus.NEEDS_ATTENTION
        elif self.health_score >= 30:
            self.lifeline_status = LifelineStatus.KEEP_BUT_WATCH
        else:
            self.lifeline_status = LifelineStatus.RETIREMENT_SOON
    
    def get_lifeline_message(self) -> str:
        """Get a human-friendly lifeline status message"""
        messages = {
            LifelineStatus.THRIVING: 
                "This device is in excellent health. Keep doing what you're doing!",
            LifelineStatus.STABLE: 
                "Solid and reliable. A few things to watch, but nothing urgent.",
            LifelineStatus.AGING_GRACEFULLY: 
                "It's getting older, but it's earned its stripes. Still trustworthy for daily use.",
            LifelineStatus.NEEDS_ATTENTION: 
                "Some issues are developing. Let's address them before they become problems.",
            LifelineStatus.KEEP_BUT_WATCH: 
                "Keep using it, but don't trust it with anything irreplaceable without backup.",
            LifelineStatus.RETIREMENT_SOON: 
                "It's served you well. Let's start planning a peaceful transition.",
            LifelineStatus.LEGACY_HERO: 
                "Retired with honors. Its data lives on safely."
        }
        return messages.get(self.lifeline_status, "Status unknown.")
    
    def get_replacement_guidance(self) -> Dict:
        """Get guidance on replacement timing"""
        age = datetime.now().year - self.year
        
        if self.lifeline_status in [LifelineStatus.THRIVING, LifelineStatus.STABLE]:
            urgency = "none"
            message = "No need to think about replacement yet."
            timeline = "2+ years"
        elif self.lifeline_status == LifelineStatus.AGING_GRACEFULLY:
            urgency = "low"
            message = "Start thinking about what comes next, but no rush."
            timeline = "12-24 months"
        elif self.lifeline_status == LifelineStatus.NEEDS_ATTENTION:
            urgency = "moderate"
            message = "Worth researching options. This one has some life left, but plan ahead."
            timeline = "6-12 months"
        elif self.lifeline_status == LifelineStatus.KEEP_BUT_WATCH:
            urgency = "elevated"
            message = "Keep backups current. When you're ready, we'll help you transition smoothly."
            timeline = "3-6 months"
        else:
            urgency = "high"
            message = "It's time. Let's find you something that fits your needs and budget."
            timeline = "Soon"
        
        return {
            "urgency": urgency,
            "message": message,
            "suggested_timeline": timeline,
            "device_age": age,
            "health_score": self.health_score,
            "sentimental_value": self.sentimental_value,
            "what_to_preserve": self.what_matters_most
        }
    
    def generate_story_intro(self) -> str:
        """Generate a story-mode intro for this device"""
        age = datetime.now().year - self.year
        
        if self.nickname:
            intro = f'"{self.nickname}" — a {self.make} {self.model}'
        else:
            intro = f"A {self.make} {self.model}"
        
        if self.origin.acquired_how == "Gift":
            intro += f", given as a gift"
        elif self.origin.acquired_how == "Inherited":
            intro += f", inherited with love"
        
        if age == 0:
            intro += ", brand new this year."
        elif age == 1:
            intro += ", just a year old."
        elif age < 4:
            intro += f", {age} years young."
        elif age < 7:
            intro += f", a seasoned {age}-year veteran."
        else:
            intro += f", a {age}-year-old legend."
        
        if self.current_role == DeviceRole.MEMORIES_KEEPER:
            intro += " It holds irreplaceable memories."
        elif self.current_role == DeviceRole.CREATIVE:
            intro += " It's been a creative companion."
        elif self.current_role == DeviceRole.BUSINESS_CRITICAL:
            intro += " It's the backbone of a business."
        
        return intro
    
    def to_passport(self) -> Dict:
        """Generate a Tech Passport for this device"""
        return {
            "device": {
                "nickname": self.nickname,
                "type": self.device_type,
                "make": self.make,
                "model": self.model,
                "year": self.year,
                "serial": self.serial
            },
            "health": {
                "score": self.health_score,
                "status": self.lifeline_status.value,
                "message": self.get_lifeline_message()
            },
            "origin": {
                "acquired": self.origin.acquired_date.isoformat() if self.origin.acquired_date else None,
                "how": self.origin.acquired_how,
                "original_purpose": self.origin.original_purpose,
                "story": self.origin.story
            },
            "history": {
                "total_events": len(self.life_events),
                "major_events": [e.__dict__ for e in self.life_events if e.severity in ["major", "critical"]],
                "owners": len(self.owners_history)
            },
            "care": {
                "last_checkup": self.last_checkup.isoformat() if self.last_checkup else None,
                "next_checkup": self.next_recommended_checkup.isoformat() if self.next_recommended_checkup else None,
                "known_quirks": self.known_quirks,
                "red_flags": self.red_flags
            },
            "relationship": {
                "first_seen": self.first_seen_by_noizy.isoformat() if self.first_seen_by_noizy else None,
                "sessions": self.total_sessions,
                "repairs": self.total_repairs,
                "days_together": self.relationship_duration_days
            },
            "guidance": self.get_replacement_guidance(),
            "generated": datetime.now().isoformat(),
            "generated_by": "NOIZYLAB"
        }


# ═══════════════════════════════════════════════════════════════════════════════
# LIFELINE MANAGER
# ═══════════════════════════════════════════════════════════════════════════════

class LifelineManager:
    """Manages all device lifelines"""
    
    def __init__(self):
        self.lifelines: Dict[str, DeviceLifeline] = {}
    
    def create_lifeline(
        self,
        device_id: str,
        device_type: str,
        make: str,
        model: str,
        year: int,
        owner: str,
        role: DeviceRole,
        origin_story: str = None
    ) -> DeviceLifeline:
        """Create a new device lifeline"""
        
        origin = DeviceOrigin(
            acquired_date=None,
            acquired_how="Unknown",
            original_owner=owner,
            original_purpose=role.value,
            purchase_price=None,
            warranty_end=None,
            story=origin_story or f"A {make} {model} that found its way to NOIZYLAB."
        )
        
        lifeline = DeviceLifeline(
            device_id=device_id,
            nickname=None,
            device_type=device_type,
            make=make,
            model=model,
            year=year,
            serial=None,
            origin=origin,
            current_owner=owner,
            current_role=role,
            lifeline_status=LifelineStatus.STABLE,
            health_score=75,
            first_seen_by_noizy=datetime.now(),
            total_sessions=1
        )
        
        self.lifelines[device_id] = lifeline
        return lifeline
    
    def get_lifeline(self, device_id: str) -> Optional[DeviceLifeline]:
        """Get a device's lifeline"""
        return self.lifelines.get(device_id)
    
    def update_health(self, device_id: str, new_score: int, reason: str):
        """Update a device's health score"""
        lifeline = self.lifelines.get(device_id)
        if lifeline:
            old_score = lifeline.health_score
            lifeline.health_score = max(0, min(100, new_score))
            lifeline.add_life_event(
                event_type="health_change",
                description=f"Health changed from {old_score} to {new_score}: {reason}",
                severity="minor" if abs(new_score - old_score) < 20 else "moderate"
            )
    
    def record_session(self, device_id: str):
        """Record a NOIZYLAB session for this device"""
        lifeline = self.lifelines.get(device_id)
        if lifeline:
            lifeline.total_sessions += 1
            lifeline.last_checkup = datetime.now()
            if lifeline.first_seen_by_noizy:
                lifeline.relationship_duration_days = (datetime.now() - lifeline.first_seen_by_noizy).days
    
    def get_all_lifelines(self) -> List[DeviceLifeline]:
        """Get all lifelines"""
        return list(self.lifelines.values())
    
    def get_devices_needing_attention(self) -> List[DeviceLifeline]:
        """Get devices that need attention"""
        attention_statuses = [
            LifelineStatus.NEEDS_ATTENTION,
            LifelineStatus.KEEP_BUT_WATCH,
            LifelineStatus.RETIREMENT_SOON
        ]
        return [l for l in self.lifelines.values() if l.lifeline_status in attention_statuses]


# Singleton
lifeline_manager = LifelineManager()

