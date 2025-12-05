#!/usr/bin/env python3
"""
FISH MUSIC INC - INTELLIGENT PROJECT FINDER
Find any project, client work, or music instantly
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import os
import subprocess
from pathlib import Path
from typing import List, Dict

class ProjectFinder:
    """Find any project across all volumes instantly"""

    def __init__(self):
        self.volumes_path = Path('/Volumes')
        self.search_keywords = {
            'clients': ['fuel', 'mcdonald', 'microsoft', 'tinker', 'deadwood', 'design', 'gavin', 'rogers'],
            'music': ['music', 'audio', 'wav', 'aif', 'mp3', 'stems', 'session', 'mix', 'master'],
            'projects': ['project', 'client', 'commercial', 'work']
        }

    def smart_search(self, query: str) -> List[Dict]:
        """Smart search across all volumes"""
        print(f"\n🔍 SMART SEARCH: '{query}'")
        print("=" * 70)
        print("Searching across all volumes...")

        results = []
        search_paths = []

        # Add local paths
        search_paths.append(Path('/Users/m2ultra/CB-01-FISHMUSICINC'))

        # Add all volumes
        if self.volumes_path.exists():
            for vol in self.volumes_path.iterdir():
                if vol.is_dir() and not vol.is_symlink():
                    if vol.name not in ['Macintosh HD', 'M2Ultra']:
                        search_paths.append(vol)

        # Search each path
        for path in search_paths:
            try:
                # Search directories
                result = subprocess.run(
                    ['find', str(path), '-maxdepth', '3', '-type', 'd',
                     '-iname', f'*{query}*'],
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                if result.returncode == 0 and result.stdout.strip():
                    for line in result.stdout.strip().split('\n'):
                        if line:
                            results.append({
                                'path': line,
                                'type': 'directory',
                                'location': path.name if path != Path('/Users/m2ultra/CB-01-FISHMUSICINC') else 'CB-01'
                            })
            except:
                pass

        return results

    def find_client_work(self, client: str) -> List[str]:
        """Find specific client work"""
        print(f"\n🏢 FINDING: {client.upper()} CLIENT WORK")
        print("=" * 70)

        found = []

        # Search all volumes
        if self.volumes_path.exists():
            for vol in self.volumes_path.iterdir():
                if vol.is_dir():
                    try:
                        result = subprocess.run(
                            ['find', str(vol), '-maxdepth', '4', '-type', 'd',
                             '-iname', f'*{client}*'],
                            capture_output=True,
                            text=True,
                            timeout=45
                        )

                        if result.returncode == 0:
                            for line in result.stdout.strip().split('\n'):
                                if line:
                                    found.append(line)
                                    print(f"   ✅ {line}")
                    except:
                        pass

        print(f"\n   Found {len(found)} location(s) for {client}!")
        return found

    def find_design_reunion_stems(self) -> Dict:
        """Specifically find Design Reunion stems"""
        print("\n🎬 FINDING DESIGN REUNION STEMS...")
        print("=" * 70)

        # Check 4TB Lacie
        lacie = Path('/Volumes/4TB Lacie')

        if not lacie.exists():
            print("   ❌ 4TB Lacie not mounted")
            return {'found': False, 'message': 'Mount 4TB Lacie drive'}

        print(f"   ✅ 4TB Lacie mounted")

        # Find Design folders
        design_folders = []
        try:
            for item in lacie.iterdir():
                if item.is_dir():
                    if any(keyword in item.name.lower() for keyword in ['design', '2025', 'reunion']):
                        design_folders.append(str(item))
                        print(f"   ✨ {item.name}")

                        # Count files
                        try:
                            result = subprocess.run(
                                ['find', str(item), '-type', 'f', '-name', '*.aif*'],
                                capture_output=True,
                                text=True,
                                timeout=30
                            )
                            if result.returncode == 0:
                                count = len([l for l in result.stdout.strip().split('\n') if l])
                                print(f"      → {count} AIFF files")
                        except:
                            pass
        except:
            pass

        return {
            'found': len(design_folders) > 0,
            'locations': design_folders,
            'count': len(design_folders)
        }

def main():
    """Main execution"""
    import sys

    print("\n🔍 FISH MUSIC INC - INTELLIGENT PROJECT FINDER")
    print("=" * 70)

    finder = ProjectFinder()

    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python3 project_finder.py search <term>")
        print("  python3 project_finder.py client <fuel|mcdonalds|microsoft|deadwood>")
        print("  python3 project_finder.py design")
        return

    command = sys.argv[1]

    if command == 'search' and len(sys.argv) > 2:
        query = sys.argv[2]
        results = finder.smart_search(query)

        if results:
            print(f"\n✅ Found {len(results)} result(s):")
            for r in results[:20]:
                print(f"   [{r['location']}] {r['path']}")

    elif command == 'client' and len(sys.argv) > 2:
        client = sys.argv[2]
        finder.find_client_work(client)

    elif command == 'design':
        finder.find_design_reunion_stems()

if __name__ == '__main__':
    main()

