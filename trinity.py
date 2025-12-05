# ROB OS - THE TRINITY
# =====================
# LIFELUV • 2NDLIFE • FLOW
# Everything you do plugs into ONE of these. If it doesn't → it's noise.

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

class TrinityPillar(Enum):
    LIFELUV = "lifeluv"     # Life support - home, money, health, marriage, calm
    SECONDLIFE = "2ndlife"  # Second act - earning power from what you already are
    FLOW = "flow"           # Daily rhythm - routines, automation, energy management

@dataclass
class LifeluvStatus:
    """LIFELUV = Your life support. Does this make life softer for Rob & Carolynne?"""
    
    # Home & Environment
    home_chaos_level: str = "unknown"  # "calm", "manageable", "chaotic"
    environment_notes: List[str] = field(default_factory=list)
    
    # Money & Safety
    monthly_comfort_target: float = 0.0
    current_monthly: float = 0.0
    emergency_fund_months: int = 0
    
    # Health & Body
    energy_today: str = "medium"  # "high", "medium", "low", "depleted"
    pain_level: int = 0  # 0-10
    hand_strain_risk: str = "low"  # "low", "medium", "high"
    
    # Love & Time with Carolynne
    quality_time_this_week: int = 0  # hours
    protected_rituals: List[str] = field(default_factory=list)
    
    def get_priority_actions(self) -> List[str]:
        actions = []
        if self.monthly_comfort_target == 0:
            actions.append("💰 Define your monthly comfort number")
        if self.home_chaos_level == "chaotic":
            actions.append("🏠 Make home feel less chaotic")
        if len(self.protected_rituals) == 0:
            actions.append("❤️ Protect 1 small ritual with Carolynne")
        return actions

@dataclass
class SecondLifeStatus:
    """2NDLIFE = Your second act. Does this build long-term earning power from what you already are?"""
    
    # NoizyLab (repairs & automation)
    noizylab_active_clients: int = 0
    noizylab_vip_retainers: int = 0
    noizylab_pipeline: List[str] = field(default_factory=list)
    
    # FishMusic / 2NDLIFE (audio & analog)
    fishmusic_active_projects: int = 0
    analog_revival_queue: List[str] = field(default_factory=list)
    
    # Heritage / AI IP
    heritage_assets: List[str] = field(default_factory=list)
    voice_model_status: str = "not_started"  # "not_started", "recording", "training", "ready"
    
    # Network & Opportunities
    warm_leads: List[str] = field(default_factory=list)
    partnerships: List[str] = field(default_factory=list)
    
    def get_revenue_estimate(self) -> Dict[str, float]:
        return {
            "noizylab_services": self.noizylab_active_clients * 150,  # avg per client
            "noizylab_retainers": self.noizylab_vip_retainers * 150,  # monthly
            "fishmusic": self.fishmusic_active_projects * 300,  # avg per project
            "total_monthly": (self.noizylab_active_clients * 150) + 
                            (self.noizylab_vip_retainers * 150) + 
                            (self.fishmusic_active_projects * 300)
        }

@dataclass
class FlowStatus:
    """FLOW = Your daily rhythm. Does this make your days smoother and lighter?"""
    
    # Current day structure
    current_phase: str = "idle"  # "intro", "verse1", "chorus", "verse2", "outro", "idle"
    work_blocks_completed: int = 0
    recovery_breaks_taken: int = 0
    
    # Energy tracking
    morning_energy: str = "medium"
    current_energy: str = "medium"
    
    # Automation status
    automations_active: List[str] = field(default_factory=list)
    shortcuts_available: List[str] = field(default_factory=list)
    
    # Daily log
    today_wins: List[str] = field(default_factory=list)
    today_blockers: List[str] = field(default_factory=list)
    
    def get_day_structure(self) -> Dict[str, Any]:
        """The day as a song structure."""
        return {
            "intro": {
                "name": "Wake / Warm-up",
                "duration": "30 min",
                "activity": "Coffee + short check-in with MC96, not doomscroll"
            },
            "verse1": {
                "name": "Work Block 1",
                "duration": "60-90 min",
                "activity": "Focused on 2NDLIFE or NoizyLab (revenue-first)"
            },
            "chorus": {
                "name": "Recovery",
                "duration": "15-30 min",
                "activity": "Sound, breathing, ASMR, stretch"
            },
            "verse2": {
                "name": "Work Block 2",
                "duration": "60-90 min",
                "activity": "Systems / infra / automation (reduce future effort)"
            },
            "outro": {
                "name": "Shutdown",
                "duration": "15 min",
                "activity": "Quick journal: 'What did I move forward today?'"
            }
        }


