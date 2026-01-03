#!/usr/bin/env python3
"""
_ORGANIZED Directory Analyzer
Analyzes, catalogs, and optimizes the _ORGANIZED directory
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import subprocess

ORGANIZED = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED")
CATALOG_FILE = ORGANIZED / ".catalog.json"

class OrganizedAnalyzer:
    def __init__(self):
        self.organized = ORGANIZED
        self.catalog = {}
        self.stats = {
            'total_projects': 0,
            'total_files': 0,
            'total_size': 0,
            'categories': defaultdict(int),
            'file_types': defaultdict(int),
            'projects': {}
        }
    
    def analyze_directory(self):
        """Analyze the entire _ORGANIZED directory"""
        print("🔍 Analyzing _ORGANIZED directory...")
        print("=" * 80)
        
        if not self.organized.exists():
            print(f"❌ Directory not found: {self.organized}")
            return
        
        # Analyze each category directory
        for item in sorted(self.organized.iterdir()):
            if item.is_dir() and not item.name.startswith('.'):
                self.analyze_category(item)
            elif item.is_file() and item.suffix.lower() == '.json':
                continue  # Skip catalog files
        
        # Generate catalog
        self.generate_catalog()
        
        # Print summary
        self.print_summary()
    
    def analyze_category(self, category_path):
        """Analyze a category directory"""
        category_name = category_path.name
        print(f"\n📁 Category: {category_name}")
        print("-" * 80)
        
        projects = []
        category_stats = {
            'projects': 0,
            'files': 0,
            'size': 0
        }
        
        # Find projects in this category
        for item in category_path.iterdir():
            if item.is_dir():
                project_info = self.analyze_project(item)
                if project_info:
                    projects.append(project_info)
                    category_stats['projects'] += 1
                    category_stats['files'] += project_info['file_count']
                    category_stats['size'] += project_info['size']
        
        # Update stats
        self.stats['categories'][category_name] = category_stats
        self.stats['total_projects'] += category_stats['projects']
        
        print(f"  Projects: {category_stats['projects']}")
        print(f"  Files: {category_stats['files']:,}")
        print(f"  Size: {self.format_size(category_stats['size'])}")
        
        # Store projects
        for project in projects:
            project['category'] = category_name
            self.stats['projects'][project['name']] = project
    
    def analyze_project(self, project_path):
        """Analyze a single project directory"""
        project_name = project_path.name
        
        # Skip system directories
        if project_name.startswith('.') or project_name in ['node_modules', '__pycache__', '.git']:
            return None
        
        file_count = 0
        total_size = 0
        file_types = defaultdict(int)
        
        # Count files and sizes
        try:
            for root, dirs, files in os.walk(project_path):
                # Skip common exclude dirs
                dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', '.venv', 'venv']]
                
                for file in files:
                    file_path = Path(root) / file
                    try:
                        size = file_path.stat().st_size
                        total_size += size
                        file_count += 1
                        
                        ext = file_path.suffix.lower()
                        if ext:
                            file_types[ext] += 1
                            self.stats['file_types'][ext] += 1
                    except:
                        pass
        except:
            return None
        
        return {
            'name': project_name,
            'path': str(project_path.relative_to(self.organized)),
            'file_count': file_count,
            'size': total_size,
            'file_types': dict(file_types),
            'main_language': self.detect_language(file_types)
        }
    
    def detect_language(self, file_types):
        """Detect main programming language from file types"""
        language_scores = {
            'Python': file_types.get('.py', 0),
            'JavaScript': file_types.get('.js', 0) + file_types.get('.jsx', 0) + file_types.get('.ts', 0),
            'Ruby': file_types.get('.rb', 0),
            'Rust': file_types.get('.rs', 0),
            'Go': file_types.get('.go', 0),
            'Java': file_types.get('.java', 0),
            'C++': file_types.get('.cpp', 0) + file_types.get('.cxx', 0),
            'C': file_types.get('.c', 0),
            'Swift': file_types.get('.swift', 0),
            'Kotlin': file_types.get('.kt', 0),
            'PHP': file_types.get('.php', 0),
        }
        
        if not language_scores or max(language_scores.values()) == 0:
            return 'Unknown'
        
        return max(language_scores, key=language_scores.get)
    
    def format_size(self, bytes_size):
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.2f} PB"
    
    def generate_catalog(self):
        """Generate catalog JSON file"""
        catalog = {
            'timestamp': datetime.now().isoformat(),
            'organized_path': str(self.organized),
            'statistics': {
                'total_projects': self.stats['total_projects'],
                'total_categories': len(self.stats['categories']),
                'categories': dict(self.stats['categories'])
            },
            'projects': {}
        }
        
        # Add project details
        for project_name, project_info in self.stats['projects'].items():
            catalog['projects'][project_name] = {
                'category': project_info['category'],
                'path': project_info['path'],
                'file_count': project_info['file_count'],
                'size': project_info['size'],
                'size_formatted': self.format_size(project_info['size']),
                'main_language': project_info['main_language'],
                'file_types': project_info['file_types']
            }
        
        # Save catalog
        with open(CATALOG_FILE, 'w') as f:
            json.dump(catalog, f, indent=2)
        
        print(f"\n💾 Catalog saved: {CATALOG_FILE}")
    
    def print_summary(self):
        """Print analysis summary"""
        print("\n" + "=" * 80)
        print("📊 ANALYSIS SUMMARY")
        print("=" * 80)
        
        print(f"\n📁 Total Projects: {self.stats['total_projects']:,}")
        print(f"📂 Categories: {len(self.stats['categories'])}")
        
        # Top categories by project count
        print("\n🏆 Top Categories by Project Count:")
        sorted_cats = sorted(
            self.stats['categories'].items(),
            key=lambda x: x[1]['projects'],
            reverse=True
        )
        for i, (cat, stats) in enumerate(sorted_cats[:10], 1):
            print(f"  {i:2}. {cat:30s} - {stats['projects']:3d} projects, {self.format_size(stats['size'])}")
        
        # Top file types
        print("\n📄 Top File Types:")
        sorted_types = sorted(
            self.stats['file_types'].items(),
            key=lambda x: x[1],
            reverse=True
        )
        for i, (ext, count) in enumerate(sorted_types[:15], 1):
            print(f"  {i:2}. {ext:10s} - {count:8,} files")
        
        print("\n" + "=" * 80)

def main():
    print("=" * 80)
    print(" " * 20 + "_ORGANIZED DIRECTORY ANALYZER")
    print("=" * 80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    analyzer = OrganizedAnalyzer()
    analyzer.analyze_directory()
    
    print(f"\n✅ Analysis complete!")
    print(f"Catalog: {CATALOG_FILE}")

if __name__ == "__main__":
    main()

