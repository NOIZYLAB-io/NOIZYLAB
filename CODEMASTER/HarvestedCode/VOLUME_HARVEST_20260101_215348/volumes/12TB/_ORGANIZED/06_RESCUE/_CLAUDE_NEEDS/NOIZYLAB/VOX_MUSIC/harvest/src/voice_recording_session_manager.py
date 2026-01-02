#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎙️ VOICE RECORDING SESSION MANAGER 🎙️                           ║
║                                                                           ║
║  Professional multi-character voice recording system                     ║
║  Tracks sessions, provides scripts, manages quality control              ║
║  Part of VOX - Voice Control Application                                 ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class RecordingSession:
    """A single voice recording session."""
    session_id: str
    date: str
    character_id: str
    character_name: str
    session_number: int  # Which session for this character

    # Recording details
    target_words: int
    actual_words: int
    duration_minutes: int

    # Quality metrics
    phrases_recorded: List[str]
    emotions_covered: List[str]
    behaviors_covered: List[str]

    # Technical info
    audio_files: List[str]
    sample_rate: int
    format: str

    # Notes
    notes: str
    issues: List[str]
    retakes_needed: List[str]


@dataclass
class CharacterVoiceProfile:
    """Complete voice profile for a character."""
    character_id: str
    character_name: str
    voice_description: str

    # Target requirements (from voice_training_calculator)
    target_quality: str  # basic, standard, professional, perfect
    target_words: int
    target_sessions: int

    # Progress
    total_words_recorded: int
    total_sessions_completed: int
    total_recording_time: int  # minutes

    # Coverage
    emotions_covered: List[str]
    behaviors_covered: List[str]
    phoneme_coverage_estimate: float

    # Sessions
    session_ids: List[str]

    # Status
    is_complete: bool
    completion_percentage: float

    # Voice model info
    voice_model_path: Optional[str]
    voice_model_trained: bool


