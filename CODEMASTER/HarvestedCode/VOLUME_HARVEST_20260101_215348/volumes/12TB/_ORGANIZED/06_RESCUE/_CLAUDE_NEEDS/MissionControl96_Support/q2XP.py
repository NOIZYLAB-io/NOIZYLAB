"""Base agent class for all NoizyFish agents"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseAgent(ABC):
    """Base class for all agents in the system"""
    
    def __init__(self, bus=None):
        self.bus = bus
        self.name = self.__class__.__name__
        self.active = True
        
    @abstractmethod
    def step(self):
        """Execute one step of the agent's logic"""
        pass
    
    def activate(self):
        """Activate the agent"""
        self.active = True
        
    def deactivate(self):
        """Deactivate the agent"""
        self.active = False
        
    def get_status(self) -> Dict[str, Any]:
        """Get agent status information"""
        return {
            "name": self.name,
            "active": self.active,
            "type": "agent"
        }