from typing import Dict, List


class WeightedSynthesizer:
    """Combines multiple genius thoughts into a unified response"""

    def __init__(self):
        self.weights = {
            "accessibility": 1.5,  # Accessibility always prioritized
            "comfort": 1.3,
            "psychology": 1.2,
            "security": 1.1,
        }

    def synthesize(self, thoughts: List[Dict], emotion: str = "neutral") -> Dict:
        """Synthesize multiple genius thoughts into one response"""
        if not thoughts:
            return {
                "response": "I'm here to help. Tell me more about what you need.",
                "sources": []
            }

        # Weight by domain importance
        weighted_thoughts = []
        for thought in thoughts:
            domain = thought.get("domain", "general")
            weight = self.weights.get(domain, 1.0)
            
            # Boost comfort/accessibility if distress detected
            if emotion in ["distress", "sadness", "anger"]:
                if domain in ["comfort", "psychology", "accessibility"]:
                    weight *= 1.5

            weighted_thoughts.append({
                **thought,
                "weight": weight
            })

        # Sort by weight
        weighted_thoughts.sort(key=lambda x: x["weight"], reverse=True)

        # Build response from top thoughts
        primary = weighted_thoughts[0]
        supporting = weighted_thoughts[1:3] if len(weighted_thoughts) > 1 else []

        response_parts = [
            f"[{primary['genius_name']}] {primary['thought']}"
        ]

        for s in supporting:
            response_parts.append(f"Additionally, {s['genius_name']} suggests: {s['thought']}")

        return {
            "response": " ".join(response_parts),
            "primary_genius": primary["genius_name"],
            "sources": [t["genius_name"] for t in weighted_thoughts],
            "emotion_boost": emotion in ["distress", "sadness", "anger"]
        }


synthesizer = WeightedSynthesizer()

