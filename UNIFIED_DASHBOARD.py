#!/usr/bin/env python3
"""
Unified Dashboard
Single view of NOIZYLAB and _ORGANIZED status
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict

NOIZYLAB = Path("/Users/m2ultra/NOIZYLAB")
ORGANIZED = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED")

class UnifiedDashboard:
    def __init__(self):
        self.noizylab = NOIZYLAB
        self.organized = ORGANIZED
    
    def get_noizylab_stats(self):
        """Get NOIZYLAB statistics"""
        stats = {
            'exists': self.noizylab.exists(),
            'projects': 0,
            'size': 0,
            'categories': {}
        }
        
        if not stats['exists']:
            return stats
        
        projects = []
        for item in self.noizylab.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                if item.name not in ['scripts', 'docs', 'logs', 'backups', 'node_modules']:
                    projects.append(item.name)
                    
                    # Estimate size (sample)
                    try:
                        # Collect files once to avoid double traversal
                        all_items = list(item.rglob('*'))
                        file_count = sum(1 for f in all_items if f.is_file())
                        
                        # Only calculate size if reasonable number of files
                        if file_count < 1000:
                            size = sum(f.stat().st_size for f in all_items if f.is_file())
                            stats['size'] += size
                    except:
                        pass
        
        stats['projects'] = len(projects)
        return stats
    
    def get_organized_stats(self):
        """Get _ORGANIZED statistics"""
        stats = {
            'exists': self.organized.exists(),
            'categories': 0,
            'projects': 0,
            'catalog_exists': False
        }
        
        if not stats['exists']:
            return stats
        
        # Load catalog if available
        catalog_file = self.organized / ".catalog.json"
        if catalog_file.exists():
            try:
                with open(catalog_file) as f:
                    catalog = json.load(f)
                    stats['catalog_exists'] = True
                    stats['projects'] = catalog.get('statistics', {}).get('total_projects', 0)
                    stats['categories'] = catalog.get('statistics', {}).get('total_categories', 0)
                    return stats
            except:
                pass
        
        # Count manually
        categories = []
        for item in self.organized.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                categories.append(item.name)
                for project in item.iterdir():
                    if project.is_dir():
                        stats['projects'] += 1
        
        stats['categories'] = len(categories)
        return stats
    
    def get_system_stats(self):
        """Get system statistics"""
        stats = {
            'disk_usage': None,
            'agents_running': False
        }
        
        # Check disk usage
        try:
            result = subprocess.run(['df', '-h', str(self.noizylab.parent)],
                                  capture_output=True, text=True)
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                parts = lines[1].split()
                if len(parts) >= 5:
                    stats['disk_usage'] = int(parts[4].rstrip('%'))
        except:
            pass
        
        # Check for running agents
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            stats['agents_running'] = 'gabriel' in result.stdout.lower() or 'mc96' in result.stdout.lower()
        except:
            pass
        
        return stats
    
    def display_dashboard(self):
        """Display unified dashboard"""
        print("\n" + "=" * 80)
        print(" " * 25 + "UNIFIED DASHBOARD")
        print("=" * 80)
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # NOIZYLAB Status
        print("📁 NOIZYLAB")
        print("-" * 80)
        noizylab_stats = self.get_noizylab_stats()
        
        if noizylab_stats['exists']:
            print(f"  Status: ✅ Active")
            print(f"  Projects: {noizylab_stats['projects']}")
            size_gb = noizylab_stats['size'] / (1024**3)
            print(f"  Size: {size_gb:.2f} GB (estimated)")
        else:
            print(f"  Status: ❌ Not found")
        
        # _ORGANIZED Status
        print("\n📁 _ORGANIZED")
        print("-" * 80)
        organized_stats = self.get_organized_stats()
        
        if organized_stats['exists']:
            print(f"  Status: ✅ Active")
            print(f"  Categories: {organized_stats['categories']}")
            print(f"  Projects: {organized_stats['projects']}")
            if organized_stats['catalog_exists']:
                print(f"  Catalog: ✅ Available")
            else:
                print(f"  Catalog: ⚠️  Not generated")
        else:
            print(f"  Status: ❌ Not found")
        
        # System Status
        print("\n💻 System")
        print("-" * 80)
        system_stats = self.get_system_stats()
        
        if system_stats['disk_usage'] is not None:
            usage = system_stats['disk_usage']
            status = "✅" if usage < 75 else "⚠️" if usage < 90 else "🚨"
            print(f"  Disk Usage: {status} {usage}%")
        
        if system_stats['agents_running']:
            print(f"  Agents: 🟢 Running")
        else:
            print(f"  Agents: ⚪ Not running")
        
        # Quick Actions
        print("\n⚡ Quick Actions")
        print("-" * 80)
        print("  1. Run health check:     python3 HEALTH_MONITOR.py")
        print("  2. Analyze NOIZYLAB:     python3 CHECK_AGENTS.py")
        print("  3. Analyze _ORGANIZED:   cd \"$ORGANIZED\" && python3 ANALYZE_ORGANIZED.py")
        print("  4. Run automation:       python3 ADVANCED_AUTOMATION.py status")
        print("  5. Open NOIZYLAB:        cd /Users/m2ultra/NOIZYLAB && ./GO.sh")
        print("  6. Open _ORGANIZED:      cd \"$ORGANIZED\" && ./ORGANIZED_MANAGER.sh")
        
        print("\n" + "=" * 80)
    
    def generate_json_report(self):
        """Generate JSON report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'noizylab': self.get_noizylab_stats(),
            'organized': self.get_organized_stats(),
            'system': self.get_system_stats()
        }
        
        report_file = self.noizylab / 'logs' / f'dashboard-{datetime.now().strftime("%Y%m%d-%H%M%S")}.json'
        report_file.parent.mkdir(exist_ok=True)
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        return report_file

def main():
    dashboard = UnifiedDashboard()
    dashboard.display_dashboard()
    
    import sys
    if '--json' in sys.argv:
        report_file = dashboard.generate_json_report()
        print(f"\n💾 JSON report saved: {report_file}")

if __name__ == "__main__":
    main()

