"""
NoizyMind Multi-Agent System
============================
Multiple specialized agents that brainstorm, debate, and synthesize.
Each agent has domain expertise and unique perspective.
"""

from typing import List, Dict, Any


class BaseAgent:
    """
    Base class for all NoizyMind agents.
    """
    name = "BaseAgent"
    expertise = "general"
    
    def analyze(self, context: Dict) -> Dict:
        """
        Analyze context and return findings.
        """
        return {
            "agent": self.name,
            "expertise": self.expertise,
            "finding": "No specific findings.",
            "confidence": 0.5,
            "recommendation": None,
        }


class ExpertAgent(BaseAgent):
    """
    Expert diagnostician - sees patterns and recommends deep analysis.
    """
    name = "Expert"
    expertise = "diagnostics"
    
    def analyze(self, context: Dict) -> Dict:
        issues = context.get("issues", [])
        stats = context.get("stats", {})
        
        findings = []
        recommendations = []
        confidence = 0.7
        
        # Pattern detection
        if len(issues) > 3:
            findings.append(f"Detected {len(issues)} recurring issues")
            recommendations.append("deep_pattern_scan")
            confidence = 0.9
        
        # Performance analysis
        cpu = stats.get("cpu_usage", 0)
        ram = stats.get("ram_usage", 0)
        if cpu > 70 and ram > 70:
            findings.append("System under heavy load")
            recommendations.append("performance_optimization")
        
        return {
            "agent": self.name,
            "expertise": self.expertise,
            "finding": "; ".join(findings) if findings else "System patterns normal",
            "confidence": confidence,
            "recommendations": recommendations,
            "summary": "Expert sees issue patterns and recommends deep scan."
        }


class SecurityAgent(BaseAgent):
    """
    Security specialist - monitors threats and network integrity.
    """
    name = "Security"
    expertise = "security"
    
    def analyze(self, context: Dict) -> Dict:
        mesh = context.get("mesh", [])
        alerts = context.get("alerts", [])
        
        findings = []
        recommendations = []
        confidence = 0.8
        
        # Ghost device detection
        ghosts = [d for d in mesh if d.get("role") == "ghost"]
        if ghosts:
            findings.append(f"{len(ghosts)} unidentified device(s) on network")
            recommendations.append("threat_scan")
            recommendations.append("isolate_ghosts")
            confidence = 0.95
        
        # Alert analysis
        if alerts:
            findings.append(f"{len(alerts)} active security alerts")
            recommendations.append("alert_triage")
        
        return {
            "agent": self.name,
            "expertise": self.expertise,
            "finding": "; ".join(findings) if findings else "Network security nominal",
            "confidence": confidence,
            "recommendations": recommendations,
            "summary": "Security agent recommends LAN sweep + threat scan."
        }


class OptimizerAgent(BaseAgent):
    """
    Performance optimizer - balances loads and routes.
    """
    name = "Optimizer"
    expertise = "performance"
    
    def analyze(self, context: Dict) -> Dict:
        stats = context.get("stats", {})
        mesh = context.get("mesh", [])
        nodes = context.get("nodes", [])
        
        findings = []
        recommendations = []
        confidence = 0.75
        
        # Load balancing
        if nodes:
            loads = [n.get("load", 0) for n in nodes]
            avg_load = sum(loads) / len(loads) if loads else 0
            max_load = max(loads) if loads else 0
            
            if max_load > avg_load * 1.5:
                findings.append("Load imbalance detected across cluster")
                recommendations.append("rebalance_cluster")
        
        # Mesh optimization
        if len(mesh) > 10:
            findings.append("Large mesh detected - optimization possible")
            recommendations.append("optimize_routes")
        
        return {
            "agent": self.name,
            "expertise": self.expertise,
            "finding": "; ".join(findings) if findings else "Performance optimal",
            "confidence": confidence,
            "recommendations": recommendations,
            "summary": "Optimizer suggests balancing cluster load + mesh routes."
        }


class EmotionAgent(BaseAgent):
    """
    Emotional intelligence - monitors user state and adapts.
    """
    name = "Emotion"
    expertise = "emotional_intelligence"
    
    def analyze(self, context: Dict) -> Dict:
        mood = context.get("avg_mood", "neutral")
        stress = context.get("stress_level", 0)
        
        findings = []
        recommendations = []
        confidence = 0.7
        
        if mood == "distress" or stress > 5:
            findings.append("User showing signs of stress")
            recommendations.append("activate_calm_mode")
            recommendations.append("simplify_interface")
            confidence = 0.85
        
        return {
            "agent": self.name,
            "expertise": self.expertise,
            "finding": "; ".join(findings) if findings else "User state stable",
            "confidence": confidence,
            "recommendations": recommendations,
            "summary": "Emotion agent monitors user wellbeing."
        }


# Agent registry
AGENTS = [
    ExpertAgent(),
    SecurityAgent(),
    OptimizerAgent(),
    EmotionAgent(),
]


def run_all_agents(context: Dict) -> List[Dict]:
    """
    Run all agents and collect their analyses.
    """
    return [agent.analyze(context) for agent in AGENTS]


def agent_synth(context: Dict) -> List[str]:
    """
    Get summary outputs from all agents.
    """
    results = run_all_agents(context)
    return [r.get("summary", "") for r in results]


def get_all_recommendations(context: Dict) -> List[str]:
    """
    Collect all recommendations from all agents.
    """
    results = run_all_agents(context)
    recommendations = []
    for r in results:
        recommendations.extend(r.get("recommendations", []))
    return list(set(recommendations))  # Deduplicate

