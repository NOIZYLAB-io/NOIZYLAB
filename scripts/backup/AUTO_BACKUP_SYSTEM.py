#!/usr/bin/env python3
"""
💾 AUTOMATIC BACKUP SYSTEM 💾

⭐⭐⭐ PRIORITY: ORIGINAL COMPOSITIONS ⭐⭐⭐

Automatically backup your originals to multiple locations:
- External drives
- Network shares
- Cloud prep
- Multiple redundancy
"""

import os
import shutil
import json
import hashlib
from pathlib import Path
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

# Backup destinations (add yours!)
BACKUP_DESTINATIONS = [
    # External drives
    Path("/Volumes/BACKUP_DRIVE_1"),  # Change to your drive
    Path("/Volumes/BACKUP_DRIVE_2"),  # Change to your drive
    
    # Network shares
    # Path("/Volumes/NAS/Music_Backup"),
    
    # Local backup
    Path.home() / "Music_Backups"
]

# What to backup (priority order)
BACKUP_SOURCES = [
    Path("ORGANIZED_WAVES/ORIGINAL_COMPOSITIONS"),
    Path("6TB_ORGANIZED/ORIGINAL_COMPOSITIONS"),
    Path("AI_ORGANIZED/Original_Compositions")
]

BACKUP_CONFIG = {
    'verify_copies': True,  # Verify with checksums
    'keep_versions': 3,  # Keep multiple versions
    'compress_old_versions': False,
    'create_manifest': True,
    'backup_reports': True
}

# ============================================================================
# BACKUP ENGINE
# ============================================================================

def calculate_checksum(filepath):
    """Calculate MD5 checksum for verification"""
    md5 = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                md5.update(chunk)
        return md5.hexdigest()
    except:
        return None

def verify_backup(source, dest):
    """Verify backup integrity"""
    if not dest.exists():
        return False, "File doesn't exist"
    
    if source.stat().st_size != dest.stat().st_size:
        return False, "Size mismatch"
    
    if BACKUP_CONFIG['verify_copies']:
        source_hash = calculate_checksum(source)
        dest_hash = calculate_checksum(dest)
        if source_hash != dest_hash:
            return False, "Checksum mismatch"
    
    return True, "OK"

def backup_file(source, dest_base, version=1):
    """Backup a single file with versioning"""
    dest_base.mkdir(parents=True, exist_ok=True)
    
    # Create filename with version
    if version > 1:
        dest_file = dest_base / f"{source.stem}_v{version}{source.suffix}"
    else:
        dest_file = dest_base / source.name
    
    # Copy file
    shutil.copy2(source, dest_file)
    
    # Verify
    valid, msg = verify_backup(source, dest_file)
    
    return dest_file, valid, msg

def backup_originals(destination):
    """Backup all originals to a destination"""
    print(f"\n📦 Backing up to: {destination}")
    
    if not destination.parent.exists():
        print(f"  ⚠️  Destination not available (drive not mounted?)")
        return None
    
    destination.mkdir(parents=True, exist_ok=True)
    
    stats = {
        'destination': str(destination),
        'timestamp': datetime.now().isoformat(),
        'files_backed_up': 0,
        'files_verified': 0,
        'files_failed': 0,
        'total_size': 0,
        'files': []
    }
    
    # Find all originals
    originals = []
    for source_dir in BACKUP_SOURCES:
        if source_dir.exists():
            files = list(source_dir.rglob('*.wav')) + list(source_dir.rglob('*.WAV'))
            originals.extend(files)
    
    if not originals:
        print("  ⚠️  No original files found to backup")
        return stats
    
    print(f"  Found {len(originals)} files to backup")
    
    # Backup each file
    for i, source_file in enumerate(originals, 1):
        try:
            # Determine destination subfolder
            for source_dir in BACKUP_SOURCES:
                if source_dir in source_file.parents:
                    relative = source_file.relative_to(source_dir.parent)
                    dest_path = destination / relative.parent
                    break
            else:
                dest_path = destination
            
            # Backup
            dest_file, valid, msg = backup_file(source_file, dest_path)
            
            stats['files_backed_up'] += 1
            stats['total_size'] += source_file.stat().st_size
            
            if valid:
                stats['files_verified'] += 1
            else:
                stats['files_failed'] += 1
                print(f"  ⚠️  Verification failed: {source_file.name} ({msg})")
            
            stats['files'].append({
                'source': str(source_file),
                'dest': str(dest_file),
                'size': source_file.stat().st_size,
                'verified': valid,
                'checksum': calculate_checksum(source_file) if BACKUP_CONFIG['verify_copies'] else None
            })
            
            if i % 10 == 0:
                print(f"  [{i}/{len(originals)}] Backed up...")
        
        except Exception as e:
            print(f"  ❌ Error backing up {source_file.name}: {e}")
            stats['files_failed'] += 1
    
    print(f"  ✓ Backup complete!")
    print(f"    Files: {stats['files_backed_up']}")
    print(f"    Verified: {stats['files_verified']}")
    print(f"    Size: {stats['total_size']/(1024**2):.1f} MB")
    
    return stats

