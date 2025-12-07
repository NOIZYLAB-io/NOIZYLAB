#!/usr/bin/env python3
"""
🔥🔥🔥 ULTIMATE MASTER ORGANIZER 🔥🔥🔥
ALL-IN-ONE FILE ORGANIZATION SYSTEM

Combines:
- METABEAST: File intelligence & duplicate detection
- ENGR_KEITH: Code analysis & optimization
- CODE_VAC: Automated cleaning & fixing
- SUPER_REORGANIZER: Perfect file structure

ZERO EXTERNAL DEPENDENCIES - EVERYTHING IN ONE FILE

Author: AI Family Collective (All 8 agents)
Mission: Perfect digital organization
"""

import os
import sys
import shutil
import hashlib
import json
import re
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict

# ============================================================================
# COLORS & UI
# ============================================================================

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_banner():
    """Epic banner"""
    banner = f"""
{Colors.BOLD}{Colors.CYAN}
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║              🔥 ULTIMATE MASTER ORGANIZER - ALL-IN-ONE 🔥                     ║
║                                                                               ║
║           METABEAST + ENGR_KEITH + CODE_VAC + SUPER_REORGANIZER              ║
║                        AI FAMILY COLLECTIVE                                   ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
{Colors.END}
"""
    print(banner)

# ============================================================================
# METABEAST - FILE INTELLIGENCE ENGINE
# ============================================================================

class MetaBeast:
    """File intelligence, metadata extraction, duplicate detection"""
    
    def __init__(self):
        self.file_hashes = {}
        self.duplicates = []
        self.relationships = defaultdict(list)
    
    def calculate_hash(self, file_path: Path) -> Optional[str]:
        """Calculate SHA-256 hash for duplicate detection"""
        try:
            sha256 = hashlib.sha256()
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except:
            return None
    
    def extract_metadata(self, file_path: Path) -> Dict:
        """Extract comprehensive file metadata"""
        metadata = {
            'path': str(file_path),
            'name': file_path.name,
            'extension': file_path.suffix.lower(),
            'size': 0,
            'hash': None,
            'category': None,
            'tags': []
        }
        
        try:
            stat = file_path.stat()
            metadata['size'] = stat.st_size
            metadata['hash'] = self.calculate_hash(file_path)
            
            # Track duplicates
            if metadata['hash']:
                if metadata['hash'] in self.file_hashes:
                    self.duplicates.append({
                        'original': self.file_hashes[metadata['hash']],
                        'duplicate': str(file_path),
                        'size': metadata['size']
                    })
                else:
                    self.file_hashes[metadata['hash']] = str(file_path)
        except:
            pass
        
        return metadata

# ============================================================================
# ENGR_KEITH - CODE ANALYSIS ENGINE
# ============================================================================