class VoiceRecordingSessionManager:
    """Manage voice recording sessions for all characters."""

    def __init__(self):
        self.base_path = Path("/Users/rsp_ms/MC96_MobileApp/VOX")
        self.sessions_dir = self.base_path / "voice_recordings" / "SESSIONS"
        self.profiles_dir = self.base_path / "voice_recordings" / "PROFILES"
        self.scripts_dir = self.base_path / "voice_recordings" / "SCRIPTS"
        self.audio_dir = self.base_path / "voice_recordings" / "AUDIO"

        # Create directories
        for dir_path in [self.sessions_dir, self.profiles_dir, self.scripts_dir, self.audio_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)

        # Import character data from other systems
        self.load_character_definitions()

        # Recording script templates
        self.script_templates = self.create_script_templates()

    def load_character_definitions(self):
        """Load character definitions from FISHY STORYS and MUSIC ISLAND."""
        # These would be imported from fishy_storys_generator.py and music_island_generator.py
        # For now, we'll define the core ones

        self.characters = {
            # FISHY STORYS Characters
            "captain_finn": {
                "name": "Captain Finn",
                "description": "Wise old fish captain, deep soothing voice (60s)",
                "target_quality": "professional",
                "voice_traits": {
                    "age": "elderly male (60s)",
                    "pitch": "medium-low",
                    "speed": "slow, deliberate",
                    "accent": "slight nautical",
                    "personality": "warm, wise, patient",
                },
            },
            "bubbles": {
                "name": "Bubbles",
                "description": "Cheerful little goldfish, bubbly high voice (6-8 child)",
                "target_quality": "professional",
                "voice_traits": {
                    "age": "young child (6-8)",
                    "pitch": "high",
                    "speed": "fast, excited",
                    "accent": "none",
                    "personality": "energetic, curious, happy",
                },
            },
            "professor_scales": {
                "name": "Professor Scales",
                "description": "Smart academic fish, clear teaching voice (40s)",
                "target_quality": "professional",
                "voice_traits": {
                    "age": "middle-aged (40s)",
                    "pitch": "medium",
                    "speed": "normal, articulate",
                    "accent": "educated British",
                    "personality": "intelligent, patient, encouraging",
                },
            },
            "marina_melody": {
                "name": "Marina Melody",
                "description": "Musical fish singer, melodic voice (30s)",
                "target_quality": "professional",
                "voice_traits": {
                    "age": "adult female (30s)",
                    "pitch": "medium-high",
                    "speed": "flowing, musical",
                    "accent": "slight Italian",
                    "personality": "artistic, expressive, joyful",
                },
            },
            "reef_explorer": {
                "name": "Reef the Explorer",
                "description": "Adventurous young fish, excited voice (12-14 teen)",
                "target_quality": "professional",
                "voice_traits": {
                    "age": "young teen (12-14)",
                    "pitch": "medium",
                    "speed": "fast, enthusiastic",
                    "accent": "American",
                    "personality": "brave, curious, energetic",
                },
            },
            "grandma_pearl": {
                "name": "Grandma Pearl",
                "description": "Loving grandma fish, warm gentle voice (80s)",
                "target_quality": "professional",
                "voice_traits": {
                    "age": "elderly female (80s)",
                    "pitch": "medium",
                    "speed": "slow, gentle",
                    "accent": "Southern comfort",
                    "personality": "loving, nurturing, wise",
                },
            },

            # MUSIC ISLAND Teachers
            "maestro_melody": {
                "name": "Maestro Melody",
                "description": "Wise music teacher, encouraging voice",
                "target_quality": "professional",
                "voice_traits": {
                    "age": "mature male (50s)",
                    "pitch": "medium",
                    "speed": "measured, clear",
                    "accent": "cultured European",
                    "personality": "wise, encouraging, patient",
                },
            },
            "rhythm_ray": {
                "name": "Rhythm Ray",
                "description": "Energetic percussion teacher, upbeat voice",
                "target_quality": "professional",
                "voice_traits": {
                    "age": "adult male (30s)",
                    "pitch": "medium-high",
                    "speed": "fast, rhythmic",
                    "accent": "urban American",
                    "personality": "energetic, fun, motivating",
                },
            },
            "harmony_hana": {
                "name": "Harmony Hana",
                "description": "Gentle piano teacher, sweet melodic voice",
                "target_quality": "professional",
                "voice_traits": {
                    "age": "adult female (30s)",
                    "pitch": "medium-high",
                    "speed": "flowing, gentle",
                    "accent": "soft Japanese",
                    "personality": "gentle, nurturing, artistic",
                },
            },
        }

    def create_script_templates(self) -> Dict:
        """Create recording script templates for different scenarios."""
        return {
            "greeting": [
                "Hello! Welcome to {location}!",
                "Hi there! I'm so glad you're here!",
                "Good to see you! Ready to learn something amazing?",
                "Hey friend! Let's have some fun today!",
                "Greetings! What an adventure we'll have!",
            ],

            "teaching": [
                "Let me show you how this works.",
                "Pay attention, this is really important!",
                "Here's a cool way to think about it.",
                "Watch carefully and follow along.",
                "I'll explain this step by step.",
            ],

            "encouraging": [
                "You're doing great! Keep going!",
                "Wonderful! You're really getting it!",
                "Excellent work! I'm so proud of you!",
                "That's it! You've got the hang of it!",
                "Fantastic! You're a natural!",
            ],

            "storytelling": [
                "Once upon a time, in the deep blue ocean...",
                "Let me tell you an amazing story!",
                "You won't believe what happened next!",
                "Long ago, when the sea was young...",
                "Gather round, I have a tale to share!",
            ],

            "questioning": [
                "What do you think will happen?",
                "Can you figure out the answer?",
                "Why do you suppose that is?",
                "What would you do in this situation?",
                "How does that make you feel?",
            ],

            "emotional_happy": [
                "This is so exciting! I can hardly contain my joy!",
                "What a wonderful day this has turned out to be!",
                "I'm so happy I could dance!",
                "This brings such warmth to my heart!",
                "Nothing could make me happier than this!",
            ],

            "emotional_sad": [
                "Oh dear, that makes me feel quite blue.",
                "Sometimes things don't go the way we hope.",
                "It's okay to feel sad sometimes.",
                "I understand how disappointing this must be.",
                "Even in sadness, we can find hope.",
            ],

            "emotional_excited": [
                "Oh my gosh! This is incredible!",
                "I can't wait! This is going to be amazing!",
                "Wow wow wow! Can you believe this?!",
                "This is the best thing ever!",
                "I'm so pumped up! Let's do this!",
            ],

            "comforting": [
                "It's going to be alright. I'm here for you.",
                "Don't worry, we'll figure this out together.",
                "You're safe now. Everything will be okay.",
                "Take a deep breath. I've got you.",
                "Remember, you're never alone in this.",
            ],

            "musical": [
                "♪ La la la, let the music flow! ♪",
                "Can you hear the rhythm in your heart?",
                "Music is the language of the soul!",
                "Let's make some beautiful sounds together!",
                "Feel the beat, let it move you!",
            ],
        }

    def create_character_profile(
        self,
        character_id: str,
        target_quality: str = "professional"
    ) -> CharacterVoiceProfile:
        """Create a new voice profile for a character."""

        if character_id not in self.characters:
            raise ValueError(f"Unknown character: {character_id}")

        char_info = self.characters[character_id]

        # Get target words from quality level
        quality_targets = {
            "basic": 750,
            "standard": 3500,
            "professional": 15000,
            "perfect": 40000,
        }

        quality_sessions = {
            "basic": 2,
            "standard": 4,
            "professional": 8,
            "perfect": 15,
        }

        profile = CharacterVoiceProfile(
            character_id=character_id,
            character_name=char_info["name"],
            voice_description=char_info["description"],
            target_quality=target_quality,
            target_words=quality_targets.get(target_quality, 15000),
            target_sessions=quality_sessions.get(target_quality, 8),
            total_words_recorded=0,
            total_sessions_completed=0,
            total_recording_time=0,
            emotions_covered=[],
            behaviors_covered=[],
            phoneme_coverage_estimate=0.0,
            session_ids=[],
            is_complete=False,
            completion_percentage=0.0,
            voice_model_path=None,
            voice_model_trained=False,
        )

        self.save_character_profile(profile)
        return profile

    def save_character_profile(self, profile: CharacterVoiceProfile):
        """Save character profile to JSON."""
        filename = f"{profile.character_id}_profile.json"
        filepath = self.profiles_dir / filename

        with open(filepath, 'w') as f:
            json.dump(asdict(profile), f, indent=2)

    def load_character_profile(self, character_id: str) -> Optional[CharacterVoiceProfile]:
        """Load character profile from JSON."""
        filename = f"{character_id}_profile.json"
        filepath = self.profiles_dir / filename

        if not filepath.exists():
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)

        return CharacterVoiceProfile(**data)

    def create_recording_session(
        self,
        character_id: str,
        target_words: int = 1875
    ) -> RecordingSession:
        """Create a new recording session for a character."""

        profile = self.load_character_profile(character_id)
        if not profile:
            profile = self.create_character_profile(character_id)

        session_number = profile.total_sessions_completed + 1
        session_id = f"{character_id}_session_{session_number}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        session = RecordingSession(
            session_id=session_id,
            date=datetime.now().isoformat(),
            character_id=character_id,
            character_name=profile.character_name,
            session_number=session_number,
            target_words=target_words,
            actual_words=0,
            duration_minutes=0,
            phrases_recorded=[],
            emotions_covered=[],
            behaviors_covered=[],
            audio_files=[],
            sample_rate=44100,
            format="WAV",
            notes="",
            issues=[],
            retakes_needed=[],
        )

        self.save_recording_session(session)
        return session

    def save_recording_session(self, session: RecordingSession):
        """Save recording session to JSON."""
        filename = f"{session.session_id}.json"
        filepath = self.sessions_dir / filename

        with open(filepath, 'w') as f:
            json.dump(asdict(session), f, indent=2)

    def load_recording_session(self, session_id: str) -> Optional[RecordingSession]:
        """Load recording session from JSON."""
        filename = f"{session_id}.json"
        filepath = self.sessions_dir / filename

        if not filepath.exists():
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)

        return RecordingSession(**data)

    def generate_recording_script(
        self,
        character_id: str,
        session_number: int,
        target_words: int = 1875
    ) -> str:
        """Generate a recording script for a session."""

        char_info = self.characters[character_id]

        script = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎙️ RECORDING SCRIPT - SESSION {session_number} 🎙️                          ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

