"""NoizySelf++ Energy Monitor - System Energy (not physical)"""
from .self_core import get_self_state, update_self_state, enter_safe_mode

def check_energy(metrics=None):
    """
    Calculate system energy based on:
    - Available compute
    - Bandwidth headroom
    - VRAM/GPU free
    - RAM free
    - Network jitter
    - Emotional load (from NoizyLife)
    """
    metrics = metrics or {}
    
    compute_available = metrics.get("compute_available", 0.7)
    bandwidth_headroom = metrics.get("bandwidth_headroom", 0.8)
    vram_free = metrics.get("vram_free", 0.6)
    ram_free = metrics.get("ram_free", 0.5)
    network_jitter = metrics.get("network_jitter", 0.1)  # Lower is better
    emotional_load = metrics.get("emotional_load", 0.2)  # Higher = more drain
    
    # Weighted energy calculation
    energy = (
        compute_available * 0.25 +
        bandwidth_headroom * 0.15 +
        vram_free * 0.20 +
        ram_free * 0.20 +
        (1 - network_jitter) * 0.10 +
        (1 - emotional_load) * 0.10
    )
    
    energy = min(1.0, max(0.0, energy))
    update_self_state("energy", energy)
    
    # Check for safe mode trigger
    if energy < 0.3:
        enter_safe_mode()
        return {"energy": energy, "safe_mode": True, "level": "critical"}
    elif energy < 0.5:
        return {"energy": energy, "safe_mode": False, "level": "low"}
    else:
        return {"energy": energy, "safe_mode": False, "level": "normal"}

def get_energy_level():
    """Get current energy level"""
    return get_self_state()["energy"]

def get_energy_breakdown(metrics=None):
    """Get detailed energy breakdown"""
    metrics = metrics or {}
    return {
        "compute_contribution": metrics.get("compute_available", 0.7) * 0.25,
        "bandwidth_contribution": metrics.get("bandwidth_headroom", 0.8) * 0.15,
        "vram_contribution": metrics.get("vram_free", 0.6) * 0.20,
        "ram_contribution": metrics.get("ram_free", 0.5) * 0.20,
        "network_contribution": (1 - metrics.get("network_jitter", 0.1)) * 0.10,
        "emotional_contribution": (1 - metrics.get("emotional_load", 0.2)) * 0.10,
    }

def is_energy_critical():
    """Check if energy is critically low"""
    return get_energy_level() < 0.3

def estimate_runtime(current_load):
    """Estimate how long system can run at current load"""
    energy = get_energy_level()
    if current_load <= 0:
        return float('inf')
    return energy / current_load * 3600  # seconds

