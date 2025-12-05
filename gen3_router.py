from typing import Dict
from .meta_mind import meta_mind
from .synthesizer import synthesizer
import sys
sys.path.insert(0, '../..')
from noizy_ai_gen2.emotion_tags import tag_emotion
from noizy_ai_gen2.empathy_map import empathy_reply


class Gen3Router:
    """The complete GEN3 routing engine"""

    def __init__(self):
        self.meta_mind = meta_mind
        self.synthesizer = synthesizer

    def process(self, text: str, context: Dict = None) -> Dict:
        """Full GEN3 processing pipeline"""
        context = context or {}

        # Step 1: Emotion detection
        emotion = tag_emotion(text)
        empathy = empathy_reply(emotion)

        # Step 2: Select geniuses
        geniuses = self.meta_mind.select_geniuses(text)

        # Step 3: Parallel thinking
        thoughts = self.meta_mind.parallel_think(text)

        # Step 4: Synthesize
        synthesis = self.synthesizer.synthesize(thoughts, emotion)

        # Step 5: Build final response
        if emotion in ["distress", "sadness", "anger"]:
            final_response = f"{empathy} {synthesis['response']}"
        else:
            final_response = synthesis['response']

        return {
            "input": text,
            "emotion": emotion,
            "empathy_layer": empathy,
            "geniuses_used": [g["name"] for g in geniuses],
            "thoughts": thoughts,
            "synthesis": synthesis,
            "final_response": final_response,
            "gen_version": "3.0"
        }


gen3_router = Gen3Router()


def route_gen3(text: str, context: Dict = None) -> Dict:
    return gen3_router.process(text, context)

