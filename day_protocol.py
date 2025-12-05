# ROB OS - DAY PROTOCOL
# ======================
# Normal Day vs Bad Day - The system adapts to YOU
# "Your nervous system can't wait. The machines can."

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, time

class DayMode(Enum):
    BUILDER = "builder"       # Normal day - creative, productive
    OPERATOR = "operator"     # Normal day - maintenance, admin
    FRAGILE = "fragile"       # Bad day - low energy, need gentleness
    FLAME = "flame"           # Bad day - burning out, need protection

class EnergyLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    DEPLETED = "depleted"

@dataclass
class DayState:
    """Current state of Rob's day."""
    mode: DayMode
    energy: EnergyLevel
    started_at: str
    
    # What's active
    sanctuary_active: bool = False
    current_world: Optional[str] = None
    
    # Task limits
    max_tasks: int = 5
    completed_tasks: int = 0
    
    # Protection flags
    block_new_clients: bool = False
    defer_decisions: bool = False
    voice_only_mode: bool = False

@dataclass
class DayProtocol:
    """Protocol settings for each day mode."""
    mode: DayMode
    
    # Morning routine
    morning_sanctuary: bool
    morning_world: str
    morning_breath: bool
    
    # Work settings
    max_tasks: int
    task_break_minutes: int
    auto_sanctuary_after_tasks: int
    
    # Protection
    block_crisis_clients: bool
    defer_big_decisions: bool
    
    # Voice
    voice_mode: str  # "guide", "sanctuary", "spark", "off"
    
    # Evening
    evening_sanctuary: bool
    evening_world: str
    
    # Messages
    morning_message: str
    check_in_message: str
    evening_message: str


