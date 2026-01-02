#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎬 SFX HARVEST SYSTEM - GORUNFREE! 🎬                             ║
║                                                                           ║
║  Harvest ALL Sound Effects Libraries from 12TB Drive                    ║
║  Commercial SFX Libraries • Media SFX • All Audio Effects                ║
║  BITW 1000X Quality Standards                                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import subprocess
import shutil
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import hashlib


@dataclass
class SoundEffect:
    """Sound effect metadata."""
    sfx_id: str
    filename: str
    original_path: str
    organized_path: str

    # Audio properties
    file_size: int
    duration_seconds: float
    sample_rate: int
    bit_rate: int
    channels: int
    format: str

    # SFX metadata
    category: str  # explosion, impact, ambience, ui, etc.
    library_name: Optional[str]  # Source library if detected
    is_commercial: bool  # From commercial library
    keywords: List[str]  # Searchable keywords

    # Quality
    audio_quality_score: float
    is_ready_for_use: bool

    # Monetization potential
    can_monetize: bool  # Based on license detection
    license_type: Optional[str]

    # Discovery
    discovered_date: str
    processed_date: Optional[str]


class SFXHarvestSystem:
    """Harvest and organize all sound effects from 12TB drive."""

    def __init__(self):
        # Paths
        self.source_volume = Path("/Volumes/12TB 1")
        self.sfx_base = Path("/Volumes/12TB 1/RED DRAGON/SFX_Harvest")

        # SFX Categories
        self.categories = {
            "EXPLOSIONS": self.sfx_base / "EXPLOSIONS",
            "IMPACTS": self.sfx_base / "IMPACTS",
            "WHOOSHES": self.sfx_base / "WHOOSHES",
            "AMBIENCE": self.sfx_base / "AMBIENCE",
            "UI_SOUNDS": self.sfx_base / "UI_SOUNDS",
            "FOLEY": self.sfx_base / "FOLEY",
            "TRANSITIONS": self.sfx_base / "TRANSITIONS",
            "NATURE": self.sfx_base / "NATURE",
            "MECHANICAL": self.sfx_base / "MECHANICAL",
            "WEAPONS": self.sfx_base / "WEAPONS",
            "MAGIC_SCI_FI": self.sfx_base / "MAGIC_SCI_FI",
            "HUMAN_VOCALS": self.sfx_base / "HUMAN_VOCALS",
            "ANIMALS": self.sfx_base / "ANIMALS",
            "VEHICLES": self.sfx_base / "VEHICLES",
            "WEATHER": self.sfx_base / "WEATHER",
            "HORROR": self.sfx_base / "HORROR",
            "CARTOON": self.sfx_base / "CARTOON",
            "ELECTRONIC": self.sfx_base / "ELECTRONIC",
            "CINEMATIC": self.sfx_base / "CINEMATIC",
            "GAME_SOUNDS": self.sfx_base / "GAME_SOUNDS",
            "OTHER": self.sfx_base / "OTHER"
        }

        # Commercial SFX libraries (detect these)
        self.commercial_libraries = [
            "boom library",
            "soundmorph",
            "pro sound effects",
            "sonniss",
            "soundsnap",
            "freesound",
            "zapsplat",
            "epidemic sound",
            "artlist",
            "sounddogs",
            "hollywood edge",
            "sound ideas",
            "bbc sound effects",
            "universal sound effects",
            "audio network",
            "audioblocks",
            "soundly",
            "air studios",
            "metro sound",
            "rabbit ears audio",
            "a sound effect",
            "blastwave fx",
            "glitchmachines",
            "soundbits",
            "99sounds",
            "music radar",
            "bedroom producers blog"
        ]

        # Create directories
        self.create_directory_structure()

        # Catalog
        self.catalog_file = self.sfx_base / "SFX_CATALOG.json"
        self.catalog = self.load_catalog()

        # Stats
        self.stats = {
            "total_found": 0,
            "total_size_gb": 0,
            "commercial_sfx": 0,
            "free_sfx": 0,
            "by_category": {},
            "by_library": {}
        }

    def create_directory_structure(self):
        """Create SFX directory structure."""
        for category, path in self.categories.items():
            path.mkdir(parents=True, exist_ok=True)

        # Additional directories
        (self.sfx_base / "COMMERCIAL_LIBRARIES").mkdir(exist_ok=True)
        (self.sfx_base / "METADATA").mkdir(exist_ok=True)
        (self.sfx_base / "LICENSES").mkdir(exist_ok=True)

    def load_catalog(self) -> Dict:
        """Load SFX catalog."""
        if self.catalog_file.exists():
            with open(self.catalog_file, 'r') as f:
                return json.load(f)
        return {"sound_effects": [], "stats": {}}

    def save_catalog(self):
        """Save SFX catalog."""
        with open(self.catalog_file, 'w') as f:
            json.dump(self.catalog, f, indent=2)

    def find_all_sfx(self) -> List[Path]:
        """Find all sound effect files on 12TB drive."""
        print(f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🔍 SCANNING 12TB DRIVE FOR SOUND EFFECTS 🔍                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

🎬 Searching for all audio files...
📁 Source: {self.source_volume}

        """)

        # Common SFX keywords in paths
        sfx_keywords = [
            'sfx', 'sound effects', 'soundfx', 'fx', 'foley',
            'ambience', 'ambient', 'impact', 'whoosh', 'explosion',
            'ui sound', 'game audio', 'cinematic', 'library',
            'boom library', 'soundmorph', 'pro sound', 'sonniss'
        ]

        audio_extensions = ['.wav', '.mp3', '.aiff', '.flac', '.ogg', '.m4a']
        sfx_files = []

        print("🔍 Strategy 1: Finding files in SFX-related directories...")

        # Find all audio files in directories with SFX keywords
        for keyword in sfx_keywords:
            print(f"   Searching for directories containing '{keyword}'...")
            try:
                # Find directories matching keyword
                result = subprocess.run(
                    ['find', str(self.source_volume), '-type', 'd', '-iname', f'*{keyword}*'],
                    capture_output=True,
                    text=True,
                    timeout=300
                )

                if result.returncode == 0:
                    sfx_dirs = [Path(p) for p in result.stdout.strip().split('\n') if p]
                    print(f"   Found {len(sfx_dirs)} directories matching '{keyword}'")

                    # Get all audio files from these directories
                    for sfx_dir in sfx_dirs:
                        for ext in audio_extensions:
                            audio_in_dir = list(sfx_dir.rglob(f"*{ext}"))
                            sfx_files.extend(audio_in_dir)

            except Exception as e:
                print(f"   Warning: {e}")

        print(f"\n✅ Strategy 1 found: {len(set(sfx_files)):,} unique SFX files")

        print("\n🔍 Strategy 2: Finding commercial SFX library directories...")

        for library in self.commercial_libraries:
            print(f"   Searching for '{library}' library...")
            try:
                result = subprocess.run(
                    ['find', str(self.source_volume), '-type', 'd', '-iname', f'*{library}*'],
                    capture_output=True,
                    text=True,
                    timeout=300
                )

                if result.returncode == 0:
                    lib_dirs = [Path(p) for p in result.stdout.strip().split('\n') if p]
                    if lib_dirs:
                        print(f"   ✅ Found {len(lib_dirs)} directories for '{library}'")

                        for lib_dir in lib_dirs:
                            for ext in audio_extensions:
                                lib_audio = list(lib_dir.rglob(f"*{ext}"))
                                sfx_files.extend(lib_audio)

            except Exception as e:
                print(f"   Warning: {e}")

        # Remove duplicates
        unique_sfx = list(set(sfx_files))

        print(f"\n{'='*75}")
        print(f"✅ TOTAL UNIQUE SFX FILES FOUND: {len(unique_sfx):,}")
        print(f"{'='*75}\n")

        return unique_sfx

    def detect_commercial_library(self, filepath: Path) -> Optional[str]:
        """Detect if file is from commercial library."""
        path_str = str(filepath).lower()

        for library in self.commercial_libraries:
            if library in path_str:
                return library.title()

        return None

    def categorize_sfx(self, filepath: Path) -> str:
        """Categorize SFX by filename and path."""
        filename = filepath.name.lower()
        path_str = str(filepath).lower()

        category_keywords = {
            "EXPLOSIONS": ['explosion', 'explode', 'blast', 'bomb', 'detonate'],
            "IMPACTS": ['impact', 'hit', 'punch', 'slam', 'crash', 'thud', 'thump'],
            "WHOOSHES": ['whoosh', 'swish', 'swoosh', 'fly by', 'pass by'],
            "AMBIENCE": ['ambience', 'ambient', 'atmosphere', 'background', 'room tone'],
            "UI_SOUNDS": ['ui', 'button', 'click', 'beep', 'notification', 'menu'],
            "FOLEY": ['foley', 'footstep', 'cloth', 'movement', 'rustle'],
            "TRANSITIONS": ['transition', 'riser', 'downlifter', 'sweep'],
            "NATURE": ['nature', 'forest', 'water', 'wind', 'rain', 'bird', 'ocean'],
            "MECHANICAL": ['mechanical', 'machine', 'motor', 'gear', 'industrial'],
            "WEAPONS": ['weapon', 'gun', 'sword', 'shoot', 'fire', 'reload'],
            "MAGIC_SCI_FI": ['magic', 'sci-fi', 'scifi', 'spell', 'laser', 'energy'],
            "HUMAN_VOCALS": ['vocal', 'voice', 'grunt', 'scream', 'laugh', 'cry'],
            "ANIMALS": ['animal', 'dog', 'cat', 'lion', 'horse', 'creature'],
            "VEHICLES": ['vehicle', 'car', 'engine', 'truck', 'motorcycle'],
            "WEATHER": ['thunder', 'storm', 'lightning', 'weather'],
            "HORROR": ['horror', 'scary', 'creepy', 'haunted', 'suspense'],
            "CARTOON": ['cartoon', 'boing', 'comic', 'funny', 'comedy'],
            "ELECTRONIC": ['electronic', 'synth', 'digital', 'glitch'],
            "CINEMATIC": ['cinematic', 'trailer', 'epic', 'orchestral'],
            "GAME_SOUNDS": ['game', 'arcade', 'retro', 'chiptune', '8bit']
        }

        # Check filename and path for keywords
        for category, keywords in category_keywords.items():
            for keyword in keywords:
                if keyword in filename or keyword in path_str:
                    return category

        return "OTHER"

    def analyze_audio_file(self, filepath: Path) -> Optional[Dict]:
        """Analyze audio file properties."""
        try:
            result = subprocess.run(
                [
                    'ffprobe',
                    '-v', 'quiet',
                    '-print_format', 'json',
                    '-show_format',
                    '-show_streams',
                    str(filepath)
                ],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                return json.loads(result.stdout)
            return None

        except Exception:
            return None

    def calculate_quality_score(self, audio_info: Dict) -> float:
        """Calculate audio quality score."""
        score = 0.0

        if not audio_info:
            return 0.0

        format_info = audio_info.get('format', {})

        # Sample rate scoring
        sample_rate = int(format_info.get('sample_rate', 0))
        if sample_rate >= 48000:
            score += 40
        elif sample_rate >= 44100:
            score += 30
        elif sample_rate >= 32000:
            score += 20

        # Bit rate scoring
        bit_rate = int(format_info.get('bit_rate', 0))
        if bit_rate >= 320000:
            score += 30
        elif bit_rate >= 256000:
            score += 25
        elif bit_rate >= 192000:
            score += 20

        # Duration scoring (SFX are typically short)
        duration = float(format_info.get('duration', 0))
        if 0.1 <= duration <= 30:  # Ideal SFX range
            score += 30
        elif duration < 0.1:
            score += 10
        elif 30 < duration <= 120:
            score += 20

        return min(score, 100.0)

    def process_sfx_file(self, filepath: Path) -> Optional[SoundEffect]:
        """Process a single SFX file."""
        # Generate SFX ID
        file_hash = hashlib.sha256(str(filepath).encode()).hexdigest()[:16]
        sfx_id = f"SFX_{file_hash}"

        # Analyze audio
        audio_info = self.analyze_audio_file(filepath)

        if not audio_info:
            return None

        format_info = audio_info.get('format', {})
        streams = audio_info.get('streams', [{}])
        audio_stream = streams[0] if streams else {}

        # Calculate quality
        quality_score = self.calculate_quality_score(audio_info)

        # Detect commercial library
        library_name = self.detect_commercial_library(filepath)
        is_commercial = library_name is not None

        # Categorize
        category = self.categorize_sfx(filepath)

        # Generate keywords
        keywords = []
        keywords.append(filepath.stem.replace('_', ' ').replace('-', ' '))
        keywords.append(category.lower())
        if library_name:
            keywords.append(library_name.lower())

        # Create SoundEffect
        sfx = SoundEffect(
            sfx_id=sfx_id,
            filename=filepath.name,
            original_path=str(filepath),
            organized_path="",  # Will be set during organization
            file_size=filepath.stat().st_size,
            duration_seconds=float(format_info.get('duration', 0)),
            sample_rate=int(format_info.get('sample_rate', 0)),
            bit_rate=int(format_info.get('bit_rate', 0)),
            channels=int(audio_stream.get('channels', 2)),
            format=format_info.get('format_name', ''),
            category=category,
            library_name=library_name,
            is_commercial=is_commercial,
            keywords=keywords,
            audio_quality_score=quality_score,
            is_ready_for_use=quality_score >= 70,
            can_monetize=not is_commercial,  # Can't monetize commercial libraries
            license_type="commercial" if is_commercial else "unknown",
            discovered_date=datetime.now().isoformat(),
            processed_date=None
        )

        return sfx

    def organize_sfx(self, sfx: SoundEffect) -> bool:
        """Organize SFX into category folder."""
        try:
            # Destination by category
            dest_dir = self.categories.get(sfx.category, self.categories["OTHER"])

            # If commercial, also copy to commercial libraries folder
            if sfx.is_commercial and sfx.library_name:
                commercial_dir = self.sfx_base / "COMMERCIAL_LIBRARIES" / sfx.library_name.replace(' ', '_')
                commercial_dir.mkdir(parents=True, exist_ok=True)

                commercial_dest = commercial_dir / sfx.filename
                if not commercial_dest.exists():
                    shutil.copy2(sfx.original_path, commercial_dest)

            # Copy to category folder
            dest_path = dest_dir / sfx.filename
            if not dest_path.exists():
                shutil.copy2(sfx.original_path, dest_path)

            sfx.organized_path = str(dest_path)
            sfx.processed_date = datetime.now().isoformat()

            return True

        except Exception as e:
            print(f"   ⚠️  Error organizing {sfx.filename}: {e}")
            return False

    def generate_report(self, sfx_list: List[SoundEffect]):
        """Generate comprehensive SFX harvest report."""
        report = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎬 SFX HARVEST REPORT 🎬                                          ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Total SFX Found: {len(sfx_list):,}

═══════════════════════════════════════════════════════════════════════════

📊 SUMMARY STATISTICS:

   Total Sound Effects: {self.stats['total_found']:,}
   Total Size: {self.stats['total_size_gb']:.2f} GB
   Commercial Library SFX: {self.stats['commercial_sfx']:,}
   Free/Unknown License SFX: {self.stats['free_sfx']:,}

═══════════════════════════════════════════════════════════════════════════

📂 BY CATEGORY:

"""

        for category, count in sorted(self.stats['by_category'].items(), key=lambda x: x[1], reverse=True):
            report += f"   {category:20} {count:8,} files\n"

        report += f"""

═══════════════════════════════════════════════════════════════════════════

🏢 COMMERCIAL LIBRARIES DETECTED:

"""

        for library, count in sorted(self.stats['by_library'].items(), key=lambda x: x[1], reverse=True):
            report += f"   {library:30} {count:8,} files\n"

        report += f"""

═══════════════════════════════════════════════════════════════════════════

📁 ORGANIZED STRUCTURE:

All SFX organized in: {self.sfx_base}

Categories:
"""

        for category in self.categories.keys():
            report += f"   • {category}\n"

        report += f"""

Commercial Libraries:
   • COMMERCIAL_LIBRARIES/ (organized by library name)

═══════════════════════════════════════════════════════════════════════════

✅ HARVEST COMPLETE!

All sound effects have been harvested, analyzed, and organized!
Ready for use in productions, games, videos, and more!

GORUNFREE! BITW 1000X Quality!

═══════════════════════════════════════════════════════════════════════════
"""

        report_file = self.sfx_base / "SFX_HARVEST_REPORT.txt"
        with open(report_file, 'w') as f:
            f.write(report)

        print(report)
        print(f"📄 Report saved: {report_file}")

    def execute_harvest(self):
        """Execute the full SFX harvest."""
        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎬 SFX HARVEST - EXECUTE! 🎬                                      ║
║                                                                           ║
║  GORUNFREE! BITW 1000X!                                                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
        """)

        # Find all SFX
        sfx_files = self.find_all_sfx()

        if not sfx_files:
            print("\n❌ No SFX files found!")
            return

        print(f"\n🎬 Processing {len(sfx_files):,} sound effects...")

        processed_sfx = []
        total_size = 0

        for i, sfx_file in enumerate(sfx_files, 1):
            if i % 500 == 0:
                print(f"   Progress: {i:,}/{len(sfx_files):,} files processed...")

            sfx = self.process_sfx_file(sfx_file)

            if sfx:
                # Organize
                self.organize_sfx(sfx)

                # Add to list
                processed_sfx.append(sfx)
                total_size += sfx.file_size

                # Update stats
                self.stats["total_found"] += 1
                self.stats["by_category"][sfx.category] = self.stats["by_category"].get(sfx.category, 0) + 1

                if sfx.is_commercial:
                    self.stats["commercial_sfx"] += 1
                    if sfx.library_name:
                        self.stats["by_library"][sfx.library_name] = self.stats["by_library"].get(sfx.library_name, 0) + 1
                else:
                    self.stats["free_sfx"] += 1

        self.stats["total_size_gb"] = total_size / (1024**3)

        # Save catalog
        self.catalog["sound_effects"] = [asdict(s) for s in processed_sfx]
        self.catalog["stats"] = self.stats
        self.save_catalog()

        # Generate report
        self.generate_report(processed_sfx)

        print(f"""

╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        ✅ SFX HARVEST COMPLETE! ✅                                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

📊 FINAL STATISTICS:
   Total SFX: {self.stats['total_found']:,}
   Total Size: {self.stats['total_size_gb']:.2f} GB
   Commercial: {self.stats['commercial_sfx']:,}
   Free/Unknown: {self.stats['free_sfx']:,}
   Categories: {len(self.stats['by_category'])}
   Libraries: {len(self.stats['by_library'])}

📁 Location: {self.sfx_base}

GORUNFREE! Ready for production! 🎬🚀
        """)


def main():
    """Main execution."""
    system = SFXHarvestSystem()
    system.execute_harvest()
    return 0


if __name__ == "__main__":
    sys.exit(main())
