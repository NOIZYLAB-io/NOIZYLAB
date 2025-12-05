"""Assistive: Auto Clicker"""
from datetime import datetime

CLICK_LOG = []

def click(x, y):
    """Click at coordinates"""
    action = {"action": "click", "x": x, "y": y, "timestamp": datetime.now().isoformat()}
    CLICK_LOG.append(action)
    return action

def double_click(x, y):
    """Double click at coordinates"""
    action = {"action": "double_click", "x": x, "y": y, "timestamp": datetime.now().isoformat()}
    CLICK_LOG.append(action)
    return action

def right_click(x, y):
    """Right click at coordinates"""
    action = {"action": "right_click", "x": x, "y": y, "timestamp": datetime.now().isoformat()}
    CLICK_LOG.append(action)
    return action

def drag(start_x, start_y, end_x, end_y):
    """Drag from start to end"""
    action = {"action": "drag", "start": (start_x, start_y), "end": (end_x, end_y), "timestamp": datetime.now().isoformat()}
    CLICK_LOG.append(action)
    return action

def move_to(x, y):
    """Move cursor to coordinates"""
    return {"action": "move", "x": x, "y": y}

def get_click_history():
    return CLICK_LOG[-50:]