class DayProtocolManager:
    """
    Manages Rob's daily operating protocol.
    Adapts the entire system to his current state.
    """
    
    def __init__(self):
        self.current_state: Optional[DayState] = None
        
        # Define protocols for each mode
        self.protocols = {
            DayMode.BUILDER: DayProtocol(
                mode=DayMode.BUILDER,
                morning_sanctuary=True,
                morning_world="skyroom",
                morning_breath=True,
                max_tasks=8,
                task_break_minutes=45,
                auto_sanctuary_after_tasks=4,
                block_crisis_clients=False,
                defer_big_decisions=False,
                voice_mode="guide",
                evening_sanctuary=True,
                evening_world="mc96_midnight",
                morning_message="Good morning, builder. What are we creating today?",
                check_in_message="You've been at it for a while. Quick breath?",
                evening_message="Good work today. Time to wind down."
            ),
            
            DayMode.OPERATOR: DayProtocol(
                mode=DayMode.OPERATOR,
                morning_sanctuary=True,
                morning_world="mc96_midnight",
                morning_breath=False,
                max_tasks=10,
                task_break_minutes=60,
                auto_sanctuary_after_tasks=5,
                block_crisis_clients=False,
                defer_big_decisions=False,
                voice_mode="guide",
                evening_sanctuary=True,
                evening_world="rain_on_the_roof",
                morning_message="Morning, operator. Let's handle the queue.",
                check_in_message="Lots done. Need a pause?",
                evening_message="Operations complete. Rest now."
            ),
            
            DayMode.FRAGILE: DayProtocol(
                mode=DayMode.FRAGILE,
                morning_sanctuary=True,
                morning_world="rain_on_the_roof",
                morning_breath=True,
                max_tasks=3,
                task_break_minutes=20,
                auto_sanctuary_after_tasks=2,
                block_crisis_clients=True,
                defer_big_decisions=True,
                voice_mode="sanctuary",
                evening_sanctuary=True,
                evening_world="soft_tide",
                morning_message="It's a gentle day. We go slow. No pressure.",
                check_in_message="You're doing enough. Really.",
                evening_message="You made it through. That's enough."
            ),
            
            DayMode.FLAME: DayProtocol(
                mode=DayMode.FLAME,
                morning_sanctuary=True,
                morning_world="silent_shore",
                morning_breath=True,
                max_tasks=1,
                task_break_minutes=15,
                auto_sanctuary_after_tasks=1,
                block_crisis_clients=True,
                defer_big_decisions=True,
                voice_mode="sanctuary",
                evening_sanctuary=True,
                evening_world="silent_shore",
                morning_message="Today is for survival, not productivity. Just exist.",
                check_in_message="Still here. Still okay. That's the whole job today.",
                evening_message="You survived. Tomorrow might be different."
            )
        }
    
    def start_day(self, mode: DayMode, energy: EnergyLevel = EnergyLevel.MEDIUM) -> DayState:
        """
        Start the day with a specific mode.
        """
        protocol = self.protocols[mode]
        
        self.current_state = DayState(
            mode=mode,
            energy=energy,
            started_at=datetime.now().isoformat(),
            sanctuary_active=protocol.morning_sanctuary,
            current_world=protocol.morning_world,
            max_tasks=protocol.max_tasks,
            block_new_clients=protocol.block_crisis_clients,
            defer_decisions=protocol.defer_big_decisions
        )
        
        return self.current_state
    
    def switch_mode(self, new_mode: DayMode) -> DayState:
        """
        Switch to a different mode mid-day.
        """
        if self.current_state:
            old_completed = self.current_state.completed_tasks
            self.current_state = self.start_day(new_mode, self.current_state.energy)
            self.current_state.completed_tasks = old_completed
        else:
            self.current_state = self.start_day(new_mode)
        
        return self.current_state
    
    def complete_task(self) -> Dict[str, Any]:
        """
        Mark a task as complete and check if sanctuary is needed.
        """
        if not self.current_state:
            return {"error": "Day not started"}
        
        self.current_state.completed_tasks += 1
        protocol = self.protocols[self.current_state.mode]
        
        result = {
            "completed": self.current_state.completed_tasks,
            "remaining": self.current_state.max_tasks - self.current_state.completed_tasks,
            "at_limit": self.current_state.completed_tasks >= self.current_state.max_tasks
        }
        
        # Check if auto-sanctuary is triggered
        if self.current_state.completed_tasks % protocol.auto_sanctuary_after_tasks == 0:
            result["sanctuary_triggered"] = True
            result["sanctuary_message"] = protocol.check_in_message
            result["suggested_world"] = protocol.morning_world
        
        # Check if at task limit
        if result["at_limit"]:
            result["limit_message"] = (
                f"You've hit your {self.current_state.mode.value} mode limit of "
                f"{self.current_state.max_tasks} tasks. Time to stop or switch modes."
            )
        
        return result
    
    def get_current_protocol(self) -> Optional[DayProtocol]:
        """Get the current day's protocol."""
        if self.current_state:
            return self.protocols[self.current_state.mode]
        return None
    
    def should_block_request(self, request_type: str) -> Dict[str, Any]:
        """
        Check if a request should be blocked based on current mode.
        """
        if not self.current_state:
            return {"blocked": False}
        
        protocol = self.protocols[self.current_state.mode]
        
        # Crisis clients blocked in fragile/flame
        if request_type == "crisis_client" and protocol.block_crisis_clients:
            return {
                "blocked": True,
                "reason": f"You're in {self.current_state.mode.value} mode. Crisis clients are deferred.",
                "alternative": "Queue for tomorrow or refer to backup support."
            }
        
        # Big decisions deferred in fragile/flame
        if request_type == "big_decision" and protocol.defer_big_decisions:
            return {
                "blocked": True,
                "reason": f"You're in {self.current_state.mode.value} mode. Big decisions wait.",
                "alternative": "Note it down. Decide when you're in builder/operator mode."
            }
        
        return {"blocked": False}
    
    def get_greeting(self) -> str:
        """Get the appropriate greeting for current state."""
        if not self.current_state:
            return "Hey. How are you doing today?"
        
        protocol = self.protocols[self.current_state.mode]
        hour = datetime.now().hour
        
        if hour < 12:
            return protocol.morning_message
        elif hour < 17:
            return protocol.check_in_message
        else:
            return protocol.evening_message
    
    def get_mode_switcher_ui(self) -> Dict[str, Any]:
        """
        Get UI configuration for the mode switcher.
        """
        return {
            "current_mode": self.current_state.mode.value if self.current_state else None,
            "modes": [
                {
                    "id": "builder",
                    "label": "Builder",
                    "emoji": "🔨",
                    "description": "Creative, productive day. Full capacity.",
                    "color": "#28a745"
                },
                {
                    "id": "operator",
                    "label": "Operator",
                    "emoji": "⚙️",
                    "description": "Maintenance, admin, handling the queue.",
                    "color": "#007bff"
                },
                {
                    "id": "fragile",
                    "label": "Fragile",
                    "emoji": "🌧️",
                    "description": "Low energy. Go slow. Protect yourself.",
                    "color": "#ffc107"
                },
                {
                    "id": "flame",
                    "label": "Flame",
                    "emoji": "🔥",
                    "description": "Burning out. Survival mode. Just exist.",
                    "color": "#dc3545"
                }
            ],
            "note": "Click to switch. The system adapts to protect you."
        }


# Singleton instance
_day_protocol = None

def get_day_protocol() -> DayProtocolManager:
    global _day_protocol
    if _day_protocol is None:
        _day_protocol = DayProtocolManager()
    return _day_protocol

