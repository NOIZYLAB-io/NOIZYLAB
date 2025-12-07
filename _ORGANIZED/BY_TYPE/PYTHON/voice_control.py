"""Assistive: Voice Control"""
from datetime import datetime

COMMANDS = {
    "open diagnostics": {"action": "navigate", "target": "/diagnostics"},
    "check status": {"action": "api_call", "target": "/core/status"},
    "book appointment": {"action": "navigate", "target": "/booking"},
    "read messages": {"action": "screen_read", "target": "messages"},
    "calm mode": {"action": "trigger_flow", "target": "calm_mode"},
    "emergency": {"action": "trigger_flow", "target": "emergency"},
    "go back": {"action": "navigate", "target": "back"},
    "scroll down": {"action": "scroll", "target": "down"},
    "scroll up": {"action": "scroll", "target": "up"},
}

COMMAND_LOG = []

def execute(command_text):
    """Execute a voice command"""
    cmd = command_text.lower().strip()
    for phrase, action in COMMANDS.items():
        if phrase in cmd:
            result = {"command": phrase, "action": action, "executed_at": datetime.now().isoformat(), "status": "executed"}
            COMMAND_LOG.append(result)
            return result
    return {"command": cmd, "status": "not_recognized", "suggestion": "Try: " + ", ".join(list(COMMANDS.keys())[:5])}

def listen():
    """Start listening for voice commands"""
    return {"status": "listening", "available_commands": list(COMMANDS.keys())}

def get_commands():
    return COMMANDS

def add_command(phrase, action):
    COMMANDS[phrase.lower()] = action
    return {"added": phrase, "action": action}

def get_command_history(limit=20):
    return COMMAND_LOG[-limit:]

