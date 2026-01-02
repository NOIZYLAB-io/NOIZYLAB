#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎙️ VOICE HARVESTER - Audio Collection & Organization 🎙️         ║
║                                                                           ║
║  GORUNFREE Voice Collection System                                       ║
║  Find, Analyze, Organize, and Catalog ALL quality voice audio           ║
║  BITW 1000X Quality Standards                                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import json
import subprocess
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import hashlib


@dataclass
class VoiceAudioFile:
    """Cataloged voice audio file."""
    # File info
    original_path: str
    filename: str
    file_hash: str
    file_size_mb: float

    # Audio properties
    duration_seconds: float
    sample_rate: int
    channels: int
    format: str
    bit_rate: int

    # Voice characteristics (analyzed)
    voice_type: str  # male, female, child, character
    estimated_age_range: str  # child, teen, adult, elderly
    vocal_quality: str  # clear, breathy, gravelly, smooth
    energy_level: str  # low, medium, high

    # Quality metrics
    audio_quality_score: float  # 0-100
    has_background_noise: bool
    has_music: bool
    is_clean_voice: bool

    # Cataloging
    category: str  # character, narration, dialogue, etc.
    tags: List[str]
    potential_uses: List[str]

    # Organization
    harvested_date: str
    organized_path: str
    notes: str


