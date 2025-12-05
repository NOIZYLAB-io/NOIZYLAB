"""
NoizyLife Voice-Based Stress Detection
======================================
Analyzes pitch variance, tremor, amplitude jitter.
Plugs directly into NoizyVoice on all platforms.
"""

from typing import Dict
import numpy as np


def analyze_stress(audio_features: Dict) -> str:
    """
    Analyze voice features to detect stress level.
    
    Features expected:
    - pitch: fundamental frequency (Hz)
    - jitter: pitch variation (0-1)
    - shimmer: amplitude variation (0-1)
    - speaking_rate: words per minute
    - pause_ratio: silence to speech ratio
    
    Returns: "low", "medium", or "high"
    """
    pitch = audio_features.get("pitch", 140)  # Normal ~140Hz
    jitter = audio_features.get("jitter", 0)
    shimmer = audio_features.get("shimmer", 0)
    speaking_rate = audio_features.get("speaking_rate", 120)
    pause_ratio = audio_features.get("pause_ratio", 0.3)
    
    # Stress indicators:
    # - Higher jitter = vocal tremor
    # - Higher shimmer = amplitude instability
    # - Pitch deviation from baseline
    # - Faster speaking rate
    # - Fewer pauses
    
    # Normalize pitch deviation (baseline ~140Hz)
    pitch_stress = abs(pitch - 140) / 100
    
    # Speaking rate stress (normal ~120 wpm)
    rate_stress = max(0, (speaking_rate - 120) / 80)
    
    # Pause stress (less pauses = more stress)
    pause_stress = max(0, (0.3 - pause_ratio) / 0.3)
    
    # Weighted stress score
    stress_score = (
        jitter * 0.25 +
        shimmer * 0.25 +
        pitch_stress * 0.2 +
        rate_stress * 0.15 +
        pause_stress * 0.15
    )
    
    if stress_score > 0.7:
        return "high"
    elif stress_score > 0.4:
        return "medium"
    return "low"


def analyze_typing_stress(typing_data: Dict) -> str:
    """
    Analyze typing patterns for stress indicators.
    
    Features:
    - wpm: words per minute
    - error_rate: backspaces per word
    - key_pressure: average key hold time (ms)
    - pause_variance: variance in inter-key timing
    """
    wpm = typing_data.get("wpm", 60)
    error_rate = typing_data.get("error_rate", 0.1)
    key_pressure = typing_data.get("key_pressure", 100)
    pause_variance = typing_data.get("pause_variance", 50)
    
    # Stress indicators:
    # - Higher error rate
    # - Longer key holds (pressing harder)
    # - More erratic timing
    # - Very fast or very slow typing
    
    speed_stress = abs(wpm - 60) / 60
    error_stress = min(1, error_rate / 0.3)
    pressure_stress = min(1, (key_pressure - 100) / 100)
    variance_stress = min(1, pause_variance / 200)
    
    stress_score = (
        error_stress * 0.35 +
        pressure_stress * 0.25 +
        variance_stress * 0.25 +
        speed_stress * 0.15
    )
    
    if stress_score > 0.6:
        return "high"
    elif stress_score > 0.35:
        return "medium"
    return "low"


def get_stress_response(level: str) -> Dict:
    """
    Get appropriate response for stress level.
    """
    responses = {
        "low": {
            "action": "none",
            "message": "You're doing great!",
            "ui_mode": "normal",
        },
        "medium": {
            "action": "suggest_break",
            "message": "Consider taking a short break soon.",
            "ui_mode": "normal",
        },
        "high": {
            "action": "activate_calm",
            "message": "Let's slow down. Take a deep breath.",
            "ui_mode": "calm",
            "trigger_healing": True,
        },
    }
    return responses.get(level, responses["low"])

