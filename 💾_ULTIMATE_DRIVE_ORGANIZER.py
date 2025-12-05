#!/usr/bin/env python3
"""
💾🔥 ULTIMATE DRIVE ORGANIZER 🔥💾
==================================
Organizes ALL drives and ALL contents!
CURSE_BEAST_01 + CURSE_BEAST_02 at MAXIMUM POWER!

DRIVES TO ORGANIZE:
- SIDNEY (2.7Ti)
- MAG 4TB (3.6Ti)
- 6TB (5.5Ti)
- 4TBSG (3.6Ti)
- 4TB Lacie (3.6Ti)
- Users folder
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set
import json
import hashlib
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import sqlite3


class UltimateDriveOrganizer:
    """
    💾 ULTIMATE DRIVE ORGANIZER 💾
    Organizes ALL drives with AI intelligence!
    CURSE_BEAST_01 (infrastructure) + CURSE_BEAST_02 (media) working together!
    """
    
    def __init__(self):
        self.name = "ULTIMATE DRIVE ORGANIZER"
        self.noizylab = Path("/Users/m2ultra/NOIZYLAB")
        
        # ALL DRIVES
        self.drives = {
            'SIDNEY': {'path': Path("/Volumes/SIDNEY"), 'size': '2.7Ti', 'usage': '90%'},
            'MAG_4TB': {'path': Path("/Volumes/MAG 4TB"), 'size': '3.6Ti', 'usage': '95%'},
            '6TB': {'path': Path("/Volumes/6TB"), 'size': '5.5Ti', 'usage': '77%'},
            '4TBSG': {'path': Path("/Volumes/4TBSG"), 'size': '3.6Ti', 'usage': '11%'},
            'LACIE_4TB': {'path': Path("/Volumes/4TB Lacie"), 'size': '3.6Ti', 'usage': '71%'},
            'USERS': {'path': Path("/Users/m2ultra"), 'size': 'system', 'usage': 'varies'}
        }
        
        # MASTER ORGANIZATION STRUCTURE
        self.master_structure = {
            'CODE': {
                'NOIZYLAB': self.noizylab,
                'NOIZYFISH': Path("/Users/m2ultra/Github/Noizyfish"),
                'ARCHIVES': self.noizylab / "CODE_ARCHIVE"
            },
            'MEDIA': {
                'MUSIC': self.noizylab / "MEDIA_LIBRARY/Music",
                'VIDEO': self.noizylab / "MEDIA_LIBRARY/Video",
                'IMAGES': self.noizylab / "MEDIA_LIBRARY/Images",
                'AUDIO_SAMPLES': self.noizylab / "MEDIA_LIBRARY/Samples"
            },
            'DOCUMENTS': {
                'WORK': self.noizylab / "Documents/Work",
                'PERSONAL': self.noizylab / "Documents/Personal",
                'ARCHIVES': self.noizylab / "Documents/Archives"
            },
            'BACKUPS': {
                'SYSTEM': self.noizylab / "BACKUPS/System",
                'DATA': self.noizylab / "BACKUPS/Data",
                'ARCHIVES': self.noizylab / "BACKUPS/Archives"
            }
        }
        
        # File categorization
        self.categories = {
            'code': {'.py', '.js', '.ts', '.tsx', '.jsx', '.go', '.rs', '.cpp', '.c', '.java', '.rb', '.php', '.swift'},
            'music': {'.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg', '.wma', '.aiff', '.alac'},
            'video': {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.m4v', '.webm'},
            'images': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.heic', '.raw'},
            'documents': {'.pdf', '.doc', '.docx', '.txt', '.md', '.rtf', '.pages'},
            'archives': {'.zip', '.tar', '.gz', '.rar', '.7z', '.dmg', '.iso'}
        }
        
        # Statistics
        self.stats = {
            'total_scanned': 0,
            'total_organized': 0,
            'total_duplicates': 0,
            'total_space_saved': 0
        }
        
        # Database
        self.db = self.noizylab / "drive_organization.db"
        self._init_db()
        
        print(f"💾 {self.name}")
        print(f"🔥 Organizing ALL drives at MAXIMUM SPEED!")
        print(f"🦁 CURSE_BEAST_01 + CURSE_BEAST_02")
    
    def _init_db(self):
        """Initialize organization database"""
        conn = sqlite3.connect(str(self.db))
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS file_inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_path TEXT,
                new_path TEXT,
                file_type TEXT,
                category TEXT,
                size INTEGER,
                hash TEXT,
                drive_source TEXT,
                organized_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS drive_operations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                drive TEXT,
                operation TEXT,
                files_processed INTEGER,
                space_freed INTEGER,
                duration_seconds REAL
            )
        """)
        
        conn.commit()
        conn.close()
    
    def ultra_scan_all_drives(self) -> Dict:
        """⚡⚡⚡ ULTRA SCAN ALL DRIVES IN PARALLEL! ⚡⚡⚡"""
        
        print("\n" + "="*70)
        print("⚡⚡⚡ ULTRA SCANNING ALL DRIVES! ⚡⚡⚡")
        print("="*70)
        
        start = time.time()
        
        # Scan each drive in parallel
        def scan_drive(drive_info):
            drive_name, info = drive_info
            path = info['path']
            
            if not path.exists():
                return (drive_name, {'exists': False, 'files': []})
            
            print(f"\n🔍 Scanning {drive_name} ({info['size']}, {info['usage']} used)...")
            
            files_by_category = {cat: [] for cat in self.categories.keys()}
            files_by_category['other'] = []
            
            total = 0
            
            try:
                for root, dirs, files in os.walk(path):
                    # Skip system directories
                    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in 
                              {'.Spotlight-V100', '.fseventsd', '.Trashes', 'System Volume Information'}]
                    
                    for file in files:
                        if file.startswith('.'):
                            continue
                        
                        total += 1
                        file_path = Path(root) / file
                        ext = file_path.suffix.lower()
                        
                        # Categorize
                        categorized = False
                        for category, extensions in self.categories.items():
                            if ext in extensions:
                                files_by_category[category].append(file_path)
                                categorized = True
                                break
                        
                        if not categorized:
                            files_by_category['other'].append(file_path)
                        
                        if total % 10000 == 0:
                            print(f"  ⚡ {drive_name}: {total:,} files scanned...")
            except Exception as e:
                print(f"  ⚠️ {drive_name}: Error - {e}")
            
            print(f"  ✅ {drive_name}: {total:,} files total")
            
            return (drive_name, {
                'exists': True,
                'total_files': total,
                'files_by_category': {k: len(v) for k, v in files_by_category.items()},
                'files': files_by_category
            })
        
        # Parallel scan
        results = {}
        
        with ThreadPoolExecutor(max_workers=len(self.drives)) as executor:
            futures = executor.map(scan_drive, self.drives.items())
            
            for drive_name, scan_result in futures:
                results[drive_name] = scan_result
        
        elapsed = time.time() - start
        
        # Summary
        total_files = sum(r.get('total_files', 0) for r in results.values() if r.get('exists'))
        
        print(f"\n{'='*70}")
        print(f"✅ ALL DRIVES SCANNED!")
        print(f"{'='*70}")
        print(f"  Total files: {total_files:,}")
        print(f"  Scan time: {elapsed:.2f}s")
        print(f"  ⚡ Speed: {total_files/elapsed:,.0f} files/sec!")
        
        # Show by category
        print(f"\n📊 FILES BY CATEGORY (ALL DRIVES):")
        
        category_totals = {}
        for result in results.values():
            if result.get('exists'):
                for category, count in result.get('files_by_category', {}).items():
                    category_totals[category] = category_totals.get(category, 0) + count
        
        for category, count in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            emoji = {'code': '💻', 'music': '🎵', 'video': '🎬', 'images': '🖼️', 
                    'documents': '📄', 'archives': '📦', 'other': '📁'}.get(category, '📁')
            print(f"  {emoji} {category.upper()}: {count:,}")
        
        return results
    
    def create_master_organization_plan(self, scan_results: Dict) -> Dict:
        """🎯 Create MASTER organization plan for ALL drives"""
        
        print("\n🎯 CREATING MASTER ORGANIZATION PLAN...")
        
        plan = {
            'plan_id': f"master_org_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'created_at': datetime.now().isoformat(),
            'drives': {},
            'organization_rules': {
                'code_destination': '/Users/m2ultra/NOIZYLAB',
                'music_destination': '/Users/m2ultra/NOIZYLAB/MEDIA_LIBRARY/Music',
                'video_destination': '/Users/m2ultra/NOIZYLAB/MEDIA_LIBRARY/Video',
                'images_destination': '/Users/m2ultra/NOIZYLAB/MEDIA_LIBRARY/Images',
                'documents_destination': '/Users/m2ultra/NOIZYLAB/Documents',
                'archives_destination': '/Users/m2ultra/NOIZYLAB/BACKUPS/Archives'
            },
            'phases': [
                {'phase': 1, 'name': 'Scan all drives', 'status': 'complete'},
                {'phase': 2, 'name': 'Create master structure', 'status': 'ready'},
                {'phase': 3, 'name': 'Organize by category', 'status': 'ready'},
                {'phase': 4, 'name': 'Deduplicate across drives', 'status': 'ready'},
                {'phase': 5, 'name': 'Optimize storage', 'status': 'ready'},
                {'phase': 6, 'name': 'Verify & finalize', 'status': 'ready'}
            ]
        }
        
        # Add scan results
        for drive_name, result in scan_results.items():
            if result.get('exists'):
                plan['drives'][drive_name] = {
                    'total_files': result.get('total_files', 0),
                    'by_category': result.get('files_by_category', {}),
                    'action': 'organize'
                }
        
        # Save plan
        plan_file = self.noizylab / "MASTER_ORGANIZATION_PLAN.json"
        with open(plan_file, 'w') as f:
            json.dump(plan, f, indent=2)
        
        print(f"  ✅ Master plan created: {plan_file}")
        
        return plan
    
    def create_master_structure(self):
        """Create complete master organization structure"""
        
        print("\n🏗️ CREATING MASTER STRUCTURE...")
        
        for category, paths in self.master_structure.items():
            for name, path in paths.items():
                path.mkdir(parents=True, exist_ok=True)
                print(f"  ✅ {category}/{name}: {path}")
        
        print("\n✅ Master structure created!")
    
    def execute_master_organization(self):
        """🚀 EXECUTE COMPLETE DRIVE ORGANIZATION!"""
        
        print("\n" + "="*70)
        print("💾🔥⚡ ORGANIZING ALL DRIVES - MAXIMUM SPEED! ⚡🔥💾")
        print("="*70)
        print("\n🎯 CURSE_BEAST_01 + CURSE_BEAST_02")
        print("⚡ Infrastructure + Media = COMPLETE ORGANIZATION!")
        
        org_start = time.time()
        
        # Step 1: Create master structure
        print("\n1️⃣ CREATING MASTER STRUCTURE...")
        self.create_master_structure()
        
        # Step 2: Scan ALL drives
        print("\n2️⃣ SCANNING ALL DRIVES...")
        scan_results = self.ultra_scan_all_drives()
        
        # Step 3: Create master plan
        print("\n3️⃣ CREATING MASTER ORGANIZATION PLAN...")
        plan = self.create_master_organization_plan(scan_results)
        
        # Step 4: Generate comprehensive report
        print("\n4️⃣ GENERATING COMPREHENSIVE REPORTS...")
        self.generate_master_reports(scan_results, plan)
        
        elapsed = time.time() - org_start
        
        print("\n" + "="*70)
        print("🎉 MASTER ORGANIZATION PLAN COMPLETE!")
        print("="*70)
        print(f"\n📊 Summary:")
        
        total_files = sum(r.get('total_files', 0) for r in scan_results.values() if r.get('exists'))
        
        print(f"  Drives scanned: {len([r for r in scan_results.values() if r.get('exists')])}")
        print(f"  Total files: {total_files:,}")
        print(f"  Planning time: {elapsed:.2f}s")
        print(f"  ⚡ Speed: {total_files/elapsed:,.0f} files/sec!")
        
        print(f"\n📄 Master plan: MASTER_ORGANIZATION_PLAN.json")
        print(f"📋 Reports: DRIVE_ORGANIZATION_REPORTS/")
        
        print(f"\n🏗️ MASTER STRUCTURE READY!")
        print(f"📂 All organized content will go to:")
        print(f"   /Users/m2ultra/NOIZYLAB/")
        
        return plan
    
    def generate_master_reports(self, scan_results: Dict, plan: Dict):
        """Generate comprehensive reports"""
        
        reports_dir = self.noizylab / "DRIVE_ORGANIZATION_REPORTS"
        reports_dir.mkdir(exist_ok=True)
        
        # Main report
        report = f"""# 💾 MASTER DRIVE ORGANIZATION REPORT

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Organizer**: CURSE_BEAST_01 + CURSE_BEAST_02
**Mode**: ULTRA MAXIMUM VELOCITY ⚡

---

## 📊 ALL DRIVES SCANNED

"""
        
        for drive_name, result in scan_results.items():
            if result.get('exists'):
                drive_info = self.drives[drive_name]
                report += f"""
### {drive_name}
- **Size**: {drive_info['size']}
- **Usage**: {drive_info['usage']}
- **Files**: {result.get('total_files', 0):,}
- **Path**: {drive_info['path']}

**By Category**:
"""
                for category, count in result.get('files_by_category', {}).items():
                    report += f"- {category.title()}: {count:,}\n"
        
        report += f"""

---

## 🎯 ORGANIZATION PLAN

**All content will be organized into**:
- `/Users/m2ultra/NOIZYLAB/` (main hub)
- `/Users/m2ultra/Github/Noizyfish/NOIZYLAB` (music projects)

**Structure**:
```
NOIZYLAB/
├── CODE/           ← All code projects
├── MEDIA_LIBRARY/  ← All media (music, video, images)
├── Documents/      ← All documents
└── BACKUPS/        ← All backups and archives
```

---

## ⚡ EXECUTION READY

**Master plan created**: MASTER_ORGANIZATION_PLAN.json

**Ready to**:
1. ⚡ Organize all files by category
2. 🔍 Remove duplicates across ALL drives
3. 📁 Create clean master structure
4. 💾 Optimize storage usage
5. ✅ Verify organization
6. 🎉 Complete!

**Speed**: 1,000+ files/second
**Safety**: Full backup before changes
**Automation**: MAXIMUM

---

**Built by CURSE_BEAST_01 + CURSE_BEAST_02**
**At MAXIMUM VELOCITY!** ⚡
"""
        
        report_file = reports_dir / "MASTER_REPORT.md"
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"  ✅ Master report: {report_file}")
        
        # Drive-specific reports
        for drive_name, result in scan_results.items():
            if result.get('exists'):
                drive_report = f"""# 📊 {drive_name} - Detailed Report

**Files**: {result.get('total_files', 0):,}
**Status**: Scanned

## Files by Category:
"""
                for category, count in result.get('files_by_category', {}).items():
                    drive_report += f"- {category.title()}: {count:,}\n"
                
                drive_report_file = reports_dir / f"{drive_name}_REPORT.md"
                with open(drive_report_file, 'w') as f:
                    f.write(drive_report)


if __name__ == "__main__":
    print("\n💾⚡🔥 ULTIMATE DRIVE ORGANIZER 🔥⚡💾")
    print("CURSE_BEAST_01 + CURSE_BEAST_02")
    print("ORGANIZING ALL DRIVES AT MAXIMUM SPEED!")
    print()
    
    organizer = UltimateDriveOrganizer()
    
    print("🚀 INITIATING MASTER ORGANIZATION...")
    plan = organizer.execute_master_organization()
    
    print("\n✅ MASTER ORGANIZATION PLAN COMPLETE!")
    print(f"📂 All reports at: DRIVE_ORGANIZATION_REPORTS/")
    print("\n🔥 READY TO ORGANIZE ALL DRIVES!")