CHARACTER: {char_info['name']}
DATE: {datetime.now().strftime('%Y-%m-%d')}
TARGET WORDS: {target_words}
ESTIMATED TIME: {target_words // 150} - {target_words // 100} minutes

═══════════════════════════════════════════════════════════════════════════

📝 VOICE PROFILE:
   Age/Type: {char_info['voice_traits']['age']}
   Pitch: {char_info['voice_traits']['pitch']}
   Speed: {char_info['voice_traits']['speed']}
   Accent: {char_info['voice_traits']['accent']}
   Personality: {char_info['voice_traits']['personality']}

═══════════════════════════════════════════════════════════════════════════

🎯 SESSION GOALS:
   □ Record ~{target_words} words
   □ Cover 3-4 different emotions
   □ Include 2-3 behavior types
   □ Maintain consistent character voice
   □ Keep energy levels appropriate

═══════════════════════════════════════════════════════════════════════════

🎬 WARM-UP (5 minutes):

Before we start recording, let's warm up your voice in character!

1. Breathing exercises (30 seconds)
2. Lip trills and tongue twisters (1 minute)
3. Speak these phrases in character:
   • "Hello, my name is {char_info['name']}"
   • "Welcome to my underwater world!"
   • "Today is going to be an amazing adventure!"

═══════════════════════════════════════════════════════════════════════════

📋 RECORDING SECTIONS:

"""

        # Add different sections
        sections = [
            ("GREETINGS & INTRODUCTIONS", "greeting", 5),
            ("TEACHING & EXPLAINING", "teaching", 10),
            ("ENCOURAGEMENT & PRAISE", "encouraging", 8),
            ("STORYTELLING & NARRATION", "storytelling", 10),
            ("QUESTIONS & CURIOSITY", "questioning", 8),
            ("HAPPY EMOTIONS", "emotional_happy", 7),
            ("SAD EMOTIONS", "emotional_sad", 5),
            ("EXCITED EMOTIONS", "emotional_excited", 7),
            ("COMFORTING & CARING", "comforting", 8),
            ("MUSICAL & RHYTHMIC", "musical", 6),
        ]

        phrase_count = 1

        for section_name, template_key, num_phrases in sections:
            script += f"""
SECTION {len([s for s in sections if sections.index(s) <= sections.index((section_name, template_key, num_phrases))])}:  {section_name}
{'─' * 75}

"""
            templates = self.script_templates.get(template_key, [])

            for i in range(min(num_phrases, len(templates))):
                phrase = templates[i % len(templates)]
                script += f"   [{phrase_count:03d}] {phrase}\n"
                phrase_count += 1

            script += "\n"

        # Add custom character-specific lines
        script += f"""
═══════════════════════════════════════════════════════════════════════════

🌟 CHARACTER-SPECIFIC LINES:

"""

        # These would be loaded from character definitions
        # For now, add generic ones
        if character_id == "captain_finn":
            custom_lines = [
                "Ahoy there, young sailors! Welcome aboard!",
                "In all my years at sea, I've learned that courage comes from the heart.",
                "The ocean teaches us patience, my friends.",
                "Let me tell you a tale from the deep blue...",
                "Steady as she goes! We'll navigate these waters together.",
            ]
        elif character_id == "bubbles":
            custom_lines = [
                "Ooh ooh! This is SO exciting!",
                "Did you know that fish can see colors humans can't?!",
                "Wheee! I love swimming through the coral!",
                "Can we be best friends? Please please please!",
                "This is the best day EVER!",
            ]
        else:
            custom_lines = [
                f"As {char_info['name']}, I welcome you to this adventure!",
                "Learning together makes everything more fun!",
                "Remember, every question is a good question!",
                "You're doing wonderfully! Keep up the great work!",
                "Let's explore the wonders of this underwater world!",
            ]

        for i, line in enumerate(custom_lines, phrase_count):
            script += f"   [{i:03d}] {line}\n"

        script += f"""

═══════════════════════════════════════════════════════════════════════════

📝 RECORDING TIPS:

1. Stay in character throughout the entire session
2. Take breaks every 15-20 minutes to rest your voice
3. Drink water regularly (room temperature is best)
4. If you make a mistake, just pause and restart the phrase
5. Maintain consistent distance from microphone (6-8 inches)
6. Record in a quiet environment
7. Have fun! Your enjoyment will show in the voice!

═══════════════════════════════════════════════════════════════════════════

✅ POST-RECORDING CHECKLIST:

□ Review all recordings for quality
□ Note any phrases that need retakes
□ Save all files with proper naming convention
□ Update session progress in system
□ Rest your voice for at least 30 minutes

═══════════════════════════════════════════════════════════════════════════

🎙️ Happy Recording! 🎙️

"""

        return script

    def complete_session(
        self,
        session_id: str,
        actual_words: int,
        duration_minutes: int,
        emotions_covered: List[str],
        behaviors_covered: List[str],
        audio_files: List[str],
        notes: str = ""
    ):
        """Mark a session as complete and update profile."""

        session = self.load_recording_session(session_id)
        if not session:
            return

        # Update session
        session.actual_words = actual_words
        session.duration_minutes = duration_minutes
        session.emotions_covered = emotions_covered
        session.behaviors_covered = behaviors_covered
        session.audio_files = audio_files
        session.notes = notes

        self.save_recording_session(session)

        # Update character profile
        profile = self.load_character_profile(session.character_id)
        if profile:
            profile.total_words_recorded += actual_words
            profile.total_sessions_completed += 1
            profile.total_recording_time += duration_minutes
            profile.session_ids.append(session_id)

            # Update emotions and behaviors
            for emotion in emotions_covered:
                if emotion not in profile.emotions_covered:
                    profile.emotions_covered.append(emotion)

            for behavior in behaviors_covered:
                if behavior not in profile.behaviors_covered:
                    profile.behaviors_covered.append(behavior)

            # Calculate completion
            profile.completion_percentage = (
                profile.total_words_recorded / profile.target_words * 100
            )
            profile.is_complete = profile.completion_percentage >= 95

            # Estimate phoneme coverage based on words
            # Rough estimate: 95% coverage at target words
            profile.phoneme_coverage_estimate = min(
                0.95 * (profile.total_words_recorded / profile.target_words),
                0.95
            )

            self.save_character_profile(profile)

    def generate_progress_report(self, character_id: str) -> str:
        """Generate a progress report for a character."""

        profile = self.load_character_profile(character_id)
        if not profile:
            return f"No profile found for {character_id}"

        report = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        📊 VOICE RECORDING PROGRESS REPORT 📊                             ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

CHARACTER: {profile.character_name}
TARGET QUALITY: {profile.target_quality.upper()}

═══════════════════════════════════════════════════════════════════════════

📈 OVERALL PROGRESS:

   Completion: {profile.completion_percentage:.1f}%
   Status: {"✅ COMPLETE!" if profile.is_complete else "🚧 IN PROGRESS"}

═══════════════════════════════════════════════════════════════════════════

📊 RECORDING STATS:

   Words Recorded: {profile.total_words_recorded:,} / {profile.target_words:,}
   Sessions Completed: {profile.total_sessions_completed} / {profile.target_sessions}
   Total Recording Time: {profile.total_recording_time} minutes ({profile.total_recording_time / 60:.1f} hours)

═══════════════════════════════════════════════════════════════════════════

🎭 COVERAGE:

   Emotions Covered: {len(profile.emotions_covered)}/8
   {', '.join(profile.emotions_covered) if profile.emotions_covered else 'None yet'}

   Behaviors Covered: {len(profile.behaviors_covered)}/8
   {', '.join(profile.behaviors_covered) if profile.behaviors_covered else 'None yet'}

   Estimated Phoneme Coverage: {profile.phoneme_coverage_estimate * 100:.1f}%

═══════════════════════════════════════════════════════════════════════════

📁 SESSIONS:

"""

        for session_id in profile.session_ids:
            session = self.load_recording_session(session_id)
            if session:
                report += f"""   Session {session.session_number}:
      Date: {session.date[:10]}
      Words: {session.actual_words}
      Duration: {session.duration_minutes} min
      Files: {len(session.audio_files)}
"""

        if not profile.is_complete:
            remaining_words = profile.target_words - profile.total_words_recorded
            remaining_sessions = profile.target_sessions - profile.total_sessions_completed

            report += f"""
═══════════════════════════════════════════════════════════════════════════

🎯 REMAINING:

   Words Needed: {remaining_words:,}
   Sessions Recommended: {remaining_sessions}
   Estimated Time: {remaining_words // 125} - {remaining_words // 100} minutes

═══════════════════════════════════════════════════════════════════════════
"""
        else:
            report += f"""
═══════════════════════════════════════════════════════════════════════════

✅ CHARACTER VOICE COMPLETE!

   Ready for voice model training!
   Voice Model Path: {profile.voice_model_path or 'Not yet trained'}

═══════════════════════════════════════════════════════════════════════════
"""

        return report


def main():
    """Demo the voice recording session manager."""
    manager = VoiceRecordingSessionManager()

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎙️ VOICE RECORDING SESSION MANAGER 🎙️                           ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)

    print("\n📋 AVAILABLE CHARACTERS:\n")
    for char_id, char_info in manager.characters.items():
        print(f"   {char_id}: {char_info['name']}")
        print(f"      {char_info['description']}")
        print()

    # Create example profile for Captain Finn
    print("=" * 75)
    print("🎯 CREATING PROFILE FOR CAPTAIN FINN")
    print("=" * 75 + "\n")

    profile = manager.create_character_profile("captain_finn", "professional")
    print(f"✅ Profile created!")
    print(f"   Target: {profile.target_words:,} words in {profile.target_sessions} sessions")

    # Generate recording script
    print("\n" + "=" * 75)
    print("📝 GENERATING RECORDING SCRIPT FOR SESSION 1")
    print("=" * 75)

    script = manager.generate_recording_script("captain_finn", 1, 1875)

    # Save script to file
    script_path = manager.scripts_dir / "captain_finn_session_1_script.txt"
    with open(script_path, 'w') as f:
        f.write(script)

    print(f"\n✅ Script generated and saved to:")
    print(f"   {script_path}")

    # Show preview
    print("\n" + "=" * 75)
    print("SCRIPT PREVIEW (first 50 lines):")
    print("=" * 75)
    print('\n'.join(script.split('\n')[:50]))
    print("\n... (script continues) ...")

    # Show progress report
    print("\n" + "=" * 75)
    print("📊 PROGRESS REPORT")
    print("=" * 75)

    report = manager.generate_progress_report("captain_finn")
    print(report)

    print("\n✅ Voice Recording Session Manager Ready!")
    print(f"\n📁 Directories:")
    print(f"   Sessions: {manager.sessions_dir}")
    print(f"   Profiles: {manager.profiles_dir}")
    print(f"   Scripts: {manager.scripts_dir}")
    print(f"   Audio: {manager.audio_dir}")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