class TrinityManager:
    """
    The Trinity Manager - Keeps LIFELUV, 2NDLIFE, and FLOW in balance.
    """
    
    def __init__(self):
        self.lifeluv = LifeluvStatus()
        self.secondlife = SecondLifeStatus()
        self.flow = FlowStatus()
        
        # Non-negotiable rules
        self.rules = [
            "If it hurts your body more than it helps your future → automate or ditch",
            "If it doesn't serve LIFELUV, 2NDLIFE, or FLOW → it goes on 'Someday/Maybe'",
            "If it makes money AND makes things calmer → it's top priority",
            "If it drains you and pays badly → it's on the chopping block"
        ]
        
        # Forever filter
        self.forever_filter = {
            "prioritize": "Money + comfort for Rob & Carolynne",
            "reduce": "Hand strain, chaos, decision fatigue",
            "default_to": "Automation, AI-as-hands, systems > one-offs",
            "keep_inside": "LIFELUV / 2NDLIFE / FLOW",
            "push_back_on": "Stuff that's cool but doesn't move those dials"
        }
    
    def classify_task(self, task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Classify a task into the Trinity.
        """
        task_lower = task.lower()
        
        # LIFELUV indicators
        lifeluv_keywords = ["home", "carolynne", "health", "money", "calm", "rest", "marriage", "comfort"]
        
        # 2NDLIFE indicators
        secondlife_keywords = ["noizylab", "fishmusic", "client", "repair", "audio", "heritage", 
                              "revenue", "sell", "service", "business"]
        
        # FLOW indicators
        flow_keywords = ["routine", "automate", "shortcut", "morning", "evening", "energy", 
                        "workflow", "system", "organize"]
        
        scores = {
            TrinityPillar.LIFELUV: sum(1 for k in lifeluv_keywords if k in task_lower),
            TrinityPillar.SECONDLIFE: sum(1 for k in secondlife_keywords if k in task_lower),
            TrinityPillar.FLOW: sum(1 for k in flow_keywords if k in task_lower)
        }
        
        max_score = max(scores.values())
        if max_score == 0:
            return {
                "pillar": None,
                "classification": "noise",
                "recommendation": "This doesn't clearly serve LIFELUV, 2NDLIFE, or FLOW. Consider: Someday/Maybe list."
            }
        
        pillar = max(scores, key=scores.get)
        return {
            "pillar": pillar.value,
            "classification": "aligned",
            "recommendation": f"This serves {pillar.value.upper()}. Proceed."
        }
    
    def get_dashboard(self) -> Dict[str, Any]:
        """
        Get the Trinity dashboard overview.
        """
        revenue = self.secondlife.get_revenue_estimate()
        
        return {
            "lifeluv": {
                "status": "needs_attention" if self.lifeluv.monthly_comfort_target == 0 else "tracking",
                "comfort_target": self.lifeluv.monthly_comfort_target,
                "current_monthly": self.lifeluv.current_monthly,
                "gap": max(0, self.lifeluv.monthly_comfort_target - self.lifeluv.current_monthly),
                "priority_actions": self.lifeluv.get_priority_actions()
            },
            "secondlife": {
                "status": "active" if revenue["total_monthly"] > 0 else "building",
                "estimated_monthly": revenue["total_monthly"],
                "active_clients": self.secondlife.noizylab_active_clients,
                "vip_retainers": self.secondlife.noizylab_vip_retainers,
                "voice_model": self.secondlife.voice_model_status
            },
            "flow": {
                "current_phase": self.flow.current_phase,
                "energy": self.flow.current_energy,
                "work_blocks_done": self.flow.work_blocks_completed,
                "today_wins": len(self.flow.today_wins)
            },
            "rules": self.rules,
            "forever_filter": self.forever_filter
        }
    
    def set_comfort_target(self, monthly_amount: float):
        """Set the monthly comfort target."""
        self.lifeluv.monthly_comfort_target = monthly_amount
    
    def add_protected_ritual(self, ritual: str):
        """Add a protected ritual with Carolynne."""
        self.lifeluv.protected_rituals.append(ritual)
    
    def log_win(self, win: str):
        """Log a win for today."""
        self.flow.today_wins.append(win)
    
    def advance_flow_phase(self) -> str:
        """Advance to the next phase of the day."""
        phases = ["intro", "verse1", "chorus", "verse2", "outro", "idle"]
        current_idx = phases.index(self.flow.current_phase) if self.flow.current_phase in phases else -1
        
        if current_idx < len(phases) - 1:
            self.flow.current_phase = phases[current_idx + 1]
            if self.flow.current_phase in ["verse1", "verse2"]:
                self.flow.work_blocks_completed += 1
            elif self.flow.current_phase == "chorus":
                self.flow.recovery_breaks_taken += 1
        
        return self.flow.current_phase


# Singleton instance
_trinity = None

def get_trinity() -> TrinityManager:
    global _trinity
    if _trinity is None:
        _trinity = TrinityManager()
    return _trinity

