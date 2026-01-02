"""Agent registry system for dynamic agent loading"""
from typing import Dict, Type, Callable
from .base import BaseAgent

# Global registry for agents
_agent_registry: Dict[str, Type[BaseAgent]] = {}


def register(name: str) -> Callable:
    """Decorator to register an agent class"""
    def decorator(cls: Type[BaseAgent]) -> Type[BaseAgent]:
        _agent_registry[name] = cls
        return cls
    return decorator


def get_agent(name: str) -> Type[BaseAgent]:
    """Get an agent class by name"""
    if name not in _agent_registry:
        raise ValueError(f"Agent '{name}' not found in registry")
    return _agent_registry[name]


def list_agents() -> Dict[str, Type[BaseAgent]]:
    """List all registered agents"""
    return _agent_registry.copy()


def create_agent(name: str, **kwargs) -> BaseAgent:
    """Create an instance of a registered agent"""
    agent_class = get_agent(name)
    return agent_class(**kwargs)