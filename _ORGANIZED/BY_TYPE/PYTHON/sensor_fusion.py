"""
NoizyHome Sensor Fusion Layer
=============================
Combines all environmental inputs into one coherent awareness state.
The unified perception layer for the smart home.
"""

from typing import Dict, List, Optional
from datetime import datetime


# Fused state history
STATE_HISTORY: List[Dict] = []

# Current fused state
CURRENT_STATE: Dict = {}


def fuse_sensors(env: Dict) -> Dict:
    """
    Fuse all sensor inputs into unified environmental state.
    
    Inputs:
    - temp: temperature in Celsius
    - humidity: relative humidity %
    - noise_db: ambient noise level
    - light_lux: light level
    - motion: boolean motion detected
    - presence: list of detected people/devices
    - room_id: identified room
    - air_quality: AQI if available
    - co2: CO2 ppm if available
    """
    fused = {
        "timestamp": datetime.now().isoformat(),
        
        # Environmental
        "temp": env.get("temp"),
        "humidity": env.get("humidity"),
        "air_quality": env.get("air_quality"),
        "co2": env.get("co2"),
        
        # Acoustic
        "noise": env.get("noise_db"),
        "noise_type": classify_noise(env.get("noise_db", 0)),
        
        # Visual
        "light": env.get("light_lux"),
        "light_type": classify_light(env.get("light_lux", 0)),
        
        # Presence
        "motion": env.get("motion", False),
        "presence": env.get("presence", []),
        "occupancy": len(env.get("presence", [])),
        
        # Location
        "room_id": env.get("room_id"),
        
        # Derived
        "comfort_score": calculate_comfort(env),
        "activity_level": estimate_activity(env),
    }
    
    # Update global state
    global CURRENT_STATE
    CURRENT_STATE = fused
    
    # Add to history
    STATE_HISTORY.append(fused)
    if len(STATE_HISTORY) > 1000:
        STATE_HISTORY[:] = STATE_HISTORY[-500:]
    
    return fused


def classify_noise(db: float) -> str:
    """
    Classify noise level into categories.
    """
    if db < 30:
        return "silent"
    elif db < 45:
        return "quiet"
    elif db < 60:
        return "moderate"
    elif db < 75:
        return "loud"
    else:
        return "very_loud"


def classify_light(lux: float) -> str:
    """
    Classify light level into categories.
    """
    if lux < 10:
        return "dark"
    elif lux < 50:
        return "dim"
    elif lux < 200:
        return "moderate"
    elif lux < 500:
        return "bright"
    else:
        return "very_bright"


def calculate_comfort(env: Dict) -> float:
    """
    Calculate overall comfort score (0-100).
    """
    score = 100
    
    # Temperature comfort (ideal: 20-24°C)
    temp = env.get("temp", 22)
    if temp < 18 or temp > 26:
        score -= 20
    elif temp < 20 or temp > 24:
        score -= 10
    
    # Humidity comfort (ideal: 40-60%)
    humidity = env.get("humidity", 50)
    if humidity < 30 or humidity > 70:
        score -= 15
    elif humidity < 40 or humidity > 60:
        score -= 5
    
    # Noise comfort
    noise = env.get("noise_db", 30)
    if noise > 60:
        score -= 20
    elif noise > 45:
        score -= 10
    
    # Light appropriateness (context-dependent)
    # For now, assume moderate light is comfortable
    light = env.get("light_lux", 200)
    if light < 50 or light > 1000:
        score -= 10
    
    # Air quality
    aqi = env.get("air_quality", 50)
    if aqi > 100:
        score -= 15
    elif aqi > 50:
        score -= 5
    
    return max(0, min(100, score))


def estimate_activity(env: Dict) -> str:
    """
    Estimate activity level based on sensor data.
    """
    motion = env.get("motion", False)
    noise = env.get("noise_db", 0)
    occupancy = len(env.get("presence", []))
    
    if not motion and occupancy == 0:
        return "vacant"
    elif not motion:
        return "idle"
    elif noise > 60:
        return "active"
    elif noise > 45:
        return "moderate"
    else:
        return "quiet_presence"


def get_current_state() -> Dict:
    """
    Get current fused state.
    """
    return CURRENT_STATE


def get_state_history(limit: int = 50) -> List[Dict]:
    """
    Get recent state history.
    """
    return STATE_HISTORY[-limit:]


def get_room_state(room_id: str) -> Optional[Dict]:
    """
    Get most recent state for a specific room.
    """
    for state in reversed(STATE_HISTORY):
        if state.get("room_id") == room_id:
            return state
    return None


def get_trend(metric: str, minutes: int = 30) -> Dict:
    """
    Get trend for a specific metric over time.
    """
    cutoff = datetime.now().timestamp() - (minutes * 60)
    
    values = []
    for state in STATE_HISTORY:
        if state.get(metric) is not None:
            try:
                ts = datetime.fromisoformat(state["timestamp"]).timestamp()
                if ts > cutoff:
                    values.append(state[metric])
            except:
                pass
    
    if not values:
        return {"trend": "unknown", "values": []}
    
    avg = sum(values) / len(values)
    recent_avg = sum(values[-5:]) / min(5, len(values))
    
    if recent_avg > avg * 1.1:
        trend = "rising"
    elif recent_avg < avg * 0.9:
        trend = "falling"
    else:
        trend = "stable"
    
    return {
        "trend": trend,
        "current": values[-1] if values else None,
        "average": round(avg, 2),
        "min": min(values),
        "max": max(values),
        "samples": len(values),
    }

