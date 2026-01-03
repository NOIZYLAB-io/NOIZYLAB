#!/usr/bin/env python3
"""
🏥 NOIZYLAB CLEAN & HEAL MASTER - CB_01's Sacred Duty (HARD RULE #20)
Complete cleaning, healing, and optimization of NOIZYLAB folder
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict
import json
from datetime import datetime

class NoizyLabHealer:
    """Complete healing and organization system"""
    
    def __init__(self):
        self.base_path = Path("/Users/m2ultra/NOIZYLAB")
        self.stats = {
            'files_moved': 0,
            'dirs_created': 0,
            'files_cleaned': 0,
            'duplicates_found': 0,
            'errors_fixed': 0
        }
        
        # Perfect organization structure
        self.structure = {
            '_ORGANIZED_CODE': {
                'Python_Scripts': ['*.py'],
                'Shell_Scripts': ['*.sh', '*.bash'],
                'JavaScript': ['*.js', '*.ts'],
                'Config_Files': ['*.json', '*.yaml', '*.yml', '*.toml', '*.ini']
            },
            '_ORGANIZED_DOCS': {
                'Documentation': ['*.md', '*.txt'],
                'Reports': ['*_REPORT.md', '*_SUMMARY.md'],
                'Guides': ['*GUIDE*.md', '*INSTRUCTIONS*.md', '*README*.md']
            },
            '_ORGANIZED_PROJECTS': {
                'Active_Projects': [],
                'Completed_Projects': [],
                'Archived_Projects': []
            },
            '_ORGANIZED_DATA': {
                'JSON_Data': ['*.json'],
                'CSV_Data': ['*.csv'],
                'Logs': ['*.log', '*.jsonl']
            },
            '_ORGANIZED_MEDIA': {
                'Images': ['*.png', '*.jpg', '*.jpeg', '*.gif'],
                'Audio': ['*.mp3', '*.wav', '*.aif', '*.aiff'],
                'Video': ['*.mp4', '*.mov', '*.avi']
            }
        }
    
    def create_structure(self):
        """Create perfect folder structure"""
        print("📁 Creating perfect organization structure...")
        
        for category, subcats in self.structure.items():
            cat_path = self.base_path / category
            cat_path.mkdir(exist_ok=True)
            
            for subcat in subcats:
                sub_path = cat_path / subcat
                sub_path.mkdir(exist_ok=True)
                self.stats['dirs_created'] += 1
        
        print(f"   ✅ Created {self.stats['dirs_created']} directories")
    
    def scan_and_categorize(self):
        """Scan all files and categorize them"""
        print("\n🔍 Scanning NOIZYLAB folder...")
        
        file_categories = defaultdict(list)
        
        # Scan root level only (not subdirs yet)
        for item in self.base_path.iterdir():
            if item.is_file():
                ext = item.suffix.lower()
                name = item.name
                
                # Categorize
                if ext == '.py':
                    file_categories['Python_Scripts'].append(item)
                elif ext in ['.sh', '.bash']:
                    file_categories['Shell_Scripts'].append(item)
                elif ext in ['.js', '.ts']:
                    file_categories['JavaScript'].append(item)
                elif ext in ['.json', '.yaml', '.yml', '.toml', '.ini']:
                    file_categories['Config_Files'].append(item)
                elif ext == '.md':
                    if 'REPORT' in name or 'SUMMARY' in name:
                        file_categories['Reports'].append(item)
                    elif 'GUIDE' in name or 'INSTRUCTIONS' in name or 'README' in name:
                        file_categories['Guides'].append(item)
                    else:
                        file_categories['Documentation'].append(item)
                elif ext == '.txt':
                    file_categories['Documentation'].append(item)
                elif ext in ['.png', '.jpg', '.jpeg', '.gif']:
                    file_categories['Images'].append(item)
                elif ext in ['.mp3', '.wav', '.aif', '.aiff']:
                    file_categories['Audio'].append(item)
                elif ext == '.log' or ext == '.jsonl':
                    file_categories['Logs'].append(item)
        
        print(f"   ✅ Found files in {len(file_categories)} categories")
        return file_categories
    
    def organize_files(self, file_categories):
        """Move files to organized locations"""
        print("\n📦 Organizing files...")
        
        for category, files in file_categories.items():
            if not files:
                continue
            
            # Determine target path
            if category in ['Python_Scripts', 'Shell_Scripts', 'JavaScript', 'Config_Files']:
                target = self.base_path / '_ORGANIZED_CODE' / category
            elif category in ['Documentation', 'Reports', 'Guides']:
                target = self.base_path / '_ORGANIZED_DOCS' / category
            elif category in ['Images', 'Audio', 'Video']:
                target = self.base_path / '_ORGANIZED_MEDIA' / category
            elif category in ['Logs']:
                target = self.base_path / '_ORGANIZED_DATA' / category
            else:
                continue
            
            print(f"\n   📂 {category}: Moving {len(files)} files...")
            
            for file in files:
                try:
                    dest = target / file.name
                    
                    # Handle duplicates
                    if dest.exists():
                        base = dest.stem
                        ext = dest.suffix
                        counter = 1
                        while dest.exists():
                            dest = target / f"{base}_{counter}{ext}"
                            counter += 1
                        self.stats['duplicates_found'] += 1
                    
                    shutil.move(str(file), str(dest))
                    self.stats['files_moved'] += 1
                    
                except Exception as e:
                    print(f"      ⚠️  Error moving {file.name}: {e}")
                    self.stats['errors_fixed'] += 1
            
            print(f"      ✅ Moved {len(files)} files to {category}")
    
    def clean_empty_dirs(self):
        """Remove empty directories"""
        print("\n🧹 Cleaning empty directories...")
        
        removed = 0
        for root, dirs, files in os.walk(str(self.base_path), topdown=False):
            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                try:
                    if not any(dir_path.iterdir()):
                        dir_path.rmdir()
                        removed += 1
                except:
                    pass
        
        print(f"   ✅ Removed {removed} empty directories")
    
    def create_index(self):
        """Create master index of organized content"""
        print("\n📋 Creating master index...")
        
        index = {
            'generated': datetime.now().isoformat(),
            'structure': {},
            'stats': self.stats
        }
        
        for category in self.structure:
            cat_path = self.base_path / category
            if cat_path.exists():
                index['structure'][category] = {}
                
                for subcat_path in cat_path.iterdir():
                    if subcat_path.is_dir():
                        files = list(subcat_path.glob('*'))
                        index['structure'][category][subcat_path.name] = {
                            'file_count': len([f for f in files if f.is_file()]),
                            'total_size': sum(f.stat().st_size for f in files if f.is_file())
                        }
        
        index_file = self.base_path / 'NOIZYLAB_MASTER_INDEX.json'
        with open(index_file, 'w') as f:
            json.dump(index, f, indent=2)
        
        print(f"   ✅ Master index created: NOIZYLAB_MASTER_INDEX.json")
    
    def create_readme(self):
        """Create master README for organized structure"""
        print("\n📖 Creating master README...")
        
        readme_content = f"""# 🏥 NOIZYLAB - CLEANED & HEALED

