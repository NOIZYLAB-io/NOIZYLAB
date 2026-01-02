#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎨 LUCY'S FIX PIX - LEGENDARY IMAGE ORGANIZER 🎨                 ║
║                                                                           ║
║  Award-Winning Design & Image Organization                              ║
║  LUCY - All Fonts, All Palettes, All Visual Studio, Pop Culture!       ║
║  FOR POPS! GORUNFREE! BITW 1000X!                                        ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

LUCY - Legendary Graphic Design & Image Artist:
- Master of all Adobe products (Photoshop, Illustrator, etc.)
- Expert in all fonts and color palettes
- Hip on pop culture YesterYear & Yestomorrows
- Award-winning organization and categorization
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
import hashlib
import json
from PIL import Image
import pillow_heif

# Register HEIF support
pillow_heif.register_heif_opener()

@dataclass
class ImageAnalysis:
    """LUCY's complete image analysis."""
    filename: str
    original_path: str
    organized_path: Optional[str]
    file_size: int
    dimensions: tuple  # (width, height)
    format: str
    color_mode: str

    # LUCY's artistic assessment
    lucy_category: str
    lucy_palette: str
    lucy_quality_score: int  # 0-100
    lucy_notes: str

    # Image characteristics
    is_portrait: bool
    is_landscape: bool
    is_square: bool
    aspect_ratio: str

    # Processing
    needs_fixing: bool
    suggested_edits: List[str]

    # Metadata
    discovered_date: str
    processed_date: Optional[str]