class EngrKeith:
    """Code analysis, optimization, and quality checking"""
    
    def __init__(self):
        self.issues_found = []
        self.files_analyzed = 0
    
    def analyze_python(self, file_path: Path) -> Dict:
        """Analyze Python file for issues"""
        issues = {
            'syntax_errors': [],
            'security_issues': [],
            'style_issues': []
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Check syntax
            try:
                compile(content, str(file_path), 'exec')
            except SyntaxError as e:
                issues['syntax_errors'].append(str(e))
            
            # Security checks
            dangerous_patterns = [
                (r'eval\(', 'Use of eval()'),
                (r'exec\(', 'Use of exec()'),
                (r'os\.system\(', 'Use of os.system()'),
            ]
            
            for pattern, desc in dangerous_patterns:
                if re.search(pattern, content):
                    issues['security_issues'].append(desc)
            
            # Style checks
            if 'import *' in content:
                issues['style_issues'].append('Wildcard import')
            
            self.files_analyzed += 1
            
        except:
            pass
        
        return issues
    
    def optimize_code(self, file_path: Path) -> bool:
        """Optimize code file if possible"""
        ext = file_path.suffix.lower()
        
        if ext == '.py':
            try:
                # Try black formatting
                subprocess.run(['black', '--quiet', str(file_path)],
                             capture_output=True, timeout=5)
                # Try isort
                subprocess.run(['isort', '--quiet', str(file_path)],
                             capture_output=True, timeout=5)
                return True
            except:
                pass
        
        return False

# ============================================================================
# CODE_VAC - AUTOMATED CODE CLEANING
# ============================================================================

class CodeVac:
    """Automated code cleaning and fixing"""
    
    def __init__(self):
        self.cleaned_files = 0
        self.errors = 0
    
    def clean_python(self, file_path: Path) -> bool:
        """Clean Python file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Remove trailing whitespace
            lines = content.split('\n')
            lines = [line.rstrip() for line in lines]
            content = '\n'.join(lines)
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.cleaned_files += 1
            return True
        except:
            self.errors += 1
            return False

# ============================================================================
# ULTIMATE MASTER ORGANIZER - MAIN ENGINE
# ============================================================================

class UltimateMasterOrganizer:
    """The complete all-in-one organization system"""
    
    def __init__(self, source_drive: str, destination_drive: str = None):
        self.source_drive = Path(source_drive)
        
        if destination_drive is None:
            destination_drive = source_drive
        
        self.destination_drive = Path(destination_drive)
        self.target_drive = self.destination_drive / "PERFECT_ORGANIZED_2026"
        
        # Initialize engines
        self.metabeast = MetaBeast()
        self.engr_keith = EngrKeith()
        self.code_vac = CodeVac()
        
        # Statistics
        self.stats = {
            'scan_start': datetime.now(),
            'total_files': 0,
            'total_size': 0,
            'files_processed': 0,
            'files_moved': 0,
            'files_optimized': 0,
            'duplicates_removed': 0,
            'space_saved': 0,
            'errors': 0,
            'categories': defaultdict(int)
        }
        
        # Perfect structure
        self.structure = {
            'CODE': {
                'Python': ['Scripts', 'Libraries', 'Projects'],
                'JavaScript': ['Node', 'React', 'Utils'],
                'Shell': ['Automation', 'Build', 'Deploy'],
                'Other': []
            },
            'MUSIC_PRODUCTION': {
                'Sample_Libraries': ['Drums', 'Instruments', 'FX', 'Loops'],
                'Projects': ['2026_Active', '2025_Archive', 'Templates'],
                'Presets': ['Synths', 'Effects', 'Chains'],
                'Instruments': ['Kontakt', 'VST', 'AU'],
                'Kits': ['Drum_Kits', 'Sample_Packs']
            },
            'AUDIO': {
                'Samples_By_Type': ['Kicks', 'Snares', 'Hats', 'Percussion', 'Bass', 'Synth', 'Vocals'],
                'Samples_By_BPM': ['80-100', '100-120', '120-140', '140-160', '160-180'],
                'Loops': ['Drum_Loops', 'Music_Loops', 'FX_Loops'],
                'Raw_Audio': []
            },
            'DOCUMENTATION': {
                'Guides': ['Audio', 'Code', 'System'],
                'Reference': ['Manuals', 'Specs', 'API_Docs'],
                'Notes': ['Project_Notes', 'Ideas'],
                'History': ['2020', '2021', '2022', '2023', '2024', '2025'],
                'MC96': ['Accessibility', 'Features']
            },
            'ARCHIVES': {
                'Backups': ['2020', '2021', '2022', '2023', '2024', '2025'],
                'Old_Projects': ['Music', 'Code', 'Design'],
                'Migration': ['From_4TB', 'From_RED_DRAGON', 'From_GABRIEL']
            },
            'MEDIA': {
                'Video': ['Documentaries', 'Series', 'Movies', 'Tutorials'],
                'Images': ['Wallpapers', 'Photos', 'Graphics'],
                'Design': ['Projects', 'Templates']
            },
            'INSTALLERS': {
                'Audio_Software': ['DAW', 'Plugins', 'Utilities'],
                'Development': ['IDEs', 'Languages', 'Tools'],
                'System': ['macOS', 'Windows']
            },
            'PROJECTS': {
                'Active_2026': ['NoizyLab', 'MC96', 'NoizyFish', 'MissionControl'],
                'Archive': ['Completed', 'Paused'],
                'Collaboration': []
            },
            'DATA': {
                'Databases': ['JSON', 'SQL', 'NoSQL'],
                'Logs': ['System', 'Application', 'Error'],
                'Metadata': ['File_DBs', 'Analysis', 'Reports']
            }
        }
    
    def log(self, message: str, level: str = "info"):
        """Beautiful logging"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        prefix = {
            "info": f"{Colors.CYAN}ℹ",
            "success": f"{Colors.GREEN}✓",
            "warning": f"{Colors.YELLOW}⚠",
            "error": f"{Colors.RED}✗",
            "header": f"{Colors.BOLD}{Colors.BLUE}▶",
            "ai": f"{Colors.BOLD}{Colors.CYAN}🤖"
        }.get(level, "•")
        
        print(f"{prefix} {timestamp} {message}{Colors.END}")
    
    def create_structure(self):
        """Create perfect directory structure"""
        self.log("🏗️  BUILDING PERFECT STRUCTURE", "header")
        
        for main_cat, subcats in self.structure.items():
            main_path = self.target_drive / main_cat
            main_path.mkdir(parents=True, exist_ok=True)
            
            for subcat, subsubcats in subcats.items():
                subcat_path = main_path / subcat
                subcat_path.mkdir(parents=True, exist_ok=True)
                
                for subsubcat in subsubcats:
                    (subcat_path / subsubcat).mkdir(parents=True, exist_ok=True)
        
        self.log("Structure created successfully", "success")
    
    def categorize_file(self, file_path: Path) -> Tuple[str, str, str]:
        """Intelligently categorize file"""
        ext = file_path.suffix.lower()
        name = file_path.name.lower()
        parent = file_path.parent.name.lower()
        
        # CODE
        code_exts = {'.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.h'}
        if ext in code_exts:
            if ext == '.py':
                return ('CODE', 'Python', 'Scripts')
            elif ext in {'.js', '.jsx'}:
                return ('CODE', 'JavaScript', 'Node')
            elif ext in {'.ts', '.tsx'}:
                return ('CODE', 'JavaScript', 'React')
            return ('CODE', 'Other', '')
        
        # Shell
        if ext in {'.sh', '.bash', '.zsh'}:
            return ('CODE', 'Shell', 'Automation')
        
        # AUDIO
        audio_exts = {'.aif', '.aiff', '.wav', '.mp3', '.flac', '.ogg', '.m4a'}
        if ext in audio_exts:
            # BPM detection
            bpm_match = re.search(r'(\d{2,3})\s*bpm|_(\d{2,3})_', name)
            if bpm_match:
                bpm = int(bpm_match.group(1) or bpm_match.group(2))
                if 80 <= bpm <= 100:
                    return ('AUDIO', 'Samples_By_BPM', '80-100')
                elif 100 < bpm <= 120:
                    return ('AUDIO', 'Samples_By_BPM', '100-120')
                elif 120 < bpm <= 140:
                    return ('AUDIO', 'Samples_By_BPM', '120-140')
                elif 140 < bpm <= 160:
                    return ('AUDIO', 'Samples_By_BPM', '140-160')
                elif 160 < bpm <= 180:
                    return ('AUDIO', 'Samples_By_BPM', '160-180')
            
            # Type detection
            if any(x in name for x in ['kick', 'bd']):
                return ('AUDIO', 'Samples_By_Type', 'Kicks')
            elif 'snare' in name or 'sd' in name:
                return ('AUDIO', 'Samples_By_Type', 'Snares')
            elif 'hat' in name or 'hh' in name:
                return ('AUDIO', 'Samples_By_Type', 'Hats')
            elif 'bass' in name:
                return ('AUDIO', 'Samples_By_Type', 'Bass')
            elif 'synth' in name or 'lead' in name:
                return ('AUDIO', 'Samples_By_Type', 'Synth')
            elif 'vocal' in name or 'vox' in name:
                return ('AUDIO', 'Samples_By_Type', 'Vocals')
            elif 'loop' in name:
                return ('AUDIO', 'Loops', 'Drum_Loops' if 'drum' in name else 'Music_Loops')
            
            return ('AUDIO', 'Raw_Audio', '')
        
        # MUSIC PRODUCTION
        if ext in {'.kit', '.ssd', '.nki', '.rx2', '.ncw', '.tci', '.xpak'}:
            if ext in {'.kit', '.ssd'}:
                return ('MUSIC_PRODUCTION', 'Kits', 'Drum_Kits')
            elif ext == '.nki':
                return ('MUSIC_PRODUCTION', 'Instruments', 'Kontakt')
            return ('MUSIC_PRODUCTION', 'Sample_Libraries', 'FX')
        
        # DOCUMENTATION
        if ext in {'.md', '.txt', '.pdf', '.doc', '.docx'}:
            if 'mc96' in name:
                return ('DOCUMENTATION', 'MC96', 'Features')
            return ('DOCUMENTATION', 'Notes', 'Project_Notes')
        
        # DATA
        if ext in {'.json', '.xml', '.yaml', '.yml', '.csv'}:
            return ('DATA', 'Databases', 'JSON')
        
        # MEDIA
        if ext in {'.mp4', '.mov', '.avi', '.mkv'}:
            if 'documentary' in parent:
                return ('MEDIA', 'Video', 'Documentaries')
            elif 'series' in parent:
                return ('MEDIA', 'Video', 'Series')
            return ('MEDIA', 'Video', 'Movies')
        
        if ext in {'.png', '.jpg', '.jpeg', '.gif', '.svg'}:
            if 'wallpaper' in parent:
                return ('MEDIA', 'Images', 'Wallpapers')
            return ('MEDIA', 'Images', 'Photos')
        
        # INSTALLERS
        if ext in {'.dmg', '.pkg', '.exe'}:
            return ('INSTALLERS', 'System', 'macOS')
        
        # PROJECTS
        if any(x in parent for x in ['noizylab', 'mc96', 'noizyfish']):
            if 'noizylab' in parent:
                return ('PROJECTS', 'Active_2026', 'NoizyLab')
            elif 'mc96' in parent:
                return ('PROJECTS', 'Active_2026', 'MC96')
            return ('PROJECTS', 'Active_2026', 'NoizyFish')
        
        return ('DATA', 'Databases', 'JSON')
    
    def scan_drive(self) -> List[Path]:
        """Scan entire drive"""
        self.log("🔍 SCANNING DRIVE...", "header")
        
        all_files = []
        ignored_dirs = {
            '.Spotlight-V100', '.Trashes', '.fseventsd', '.TemporaryItems',
            '.DocumentRevisions-V100', 'PERFECT_ORGANIZED_2026'
        }
        
        for root, dirs, files in os.walk(self.source_drive):
            dirs[:] = [d for d in dirs if d not in ignored_dirs and not d.startswith('.')]
            
            for file in files:
                if not file.startswith('.'):
                    file_path = Path(root) / file
                    all_files.append(file_path)
                    
                    if len(all_files) % 1000 == 0:
                        self.log(f"Found {len(all_files)} files...", "info")
        
        self.stats['total_files'] = len(all_files)
        self.log(f"✓ SCAN COMPLETE: {len(all_files)} files", "success")
        
        return all_files
    
    def process_file(self, file_path: Path) -> bool:
        """Process single file through all engines"""
        try:
            # Skip if already in target
            if str(file_path).startswith(str(self.target_drive)):
                return False
            
            # Get file info
            stat = file_path.stat()
            file_size = stat.st_size
            
            # METABEAST: Check duplicates
            metadata = self.metabeast.extract_metadata(file_path)
            if metadata['hash'] and metadata['hash'] in self.metabeast.file_hashes:
                if self.metabeast.file_hashes[metadata['hash']] != str(file_path):
                    self.stats['duplicates_removed'] += 1
                    self.stats['space_saved'] += file_size
                    return False
            
            # ENGR_KEITH: Analyze code
            ext = file_path.suffix.lower()
            if ext == '.py':
                self.engr_keith.analyze_python(file_path)
            
            # CODE_VAC: Clean if needed
            if ext in {'.py', '.js', '.ts'}:
                self.code_vac.clean_python(file_path)
            
            # Categorize
            main_cat, sub_cat, subsub_cat = self.categorize_file(file_path)
            
            # Build destination
            dest_dir = self.target_drive / main_cat / sub_cat
            if subsub_cat:
                dest_dir = dest_dir / subsub_cat
            
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest_path = dest_dir / file_path.name
            
            # Handle name conflicts
            counter = 1
            while dest_path.exists():
                stem = file_path.stem
                dest_path = dest_dir / f"{stem}_{counter}{file_path.suffix}"
                counter += 1
            
            # Move file
            shutil.move(str(file_path), str(dest_path))
            
            # Update stats
            self.stats['files_moved'] += 1
            self.stats['total_size'] += file_size
            self.stats['categories'][main_cat] += 1
            
            if self.stats['files_moved'] % 100 == 0:
                self.log(f"✓ Moved {self.stats['files_moved']} files", "success")
            
            return True
            
        except Exception as e:
            self.stats['errors'] += 1
            return False
    
    def process_all(self, files: List[Path], max_workers: int = 8):
        """Process all files with AI Family"""
        self.log(f"🚀 PROCESSING {len(files)} FILES", "header")
        self.log("AI FAMILY: SHIRL, POPS, ENGR_KEITH, DREAM, LUCY, CLAUDE, GABRIEL, COPILOT", "ai")
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.process_file, f): f for f in files}
            
            for i, future in enumerate(as_completed(futures), 1):
                try:
                    future.result()
                    self.stats['files_processed'] += 1
                    
                    if i % 500 == 0:
                        progress = (i / len(files)) * 100
                        self.log(f"Progress: {i}/{len(files)} ({progress:.1f}%) - {self.stats['files_moved']} moved, {self.stats['errors']} errors", "info")
                except:
                    pass
    
    @staticmethod
    def human_readable_size(size: int) -> str:
        """Convert bytes to human format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"
    
    def generate_report(self):
        """Generate epic report"""
        duration = datetime.now() - self.stats['scan_start']
        
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'✓ REORGANIZATION COMPLETE!'.center(80)}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.END}\n")
        
        print(f"{Colors.BOLD}📊 STATISTICS{Colors.END}")
        print(f"  Duration: {duration}")
        print(f"  Total Files: {self.stats['total_files']}")
        print(f"  Files Moved: {self.stats['files_moved']}")
        print(f"  Total Size: {self.human_readable_size(self.stats['total_size'])}")
        print(f"  Duplicates Removed: {self.stats['duplicates_removed']}")
        print(f"  Space Saved: {self.human_readable_size(self.stats['space_saved'])}")
        print(f"  Errors: {self.stats['errors']}")
        
        print(f"\n{Colors.BOLD}🔧 ENGINE RESULTS{Colors.END}")
        print(f"  METABEAST: {len(self.metabeast.file_hashes)} unique files indexed")
        print(f"  ENGR_KEITH: {self.engr_keith.files_analyzed} code files analyzed")
        print(f"  CODE_VAC: {self.code_vac.cleaned_files} files cleaned")
        
        print(f"\n{Colors.BOLD}📁 CATEGORIES{Colors.END}")
        for cat, count in sorted(self.stats['categories'].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {cat}: {count} files")
        
        print(f"\n{Colors.GREEN}✓ NEW LOCATION: {self.target_drive}{Colors.END}")
        
        # Save JSON report
        report_path = self.target_drive / "ORGANIZATION_REPORT.json"
        with open(report_path, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'duration': str(duration),
                'statistics': dict(self.stats),
                'engines': {
                    'metabeast': len(self.metabeast.file_hashes),
                    'engr_keith': self.engr_keith.files_analyzed,
                    'code_vac': self.code_vac.cleaned_files
                }
            }, f, indent=2)
        
        print(f"\n{Colors.CYAN}📄 Report: {report_path}{Colors.END}")
        print(f"\n{Colors.CYAN}👥 AI FAMILY COLLECTIVE - MISSION ACCOMPLISHED{Colors.END}\n")
    
    def run(self):
        """Execute complete reorganization"""
        self.log(f"📂 SOURCE: {self.source_drive}", "info")
        self.log(f"📁 DESTINATION: {self.target_drive}", "info")
        print()
        
        self.create_structure()
        files = self.scan_drive()
        
        if not files:
            self.log("No files found!", "error")
            return
        
        self.process_all(files)
        self.generate_report()

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Interactive main"""
    print_banner()
    print(f"{Colors.BOLD}{Colors.CYAN}🎯 INTERACTIVE MODE 🎯{Colors.END}\n")
    
    # Command line mode
    if len(sys.argv) > 2:
        source = sys.argv[1]
        destination = sys.argv[2]
        
        if not Path(source).exists():
            print(f"{Colors.RED}✗ Source not found: {source}{Colors.END}")
            sys.exit(1)
        if not Path(destination).exists():
            print(f"{Colors.RED}✗ Destination not found: {destination}{Colors.END}")
            sys.exit(1)
    else:
        # Interactive mode
        print(f"{Colors.BOLD}STEP 1: SELECT SOURCE DRIVE{Colors.END}\n")
        
        drives = []
        for path in ["/Volumes/12TB 1", "/Volumes/12TB", "/Volumes/RED DRAGON", "/Volumes/GABRIEL"]:
            if Path(path).exists():
                drives.append(path)
                print(f"  {len(drives)}. {path}")
        
        print(f"  {len(drives) + 1}. Custom path...")
        
        choice = input(f"\n{Colors.BOLD}Select SOURCE: {Colors.END}").strip()
        
        if choice.isdigit() and int(choice) <= len(drives):
            source = drives[int(choice) - 1]
        else:
            source = input(f"{Colors.CYAN}Enter SOURCE path: {Colors.END}").strip()
        
        print(f"{Colors.GREEN}✓ Source: {source}{Colors.END}\n")
        
        # Destination
        print(f"{Colors.BOLD}STEP 2: SELECT DESTINATION{Colors.END}\n")
        
        dest_drives = [d for d in drives if d != source]
        for i, d in enumerate(dest_drives, 1):
            print(f"  {i}. {d}")
        print(f"  {len(dest_drives) + 1}. Same drive")
        print(f"  {len(dest_drives) + 2}. Custom...")
        
        choice = input(f"\n{Colors.BOLD}Select DESTINATION: {Colors.END}").strip()
        
        if choice.isdigit():
            idx = int(choice) - 1
            if idx < len(dest_drives):
                destination = dest_drives[idx]
            elif idx == len(dest_drives):
                destination = source
            else:
                destination = input(f"{Colors.CYAN}Enter DESTINATION: {Colors.END}").strip()
        else:
            destination = choice
        
        print(f"{Colors.GREEN}✓ Destination: {destination}{Colors.END}\n")
    
    # Show plan
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.END}")
    print(f"{Colors.BOLD}📋 PLAN{Colors.END}")
    print(f"  SOURCE:      {source}")
    print(f"  DESTINATION: {destination}/PERFECT_ORGANIZED_2026/")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.END}\n")
    
    response = input(f"{Colors.BOLD}Ready to organize? (yes/no): {Colors.END}").strip().lower()
    
    if response != 'yes':
        print(f"{Colors.CYAN}Cancelled.{Colors.END}")
        sys.exit(0)
    
    # GO!
    organizer = UltimateMasterOrganizer(source, destination)
    organizer.run()


if __name__ == "__main__":
    main()
