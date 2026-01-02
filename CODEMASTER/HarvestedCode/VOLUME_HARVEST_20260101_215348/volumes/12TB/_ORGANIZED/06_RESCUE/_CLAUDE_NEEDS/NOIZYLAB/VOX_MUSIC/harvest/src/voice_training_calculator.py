#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎤 VOICE MODEL TRAINING CALCULATOR 🎤                             ║
║                                                                           ║
║  Calculate optimal training data for perfect voice cloning              ║
║  with full emotional range and behavioral patterns                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class VoiceModelRequirements:
    """Voice model training requirements."""
    quality_level: str
    total_words: int
    unique_sentences: int
    recording_minutes: int
    emotions_covered: List[str]
    behaviors_covered: List[str]
    phoneme_coverage: float
    recommended_sessions: int


class VoiceTrainingCalculator:
    """Calculate training data requirements for voice models."""

    def __init__(self):
        # Emotion categories
        self.emotions = {
            "happiness": ["joy", "excitement", "contentment", "amusement"],
            "sadness": ["sorrow", "disappointment", "melancholy", "grief"],
            "anger": ["frustration", "irritation", "rage", "annoyance"],
            "fear": ["anxiety", "worry", "terror", "nervousness"],
            "surprise": ["shock", "amazement", "astonishment", "wonder"],
            "disgust": ["revulsion", "distaste", "contempt"],
            "neutral": ["calm", "factual", "observational"],
            "love": ["affection", "tenderness", "warmth", "caring"],
        }

        # Behavioral patterns
        self.behaviors = {
            "teaching": ["explaining", "instructing", "guiding", "demonstrating"],
            "storytelling": ["narrating", "describing", "dramatizing", "captivating"],
            "conversing": ["chatting", "discussing", "debating", "questioning"],
            "commanding": ["directing", "ordering", "leading", "authorizing"],
            "comforting": ["soothing", "reassuring", "supporting", "empathizing"],
            "entertaining": ["joking", "playing", "performing", "amusing"],
            "professional": ["presenting", "reporting", "analyzing", "summarizing"],
            "casual": ["relaxed", "informal", "friendly", "spontaneous"],
        }

        # Voice quality levels
        self.quality_levels = {
            "basic": {
                "description": "Basic voice recognition, limited emotional range",
                "word_count": (500, 1000),
                "sentences": (50, 100),
                "minutes": (5, 10),
                "emotion_coverage": 0.3,  # 30%
                "behavior_coverage": 0.25,  # 25%
                "phoneme_coverage": 0.6,  # 60%
                "sessions": (1, 2),
            },
            "standard": {
                "description": "Good voice quality, moderate emotional expression",
                "word_count": (2000, 5000),
                "sentences": (200, 500),
                "minutes": (20, 50),
                "emotion_coverage": 0.6,  # 60%
                "behavior_coverage": 0.5,  # 50%
                "phoneme_coverage": 0.85,  # 85%
                "sessions": (3, 5),
            },
            "professional": {
                "description": "High-quality voice, full emotional range",
                "word_count": (10000, 20000),
                "sentences": (1000, 2000),
                "minutes": (100, 200),
                "emotion_coverage": 0.9,  # 90%
                "behavior_coverage": 0.8,  # 80%
                "phoneme_coverage": 0.95,  # 95%
                "sessions": (5, 10),
            },
            "perfect": {
                "description": "Perfect voice clone, complete emotional & behavioral range",
                "word_count": (30000, 50000),
                "sentences": (3000, 5000),
                "minutes": (300, 500),
                "emotion_coverage": 1.0,  # 100%
                "behavior_coverage": 1.0,  # 100%
                "phoneme_coverage": 0.99,  # 99%
                "sessions": (10, 20),
            }
        }

    def calculate_requirements(self, quality: str = "professional") -> VoiceModelRequirements:
        """Calculate voice model requirements for a quality level."""
        if quality not in self.quality_levels:
            quality = "professional"

        level = self.quality_levels[quality]

        # Calculate emotional coverage
        emotions_needed = int(len(self.emotions) * level["emotion_coverage"])
        emotions_list = list(self.emotions.keys())[:emotions_needed]

        # Calculate behavioral coverage
        behaviors_needed = int(len(self.behaviors) * level["behavior_coverage"])
        behaviors_list = list(self.behaviors.keys())[:behaviors_needed]

        # Get average values
        word_count = (level["word_count"][0] + level["word_count"][1]) // 2
        sentences = (level["sentences"][0] + level["sentences"][1]) // 2
        minutes = (level["minutes"][0] + level["minutes"][1]) // 2
        sessions = (level["sessions"][0] + level["sessions"][1]) // 2

        return VoiceModelRequirements(
            quality_level=quality,
            total_words=word_count,
            unique_sentences=sentences,
            recording_minutes=minutes,
            emotions_covered=emotions_list,
            behaviors_covered=behaviors_list,
            phoneme_coverage=level["phoneme_coverage"],
            recommended_sessions=sessions
        )

    def generate_training_script(self, quality: str = "professional") -> Dict:
        """Generate a training script with recommended phrases."""
        req = self.calculate_requirements(quality)

        script = {
            "overview": {
                "quality_level": quality,
                "total_words": req.total_words,
                "total_sentences": req.unique_sentences,
                "recording_time": f"{req.recording_minutes} minutes",
                "sessions": req.recommended_sessions,
            },
            "emotions_to_capture": {},
            "behaviors_to_demonstrate": {},
            "example_phrases": []
        }

        # Generate emotional examples
        for emotion in req.emotions_covered:
            variations = self.emotions[emotion]
            script["emotions_to_capture"][emotion] = {
                "variations": variations,
                "required_samples": len(variations) * 3  # 3 samples per variation
            }

        # Generate behavioral examples
        for behavior in req.behaviors_covered:
            variations = self.behaviors[behavior]
            script["behaviors_to_demonstrate"][behavior] = {
                "variations": variations,
                "required_samples": len(variations) * 3
            }

        # Example phrases for each emotion/behavior combo
        examples = [
            # Teaching + Happiness
            "I'm so excited to share this amazing discovery with you!",
            "Let me show you how wonderfully this works!",

            # Storytelling + Surprise
            "And then, out of nowhere, the most incredible thing happened!",
            "You won't believe what I saw next!",

            # Conversing + Neutral
            "That's an interesting point of view. Tell me more about it.",
            "I understand what you're saying. Let's explore that further.",

            # Commanding + Anger
            "Stop that immediately! This is unacceptable!",
            "I will not tolerate this behavior any longer!",

            # Comforting + Love
            "Everything's going to be alright. I'm here for you.",
            "You're so important to me. Never forget that.",

            # Professional + Neutral
            "According to the latest research, we can conclude that...",
            "The data suggests a clear trend in this direction.",

            # Casual + Happiness
            "Oh man, that's hilarious! Tell me another one!",
            "This is so cool! I can't wait to try it!",

            # Storytelling + Fear
            "The shadows grew darker, and I could feel something watching...",
            "My heart pounded as I realized what was about to happen.",
        ]

        script["example_phrases"] = examples[:20]  # Limit to 20 examples

        return script

    def print_analysis(self):
        """Print comprehensive analysis of all quality levels."""
        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎤 VOICE MODEL TRAINING REQUIREMENTS ANALYSIS 🎤                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
        """)

        for quality_name, quality_data in self.quality_levels.items():
            print(f"\n{'='*75}")
            print(f"🎯 {quality_name.upper()} QUALITY")
            print(f"{'='*75}")
            print(f"\n📝 Description: {quality_data['description']}")
            print(f"\n📊 Requirements:")
            print(f"   Words:          {quality_data['word_count'][0]:,} - {quality_data['word_count'][1]:,}")
            print(f"   Sentences:      {quality_data['sentences'][0]:,} - {quality_data['sentences'][1]:,}")
            print(f"   Recording Time: {quality_data['minutes'][0]}-{quality_data['minutes'][1]} minutes")
            print(f"   Sessions:       {quality_data['sessions'][0]}-{quality_data['sessions'][1]} recording sessions")
            print(f"\n🎭 Coverage:")
            print(f"   Emotions:       {quality_data['emotion_coverage']*100:.0f}%")
            print(f"   Behaviors:      {quality_data['behavior_coverage']*100:.0f}%")
            print(f"   Phonemes:       {quality_data['phoneme_coverage']*100:.0f}%")

            req = self.calculate_requirements(quality_name)
            print(f"\n✅ Emotional Range ({len(req.emotions_covered)} categories):")
            for emotion in req.emotions_covered:
                print(f"      {emotion.title()}")

            print(f"\n✅ Behavioral Patterns ({len(req.behaviors_covered)} patterns):")
            for behavior in req.behaviors_covered:
                print(f"      {behavior.title()}")

        print(f"\n\n{'='*75}")
        print("🎯 RECOMMENDATIONS FOR FISHY STORYS & MUSIC ISLAND")
        print(f"{'='*75}\n")

        print("For Children's Content (FISHY STORYS, MUSIC ISLAND):")
        print("\n   Recommended Quality: PROFESSIONAL to PERFECT")
        print("\n   Why?")
        print("   ✓ Children respond strongly to emotional authenticity")
        print("   ✓ Educational content needs clarity and engagement")
        print("   ✓ Storytelling requires full dramatic range")
        print("   ✓ Music instruction needs precise tonal control")
        print("\n   Suggested Approach:")
        print("   1. Start with PROFESSIONAL (10,000-20,000 words)")
        print("   2. Focus on happy, excited, teaching emotions")
        print("   3. Emphasize storytelling and teaching behaviors")
        print("   4. Record in 5-10 sessions for consistency")
        print("   5. Include musical phrases and rhythmic speech")
        print()


def main():
    """Main entry point."""
    calculator = VoiceTrainingCalculator()

    calculator.print_analysis()

    print("\n" + "="*75)
    print("📋 GENERATING SAMPLE TRAINING SCRIPT (PROFESSIONAL)")
    print("="*75 + "\n")

    script = calculator.generate_training_script("professional")

    print("Overview:")
    for key, value in script["overview"].items():
        print(f"  {key}: {value}")

    print(f"\nEmotions to Capture: {len(script['emotions_to_capture'])}")
    print(f"Behaviors to Demonstrate: {len(script['behaviors_to_demonstrate'])}")

    print("\nExample Training Phrases (20 of many):")
    for i, phrase in enumerate(script["example_phrases"], 1):
        print(f"  {i}. \"{phrase}\"")

    print("\n" + "="*75)
    print("\n💡 TIP: For best results, record in a quiet environment")
    print("        with consistent distance from microphone (6-8 inches)")
    print()

    return 0


if __name__ == "__main__":
    main()
