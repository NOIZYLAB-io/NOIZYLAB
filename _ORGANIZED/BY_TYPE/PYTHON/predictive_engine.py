from typing import Dict, List, Optional
import time

USER_CONTEXT = {}


class PredictiveEngine:
    """
    Predicts what the user needs next before they ask.
    Auto-triggers actions based on context and patterns.
    """

    def __init__(self):
        self.patterns = {
            "slow": ["run_performance_scan", "check_memory", "analyze_startup"],
            "noise": ["check_fans", "check_hdd_health", "thermal_scan"],
            "crash": ["check_logs", "memory_test", "driver_check"],
            "virus": ["malware_scan", "quarantine_check", "browser_reset"],
            "network": ["ping_test", "dns_check", "router_status"],
            "stress": ["activate_calm_mode", "simplify_ui", "slow_animations"],
            "confused": ["show_help_bubble", "voice_suggestion", "step_by_step"],
        }

        self.micro_empathy = [
            "Hold on — I've got you. Let me check that for you.",
            "One sec, I'm on it.",
            "Let me take a look at that for you.",
            "I see what's happening. Give me a moment.",
            "Got it. Working on this now.",
        ]

    def predict_action(self, user_input: str, context: Dict = None) -> Dict:
        """Predict and suggest next actions"""
        input_lower = user_input.lower()
        suggested_actions = []

        for keyword, actions in self.patterns.items():
            if keyword in input_lower:
                suggested_actions.extend(actions)

        return {
            "predicted_actions": suggested_actions[:3],
            "confidence": len(suggested_actions) / 10,
            "auto_trigger": len(suggested_actions) > 0
        }

    def get_empathy_response(self) -> str:
        """Get a micro-empathy response"""
        import random
        return random.choice(self.micro_empathy)

    def detect_hesitation(self, typing_speed: float, pauses: int) -> bool:
        """Detect if user is hesitating"""
        return typing_speed < 2.0 or pauses > 3

    def should_show_help(self, context: Dict) -> bool:
        """Determine if help bubble should appear"""
        return (
            context.get("hesitation", False) or
            context.get("repeated_question", False) or
            context.get("error_count", 0) > 2
        )


class FlowThread:
    """Remembers last 4 steps and connects them seamlessly"""

    def __init__(self, user_id: str):
        self.user_id = user_id
        if user_id not in USER_CONTEXT:
            USER_CONTEXT[user_id] = {"steps": [], "start": time.time()}
        self.context = USER_CONTEXT[user_id]

    def add_step(self, step: str, data: Dict = None):
        self.context["steps"].append({
            "step": step,
            "data": data or {},
            "timestamp": time.time()
        })
        # Keep only last 4
        self.context["steps"] = self.context["steps"][-4:]

    def get_flow(self) -> List[Dict]:
        return self.context["steps"]

    def get_summary(self) -> str:
        steps = self.context["steps"]
        if not steps:
            return "Starting fresh."
        return f"We've covered: {', '.join([s['step'] for s in steps])}"


predictive = PredictiveEngine()

