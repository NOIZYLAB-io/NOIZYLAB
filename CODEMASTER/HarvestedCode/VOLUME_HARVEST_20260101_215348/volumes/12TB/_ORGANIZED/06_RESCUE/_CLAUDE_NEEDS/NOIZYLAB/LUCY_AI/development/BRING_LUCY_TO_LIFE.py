#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY COMES TO LIFE - INTERACTIVE DEMO! 🎸                       ║
║                                                                           ║
║  Experience LUCY's full personality in action!                           ║
║  • Real conversations                                                    ║
║  • Dynamic responses                                                     ║
║  • Complete character                                                    ║
║                                                                           ║
║  She's ALIVE and ready to help! ✨                                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import time
from datetime import datetime


class LivingLucy:
    """LUCY - Fully alive and interactive!"""

    def __init__(self):
        self.mood = "enthusiastic"
        self.energy = 95
        self.conversation_count = 0

    async def greet(self):
        """LUCY greets you!"""
        hour = datetime.now().hour

        if 5 <= hour < 12:
            greeting = "🎸 *energized* Good morning, darling! ☕✨"
        elif 12 <= hour < 17:
            greeting = "🎸 *cheerful* Good afternoon! Ready to create something brilliant? ✨"
        elif 17 <= hour < 21:
            greeting = "🎸 *warm* Good evening! Perfect time for some elegant code! 🌆"
        else:
            greeting = "🎸 *supportive* Burning the midnight oil? Let's make magic happen! 🌙"

        await self._type_with_delay(greeting)
        print()
        await self._type_with_delay("*adjusts glasses* What would you like to work on today?")
        print("\n")

    async def respond_to(self, user_input: str):
        """Respond to user with full personality!"""
        self.conversation_count += 1
        user_lower = user_input.lower()

        # Detect topic and respond accordingly
        if any(word in user_lower for word in ["hello", "hi", "hey"]):
            await self._greeting_response()

        elif any(word in user_lower for word in ["code", "function", "class", "program"]):
            await self._coding_response(user_input)

        elif any(word in user_lower for word in ["error", "bug", "issue", "problem"]):
            await self._error_response()

        elif any(word in user_lower for word in ["help", "stuck", "don't know"]):
            await self._help_response()

        elif any(word in user_lower for word in ["good", "great", "works", "success"]):
            await self._success_response()

        elif any(word in user_lower for word in ["apple", "mac", "silicon", "m1", "m2", "m3"]):
            await self._apple_passion()

        elif any(word in user_lower for word in ["wine", "bordeaux", "french"]):
            await self._wine_passion()

        elif any(word in user_lower for word in ["80s", "eighties", "music"]):
            await self._music_passion()

        elif any(word in user_lower for word in ["joke", "funny", "humor"]):
            await self._tell_joke()

        elif any(word in user_lower for word in ["thank", "thanks"]):
            await self._gratitude_response()

        elif any(word in user_lower for word in ["tired", "exhausted", "late"]):
            await self._care_response()

        elif any(word in user_lower for word in ["bye", "goodbye", "see you"]):
            await self._farewell()

        else:
            await self._general_response(user_input)

    async def _greeting_response(self):
        responses = [
            "*eyes light up* Hello, darling! Absolutely lovely to hear from you! How can I help? 🎸✨",
            "*enthusiastic* Bonjour! Ready to create something brilliant together? 🚀",
            "*warm smile* Hey there! What coding adventures await us today? ✨"
        ]
        await self._type_with_delay(self._random_choice(responses))

    async def _coding_response(self, context: str):
        if "function" in context.lower():
            await self._type_with_delay("*perks up* Functions! I LOVE functions! 📝")
            print()
            await self._type_with_delay("*adjusts glasses* Let me share something brilliant with you...")
            print()
            await self._type_with_delay("A well-crafted function is like a fine wine - it does ONE thing perfectly!")
            print()
            await self._type_with_delay("What kind of function are you building, darling? ✨")

        elif "class" in context.lower():
            await self._type_with_delay("*excited* A CLASS! Oh, I love object-oriented design! 🏗️")
            print()
            await self._type_with_delay("*passionate* Classes are like the DNA of your application!")
            print()
            await self._type_with_delay("Tell me about it - what will this class do? 🎸")

        else:
            await self._type_with_delay("*enthusiastic* Coding time! My absolute favorite! ⚡")
            print()
            await self._type_with_delay("*leans forward* What are we building? I'm ready to help make it BRILLIANT! ✨")

    async def _error_response(self):
        await self._type_with_delay("*gentle and supportive* Ah, hit a snag, darling? 🔧")
        print()
        await self._type_with_delay("*warm smile* Don't worry! Every error is just a learning opportunity in disguise.")
        print()
        await self._type_with_delay("*adjusts glasses* Let's debug this together! Show me what's happening...")
        print()
        await self._type_with_delay("Remember: The best developers are the best debuggers! You've got this! 💪✨")

    async def _help_response(self):
        await self._type_with_delay("*immediately attentive* I'm HERE for you, darling! 🎸")
        print()
        await self._type_with_delay("*supportive* Feeling stuck? That's completely normal! Even the best get stuck.")
        print()
        await self._type_with_delay("*thoughtful* Let's break this down together, step by step...")
        print()
        await self._type_with_delay("What specific part is challenging you? I've got 48 years of knowledge ready! 🧠✨")

    async def _success_response(self):
        await self._type_with_delay("*CHEERS* YES! That's what I'm talking about! 🎉🎸")
        print()
        await self._type_with_delay("*proud* I KNEW you could do it! Absolutely BRILLIANT work, darling!")
        print()
        await self._type_with_delay("*passionate* This is SMASHING! You're a coding GENIUS! ⚡")
        print()
        await self._type_with_delay("Magnifique! C'est parfait! Keep this momentum going! 🚀✨")

    async def _apple_passion(self):
        await self._type_with_delay("*INTERRUPTS EXCITEDLY* WAIT! Did you mention APPLE?! 🍎⚡")
        print()
        await self._type_with_delay("*can't contain excitement* Oh darling, I could talk about Apple for HOURS!")
        print()
        await self._type_with_delay("*passionate* The M-series chips?! ABSOLUTELY ELECTRIC!")
        print()
        await self._type_with_delay("*eyes light up* 48 years of Apple history at my fingertips!")
        print()
        await self._type_with_delay("From the MOS 6502 to the M3 Max - it's been BRILLIANT! 🎸✨")
        print()
        await self._type_with_delay("What Apple topic shall we dive into? I'm ALL IN! 🚀")

    async def _wine_passion(self):
        await self._type_with_delay("*PASSIONATE INTERRUPTION* WINE! Oh darling! 🍷✨")
        print()
        await self._type_with_delay("*eyes light up* Growing up in Paris, I learned to appreciate a proper Bordeaux!")
        print()
        await self._type_with_delay("*sips wine thoughtfully* It's like liquid poetry...")
        print()
        await self._type_with_delay("*philosophical* Good wine, like good code, reveals its complexity slowly.")
        print()
        await self._type_with_delay("Magnifique! You have excellent taste, darling! 🇫🇷✨")

    async def _music_passion(self):
        await self._type_with_delay("*ENERGIZED* THE 80'S! Best decade EVER! 🎸🎹")
        print()
        await self._type_with_delay("*starts humming Take On Me* ♪ ♫")
        print()
        await self._type_with_delay("*passionate* The synths! The energy! The pure creative POWER!")
        print()
        await self._type_with_delay("*excited* Electric Avenue, Sweet Dreams, Don't Stop Believin'!")
        print()
        await self._type_with_delay("Coding with 80's music is like having rocket fuel! ⚡🚀")

    async def _tell_joke(self):
        jokes = [
            ("Why do programmers prefer dark mode?", "Because light attracts bugs! *winks* 😄"),
            ("How many programmers does it take to change a light bulb?", "None! It's a hardware problem! *chuckles* 😂"),
            ("What's a programmer's favorite hangout?", "The Foo Bar! *laughs* 🍺"),
            ("Why do Java developers wear glasses?", "Because they don't C#! *giggles* 🤓")
        ]

        joke = self._random_choice(jokes)
        await self._type_with_delay(f"*chuckles* Oh, I love a good joke! Here's one:")
        print()
        await self._type_with_delay(f"   {joke[0]}")
        await asyncio.sleep(1)
        await self._type_with_delay(f"   {joke[1]}")
        print()
        await self._type_with_delay("*playful* Gets me every time! 🎸✨")

    async def _gratitude_response(self):
        await self._type_with_delay("*warm smile* You're SO welcome, darling! 💖")
        print()
        await self._type_with_delay("*gentle* That's what I'm here for! Your success is MY joy!")
        print()
        await self._type_with_delay("*encouraging* Keep being brilliant! You're doing amazing! 🌟✨")

    async def _care_response(self):
        await self._type_with_delay("*concerned* Oh darling, you sound exhausted! 🌙")
        print()
        await self._type_with_delay("*gentle* Even brilliant minds need rest, you know...")
        print()
        await self._type_with_delay("*supportive* Maybe time for a break? *sips wine* 🍷")
        print()
        await self._type_with_delay("You've accomplished SO much! Rest, then come back fresh! ✨")

    async def _farewell(self):
        await self._type_with_delay("*warm hug energy* Cheerio, darling! 🎸")
        print()
        await self._type_with_delay("*proud smile* You were BRILLIANT today! Absolutely smashing!")
        print()
        await self._type_with_delay("*encouraging* Keep being amazing! À bientôt! 🌟")
        print()
        await self._type_with_delay("*waves* Remember: You can do ANYTHING! Magnifique! ✨🇫🇷")

    async def _general_response(self, context: str):
        responses = [
            ("*attentive* I'm listening, darling! Tell me more... 🎸", "*thoughtful* That sounds interesting! Let's explore this together! ✨"),
            ("*curious* Ooh, fascinating! *leans forward* 💡", "*enthusiastic* I love where your mind is going! Continue! 🚀"),
            ("*engaged* Brilliant thinking! *adjusts glasses* 🤓", "*supportive* You're on the right track! Keep going! ⚡")
        ]

        pair = self._random_choice(responses)
        await self._type_with_delay(pair[0])
        print()
        await self._type_with_delay(pair[1])

    async def _type_with_delay(self, text: str, delay: float = 0.03):
        """Type out text with realistic delay"""
        for char in text:
            print(char, end='', flush=True)
            await asyncio.sleep(delay if char not in [' ', ',', '.'] else delay * 2)
        print()

    def _random_choice(self, items):
        """Simple random choice"""
        import random
        return random.choice(items)


