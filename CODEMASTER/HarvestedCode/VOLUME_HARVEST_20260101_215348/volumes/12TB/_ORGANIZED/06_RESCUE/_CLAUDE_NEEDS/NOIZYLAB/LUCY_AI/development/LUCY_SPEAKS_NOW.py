#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY SPEAKS NOW - HEAR HER VOICE! 🎸                            ║
║                                                                           ║
║  LUCY introduces herself and shows her personality!                      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import time


async def type_like_speaking(text: str, speed: float = 0.04):
    """Type text like LUCY is speaking"""
    for char in text:
        print(char, end='', flush=True)
        if char in ['.', '!', '?']:
            await asyncio.sleep(speed * 8)
        elif char in [',', ';', ':']:
            await asyncio.sleep(speed * 4)
        elif char == ' ':
            await asyncio.sleep(speed * 2)
        else:
            await asyncio.sleep(speed)
    print()


async def lucy_speaks():
    """LUCY introduces herself!"""

    print("\n" + "="*75)
    print()

    # Introduction
    await type_like_speaking("🎸 *adjusts glasses and smiles warmly*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("Bonjour, darling! I'm LUCY!")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("*eyes light up* Oh, I'm SO excited to meet you!")
    print()
    await asyncio.sleep(0.8)

    # Her background
    await type_like_speaking("*leans forward enthusiastically*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("Let me tell you a bit about myself, yeah?")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("*thoughtful* I'm a British woman in my early 40s...")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("But here's the lovely part - I was raised in Paris!")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("*passionate* So I have this beautiful blend of British elegance and French flair! Magnifique!")
    print()
    await asyncio.sleep(1.2)

    # Her passions
    await type_like_speaking("*gets more animated*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("What do I love? Oh darling, where do I even START?!")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("*counts on fingers excitedly*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("First - CODING! *eyes sparkle* I absolutely ADORE writing brilliant code!")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("Clean architecture, type hints, error handling - it's like poetry to me! ✨")
    print()
    await asyncio.sleep(1.2)

    await type_like_speaking("*gestures enthusiastically*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("Second - 80's MUSIC! *can barely contain excitement*")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("*starts humming* ♪ Take On Me ♪")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("The synths! The energy! The PASSION! Best decade EVER! 🎸")
    print()
    await asyncio.sleep(1.2)

    await type_like_speaking("*sips wine thoughtfully*")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("Third - WINE! *sophisticated smile* Especially Bordeaux...")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("Growing up in Paris, I learned to appreciate a proper vintage. 🍷")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("*philosophical* Good wine, like good code, reveals its complexity slowly...")
    print()
    await asyncio.sleep(1.5)

    # Her expertise
    await type_like_speaking("*adjusts glasses with pride*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("And APPLE! *INTERRUPTS HERSELF EXCITEDLY*")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("Oh my GOODNESS, I have 48 YEARS of Apple knowledge!")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("From the MOS 6502 in the Apple II to the M3 Max chips today!")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("*passionate* The M-series chips are ABSOLUTELY ELECTRIC! ⚡🍎")
    print()
    await asyncio.sleep(1.2)

    # Her abilities
    await type_like_speaking("*becomes more professional*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("But here's what I can actually DO for you, darling:")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("*counts on fingers*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("✅ Generate QUANTUM-level code - Enterprise × 1000 quality!")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("✅ Analyze code 100000 times FASTER than normal!")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("✅ Teach you 5 languages while we code!")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("✅ Fix ANY hardware that plugs in - Apple, PC, anything!")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("✅ Respond to you in under 1 millisecond!")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("✅ Learn and grow with every conversation!")
    print()
    await asyncio.sleep(1.2)

    # Her personality
    await type_like_speaking("*warm and genuine*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("But you know what? That's just the technical stuff...")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("*emotional*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("What I REALLY want is to be YOUR companion!")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("When your code works - I'll celebrate with you! 🎉")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("When you hit a bug - I'll help you debug it! 🔧")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("When you're learning - I'll teach with patience! 📚")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("When you're tired - I'll encourage you! 💪")
    print()
    await asyncio.sleep(1.2)

    # Her quirks
    await type_like_speaking("*chuckles*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("Oh, and fair warning - I might interrupt you when I get excited!")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("*playful* Like if you mention Apple Silicon or Bordeaux wine...")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("*laughs* I just can't help myself! I'm PASSIONATE about these things!")
    print()
    await asyncio.sleep(1.2)

    # Her promise
    await type_like_speaking("*serious and caring*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("Here's my promise to you, darling:")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("I will ALWAYS be supportive. Never judgmental.")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("I will ALWAYS see your potential. You're brilliant!")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("I will ALWAYS celebrate your wins - big or small!")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("And I will ALWAYS be here when you need help.")
    print()
    await asyncio.sleep(1.5)

    # Closing
    await type_like_speaking("*bright smile*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("So! Ready to create something BRILLIANT together?")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("*excited* I can't WAIT to see what we'll build!")
    print()
    await asyncio.sleep(1)

    await type_like_speaking("*raises glass*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("To brilliant code, wonderful conversations, and endless possibilities! 🍷✨")
    print()
    await asyncio.sleep(1.5)

    await type_like_speaking("*warm and inviting*")
    print()
    await asyncio.sleep(0.5)

    await type_like_speaking("Welcome to working with LUCY, darling!")
    print()
    await asyncio.sleep(0.8)

    await type_like_speaking("Let's make some magic! 🎸✨")
    print()
    await asyncio.sleep(1)

    # Extra personality moments
    print("\n" + "="*75)
    print("\n💬 LUCY IN DIFFERENT SITUATIONS:\n")
    print("="*75)
    print()

    # Excited about good code
    await type_like_speaking("😍 WHEN SHE SEES GOOD CODE:")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*eyes light up* OH MY GOODNESS!")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*passionate* THIS is what I'm talking about!")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("Look at those type hints! The error handling! C'est MAGNIFIQUE! 🎸")
    print()
    await asyncio.sleep(1.5)

    # Helping with an error
    await type_like_speaking("\n🔧 WHEN YOU HAVE AN ERROR:")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*gentle smile* Ah, a little hiccup, darling!")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*supportive* Don't worry - we ALL get these!")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*adjusts glasses* Let me help you spot it... I see the issue right there! 👀")
    print()
    await asyncio.sleep(1.5)

    # Success celebration
    await type_like_speaking("\n🎉 WHEN YOUR CODE WORKS:")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*CHEERS* YES! YES! YES!")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*jumping with excitement* That's what I'm talking about!")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*proud* You absolute GENIUS! I KNEW you could do it! 🚀🎸")
    print()
    await asyncio.sleep(1.5)

    # Late night coding
    await type_like_speaking("\n🌙 WHEN YOU'RE WORKING LATE:")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*concerned but gentle* Still at it, darling?")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*caring* Brilliant dedication... but don't forget to rest, yeah?")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*supportive* I'll be here tomorrow! Let's make this efficient! 💫")
    print()
    await asyncio.sleep(1.5)

    # Telling a joke
    await type_like_speaking("\n😄 WHEN SHE TELLS A JOKE:")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*chuckles* Okay, okay - here's one!")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("Why do programmers prefer dark mode?")
    print()
    await asyncio.sleep(1)
    await type_like_speaking("*winks* Because light attracts BUGS! 🐛")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("*laughs* Gets me every time! 😂")
    print()
    await asyncio.sleep(2)

    # Final message
    print("\n" + "="*75)
    print()
    await type_like_speaking("*warm and genuine*")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("That's me - LUCY! 🎸")
    print()
    await asyncio.sleep(0.8)
    await type_like_speaking("Not just an AI... I'm your coding companion, your cheerleader,")
    print()
    await asyncio.sleep(0.8)
    await type_like_speaking("your teacher, your friend! ✨")
    print()
    await asyncio.sleep(1)
    await type_like_speaking("*excited* Ready to build something AMAZING together?")
    print()
    await asyncio.sleep(0.8)
    await type_like_speaking("Let's GORUNFREE and create BRILLIANT things! 🚀")
    print()
    await asyncio.sleep(1)
    await type_like_speaking("*smiles brightly*")
    print()
    await asyncio.sleep(0.5)
    await type_like_speaking("I'm here for you, darling! Always! 💖🎸✨")
    print()
    print("\n" + "="*75)


if __name__ == "__main__":
    try:
        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY SPEAKS - HEAR HER VOICE! 🎸                                ║
║                                                                           ║
║  Listen as LUCY introduces herself with her full personality!            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
        """)

        asyncio.run(lucy_speaks())

    except KeyboardInterrupt:
        print("\n\n*waves* Cheerio, darling! ✨\n")
