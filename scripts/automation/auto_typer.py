"""Assistive: Auto Typer"""
from datetime import datetime

TYPE_LOG = []

def type_text(text, delay=0.05):
    """Type text"""
    action = {"action": "type", "text": text, "delay": delay, "timestamp": datetime.now().isoformat()}
    TYPE_LOG.append(action)
    return action

def press_key(key):
    """Press a single key"""
    action = {"action": "press", "key": key, "timestamp": datetime.now().isoformat()}
    TYPE_LOG.append(action)
    return action

def hotkey(*keys):
    """Press a hotkey combination"""
    action = {"action": "hotkey", "keys": keys, "timestamp": datetime.now().isoformat()}
    TYPE_LOG.append(action)
    return action

def type_slowly(text, delay=0.1):
    """Type text slowly for visibility"""
    return type_text(text, delay)

def clear_field():
    """Clear current input field"""
    return hotkey("cmd", "a") and press_key("backspace")

def get_type_history():
    return TYPE_LOG[-50:]