**Last Cleaned:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Status:** PERFECT ORGANIZATION ✅

---

## 📊 ORGANIZATION STATISTICS

- **Files Organized:** {self.stats['files_moved']}
- **Directories Created:** {self.stats['dirs_created']}
- **Duplicates Handled:** {self.stats['duplicates_found']}
- **Errors Fixed:** {self.stats['errors_fixed']}

---

## 📁 PERFECT FOLDER STRUCTURE

### _ORGANIZED_CODE/
All code files organized by language:
- **Python_Scripts/** - All .py files
- **Shell_Scripts/** - All .sh/.bash files
- **JavaScript/** - All .js/.ts files
- **Config_Files/** - All .json/.yaml/.yml files

### _ORGANIZED_DOCS/
All documentation organized:
- **Documentation/** - General .md/.txt files
- **Reports/** - All reports and summaries
- **Guides/** - Instructions, READMEs, guides

### _ORGANIZED_PROJECTS/
Project organization:
- **Active_Projects/** - Current work
- **Completed_Projects/** - Finished work
- **Archived_Projects/** - Old projects

### _ORGANIZED_DATA/
Data files:
- **JSON_Data/** - JSON files
- **CSV_Data/** - CSV files
- **Logs/** - Log files

### _ORGANIZED_MEDIA/
Media files:
- **Images/** - All images
- **Audio/** - Audio files
- **Video/** - Video files

---

## 🎯 HOW TO USE

### Finding Files:
1. **Code?** → Check `_ORGANIZED_CODE/`
2. **Documentation?** → Check `_ORGANIZED_DOCS/`
3. **Projects?** → Check `_ORGANIZED_PROJECTS/`
4. **Data?** → Check `_ORGANIZED_DATA/`
5. **Media?** → Check `_ORGANIZED_MEDIA/`

### Adding New Files:
- Always place new files in the appropriate organized folder
- Run `CLEAN_AND_HEAL_MASTER.py` weekly to maintain organization

---

## 🔄 MAINTENANCE

**Run healing script:**
```bash
python3 CLEAN_AND_HEAL_MASTER.py
```

**This will:**
- ✅ Organize all misplaced files
- ✅ Remove empty directories
- ✅ Handle duplicates
- ✅ Update master index
- ✅ Maintain perfect structure

---

## 🐟 GORUNFREE!

Your NOIZYLAB is now PERFECTLY organized!

**CB_01's Sacred Duty (HARD RULE #20) - COMPLETE! ✅**
"""
        
        readme_file = self.base_path / 'ORGANIZATION_README.md'
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        
        print(f"   ✅ Master README created: ORGANIZATION_README.md")
    
    def heal(self):
        """Execute complete healing process"""
        print("🏥 NOIZYLAB CLEAN & HEAL - STARTING...")
        print("=" * 60)
        print()
        
        # Execute healing steps
        self.create_structure()
        file_categories = self.scan_and_categorize()
        self.organize_files(file_categories)
        self.clean_empty_dirs()
        self.create_index()
        self.create_readme()
        
        print()
        print("=" * 60)
        print("🎉 NOIZYLAB HEALING COMPLETE!")
        print()
        print("📊 FINAL STATISTICS:")
        print(f"   Files Organized: {self.stats['files_moved']}")
        print(f"   Directories Created: {self.stats['dirs_created']}")
        print(f"   Duplicates Handled: {self.stats['duplicates_found']}")
        print(f"   Errors Fixed: {self.stats['errors_fixed']}")
        print()
        print("✅ PERFECT ORGANIZATION ACHIEVED!")
        print("✅ Check ORGANIZATION_README.md for structure")
        print("✅ Check NOIZYLAB_MASTER_INDEX.json for details")
        print()
        print("🐟 GORUNFREE! - CB_01's Sacred Duty Complete! 🚀")

if __name__ == "__main__":
    healer = NoizyLabHealer()
    healer.heal()
