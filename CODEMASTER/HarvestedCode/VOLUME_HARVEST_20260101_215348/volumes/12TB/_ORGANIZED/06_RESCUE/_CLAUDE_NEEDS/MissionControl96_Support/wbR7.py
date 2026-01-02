"""
NoizyFish Agents Package
Modular agent system for Mission Control 96
"""

from .base import BaseAgent
from .registry import register, get_agent, list_agents, create_agent

# Import all agent modules to register them
from . import agent_client_portal

__all__ = [
    "BaseAgent",
    "register", 
    "get_agent", 
    "list_agents", 
    "create_agent"
]