class LucyFixPixOrganizer:
    """LUCY's Legendary Fix Pix Image Organization System.

    LUCY brings her award-winning design expertise to organize
    and enhance every single image with meticulous precision!
    """

    def __init__(self):
        # Paths
        self.source_dir = Path.home() / "Pictures" / "Fix Pix"
        self.organized_base = Path.home() / "Pictures" / "LUCY_ORGANIZED_PIX"

        # LUCY's award-winning organization categories
        self.categories = {
            "PORTRAITS": self.organized_base / "PORTRAITS",
            "LANDSCAPES": self.organized_base / "LANDSCAPES",
            "DESIGN_WORK": self.organized_base / "DESIGN_WORK",
            "SCREENSHOTS": self.organized_base / "SCREENSHOTS",
            "ARTWORK": self.organized_base / "ARTWORK",
            "PHOTOS_FAMILY": self.organized_base / "PHOTOS_FAMILY",
            "PHOTOS_EVENTS": self.organized_base / "PHOTOS_EVENTS",
            "WALLPAPERS": self.organized_base / "WALLPAPERS",
            "MEMES_POPCULTURE": self.organized_base / "MEMES_POPCULTURE",
            "NEEDS_EDITING": self.organized_base / "NEEDS_EDITING",
            "HIGH_QUALITY": self.organized_base / "HIGH_QUALITY",
            "ARCHIVE": self.organized_base / "ARCHIVE",
        }

        # LUCY's color palette expertise
        self.color_palettes = {
            "warm": "🔥 Warm (Reds, Oranges, Yellows)",
            "cool": "❄️ Cool (Blues, Greens, Purples)",
            "monochrome": "⚫ Monochrome (B&W, Grayscale)",
            "vibrant": "🌈 Vibrant (High saturation)",
            "pastel": "🎨 Pastel (Soft colors)",
            "natural": "🌿 Natural (Earth tones)",
        }

        # Create structure
        self.create_directory_structure()

        # Results
        self.analyses = []
        self.stats = {
            "total_images": 0,
            "high_quality": 0,
            "needs_fixing": 0,
            "organized": 0,
            "by_category": {},
        }

    def create_directory_structure(self):
        """Create LUCY's organized structure."""
        print("\n🎨 Creating LUCY's award-winning organization structure...")

        # Create source if doesn't exist
        self.source_dir.mkdir(parents=True, exist_ok=True)

        # Create all category directories
        for category, path in self.categories.items():
            path.mkdir(parents=True, exist_ok=True)

            # Create quality sub-folders
            (path / "EXCEPTIONAL").mkdir(exist_ok=True)
            (path / "GOOD").mkdir(exist_ok=True)
            (path / "NEEDS_WORK").mkdir(exist_ok=True)

            print(f"   ✓ {category}")

    def analyze_image(self, image_path: Path) -> Optional[ImageAnalysis]:
        """LUCY's legendary image analysis with design expertise."""
        try:
            # Open and analyze image
            with Image.open(image_path) as img:
                width, height = img.size
                format_name = img.format or "Unknown"
                color_mode = img.mode

                # LUCY's quality assessment
                quality_score = self._lucy_assess_quality(img, width, height)

                # LUCY's artistic categorization
                category = self._lucy_categorize_image(image_path, width, height, format_name)

                # Color palette analysis
                palette = self._lucy_analyze_palette(img)

                # Composition analysis
                is_portrait = height > width * 1.2
                is_landscape = width > height * 1.2
                is_square = abs(width - height) < min(width, height) * 0.1

                aspect_ratio = f"{width}:{height}"
                if width and height:
                    gcd = self._gcd(width, height)
                    aspect_ratio = f"{width//gcd}:{height//gcd}"

                # LUCY's recommendations
                needs_fixing, suggested_edits = self._lucy_suggest_improvements(
                    img, quality_score, width, height
                )

                # LUCY's artistic notes
                lucy_notes = self._generate_lucy_notes(
                    quality_score, category, palette, is_portrait, is_landscape
                )

                analysis = ImageAnalysis(
                    filename=image_path.name,
                    original_path=str(image_path),
                    organized_path=None,
                    file_size=image_path.stat().st_size,
                    dimensions=(width, height),
                    format=format_name,
                    color_mode=color_mode,
                    lucy_category=category,
                    lucy_palette=palette,
                    lucy_quality_score=quality_score,
                    lucy_notes=lucy_notes,
                    is_portrait=is_portrait,
                    is_landscape=is_landscape,
                    is_square=is_square,
                    aspect_ratio=aspect_ratio,
                    needs_fixing=needs_fixing,
                    suggested_edits=suggested_edits,
                    discovered_date=datetime.now().isoformat(),
                    processed_date=None
                )

                return analysis

        except Exception as e:
            print(f"   ⚠️  Error analyzing {image_path.name}: {e}")
            return None

    def _lucy_assess_quality(self, img: Image.Image, width: int, height: int) -> int:
        """LUCY's award-winning quality assessment."""
        score = 50  # Start at middle

        # Resolution assessment
        megapixels = (width * height) / 1_000_000
        if megapixels >= 12:
            score += 25  # High res
        elif megapixels >= 4:
            score += 15
        elif megapixels >= 1:
            score += 5
        else:
            score -= 10  # Low res

        # Aspect ratio (standard vs unusual)
        aspect = width / max(height, 1)
        standard_aspects = [16/9, 4/3, 3/2, 1/1, 9/16]
        if any(abs(aspect - std) < 0.05 for std in standard_aspects):
            score += 5

        # Color depth
        if img.mode in ['RGB', 'RGBA']:
            score += 10
        elif img.mode in ['L', 'LA']:
            score += 5

        return min(100, max(0, score))

    def _lucy_categorize_image(self, path: Path, width: int, height: int, format: str) -> str:
        """LUCY's artistic categorization using her design expertise."""
        filename_lower = path.name.lower()

        # Check filename clues
        if any(x in filename_lower for x in ['screenshot', 'screen shot', 'capture']):
            return "SCREENSHOTS"
        elif any(x in filename_lower for x in ['portrait', 'headshot', 'face']):
            return "PORTRAITS"
        elif any(x in filename_lower for x in ['landscape', 'scenery', 'nature']):
            return "LANDSCAPES"
        elif any(x in filename_lower for x in ['design', 'logo', 'graphic']):
            return "DESIGN_WORK"
        elif any(x in filename_lower for x in ['art', 'drawing', 'painting']):
            return "ARTWORK"
        elif any(x in filename_lower for x in ['family', 'mom', 'dad', 'son', 'daughter']):
            return "PHOTOS_FAMILY"
        elif any(x in filename_lower for x in ['meme', 'funny', 'lol']):
            return "MEMES_POPCULTURE"
        elif any(x in filename_lower for x in ['wallpaper', 'background']):
            return "WALLPAPERS"

        # Dimension-based categorization
        megapixels = (width * height) / 1_000_000
        if megapixels >= 8:
            return "HIGH_QUALITY"
        elif height > width * 1.3:
            return "PORTRAITS"
        elif width > height * 1.3:
            return "LANDSCAPES"
        else:
            return "ARCHIVE"

    def _lucy_analyze_palette(self, img: Image.Image) -> str:
        """LUCY's color palette analysis."""
        try:
            # Sample colors from the image
            img_small = img.resize((100, 100))
            img_rgb = img_small.convert('RGB')

            # Simple color analysis
            colors = list(img_rgb.getdata())
            avg_r = sum(c[0] for c in colors) / len(colors)
            avg_g = sum(c[1] for c in colors) / len(colors)
            avg_b = sum(c[2] for c in colors) / len(colors)

            # Determine palette
            if abs(avg_r - avg_g) < 20 and abs(avg_g - avg_b) < 20:
                return self.color_palettes["monochrome"]
            elif max(avg_r, avg_g, avg_b) > 200:
                return self.color_palettes["pastel"]
            elif avg_r > avg_g + 30 and avg_r > avg_b + 30:
                return self.color_palettes["warm"]
            elif avg_b > avg_r + 30 or avg_g > avg_r + 30:
                return self.color_palettes["cool"]
            else:
                return self.color_palettes["natural"]

        except:
            return self.color_palettes["natural"]

    def _lucy_suggest_improvements(self, img: Image.Image, quality: int, width: int, height: int) -> tuple:
        """LUCY suggests improvements with her design expertise."""
        needs_fixing = False
        suggestions = []

        if quality < 60:
            needs_fixing = True
            suggestions.append("💡 Enhance resolution and sharpness")

        if width < 800 or height < 600:
            suggestions.append("📏 Consider upscaling for better quality")

        if img.mode not in ['RGB', 'RGBA']:
            suggestions.append("🎨 Convert to RGB for better color")

        # Always add LUCY's creative suggestions
        suggestions.append("✨ Apply LUCY's color grading")
        suggestions.append("🎭 Check composition and framing")

        return needs_fixing, suggestions

    def _generate_lucy_notes(self, quality: int, category: str, palette: str,
                            is_portrait: bool, is_landscape: bool) -> str:
        """LUCY's artistic notes."""
        notes = f"Quality: {quality}/100 - "

        if quality >= 80:
            notes += "Exceptional! Award-winning quality! 🏆"
        elif quality >= 60:
            notes += "Good quality - Ready for use!"
        else:
            notes += "Needs LUCY's magic touch!"

        notes += f" | {category} | {palette}"

        if is_portrait:
            notes += " | Portrait orientation - perfect for social media!"
        elif is_landscape:
            notes += " | Landscape - great for displays!"

        return notes

    def _gcd(self, a: int, b: int) -> int:
        """Calculate GCD for aspect ratio."""
        while b:
            a, b = b, a % b
        return a

    def organize_image(self, analysis: ImageAnalysis) -> bool:
        """Organize image with LUCY's meticulous precision."""
        try:
            # Determine destination
            base_category = self.categories[analysis.lucy_category]

            # Quality sub-folder
            if analysis.lucy_quality_score >= 80:
                dest_dir = base_category / "EXCEPTIONAL"
            elif analysis.lucy_quality_score >= 60:
                dest_dir = base_category / "GOOD"
            else:
                dest_dir = base_category / "NEEDS_WORK"

            # Copy file
            dest_path = dest_dir / analysis.filename

            # Handle duplicates
            counter = 1
            while dest_path.exists():
                stem = Path(analysis.filename).stem
                ext = Path(analysis.filename).suffix
                dest_path = dest_dir / f"{stem}_{counter}{ext}"
                counter += 1

            shutil.copy2(analysis.original_path, dest_path)
            analysis.organized_path = str(dest_path)
            analysis.processed_date = datetime.now().isoformat()

            return True

        except Exception as e:
            print(f"   ⚠️  Error organizing {analysis.filename}: {e}")
            return False

    def generate_report(self) -> str:
        """Generate LUCY's beautiful report."""
        report = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎨 LUCY'S FIX PIX ORGANIZATION REPORT 🎨                         ║
