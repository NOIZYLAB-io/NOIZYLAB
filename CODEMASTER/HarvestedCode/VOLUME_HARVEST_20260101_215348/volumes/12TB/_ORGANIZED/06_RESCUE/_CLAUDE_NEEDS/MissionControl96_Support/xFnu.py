#!/usr/bin/env python3
"""
NOIZYGENIE Ultimate Library Organization System
Find the perfect home for every library in the Desktop Lab
"""

import os
import shutil
import json
from pathlib import Path
from collections import defaultdict, Counter
import time
from datetime import datetime
import re
import sys
sys.path.append('/Users/rsp_ms')
from palatino_terminal import PalatinoTerminal

class UltimateLibraryOrganizer:
    def __init__(self):
        self.pt = PalatinoTerminal()
        self.kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
        self.reports_dir = self.kontakt_lab / "REPORTS"
        
        # Create comprehensive organization structure
        self.organization_map = {
            # GENRE-BASED ORGANIZATION
            "ELECTRONIC": {
                "path": "01_ELECTRONIC",
                "keywords": ["electronic", "techno", "house", "trance", "ambient", "electro", "synth", "edm", "dance"],
                "subcategories": {
                    "BASS": ["bass", "sub", "wobble", "808"],
                    "LEADS": ["lead", "melody", "solo", "riff"],
                    "PADS": ["pad", "string", "choir", "atmosphere", "texture"],
                    "DRUMS": ["drum", "beat", "percussion", "rhythm", "kick", "snare", "hihat"],
                    "FX": ["fx", "effect", "sweep", "riser", "impact", "transition"],
                    "ARPEGGIOS": ["arp", "sequence", "pattern", "gate"]
                }
            },
            
            "ORCHESTRAL": {
                "path": "02_ORCHESTRAL",
                "keywords": ["orchestra", "classical", "string", "brass", "woodwind", "symphony", "cinematic"],
                "subcategories": {
                    "STRINGS": ["violin", "viola", "cello", "contrabass", "string", "bow"],
                    "BRASS": ["trumpet", "trombone", "french horn", "tuba", "brass"],
                    "WOODWINDS": ["flute", "clarinet", "oboe", "bassoon", "sax", "woodwind"],
                    "PERCUSSION": ["timpani", "orchestral percussion", "cymbal", "gong"],
                    "CHOIR": ["choir", "vocal", "voice", "soprano", "alto", "tenor", "bass"],
                    "ENSEMBLES": ["ensemble", "section", "full orchestra"]
                }
            },
            
            "ACOUSTIC": {
                "path": "03_ACOUSTIC",
                "keywords": ["acoustic", "guitar", "piano", "organ", "real", "recorded", "live"],
                "subcategories": {
                    "PIANO": ["piano", "grand", "upright", "electric piano", "ep", "rhodes", "wurly"],
                    "GUITAR": ["guitar", "acoustic guitar", "fingerpicked", "strum", "classical guitar"],
                    "ORGAN": ["organ", "hammond", "church", "pipe"],
                    "ETHNIC": ["ethnic", "world", "traditional", "folk", "sitar", "tabla", "didgeridoo"],
                    "MALLETS": ["mallet", "vibraphone", "marimba", "xylophone", "bells", "chime"],
                    "PLUCKED": ["harp", "mandolin", "banjo", "dulcimer", "zither"]
                }
            },
            
            "URBAN": {
                "path": "04_URBAN",
                "keywords": ["hip hop", "rap", "trap", "rnb", "soul", "funk", "urban", "street"],
                "subcategories": {
                    "DRUMS": ["trap", "boom bap", "drill", "beat", "break"],
                    "BASS": ["808", "sub bass", "funk bass", "slap"],
                    "KEYS": ["rhodes", "keys", "chord", "stab"],
                    "VOCAL": ["vocal", "chop", "sample", "acapella", "hook"],
                    "BRASS": ["horn", "stab", "section", "trumpet"],
                    "GUITAR": ["funk guitar", "rhythm", "clean"]
                }
            },
            
            "ROCK_POP": {
                "path": "05_ROCK_POP",
                "keywords": ["rock", "pop", "alternative", "indie", "punk", "metal"],
                "subcategories": {
                    "GUITAR": ["electric guitar", "distortion", "clean", "power chord", "riff"],
                    "BASS": ["bass guitar", "pick", "finger", "fretless"],
                    "DRUMS": ["rock drums", "live drums", "acoustic drums"],
                    "KEYS": ["organ", "piano", "synth"],
                    "VOCAL": ["vocal", "harmony", "choir"],
                    "EFFECTS": ["amp", "pedal", "reverb", "delay"]
                }
            },
            
            "WORLD_ETHNIC": {
                "path": "06_WORLD_ETHNIC",
                "keywords": ["world", "ethnic", "traditional", "folk", "cultural", "native"],
                "subcategories": {
                    "ASIAN": ["asian", "chinese", "japanese", "indian", "gamelan", "koto", "sitar"],
                    "AFRICAN": ["african", "djembe", "kalimba", "talking drum"],
                    "MIDDLE_EASTERN": ["middle eastern", "oud", "qanun", "tabla", "darbuka"],
                    "LATIN": ["latin", "flamenco", "mariachi", "samba", "bossa"],
                    "EUROPEAN": ["irish", "scottish", "celtic", "accordion", "bagpipe"],
                    "NATIVE": ["native american", "flute", "drum", "chant"]
                }
            },
            
            # INSTRUMENT-BASED ORGANIZATION
            "SYNTHESIZERS": {
                "path": "07_SYNTHESIZERS",
                "keywords": ["synth", "analog", "digital", "fm", "wavetable", "virtual analog"],
                "subcategories": {
                    "ANALOG": ["analog", "moog", "minimoog", "oberheim", "prophet"],
                    "DIGITAL": ["digital", "fm", "dx7", "operator"],
                    "WAVETABLE": ["wavetable", "wave", "ppu", "serum style"],
                    "VINTAGE": ["vintage", "retro", "classic", "80s"],
                    "MODERN": ["modern", "contemporary", "cutting edge"],
                    "MODULAR": ["modular", "eurorack", "cv", "patched"]
                }
            },
            
            "DRUMS_PERCUSSION": {
                "path": "08_DRUMS_PERCUSSION",
                "keywords": ["drum", "percussion", "beat", "rhythm", "kit"],
                "subcategories": {
                    "ACOUSTIC_KITS": ["acoustic", "live", "recorded", "studio"],
                    "ELECTRONIC": ["electronic", "machine", "programmable", "synthetic"],
                    "ETHNIC_PERC": ["ethnic", "hand drum", "frame drum", "talking drum"],
                    "ORCHESTRAL": ["timpani", "orchestral", "concert", "classical"],
                    "LOOPS": ["loop", "break", "groove", "pattern"],
                    "ONE_SHOTS": ["one shot", "single", "hit", "sample"]
                }
            },
            
            # SPECIAL CATEGORIES
            "LOOPS_GROOVES": {
                "path": "09_LOOPS_GROOVES",
                "keywords": ["loop", "groove", "pattern", "sequence", "break", "phrase"],
                "subcategories": {
                    "DRUM_LOOPS": ["drum loop", "beat", "break", "groove"],
                    "BASS_LOOPS": ["bass loop", "bassline", "groove"],
                    "MELODIC": ["melodic", "melody", "phrase", "riff"],
                    "CHORD": ["chord", "progression", "harmony"],
                    "RHYTHMIC": ["rhythmic", "percussion", "shaker", "tambourine"],
                    "FULL_MIX": ["full", "mix", "construction", "stem"]
                }
            },
            
            "SOUNDSCAPES_FX": {
                "path": "10_SOUNDSCAPES_FX",
                "keywords": ["soundscape", "ambient", "texture", "fx", "effect", "sound design"],
                "subcategories": {
                    "AMBIENT": ["ambient", "drone", "pad", "wash"],
                    "RISERS": ["riser", "sweep", "build", "crescendo"],
                    "IMPACTS": ["impact", "hit", "slam", "crash"],
                    "TRANSITIONS": ["transition", "whoosh", "swipe", "pass"],
                    "TEXTURES": ["texture", "grain", "noise", "static"],
                    "ATMOSPHERES": ["atmosphere", "space", "room", "environment"]
                }
            },
            
            "VOCALS": {
                "path": "11_VOCALS",
                "keywords": ["vocal", "voice", "sing", "choir", "spoken", "chant"],
                "subcategories": {
                    "LEAD_VOCALS": ["lead", "solo", "main", "melody"],
                    "BACKING": ["backing", "harmony", "support", "bg"],
                    "CHOIR": ["choir", "ensemble", "group", "mass"],
                    "SPOKEN": ["spoken", "talk", "speech", "narration"],
                    "PROCESSED": ["processed", "vocoder", "auto tune", "effect"],
                    "ETHNIC": ["ethnic", "traditional", "chant", "ritual"]
                }
            },
            
            # TECHNICAL CATEGORIES
            "CONSTRUCTION_KITS": {
                "path": "12_CONSTRUCTION_KITS",
                "keywords": ["construction", "kit", "stems", "multitrack", "project"],
                "subcategories": {
                    "ELECTRONIC": ["electronic", "edm", "house", "techno"],
                    "HIP_HOP": ["hip hop", "trap", "boom bap"],
                    "ROCK": ["rock", "band", "live"],
                    "POP": ["pop", "commercial", "radio"],
                    "CINEMATIC": ["cinematic", "film", "score", "trailer"],
                    "WORLD": ["world", "ethnic", "fusion"]
                }
            },
            
            "MULTIS_COMBIS": {
                "path": "13_MULTIS_COMBIS",
                "keywords": ["multi", "combi", "combination", "layer", "split", "performance"],
                "subcategories": {
                    "LAYERED": ["layer", "stack", "thick", "fat"],
                    "SPLIT": ["split", "zone", "keyboard"],
                    "PERFORMANCE": ["performance", "live", "gig", "stage"],
                    "COMPLEX": ["complex", "evolving", "modulated"],
                    "SIMPLE": ["simple", "basic", "clean"],
                    "SPECIALTY": ["specialty", "unique", "custom"]
                }
            }
        }
        
        # Statistics tracking
        self.stats = {
            'libraries_analyzed': 0,
            'libraries_moved': 0,
            'perfect_matches': 0,
            'good_matches': 0,
            'generic_matches': 0,
            'unmatched': 0,
            'subcategories_created': 0
        }
    
    def analyze_library_content(self, library_path):
        """Deep analysis of library content to determine best categorization"""
        analysis = {
            'name': library_path.name,
            'path': library_path,
            'keywords_found': set(),
            'file_analysis': {},
            'structure_analysis': {},
            'content_confidence': 0
        }
        
        # Analyze library name
        name_lower = library_path.name.lower()
        name_words = re.findall(r'\b\w+\b', name_lower)
        analysis['name_words'] = name_words
        
        # Analyze directory structure
        subdirs = [d.name.lower() for d in library_path.iterdir() if d.is_dir()]
        analysis['subdirectories'] = subdirs
        
        # Analyze file types and names
        file_types = {'.nki': 0, '.nkm': 0, '.nkc': 0, '.ncw': 0, '.wav': 0, '.aiff': 0}
        sample_files = []
        instrument_files = []
        
        for file_path in library_path.rglob("*"):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                if ext in file_types:
                    file_types[ext] += 1
                    
                    if ext in ['.nki', '.nkm', '.nkc']:
                        instrument_files.append(file_path.name.lower())
                    elif ext in ['.ncw', '.wav', '.aiff']:
                        sample_files.append(file_path.name.lower())
        
        analysis['file_analysis'] = file_types
        analysis['total_instruments'] = file_types['.nki'] + file_types['.nkm'] + file_types['.nkc']
        analysis['total_samples'] = file_types['.ncw'] + file_types['.wav'] + file_types['.aiff']
        
        # Extract keywords from file names
        all_filenames = instrument_files + sample_files
        filename_text = ' '.join(all_filenames)
        filename_words = re.findall(r'\b\w{3,}\b', filename_text)
        analysis['filename_words'] = list(set(filename_words))
        
        return analysis
    
    def find_best_category(self, library_analysis):
        """Find the best category match for a library"""
        best_matches = []
        
        # Get all text to analyze
        search_text = (
            library_analysis['name'].lower() + ' ' +
            ' '.join(library_analysis['name_words']) + ' ' +
            ' '.join(library_analysis['subdirectories']) + ' ' +
            ' '.join(library_analysis['filename_words'][:50])  # Limit to prevent overflow
        )
        
        # Score each category
        for category_name, category_info in self.organization_map.items():
            score = 0
            matched_keywords = []
            matched_subcategory = None
            subcategory_score = 0
            
            # Check main category keywords
            for keyword in category_info['keywords']:
                if keyword in search_text:
                    score += 10
                    matched_keywords.append(keyword)
            
            # Check subcategory keywords for better placement
            for subcat_name, subcat_keywords in category_info['subcategories'].items():
                subcat_match_score = 0
                subcat_matches = []
                
                for keyword in subcat_keywords:
                    if keyword in search_text:
                        subcat_match_score += 15  # Higher score for subcategory matches
                        subcat_matches.append(keyword)
                
                if subcat_match_score > subcategory_score:
                    subcategory_score = subcat_match_score
                    matched_subcategory = subcat_name
            
            total_score = score + subcategory_score
            
            if total_score > 0:
                best_matches.append({
                    'category': category_name,
                    'subcategory': matched_subcategory,
                    'score': total_score,
                    'keywords': matched_keywords,
                    'confidence': min(total_score / 20, 1.0)  # Normalize to 0-1
                })
        
        # Sort by score
        best_matches.sort(key=lambda x: x['score'], reverse=True)
        
        return best_matches[0] if best_matches else None
    
    def create_organization_structure(self):
        """Create the complete organization directory structure"""
        self.pt.subheader("Creating Master Organization Structure")
        
        for category_name, category_info in self.organization_map.items():
            # Create main category directory
            main_dir = self.kontakt_lab / category_info['path']
            main_dir.mkdir(exist_ok=True, parents=True)
            
            # Create subcategory directories
            for subcat_name in category_info['subcategories'].keys():
                subcat_dir = main_dir / subcat_name
                subcat_dir.mkdir(exist_ok=True)
                self.stats['subcategories_created'] += 1
            
            print(f"   📁 {category_name}: {len(category_info['subcategories'])} subcategories")
        
        self.pt.success(f"Organization structure created: {len(self.organization_map)} categories")
    
    def move_library_to_home(self, library_analysis, category_match):
        """Move library to its perfect home"""
        source_path = library_analysis['path']
        category_info = self.organization_map[category_match['category']]
        
        # Determine target directory
        main_category_dir = self.kontakt_lab / category_info['path']
        
        if category_match['subcategory']:
            target_dir = main_category_dir / category_match['subcategory'] / source_path.name
        else:
            target_dir = main_category_dir / source_path.name
        
        # Ensure target directory doesn't already exist
        counter = 1
        original_target = target_dir
        while target_dir.exists():
            target_dir = original_target.parent / f"{original_target.name}_{counter:02d}"
            counter += 1
        
        try:
            # Move the library
            shutil.move(str(source_path), str(target_dir))
            self.stats['libraries_moved'] += 1
            
            # Update confidence stats
            if category_match['confidence'] >= 0.8:
                self.stats['perfect_matches'] += 1
                confidence_level = "🎯 PERFECT"
            elif category_match['confidence'] >= 0.5:
                self.stats['good_matches'] += 1
                confidence_level = "✅ GOOD"
            else:
                self.stats['generic_matches'] += 1
                confidence_level = "📁 GENERIC"
            
            return target_dir, confidence_level
            
        except Exception as e:
            print(f"      ❌ Error moving {source_path.name}: {e}")
            return None, "ERROR"
    
    def create_organization_report(self):
        """Create comprehensive organization report"""
        report_file = self.reports_dir / f"ORGANIZATION_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_file, 'w') as f:
            f.write("🎹 NOIZYGENIE Ultimate Library Organization Report\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("📊 ORGANIZATION STATISTICS:\n")
            f.write(f"   Libraries Analyzed: {self.stats['libraries_analyzed']}\n")
            f.write(f"   Libraries Moved: {self.stats['libraries_moved']}\n")
            f.write(f"   Perfect Matches: {self.stats['perfect_matches']}\n")
            f.write(f"   Good Matches: {self.stats['good_matches']}\n")
            f.write(f"   Generic Matches: {self.stats['generic_matches']}\n")
            f.write(f"   Unmatched: {self.stats['unmatched']}\n")
            f.write(f"   Subcategories Created: {self.stats['subcategories_created']}\n\n")
            
            f.write("📁 ORGANIZATION STRUCTURE:\n")
            for category_name, category_info in self.organization_map.items():
                f.write(f"\n{category_name} ({category_info['path']}):\n")
                for subcat in category_info['subcategories'].keys():
                    f.write(f"   - {subcat}\n")
        
        self.pt.success(f"Organization report saved: {report_file.name}")
    
    def run_ultimate_organization(self):
        """Execute the ultimate library organization"""
        start_time = time.time()
        
        self.pt.header("NOIZYGENIE Ultimate Library Organization System")
        self.pt.info("Mission", "Find the perfect home for every library")
        self.pt.info("Categories", f"{len(self.organization_map)} main categories")
        self.pt.info("Subcategories", f"{sum(len(cat['subcategories']) for cat in self.organization_map.values())}")
        self.pt.info("Started", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        # Step 1: Create organization structure
        self.create_organization_structure()
        
        # Step 2: Analyze all libraries
        self.pt.section_break()
        self.pt.subheader("Analyzing All Libraries for Perfect Placement")
        
        # Get all libraries (exclude organization directories and system folders)
        all_libraries = []
        exclude_dirs = {
            'REPORTS', '6TB_ARCHIVE', 'ORGANIZED_LIBRARIES', 'SAMPLE_ARCHIVES', 
            'BACKUP', 'TEMP_PROCESSING'
        }
        
        # Add organization directories to exclude list
        for category_info in self.organization_map.values():
            exclude_dirs.add(category_info['path'])
        
        for item in self.kontakt_lab.iterdir():
            if (item.is_dir() and 
                not item.name.startswith('.') and 
                item.name not in exclude_dirs):
                all_libraries.append(item)
        
        self.pt.info("Libraries to organize", f"{len(all_libraries):,}")
        
        # Step 3: Process each library
        organized_count = 0
        for i, library_path in enumerate(all_libraries, 1):
            print(f"\n📦 Analyzing {i:3d}/{len(all_libraries)}: {library_path.name}")
            
            # Analyze library content
            library_analysis = self.analyze_library_content(library_path)
            self.stats['libraries_analyzed'] += 1
            
            # Find best category match
            category_match = self.find_best_category(library_analysis)
            
            if category_match:
                print(f"   🎯 Best match: {category_match['category']}")
                if category_match['subcategory']:
                    print(f"      📂 Subcategory: {category_match['subcategory']}")
                print(f"      🎲 Confidence: {category_match['confidence']:.1%}")
                
                # Move library to its home
                new_location, confidence_level = self.move_library_to_home(library_analysis, category_match)
                
                if new_location:
                    print(f"      {confidence_level} → {new_location.relative_to(self.kontakt_lab)}")
                    organized_count += 1
                else:
                    print(f"      ❌ Failed to move")
            else:
                print(f"   ❓ No clear category match found")
                self.stats['unmatched'] += 1
            
            # Progress indicator
            if i % 20 == 0:
                print(f"      ⏸️  Progress checkpoint: {i}/{len(all_libraries)} libraries processed...")
        
        # Step 4: Generate final report
        self.pt.section_break()
        self.pt.complete("ULTIMATE ORGANIZATION COMPLETE!")
        
        elapsed_time = time.time() - start_time
        
        self.pt.info("Total Libraries", f"{len(all_libraries):,}")
        self.pt.info("Successfully Organized", f"{organized_count:,}")
        self.pt.info("Perfect Matches", f"{self.stats['perfect_matches']}")
        self.pt.info("Good Matches", f"{self.stats['good_matches']}")
        self.pt.info("Generic Matches", f"{self.stats['generic_matches']}")
        self.pt.info("Processing Time", f"{elapsed_time/60:.1f} minutes")
        
        # Create comprehensive report
        self.create_organization_report()
        
        # Update HTML masterlist
        print(f"\n📊 Updating HTML masterlist with new organization...")
        os.system("python3 ~/auto_scan.py")
        
        self.pt.section_break()
        self.pt.success("🎹 Every library now has a perfect home in the NOIZYGENIE Arsenal! 🎹")
        self.pt.timestamp()

if __name__ == "__main__":
    try:
        organizer = UltimateLibraryOrganizer()
        organizer.run_ultimate_organization()
    except KeyboardInterrupt:
        print("\n⏹️  Ultimate organization cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()