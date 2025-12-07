"""
NoizyHome Room Memory
=====================
Long-term learning of how each room is used.
Powers predictive behavior and personalization.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
from collections import Counter


# Room activity memory
ROOM_MEMORY: Dict[str, List[Dict]] = {}

# Learned room profiles
ROOM_PROFILES: Dict[str, Dict] = {}


def update_room_memory(room_id: str, activity: Dict) -> List[Dict]:
    """
    Record an activity in a room.
    
    Activity includes:
    - type: "work", "creative", "rest", "meeting", "exercise", etc.
    - person: who was there
    - duration_minutes: how long
    - mood: mood during activity
    - energy: energy level
    - time: hour of day
    """
    if room_id not in ROOM_MEMORY:
        ROOM_MEMORY[room_id] = []
    
    entry = {
        **activity,
        "timestamp": datetime.now().isoformat(),
        "hour": datetime.now().hour,
        "day_of_week": datetime.now().weekday(),
    }
    
    ROOM_MEMORY[room_id].append(entry)
    
    # Trim if too large
    if len(ROOM_MEMORY[room_id]) > 500:
        ROOM_MEMORY[room_id] = ROOM_MEMORY[room_id][-250:]
    
    # Update room profile
    _update_room_profile(room_id)
    
    return ROOM_MEMORY[room_id]


def _update_room_profile(room_id: str) -> None:
    """
    Update learned profile for a room.
    """
    activities = ROOM_MEMORY.get(room_id, [])
    if not activities:
        return
    
    # Count activity types
    activity_types = Counter(a.get("type") for a in activities)
    
    # Count by hour
    hour_usage = Counter(a.get("hour") for a in activities)
    
    # Calculate average mood/energy
    moods = [a.get("mood") for a in activities if a.get("mood")]
    energies = [a.get("energy") for a in activities if a.get("energy")]
    
    # Find primary use
    primary_use = activity_types.most_common(1)[0][0] if activity_types else "unknown"
    
    # Find peak hours
    peak_hours = [h for h, _ in hour_usage.most_common(3)]
    
    ROOM_PROFILES[room_id] = {
        "primary_use": primary_use,
        "activity_distribution": dict(activity_types),
        "peak_hours": peak_hours,
        "total_activities": len(activities),
        "avg_mood": sum(1 for m in moods if m in ["good", "great"]) / len(moods) if moods else 0.5,
        "avg_energy": sum(energies) / len(energies) if energies else 0.5,
        "updated": datetime.now().isoformat(),
    }


def get_room_memory(room_id: str, limit: int = 50) -> List[Dict]:
    """
    Get activity history for a room.
    """
    return ROOM_MEMORY.get(room_id, [])[-limit:]


def get_room_profile(room_id: str) -> Optional[Dict]:
    """
    Get learned profile for a room.
    """
    return ROOM_PROFILES.get(room_id)


def predict_room_use(room_id: str, hour: int = None) -> Dict:
    """
    Predict what a room will be used for at a given time.
    """
    if hour is None:
        hour = datetime.now().hour
    
    activities = ROOM_MEMORY.get(room_id, [])
    
    # Filter to same hour
    same_hour = [a for a in activities if a.get("hour") == hour]
    
    if not same_hour:
        return {"prediction": "unknown", "confidence": 0}
    
    # Count activities at this hour
    activity_types = Counter(a.get("type") for a in same_hour)
    most_common = activity_types.most_common(1)[0]
    
    return {
        "prediction": most_common[0],
        "confidence": most_common[1] / len(same_hour),
        "alternatives": [t for t, _ in activity_types.most_common(3)[1:]],
    }


def get_room_insights(room_id: str) -> Dict:
    """
    Get insights about room usage patterns.
    """
    profile = ROOM_PROFILES.get(room_id)
    activities = ROOM_MEMORY.get(room_id, [])
    
    if not profile or not activities:
        return {"message": "Not enough data"}
    
    # Calculate insights
    insights = []
    
    # Primary use insight
    insights.append(f"This room is primarily used for {profile['primary_use']}")
    
    # Peak hours insight
    if profile.get("peak_hours"):
        hours_str = ", ".join(f"{h}:00" for h in profile["peak_hours"])
        insights.append(f"Most active during: {hours_str}")
    
    # Mood insight
    if profile.get("avg_mood", 0.5) > 0.7:
        insights.append("This room is associated with positive moods")
    elif profile.get("avg_mood", 0.5) < 0.3:
        insights.append("Consider improving this room's atmosphere")
    
    # Energy insight
    if profile.get("avg_energy", 0.5) < 0.4:
        insights.append("Activities here tend to be low-energy")
    
    return {
        "profile": profile,
        "insights": insights,
        "data_points": len(activities),
    }


def get_all_room_profiles() -> Dict[str, Dict]:
    """
    Get profiles for all rooms.
    """
    return ROOM_PROFILES


def suggest_room_for_activity(activity_type: str) -> Optional[str]:
    """
    Suggest the best room for a given activity type.
    """
    best_room = None
    best_score = 0
    
    for room_id, profile in ROOM_PROFILES.items():
        distribution = profile.get("activity_distribution", {})
        score = distribution.get(activity_type, 0)
        
        if score > best_score:
            best_score = score
            best_room = room_id
    
    return best_room