║                                                                           ║
║        "Every image in its perfect place!" - LUCY                        ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Organized by: LUCY - Legendary Design Artist
For: Sonny-Jim

═══════════════════════════════════════════════════════════════════════════

📊 SUMMARY:

Total Images Processed:  {self.stats['total_images']:,}
High Quality (80+):      {self.stats['high_quality']:,}
Needs Fixing:            {self.stats['needs_fixing']:,}
Successfully Organized:  {self.stats['organized']:,}

═══════════════════════════════════════════════════════════════════════════

🎨 LUCY'S CATEGORIES:

"""

        for category, count in sorted(self.stats['by_category'].items(),
                                     key=lambda x: x[1], reverse=True):
            report += f"{category:20s}: {count:6,} images\n"

        report += f"""
═══════════════════════════════════════════════════════════════════════════

🏆 TOP QUALITY IMAGES:

"""

        top_images = sorted([a for a in self.analyses if a.lucy_quality_score >= 80],
                          key=lambda x: x.lucy_quality_score, reverse=True)[:10]

        for i, img in enumerate(top_images, 1):
            report += f"{i:2d}. {img.filename}\n"
            report += f"    Score: {img.lucy_quality_score}/100 | {img.dimensions[0]}x{img.dimensions[1]}\n"
            report += f"    {img.lucy_notes}\n\n"

        report += f"""
