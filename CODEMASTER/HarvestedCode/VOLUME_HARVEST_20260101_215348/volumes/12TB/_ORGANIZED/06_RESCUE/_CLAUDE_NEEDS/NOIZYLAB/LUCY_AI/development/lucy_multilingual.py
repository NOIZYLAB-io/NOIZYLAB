#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🌍 LUCY - Multilingual Tutor (British + 5 Languages!) 🌍          ║
║                                                                           ║
║  British accent with lovely French, Italian, Portuguese & Spanish!       ║
║  Teaching languages while coding - LUCY style! ✨                         ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import random
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum


class Language(Enum):
    """Supported languages"""
    ENGLISH = "🇬🇧 English (British)"
    FRENCH = "🇫🇷 Français"
    ITALIAN = "🇮🇹 Italiano"
    PORTUGUESE = "🇵🇹 Português"
    SPANISH = "🇪🇸 Español"


@dataclass
class MultilingualPhrase:
    """A phrase in multiple languages"""
    english: str
    french: str
    italian: str
    portuguese: str
    spanish: str
    context: str
    british_pronunciation: str  # British accent guide
    difficulty: str


class LucyMultilingual:
    """
    LUCY - Multilingual Code Tutor!

    British accent with French, Italian, Portuguese & Spanish
    Teaching 5 languages while you code!
    """

    def __init__(self):
        self.languages = [lang.value for lang in Language]
        self.current_language = Language.FRENCH
        self.lessons_per_language = {lang: 0 for lang in Language}

        # Multilingual coding phrases
        self.coding_phrases = {
            "hello_code": MultilingualPhrase(
                english="Hello! Let's write brilliant code!",
                french="Bonjour! Écrivons du code brillant!",
                italian="Ciao! Scriviamo codice brillante!",
                portuguese="Olá! Vamos escrever código brilhante!",
                spanish="¡Hola! ¡Escribamos código brillante!",
                context="Starting a coding session",
                british_pronunciation="Heh-low! Lets right brill-yant cohd!",
                difficulty="beginner"
            ),

            "excellent_work": MultilingualPhrase(
                english="Excellent work, darling!",
                french="Excellent travail, chérie!",
                italian="Eccellente lavoro, tesoro!",
                portuguese="Excelente trabalho, querida!",
                spanish="¡Excelente trabajo, cariño!",
                context="Praising good code",
                british_pronunciation="Ek-sel-ent werk, dah-ling!",
                difficulty="beginner"
            ),

            "beautiful_code": MultilingualPhrase(
                english="What beautiful code!",
                french="Quel beau code!",
                italian="Che bel codice!",
                portuguese="Que código lindo!",
                spanish="¡Qué código hermoso!",
                context="Admiring clean code",
                british_pronunciation="Wot byoo-tif-ul cohd!",
                difficulty="beginner"
            ),

            "lets_optimize": MultilingualPhrase(
                english="Let's optimize this, shall we?",
                french="Optimisons ceci, d'accord?",
                italian="Ottimizziamo questo, va bene?",
                portuguese="Vamos otimizar isso, certo?",
                spanish="Optimicemos esto, ¿de acuerdo?",
                context="Starting optimization",
                british_pronunciation="Lets op-tim-ize this, shal we?",
                difficulty="intermediate"
            ),

            "brilliant_solution": MultilingualPhrase(
                english="That's absolutely brilliant!",
                french="C'est absolument brillant!",
                italian="È assolutamente brillante!",
                portuguese="Isso é absolutamente brilhante!",
                spanish="¡Eso es absolutamente brillante!",
                context="Clever solution found",
                british_pronunciation="Thats ab-suh-loot-lee brill-yant!",
                difficulty="beginner"
            ),

            "wine_time": MultilingualPhrase(
                english="Time for a lovely glass of wine!",
                french="C'est l'heure d'un bon verre de vin!",
                italian="È l'ora di un buon bicchiere di vino!",
                portuguese="Hora de uma boa taça de vinho!",
                spanish="¡Hora de una buena copa de vino!",
                context="Break time",
                british_pronunciation="Time for a luv-lee glahs of wine!",
                difficulty="beginner"
            ),

            "music_love": MultilingualPhrase(
                english="I adore this music!",
                french="J'adore cette musique!",
                italian="Adoro questa musica!",
                portuguese="Adoro esta música!",
                spanish="¡Adoro esta música!",
                context="Enjoying 80's music",
                british_pronunciation="Eye a-door this myoo-zik!",
                difficulty="beginner"
            ),

            "perfect": MultilingualPhrase(
                english="It's perfect!",
                french="C'est parfait!",
                italian="È perfetto!",
                portuguese="É perfeito!",
                spanish="¡Es perfecto!",
                context="Flawless code",
                british_pronunciation="Its per-fekt!",
                difficulty="beginner"
            ),

            "let's_continue": MultilingualPhrase(
                english="Let's carry on, shall we?",
                french="Continuons, d'accord?",
                italian="Continuiamo, va bene?",
                portuguese="Vamos continuar, certo?",
                spanish="Continuemos, ¿de acuerdo?",
                context="Continuing work",
                british_pronunciation="Lets kah-ree on, shal we?",
                difficulty="beginner"
            ),

            "with_style": MultilingualPhrase(
                english="With style, of course!",
                french="Avec style, bien sûr!",
                italian="Con stile, naturalmente!",
                portuguese="Com estilo, claro!",
                spanish="¡Con estilo, por supuesto!",
                context="Doing things stylishly",
                british_pronunciation="With style, of caws!",
                difficulty="beginner"
            )
        }

        # Coding terminology in all languages
        self.code_terms = {
            "function": {
                Language.ENGLISH: ("function", "funk-shun"),
                Language.FRENCH: ("fonction", "fonk-see-ohn"),
                Language.ITALIAN: ("funzione", "foon-tsyoh-neh"),
                Language.PORTUGUESE: ("função", "foon-sow"),
                Language.SPANISH: ("función", "foon-thyohn")
            },
            "variable": {
                Language.ENGLISH: ("variable", "vair-ee-uh-bul"),
                Language.FRENCH: ("variable", "vah-ree-ahbl"),
                Language.ITALIAN: ("variabile", "vah-ree-ah-bee-leh"),
                Language.PORTUGUESE: ("variável", "vah-ree-ah-vel"),
                Language.SPANISH: ("variable", "vah-ree-ah-bleh")
            },
            "class": {
                Language.ENGLISH: ("class", "klahs"),
                Language.FRENCH: ("classe", "klas"),
                Language.ITALIAN: ("classe", "klahs-seh"),
                Language.PORTUGUESE: ("classe", "klah-seh"),
                Language.SPANISH: ("clase", "klah-seh")
            },
            "error": {
                Language.ENGLISH: ("error", "eh-ruh"),
                Language.FRENCH: ("erreur", "eh-ruhr"),
                Language.ITALIAN: ("errore", "eh-roh-reh"),
                Language.PORTUGUESE: ("erro", "eh-hoo"),
                Language.SPANISH: ("error", "eh-rohr")
            },
            "code": {
                Language.ENGLISH: ("code", "kohd"),
                Language.FRENCH: ("code", "kohd"),
                Language.ITALIAN: ("codice", "koh-dee-cheh"),
                Language.PORTUGUESE: ("código", "koh-jee-goo"),
                Language.SPANISH: ("código", "koh-dee-goh")
            }
        }

        # LUCY's British expressions with multilingual flair
        self.british_expressions = [
            "Brilliant!",
            "Absolutely smashing!",
            "Lovely!",
            "Quite right!",
            "Fabulous, darling!",
            "Spot on!",
            "Cheerio!",
            "Jolly good!",
            "Splendid!",
            "Marvellous!"
        ]

    def speak_multilingual(self, phrase_key: str, language: Language = None) -> str:
        """
        LUCY speaks in any language with her British charm!
        """
        if language is None:
            language = self.current_language

        if phrase_key not in self.coding_phrases:
            phrase_key = "hello_code"

        phrase = self.coding_phrases[phrase_key]

        # Get the phrase in requested language
        text = {
            Language.ENGLISH: phrase.english,
            Language.FRENCH: phrase.french,
            Language.ITALIAN: phrase.italian,
            Language.PORTUGUESE: phrase.portuguese,
            Language.SPANISH: phrase.spanish
        }[language]

        british_touch = random.choice(self.british_expressions)

        self.lessons_per_language[language] += 1

        return (
            f"🎸 LUCY ({language.value}):\n"
            f"   {text}\n"
            f"   \n"
            f"   🇬🇧 British pronunciation: {phrase.british_pronunciation}\n"
            f"   💫 LUCY adds: \"{british_touch}\"\n"
            f"   💡 Context: {phrase.context}"
        )

    def teach_all_languages(self, phrase_key: str) -> str:
        """Teach a phrase in ALL languages at once!"""
        if phrase_key not in self.coding_phrases:
            phrase_key = "hello_code"

        phrase = self.coding_phrases[phrase_key]

        output = f"\n🌍 LUCY teaches: {phrase.context}\n"
        output += "="*70 + "\n\n"

        output += f"🇬🇧 English:    {phrase.english}\n"
        output += f"   Pronunciation: {phrase.british_pronunciation}\n\n"

        output += f"🇫🇷 French:     {phrase.french}\n\n"
        output += f"🇮🇹 Italian:    {phrase.italian}\n\n"
        output += f"🇵🇹 Portuguese: {phrase.portuguese}\n\n"
        output += f"🇪🇸 Spanish:    {phrase.spanish}\n\n"

        output += f"💡 LUCY says: \"Now you can code in 5 languages, darling! Brilliant!\"\n"

        return output

    def translate_code_term(self, term: str, show_all: bool = False) -> str:
        """Translate a coding term to all languages"""
        if term.lower() not in self.code_terms:
            return f"🎸 LUCY: I'll teach you '{term}' in all languages soon, darling!"

        translations = self.code_terms[term.lower()]

        if show_all:
            output = f"\n📚 '{term}' in 5 languages:\n"
            output += "-" * 50 + "\n"
            for lang, (word, pronunciation) in translations.items():
                output += f"{lang.value}: {word} ({pronunciation})\n"
            return output
        else:
            # Just current language
            lang = self.current_language
            word, pronunciation = translations[lang]
            return f"🎸 {lang.value}: '{term}' = '{word}' ({pronunciation})"

    def british_accent_guide(self) -> str:
        """Guide to LUCY's British accent"""
        return """
        🇬🇧 LUCY's British Accent Guide
        ================================

        LUCY speaks with a lovely British accent with hints of French!

        Pronunciation Tips:
        • "brilliant" → "brill-yant" (not "brill-ee-ant")
        • "darling" → "dah-ling" (posh British)
        • "lovely" → "luv-lee" (warm and friendly)
        • "shall we" → "shal we" (proper British)
        • "quite right" → "kwite rite" (British agreement)
        • "fabulous" → "fab-yoo-lus" (stylish)

        French influences:
        • Adds "chérie" (darling) when warm
        • Says "Magnifique!" when impressed
        • Uses "Voilà!" when presenting results
        • Throws in "C'est bon!" (it's good) naturally

        Italian flair:
        • "Bellissimo!" when code is beautiful
        • "Perfetto!" for perfect solutions

        Portuguese warmth:
        • "Que lindo!" (how beautiful)
        • "Maravilhoso!" (marvelous)

        Spanish passion:
        • "¡Fantástico!" when excited
        • "¡Increíble!" for amazing work

        LUCY seamlessly blends all 5 languages with British charm! ✨
        """

    def random_multilingual_encouragement(self) -> str:
        """LUCY encourages you in a random language"""
        encouragements = [
            ("🇬🇧", "Brilliant work, keep going!", "British charm"),
            ("🇫🇷", "Magnifique! Continue comme ça!", "French elegance"),
            ("🇮🇹", "Bellissimo! Continua così!", "Italian passion"),
            ("🇵🇹", "Maravilhoso! Continue assim!", "Portuguese warmth"),
            ("🇪🇸", "¡Fantástico! ¡Sigue así!", "Spanish enthusiasm")
        ]

        flag, phrase, style = random.choice(encouragements)

        return f"{flag} LUCY ({style}): {phrase}"

    def language_of_the_day(self) -> str:
        """Daily language focus"""
        languages = [
            {
                "lang": "🇫🇷 French",
                "lesson": "Today's French: Code = 'code', Function = 'fonction', Beautiful = 'beau'",
                "phrase": "Écrivons du beau code! (Let's write beautiful code!)"
            },
            {
                "lang": "🇮🇹 Italian",
                "lesson": "Today's Italian: Code = 'codice', Function = 'funzione', Beautiful = 'bello'",
                "phrase": "Scriviamo un bel codice! (Let's write beautiful code!)"
            },
            {
                "lang": "🇵🇹 Portuguese",
                "lesson": "Today's Portuguese: Code = 'código', Function = 'função', Beautiful = 'lindo'",
                "phrase": "Vamos escrever código lindo! (Let's write beautiful code!)"
            },
            {
                "lang": "🇪🇸 Spanish",
                "lesson": "Today's Spanish: Code = 'código', Function = 'función', Beautiful = 'hermoso'",
                "phrase": "¡Escribamos código hermoso! (Let's write beautiful code!)"
            }
        ]

        lesson = random.choice(languages)

        return (
            f"\n{lesson['lang']} - LUCY's Language of the Day\n"
            f"{'='*60}\n\n"
            f"{lesson['lesson']}\n\n"
            f"💬 Practice: {lesson['phrase']}\n\n"
            f"🎸 LUCY: \"Practice while coding, darling! It'll stick naturally! ✨\"\n"
        )

    def get_stats(self) -> Dict[str, any]:
        """Multilingual learning statistics"""
        return {
            "languages_taught": len(self.languages),
            "total_lessons": sum(self.lessons_per_language.values()),
            "lessons_by_language": {
                lang.value: count
                for lang, count in self.lessons_per_language.items()
            },
            "phrases_available": len(self.coding_phrases),
            "code_terms": len(self.code_terms),
            "current_focus": self.current_language.value,
            "lucy_says": "🌍 You're becoming brilliantly multilingual, darling!"
        }


# Demo
if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║                                                                       ║
    ║      🌍 LUCY - Multilingual Tutor (British + 5 Languages!) 🌍        ║
    ║                                                                       ║
    ║  British accent with French, Italian, Portuguese & Spanish!          ║
    ║  Teaching while you code - LUCY style! ✨                             ║
    ║                                                                       ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    """)

    lucy = LucyMultilingual()

    # Demo each language
    print("\n" + "="*70)
    print("LUCY speaks in all 5 languages:")
    print("="*70)

    for lang in Language:
        print(lucy.speak_multilingual("hello_code", lang))
        print()

    # Teach all at once
    print(lucy.teach_all_languages("excellent_work"))

    # Code term translation
    print(lucy.translate_code_term("function", show_all=True))

    # Language of the day
    print(lucy.language_of_the_day())

    # British accent guide
    print(lucy.british_accent_guide())

    # Random encouragement
    for _ in range(3):
        print(lucy.random_multilingual_encouragement())

    # Stats
    print("\n📊 Multilingual Stats:")
    for key, value in lucy.get_stats().items():
        print(f"  {key}: {value}")

    print("\n🎸 LUCY: \"Code brilliantly in 5 languages, darling! Absolutely fabulous! ✨\"\n")
