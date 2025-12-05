"""Assistive: VR Controls"""
from datetime import datetime

VR_LOG = []

def vr_gesture(gesture_type, data=None):
    """Handle VR gesture"""
    gestures = {"pinch": "select", "swipe_left": "back", "swipe_right": "forward", "palm_up": "menu", "fist": "grab", "point": "click"}
    action = gestures.get(gesture_type, "unknown")
    result = {"gesture": gesture_type, "action": action, "data": data, "timestamp": datetime.now().isoformat()}
    VR_LOG.append(result)
    return result

def vr_gaze(target, duration=0.5):
    """Handle gaze-based selection"""
    result = {"action": "gaze_select" if duration > 0.5 else "gaze_hover", "target": target, "duration": duration, "timestamp": datetime.now().isoformat()}
    VR_LOG.append(result)
    return result

def vr_voice(command):
    """Handle VR voice command"""
    from .voice_control import execute
    result = execute(command)
    result["source"] = "vr"
    VR_LOG.append(result)
    return result

def get_hand_position():
    """Get current hand positions"""
    return {"left": {"x": 0, "y": 1, "z": -0.5}, "right": {"x": 0.3, "y": 1, "z": -0.5}}

def get_vr_log():
    return VR_LOG[-50:]

