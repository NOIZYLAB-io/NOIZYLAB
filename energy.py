"""
NoizyLife Energy Tracking
=========================
Simple weighted decay model across your day.
Tracks energy levels and suggests actions.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional


class EnergyTracker:
    """
    Tracks and models user energy throughout the day.
    """
    
    def __init__(self):
        self.energy = 1.0  # Normalized 0-1
        self.history: List[Dict] = []
        self.last_update = datetime.now()
        self.daily_peak = 1.0
        self.daily_low = 1.0
    
    def update(self, event: str) -> float:
        """
        Update energy based on event.
        Returns new energy level.
        """
        # Event impacts
        impacts = {
            # Draining events
            "focus_work": -0.05,
            "meeting": -0.08,
            "stress": -0.10,
            "conflict": -0.12,
            "long_session": -0.07,
            "multitask": -0.06,
            "deadline": -0.09,
            
            # Restoring events
            "break": 0.03,
            "walk": 0.05,
            "meal": 0.04,
            "coffee": 0.03,
            "win": 0.08,
            "flow_state": 0.02,  # Flow gives energy!
            "meditation": 0.06,
            "stretch": 0.02,
            "music": 0.03,
            "laugh": 0.04,
            "nap": 0.15,
            
            # Neutral
            "idle": 0.01,
        }
        
        impact = impacts.get(event, 0)
        self.energy += impact
        
        # Clamp to 0-1
        self.energy = max(0, min(1, self.energy))
        
        # Track peaks and lows
        self.daily_peak = max(self.daily_peak, self.energy)
        self.daily_low = min(self.daily_low, self.energy)
        
        # Log history
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "event": event,
            "impact": impact,
            "level": self.energy,
        })
        
        self.last_update = datetime.now()
        return self.energy
    
    def get_level(self) -> float:
        """
        Get current energy level with time decay.
        """
        # Natural decay over time (0.5% per minute of inactivity)
        minutes_since = (datetime.now() - self.last_update).seconds / 60
        decay = minutes_since * 0.005
        
        return max(0, self.energy - decay)
    
    def get_status(self) -> Dict:
        """
        Get energy status with recommendations.
        """
        level = self.get_level()
        
        if level > 0.8:
            status = "high"
            message = "Energy is great! Perfect time for challenging tasks."
            color = "#2ECC71"
        elif level > 0.5:
            status = "good"
            message = "Energy is solid. Keep going!"
            color = "#F5C542"
        elif level > 0.3:
            status = "low"
            message = "Energy dropping. Consider a break soon."
            color = "#E67E22"
        else:
            status = "critical"
            message = "Energy depleted. Take a break now."
            color = "#FF3747"
        
        return {
            "level": round(level, 2),
            "percent": round(level * 100),
            "status": status,
            "message": message,
            "color": color,
            "daily_peak": round(self.daily_peak * 100),
            "daily_low": round(self.daily_low * 100),
        }
    
    def get_graph_data(self, hours: int = 8) -> List[Dict]:
        """
        Get energy history for graphing.
        """
        cutoff = datetime.now() - timedelta(hours=hours)
        return [
            h for h in self.history
            if datetime.fromisoformat(h["timestamp"]) > cutoff
        ]
    
    def reset_daily(self):
        """
        Reset for new day.
        """
        self.energy = 0.8  # Start fresh but not at 100%
        self.daily_peak = self.energy
        self.daily_low = self.energy
        self.history = []


# Global tracker instance
_tracker = EnergyTracker()


def update_energy(event: str) -> float:
    """
    Update global energy tracker.
    """
    return _tracker.update(event)


def get_energy() -> float:
    """
    Get current energy level.
    """
    return _tracker.get_level()


def get_energy_status() -> Dict:
    """
    Get full energy status.
    """
    return _tracker.get_status()


def get_energy_graph(hours: int = 8) -> List[Dict]:
    """
    Get energy graph data.
    """
    return _tracker.get_graph_data(hours)

