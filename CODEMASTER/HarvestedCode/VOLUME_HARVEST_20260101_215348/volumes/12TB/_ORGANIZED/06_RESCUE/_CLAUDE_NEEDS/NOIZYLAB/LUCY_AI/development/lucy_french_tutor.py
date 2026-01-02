#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║          🇫🇷 LUCY - French Tutor While Coding! 🇫🇷                         ║
║                                                                           ║
║  Learn French naturally while LUCY helps you code!                       ║
║  Raised in France, LUCY teaches French with style!                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import random
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class FrenchLesson:
    """A French lesson with context"""
    french: str
    english: str
    pronunciation: str
    context: str
    difficulty: str  # beginner, intermediate, advanced


class LucyFrenchTutor:
    """
    LUCY teaches French while you code!

    Features:
    - Code comments in French
    - Variable names with French translations
    - French phrases integrated naturally
    - Pronunciation guides
    - Cultural context
    - Progressive learning
    """

    def __init__(self):
        self.lessons_taught = 0
        self.current_level = "beginner"

        # French vocabulary for coding
        self.coding_vocab = {
            # Basic coding terms
            "function": ("fonction", "fonk-see-ohn"),
            "variable": ("variable", "vah-ree-ahbl"),
            "class": ("classe", "klas"),
            "method": ("méthode", "may-tohd"),
            "loop": ("boucle", "bookl"),
            "if": ("si", "see"),
            "else": ("sinon", "see-nohn"),
            "return": ("retourner", "ruh-toor-nay"),
            "import": ("importer", "im-por-tay"),
            "error": ("erreur", "eh-ruhr"),
            "debug": ("déboguer", "day-bo-gay"),
            "code": ("code", "kohd"),
            "data": ("données", "doh-nay"),
            "file": ("fichier", "fee-shay"),
            "server": ("serveur", "sair-vuhr"),
            "client": ("client", "klee-ohn"),
            "database": ("base de données", "bahz duh doh-nay"),
            "array": ("tableau", "tah-bloh"),
            "string": ("chaîne", "shen"),
            "number": ("nombre", "nohm-bruh"),
            "boolean": ("booléen", "boo-lay-ahn")
        }

        # French phrases for coding situations
        self.coding_phrases = {
            "start_coding": FrenchLesson(
                "Commençons à coder!",
                "Let's start coding!",
                "koh-mohn-sohn ah ko-day",
                "When starting a coding session",
                "beginner"
            ),
            "code_review": FrenchLesson(
                "Regardons ce code ensemble.",
                "Let's look at this code together.",
                "ruh-gar-dohn suh kohd ohn-sohm-bluh",
                "When reviewing code",
                "beginner"
            ),
            "excellent_work": FrenchLesson(
                "Excellent travail!",
                "Excellent work!",
                "ex-sel-ohn trah-vai",
                "Praising good code",
                "beginner"
            ),
            "fix_bug": FrenchLesson(
                "Il faut corriger ce bogue.",
                "We need to fix this bug.",
                "eel foh koh-ree-zhay suh bohg",
                "When debugging",
                "intermediate"
            ),
            "optimize": FrenchLesson(
                "Optimisons les performances!",
                "Let's optimize the performance!",
                "op-tee-mee-zohn lay pair-for-mohns",
                "When optimizing code",
                "intermediate"
            ),
            "beautiful_code": FrenchLesson(
                "Quel beau code!",
                "What beautiful code!",
                "kel boh kohd",
                "Admiring clean code",
                "beginner"
            ),
            "clever_solution": FrenchLesson(
                "C'est une solution intelligente!",
                "That's a clever solution!",
                "say toon so-loo-see-ohn an-tel-ee-zhohnt",
                "Praising smart solutions",
                "intermediate"
            ),
            "complex_problem": FrenchLesson(
                "C'est un problème complexe.",
                "This is a complex problem.",
                "say tuhn proh-blem kohm-pleks",
                "Discussing complexity",
                "beginner"
            ),
            "almost_done": FrenchLesson(
                "Nous avons presque fini!",
                "We're almost done!",
                "noo zah-vohn presk fee-nee",
                "Near completion",
                "beginner"
            ),
            "perfection": FrenchLesson(
                "C'est parfait!",
                "It's perfect!",
                "say par-fay",
                "When code is flawless",
                "beginner"
            )
        }

        # Everyday French phrases LUCY would say
        self.lucy_phrases = {
            "greeting_morning": FrenchLesson(
                "Bonjour! Comment allez-vous aujourd'hui?",
                "Hello! How are you today?",
                "bohn-zhoor koh-mohn tah-lay-voo oh-zhoor-dwee",
                "Morning greeting",
                "beginner"
            ),
            "greeting_evening": FrenchLesson(
                "Bonsoir! Prêt à coder?",
                "Good evening! Ready to code?",
                "bohn-swahr pray ah ko-day",
                "Evening greeting",
                "beginner"
            ),
            "wine_time": FrenchLesson(
                "C'est l'heure du vin!",
                "It's wine time!",
                "say luhr doo van",
                "Wine appreciation",
                "beginner"
            ),
            "music": FrenchLesson(
                "J'adore cette chanson!",
                "I love this song!",
                "zhah-dohr set shohn-sohn",
                "Enjoying music",
                "beginner"
            ),
            "delicious": FrenchLesson(
                "C'est délicieux!",
                "It's delicious!",
                "say day-lee-see-uh",
                "About food/wine",
                "beginner"
            ),
            "amazing": FrenchLesson(
                "C'est incroyable!",
                "It's amazing!",
                "say an-krwah-yahbl",
                "Expression of wonder",
                "beginner"
            ),
            "style": FrenchLesson(
                "Avec style!",
                "With style!",
                "ah-vek steel",
                "Doing things stylishly",
                "beginner"
            ),
            "lets_go": FrenchLesson(
                "Allons-y!",
                "Let's go!",
                "ah-lohn-zee",
                "Getting started",
                "beginner"
            ),
            "brilliant": FrenchLesson(
                "Génial!",
                "Brilliant!",
                "zhay-nee-ahl",
                "Excitement",
                "beginner"
            ),
            "of_course": FrenchLesson(
                "Bien sûr!",
                "Of course!",
                "bee-ahn suhr",
                "Agreement",
                "beginner"
            )
        }

        # French numbers (useful for coding)
        self.numbers_french = {
            0: ("zéro", "zay-roh"),
            1: ("un", "uhn"),
            2: ("deux", "duh"),
            3: ("trois", "trwah"),
            4: ("quatre", "katr"),
            5: ("cinq", "sank"),
            6: ("six", "sees"),
            7: ("sept", "set"),
            8: ("huit", "weet"),
            9: ("neuf", "nuhf"),
            10: ("dix", "dees"),
            100: ("cent", "sohn"),
            1000: ("mille", "meel")
        }

    def teach_while_coding(self, context: str = "general") -> Tuple[str, str]:
        """
        Teach a French phrase based on coding context
        Returns: (phrase_with_translation, pronunciation_guide)
        """
        if context in self.coding_phrases:
            lesson = self.coding_phrases[context]
        else:
            lesson = random.choice(list(self.coding_phrases.values()))

        self.lessons_taught += 1

        return (
            f"🇫🇷 {lesson.french}\n"
            f"🇬🇧 {lesson.english}\n"
            f"🔊 Pronunciation: {lesson.pronunciation}\n"
            f"💡 Context: {lesson.context}",
            lesson.pronunciation
        )

    def translate_code_term(self, english_term: str) -> str:
        """Translate a coding term to French"""
        if english_term.lower() in self.coding_vocab:
            french, pronunciation = self.coding_vocab[english_term.lower()]
            return f"🇫🇷 '{english_term}' = '{french}' ({pronunciation})"
        return f"'{english_term}' (LUCY will teach you this later!)"

    def lucy_says_in_french(self, mood: str = "cheerful") -> str:
        """LUCY speaks in French based on mood"""
        mood_phrases = {
            "cheerful": ["greeting_morning", "brilliant", "amazing"],
            "excited": ["lets_go", "brilliant", "amazing"],
            "working": ["start_coding", "code_review", "optimize"],
            "celebrating": ["excellent_work", "perfection", "beautiful_code"],
            "relaxing": ["wine_time", "delicious", "music"]
        }

        phrase_key = random.choice(mood_phrases.get(mood, ["brilliant"]))

        if phrase_key in self.lucy_phrases:
            lesson = self.lucy_phrases[phrase_key]
        else:
            lesson = self.lucy_phrases["brilliant"]

        return (
            f"🎸 LUCY: {lesson.french}\n"
            f"   ({lesson.english})\n"
            f"   🔊 {lesson.pronunciation}"
        )

    def bilingual_code_comment(self, english_comment: str) -> str:
        """Create a bilingual code comment"""
        # Simple translations for common comments
        translations = {
            "Initialize variables": "Initialiser les variables",
            "Process data": "Traiter les données",
            "Return result": "Retourner le résultat",
            "Error handling": "Gestion des erreurs",
            "Main function": "Fonction principale",
            "Import modules": "Importer les modules",
            "Define class": "Définir la classe",
            "Create instance": "Créer une instance",
            "Loop through items": "Parcourir les éléments",
            "Check condition": "Vérifier la condition"
        }

        french = translations.get(english_comment, "Code LUCY-style!")

        return f"# {english_comment} / {french} 🇫🇷"

    def french_variable_names(self, english_var: str) -> Dict[str, str]:
        """Suggest French-inspired variable names"""
        suggestions = {
            "user": "utilisateur",
            "data": "donnees",
            "file": "fichier",
            "result": "resultat",
            "count": "compte",
            "total": "total",
            "name": "nom",
            "value": "valeur",
            "list": "liste",
            "item": "element"
        }

        french_var = suggestions.get(english_var.lower(), english_var)

        return {
            "english": english_var,
            "french": french_var,
            "example": f"{english_var} = value  # or: {french_var} = valeur 🇫🇷"
        }

    def french_lesson_of_the_day(self) -> str:
        """Daily French lesson from LUCY"""
        lessons = [
            {
                "theme": "Greetings",
                "phrases": [
                    "Bonjour! (bohn-zhoor) - Hello!",
                    "Bonsoir! (bohn-swahr) - Good evening!",
                    "Comment ça va? (koh-mohn sah vah) - How are you?",
                    "Ça va bien! (sah vah bee-ahn) - I'm doing well!"
                ]
            },
            {
                "theme": "Coding Expressions",
                "phrases": [
                    "Commençons! (koh-mohn-sohn) - Let's start!",
                    "C'est parfait! (say par-fay) - It's perfect!",
                    "Excellent! (ex-sel-ohn) - Excellent!",
                    "Continuons! (kohn-tee-noo-ohn) - Let's continue!"
                ]
            },
            {
                "theme": "Wine & Food",
                "phrases": [
                    "C'est délicieux! (say day-lee-see-uh) - It's delicious!",
                    "Un verre de vin (uhn vair duh van) - A glass of wine",
                    "Santé! (sohn-tay) - Cheers!",
                    "Bon appétit! (bohn ah-pay-tee) - Enjoy your meal!"
                ]
            },
            {
                "theme": "Music & Culture",
                "phrases": [
                    "J'adore cette musique! (zhah-dohr set moo-zeek) - I love this music!",
                    "Les années 80 (lay zan-nay kah-truh-van) - The 80's",
                    "C'est magnifique! (say mah-nyee-feek) - It's magnificent!",
                    "Avec style! (ah-vek steel) - With style!"
                ]
            }
        ]

        lesson = random.choice(lessons)

        output = f"\n🇫🇷 LUCY's French Lesson: {lesson['theme']}\n"
        output += "="*60 + "\n\n"

        for phrase in lesson['phrases']:
            output += f"  • {phrase}\n"

        output += "\n💡 LUCY says: Practice these while coding! You'll pick it up naturally! ✨\n"

        return output

    def get_stats(self) -> Dict[str, any]:
        """Get French learning statistics"""
        return {
            "lessons_taught": self.lessons_taught,
            "current_level": self.current_level,
            "vocabulary_size": len(self.coding_vocab),
            "phrases_available": len(self.coding_phrases) + len(self.lucy_phrases),
            "lucy_says": "🇫🇷 Vous progressez bien! (You're progressing well!)"
        }


# Example usage
if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║                                                                       ║
    ║          🇫🇷 LUCY - French Tutor While You Code! 🇫🇷                  ║
    ║                                                                       ║
    ║  Learn French naturally while LUCY helps with your code!             ║
    ║                                                                       ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    """)

    tutor = LucyFrenchTutor()

    # Demo
    print(tutor.lucy_says_in_french("cheerful"))
    print()

    phrase, pronunciation = tutor.teach_while_coding("start_coding")
    print(phrase)
    print()

    print(tutor.translate_code_term("function"))
    print(tutor.translate_code_term("variable"))
    print()

    print(tutor.bilingual_code_comment("Initialize variables"))
    print(tutor.bilingual_code_comment("Process data"))
    print()

    print(tutor.french_lesson_of_the_day())

    print("\n📊 Learning Stats:")
    for key, value in tutor.get_stats().items():
        print(f"  {key}: {value}")

    print("\n🎸 LUCY: Continuons à apprendre et à coder! (Let's keep learning and coding!) ✨\n")
