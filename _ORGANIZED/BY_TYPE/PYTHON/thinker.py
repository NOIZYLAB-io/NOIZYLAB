"""
NoizyMind Continuous Thinker
============================
Background loop that continuously thinks, plans, and learns.
The always-running brain of NoizyOS.
"""

import asyncio
from typing import Callable, Dict, Any
from datetime import datetime
from .planner import generate_plan
from .encoder import store_memory, get_memory_stats


class NoizyThinker:
    """
    Continuous thinking agent that runs in the background.
    """
    
    def __init__(self, fetch_context: Callable, interval: int = 20):
        self.fetch_context = fetch_context
        self.interval = interval
        self.running = False
        self.thought_count = 0
        self.last_thought = None
        self.insights = []
    
    async def start(self):
        """
        Start the thinking loop.
        """
        self.running = True
        await self._think_loop()
    
    def stop(self):
        """
        Stop the thinking loop.
        """
        self.running = False
    
    async def _think_loop(self):
        """
        Main thinking loop - runs continuously.
        """
        while self.running:
            try:
                # Fetch current system context
                context = await self.fetch_context()
                
                # Generate plan based on context
                plan = generate_plan(context)
                
                # Store the thought
                thought = self._formulate_thought(plan, context)
                store_memory(thought, meta={
                    "type": "thought",
                    "importance": self._calculate_importance(plan),
                    "plan_count": len(plan),
                })
                
                self.thought_count += 1
                self.last_thought = thought
                
                # Check for insights
                insight = self._extract_insight(plan, context)
                if insight:
                    self.insights.append(insight)
                    store_memory(insight, meta={
                        "type": "insight",
                        "importance": 2.0,
                    })
                
                # Auto-execute critical tasks
                await self._auto_execute(plan)
                
            except Exception as e:
                store_memory(f"Thinker error: {str(e)}", meta={
                    "type": "error",
                    "importance": 1.5,
                })
            
            await asyncio.sleep(self.interval)
    
    def _formulate_thought(self, plan: list, context: Dict) -> str:
        """
        Convert plan into a natural language thought.
        """
        if not plan:
            return "System is running smoothly. No immediate actions needed."
        
        critical = [t for t in plan if t.get("priority") == "critical"]
        high = [t for t in plan if t.get("priority") == "high"]
        
        if critical:
            return f"ALERT: {len(critical)} critical issue(s) detected. " + \
                   f"Primary concern: {critical[0]['title']}. " + \
                   f"Reason: {critical[0]['reason']}"
        
        if high:
            return f"Attention needed: {len(high)} high-priority task(s). " + \
                   f"Top priority: {high[0]['title']}. " + \
                   f"Full plan has {len(plan)} items."
        
        return f"Generated plan with {len(plan)} tasks. " + \
               f"System health appears stable. " + \
               f"Running proactive optimizations."
    
    def _calculate_importance(self, plan: list) -> float:
        """
        Calculate thought importance based on plan urgency.
        """
        if not plan:
            return 0.5
        
        critical = sum(1 for t in plan if t.get("priority") == "critical")
        high = sum(1 for t in plan if t.get("priority") == "high")
        
        return min(3.0, 1.0 + (critical * 1.0) + (high * 0.5))
    
    def _extract_insight(self, plan: list, context: Dict) -> str:
        """
        Extract learning insights from patterns.
        """
        stats = context.get("stats", {})
        
        # Example insight detection
        if stats.get("temp", 0) > 75 and stats.get("cpu_usage", 0) > 70:
            return "Pattern detected: High CPU correlates with elevated temperature. " + \
                   "Consider improving cooling or reducing parallel workloads."
        
        return None
    
    async def _auto_execute(self, plan: list):
        """
        Auto-execute critical tasks that are marked for immediate action.
        """
        for task in plan:
            if task.get("auto_execute") and task.get("priority") == "critical":
                # Log the auto-execution
                store_memory(
                    f"Auto-executing critical task: {task['title']}",
                    meta={"type": "action", "importance": 2.5}
                )
                # Actual execution would be handled by NoizyOps
    
    def get_status(self) -> Dict:
        """
        Get thinker status.
        """
        return {
            "running": self.running,
            "thought_count": self.thought_count,
            "last_thought": self.last_thought,
            "insights_count": len(self.insights),
            "memory_stats": get_memory_stats(),
        }


# Global thinker instance
_thinker = None


async def start_thinker(fetch_context: Callable, interval: int = 20):
    """
    Start the global thinker instance.
    """
    global _thinker
    _thinker = NoizyThinker(fetch_context, interval)
    await _thinker.start()


def get_thinker() -> NoizyThinker:
    """
    Get the global thinker instance.
    """
    return _thinker

