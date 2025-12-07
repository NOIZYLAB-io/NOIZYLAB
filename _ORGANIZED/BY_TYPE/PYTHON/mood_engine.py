"""
NoizyHome Mood-Based Environment Engine
=======================================
Adapts lighting, sound, and temperature to your mood,
energy level, and stress state. Your house responds to YOU.
"""

from typing import Dict, Optional
from datetime import datetime


# Environment presets
PRESETS = {
    "flow": {
        "lights": "bright_cool",
        "light_temp": 5500,  # Kelvin
        "light_brightness": 90,
        "sound": "silence",
        "temp_delta": 0,
        "humidity_target": 50,
    },
    "focus": {
        "lights": "neutral",
        "light_temp": 4500,
        "light_brightness": 80,
        "sound": "white_noise_low",
        "temp_delta": -1,
        "humidity_target": 50,
    },
    "creative": {
        "lights": "neon_pulse",
        "light_temp": 4000,
        "light_brightness": 70,
        "sound": "silence",
        "temp_delta": 0,
        "humidity_target": 50,
    },
    "chill": {
        "lights": "warm_dim",
        "light_temp": 2700,
        "light_brightness": 40,
        "sound": "lo_fi",
        "temp_delta": 1,
        "humidity_target": 55,
    },
    "sleep": {
        "lights": "off",
        "light_temp": 2200,
        "light_brightness": 0,
        "sound": "brown_noise",
        "temp_delta": -2,
        "humidity_target": 55,
    },
    "repair": {
        "lights": "bright_neutral",
        "light_temp": 5000,
        "light_brightness": 100,
        "sound": "silence",
        "temp_delta": -1,
        "humidity_target": 45,
    },
    "calm": {
        "lights": "warm_soft",
        "light_temp": 2700,
        "light_brightness": 30,
        "sound": "asmr",
        "temp_delta": 0,
        "humidity_target": 55,
    },
    "emergency": {
        "lights": "bright_alert",
        "light_temp": 6500,
        "light_brightness": 100,
        "sound": "alert_soft",
        "temp_delta": 0,
        "humidity_target": 50,
    },
}


def choose_environment(
    mood: str,
    energy: float,
    stress: str,
    time_of_day: Optional[int] = None
) -> Dict:
    """
    Choose optimal environment based on user state.
    
    Args:
        mood: "creative", "focused", "relaxed", "tired", etc.
        energy: 0.0 to 1.0
        stress: "low", "medium", "high"
        time_of_day: hour (0-23)
    
    Returns environment configuration.
    """
    if time_of_day is None:
        time_of_day = datetime.now().hour
    
    # High stress overrides everything
    if stress == "high":
        return {
            "preset": "calm",
            "lights": "warm_dim",
            "light_temp": 2700,
            "light_brightness": 25,
            "sound": "asmr",
            "temp_delta": -1,
            "reason": "High stress detected - activating calm mode",
        }
    
    # Very low energy
    if energy < 0.3:
        if time_of_day >= 21 or time_of_day < 6:
            return {
                "preset": "sleep",
                "lights": "off",
                "light_temp": 2200,
                "light_brightness": 0,
                "sound": "brown_noise",
                "temp_delta": -2,
                "reason": "Low energy + late hour - sleep mode",
            }
        else:
            return {
                "preset": "chill",
                "lights": "soft_cool",
                "light_temp": 3500,
                "light_brightness": 40,
                "sound": "brown_noise",
                "temp_delta": -1,
                "reason": "Low energy - rest mode",
            }
    
    # Mood-based selection
    if mood == "creative":
        return {
            "preset": "creative",
            "lights": "neon_pulse",
            "light_temp": 4000,
            "light_brightness": 70,
            "sound": "silence",
            "temp_delta": 0,
            "reason": "Creative mode - inspiring atmosphere",
        }
    
    if mood == "focused":
        return {
            "preset": "focus",
            "lights": "bright_cool",
            "light_temp": 5500,
            "light_brightness": 85,
            "sound": "silence",
            "temp_delta": -1,
            "reason": "Focus mode - optimal concentration",
        }
    
    if mood == "relaxed":
        return {
            "preset": "chill",
            "lights": "warm_dim",
            "light_temp": 2700,
            "light_brightness": 40,
            "sound": "lo_fi",
            "temp_delta": 1,
            "reason": "Relaxed mode - comfortable atmosphere",
        }
    
    # Default neutral
    return {
        "preset": "neutral",
        "lights": "neutral",
        "light_temp": 4000,
        "light_brightness": 60,
        "sound": "none",
        "temp_delta": 0,
        "reason": "Neutral mode",
    }


def get_preset(name: str) -> Optional[Dict]:
    """
    Get a specific environment preset.
    """
    return PRESETS.get(name)


def apply_preset(name: str) -> Dict:
    """
    Apply a preset and return the configuration.
    """
    preset = PRESETS.get(name)
    if not preset:
        return {"error": f"Unknown preset: {name}"}
    
    return {
        "applied": name,
        **preset,
        "timestamp": datetime.now().isoformat(),
    }


def blend_environments(env1: Dict, env2: Dict, weight: float = 0.5) -> Dict:
    """
    Blend two environments together.
    Weight 0.0 = all env1, 1.0 = all env2.
    """
    def blend_value(v1, v2, w):
        if isinstance(v1, (int, float)) and isinstance(v2, (int, float)):
            return v1 * (1 - w) + v2 * w
        return v2 if w > 0.5 else v1
    
    blended = {}
    all_keys = set(env1.keys()) | set(env2.keys())
    
    for key in all_keys:
        v1 = env1.get(key)
        v2 = env2.get(key)
        
        if v1 is None:
            blended[key] = v2
        elif v2 is None:
            blended[key] = v1
        else:
            blended[key] = blend_value(v1, v2, weight)
    
    return blended


def transition_environment(
    current: Dict,
    target: Dict,
    duration_seconds: int = 30
) -> Dict:
    """
    Generate transition plan between environments.
    """
    steps = max(1, duration_seconds // 5)  # Update every 5 seconds
    
    transitions = []
    for i in range(steps + 1):
        weight = i / steps
        step_env = blend_environments(current, target, weight)
        step_env["step"] = i
        step_env["time_offset"] = i * 5
        transitions.append(step_env)
    
    return {
        "duration": duration_seconds,
        "steps": steps,
        "transitions": transitions,
    }

