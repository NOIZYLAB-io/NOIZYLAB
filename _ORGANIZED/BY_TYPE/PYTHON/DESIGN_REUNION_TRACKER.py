#!/usr/bin/env python3
"""
DESIGN REUNION SHOW - PROJECT TRACKER
CRITICAL PROJECT: Complete mix for Gavin Lumsden (Rogers)
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

class DesignReunionTracker:
    """Track Design Reunion Show completion - HIGHEST PRIORITY"""
    
    def __init__(self):
        self.project_path = Path('/Users/m2ultra/CB-01-FISHMUSICINC/projects/design-reunion')
        self.stems_path = Path('/Volumes/4TB Lacie')  # Design 2025 stems location
        
        self.project_info = {
            'name': 'Design Reunion Show',
            'client': 'Gavin Lumsden (Rogers)',
            'client_email': 'gavin@rogers.com',
            'client_organization': 'Rogers Media',
            'priority': 'HIGHEST',
            'status': 'IN_PROGRESS',
            'description': 'Live show recording filmed by Gavin Lumsden with Rogers crew. ROB owes Gavin completion of this mix - CRITICAL personal commitment.',
            'stems_location': str(self.stems_path / 'Design 2025') if self.stems_path.exists() else 'NOT FOUND',
            'stems_accessible': self.stems_path.exists()
        }
        
        self.workflow = {
            'phase_1_locate_stems': {
                'name': 'Locate Design 2025 Stems',
                'tasks': [
                    {'task': 'Find 4TB Lacie drive', 'status': 'complete' if self.stems_path.exists() else 'pending'},
                    {'task': 'Verify Design 2025 folder exists', 'status': 'pending'},
                    {'task': 'Count stem files', 'status': 'pending'},
                    {'task': 'Verify file integrity', 'status': 'pending'}
                ],
                'status': 'in_progress' if self.stems_path.exists() else 'pending'
            },
            'phase_2_organize': {
                'name': 'Organize & Import Stems',
                'tasks': [
                    {'task': 'Create project folder structure', 'status': 'pending'},
                    {'task': 'Import stems to working directory', 'status': 'pending'},
                    {'task': 'Back up original stems', 'status': 'pending'},
                    {'task': 'Verify all tracks present', 'status': 'pending'}
                ],
                'status': 'pending'
            },
            'phase_3_mix': {
                'name': 'Complete Mix',
                'tasks': [
                    {'task': 'Load stems into DAW', 'status': 'pending'},
                    {'task': 'Balance & rough mix', 'status': 'pending'},
                    {'task': 'Process & effects', 'status': 'pending'},
                    {'task': 'Fine-tune mix', 'status': 'pending'},
                    {'task': 'Reference check', 'status': 'pending'},
                    {'task': 'Final mix approval', 'status': 'pending'}
                ],
                'status': 'pending'
            },
            'phase_4_master': {
                'name': 'Mastering',
                'tasks': [
                    {'task': 'Export stereo mixdown', 'status': 'pending'},
                    {'task': 'Master for video sync', 'status': 'pending'},
                    {'task': 'Quality check', 'status': 'pending'},
                    {'task': 'Backup master files', 'status': 'pending'}
                ],
                'status': 'pending'
            },
            'phase_5_delivery': {
                'name': 'Deliver to Gavin/Rogers',
                'tasks': [
                    {'task': 'Export final masters (WAV/MP3)', 'status': 'pending'},
                    {'task': 'Sync with Rogers video', 'status': 'pending'},
                    {'task': 'Send to Gavin Lumsden', 'status': 'pending'},
                    {'task': 'Get approval', 'status': 'pending'},
                    {'task': 'Archive project', 'status': 'pending'}
                ],
                'status': 'pending'
            }
        }
    
    def find_stems(self) -> Dict:
        """Find Design 2025 stems on 4TB Lacie"""
        print("\n🔍 SEARCHING FOR DESIGN 2025 STEMS...")
        print("=" * 70)
        
        results = {
            'drive_found': self.stems_path.exists(),
            'drive_path': str(self.stems_path),
            'design_folders': [],
            'total_stems': 0
        }
        
        if not results['drive_found']:
            print(f"   ❌ 4TB Lacie not found at: {self.stems_path}")
            print(f"   💡 Mount the drive and run again")
            return results
        
        print(f"   ✅ 4TB Lacie found at: {self.stems_path}")
        
        # Search for Design-related folders
        try:
            for item in self.stems_path.iterdir():
                if item.is_dir():
                    name_lower = item.name.lower()
                    if any(keyword in name_lower for keyword in ['design', '2025', 'reunion']):
                        results['design_folders'].append({
                            'name': item.name,
                            'path': str(item)
                        })
                        print(f"   ✨ Found: {item.name}")
        except PermissionError:
            print(f"   ⚠️  Permission denied accessing drive")
        
        print(f"\n   Found {len(results['design_folders'])} Design-related folder(s)")
        
        return results
    
    def print_project_status(self):
        """Print complete project status"""
        print("\n" + "═" * 70)
        print("🔥 DESIGN REUNION SHOW - PROJECT STATUS")
        print("═" * 70)
        print(f"\n⭐ PRIORITY: {self.project_info['priority']}")
        print(f"📊 STATUS: {self.project_info['status']}")
        print(f"\n👤 CLIENT: {self.project_info['client']}")
        print(f"   Organization: {self.project_info['client_organization']}")
        print(f"   Email: {self.project_info['client_email']}")
        
        print(f"\n📝 DESCRIPTION:")
        print(f"   {self.project_info['description']}")
        
        print(f"\n💾 STEMS LOCATION:")
        if self.project_info['stems_accessible']:
            print(f"   ✅ {self.project_info['stems_location']}")
        else:
            print(f"   ❌ 4TB Lacie not mounted - mount drive to access stems")
        
        print(f"\n📋 WORKFLOW PROGRESS:")
        
        total_tasks = 0
        completed_tasks = 0
        
        for phase_id, phase in self.workflow.items():
            print(f"\n   {phase['name'].upper()}:")
            
            phase_complete = 0
            for task in phase['tasks']:
                total_tasks += 1
                status_icon = "✅" if task['status'] == 'complete' else "⏳" if task['status'] == 'in_progress' else "☐"
                print(f"      {status_icon} {task['task']}")
                if task['status'] == 'complete':
                    phase_complete += 1
                    completed_tasks += 1
            
            phase_pct = round(phase_complete / len(phase['tasks']) * 100) if phase['tasks'] else 0
            print(f"      Progress: {phase_complete}/{len(phase['tasks'])} ({phase_pct}%)")
        
        overall_pct = round(completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        print(f"\n🎯 OVERALL PROGRESS: {completed_tasks}/{total_tasks} tasks ({overall_pct}%)")
        
        print("\n" + "═" * 70)
        print("💡 NEXT STEPS:")
        print("   1. Mount 4TB Lacie drive")
        print("   2. Locate Design 2025 stems folder")
        print("   3. Verify all stem files present")
        print("   4. Import into DAW and start mixing!")
        print("=" * 70)
        print("\nGORUNFREE! 🎸🔥")
    
    def save_project_status(self):
        """Save project status to JSON"""
        output_file = self.project_path / 'design_reunion_status.json'
        
        data = {
            'project_info': self.project_info,
            'workflow': self.workflow,
            'last_updated': datetime.now().isoformat()
        }
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\n💾 Project status saved to: {output_file}")

def main():
    """Main execution"""
    print("\n🔥 DESIGN REUNION SHOW - GAVIN LUMSDEN / ROGERS")
    print("=" * 70)
    print("HIGHEST PRIORITY PROJECT - Personal commitment to complete!")
    print("=" * 70)
    
    tracker = DesignReunionTracker()
    
    # Find stems
    stems_results = tracker.find_stems()
    
    # Show project status
    tracker.print_project_status()
    
    # Save status
    tracker.save_project_status()

if __name__ == '__main__':
    main()

