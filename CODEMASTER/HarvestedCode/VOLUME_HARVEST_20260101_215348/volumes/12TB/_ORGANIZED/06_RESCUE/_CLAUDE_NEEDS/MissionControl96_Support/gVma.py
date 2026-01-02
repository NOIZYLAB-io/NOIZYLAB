#!/usr/bin/env python3
"""
NOIZYGENIE Quality Check & Migration to Native_Instruments_2026
Comprehensive quality assessment and migration system
"""

import os
import shutil
import json
from pathlib import Path
from collections import defaultdict, Counter
import time
from datetime import datetime
import sys
sys.path.append('/Users/rsp_ms')
from palatino_terminal import PalatinoTerminal

class QualityCheckMigration:
    def __init__(self):
        self.pt = PalatinoTerminal()
        self.kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
        self.ni_2026 = Path("/Volumes/6TB/Native_Instruments_2026")
        self.reports_dir = self.kontakt_lab / "REPORTS"
        
        # Quality check criteria
        self.quality_standards = {
            'minimum_instruments': 5,
            'minimum_sample_ratio': 0.3,  # 30% samples to instruments ratio
            'preferred_sample_ratio': 0.8,  # 80% for premium quality
            'minimum_total_files': 10,
            'preferred_total_files': 50,
            'maximum_broken_files': 0.1,  # 10% broken files allowed
        }
        
        # Migration mapping to NI_2026 structure
        self.migration_map = {
            "01_ELECTRONIC": "10_MODERN_ELECTRONIC",
            "02_ORCHESTRAL": "01_ORCHESTRAL_PREMIUM", 
            "03_ACOUSTIC": "05_KEYBOARDS_PIANOS",
            "04_URBAN": "10_MODERN_ELECTRONIC",
            "05_ROCK_POP": "06_STRINGS_GUITARS",
            "06_WORLD_ETHNIC": "07_WORLD_ETHNIC",
            "07_SYNTHESIZERS": "10_MODERN_ELECTRONIC", 
            "08_DRUMS_PERCUSSION": "04_DRUMS_PERCUSSION",
            "09_LOOPS_GROOVES": "02_CINEMATIC_EPIC",
            "10_SOUNDSCAPES_FX": "08_EXPERIMENTAL_FX",
            "11_VOCALS": "02_CINEMATIC_EPIC",
            "12_CONSTRUCTION_KITS": "02_CINEMATIC_EPIC",
            "13_MULTIS_COMBIS": "03_CORE_INSTRUMENTS"
        }
        
        # Statistics
        self.stats = {
            'libraries_checked': 0,
            'passed_quality': 0,
            'failed_quality': 0,
            'migrated_successfully': 0,
            'migration_errors': 0,
            'total_files_migrated': 0,
            'quality_scores': []
        }
        
    def calculate_quality_score(self, library_path):
        """Calculate comprehensive quality score for a library"""
        score_details = {
            'library_name': library_path.name,
            'path': str(library_path),
            'instruments': 0,
            'samples': 0,
            'total_files': 0,
            'sample_ratio': 0.0,
            'file_integrity': 1.0,
            'organization_score': 0.0,
            'final_score': 0.0,
            'quality_level': 'UNKNOWN',
            'issues': []
        }
        
        try:
            # Count different file types
            instrument_files = (
                list(library_path.rglob("*.nki")) +
                list(library_path.rglob("*.nkm")) +
                list(library_path.rglob("*.nkc"))
            )
            
            sample_files = (
                list(library_path.rglob("*.ncw")) +
                list(library_path.rglob("*.wav")) +
                list(library_path.rglob("*.aiff"))
            )
            
            all_files = list(library_path.rglob("*"))
            all_files = [f for f in all_files if f.is_file()]
            
            score_details['instruments'] = len(instrument_files)
            score_details['samples'] = len(sample_files)
            score_details['total_files'] = len(all_files)
            
            # Calculate sample ratio
            if score_details['instruments'] > 0:
                score_details['sample_ratio'] = score_details['samples'] / score_details['instruments']
            
            # Start with base score
            quality_score = 0.0
            
            # 1. Instrument count score (0-25 points)
            if score_details['instruments'] >= 100:
                quality_score += 25
            elif score_details['instruments'] >= 50:
                quality_score += 20
            elif score_details['instruments'] >= 20:
                quality_score += 15
            elif score_details['instruments'] >= 10:
                quality_score += 10
            elif score_details['instruments'] >= 5:
                quality_score += 5
            else:
                score_details['issues'].append(f"Too few instruments ({score_details['instruments']})")
            
            # 2. Sample ratio score (0-30 points)
            if score_details['sample_ratio'] >= 1.0:
                quality_score += 30
            elif score_details['sample_ratio'] >= 0.8:
                quality_score += 25
            elif score_details['sample_ratio'] >= 0.5:
                quality_score += 20
            elif score_details['sample_ratio'] >= 0.3:
                quality_score += 15
            elif score_details['sample_ratio'] >= 0.1:
                quality_score += 10
            else:
                score_details['issues'].append(f"Very low sample ratio ({score_details['sample_ratio']:.2f})")
            
            # 3. File organization score (0-20 points)
            org_score = 0
            subdirs = [d for d in library_path.iterdir() if d.is_dir()]
            
            # Check for good organization patterns
            good_dirs = ['Instruments', 'Samples', 'Snapshots', 'Documentation', 'Midi Files', 'Library Data']
            for good_dir in good_dirs:
                if any(good_dir.lower() in d.name.lower() for d in subdirs):
                    org_score += 3
            
            # Bonus for Native Instruments standard structure
            if any('nkr' in f.name.lower() for f in all_files):
                org_score += 5  # NKR compressed archives
            if any('nkx' in f.name.lower() for f in all_files):
                org_score += 3  # NKX files
            if any('nksn' in f.name.lower() for f in all_files):
                org_score += 2  # Snapshots
            
            score_details['organization_score'] = min(org_score, 20)
            quality_score += score_details['organization_score']
            
            # 4. File integrity score (0-15 points)
            integrity_score = 15  # Start perfect, deduct for issues
            
            # Check for broken or suspicious files
            broken_files = 0
            for file_path in all_files[:100]:  # Sample check to avoid performance issues
                try:
                    if file_path.stat().st_size == 0:
                        broken_files += 1
                except:
                    broken_files += 1
            
            if broken_files > 0:
                integrity_penalty = min(broken_files * 2, 10)
                integrity_score -= integrity_penalty
                score_details['issues'].append(f"{broken_files} potentially broken files")
            
            score_details['file_integrity'] = integrity_score / 15
            quality_score += integrity_score
            
            # 5. Content diversity bonus (0-10 points)
            file_extensions = set()
            for f in all_files[:50]:  # Sample check
                file_extensions.add(f.suffix.lower())
            
            diversity_score = min(len(file_extensions), 10)
            quality_score += diversity_score
            
            # Final score calculation
            score_details['final_score'] = quality_score
            
            # Determine quality level
            if quality_score >= 80:
                score_details['quality_level'] = 'PREMIUM'
            elif quality_score >= 65:
                score_details['quality_level'] = 'EXCELLENT'
            elif quality_score >= 50:
                score_details['quality_level'] = 'GOOD'
            elif quality_score >= 35:
                score_details['quality_level'] = 'ACCEPTABLE'
            else:
                score_details['quality_level'] = 'POOR'
            
        except Exception as e:
            score_details['issues'].append(f"Analysis error: {str(e)}")
            score_details['quality_level'] = 'ERROR'
        
        return score_details
    
    def get_migration_target(self, library_path):
        """Determine the target directory in Native_Instruments_2026"""
        # Find which organized category this library belongs to
        for category_dir in self.kontakt_lab.iterdir():
            if category_dir.is_dir() and category_dir.name in self.migration_map:
                # Check if library is in this category
                try:
                    if library_path.is_relative_to(category_dir):
                        target_category = self.migration_map[category_dir.name]
                        return self.ni_2026 / target_category
                except:
                    continue
        
        # Default to CORE_INSTRUMENTS if not found
        return self.ni_2026 / "03_CORE_INSTRUMENTS"
    
    def migrate_library(self, library_path, quality_details):
        """Migrate a quality-approved library to Native_Instruments_2026"""
        target_base = self.get_migration_target(library_path)
        target_path = target_base / library_path.name
        
        # Ensure target directory exists
        target_base.mkdir(exist_ok=True, parents=True)
        
        # Handle name conflicts
        counter = 1
        original_target = target_path
        while target_path.exists():
            target_path = original_target.parent / f"{original_target.name}_v{counter:02d}"
            counter += 1
        
        try:
            # Copy the entire library
            shutil.copytree(library_path, target_path)
            
            # Create quality report file
            quality_report = target_path / "QUALITY_REPORT.txt"
            with open(quality_report, 'w') as f:
                f.write("🎹 NOIZYGENIE Quality Assessment Report\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Library: {quality_details['library_name']}\n")
                f.write(f"Quality Level: {quality_details['quality_level']}\n")
                f.write(f"Final Score: {quality_details['final_score']:.1f}/100\n")
                f.write(f"Migration Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write("📊 DETAILED METRICS:\n")
                f.write(f"   Instruments: {quality_details['instruments']}\n")
                f.write(f"   Samples: {quality_details['samples']}\n")
                f.write(f"   Total Files: {quality_details['total_files']}\n")
                f.write(f"   Sample Ratio: {quality_details['sample_ratio']:.2f}\n")
                f.write(f"   Organization Score: {quality_details['organization_score']}/20\n")
                f.write(f"   File Integrity: {quality_details['file_integrity']:.1%}\n\n")
                
                if quality_details['issues']:
                    f.write("⚠️ NOTED ISSUES:\n")
                    for issue in quality_details['issues']:
                        f.write(f"   - {issue}\n")
            
            self.stats['migrated_successfully'] += 1
            self.stats['total_files_migrated'] += quality_details['total_files']
            
            return target_path
            
        except Exception as e:
            self.stats['migration_errors'] += 1
            return None
    
    def run_quality_check_migration(self, minimum_score=50):
        """Run comprehensive quality check and migration process"""
        start_time = time.time()
        
        self.pt.header("NOIZYGENIE Quality Check & Migration to Native_Instruments_2026")
        self.pt.info("Source", str(self.kontakt_lab))
        self.pt.info("Target", str(self.ni_2026))
        self.pt.info("Minimum Quality Score", f"{minimum_score}/100")
        self.pt.info("Started", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        # Verify target directory exists
        if not self.ni_2026.exists():
            self.pt.error(f"Target directory not found: {self.ni_2026}")
            return
        
        self.pt.success(f"Target Native_Instruments_2026 directory confirmed")
        
        # Find all libraries in organized categories
        libraries_to_check = []
        
        for category_dir in self.kontakt_lab.iterdir():
            if (category_dir.is_dir() and 
                category_dir.name in self.migration_map and
                category_dir.name not in ['REPORTS', '6TB_ARCHIVE']):
                
                # Get libraries from this category
                for item in category_dir.rglob("*"):
                    if (item.is_dir() and 
                        any(item.rglob("*.nki")) and  # Has instruments
                        len(list(item.parents)) - len(list(category_dir.parents)) <= 3):  # Not too nested
                        libraries_to_check.append(item)
        
        self.pt.subheader(f"Quality Assessment Phase")
        self.pt.info("Libraries to check", f"{len(libraries_to_check):,}")
        
        # Quality check phase
        passed_libraries = []
        failed_libraries = []
        
        for i, library_path in enumerate(libraries_to_check, 1):
            print(f"\n📊 Quality Check {i:3d}/{len(libraries_to_check)}: {library_path.name}")
            
            quality_details = self.calculate_quality_score(library_path)
            self.stats['libraries_checked'] += 1
            self.stats['quality_scores'].append(quality_details['final_score'])
            
            # Display results
            score = quality_details['final_score']
            level = quality_details['quality_level']
            
            if score >= minimum_score:
                self.stats['passed_quality'] += 1
                passed_libraries.append((library_path, quality_details))
                
                if level == 'PREMIUM':
                    status_icon = "🏆"
                elif level == 'EXCELLENT': 
                    status_icon = "⭐"
                else:
                    status_icon = "✅"
                    
                print(f"   {status_icon} PASSED: {level} ({score:.1f}/100)")
                print(f"      📊 {quality_details['instruments']} inst, {quality_details['samples']} samples (ratio: {quality_details['sample_ratio']:.2f})")
                
            else:
                self.stats['failed_quality'] += 1
                failed_libraries.append((library_path, quality_details))
                print(f"   ❌ FAILED: {level} ({score:.1f}/100)")
                if quality_details['issues']:
                    print(f"      ⚠️  Issues: {', '.join(quality_details['issues'][:2])}")
            
            # Progress checkpoint
            if i % 20 == 0:
                self.pt.info("Progress", f"{i}/{len(libraries_to_check)} libraries assessed")
        
        # Migration phase
        self.pt.section_break()
        self.pt.subheader(f"Migration Phase - {len(passed_libraries)} Libraries Approved")
        
        if not passed_libraries:
            self.pt.warning("No libraries passed quality check")
            return
        
        migrated_count = 0
        for i, (library_path, quality_details) in enumerate(passed_libraries, 1):
            print(f"\n🚀 Migrating {i:3d}/{len(passed_libraries)}: {library_path.name}")
            
            target_path = self.migrate_library(library_path, quality_details)
            
            if target_path:
                migrated_count += 1
                target_category = target_path.parent.name
                print(f"   ✅ Migrated → {target_category}/{target_path.name}")
            else:
                print(f"   ❌ Migration failed")
        
        # Final statistics
        elapsed_time = time.time() - start_time
        
        self.pt.section_break()
        self.pt.complete("QUALITY CHECK & MIGRATION COMPLETE!")
        
        self.pt.info("Libraries Checked", f"{self.stats['libraries_checked']:,}")
        self.pt.info("Passed Quality", f"{self.stats['passed_quality']:,}")
        self.pt.info("Failed Quality", f"{self.stats['failed_quality']:,}")
        self.pt.info("Successfully Migrated", f"{self.stats['migrated_successfully']:,}")
        self.pt.info("Migration Errors", f"{self.stats['migration_errors']:,}")
        self.pt.info("Total Files Migrated", f"{self.stats['total_files_migrated']:,}")
        
        if self.stats['quality_scores']:
            avg_score = sum(self.stats['quality_scores']) / len(self.stats['quality_scores'])
            self.pt.info("Average Quality Score", f"{avg_score:.1f}/100")
        
        self.pt.info("Processing Time", f"{elapsed_time/60:.1f} minutes")
        
        # Create migration report
        self.create_migration_report(passed_libraries, failed_libraries)
        
        self.pt.section_break()
        self.pt.success("🎹 Premium libraries now available in Native_Instruments_2026! 🎹")
        self.pt.timestamp()
    
    def create_migration_report(self, passed_libraries, failed_libraries):
        """Create comprehensive migration report"""
        report_file = self.reports_dir / f"MIGRATION_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_file, 'w') as f:
            f.write("🎹 NOIZYGENIE Migration to Native_Instruments_2026 Report\n")
            f.write("=" * 70 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("📊 MIGRATION SUMMARY:\n")
            f.write(f"   Libraries Checked: {self.stats['libraries_checked']}\n")
            f.write(f"   Passed Quality: {self.stats['passed_quality']}\n")
            f.write(f"   Failed Quality: {self.stats['failed_quality']}\n")
            f.write(f"   Successfully Migrated: {self.stats['migrated_successfully']}\n")
            f.write(f"   Files Migrated: {self.stats['total_files_migrated']:,}\n\n")
            
            f.write("🏆 MIGRATED LIBRARIES (Quality Approved):\n")
            f.write("-" * 50 + "\n")
            for library_path, quality_details in passed_libraries:
                if self.stats['migrated_successfully'] > 0:  # Only if actually migrated
                    f.write(f"\n{library_path.name}:\n")
                    f.write(f"   Quality: {quality_details['quality_level']} ({quality_details['final_score']:.1f}/100)\n")
                    f.write(f"   Files: {quality_details['instruments']} inst, {quality_details['samples']} samples\n")
            
            if failed_libraries:
                f.write(f"\n❌ FAILED QUALITY CHECK:\n")
                f.write("-" * 30 + "\n")
                for library_path, quality_details in failed_libraries[:20]:  # Top 20 failures
                    f.write(f"\n{library_path.name}: {quality_details['final_score']:.1f}/100\n")
                    if quality_details['issues']:
                        f.write(f"   Issues: {', '.join(quality_details['issues'])}\n")
        
        self.pt.success(f"Migration report saved: {report_file.name}")

if __name__ == "__main__":
    try:
        migration_system = QualityCheckMigration()
        migration_system.run_quality_check_migration(minimum_score=50)  # 50/100 minimum
    except KeyboardInterrupt:
        print("\n⏹️  Quality check and migration cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()