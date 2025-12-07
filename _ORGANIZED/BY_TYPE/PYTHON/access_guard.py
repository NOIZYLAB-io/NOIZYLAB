"""
NoizyHome Access Intelligence
=============================
Tracks doors, windows, entry points, motion, and presence.
Integrates with NoizyShield+ for security escalation.
"""

from typing import Dict, List, Optional
from datetime import datetime, time


# Access event log
ACCESS_LOG: List[Dict] = []

# Access points registry
ACCESS_POINTS: Dict[str, Dict] = {}

# Expected presence patterns
PRESENCE_PATTERNS: Dict[int, List[str]] = {}  # hour -> expected people


def evaluate_access(event: Dict) -> Optional[Dict]:
    """
    Evaluate an access event for anomalies.
    
    Event includes:
    - type: "door_open", "door_close", "window_open", "motion", "entry"
    - location: access point ID
    - time: hour (0-23)
    - expected: whether this was expected
    - person: identified person if known
    """
    event_type = event.get("type")
    location = event.get("location")
    hour = event.get("time", datetime.now().hour)
    expected = event.get("expected", True)
    person = event.get("person")
    
    alert = None
    
    # Night access (midnight to 5am)
    if hour >= 0 and hour < 5:
        if event_type in ["door_open", "entry"]:
            alert = {
                "type": "night_access",
                "severity": "high",
                "detail": f"Access at {hour}:00 - {event_type} at {location}",
                "location": location,
            }
    
    # Unexpected presence
    if not expected and event_type == "motion":
        alert = {
            "type": "unexpected_presence",
            "severity": "medium",
            "detail": f"Unexpected motion at {location}",
            "location": location,
        }
    
    # Unknown person entry
    if event_type == "entry" and not person:
        alert = {
            "type": "unknown_entry",
            "severity": "high",
            "detail": f"Unidentified entry at {location}",
            "location": location,
        }
    
    # Window open at night
    if event_type == "window_open" and (hour >= 22 or hour < 6):
        alert = {
            "type": "night_window",
            "severity": "low",
            "detail": f"Window opened at night - {location}",
            "location": location,
        }
    
    # Log the event
    log_access(event, alert)
    
    return alert


def log_access(event: Dict, alert: Optional[Dict] = None) -> None:
    """
    Log an access event.
    """
    entry = {
        **event,
        "timestamp": datetime.now().isoformat(),
        "alert": alert,
    }
    
    ACCESS_LOG.append(entry)
    
    # Trim log
    if len(ACCESS_LOG) > 1000:
        ACCESS_LOG[:] = ACCESS_LOG[-500:]


def register_access_point(point_id: str, config: Dict) -> None:
    """
    Register an access point (door, window, etc.).
    
    Config includes:
    - type: "door", "window", "garage", "gate"
    - location: room or area name
    - monitored: whether it's actively monitored
    - secure_hours: list of hours when access is restricted
    """
    ACCESS_POINTS[point_id] = {
        **config,
        "registered": datetime.now().isoformat(),
        "last_event": None,
    }


def get_access_status() -> Dict:
    """
    Get current status of all access points.
    """
    status = {}
    for point_id, config in ACCESS_POINTS.items():
        # Find last event for this point
        last_event = None
        for event in reversed(ACCESS_LOG):
            if event.get("location") == point_id:
                last_event = event
                break
        
        status[point_id] = {
            **config,
            "last_event": last_event,
        }
    
    return status


def get_access_log(limit: int = 50, location: str = None) -> List[Dict]:
    """
    Get access event history.
    """
    logs = ACCESS_LOG
    
    if location:
        logs = [l for l in logs if l.get("location") == location]
    
    return logs[-limit:]


def get_alerts(hours: int = 24) -> List[Dict]:
    """
    Get recent access alerts.
    """
    cutoff = datetime.now().timestamp() - (hours * 3600)
    
    alerts = []
    for event in ACCESS_LOG:
        if event.get("alert"):
            try:
                ts = datetime.fromisoformat(event["timestamp"]).timestamp()
                if ts > cutoff:
                    alerts.append(event["alert"])
            except:
                pass
    
    return alerts


def set_presence_pattern(hour: int, expected_people: List[str]) -> None:
    """
    Set expected presence pattern for an hour.
    Used for anomaly detection.
    """
    PRESENCE_PATTERNS[hour] = expected_people


def is_presence_expected(person: str, hour: int = None) -> bool:
    """
    Check if a person's presence is expected at this time.
    """
    if hour is None:
        hour = datetime.now().hour
    
    expected = PRESENCE_PATTERNS.get(hour, [])
    return person in expected or not expected  # If no pattern, assume expected


def get_occupancy_summary() -> Dict:
    """
    Get current occupancy summary.
    """
    # Find recent motion/presence events
    recent_presence = set()
    for event in reversed(ACCESS_LOG[-50:]):
        if event.get("person"):
            recent_presence.add(event["person"])
    
    return {
        "current_occupants": list(recent_presence),
        "count": len(recent_presence),
        "last_activity": ACCESS_LOG[-1] if ACCESS_LOG else None,
    }

