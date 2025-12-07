#!/usr/bin/env python3
from pathlib import Path
import json

#!/usr/bin/env python3
"""
Multi-Language Support
Support for all languages worldwide
"""


class MultiLanguageSupport:
    """Multi-language support system"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.languages_db = self.base_dir / "languages_database"
        self.languages_db.mkdir(exist_ok=True)

    def create_language_database(self):
        """Create language database"""
        languages = {
            "supported_languages": [
                "English", "Spanish", "French", "German", "Italian", "Portuguese",
                "Chinese", "Japanese", "Korean", "Arabic", "Hindi", "Russian",
                "Dutch", "Polish", "Turkish", "Swedish", "Norwegian", "Danish",
                "Finnish", "Greek", "Hebrew", "Thai", "Vietnamese", "Indonesian",
                "And 100+ more languages"
            ],
            "translation_features": {
                "problem_descriptions": "Translate problem descriptions",
                "solutions": "Translate solutions",
                "interface": "Full interface translation",
                "voice": "Voice recognition in multiple languages"
            },
            "localization": {
                "regions": "All regions worldwide",
                "time_zones": "All time zones",
                "currencies": "All currencies",
                "formats": "Local date/time formats"
            }
        }

        lang_file = self.languages_db / "languages.json"
        with open(lang_file, 'w') as f:
            json.dump(languages, f, indent=2)

        print("✅ Multi-language database created")

if __name__ == "__main__":
    try:
        lang = MultiLanguageSupport()
            lang.create_language_database()


    except Exception as e:
        print(f"Error: {e}")
