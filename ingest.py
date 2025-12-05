"""
NoizyVision Ingestion Pipeline
==============================
Accepts frames from any device and routes to analysis.
"""

from typing import Dict, Any, Optional
import numpy as np
from datetime import datetime
from .vision_core import analyze_frame, VisionResult


# Frame buffer for multi-device support
FRAME_BUFFER: Dict[str, Dict] = {}

# Analysis history
ANALYSIS_HISTORY: list = []


def ingest_frame(frame_bytes: bytes, device_id: str) -> Dict[str, Any]:
    """
    Ingest a frame from a device and analyze it.
    """
    # Convert bytes to numpy array
    try:
        arr = np.frombuffer(frame_bytes, dtype=np.uint8)
    except Exception as e:
        return {
            "device": device_id,
            "error": f"Failed to parse frame: {str(e)}",
            "success": False,
        }
    
    # Analyze the frame
    result = analyze_frame(arr, device_id)
    
    # Store in buffer
    FRAME_BUFFER[device_id] = {
        "last_frame": datetime.now().isoformat(),
        "last_result": result.to_dict(),
    }
    
    # Add to history
    log_analysis(result)
    
    return {
        "device": device_id,
        "analysis": result.to_dict(),
        "success": True,
    }


def ingest_frame_array(arr: np.ndarray, device_id: str) -> Dict[str, Any]:
    """
    Ingest a numpy array directly.
    """
    result = analyze_frame(arr, device_id)
    
    FRAME_BUFFER[device_id] = {
        "last_frame": datetime.now().isoformat(),
        "last_result": result.to_dict(),
    }
    
    log_analysis(result)
    
    return {
        "device": device_id,
        "analysis": result.to_dict(),
        "success": True,
    }


def log_analysis(result: VisionResult) -> None:
    """
    Log analysis to history.
    """
    ANALYSIS_HISTORY.append({
        "timestamp": result.timestamp,
        "device": result.device_id,
        "objects": result.objects,
        "faces_count": len(result.faces),
        "motion": result.motion,
        "scene": result.scene,
        "anomalies": result.anomalies,
    })
    
    # Trim history
    if len(ANALYSIS_HISTORY) > 1000:
        ANALYSIS_HISTORY[:] = ANALYSIS_HISTORY[-500:]


def get_device_status(device_id: str) -> Optional[Dict]:
    """
    Get the latest status for a device.
    """
    return FRAME_BUFFER.get(device_id)


def get_all_devices() -> Dict[str, Dict]:
    """
    Get status for all devices.
    """
    return FRAME_BUFFER


def get_recent_analyses(limit: int = 50) -> list:
    """
    Get recent analysis history.
    """
    return ANALYSIS_HISTORY[-limit:]


def get_devices_with_motion() -> list:
    """
    Get devices currently detecting motion.
    """
    return [
        device_id for device_id, data in FRAME_BUFFER.items()
        if data.get("last_result", {}).get("motion")
    ]


def get_devices_with_faces() -> list:
    """
    Get devices currently detecting faces.
    """
    return [
        device_id for device_id, data in FRAME_BUFFER.items()
        if data.get("last_result", {}).get("faces")
    ]


def clear_device_buffer(device_id: str) -> bool:
    """
    Clear buffer for a device.
    """
    if device_id in FRAME_BUFFER:
        del FRAME_BUFFER[device_id]
        return True
    return False

