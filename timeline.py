"""
NoizySync+ Persistent Timeline
==============================
Everything goes onto a global searchable timeline.
Your entire life & system is now searchable.
"""

import time
from typing import Dict, List, Optional
from datetime import datetime, timedelta


# Global timeline
TIMELINE: List[Dict] = []

# Event categories
CATEGORIES = [
    "session",      # User sessions
    "job",          # Compute jobs
    "ai",           # AI actions/predictions
    "mesh",         # Network events
    "security",     # Security events
    "life",         # NoizyLife events
    "device",       # Device events
    "customer",     # Customer interactions
    "system",       # System events
]


def log_event(event: Dict) -> Dict:
    """
    Log an event to the timeline.
    
    Event structure:
    - type: event type
    - category: one of CATEGORIES
    - title: human-readable title
    - description: detailed description
    - device: originating device
    - user: associated user
    - data: additional data
    """
    entry = {
        "id": len(TIMELINE),
        "timestamp": time.time(),
        "datetime": datetime.now().isoformat(),
        **event,
    }
    
    TIMELINE.append(entry)
    
    # Trim if too large
    if len(TIMELINE) > 10000:
        TIMELINE[:] = TIMELINE[-5000:]
    
    return entry


def get_timeline(limit: int = 100) -> List[Dict]:
    """
    Get recent timeline events.
    """
    return TIMELINE[-limit:]


def search_timeline(
    query: str = None,
    category: str = None,
    device: str = None,
    hours: int = None,
    limit: int = 100
) -> List[Dict]:
    """
    Search timeline with filters.
    """
    results = TIMELINE
    
    # Filter by time
    if hours:
        cutoff = time.time() - (hours * 3600)
        results = [e for e in results if e["timestamp"] > cutoff]
    
    # Filter by category
    if category:
        results = [e for e in results if e.get("category") == category]
    
    # Filter by device
    if device:
        results = [e for e in results if e.get("device") == device]
    
    # Search in title/description
    if query:
        query_lower = query.lower()
        results = [
            e for e in results
            if query_lower in e.get("title", "").lower()
            or query_lower in e.get("description", "").lower()
        ]
    
    return results[-limit:]


def get_timeline_by_category(category: str, limit: int = 50) -> List[Dict]:
    """
    Get timeline events for a specific category.
    """
    return [e for e in TIMELINE if e.get("category") == category][-limit:]


def get_device_timeline(device_id: str, limit: int = 50) -> List[Dict]:
    """
    Get timeline for a specific device.
    """
    return [e for e in TIMELINE if e.get("device") == device_id][-limit:]


def get_user_timeline(user_id: str, limit: int = 50) -> List[Dict]:
    """
    Get timeline for a specific user.
    """
    return [e for e in TIMELINE if e.get("user") == user_id][-limit:]


def get_timeline_summary(hours: int = 24) -> Dict:
    """
    Get summary of timeline activity.
    """
    cutoff = time.time() - (hours * 3600)
    recent = [e for e in TIMELINE if e["timestamp"] > cutoff]
    
    # Count by category
    by_category = {}
    for e in recent:
        cat = e.get("category", "unknown")
        by_category[cat] = by_category.get(cat, 0) + 1
    
    # Count by device
    by_device = {}
    for e in recent:
        dev = e.get("device", "unknown")
        by_device[dev] = by_device.get(dev, 0) + 1
    
    return {
        "total_events": len(recent),
        "by_category": by_category,
        "by_device": by_device,
        "hours": hours,
    }


def replay_session(
    start_time: float,
    end_time: float,
    device: str = None
) -> List[Dict]:
    """
    Get events for session replay.
    """
    events = [
        e for e in TIMELINE
        if start_time <= e["timestamp"] <= end_time
    ]
    
    if device:
        events = [e for e in events if e.get("device") == device]
    
    return events


# Convenience logging functions
def log_session_event(title: str, device: str, **kwargs) -> Dict:
    return log_event({
        "type": "session",
        "category": "session",
        "title": title,
        "device": device,
        **kwargs,
    })


def log_ai_event(title: str, **kwargs) -> Dict:
    return log_event({
        "type": "ai_action",
        "category": "ai",
        "title": title,
        **kwargs,
    })


def log_customer_event(title: str, customer: str, **kwargs) -> Dict:
    return log_event({
        "type": "customer",
        "category": "customer",
        "title": title,
        "customer": customer,
        **kwargs,
    })

