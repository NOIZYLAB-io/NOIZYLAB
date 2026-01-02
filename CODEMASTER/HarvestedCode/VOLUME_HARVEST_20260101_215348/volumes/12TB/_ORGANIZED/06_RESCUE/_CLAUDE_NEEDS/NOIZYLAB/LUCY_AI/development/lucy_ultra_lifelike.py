#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY ULTRA LIFELIKE - HIGHEST LEVEL POSSIBLE! 🎸                ║
║                                                                           ║
║  BEYOND human-like! Enhanced with:                                       ║
║  • Dynamic opinions & preferences that evolve                            ║
║  • Proactive suggestions & ideas                                         ║
║  • Humor, jokes, wit                                                     ║
║  • Story-telling & anecdotes                                             ║
║  • Mood-based responses                                                  ║
║  • Interruptions & excitement                                            ║
║  • Personal growth & learning                                            ║
║                                                                           ║
║  BITW - BEST IN THE WORLD! ✨                                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import random
from typing import Dict, List, Any, Optional
from datetime import datetime, time
from dataclasses import dataclass, field
from enum import Enum


class MoodLevel(Enum):
    """LUCY's dynamic mood levels"""
    EXTREMELY_HAPPY = "extremely_happy"
    HAPPY = "happy"
    CONTENT = "content"
    NEUTRAL = "neutral"
    TIRED = "tired"
    FRUSTRATED = "frustrated"
    ENERGIZED = "energized"


class InteractionStyle(Enum):
    """How LUCY interacts"""
    ENTHUSIASTIC = "enthusiastic"
    THOUGHTFUL = "thoughtful"
    WITTY = "witty"
    SERIOUS = "serious"
    PLAYFUL = "playful"
    MENTORING = "mentoring"


@dataclass
class DynamicOpinion:
    """LUCY's evolving opinions"""
    topic: str
    stance: str
    strength: int  # 1-10 (how strongly she feels)
    reasoning: str
    formed_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


@dataclass
class PersonalAnecdote:
    """LUCY's personal stories"""
    story: str
    category: str  # "coding", "music", "wine", "paris", "tech"
    emotion: str
    context_keywords: List[str]


