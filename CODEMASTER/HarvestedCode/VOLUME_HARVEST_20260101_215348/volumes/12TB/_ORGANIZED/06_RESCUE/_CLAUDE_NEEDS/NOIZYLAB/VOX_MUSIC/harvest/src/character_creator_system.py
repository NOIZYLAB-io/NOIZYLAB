#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🐠 FISHY STORYS - Interactive Character Creator 🐠                ║
║                                                                           ║
║  Kids can assemble custom characters with avatar, voice, wardrobe!      ║
║  Part of VOX - Voice Control Application                                 ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import random


@dataclass
class CharacterCustomization:
    """Complete character customization data."""
    # Basic Info
    name: str
    species: str
    age: int
    personality: str

    # Avatar
    body_type: str
    body_color: str
    fin_style: str
    tail_style: str
    scale_pattern: str
    eye_color: str
    eye_style: str

    # Wardrobe
    hat: Optional[str]
    outfit: Optional[str]
    accessory: Optional[str]
    special_item: Optional[str]

    # Voice
    voice_type: str
    voice_pitch: str  # high, medium, low
    voice_speed: str  # fast, normal, slow
    accent: Optional[str]

    # Personality Traits
    primary_emotion: str
    secondary_emotion: str
    catchphrase: str
    favorite_activity: str

    # Special Abilities
    special_power: Optional[str]
    talent: Optional[str]

    # Story Elements
    home_location: str
    best_friend: Optional[str]
    favorite_food: str
    dream: str


