"""Assistive: UI Navigator"""
from datetime import datetime

NAVIGATION_LOG = []

def navigate(target):
    """Navigate to a UI target"""
    nav = {"action": "navigate", "target": target, "timestamp": datetime.now().isoformat()}
    NAVIGATION_LOG.append(nav)
    return nav

def click_element(selector):
    """Click a UI element by selector"""
    action = {"action": "click_element", "selector": selector, "timestamp": datetime.now().isoformat()}
    NAVIGATION_LOG.append(action)
    return action

def scroll(direction, amount=100):
    """Scroll the page"""
    action = {"action": "scroll", "direction": direction, "amount": amount, "timestamp": datetime.now().isoformat()}
    NAVIGATION_LOG.append(action)
    return action

def focus(element_id):
    """Focus on an element"""
    return {"action": "focus", "element": element_id}

def get_current_location():
    if NAVIGATION_LOG: return NAVIGATION_LOG[-1].get("target")
    return "/"

def get_navigation_history():
    return NAVIGATION_LOG[-20:]

