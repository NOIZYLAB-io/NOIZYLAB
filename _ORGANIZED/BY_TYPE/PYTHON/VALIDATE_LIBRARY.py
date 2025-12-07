#!/usr/bin/env python3
"""
EXS24 Master Library - Library Validator
Validates library integrity and checks for issues
"""

import json
import os
from pathlib import Path
from datetime import datetime

class LibraryValidator:
    def __init__(self, scan_data_file=None):
        if scan_data_file is None:
            scan_data_file = Path(__file__).parent / "SCAN_DATA.json"
        self.scan_data_file = Path(scan_data_file)
        self.data = None
        self.issues = []
        self.warnings = []
        self.load_data()
    
    def load_data(self):
        """Load scan data"""
        if not self.scan_data_file.exists():
            print("⚠️  No scan data found. Run SCAN_AND_ORGANIZE.py first.")
            return False
        
        try:
            with open(self.scan_data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            return True
        except Exception as e:
            print(f"⚠️  Error loading data: {e}")
            return False
    
    def validate_file_existence(self):
        """Check if all files in scan data actually exist"""
        if not self.data:
            return
        
        print("🔍 Validating file existence...")
        files = self.data.get('exs_files', [])
        missing = []
        
        for file_path in files:
            full_path = Path(__file__).parent / file_path
            if not full_path.exists():
                missing.append(file_path)
        
        if missing:
            self.issues.append(f"Missing files: {len(missing)}")
            print(f"  ⚠️  Found {len(missing)} missing files")
        else:
            print("  ✅ All files exist")
        
        return len(missing)
    
    def validate_naming(self):
        """Validate file naming conventions"""
        if not self.data:
            return
        
        print("🔍 Validating naming conventions...")
        inconsistencies = self.data.get('naming_inconsistencies', [])
        
        if inconsistencies:
            self.issues.append(f"Naming inconsistencies: {len(inconsistencies)}")
            print(f"  ⚠️  Found {len(inconsistencies)} naming issues")
        else:
            print("  ✅ All files follow naming conventions")
        
        return len(inconsistencies)
    
    def validate_structure(self):
        """Validate directory structure"""
        if not self.data:
            return
        
        print("🔍 Validating directory structure...")
        loose_files = self.data.get('loose_files', [])
        empty_dirs = self.data.get('empty_dirs', [])
        
        if loose_files:
            self.warnings.append(f"Loose files: {len(loose_files)}")
            print(f"  ⚠️  Found {len(loose_files)} loose files")
        
        if empty_dirs:
            self.warnings.append(f"Empty directories: {len(empty_dirs)}")
            print(f"  ⚠️  Found {len(empty_dirs)} empty directories")
        
        if not loose_files and not empty_dirs:
            print("  ✅ Directory structure is clean")
        
        return len(loose_files) + len(empty_dirs)
    
    def validate_collections(self):
        """Validate collection organization"""
        if not self.data:
            return
        
        print("🔍 Validating collections...")
        collections = self.data.get('collections', {})
        
        if not collections:
            self.issues.append("No collections detected")
            print("  ⚠️  No collections found")
        else:
            print(f"  ✅ Found {len(collections)} collections")
        
        # Check for very small collections (might be misorganized)
        small_collections = [c for c, files in collections.items() 
                           if (isinstance(files, list) and len(files) < 3) or 
                              (isinstance(files, int) and files < 3)]
        
        if small_collections:
            self.warnings.append(f"Small collections: {len(small_collections)}")
            print(f"  ⚠️  Found {len(small_collections)} very small collections")
        
        return len(collections)
    
    def validate_duplicates(self):
        """Validate duplicate files"""
        if not self.data:
            return
        
        print("🔍 Validating duplicates...")
        filename_dupes = len(self.data.get('duplicates', {}))
        true_dupes = len(self.data.get('duplicates_by_hash', {}))
        
        if true_dupes > 0:
            self.warnings.append(f"True duplicates: {true_dupes} groups")
            print(f"  ⚠️  Found {true_dupes} groups of true duplicates")
        
        if filename_dupes > 1000:
            self.warnings.append(f"Many duplicate filenames: {filename_dupes}")
            print(f"  ⚠️  Found {filename_dupes} duplicate filenames")
        
        if true_dupes == 0 and filename_dupes < 1000:
            print("  ✅ Duplicate situation is acceptable")
        
        return true_dupes + filename_dupes
    
    def run_validation(self):
        """Run all validation checks"""
        if not self.data:
            print("⚠️  Cannot run validation without scan data")
            return False
        
        print("=" * 80)
        print("🔍 EXS24 LIBRARY VALIDATION")
        print("=" * 80)
        print()
        
        self.validate_file_existence()
        print()
        self.validate_naming()
        print()
        self.validate_structure()
        print()
        self.validate_collections()
        print()
        self.validate_duplicates()
        print()
        
        # Summary
        print("=" * 80)
        print("📊 VALIDATION SUMMARY")
        print("=" * 80)
        
        if self.issues:
            print(f"\n❌ ISSUES FOUND: {len(self.issues)}")
            for issue in self.issues:
                print(f"  • {issue}")
        else:
            print("\n✅ No critical issues found")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS: {len(self.warnings)}")
            for warning in self.warnings:
                print(f"  • {warning}")
        else:
            print("\n✅ No warnings")
        
        print()
        
        if not self.issues and not self.warnings:
            print("🎉 Library validation passed! Everything looks good.")
        elif not self.issues:
            print("✅ Library is functional, but some optimizations are recommended.")
        else:
            print("⚠️  Library has issues that should be addressed.")
        
        return len(self.issues) == 0


def main():
    validator = LibraryValidator()
    validator.run_validation()


if __name__ == "__main__":
    main()




