#!/usr/bin/env python3
"""
🧠 CLAUDE ULTIMATE WORKFLOW - 50X FASTER
Organizes and processes everything Claude needs with maximum efficiency
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

class ClaudeWorkflowEngine:
    def __init__(self):
        self.source_folders = [
            '/Users/m2ultra/NOIZYLAB/_CLAUDE_NEEDS',
            '/Users/m2ultra/NOIZYLAB/_CONSOLIDATED_CODE/_CLAUDE_NEEDS'
        ]
        
        self.target_git = '/Users/m2ultra/Github/Noizyfish/NOIZYLAB'
        
        self.categories = {
            'CODE': ['.py', '.js', '.ts', '.tsx', '.jsx', '.java', '.go', '.rs', '.c', '.cpp'],
            'CONFIG': ['.json', '.yml', '.yaml', '.toml', '.ini', '.env'],
            'DOCS': ['.md', '.txt', '.rst', '.pdf'],
            'SCRIPTS': ['.sh', '.bash', '.zsh', '.command'],
            'WEB': ['.html', '.css', '.scss', '.sass', '.vue', '.svelte'],
            'DATA': ['.csv', '.xml', '.sql', '.db', '.sqlite'],
            'MEDIA': ['.mp4', '.wav', '.mp3', '.aif', '.m4a', '.mov']
        }
        
        self.stats = {
            'files_organized': 0,
            'code_files': 0,
            'media_files': 0,
            'total_size': 0,
            'by_category': {}
        }
    
    def scan_claude_needs(self):
        """ULTRA FAST scanning of Claude needs"""
        print("🧠 SCANNING CLAUDE NEEDS...")
        print("=" * 60)
        
        all_files = []
        
        for source in self.source_folders:
            if not os.path.exists(source):
                print(f"⚠️  {source} not found")
                continue
            
            print(f"📂 Scanning: {source}")
            
            for root, dirs, files in os.walk(source):
                # Skip hidden and cache directories
                dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
                
                for file in files:
                    if file.startswith('.'):
                        continue
                    
                    file_path = os.path.join(root, file)
                    ext = Path(file).suffix.lower()
                    
                    try:
                        size = os.path.getsize(file_path)
                        all_files.append({
                            'path': file_path,
                            'name': file,
                            'ext': ext,
                            'size': size,
                            'category': self.categorize_file(ext)
                        })
                    except (OSError, PermissionError):
                        continue
        
        print(f"✅ Found {len(all_files):,} files")
        return all_files
    
    def categorize_file(self, ext):
        """Categorize file by extension"""
        for category, extensions in self.categories.items():
            if ext in extensions:
                return category
        return 'OTHER'
    
    def organize_code_only(self, files):
        """Copy ONLY code files to git repo - FAST"""
        print("\n🚀 ORGANIZING CODE FILES...")
        print("=" * 60)
        
        target_claude = os.path.join(self.target_git, '_CLAUDE_ORGANIZED')
        os.makedirs(target_claude, exist_ok=True)
        
        code_files = [f for f in files if f['category'] in ['CODE', 'CONFIG', 'DOCS', 'SCRIPTS', 'WEB']]
        
        print(f"📦 Processing {len(code_files):,} code files...")
        
        organized = 0
        
        for file_info in code_files:
            try:
                # Create category subfolder
                category_folder = os.path.join(target_claude, file_info['category'])
                os.makedirs(category_folder, exist_ok=True)
                
                # Copy file
                dest = os.path.join(category_folder, file_info['name'])
                
                # Handle duplicates
                counter = 1
                while os.path.exists(dest):
                    name_parts = os.path.splitext(file_info['name'])
                    dest = os.path.join(category_folder, f"{name_parts[0]}_{counter}{name_parts[1]}")
                    counter += 1
                
                shutil.copy2(file_info['path'], dest)
                organized += 1
                
                # Update stats
                self.stats['files_organized'] += 1
                self.stats['total_size'] += file_info['size']
                self.stats['by_category'][file_info['category']] = \
                    self.stats['by_category'].get(file_info['category'], 0) + 1
                
                if organized % 100 == 0:
                    print(f"  ✓ Organized {organized:,} files...")
                    
            except Exception as e:
                print(f"  ⚠️  Error with {file_info['name']}: {e}")
                continue
        
        print(f"✅ Organized {organized:,} code files!")
        return organized
    
    def create_index(self, files):
        """Create searchable index of all files"""
        print("\n📇 CREATING MASTER INDEX...")
        
        index_path = os.path.join(self.target_git, '_CLAUDE_ORGANIZED', 'MASTER_INDEX.json')
        
        index_data = {
            'created': datetime.now().isoformat(),
            'total_files': len(files),
            'by_category': {},
            'by_extension': {},
            'files': []
        }
        
        for file_info in files:
            if file_info['category'] in ['CODE', 'CONFIG', 'DOCS', 'SCRIPTS', 'WEB']:
                index_data['files'].append({
                    'name': file_info['name'],
                    'category': file_info['category'],
                    'extension': file_info['ext'],
                    'size': file_info['size']
                })
                
                # Count by category
                index_data['by_category'][file_info['category']] = \
                    index_data['by_category'].get(file_info['category'], 0) + 1
                
                # Count by extension
                index_data['by_extension'][file_info['ext']] = \
                    index_data['by_extension'].get(file_info['ext'], 0) + 1
        
        with open(index_path, 'w') as f:
            json.dump(index_data, f, indent=2)
        
        print(f"✅ Index created: {index_path}")
        return index_path
    
    def generate_report(self):
        """Generate comprehensive report"""
        print("\n" + "=" * 60)
        print("📊 CLAUDE WORKFLOW COMPLETE")
        print("=" * 60)
        
        print(f"\n✅ Files Organized: {self.stats['files_organized']:,}")
        print(f"💾 Total Size: {self.format_size(self.stats['total_size'])}")
        
        print(f"\n📦 BY CATEGORY:")
        for category, count in sorted(self.stats['by_category'].items(), 
                                     key=lambda x: x[1], reverse=True):
            print(f"  {category:12} | {count:>6,} files")
        
        # Save report
        report_path = f"/Users/m2ultra/CLAUDE_WORKFLOW_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_path, 'w') as f:
            json.dump(self.stats, f, indent=2)
        
        print(f"\n💾 Report saved: {report_path}")
        
        print("\n🎯 NEXT STEPS:")
        print("  1. Review organized files in: _CLAUDE_ORGANIZED/")
        print("  2. Check MASTER_INDEX.json for complete inventory")
        print("  3. Commit to git: cd Github/Noizyfish/NOIZYLAB && git add -A")
        print("  4. Large media files excluded (Git LFS recommended)")
        
        return report_path
    
    def format_size(self, bytes_size):
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.2f} PB"
    
    def run(self):
        """Execute complete workflow"""
        print("\n" + "🧠" * 30)
        print("CLAUDE ULTIMATE WORKFLOW - MAXIMUM VELOCITY")
        print("🧠" * 30 + "\n")
        
        # Scan
        files = self.scan_claude_needs()
        
        if not files:
            print("❌ No files found!")
            return
        
        # Organize code only
        self.organize_code_only(files)
        
        # Create index
        self.create_index(files)
        
        # Generate report
        self.generate_report()
        
        print("\n✨ WORKFLOW COMPLETE!")

if __name__ == "__main__":
    engine = ClaudeWorkflowEngine()
    engine.run()
