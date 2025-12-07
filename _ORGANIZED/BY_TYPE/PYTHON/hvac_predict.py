"""
NoizyHome HVAC Predictor
========================
Predicts heating/cooling needs based on compute heat,
occupancy, stress levels, and time patterns.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta


# HVAC history for learning
HVAC_HISTORY: List[Dict] = []

# Learned patterns
PATTERNS: Dict[int, Dict] = {}  # hour -> typical adjustment


def predict_hvac(context: Dict) -> float:
    """
    Predict HVAC adjustment needed.
    
    Context includes:
    - compute_heat: heat from computing devices (0-100)
    - presence: list of people in space
    - stress: stress level
    - current_temp: current temperature
    - target_temp: desired temperature
    - outdoor_temp: outside temperature
    - time_of_day: hour
    
    Returns adjustment in degrees Celsius (-3 to +3).
    """
    compute_heat = context.get("compute_heat", 0)
    people = len(context.get("presence", []))
    stress = context.get("stress", "low")
    current_temp = context.get("current_temp", 22)
    target_temp = context.get("target_temp", 22)
    outdoor_temp = context.get("outdoor_temp", 20)
    hour = context.get("time_of_day", datetime.now().hour)
    
    adjustment = 0.0
    
    # Compute heat compensation
    # Every 20% GPU load = ~0.5°C room temp increase
    compute_adjustment = -(compute_heat * 0.025)
    adjustment += compute_adjustment
    
    # Occupancy adjustment
    # Each person adds ~0.3°C
    people_adjustment = -(people * 0.3)
    adjustment += people_adjustment
    
    # Stress-based adjustment
    # High stress = cooler environment helps
    if stress == "high":
        adjustment -= 1.0
    elif stress == "medium":
        adjustment -= 0.5
    
    # Time-of-day patterns
    if hour >= 22 or hour < 6:
        # Night - cooler for sleep
        adjustment -= 1.0
    elif hour >= 14 and hour < 16:
        # Afternoon slump - slightly cooler
        adjustment -= 0.5
    
    # Outdoor compensation
    if outdoor_temp > 30:
        adjustment -= 0.5  # Extra cooling on hot days
    elif outdoor_temp < 10:
        adjustment += 0.5  # Extra heating on cold days
    
    # Learn from patterns
    learned = PATTERNS.get(hour, {}).get("avg_adjustment", 0)
    adjustment = adjustment * 0.7 + learned * 0.3
    
    # Clamp to reasonable range
    adjustment = max(-3, min(3, adjustment))
    
    # Log for learning
    log_hvac_decision(context, adjustment)
    
    return round(adjustment, 1)


def log_hvac_decision(context: Dict, adjustment: float) -> None:
    """
    Log HVAC decision for pattern learning.
    """
    entry = {
        "timestamp": datetime.now().isoformat(),
        "hour": datetime.now().hour,
        "adjustment": adjustment,
        "context": context,
    }
    
    HVAC_HISTORY.append(entry)
    
    # Update patterns
    hour = entry["hour"]
    if hour not in PATTERNS:
        PATTERNS[hour] = {"adjustments": [], "avg_adjustment": 0}
    
    PATTERNS[hour]["adjustments"].append(adjustment)
    if len(PATTERNS[hour]["adjustments"]) > 100:
        PATTERNS[hour]["adjustments"] = PATTERNS[hour]["adjustments"][-50:]
    
    PATTERNS[hour]["avg_adjustment"] = sum(PATTERNS[hour]["adjustments"]) / len(PATTERNS[hour]["adjustments"])
    
    # Trim history
    if len(HVAC_HISTORY) > 1000:
        HVAC_HISTORY[:] = HVAC_HISTORY[-500:]


def get_hvac_schedule() -> Dict:
    """
    Get predicted HVAC schedule for the day.
    """
    schedule = {}
    
    for hour in range(24):
        pattern = PATTERNS.get(hour, {})
        schedule[hour] = {
            "predicted_adjustment": pattern.get("avg_adjustment", 0),
            "samples": len(pattern.get("adjustments", [])),
        }
    
    return schedule


def get_efficiency_report(days: int = 7) -> Dict:
    """
    Get HVAC efficiency report.
    """
    cutoff = datetime.now() - timedelta(days=days)
    
    recent = [
        h for h in HVAC_HISTORY
        if datetime.fromisoformat(h["timestamp"]) > cutoff
    ]
    
    if not recent:
        return {"message": "Not enough data"}
    
    adjustments = [h["adjustment"] for h in recent]
    
    return {
        "period_days": days,
        "total_adjustments": len(recent),
        "avg_adjustment": round(sum(adjustments) / len(adjustments), 2),
        "max_cooling": min(adjustments),
        "max_heating": max(adjustments),
        "stability": 1 - (max(adjustments) - min(adjustments)) / 6,  # 0-1 scale
    }


def predict_preemptive(schedule: Dict, minutes_ahead: int = 30) -> Optional[float]:
    """
    Predict what adjustment will be needed soon.
    Allows preemptive HVAC changes.
    """
    future_hour = (datetime.now() + timedelta(minutes=minutes_ahead)).hour
    
    if future_hour in PATTERNS:
        return PATTERNS[future_hour].get("avg_adjustment", 0)
    
    return None

