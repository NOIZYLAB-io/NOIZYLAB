"""
NoizyLife Daily Check-In
========================
Lightweight, fast mood and energy tracking.
No heavy journaling - just vibes.
"""

from datetime import datetime, date
from typing import Dict, List, Optional
import json


# In-memory storage (would be database in production)
CHECKINS: List[Dict] = []


def check_in(
    mood: str,
    energy: int,
    notes: str = "",
    stress: str = "low"
) -> Dict:
    """
    Record a daily check-in.
    
    Args:
        mood: "great", "good", "okay", "low", "bad"
        energy: 1-10 scale
        notes: optional short note
        stress: "low", "medium", "high"
    
    Returns: stored entry
    """
    entry = {
        "timestamp": datetime.now().isoformat(),
        "date": date.today().isoformat(),
        "mood": mood,
        "energy": energy,
        "notes": notes,
        "stress": stress,
    }
    
    CHECKINS.append(entry)
    
    # Also store in NoizyMind for semantic search
    try:
        from ..noizymind.encoder import store_memory
        memory_text = f"Check-in: Mood={mood}, Energy={energy}/10, Stress={stress}"
        if notes:
            memory_text += f", Notes: {notes}"
        store_memory(memory_text, meta={"type": "checkin", "date": entry["date"]})
    except ImportError:
        pass
    
    return {"stored": True, "entry": entry}


def get_today_checkins() -> List[Dict]:
    """
    Get all check-ins from today.
    """
    today = date.today().isoformat()
    return [c for c in CHECKINS if c["date"] == today]


def get_recent_checkins(days: int = 7) -> List[Dict]:
    """
    Get check-ins from the last N days.
    """
    from datetime import timedelta
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    return [c for c in CHECKINS if c["date"] >= cutoff]


def get_mood_trend(days: int = 7) -> Dict:
    """
    Analyze mood trend over time.
    """
    recent = get_recent_checkins(days)
    if not recent:
        return {"trend": "unknown", "data": []}
    
    mood_scores = {
        "great": 5,
        "good": 4,
        "okay": 3,
        "low": 2,
        "bad": 1,
    }
    
    scores = [mood_scores.get(c["mood"], 3) for c in recent]
    avg = sum(scores) / len(scores)
    
    # Trend detection
    if len(scores) >= 3:
        first_half = sum(scores[:len(scores)//2]) / (len(scores)//2)
        second_half = sum(scores[len(scores)//2:]) / (len(scores) - len(scores)//2)
        
        if second_half > first_half + 0.5:
            trend = "improving"
        elif second_half < first_half - 0.5:
            trend = "declining"
        else:
            trend = "stable"
    else:
        trend = "insufficient_data"
    
    return {
        "trend": trend,
        "average": round(avg, 2),
        "count": len(recent),
        "data": recent,
    }


def quick_checkin(emoji: str) -> Dict:
    """
    Ultra-quick check-in via emoji.
    """
    emoji_map = {
        "😊": ("great", 8),
        "🙂": ("good", 7),
        "😐": ("okay", 5),
        "😔": ("low", 3),
        "😢": ("bad", 2),
        "🔥": ("great", 10),
        "😴": ("okay", 2),
        "💪": ("good", 9),
        "😰": ("low", 4),
    }
    
    mood, energy = emoji_map.get(emoji, ("okay", 5))
    return check_in(mood, energy, notes=f"Quick: {emoji}")

