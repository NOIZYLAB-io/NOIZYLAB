"""NoizySelf++ Stress Monitor - CPU, GPU, Thermal, Voice, Task Queue Analysis"""
from .self_core import get_self_state, update_self_state

def check_stress(metrics=None):
    """
    Calculate stress level based on:
    - CPU load
    - GPU load
    - Cluster thermal readings
    - User voice tone
    - Number of tasks in queue
    - Memory fragmentation
    """
    metrics = metrics or {}
    
    cpu_load = metrics.get("cpu_load", 0.3)
    gpu_load = metrics.get("gpu_load", 0.2)
    thermal = metrics.get("thermal", 0.4)  # 0-1 scale, 1 = critical
    voice_stress = metrics.get("voice_stress", 0.1)
    task_queue = metrics.get("task_queue_size", 0)
    memory_frag = metrics.get("memory_fragmentation", 0.1)
    
    # Weighted stress calculation
    stress = (
        cpu_load * 0.25 +
        gpu_load * 0.20 +
        thermal * 0.20 +
        voice_stress * 0.15 +
        min(task_queue / 100, 1.0) * 0.10 +
        memory_frag * 0.10
    )
    
    stress = min(1.0, max(0.0, stress))
    update_self_state("stress", stress)
    
    # Check if reflex loop should trigger
    if stress > 0.75:
        return {"stress": stress, "trigger_reflex": True, "level": "critical"}
    elif stress > 0.5:
        return {"stress": stress, "trigger_reflex": False, "level": "elevated"}
    else:
        return {"stress": stress, "trigger_reflex": False, "level": "normal"}

def get_stress_level():
    """Get current stress level"""
    return get_self_state()["stress"]

def get_stress_breakdown(metrics=None):
    """Get detailed stress breakdown"""
    metrics = metrics or {}
    return {
        "cpu_contribution": metrics.get("cpu_load", 0.3) * 0.25,
        "gpu_contribution": metrics.get("gpu_load", 0.2) * 0.20,
        "thermal_contribution": metrics.get("thermal", 0.4) * 0.20,
        "voice_contribution": metrics.get("voice_stress", 0.1) * 0.15,
        "queue_contribution": min(metrics.get("task_queue_size", 0) / 100, 1.0) * 0.10,
        "memory_contribution": metrics.get("memory_fragmentation", 0.1) * 0.10,
    }

def is_stress_critical():
    """Check if stress is at critical level"""
    return get_stress_level() > 0.75

