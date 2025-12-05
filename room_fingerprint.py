"""
NoizyHome Room Fingerprinting
=============================
Identifies rooms using WiFi signals, device presence,
noise patterns, mesh topology, and light levels.
No cameras or beacons required - pure AI inference.
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime
import hashlib


# Room fingerprint database
ROOM_FINGERPRINTS: Dict[str, Dict] = {}

# Room names mapping
ROOM_NAMES: Dict[str, str] = {}


def fingerprint_room(data: Dict) -> str:
    """
    Generate a unique fingerprint for a room based on sensor data.
    
    Data includes:
    - wifi_levels: list of (BSSID, signal_strength) tuples
    - noise_db: ambient noise level
    - light_lux: light level
    - devices: list of device MACs present
    - time_of_day: hour of day
    """
    # Create a stable hash from environmental factors
    wifi_sig = tuple(sorted(data.get("wifi_levels", [])))
    noise_band = round(data.get("noise_db", 0) / 10) * 10  # Round to nearest 10
    light_band = round(data.get("light_lux", 0) / 100) * 100  # Round to nearest 100
    devices = tuple(sorted(data.get("devices", [])))
    
    # Create composite fingerprint
    fingerprint_data = f"{wifi_sig}|{noise_band}|{light_band}|{devices}"
    fingerprint = hashlib.md5(fingerprint_data.encode()).hexdigest()[:12]
    
    return fingerprint


def identify_room(data: Dict) -> Optional[str]:
    """
    Identify which room based on current sensor data.
    Returns room_id if match found, None otherwise.
    """
    current_fp = fingerprint_room(data)
    
    # Check for exact match
    if current_fp in ROOM_FINGERPRINTS:
        return current_fp
    
    # Check for similar fingerprints (fuzzy matching)
    best_match = None
    best_score = 0
    
    for room_id, room_data in ROOM_FINGERPRINTS.items():
        score = _calculate_similarity(data, room_data.get("baseline", {}))
        if score > best_score and score > 0.7:  # 70% threshold
            best_score = score
            best_match = room_id
    
    return best_match


def register_room(data: Dict, name: str = None) -> str:
    """
    Register a new room fingerprint.
    """
    room_id = fingerprint_room(data)
    
    ROOM_FINGERPRINTS[room_id] = {
        "baseline": data,
        "created": datetime.now().isoformat(),
        "samples": 1,
        "last_seen": datetime.now().isoformat(),
    }
    
    if name:
        ROOM_NAMES[room_id] = name
    
    return room_id


def update_room_fingerprint(room_id: str, data: Dict) -> None:
    """
    Update room fingerprint with new sample (adaptive learning).
    """
    if room_id not in ROOM_FINGERPRINTS:
        return
    
    room = ROOM_FINGERPRINTS[room_id]
    room["samples"] += 1
    room["last_seen"] = datetime.now().isoformat()
    
    # Rolling average for baseline values
    baseline = room["baseline"]
    alpha = 0.1  # Learning rate
    
    for key in ["noise_db", "light_lux"]:
        if key in data and key in baseline:
            baseline[key] = baseline[key] * (1 - alpha) + data[key] * alpha


def _calculate_similarity(data1: Dict, data2: Dict) -> float:
    """
    Calculate similarity score between two room fingerprints.
    """
    score = 0
    factors = 0
    
    # WiFi similarity
    wifi1 = set(w[0] for w in data1.get("wifi_levels", []))
    wifi2 = set(w[0] for w in data2.get("wifi_levels", []))
    if wifi1 and wifi2:
        wifi_sim = len(wifi1 & wifi2) / len(wifi1 | wifi2)
        score += wifi_sim * 0.4
        factors += 0.4
    
    # Noise similarity
    noise1 = data1.get("noise_db", 0)
    noise2 = data2.get("noise_db", 0)
    if noise1 and noise2:
        noise_sim = 1 - min(abs(noise1 - noise2) / 50, 1)
        score += noise_sim * 0.2
        factors += 0.2
    
    # Light similarity
    light1 = data1.get("light_lux", 0)
    light2 = data2.get("light_lux", 0)
    if light1 and light2:
        light_sim = 1 - min(abs(light1 - light2) / 1000, 1)
        score += light_sim * 0.2
        factors += 0.2
    
    # Device similarity
    dev1 = set(data1.get("devices", []))
    dev2 = set(data2.get("devices", []))
    if dev1 and dev2:
        dev_sim = len(dev1 & dev2) / len(dev1 | dev2)
        score += dev_sim * 0.2
        factors += 0.2
    
    return score / factors if factors > 0 else 0


def get_room_name(room_id: str) -> str:
    """
    Get human-readable room name.
    """
    return ROOM_NAMES.get(room_id, f"Room-{room_id[:6]}")


def list_rooms() -> List[Dict]:
    """
    List all registered rooms.
    """
    return [
        {
            "id": room_id,
            "name": get_room_name(room_id),
            **data
        }
        for room_id, data in ROOM_FINGERPRINTS.items()
    ]

