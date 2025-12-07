#!/usr/bin/env python3
"""
Project Health Monitor
Comprehensive health checks for all projects
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

NOIZYLAB = Path("/Users/m2ultra/NOIZYLAB")

class HealthMonitor:
    def __init__(self):
        self.noizylab = NOIZYLAB
        self.issues = []
        self.warnings = []
        self.recommendations = []
        self.stats = {}
    
    def check_disk_space(self):
        """Check available disk space"""
        print("💾 Checking disk space...")
        
        try:
            result = subprocess.run(['df', '-h', str(self.noizylab)],
                                  capture_output=True, text=True)
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                parts = lines[1].split()
                if len(parts) >= 5:
                    usage = int(parts[4].rstrip('%'))
                    
                    self.stats['disk_usage'] = usage
                    
                    if usage > 90:
                        self.issues.append(f"🚨 Disk usage critical: {usage}%")
                    elif usage > 75:
                        self.warnings.append(f"⚠️  Disk usage high: {usage}%")
                    else:
                        print(f"  ✅ Disk usage: {usage}%")
        except:
            self.warnings.append("⚠️  Could not check disk space")
    
    def check_large_files(self, threshold_mb=100):
        """Find large files"""
        print(f"📊 Checking for large files (>={threshold_mb}MB)...")
        
        large_files = []
        threshold = threshold_mb * 1024 * 1024
        
        for root, dirs, files in os.walk(self.noizylab):
            # Skip common large directories
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', 'venv', '.venv']]
            
            for file in files:
                file_path = Path(root) / file
                try:
                    size = file_path.stat().st_size
                    if size >= threshold:
                        large_files.append({
                            'path': str(file_path.relative_to(self.noizylab)),
                            'size': size
                        })
                except:
                    pass
        
        if large_files:
            large_files.sort(key=lambda x: x['size'], reverse=True)
            self.stats['large_files'] = len(large_files)
            
            print(f"  ⚠️  Found {len(large_files)} large files")
            
            if len(large_files) > 10:
                self.warnings.append(f"⚠️  {len(large_files)} large files found (>{threshold_mb}MB)")
                
                # Show top 5
                print("  Top 5:")
                for i, file_info in enumerate(large_files[:5], 1):
                    size_mb = file_info['size'] / (1024 * 1024)
                    print(f"    {i}. {size_mb:.1f} MB - {file_info['path']}")
                
                self.recommendations.append(
                    f"Consider archiving {len(large_files)} large files to external drive"
                )
        else:
            print("  ✅ No large files found")
    
    def check_project_health(self):
        """Check individual project health"""
        print("📦 Checking project health...")
        
        projects = []
        unhealthy = []
        
        for item in self.noizylab.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                if item.name not in ['scripts', 'docs', 'logs', 'backups', 'node_modules']:
                    projects.append(item)
        
        for project in projects:
            issues = []
            
            # Check for common issues
            has_readme = (project / 'README.md').exists()
            has_git = (project / '.git').exists()
            has_node_modules = (project / 'node_modules').exists()
            
            if not has_readme:
                issues.append("No README.md")
            
            # Check for very old modifications
            try:
                mtime = project.stat().st_mtime
                days_old = (datetime.now().timestamp() - mtime) / 86400
                
                if days_old > 90:
                    issues.append(f"Inactive ({int(days_old)} days)")
            except:
                pass
            
            if issues:
                unhealthy.append({
                    'name': project.name,
                    'issues': issues
                })
        
        self.stats['total_projects'] = len(projects)
        self.stats['unhealthy_projects'] = len(unhealthy)
        
        if unhealthy:
            print(f"  ⚠️  {len(unhealthy)} projects need attention")
            for project in unhealthy[:10]:
                print(f"    • {project['name']}: {', '.join(project['issues'])}")
        else:
            print(f"  ✅ All {len(projects)} projects look healthy")
    
    def check_duplicates(self):
        """Check for duplicate projects"""
        print("🔍 Checking for duplicates...")
        
        project_names = defaultdict(list)
        
        for item in self.noizylab.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                project_names[item.name.lower()].append(str(item))
        
        duplicates = {name: paths for name, paths in project_names.items() if len(paths) > 1}
        
        if duplicates:
            self.stats['duplicates'] = len(duplicates)
            self.warnings.append(f"⚠️  Found {len(duplicates)} duplicate project names")
            print(f"  ⚠️  Found {len(duplicates)} potential duplicates")
        else:
            print("  ✅ No duplicates found")
    
    def check_dependencies(self):
        """Check for dependency issues"""
        print("📚 Checking dependencies...")
        
        requirements_files = list(self.noizylab.rglob('requirements*.txt'))
        package_json_files = list(self.noizylab.rglob('package.json'))
        
        self.stats['requirements_files'] = len(requirements_files)
        self.stats['package_json_files'] = len(package_json_files)
        
        print(f"  📄 Found {len(requirements_files)} requirements files")
        print(f"  📦 Found {len(package_json_files)} package.json files")
        
        if len(requirements_files) > 5 or len(package_json_files) > 5:
            self.recommendations.append(
                "Consider consolidating dependencies or using a monorepo structure"
            )
    
    def generate_report(self):
        """Generate health report"""
        print("\n" + "=" * 80)
        print("📊 HEALTH REPORT")
        print("=" * 80)
        
        print("\n🚨 Critical Issues:")
        if self.issues:
            for issue in self.issues:
                print(f"  {issue}")
        else:
            print("  None ✅")
        
        print("\n⚠️  Warnings:")
        if self.warnings:
            for warning in self.warnings:
                print(f"  {warning}")
        else:
            print("  None ✅")
        
        print("\n💡 Recommendations:")
        if self.recommendations:
            for rec in self.recommendations:
                print(f"  • {rec}")
        else:
            print("  None - system looks good! ✅")
        
        print("\n📈 Statistics:")
        for key, value in self.stats.items():
            print(f"  • {key}: {value}")
        
        # Save report
        report_file = self.noizylab / 'logs' / f'health-report-{datetime.now().strftime("%Y%m%d-%H%M%S")}.json'
        report_file.parent.mkdir(exist_ok=True)
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'issues': self.issues,
            'warnings': self.warnings,
            'recommendations': self.recommendations,
            'stats': self.stats
        }
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n💾 Report saved: {report_file}")
    
    def run_full_check(self):
        """Run all health checks"""
        print("=" * 80)
        print(" " * 25 + "HEALTH MONITOR")
        print("=" * 80)
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        self.check_disk_space()
        self.check_large_files()
        self.check_project_health()
        self.check_duplicates()
        self.check_dependencies()
        
        self.generate_report()
        
        print("\n" + "=" * 80)
        print("✅ Health check complete!")
        print("=" * 80)

def main():
    monitor = HealthMonitor()
    monitor.run_full_check()

if __name__ == "__main__":
    main()

