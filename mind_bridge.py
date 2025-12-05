"""
NoizyVision Mind Bridge
=======================
Visual event memory creation for NoizyMind.
"""

from typing import Dict, List, Optional
from datetime import datetime


# Local visual memory buffer
VISUAL_MEMORY: List[Dict] = []


def log_visual_event(event: str, context: Dict = None) -> Dict:
    """
    Log a visual event to NoizyMind memory.
    """
    memory_entry = {
        "content": f"Visual: {event}",
        "type": "vision",
        "timestamp": datetime.now().isoformat(),
        "context": context or {},
    }
    
    # Store locally
    VISUAL_MEMORY.append(memory_entry)
    
    # Trim buffer
    if len(VISUAL_MEMORY) > 500:
        VISUAL_MEMORY[:] = VISUAL_MEMORY[-250:]
    
    # Try to store in NoizyMind
    try:
        from ..noizymind.encoder import store_memory
        store_memory(memory_entry["content"], meta={"type": "vision", **memory_entry["context"]})
        memory_entry["stored_in_mind"] = True
    except ImportError:
        memory_entry["stored_in_mind"] = False
    
    return memory_entry


def log_detection_event(analysis: Dict, device_id: str = None) -> Dict:
    """
    Log a detection event with full analysis.
    """
    # Build event description
    parts = []
    
    if analysis.get("objects"):
        parts.append(f"Objects: {', '.join(analysis['objects'])}")
    
    if analysis.get("faces"):
        face_ids = [f.get("id", "unknown") for f in analysis["faces"]]
        parts.append(f"Faces: {', '.join(face_ids)}")
    
    if analysis.get("motion"):
        parts.append("Motion detected")
    
    if analysis.get("scene"):
        parts.append(f"Scene: {analysis['scene']}")
    
    event_desc = " | ".join(parts) if parts else "Visual observation"
    
    return log_visual_event(event_desc, {
        "device": device_id,
        "full_analysis": analysis,
    })


def log_face_recognition(face_id: str, confidence: float, device_id: str = None) -> Dict:
    """
    Log a face recognition event.
    """
    if face_id == "unknown":
        event = f"Unknown face detected (confidence: {confidence:.2f})"
    else:
        event = f"Recognized {face_id} (confidence: {confidence:.2f})"
    
    return log_visual_event(event, {
        "face_id": face_id,
        "confidence": confidence,
        "device": device_id,
    })


def log_scene_change(from_scene: str, to_scene: str, device_id: str = None) -> Dict:
    """
    Log a scene change event.
    """
    event = f"Scene changed: {from_scene} → {to_scene}"
    
    return log_visual_event(event, {
        "from_scene": from_scene,
        "to_scene": to_scene,
        "device": device_id,
    })


def log_anomaly(anomaly: str, analysis: Dict, device_id: str = None) -> Dict:
    """
    Log a visual anomaly.
    """
    event = f"Anomaly: {anomaly}"
    
    return log_visual_event(event, {
        "anomaly": anomaly,
        "analysis": analysis,
        "device": device_id,
    })


def get_visual_memory(limit: int = 50) -> List[Dict]:
    """
    Get recent visual memory.
    """
    return VISUAL_MEMORY[-limit:]


def search_visual_memory(query: str) -> List[Dict]:
    """
    Search visual memory.
    """
    query_lower = query.lower()
    return [
        m for m in VISUAL_MEMORY
        if query_lower in m.get("content", "").lower()
    ]


def get_memory_stats() -> Dict:
    """
    Get visual memory statistics.
    """
    return {
        "total_entries": len(VISUAL_MEMORY),
        "stored_in_mind": sum(1 for m in VISUAL_MEMORY if m.get("stored_in_mind")),
        "oldest": VISUAL_MEMORY[0]["timestamp"] if VISUAL_MEMORY else None,
        "newest": VISUAL_MEMORY[-1]["timestamp"] if VISUAL_MEMORY else None,
    }