class VoiceHarvester:
    """Harvest and organize voice audio from entire volumes."""

    def __init__(self):
        self.base_path = Path("/Volumes/12TB 1/NOIZYVOX")
        self.harvest_dir = self.base_path
        self.catalog_file = self.harvest_dir / "VOICE_CATALOG.json"

        # Organized by category
        self.categories = {
            "character_voices": self.harvest_dir / "CHARACTER_VOICES",
            "narration": self.harvest_dir / "NARRATION",
            "dialogue": self.harvest_dir / "DIALOGUE",
            "children": self.harvest_dir / "CHILDREN_VOICES",
            "male_adult": self.harvest_dir / "MALE_ADULT",
            "female_adult": self.harvest_dir / "FEMALE_ADULT",
            "elderly": self.harvest_dir / "ELDERLY_VOICES",
            "special_fx": self.harvest_dir / "SPECIAL_FX_VOICES",
            "emotional": self.harvest_dir / "EMOTIONAL_SAMPLES",
            "teaching": self.harvest_dir / "TEACHING_VOICES",
        }

        # Create all directories
        for category_dir in self.categories.values():
            category_dir.mkdir(parents=True, exist_ok=True)

        self.catalog = self.load_catalog()

    def load_catalog(self) -> Dict:
        """Load existing catalog or create new one."""
        if self.catalog_file.exists():
            with open(self.catalog_file, 'r') as f:
                return json.load(f)
        return {"files": [], "stats": {}}

    def save_catalog(self):
        """Save catalog to JSON."""
        with open(self.catalog_file, 'w') as f:
            json.dump(self.catalog, f, indent=2)

    def calculate_file_hash(self, filepath: Path) -> str:
        """Calculate SHA256 hash of file."""
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def analyze_audio_file(self, filepath: Path) -> Optional[Dict]:
        """Analyze audio file using ffprobe."""
        try:
            cmd = [
                "ffprobe",
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                "-show_streams",
                str(filepath)
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                data = json.loads(result.stdout)
                stream = data.get("streams", [{}])[0]
                format_info = data.get("format", {})

                return {
                    "duration": float(format_info.get("duration", 0)),
                    "sample_rate": int(stream.get("sample_rate", 0)),
                    "channels": int(stream.get("channels", 0)),
                    "bit_rate": int(format_info.get("bit_rate", 0)),
                    "format": format_info.get("format_name", "unknown"),
                }
        except Exception as e:
            print(f"   ⚠️  Analysis error: {e}")

        return None

    def detect_voice_characteristics(self, filepath: Path, audio_info: Dict) -> Dict:
        """Detect voice characteristics from audio."""
        # This is a simplified version - in production you'd use ML models
        # For now, use heuristics based on audio properties

        characteristics = {
            "voice_type": "unknown",
            "estimated_age_range": "unknown",
            "vocal_quality": "unknown",
            "energy_level": "medium",
        }

        sample_rate = audio_info.get("sample_rate", 0)
        duration = audio_info.get("duration", 0)

        # Simple heuristics (would be replaced with ML in production)
        if sample_rate >= 44100:
            characteristics["vocal_quality"] = "clear"
        elif sample_rate >= 22050:
            characteristics["vocal_quality"] = "good"
        else:
            characteristics["vocal_quality"] = "basic"

        # Analyze filename for clues
        filename_lower = filepath.name.lower()

        if any(word in filename_lower for word in ["child", "kid", "baby", "young"]):
            characteristics["voice_type"] = "child"
            characteristics["estimated_age_range"] = "child"
        elif any(word in filename_lower for word in ["woman", "female", "girl", "lady"]):
            characteristics["voice_type"] = "female"
            characteristics["estimated_age_range"] = "adult"
        elif any(word in filename_lower for word in ["man", "male", "boy", "guy"]):
            characteristics["voice_type"] = "male"
            characteristics["estimated_age_range"] = "adult"
        elif any(word in filename_lower for word in ["old", "elderly", "grandma", "grandpa"]):
            characteristics["estimated_age_range"] = "elderly"
        elif any(word in filename_lower for word in ["character", "cartoon", "disney"]):
            characteristics["voice_type"] = "character"

        return characteristics

    def categorize_file(self, filepath: Path, characteristics: Dict) -> Tuple[str, List[str]]:
        """Determine category and tags for file."""
        filename_lower = filepath.name.lower()

        # Determine primary category
        category = "dialogue"  # default

        if characteristics["voice_type"] == "character":
            category = "character_voices"
        elif characteristics["voice_type"] == "child" or characteristics["estimated_age_range"] == "child":
            category = "children"
        elif characteristics["estimated_age_range"] == "elderly":
            category = "elderly"
        elif characteristics["voice_type"] == "male":
            category = "male_adult"
        elif characteristics["voice_type"] == "female":
            category = "female_adult"
        elif any(word in filename_lower for word in ["narrat", "story", "book"]):
            category = "narration"
        elif any(word in filename_lower for word in ["teach", "instruct", "learn", "lesson"]):
            category = "teaching"
        elif any(word in filename_lower for word in ["emotion", "cry", "laugh", "scream", "happy", "sad"]):
            category = "emotional"

        # Generate tags
        tags = []

        # Emotion tags
        emotion_keywords = {
            "happy": ["happy", "joy", "laugh", "cheer"],
            "sad": ["sad", "cry", "weep", "sorrow"],
            "angry": ["angry", "mad", "rage", "yell"],
            "scared": ["scared", "fear", "terror", "afraid"],
            "excited": ["excited", "energetic", "enthusiastic"],
        }

        for emotion, keywords in emotion_keywords.items():
            if any(kw in filename_lower for kw in keywords):
                tags.append(emotion)

        # Context tags
        if any(word in filename_lower for word in ["disney", "cartoon", "animation"]):
            tags.append("animated")
        if any(word in filename_lower for word in ["tale", "spin", "baloo"]):
            tags.append("talespin")
        if any(word in filename_lower for word in ["music", "sing", "song"]):
            tags.append("musical")
        if any(word in filename_lower for word in ["dialogue", "conversation", "talk"]):
            tags.append("dialogue")

        return category, tags

    def determine_potential_uses(self, characteristics: Dict, category: str) -> List[str]:
        """Determine potential uses for this voice."""
        uses = []

        if category == "character_voices":
            uses.extend([
                "FISHY STORYS characters",
                "MUSI teaching characters",
                "Game characters",
                "Animation voice-over",
            ])

        if category == "children":
            uses.extend([
                "Children's educational content",
                "FISHY STORYS (Bubbles type)",
                "Young character voices",
            ])

        if category == "narration":
            uses.extend([
                "Audiobook narration",
                "Story telling",
                "Documentary voice-over",
            ])

        if category == "teaching":
            uses.extend([
                "MUSI instructors",
                "Educational videos",
                "Tutorial voice-over",
            ])

        if category == "elderly":
            uses.extend([
                "FISHY STORYS (Grandma Pearl, Captain Finn)",
                "Wise character voices",
                "Storyteller voices",
            ])

        if characteristics.get("vocal_quality") == "clear":
            uses.append("Professional voice cloning")

        return uses

    def harvest_file(self, filepath: Path, quality_threshold: float = 60.0) -> Optional[VoiceAudioFile]:
        """Harvest a single audio file."""
        # Check if already cataloged
        file_hash = self.calculate_file_hash(filepath)
        for cataloged in self.catalog.get("files", []):
            if cataloged.get("file_hash") == file_hash:
                return None  # Already have this file

        # Analyze audio
        audio_info = self.analyze_audio_file(filepath)
        if not audio_info:
            return None

        # Skip very short files (< 0.5 seconds)
        if audio_info["duration"] < 0.5:
            return None

        # Detect voice characteristics
        characteristics = self.detect_voice_characteristics(filepath, audio_info)

        # Categorize
        category, tags = self.categorize_file(filepath, characteristics)

        # Determine potential uses
        potential_uses = self.determine_potential_uses(characteristics, category)

        # Calculate quality score (simplified)
        quality_score = 70.0  # Base score
        if audio_info["sample_rate"] >= 44100:
            quality_score += 15
        if audio_info["bit_rate"] >= 256000:
            quality_score += 10
        if characteristics["vocal_quality"] == "clear":
            quality_score += 5

        # Skip low quality
        if quality_score < quality_threshold:
            return None

        # Create voice audio file record
        voice_file = VoiceAudioFile(
            original_path=str(filepath),
            filename=filepath.name,
            file_hash=file_hash,
            file_size_mb=filepath.stat().st_size / (1024 * 1024),
            duration_seconds=audio_info["duration"],
            sample_rate=audio_info["sample_rate"],
            channels=audio_info["channels"],
            format=audio_info["format"],
            bit_rate=audio_info["bit_rate"],
            voice_type=characteristics["voice_type"],
            estimated_age_range=characteristics["estimated_age_range"],
            vocal_quality=characteristics["vocal_quality"],
            energy_level=characteristics["energy_level"],
            audio_quality_score=quality_score,
            has_background_noise=False,  # Would need deeper analysis
            has_music=False,  # Would need deeper analysis
            is_clean_voice=True,  # Assume true for high quality
            category=category,
            tags=tags,
            potential_uses=potential_uses,
            harvested_date=datetime.now().isoformat(),
            organized_path="",  # Will be set when organizing
            notes="",
        )

        # Copy to organized location
        dest_dir = self.categories[category]
        dest_path = dest_dir / filepath.name

        # Handle duplicate filenames
        counter = 1
        while dest_path.exists():
            dest_path = dest_dir / f"{filepath.stem}_{counter}{filepath.suffix}"
            counter += 1

        try:
            shutil.copy2(filepath, dest_path)
            voice_file.organized_path = str(dest_path)
            return voice_file
        except Exception as e:
            print(f"   ❌ Copy error: {e}")
            return None

    def harvest_directory(self, directory: Path, recursive: bool = True):
        """Harvest all voice files from a directory."""
        print(f"\n🎙️  Harvesting voice files from: {directory}")
        print("=" * 75)

        # Find all audio files
        audio_extensions = [".wav", ".mp3", ".m4a", ".aiff", ".flac", ".ogg"]

        if recursive:
            audio_files = []
            for ext in audio_extensions:
                audio_files.extend(directory.rglob(f"*{ext}"))
        else:
            audio_files = []
            for ext in audio_extensions:
                audio_files.extend(directory.glob(f"*{ext}"))

        print(f"📊 Found {len(audio_files)} audio files to analyze\n")

        harvested_count = 0
        skipped_count = 0

        for i, audio_file in enumerate(audio_files, 1):
            if i % 100 == 0:
                print(f"   Progress: {i}/{len(audio_files)} files processed...")

            voice_file = self.harvest_file(audio_file)

            if voice_file:
                self.catalog["files"].append(asdict(voice_file))
                harvested_count += 1

                if harvested_count % 10 == 0:
                    self.save_catalog()  # Save periodically
            else:
                skipped_count += 1

        # Final save
        self.save_catalog()

        # Update stats
        self.catalog["stats"] = {
            "total_harvested": harvested_count,
            "total_analyzed": len(audio_files),
            "last_harvest_date": datetime.now().isoformat(),
        }
        self.save_catalog()

        print(f"\n✅ Harvest complete!")
        print(f"   Harvested: {harvested_count} files")
        print(f"   Skipped: {skipped_count} files")
        print(f"   Total in catalog: {len(self.catalog['files'])} files")

    def generate_harvest_report(self) -> str:
        """Generate comprehensive harvest report."""
        files = self.catalog.get("files", [])

        if not files:
            return "No files in catalog yet."

        # Calculate statistics
        categories_count = {}
        voice_types_count = {}
        total_duration = 0
        total_size = 0

        for file_data in files:
            category = file_data.get("category", "unknown")
            categories_count[category] = categories_count.get(category, 0) + 1

            voice_type = file_data.get("voice_type", "unknown")
            voice_types_count[voice_type] = voice_types_count.get(voice_type, 0) + 1

            total_duration += file_data.get("duration_seconds", 0)
            total_size += file_data.get("file_size_mb", 0)

        report = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎙️ VOICE HARVEST REPORT 🎙️                                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

📊 OVERALL STATISTICS:

   Total Files Harvested: {len(files):,}
   Total Duration: {total_duration/60:.1f} minutes ({total_duration/3600:.1f} hours)
   Total Size: {total_size:.2f} MB ({total_size/1024:.2f} GB)
   Average Quality Score: {sum(f.get('audio_quality_score', 0) for f in files) / len(files):.1f}/100

═══════════════════════════════════════════════════════════════════════════

📁 BY CATEGORY:

"""

        for category, count in sorted(categories_count.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / len(files)) * 100
            report += f"   {category.replace('_', ' ').title():<25} {count:>6} files ({percentage:>5.1f}%)\n"

        report += f"""
═══════════════════════════════════════════════════════════════════════════

🎤 BY VOICE TYPE:

"""

        for voice_type, count in sorted(voice_types_count.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / len(files)) * 100
            report += f"   {voice_type.title():<25} {count:>6} files ({percentage:>5.1f}%)\n"

        report += f"""
═══════════════════════════════════════════════════════════════════════════

🌟 TOP QUALITY FILES (Top 10):

"""

        top_files = sorted(files, key=lambda x: x.get("audio_quality_score", 0), reverse=True)[:10]

        for i, file_data in enumerate(top_files, 1):
            report += f"""   {i}. {file_data.get('filename', 'unknown')}
      Quality: {file_data.get('audio_quality_score', 0):.1f}/100
      Type: {file_data.get('voice_type', 'unknown')}
      Category: {file_data.get('category', 'unknown')}
      Duration: {file_data.get('duration_seconds', 0):.1f}s

"""

        report += f"""═══════════════════════════════════════════════════════════════════════════

📍 STORAGE LOCATIONS:

"""

        for category_name, category_path in self.categories.items():
            file_count = categories_count.get(category_name, 0)
            report += f"   {category_name.replace('_', ' ').title():<25} {file_count:>4} files\n"
            report += f"      {category_path}\n\n"

        report += f"""═══════════════════════════════════════════════════════════════════════════

✅ HARVEST COMPLETE - ALL FILES ORGANIZED AND CATALOGED!

Catalog file: {self.catalog_file}

"""

        return report


def main():
    """Main entry point."""
    harvester = VoiceHarvester()

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎙️ VOICE HARVESTER - GORUNFREE! 🎙️                              ║
║                                                                           ║
║  BITW 1000X Quality Voice Collection System                              ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

READY TO HARVEST VOICES!

Usage:
  1. Place audio files in a directory
  2. Run: harvester.harvest_directory(Path("/path/to/audio"))
  3. View report: harvester.generate_harvest_report()

Categories:
""")

    for category_name, category_path in harvester.categories.items():
        print(f"  • {category_name.replace('_', ' ').title()}")

    print(f"\nCatalog: {harvester.catalog_file}")
    print(f"Current catalog size: {len(harvester.catalog.get('files', []))} files")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