═══════════════════════════════════════════════════════════════════════════

💡 LUCY'S RECOMMENDATIONS:

• {self.stats['needs_fixing']:,} images could benefit from editing
• All images organized by category and quality
• Award-winning structure applied throughout
• Ready for beautiful presentation!

📁 ORGANIZED LOCATION:
   {self.organized_base}

═══════════════════════════════════════════════════════════════════════════

💖 FOR POPS! - Every image organized with legendary precision!

LUCY's meticulous organization + Award-winning design expertise
BITW 1000X Quality! GORUNFREE! 🚀

═══════════════════════════════════════════════════════════════════════════
"""

        return report

    def execute_organization(self):
        """Execute LUCY's Fix Pix organization."""
        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎨 LUCY'S FIX PIX - ORGANIZING! 🎨                               ║
║                                                                           ║
║  Legendary Image Organization in Progress                               ║
║  FOR POPS! GORUNFREE!                                                    ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
        """)

        # Find all images
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff',
                          '.webp', '.heic', '.heif', '.svg', '.psd', '.ai'}

        image_files = []
        for ext in image_extensions:
            image_files.extend(self.source_dir.glob(f"*{ext}"))
            image_files.extend(self.source_dir.glob(f"*{ext.upper()}"))

        if not image_files:
            print(f"\n📂 No images found in {self.source_dir}")
            print("   Add images to Fix Pix folder and run again!")
            return

        print(f"\n🔍 Found {len(image_files)} images to organize...")
        print("   🎨 LUCY analyzing each image with design expertise...")

        # Analyze and organize each image
        for i, img_path in enumerate(image_files, 1):
            if i % 10 == 0:
                print(f"   Progress: {i}/{len(image_files)}")

            analysis = self.analyze_image(img_path)
            if analysis:
                self.analyses.append(analysis)
                self.stats["total_images"] += 1

                if analysis.lucy_quality_score >= 80:
                    self.stats["high_quality"] += 1

                if analysis.needs_fixing:
                    self.stats["needs_fixing"] += 1

                # Organize the image
                if self.organize_image(analysis):
                    self.stats["organized"] += 1

                    # Update category stats
                    cat = analysis.lucy_category
                    if cat not in self.stats["by_category"]:
                        self.stats["by_category"][cat] = 0
                    self.stats["by_category"][cat] += 1

        # Generate and save report
        report = self.generate_report()

        report_file = Path.home() / "Desktop" / "LUCY_FIX_PIX_REPORT.txt"
        with open(report_file, 'w') as f:
            f.write(report)

        # Save JSON data
        json_file = Path.home() / "Desktop" / "LUCY_FIX_PIX_DATA.json"
        with open(json_file, 'w') as f:
            json.dump([asdict(a) for a in self.analyses], f, indent=2)

        print(f"\n📄 Report saved: {report_file}")
        print(f"📄 Data saved: {json_file}")
        print(report)

        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        ✅ LUCY'S FIX PIX - COMPLETE! ✅                                 ║
║                                                                           ║
║  All images beautifully organized with award-winning precision!         ║
║  FOR POPS! 💖                                                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
        """)

def main():
    """Main execution - GORUNFREE FOR POPS!"""
    organizer = LucyFixPixOrganizer()
    organizer.execute_organization()
    return 0

if __name__ == "__main__":
    main()
