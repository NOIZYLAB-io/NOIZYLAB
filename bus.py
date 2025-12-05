"""
NoizyCore Event Bus
===================
Global publish/subscribe system for all modules.
The bloodstream of the AI organism.
"""

from typing import Dict, Any, Callable, List, Optional
from datetime import datetime
from threading import Lock
from dataclasses import dataclass, field
from enum import Enum
import uuid


class EventPriority(int, Enum):
    LOW = 0
    NORMAL = 1
    HIGH = 2
    CRITICAL = 3
    EMERGENCY = 4


@dataclass
class Event:
    """
    System event structure.
    """
    type: str
    data: Dict[str, Any] = field(default_factory=dict)
    source: str = "system"
    priority: EventPriority = EventPriority.NORMAL
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "type": self.type,
            "data": self.data,
            "source": self.source,
            "priority": self.priority.value,
            "timestamp": self.timestamp,
        }


# Subscribers list with lock
_subscribers_lock = Lock()
_subscribers: List[Dict] = []

# Event history
_event_history: List[Event] = []
_history_lock = Lock()
MAX_HISTORY = 1000


def subscribe(callback: Callable, event_types: List[str] = None, priority_min: EventPriority = None) -> str:
    """
    Subscribe to events.
    
    Args:
        callback: Function to call with event
        event_types: Optional list of event types to filter
        priority_min: Minimum priority to receive
    
    Returns:
        Subscription ID
    """
    sub_id = str(uuid.uuid4())
    
    with _subscribers_lock:
        _subscribers.append({
            "id": sub_id,
            "callback": callback,
            "event_types": event_types,
            "priority_min": priority_min,
        })
    
    return sub_id


def unsubscribe(sub_id: str) -> bool:
    """
    Unsubscribe from events.
    """
    with _subscribers_lock:
        for i, sub in enumerate(_subscribers):
            if sub["id"] == sub_id:
                _subscribers.pop(i)
                return True
    return False


def publish(event: Any) -> Event:
    """
    Publish an event to all subscribers.
    
    Args:
        event: Event object or dict with type and data
    """
    # Convert dict to Event if needed
    if isinstance(event, dict):
        event = Event(
            type=event.get("type", "unknown"),
            data=event.get("data", event),
            source=event.get("source", "system"),
            priority=EventPriority(event.get("priority", 1)),
        )
    
    # Store in history
    with _history_lock:
        _event_history.append(event)
        if len(_event_history) > MAX_HISTORY:
            _event_history[:] = _event_history[-MAX_HISTORY//2:]
    
    # Notify subscribers
    with _subscribers_lock:
        subscribers_copy = _subscribers.copy()
    
    for sub in subscribers_copy:
        # Filter by event type
        if sub["event_types"] and event.type not in sub["event_types"]:
            continue
        
        # Filter by priority
        if sub["priority_min"] and event.priority.value < sub["priority_min"].value:
            continue
        
        # Call subscriber
        try:
            sub["callback"](event)
        except Exception as e:
            print(f"[BUS] Subscriber error: {e}")
    
    return event


def publish_simple(event_type: str, data: Dict = None, source: str = "system") -> Event:
    """
    Simple publish helper.
    """
    return publish(Event(type=event_type, data=data or {}, source=source))


def get_history(limit: int = 100, event_type: str = None) -> List[Dict]:
    """
    Get event history.
    """
    with _history_lock:
        events = _event_history[-limit:]
    
    if event_type:
        events = [e for e in events if e.type == event_type]
    
    return [e.to_dict() for e in events]


def get_subscriber_count() -> int:
    """
    Get number of active subscribers.
    """
    with _subscribers_lock:
        return len(_subscribers)


def clear_history() -> int:
    """
    Clear event history.
    """
    with _history_lock:
        count = len(_event_history)
        _event_history.clear()
    return count


# Convenience functions for common events
def emit_state_update(key: str, value: Any, source: str = "state") -> Event:
    """Emit a state update event."""
    return publish_simple("state_update", {"key": key, "value": value}, source)


def emit_heartbeat(state: Dict) -> Event:
    """Emit a heartbeat event."""
    return publish_simple("heartbeat", {"state": state}, "core")


def emit_alert(message: str, level: str = "warning", source: str = "system") -> Event:
    """Emit an alert event."""
    priority = EventPriority.HIGH if level == "critical" else EventPriority.NORMAL
    return publish(Event(
        type="alert",
        data={"message": message, "level": level},
        source=source,
        priority=priority,
    ))


def emit_module_event(module: str, action: str, data: Dict = None) -> Event:
    """Emit a module-specific event."""
    return publish_simple(f"{module}_{action}", data or {}, module)