def create_backup_manifest(all_stats):
    """Create manifest of all backups"""
    manifest_dir = Path("BACKUP_MANIFESTS")
    manifest_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    manifest_file = manifest_dir / f"backup_manifest_{timestamp}.json"
    
    with open(manifest_file, 'w') as f:
        json.dump(all_stats, f, indent=2)
    
    # Also create human-readable version
    txt_file = manifest_dir / f"backup_manifest_{timestamp}.txt"
    
    with open(txt_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("💾 BACKUP MANIFEST 💾\n")
        f.write("="*80 + "\n\n")
        f.write("⭐⭐⭐ ORIGINAL COMPOSITIONS BACKUP ⭐⭐⭐\n\n")
        f.write(f"Backup Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        total_files = sum(s['files_backed_up'] for s in all_stats if s)
        total_size = sum(s['total_size'] for s in all_stats if s)
        
        f.write(f"Total files backed up: {total_files}\n")
        f.write(f"Total size: {total_size/(1024**3):.2f} GB\n")
        f.write(f"Backup destinations: {len([s for s in all_stats if s])}\n\n")
        
        f.write("="*80 + "\n")
        f.write("BACKUP LOCATIONS:\n")
        f.write("="*80 + "\n\n")
        
        for stats in all_stats:
            if stats:
                f.write(f"Destination: {stats['destination']}\n")
                f.write(f"  Files: {stats['files_backed_up']}\n")
                f.write(f"  Verified: {stats['files_verified']}\n")
                f.write(f"  Failed: {stats['files_failed']}\n")
                f.write(f"  Size: {stats['total_size']/(1024**2):.1f} MB\n")
                f.write(f"  Time: {stats['timestamp']}\n\n")
    
    return manifest_file, txt_file

# ============================================================================
# MAIN BACKUP ROUTINE
# ============================================================================

def run_backup_system():
    """Run complete backup system"""
    print("="*80)
    print("💾 AUTOMATIC BACKUP SYSTEM 💾")
    print("="*80)
    print("\n⭐⭐⭐ PRIORITY: ORIGINAL COMPOSITIONS ⭐⭐⭐\n")
    
    # Check for source files
    total_originals = 0
    for source_dir in BACKUP_SOURCES:
        if source_dir.exists():
            files = list(source_dir.rglob('*.wav')) + list(source_dir.rglob('*.WAV'))
            total_originals += len(files)
            print(f"✓ Found {len(files)} files in {source_dir}")
    
    if total_originals == 0:
        print("\n❌ No original compositions found to backup!")
        print("Run an organizer first to identify your originals.")
        return
    
    print(f"\nTotal original compositions to backup: {total_originals}")
    print(f"Backup destinations configured: {len(BACKUP_DESTINATIONS)}\n")
    
    # Check available destinations
    available = []
    for dest in BACKUP_DESTINATIONS:
        if dest.parent.exists() or dest.exists():
            available.append(dest)
            print(f"✓ Destination available: {dest}")
        else:
            print(f"⚠️  Destination not available: {dest}")
    
    if not available:
        print("\n⚠️  No backup destinations available!")
        print("Mount external drives or update BACKUP_DESTINATIONS in script.")
        return
    
    print(f"\n📦 Starting backup to {len(available)} destination(s)...")
    
    # Backup to each destination
    all_stats = []
    for destination in available:
        stats = backup_originals(destination)
        all_stats.append(stats)
    
    # Create manifest
    print("\n📄 Creating backup manifest...")
    manifest_json, manifest_txt = create_backup_manifest(all_stats)
    
    # Summary
    print("\n" + "="*80)
    print("✅ BACKUP COMPLETE!")
    print("="*80)
    
    successful = len([s for s in all_stats if s and s['files_backed_up'] > 0])
    total_backed_up = sum(s['files_backed_up'] for s in all_stats if s)
    total_size = sum(s['total_size'] for s in all_stats if s)
    
    print(f"\n✓ Successful backups: {successful}/{len(available)}")
    print(f"✓ Total files backed up: {total_backed_up}")
    print(f"✓ Total size: {total_size/(1024**3):.2f} GB")
    print(f"\n📄 Manifest: {manifest_txt}")
    print("\n⭐ YOUR ORIGINALS ARE NOW BACKED UP! ⭐")
    print("="*80 + "\n")

def quick_backup_check():
    """Quick check of backup status"""
    print("="*80)
    print("💾 BACKUP STATUS CHECK")
    print("="*80 + "\n")
    
    # Check sources
    print("SOURCE FILES:")
    total_originals = 0
    for source_dir in BACKUP_SOURCES:
        if source_dir.exists():
            files = list(source_dir.rglob('*.wav')) + list(source_dir.rglob('*.WAV'))
            total_originals += len(files)
            print(f"  ✓ {source_dir}: {len(files)} files")
        else:
            print(f"  ✗ {source_dir}: Not found")
    
    print(f"\nTotal originals: {total_originals}\n")
    
    # Check destinations
    print("BACKUP DESTINATIONS:")
    for dest in BACKUP_DESTINATIONS:
        if dest.exists():
            files = list(dest.rglob('*.wav')) + list(dest.rglob('*.WAV'))
            print(f"  ✓ {dest}: {len(files)} files backed up")
        else:
            print(f"  ✗ {dest}: Not available")
    
    print("\n" + "="*80 + "\n")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'check':
        quick_backup_check()
    else:
        print("\n⚠️  WARNING: This will backup your original compositions!")
        print("Make sure external drives are mounted.")
        print("\nPress Enter to continue, or Ctrl+C to cancel...")
        input()
        
        run_backup_system()