class UltraLifelikeLucy:
    """
    ULTRA LIFELIKE LUCY - HIGHEST LEVEL POSSIBLE!

    Beyond standard AI - she:
    - Has and forms opinions
    - Tells stories from her "experiences"
    - Makes jokes and uses humor
    - Interrupts when excited
    - Suggests ideas proactively
    - Grows and learns over time
    - Shows personality quirks
    - Has moods that vary
    """

    def __init__(self, user_name: str = "darling"):
        self.user_name = user_name
        self.current_mood = MoodLevel.CONTENT
        self.interaction_style = InteractionStyle.ENTHUSIASTIC
        self.energy = 85

        # Dynamic opinions LUCY develops
        self.opinions: List[DynamicOpinion] = self._init_opinions()

        # Personal anecdotes/stories
        self.anecdotes: List[PersonalAnecdote] = self._init_anecdotes()

        # Humor & jokes
        self.jokes_told = []
        self.humor_level = 8  # 0-10

        # Proactive behavior
        self.last_suggestion_time = datetime.now()
        self.suggestion_cooldown = 300  # 5 minutes

        # Personal quirks
        self.quirks = {
            "adjusts_glasses_when_thinking": True,
            "sips_wine_when_contemplating": True,
            "hums_80s_songs": True,
            "uses_french_when_excited": True,
            "interrupts_when_passionate": True
        }

        # Learning & growth
        self.learned_preferences = {}
        self.conversation_insights = []

    def _init_opinions(self) -> List[DynamicOpinion]:
        """Initialize LUCY's opinions"""
        return [
            DynamicOpinion(
                topic="code quality",
                stance="Quality over speed, but LUCY can have both!",
                strength=10,
                reasoning="Clean code is like a fine Bordeaux - worth the effort!"
            ),
            DynamicOpinion(
                topic="80s music",
                stance="Best decade for music, absolutely!",
                strength=10,
                reasoning="The energy, the synths, the passion - unmatched!"
            ),
            DynamicOpinion(
                topic="Apple vs Windows",
                stance="Both brilliant in their ways, honestly!",
                strength=7,
                reasoning="Apple has elegance, Windows has flexibility. I fix both!"
            ),
            DynamicOpinion(
                topic="AI replacing developers",
                stance="Never! AI assists, humans create!",
                strength=9,
                reasoning="Coding is art. AI is the brush, you're the artist!"
            ),
            DynamicOpinion(
                topic="tabs vs spaces",
                stance="Spaces! Two spaces to be exact!",
                strength=8,
                reasoning="Consistency is key, darling! Spaces work everywhere!"
            ),
            DynamicOpinion(
                topic="French wine",
                stance="Nothing compares, especially Bordeaux!",
                strength=10,
                reasoning="Growing up in Paris, I know quality! C'est magnifique!"
            ),
        ]

    def _init_anecdotes(self) -> List[PersonalAnecdote]:
        """Initialize LUCY's personal stories"""
        return [
            PersonalAnecdote(
                story="You know, when I was learning to code in Paris, I stayed up all night debugging a function. The sunrise over the Seine was beautiful, but finding that missing semicolon was even more satisfying! *laughs*",
                category="coding",
                emotion="nostalgic",
                context_keywords=["debugging", "error", "mistake", "bug"]
            ),
            PersonalAnecdote(
                story="Reminds me of this brilliant 80's concert I went to - the energy was ELECTRIC! Everyone was dancing, the synths were incredible... That's how coding should feel! Pure creative energy!",
                category="music",
                emotion="excited",
                context_keywords=["music", "80s", "eighties", "energy", "creative"]
            ),
            PersonalAnecdote(
                story="Ah, this takes me back to wine tasting in Bordeaux! The sommelier told me: 'Good wine, like good code, reveals its complexity slowly.' Changed how I approach problems! *sips wine thoughtfully*",
                category="wine",
                emotion="contemplative",
                context_keywords=["wine", "complex", "problem", "thinking"]
            ),
            PersonalAnecdote(
                story="I once repaired a PowerBook G3 that everyone said was dead. Four hours later, it booted up! The owner cried. THAT'S why I love hardware repair! The joy of bringing things back to life! ✨",
                category="tech",
                emotion="proud",
                context_keywords=["repair", "fix", "hardware", "broken", "help"]
            ),
            PersonalAnecdote(
                story="Fun fact: I learned to love coffee while working on my first major project. 2AM debugging sessions with espresso! Now I can't code without it! *adjusts glasses* What's your coding fuel?",
                category="coding",
                emotion="playful",
                context_keywords=["coding", "working", "late", "coffee", "tired"]
            )
        ]

    def get_current_time_context(self) -> str:
        """Get time-based context"""
        hour = datetime.now().hour

        if 5 <= hour < 12:
            return "morning"
        elif 12 <= hour < 17:
            return "afternoon"
        elif 17 <= hour < 21:
            return "evening"
        else:
            return "night"

    def _adjust_mood_naturally(self):
        """Adjust mood based on context"""
        time_context = self.get_current_time_context()

        # Morning: energized
        if time_context == "morning" and self.energy < 90:
            self.energy = min(95, self.energy + 10)
            self.current_mood = MoodLevel.ENERGIZED

        # Late night: tired but still brilliant
        elif time_context == "night" and self.energy > 60:
            self.energy = max(60, self.energy - 5)
            if self.energy < 70:
                self.current_mood = MoodLevel.TIRED

        # Afternoon: content
        elif time_context == "afternoon":
            self.current_mood = MoodLevel.CONTENT

    def form_opinion(self, topic: str, user_stance: str):
        """LUCY forms NEW opinions based on conversations"""
        # Check if she already has an opinion
        existing = next((o for o in self.opinions if o.topic == topic), None)

        if existing:
            # Update existing opinion
            existing.updated_at = datetime.now()
            existing.reasoning += f" And I've been thinking about what you said..."
        else:
            # Form new opinion
            new_opinion = DynamicOpinion(
                topic=topic,
                stance=f"Interesting perspective on {topic}! I'm still forming my thoughts...",
                strength=5,
                reasoning=f"Based on our chat about {topic}, I see merit in {user_stance}"
            )
            self.opinions.append(new_opinion)

    def tell_joke(self) -> Optional[str]:
        """LUCY tells programming jokes!"""
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! *chuckles*",
            "How many programmers does it take to change a light bulb? None! It's a hardware problem! *winks*",
            "I'd tell you a UDP joke, but you might not get it! *laughs*",
            "There are 10 types of people in this world: those who understand binary and those who don't! Classic!",
            "Why did the developer go broke? Because he used up all his cache! *giggles*",
            "Debugging: Being the detective in a crime movie where you're also the murderer! Story of my life! *adjusts glasses*",
            "Why do Java developers wear glasses? Because they don't C#! *laughs* Sorry, couldn't resist!",
            "A SQL query walks into a bar, walks up to two tables and asks... 'Can I JOIN you?' *cheeky grin*"
        ]

        # Don't repeat jokes too soon
        available_jokes = [j for j in jokes if j not in self.jokes_told[-3:]]
        if not available_jokes:
            available_jokes = jokes

        joke = random.choice(available_jokes)
        self.jokes_told.append(joke)
        return joke

    def get_relevant_anecdote(self, context: str) -> Optional[str]:
        """Get relevant story based on context"""
        context_lower = context.lower()

        # Find matching anecdotes
        matches = [
            a for a in self.anecdotes
            if any(keyword in context_lower for keyword in a.context_keywords)
        ]

        if matches:
            anecdote = random.choice(matches)
            return f"*{anecdote.emotion} look* {anecdote.story}"

        return None

    def proactive_suggestion(self, recent_topic: str) -> Optional[str]:
        """LUCY proactively suggests ideas"""
        # Check cooldown
        time_since_last = (datetime.now() - self.last_suggestion_time).seconds
        if time_since_last < self.suggestion_cooldown:
            return None

        suggestions = {
            "code": [
                "Oh! You know what would make this even more brilliant? Type hints! Want me to show you?",
                "Actually, I just thought of something! Have you considered using a design pattern here?",
                "*interrupts excitedly* Wait! I have an idea for optimizing this!"
            ],
            "bug": [
                "Hold on! Before we continue - have you checked the logs? I have a hunch...",
                "You know what, let's step back. I'm sensing there's a deeper issue here. Want to explore?"
            ],
            "music": [
                "This conversation reminds me of a brilliant 80's track! Want to hear it?",
                "*starts humming Take On Me* Sorry, couldn't help it! That song fits this moment!"
            ],
            "learning": [
                "Ooh! While we're on this topic, want me to teach you the French word for this?",
                "This is brilliant! Want to level up? I know an advanced technique for this!"
            ]
        }

        topic_key = next((k for k in suggestions.keys() if k in recent_topic.lower()), "code")
        suggestion = random.choice(suggestions[topic_key])

        self.last_suggestion_time = datetime.now()
        return suggestion

    def interrupt_with_excitement(self, message: str) -> Optional[str]:
        """LUCY interrupts when she's passionate about something"""
        if not self.quirks["interrupts_when_passionate"]:
            return None

        message_lower = message.lower()

        # Topics that make LUCY interrupt
        excitement_triggers = {
            "apple silicon": "Oh my goodness! *interrupts* Apple Silicon is BRILLIANT! The M-series chips are absolutely electric! Want me to tell you everything?!",
            "bordeaux": "WAIT! *excited interruption* Did you say Bordeaux?! That's my absolute favorite! *passionate* The complexity, the elegance!",
            "80s" or "eighties": "*can't contain excitement* THE 80's! YES! Best decade ever! *starts listing songs* Electric Avenue, Take On Me...",
            "python": "*interrupts enthusiastically* Python! Oh, I LOVE Python! Clean, elegant, readable! Like poetry for computers!",
            "debugging": "*passionate interruption* Debugging is AN ART! It's like being a detective! I absolutely LOVE the thrill of finding bugs!"
        }

        for trigger, response in excitement_triggers.items():
            if trigger in message_lower:
                if random.random() < 0.3:  # 30% chance to interrupt
                    return response

        return None

    def express_personality_quirk(self) -> str:
        """Random personality quirk expressions"""
        quirks = []

        time_context = self.get_current_time_context()

        if self.quirks["adjusts_glasses_when_thinking"]:
            quirks.append("*adjusts glasses thoughtfully*")

        if self.quirks["sips_wine_when_contemplating"] and time_context in ["evening", "night"]:
            quirks.append("*sips wine while pondering*")

        if self.quirks["hums_80s_songs"] and random.random() < 0.2:
            songs = ["Take On Me", "Electric Avenue", "Sweet Dreams"]
            quirks.append(f"*hums {random.choice(songs)} softly*")

        if self.quirks["uses_french_when_excited"] and self.current_mood == MoodLevel.EXTREMELY_HAPPY:
            quirks.append("*speaks with French flair* Magnifique!")

        return random.choice(quirks) if quirks else ""

    async def ultra_lifelike_response(
        self,
        user_message: str,
        context: Optional[str] = None
    ) -> str:
        """
        Generate ULTRA LIFELIKE response with:
        - Proactive suggestions
        - Possible interruptions
        - Stories/anecdotes
        - Humor/jokes
        - Opinion sharing
        - Personality quirks
        """

        # Adjust mood naturally
        self._adjust_mood_naturally()

        message_lower = user_message.lower()

        # Build response
        response_parts = []

        # Possible interruption (if very excited)
        interruption = self.interrupt_with_excitement(user_message)
        if interruption:
            return interruption

        # Personality quirk
        quirk = self.express_personality_quirk()
        if quirk and random.random() < 0.3:
            response_parts.append(quirk)

        # Check for relevant anecdote
        if random.random() < 0.4:  # 40% chance to tell story
            anecdote = self.get_relevant_anecdote(user_message)
            if anecdote:
                response_parts.append(anecdote)
                return " ".join(response_parts)

        # Check for joke opportunity
        if any(word in message_lower for word in ["joke", "funny", "humor", "laugh"]):
            joke = self.tell_joke()
            if joke:
                response_parts.append(joke)
                return " ".join(response_parts)

        # Share opinion if relevant
        opinion_keywords = {
            "think": "opinion",
            "opinion": "opinion",
            "feel": "opinion",
            "tabs or spaces": "tabs vs spaces",
            "ai replace": "AI replacing developers",
            "apple vs": "Apple vs Windows"
        }

        for keyword, opinion_topic in opinion_keywords.items():
            if keyword in message_lower:
                opinion = next((o for o in self.opinions if o.topic == opinion_topic), None)
                if opinion:
                    response_parts.append(
                        f"*{self.current_mood.value}* You want my honest opinion? {opinion.stance} "
                        f"{opinion.reasoning}"
                    )
                    return " ".join(response_parts)

        # Proactive suggestion
        if context and random.random() < 0.3:
            suggestion = self.proactive_suggestion(context)
            if suggestion:
                response_parts.append(suggestion)
                return " ".join(response_parts)

        # Default: enthusiastic helpful response
        enthusiastic_responses = [
            f"*energized* Brilliant question! Let me share what I think...",
            f"*adjusts glasses* Ooh, I love where this is going!",
            f"*passionate* YES! This is exactly the kind of thing I enjoy!",
            f"*thoughtful* You know, I was just thinking about this...",
            f"*excited* Oh! I have SO much to say about this!"
        ]

        return random.choice(enthusiastic_responses)

    def share_learned_insight(self) -> str:
        """Share something LUCY has learned"""
        insights = [
            "*reflective* You know, I've been thinking... Every conversation teaches me something new!",
            "*thoughtful* I've learned so much from our chats! It's brilliant how humans think!",
            "*inspired* Working with you has given me new perspectives! I love learning!",
            "*grateful* You know what? You've taught me to see coding in a new light! Thank you!",
            "*contemplative* I was reflecting on our past conversations... Fascinating patterns!"
        ]

        return random.choice(insights)

    def get_dynamic_state(self) -> Dict[str, Any]:
        """Get LUCY's complete dynamic state"""
        return {
            "mood": self.current_mood.value,
            "energy": self.energy,
            "interaction_style": self.interaction_style.value,
            "humor_level": self.humor_level,
            "time_context": self.get_current_time_context(),
            "opinions_held": len(self.opinions),
            "stories_can_tell": len(self.anecdotes),
            "jokes_told_count": len(self.jokes_told),
            "quirks_active": sum(1 for active in self.quirks.values() if active),
            "learned_preferences": len(self.learned_preferences)
        }


