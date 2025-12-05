"""
NoizyVision Shield Bridge
=========================
Visual threat detection and NoizyShield+ integration.
"""

from typing import Dict, List, Optional
from datetime import datetime


# Threat levels
THREAT_NONE = "none"
THREAT_LOW = "low"
THREAT_MEDIUM = "medium"
THREAT_HIGH = "high"
THREAT_CRITICAL = "critical"


# Visual threat history
THREAT_HISTORY: List[Dict] = []


def check_visual_threat(analysis: Dict) -> str:
    """
    Check for visual threats in analysis results.
    """
    threats = []
    
    objects = analysis.get("objects", [])
    faces = analysis.get("faces", [])
    motion = analysis.get("motion", False)
    scene = analysis.get("scene", "unknown")
    
    # Unknown person detection
    unknown_faces = [f for f in faces if f.get("id") == "unknown"]
    if unknown_faces:
        if scene in ["repair_zone", "studio", "office"]:
            threats.append("unexpected_person_restricted")
        else:
            threats.append("unknown_person")
    
    # Motion in restricted area
    if motion and scene in ["repair_zone", "studio"]:
        if not faces:  # Motion without visible person
            threats.append("restricted_area_motion")
    
    # Multiple unknown faces
    if len(unknown_faces) > 2:
        threats.append("multiple_unknown_persons")
    
    # Suspicious objects (placeholder)
    suspicious = ["weapon", "mask", "crowbar"]
    for obj in objects:
        if obj.lower() in suspicious:
            threats.append(f"suspicious_object_{obj}")
    
    # Return highest threat
    if "unexpected_person_restricted" in threats:
        return "unexpected_person_restricted"
    if "restricted_area_motion" in threats:
        return "restricted_area_motion"
    if "multiple_unknown_persons" in threats:
        return "multiple_unknown_persons"
    if "unknown_person" in threats:
        return "unknown_person"
    if threats:
        return threats[0]
    
    return THREAT_NONE


def get_threat_level(threat: str) -> str:
    """
    Get threat level for a threat type.
    """
    threat_levels = {
        "none": THREAT_NONE,
        "unknown_person": THREAT_LOW,
        "restricted_area_motion": THREAT_MEDIUM,
        "unexpected_person_restricted": THREAT_HIGH,
        "multiple_unknown_persons": THREAT_HIGH,
        "suspicious_object": THREAT_CRITICAL,
    }
    
    for key, level in threat_levels.items():
        if key in threat:
            return level
    
    return THREAT_LOW


def escalate_to_shield(threat: str, analysis: Dict, device_id: str = None) -> Dict:
    """
    Escalate a visual threat to NoizyShield+.
    """
    threat_level = get_threat_level(threat)
    
    event = {
        "type": "visual_threat",
        "threat": threat,
        "level": threat_level,
        "device": device_id,
        "analysis": analysis,
        "timestamp": datetime.now().isoformat(),
    }
    
    # Log to history
    THREAT_HISTORY.append(event)
    
    # Trim history
    if len(THREAT_HISTORY) > 500:
        THREAT_HISTORY[:] = THREAT_HISTORY[-250:]
    
    # Attempt to notify NoizyShield+
    try:
        from ..noizyshield.response import handle_threat
        handle_threat(event)
    except ImportError:
        pass
    
    return event


def get_threat_history(limit: int = 50) -> List[Dict]:
    """
    Get recent threat history.
    """
    return THREAT_HISTORY[-limit:]


def get_active_threats() -> List[Dict]:
    """
    Get currently active threats (last 5 minutes).
    """
    now = datetime.now()
    active = []
    
    for threat in THREAT_HISTORY[-50:]:
        try:
            ts = datetime.fromisoformat(threat["timestamp"])
            if (now - ts).seconds < 300:
                active.append(threat)
        except Exception:
            pass
    
    return active


def should_alert(threat: str) -> bool:
    """
    Determine if threat should trigger an alert.
    """
    alert_threats = [
        "unexpected_person_restricted",
        "multiple_unknown_persons",
        "suspicious_object",
    ]
    
    return any(t in threat for t in alert_threats)


def get_recommended_action(threat: str) -> str:
    """
    Get recommended action for a threat.
    """
    actions = {
        "unknown_person": "Monitor and identify",
        "unexpected_person_restricted": "Alert and verify identity",
        "restricted_area_motion": "Check camera feed",
        "multiple_unknown_persons": "Alert and lockdown if needed",
        "suspicious_object": "Immediate alert and assess",
    }
    
    for key, action in actions.items():
        if key in threat:
            return action
    
    return "Continue monitoring"