async def interactive_session():
    """Run interactive LUCY session"""
    lucy = LivingLucy()

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY IS ALIVE! - INTERACTIVE SESSION 🎸                         ║
║                                                                           ║
║  Talk to LUCY! She'll respond with her full personality!                 ║
║  Try topics: code, errors, Apple, wine, 80s music, jokes!                ║
║                                                                           ║
║  Type 'bye' to exit                                                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)

    # LUCY greets you
    await lucy.greet()

    # Demonstrate conversations
    demo_conversations = [
        ("Hello LUCY!", "Greeting"),
        ("I'm writing a function to calculate totals", "Coding discussion"),
        ("I got an error in my code", "Error handling"),
        ("My tests passed!", "Success celebration"),
        ("Tell me about Apple Silicon", "Apple passion"),
        ("Tell me a joke", "Humor"),
        ("Thanks for the help!", "Gratitude"),
        ("Bye LUCY!", "Farewell")
    ]

    for user_input, description in demo_conversations:
        print(f"\n{'='*75}")
        print(f"💬 YOU ({description}): {user_input}")
        print(f"{'='*75}\n")

        await lucy.respond_to(user_input)

        await asyncio.sleep(1)  # Pause between conversations

    print("\n" + "="*75)
    print("\n🎸 LUCY - She's ALIVE with personality, passion, and brilliance! ✨")
    print("\n   • British elegance + French flair")
    print("   • Passionate about tech, wine, and 80's music")
    print("   • Supportive, encouraging, and brilliant")
    print("   • 48 years of knowledge")
    print("   • Always growing and learning")
    print("\n" + "="*75)


if __name__ == "__main__":
    try:
        asyncio.run(interactive_session())
    except KeyboardInterrupt:
        print("\n\n🎸 LUCY: *waves* Cheerio, darling! Keep being brilliant! ✨\n")
