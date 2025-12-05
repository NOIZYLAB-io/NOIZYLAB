#!/usr/bin/env python3
"""
⚡ ULTRA FAST CODE SCANNER ⚡
============================
Scans ALL volumes for code files at LIGHTNING SPEED!
CURSE_BEAST_01 + CURSE_BEAST_02 working together!
"""

import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from typing import List, Dict, Set


class UltraFastCodeScanner:
    """Lightning-fast multi-threaded code scanner"""
    
    def __init__(self):
        # Code extensions to find
        self.code_extensions = {
            '.py', '.js', '.ts', '.tsx', '.jsx',
            '.go', '.rs', '.cpp', '.c', '.h',
            '.java', '.rb', '.php', '.swift',
            '.sh', '.bash', '.zsh'
        }
        
        # Approved locations (ONLY these!)
        self.approved_locations = {
            Path("/Users/m2ultra/NOIZYLAB"),
            Path("/Users/m2ultra/Github/Noizyfish/NOIZYLAB")
        }
        
        # Volumes to scan
        self.scan_volumes = [
            "/Volumes/SIDNEY",
            "/Volumes/MAG 4TB",
            "/Volumes/6TB",
            "/Volumes/4TBSG",
            "/Volumes/4TB Lacie",
            "/Volumes/_CLAUDE_NEEDS"
        ]
        
        self.files_found = []
        self.total_scanned = 0
        
    def ultra_scan(self, directories: List[str] = None) -> Dict:
        """⚡⚡⚡ ULTRA FAST PARALLEL SCAN! ⚡⚡⚡"""
        
        print("\n⚡⚡⚡ ULTRA FAST CODE SCANNER - CURSE_BEAST MODE! ⚡⚡⚡")
        print("="*70)
        
        if directories is None:
            # Scan all volumes + home
            directories = self.scan_volumes.copy()
            directories.append("/Users/m2ultra")
        
        # Filter existing directories
        existing_dirs = [Path(d) for d in directories if Path(d).exists()]
        
        print(f"\n🔍 Scanning {len(existing_dirs)} locations...")
        for d in existing_dirs:
            print(f"  📂 {d}")
        
        start_time = time.time()
        
        # Parallel scan
        code_files = []
        
        def scan_single_dir(directory):
            """Scan single directory"""
            local_files = []
            try:
                for root, dirs, files in os.walk(directory):
                    # Skip system directories
                    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in 
                              {'node_modules', '__pycache__', 'venv', 'env', '.git'}]
                    
                    for file in files:
                        if any(file.endswith(ext) for ext in self.code_extensions):
                            file_path = Path(root) / file
                            local_files.append(file_path)
                            
                            if len(local_files) % 1000 == 0:
                                print(f"  ⚡ Found {len(local_files)} files in {directory}...")
            except Exception as e:
                pass
            
            return local_files
        
        # Parallel execution
        with ThreadPoolExecutor(max_workers=len(existing_dirs)) as executor:
            futures = {executor.submit(scan_single_dir, str(d)): d for d in existing_dirs}
            
            for future in as_completed(futures):
                directory = futures[future]
                try:
                    files = future.result()
                    code_files.extend(files)
                    print(f"  ✅ {directory}: {len(files)} code files")
                except Exception as e:
                    print(f"  ⚠️  {directory}: Error - {e}")
        
        elapsed = time.time() - start_time
        
        # Categorize files
        approved = []
        unauthorized = []
        
        for file_path in code_files:
            is_approved = any(
                str(file_path).startswith(str(approved_loc)) 
                for approved_loc in self.approved_locations
            )
            
            if is_approved:
                approved.append(file_path)
            else:
                unauthorized.append(file_path)
        
        print(f"\n{'='*70}")
        print(f"⚡ ULTRA SCAN COMPLETE!")
        print(f"{'='*70}")
        print(f"  Total files found: {len(code_files):,}")
        print(f"  Scan time: {elapsed:.2f}s")
        print(f"  Speed: {len(code_files)/elapsed:,.0f} files/sec!")
        print(f"\n📊 Results:")
        print(f"  ✅ Approved locations: {len(approved):,} files")
        print(f"  ⚠️  Unauthorized locations: {len(unauthorized):,} files")
        
        # Show unauthorized locations summary
        if unauthorized:
            print(f"\n⚠️  CODE IN UNAUTHORIZED LOCATIONS:")
            
            # Group by volume
            by_volume = {}
            for file_path in unauthorized:
                volume = str(file_path).split('/')[0:3]
                volume_name = '/'.join(volume)
                by_volume[volume_name] = by_volume.get(volume_name, 0) + 1
            
            for volume, count in sorted(by_volume.items(), key=lambda x: x[1], reverse=True):
                print(f"  📂 {volume}: {count:,} files")
        
        return {
            'total': len(code_files),
            'approved': len(approved),
            'unauthorized': len(unauthorized),
            'unauthorized_files': unauthorized[:100],  # First 100
            'elapsed': elapsed,
            'speed_fps': len(code_files)/elapsed if elapsed > 0 else 0
        }
    
    def generate_cleanup_report(self, scan_result: Dict):
        """Generate cleanup report"""
        
        report_file = Path("/Users/m2ultra/NOIZYLAB/⚡_CODE_CLEANUP_REPORT.md")
        
        report = f"""# ⚡ CODE CLEANUP REPORT

**Generated**: {time.strftime('%Y-%m-%d %H:%M:%S')}
**Scanner**: CURSE_BEAST_01 + CURSE_BEAST_02

---

## 📊 SCAN RESULTS

- **Total code files found**: {scan_result['total']:,}
- **Approved locations**: {scan_result['approved']:,} files ✅
- **Unauthorized locations**: {scan_result['unauthorized']:,} files ⚠️
- **Scan speed**: {scan_result['speed_fps']:,.0f} files/second ⚡

---

## ✅ APPROVED LOCATIONS (Keep!)

1. `/Users/m2ultra/NOIZYLAB` ✅
2. `/Users/m2ultra/Github/Noizyfish/NOIZYLAB` ✅

---

## ⚠️ UNAUTHORIZED LOCATIONS (Review!)

Files found outside approved locations: {scan_result['unauthorized']:,}

### Sample files to review:
"""
        
        for i, file_path in enumerate(scan_result['unauthorized_files'][:50], 1):
            report += f"\n{i}. `{file_path}`"
        
        report += f"""

---

## 🎯 NEXT STEPS

1. **Review** unauthorized files
2. **Move** important code to approved locations
3. **Delete** duplicates and unused code
4. **Verify** nothing critical in unauthorized locations
5. **Clean up** once verified!

---

**Generated by CURSE_BEAST_01 at LIGHTNING SPEED!** ⚡
"""
        
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"\n📄 Cleanup report saved: {report_file}")
        
        return report_file


if __name__ == "__main__":
    print("⚡⚡⚡ ULTRA FAST CODE SCANNER ⚡⚡⚡")
    print("CURSE_BEAST_01 + CURSE_BEAST_02")
    print()
    
    scanner = UltraFastCodeScanner()
    
    # ULTRA SCAN!
    result = scanner.ultra_scan()
    
    # Generate report
    report = scanner.generate_cleanup_report(result)
    
    print(f"\n✅ ULTRA SCAN COMPLETE!")
    print(f"📄 Review report: {report}")