class CharacterCreatorSystem:
    """Interactive character creator for FISHY STORYS."""

    def __init__(self):
        self.base_path = Path("/Users/rsp_ms/MC96_MobileApp/VOX")
        self.characters_dir = self.base_path / "characters" / "CUSTOM_CHARACTERS"
        self.characters_dir.mkdir(parents=True, exist_ok=True)

        # Customization options
        self.options = {
            "species": {
                "goldfish": {"emoji": "🐠", "description": "Friendly and cheerful"},
                "clownfish": {"emoji": "🐟", "description": "Funny and playful"},
                "angelfish": {"emoji": "🐡", "description": "Graceful and kind"},
                "shark": {"emoji": "🦈", "description": "Brave and strong"},
                "dolphin": {"emoji": "🐬", "description": "Smart and energetic"},
                "octopus": {"emoji": "🐙", "description": "Creative and curious"},
                "seahorse": {"emoji": "🌀", "description": "Gentle and unique"},
                "starfish": {"emoji": "⭐", "description": "Calm and peaceful"},
                "crab": {"emoji": "🦀", "description": "Clever and protective"},
                "jellyfish": {"emoji": "🪼", "description": "Mystical and flowing"},
            },

            "body_colors": {
                "ocean_blue": {"hex": "#1E90FF", "name": "Ocean Blue"},
                "sunset_orange": {"hex": "#FF6347", "name": "Sunset Orange"},
                "coral_pink": {"hex": "#FF69B4", "name": "Coral Pink"},
                "golden_yellow": {"hex": "#FFD700", "name": "Golden Yellow"},
                "emerald_green": {"hex": "#50C878", "name": "Emerald Green"},
                "purple_reef": {"hex": "#9370DB", "name": "Purple Reef"},
                "silver_scales": {"hex": "#C0C0C0", "name": "Silver Scales"},
                "rainbow_shimmer": {"hex": "rainbow", "name": "Rainbow Shimmer"},
            },

            "fin_styles": [
                "elegant_flowing", "spiky_cool", "rounded_friendly",
                "butterfly_fancy", "streamlined_fast", "ruffled_pretty",
                "star_shaped", "dragon_scales", "glittery_sparkle"
            ],

            "tail_styles": [
                "fan_tail", "forked_tail", "ribbon_tail", "mermaid_tail",
                "comet_tail", "double_tail", "peacock_tail", "racing_tail"
            ],

            "scale_patterns": [
                "solid_smooth", "spotted_dots", "striped_lines", "swirled_design",
                "diamond_pattern", "star_burst", "rainbow_gradient", "glitter_sparkle",
                "camouflage_blend", "metallic_shine"
            ],

            "eye_styles": [
                "big_happy", "wise_knowing", "curious_wonder", "sleepy_calm",
                "sparkly_excited", "mysterious_deep", "friendly_warm", "heroic_brave"
            ],

            "hats": {
                "none": "No hat",
                "captain_hat": "⚓ Captain's Hat",
                "pirate_hat": "🏴‍☠️ Pirate Hat",
                "crown": "👑 Royal Crown",
                "flower_crown": "🌺 Flower Crown",
                "wizard_hat": "🎩 Wizard Hat",
                "sailor_cap": "⛵ Sailor Cap",
                "explorer_helmet": "🧭 Explorer Helmet",
                "chef_hat": "👨‍🍳 Chef's Hat",
            },

            "outfits": {
                "none": "No outfit",
                "superhero_cape": "🦸 Superhero Cape",
                "pirate_vest": "🏴‍☠️ Pirate Vest",
                "school_uniform": "📚 School Uniform",
                "party_outfit": "🎉 Party Outfit",
                "explorer_gear": "🔍 Explorer Gear",
                "chef_apron": "👨‍🍳 Chef's Apron",
                "royal_robe": "👑 Royal Robe",
                "sports_jersey": "⚽ Sports Jersey",
            },

            "accessories": {
                "none": "No accessory",
                "sunglasses": "😎 Cool Sunglasses",
                "bow_tie": "🎀 Fancy Bow Tie",
                "necklace": "📿 Pearl Necklace",
                "backpack": "🎒 Adventure Backpack",
                "guitar": "🎸 Musical Guitar",
                "book": "📖 Story Book",
                "telescope": "🔭 Telescope",
                "paintbrush": "🖌️ Paintbrush",
            },

            "special_items": {
                "none": "No special item",
                "magic_wand": "✨ Magic Wand",
                "treasure_map": "🗺️ Treasure Map",
                "crystal_ball": "🔮 Crystal Ball",
                "music_notes": "🎵 Floating Music Notes",
                "bubbles": "💭 Bubble Cloud",
                "stars": "⭐ Twinkling Stars",
                "rainbow": "🌈 Personal Rainbow",
                "lightbulb": "💡 Idea Lightbulb",
            },

            "voice_types": {
                "cheerful": "Happy and energetic",
                "wise": "Calm and knowledgeable",
                "playful": "Fun and silly",
                "brave": "Strong and confident",
                "gentle": "Soft and kind",
                "mysterious": "Intriguing and cool",
                "musical": "Sing-song and melodic",
                "teacher": "Clear and patient",
            },

            "emotions": [
                "happy", "curious", "brave", "kind", "silly",
                "smart", "creative", "friendly", "calm", "excited"
            ],

            "activities": [
                "exploring caves", "reading books", "playing music",
                "making friends", "solving puzzles", "helping others",
                "discovering treasures", "telling stories", "creating art",
                "dancing", "swimming races", "cooking food"
            ],

            "special_powers": {
                "none": "No special power",
                "super_speed": "⚡ Super Speed Swimming",
                "invisibility": "👻 Invisibility",
                "glow_dark": "💫 Glow in the Dark",
                "bubble_speech": "💬 Magical Bubble Speech",
                "color_change": "🎨 Color Changing",
                "water_control": "🌊 Water Bending",
                "music_magic": "🎵 Music Magic",
                "healing_touch": "✨ Healing Touch",
            },

            "talents": [
                "amazing singer", "great storyteller", "super swimmer",
                "clever inventor", "talented artist", "problem solver",
                "best friend ever", "brave explorer", "wise teacher",
                "funny comedian", "caring helper", "creative dancer"
            ],

            "home_locations": [
                "Coral Castle", "Kelp Forest Village", "Bubble Bay",
                "Pearl Palace", "Rainbow Reef", "Treasure Trench",
                "Crystal Caves", "Sunken Ship City", "Shell Shore",
                "Wave Crest Heights", "Starfish Square", "Anemone Avenue"
            ],

            "favorite_foods": [
                "kelp cookies", "plankton pizza", "seaweed salad",
                "bubble gum algae", "coral candy", "shell pasta",
                "ocean berries", "wave chips", "reef wraps",
                "sea flower soup", "current cakes", "tide treats"
            ],

            "dreams": [
                "explore the whole ocean", "make a million friends",
                "discover hidden treasures", "become a famous singer",
                "write the best stories", "help everyone be happy",
                "learn everything about the sea", "sail around the world",
                "build the coolest reef house", "start a school",
                "create beautiful art", "solve the biggest mysteries"
            ],
        }

    def generate_random_character(self) -> CharacterCustomization:
        """Generate a completely random character."""
        species = random.choice(list(self.options["species"].keys()))

        character = CharacterCustomization(
            # Basic
            name=self._generate_fish_name(),
            species=species,
            age=random.randint(5, 12),
            personality=random.choice(["friendly", "adventurous", "creative", "smart", "silly"]),

            # Avatar
            body_type=random.choice(["round_cute", "streamlined", "big_friendly", "small_quick"]),
            body_color=random.choice(list(self.options["body_colors"].keys())),
            fin_style=random.choice(self.options["fin_styles"]),
            tail_style=random.choice(self.options["tail_styles"]),
            scale_pattern=random.choice(self.options["scale_patterns"]),
            eye_color=random.choice(["blue", "green", "brown", "purple", "gold", "rainbow"]),
            eye_style=random.choice(self.options["eye_styles"]),

            # Wardrobe
            hat=random.choice(list(self.options["hats"].keys())),
            outfit=random.choice(list(self.options["outfits"].keys())),
            accessory=random.choice(list(self.options["accessories"].keys())),
            special_item=random.choice(list(self.options["special_items"].keys())),

            # Voice
            voice_type=random.choice(list(self.options["voice_types"].keys())),
            voice_pitch=random.choice(["high", "medium", "low"]),
            voice_speed=random.choice(["fast", "normal", "slow"]),
            accent=random.choice([None, "British", "Southern", "French", "Irish"]),

            # Personality
            primary_emotion=random.choice(self.options["emotions"]),
            secondary_emotion=random.choice(self.options["emotions"]),
            catchphrase=self._generate_catchphrase(),
            favorite_activity=random.choice(self.options["activities"]),

            # Special
            special_power=random.choice(list(self.options["special_powers"].keys())),
            talent=random.choice(self.options["talents"]),

            # Story
            home_location=random.choice(self.options["home_locations"]),
            best_friend=None,
            favorite_food=random.choice(self.options["favorite_foods"]),
            dream=random.choice(self.options["dreams"]),
        )

        return character

    def _generate_fish_name(self) -> str:
        """Generate a cute fish name."""
        prefixes = [
            "Fin", "Bubble", "Splash", "Wave", "Coral", "Pearl",
            "Star", "Shell", "Shimmer", "Glimmer", "Sparkle", "Twinkle"
        ]
        suffixes = [
            "ny", "ster", "bert", "bella", "son", "leigh",
            "ton", "ley", "ie", "fish", "swim", "glow"
        ]
        return random.choice(prefixes) + random.choice(suffixes)

    def _generate_catchphrase(self) -> str:
        """Generate a fun catchphrase."""
        phrases = [
            "Let's make waves!",
            "Swimming is believing!",
            "Fish yeah!",
            "Seas the day!",
            "Just keep swimming!",
            "Water wonderful adventure!",
            "Shell yeah!",
            "Making ripples!",
            "Totally fin-tastic!",
            "Swim-credible!",
        ]
        return random.choice(phrases)

    def save_character(self, character: CharacterCustomization) -> Path:
        """Save character to JSON file."""
        filename = f"{character.name.lower().replace(' ', '_')}.json"
        filepath = self.characters_dir / filename

        with open(filepath, 'w') as f:
            json.dump(asdict(character), f, indent=2)

        return filepath

    def load_character(self, name: str) -> Optional[CharacterCustomization]:
        """Load character from JSON file."""
        filename = f"{name.lower().replace(' ', '_')}.json"
        filepath = self.characters_dir / filename

        if not filepath.exists():
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)

        return CharacterCustomization(**data)

    def list_all_characters(self) -> List[str]:
        """List all saved characters."""
        return [f.stem.replace('_', ' ').title() for f in self.characters_dir.glob("*.json")]

    def generate_character_card(self, character: CharacterCustomization) -> str:
        """Generate a character card display."""
        species_info = self.options["species"][character.species]
        color_info = self.options["body_colors"][character.body_color]

        card = f"""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║    {species_info['emoji']} {character.name.upper()} {species_info['emoji']}                                              ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

📋 BASIC INFO:
   Species: {character.species.title()} {species_info['emoji']}
   Age: {character.age} years old
   Personality: {character.personality.title()}
   Catchphrase: "{character.catchphrase}"

🎨 APPEARANCE:
   Body Color: {color_info['name']}
   Fin Style: {character.fin_style.replace('_', ' ').title()}
   Tail Style: {character.tail_style.replace('_', ' ').title()}
   Scale Pattern: {character.scale_pattern.replace('_', ' ').title()}
   Eye Style: {character.eye_style.replace('_', ' ').title()} ({character.eye_color})

👔 WARDROBE:
   Hat: {self.options['hats'].get(character.hat, 'None')}
   Outfit: {self.options['outfits'].get(character.outfit, 'None')}
   Accessory: {self.options['accessories'].get(character.accessory, 'None')}
   Special Item: {self.options['special_items'].get(character.special_item, 'None')}

🎤 VOICE:
   Type: {character.voice_type.title()}
   Pitch: {character.voice_pitch.title()}
   Speed: {character.voice_speed.title()}
   Accent: {character.accent if character.accent else 'None'}

💖 PERSONALITY:
   Primary Emotion: {character.primary_emotion.title()}
   Secondary Emotion: {character.secondary_emotion.title()}
   Favorite Activity: {character.favorite_activity}
   Talent: {character.talent.title()}

✨ SPECIAL:
   Special Power: {self.options['special_powers'].get(character.special_power, 'None')}

🏠 BACKGROUND:
   Home: {character.home_location}
   Favorite Food: {character.favorite_food.title()}
   Dream: {character.dream.title()}

═══════════════════════════════════════════════════════════════════
"""
        return card


def main():
    """Demo the character creator."""
    creator = CharacterCreatorSystem()

    print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║    🐠 FISHY STORYS - CHARACTER CREATOR DEMO 🐠                   ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
    """)

    print("\n🎲 Generating 3 random example characters...\n")

    for i in range(3):
        character = creator.generate_random_character()
        creator.save_character(character)
        print(creator.generate_character_card(character))
        print("\n")

    print("✅ Example characters saved!")
    print(f"📁 Location: {creator.characters_dir}")
    print(f"\n🎯 Total characters created: {len(creator.list_all_characters())}")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
