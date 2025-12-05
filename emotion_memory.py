"""
NoizyMemory GEN-1 — Layer 4: Emotional Memory
=============================================
Tracks mood patterns over time for personalized interactions.
Enables emotional trend analysis and adaptive AI behavior.
"""

from datetime import datetime
from typing import Dict, List, Any, Optional
from collections import Counter

# In-memory store (replace with database in production)
EMO_MEMORY: Dict[str, List[Dict[str, Any]]] = {}


def log_emotion(email: str, mood: str, context: Optional[str] = None) -> bool:
    """
    Log an emotional state for a client.
    
    Args:
        email: Client identifier
        mood: Mood category (distress, anxious, confused, frustrated, unhappy, happy, positive, neutral)
        context: Optional context about what triggered this mood
    
    Returns:
        True if successful
    """
    if email not in EMO_MEMORY:
        EMO_MEMORY[email] = []
    
    entry = {
        "mood": mood,
        "timestamp": datetime.now().isoformat()
    }
    
    if context:
        entry["context"] = context
    
    EMO_MEMORY[email].append(entry)
    return True


def average_mood(email: str) -> str:
    """
    Calculate the most common mood for a client.
    
    Args:
        email: Client identifier
    
    Returns:
        Most frequent mood, or "neutral" if no data
    """
    moods = EMO_MEMORY.get(email, [])
    
    if not moods:
        return "neutral"
    
    mood_list = [m.get("mood", "neutral") for m in moods]
    counter = Counter(mood_list)
    
    return counter.most_common(1)[0][0]


def emotion_trend(email: str, last_n: int = 10) -> Dict[str, Any]:
    """
    Analyze emotional trends over recent interactions.
    
    Args:
        email: Client identifier
        last_n: Number of recent entries to analyze
    
    Returns:
        Dict with trend analysis
    """
    moods = EMO_MEMORY.get(email, [])
    
    if not moods:
        return {
            "trend": "unknown",
            "recent_moods": [],
            "improving": None,
            "stress_level": "low"
        }
    
    recent = moods[-last_n:]
    mood_list = [m.get("mood", "neutral") for m in recent]
    
    # Calculate stress level
    stress_moods = ["distress", "anxious", "frustrated", "unhappy"]
    stress_count = sum(1 for m in mood_list if m in stress_moods)
    stress_ratio = stress_count / len(mood_list) if mood_list else 0
    
    if stress_ratio > 0.6:
        stress_level = "high"
    elif stress_ratio > 0.3:
        stress_level = "medium"
    else:
        stress_level = "low"
    
    # Determine trend direction
    if len(mood_list) >= 3:
        positive_moods = ["happy", "positive", "neutral"]
        first_half = mood_list[:len(mood_list)//2]
        second_half = mood_list[len(mood_list)//2:]
        
        first_positive = sum(1 for m in first_half if m in positive_moods)
        second_positive = sum(1 for m in second_half if m in positive_moods)
        
        if second_positive > first_positive:
            trend = "improving"
            improving = True
        elif second_positive < first_positive:
            trend = "declining"
            improving = False
        else:
            trend = "stable"
            improving = None
    else:
        trend = "insufficient_data"
        improving = None
    
    return {
        "trend": trend,
        "recent_moods": mood_list,
        "improving": improving,
        "stress_level": stress_level,
        "dominant_mood": average_mood(email)
    }


def get_mood_history(email: str, limit: Optional[int] = None) -> List[Dict]:
    """Get full mood history for a client."""
    moods = EMO_MEMORY.get(email, [])
    
    if limit:
        return moods[-limit:]
    
    return moods


def is_client_stressed(email: str) -> bool:
    """Quick check if client is currently stressed."""
    trend = emotion_trend(email, last_n=5)
    return trend.get("stress_level") == "high"


def get_mood_recommendation(email: str) -> str:
    """Get AI behavior recommendation based on emotional state."""
    trend = emotion_trend(email)
    mood = average_mood(email)
    
    if trend.get("stress_level") == "high" or mood == "distress":
        return "Use calm, slow, reassuring tone. Avoid technical jargon. Be patient."
    elif mood in ["anxious", "confused"]:
        return "Be clear and step-by-step. Offer reassurance. Check for understanding."
    elif mood in ["frustrated", "unhappy"]:
        return "Acknowledge frustration. Be solution-focused. Show empathy."
    elif mood in ["happy", "positive"]:
        return "Match energy. Be friendly and efficient. Light humor okay."
    else:
        return "Professional, friendly, balanced approach."