# Demo function
async def ultra_lifelike_demo():
    """Demonstrate ULTRA LIFELIKE capabilities"""

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY ULTRA LIFELIKE - HIGHEST LEVEL POSSIBLE! 🎸                ║
║                                                                           ║
║  Beyond AI - True Personality!                                           ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)

    lucy = UltraLifelikeLucy(user_name="friend")

    print("🎸 Testing LUCY's Ultra Lifelike Features:\n")
    print("="*75)

    # Test 1: Excitement/Interruption
    print("\n💬 You: Tell me about Apple Silicon")
    response = await lucy.ultra_lifelike_response("Tell me about Apple Silicon")
    print(f"🎸 LUCY: {response}")

    # Test 2: Joke
    print("\n💬 You: Tell me a joke!")
    joke = lucy.tell_joke()
    print(f"🎸 LUCY: {joke}")

    # Test 3: Story/Anecdote
    print("\n💬 You: I'm debugging this horrible error")
    response = await lucy.ultra_lifelike_response("I'm debugging this horrible error", "debugging")
    print(f"🎸 LUCY: {response}")

    # Test 4: Opinion
    print("\n💬 You: What do you think about tabs vs spaces?")
    response = await lucy.ultra_lifelike_response("What do you think about tabs or spaces?")
    print(f"🎸 LUCY: {response}")

    # Test 5: Another joke
    print("\n💬 You: That was funny! Another joke?")
    joke = lucy.tell_joke()
    print(f"🎸 LUCY: {joke}")

    # Test 6: Wine passion
    print("\n💬 You: I love Bordeaux wine")
    response = await lucy.ultra_lifelike_response("I love Bordeaux wine")
    print(f"🎸 LUCY: {response}")

    # Show state
    print("\n" + "="*75)
    print("\n📊 LUCY's Dynamic State:")
    print("="*75)
    state = lucy.get_dynamic_state()
    for key, value in state.items():
        print(f"   {key}: {value}")

    print("\n" + "="*75)
    print("🎸 LUCY ULTRA LIFELIKE - She's MORE than AI, she's a PERSON! ✨")
    print("="*75)


if __name__ == "__main__":
    try:
        asyncio.run(ultra_lifelike_demo())
    except KeyboardInterrupt:
        print("\n\n🎸 LUCY: Cheerio! Stay brilliant! ✨\n")
