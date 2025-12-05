#!/usr/bin/env python3
"""
GOD DEEP SCANNER - Full Metadata & File Integrity Scanner
CB_01 - Fish Music Inc
Scans ALL files, extracts metadata, finds broken/corrupt files, HEALS!
GORUNFREE! 🎸🔥
"""

import os
import sys
import json
import hashlib
import struct
import wave
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Colors
class C:
    R = '\033[0;31m'
    G = '\033[0;32m'
    Y = '\033[1;33m'
    B = '\033[0;34m'
    M = '\033[0;35m'
    C = '\033[0;36m'
    BOLD = '\033[1m'
    NC = '\033[0m'

# Thread-safe counters
class Counter:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0
    def inc(self, n=1):
        with self.lock:
            self.value += n
    def get(self):
        with self.lock:
            return self.value

class DeepScanner:
    """Deep file scanner with metadata extraction and healing"""

    # Audio file signatures (magic bytes)
    SIGNATURES = {
        b'RIFF': 'WAV',
        b'FORM': 'AIFF',
        b'ID3': 'MP3',
        b'\xff\xfb': 'MP3',
        b'\xff\xfa': 'MP3',
        b'fLaC': 'FLAC',
        b'OggS': 'OGG',
        b'\x00\x00\x00': 'M4A/AAC',  # Partial
        b'NKS': 'NKS',  # Native Instruments
        b'/NI/': 'NKI',  # Kontakt
    }

    # File types to scan
    AUDIO_EXTENSIONS = {'.wav', '.aif', '.aiff', '.mp3', '.flac', '.ogg', '.m4a', '.aac', '.rex', '.rx2'}
    SAMPLE_EXTENSIONS = {'.nki', '.nkm', '.nkx', '.nkc', '.nkr', '.ncw', '.nks'}
    PRESET_EXTENSIONS = {'.fxp', '.fxb', '.vstpreset', '.aupreset', '.nmsv'}
    DATA_EXTENSIONS = {'.nicnt', '.xml', '.json', '.plist', '.db'}

    def __init__(self, output_dir=None):
        self.output_dir = Path(output_dir) if output_dir else Path.home() / ".god-deep-scan"
        self.output_dir.mkdir(exist_ok=True)

        # Results
        self.files_scanned = Counter()
        self.files_healthy = Counter()
        self.files_corrupt = Counter()
        self.files_healed = Counter()
        self.total_size = Counter()

        self.corrupt_files = []
        self.healed_files = []
        self.metadata_index = {}
        self.errors = []

        self.scan_start = None
        self.scan_end = None

    def get_file_hash(self, filepath, quick=True):
        """Get MD5 hash of file (quick=first 1MB only)"""
        try:
            hasher = hashlib.md5()
            with open(filepath, 'rb') as f:
                if quick:
                    hasher.update(f.read(1024 * 1024))
                else:
                    for chunk in iter(lambda: f.read(65536), b''):
                        hasher.update(chunk)
            return hasher.hexdigest()
        except:
            return None

    def detect_file_type(self, filepath):
        """Detect file type from magic bytes"""
        try:
            with open(filepath, 'rb') as f:
                header = f.read(16)

            for sig, ftype in self.SIGNATURES.items():
                if header.startswith(sig):
                    return ftype

            # Check by extension
            ext = filepath.suffix.lower()
            if ext in self.AUDIO_EXTENSIONS:
                return ext[1:].upper()
            elif ext in self.SAMPLE_EXTENSIONS:
                return f"NI-{ext[1:].upper()}"

            return "UNKNOWN"
        except:
            return "ERROR"

    def check_wav_integrity(self, filepath):
        """Check WAV file integrity"""
        try:
            with wave.open(str(filepath), 'rb') as w:
                params = w.getparams()
                # Try to read a frame to verify
                w.readframes(min(1000, params.nframes))
                return {
                    'valid': True,
                    'channels': params.nchannels,
                    'sample_rate': params.framerate,
                    'bit_depth': params.sampwidth * 8,
                    'frames': params.nframes,
                    'duration': params.nframes / params.framerate if params.framerate else 0
                }
        except Exception as e:
            return {'valid': False, 'error': str(e)}

    def check_aiff_integrity(self, filepath):
        """Check AIFF file integrity"""
        try:
            import aifc
            with aifc.open(str(filepath), 'rb') as a:
                params = a.getparams()
                return {
                    'valid': True,
                    'channels': params.nchannels,
                    'sample_rate': params.framerate,
                    'bit_depth': params.sampwidth * 8,
                    'frames': params.nframes
                }
        except Exception as e:
            return {'valid': False, 'error': str(e)}

    def check_ni_file_integrity(self, filepath):
        """Check Native Instruments file integrity"""
        try:
            size = filepath.stat().st_size
            if size == 0:
                return {'valid': False, 'error': 'Empty file'}

            with open(filepath, 'rb') as f:
                header = f.read(64)

            # Basic header check
            if len(header) < 16:
                return {'valid': False, 'error': 'File too small'}

            return {
                'valid': True,
                'size': size,
                'type': filepath.suffix[1:].upper()
            }
        except Exception as e:
            return {'valid': False, 'error': str(e)}

    def extract_wav_metadata(self, filepath):
        """Extract metadata from WAV file"""
        meta = {}
        try:
            with open(filepath, 'rb') as f:
                # Read RIFF header
                riff = f.read(4)
                if riff != b'RIFF':
                    return meta

                size = struct.unpack('<I', f.read(4))[0]
                wave_id = f.read(4)

                # Parse chunks
                while f.tell() < size + 8:
                    try:
                        chunk_id = f.read(4)
                        if len(chunk_id) < 4:
                            break
                        chunk_size = struct.unpack('<I', f.read(4))[0]

                        if chunk_id == b'fmt ':
                            fmt_data = f.read(chunk_size)
                            if len(fmt_data) >= 16:
                                audio_fmt, channels, sample_rate, byte_rate, block_align, bits = struct.unpack('<HHIIHH', fmt_data[:16])
                                meta['channels'] = channels
                                meta['sample_rate'] = sample_rate
                                meta['bit_depth'] = bits

                        elif chunk_id == b'LIST':
                            list_data = f.read(chunk_size)
                            if list_data[:4] == b'INFO':
                                # Parse INFO tags
                                pos = 4
                                while pos < len(list_data) - 8:
                                    tag = list_data[pos:pos+4].decode('ascii', errors='ignore')
                                    tag_size = struct.unpack('<I', list_data[pos+4:pos+8])[0]
                                    tag_data = list_data[pos+8:pos+8+tag_size].decode('utf-8', errors='ignore').rstrip('\x00')

                                    if tag == 'INAM':
                                        meta['title'] = tag_data
                                    elif tag == 'IART':
                                        meta['artist'] = tag_data
                                    elif tag == 'IPRD':
                                        meta['album'] = tag_data
                                    elif tag == 'ICMT':
                                        meta['comment'] = tag_data
                                    elif tag == 'IGNR':
                                        meta['genre'] = tag_data
                                    elif tag == 'ICRD':
                                        meta['date'] = tag_data

                                    pos += 8 + tag_size + (tag_size % 2)

                        elif chunk_id == b'bext':
                            # Broadcast WAV extension
                            bext_data = f.read(min(chunk_size, 602))
                            if len(bext_data) >= 256:
                                meta['description'] = bext_data[:256].decode('utf-8', errors='ignore').rstrip('\x00')
                                meta['originator'] = bext_data[256:288].decode('utf-8', errors='ignore').rstrip('\x00')

                        else:
                            f.seek(chunk_size + (chunk_size % 2), 1)
                    except:
                        break
        except:
            pass
        return meta

    def extract_nicnt_metadata(self, filepath):
        """Extract metadata from .nicnt file"""
        meta = {}
        try:
            import xml.etree.ElementTree as ET
            tree = ET.parse(filepath)
            root = tree.getroot()

            for elem in root.iter():
                if elem.text:
                    if elem.tag == 'Name':
                        meta['name'] = elem.text
                    elif elem.tag == 'Company':
                        meta['vendor'] = elem.text
                    elif elem.tag == 'HU':
                        meta['id'] = elem.text
                    elif elem.tag == 'Version':
                        meta['version'] = elem.text
                    elif elem.tag == 'Author':
                        meta['author'] = elem.text
        except:
            pass
        return meta

    def heal_wav_file(self, filepath):
        """Attempt to heal a corrupt WAV file"""
        try:
            backup_path = filepath.with_suffix('.wav.bak')
            healed_path = filepath.with_suffix('.healed.wav')

            # Try using sox or ffmpeg
            # First try sox
            result = subprocess.run(
                ['sox', str(filepath), str(healed_path)],
                capture_output=True, timeout=60
            )

            if result.returncode == 0 and healed_path.exists():
                # Verify healed file
                check = self.check_wav_integrity(healed_path)
                if check.get('valid'):
                    # Backup original, replace with healed
                    filepath.rename(backup_path)
                    healed_path.rename(filepath)
                    return {'healed': True, 'method': 'sox', 'backup': str(backup_path)}
                else:
                    healed_path.unlink()

            # Try ffmpeg
            result = subprocess.run(
                ['ffmpeg', '-i', str(filepath), '-c:a', 'pcm_s16le', str(healed_path), '-y'],
                capture_output=True, timeout=60
            )

            if result.returncode == 0 and healed_path.exists():
                check = self.check_wav_integrity(healed_path)
                if check.get('valid'):
                    filepath.rename(backup_path)
                    healed_path.rename(filepath)
                    return {'healed': True, 'method': 'ffmpeg', 'backup': str(backup_path)}
                else:
                    healed_path.unlink()

            return {'healed': False, 'error': 'Could not heal file'}
        except Exception as e:
            return {'healed': False, 'error': str(e)}

    def scan_file(self, filepath):
        """Scan a single file for integrity and metadata"""
        result = {
            'path': str(filepath),
            'name': filepath.name,
            'size': 0,
            'type': None,
            'valid': True,
            'metadata': {},
            'error': None
        }

        try:
            stat = filepath.stat()
            result['size'] = stat.st_size
            result['modified'] = datetime.fromtimestamp(stat.st_mtime).isoformat()

            self.total_size.inc(stat.st_size)

            ext = filepath.suffix.lower()
            result['type'] = self.detect_file_type(filepath)

            # Check integrity based on type
            if ext == '.wav':
                check = self.check_wav_integrity(filepath)
                result['valid'] = check.get('valid', False)
                result['metadata'] = self.extract_wav_metadata(filepath)
                result['audio_info'] = check

            elif ext in {'.aif', '.aiff'}:
                check = self.check_aiff_integrity(filepath)
                result['valid'] = check.get('valid', False)
                result['audio_info'] = check

            elif ext in self.SAMPLE_EXTENSIONS:
                check = self.check_ni_file_integrity(filepath)
                result['valid'] = check.get('valid', False)

            elif ext == '.nicnt':
                result['metadata'] = self.extract_nicnt_metadata(filepath)
                result['valid'] = True

            else:
                # Basic check - file readable and not empty
                result['valid'] = stat.st_size > 0

            if not result['valid']:
                result['error'] = check.get('error', 'Unknown error') if 'check' in dir() else 'Invalid file'

        except Exception as e:
            result['valid'] = False
            result['error'] = str(e)

        return result

    def scan_directory(self, scan_path, heal=False, max_workers=8):
        """Scan directory for all files"""
        scan_path = Path(scan_path)

        if not scan_path.exists():
            print(f"{C.R}Path not found: {scan_path}{C.NC}")
            return

        print(f"\n{C.BOLD}{C.M}🔍 DEEP SCANNING: {scan_path}{C.NC}")
        print(f"{C.C}{'=' * 60}{C.NC}")
        print(f"{C.C}Heal mode: {'ON' if heal else 'OFF'}{C.NC}")
        print(f"{C.C}Threads: {max_workers}{C.NC}")
        print()

        self.scan_start = datetime.now()

        # Collect all files
        all_files = []
        extensions = self.AUDIO_EXTENSIONS | self.SAMPLE_EXTENSIONS | self.PRESET_EXTENSIONS | self.DATA_EXTENSIONS

        print(f"{C.C}Collecting files...{C.NC}", end='', flush=True)
        for item in scan_path.rglob('*'):
            if item.is_file() and item.suffix.lower() in extensions:
                all_files.append(item)
        print(f" {C.G}{len(all_files)} files found{C.NC}")

        # Scan files with thread pool
        print(f"\n{C.C}Scanning files...{C.NC}")

        corrupt_list = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.scan_file, f): f for f in all_files}

            done = 0
            for future in as_completed(futures):
                done += 1
                if done % 100 == 0 or done == len(all_files):
                    pct = (done / len(all_files)) * 100
                    print(f"\r{C.C}Progress: {done}/{len(all_files)} ({pct:.1f}%) | Corrupt: {len(corrupt_list)}{C.NC}    ", end='', flush=True)

                try:
                    result = future.result()
                    self.files_scanned.inc()

                    if result['valid']:
                        self.files_healthy.inc()
                    else:
                        self.files_corrupt.inc()
                        corrupt_list.append(result)

                    # Index metadata
                    if result.get('metadata'):
                        self.metadata_index[result['path']] = result['metadata']

                except Exception as e:
                    self.errors.append(str(e))

        print()

        self.corrupt_files = corrupt_list

        # Heal corrupt files if requested
        if heal and corrupt_list:
            print(f"\n{C.Y}🔧 HEALING {len(corrupt_list)} CORRUPT FILES...{C.NC}")

            for cf in corrupt_list:
                filepath = Path(cf['path'])
                if filepath.suffix.lower() == '.wav':
                    print(f"  {C.C}Healing: {filepath.name}{C.NC}", end='', flush=True)
                    heal_result = self.heal_wav_file(filepath)
                    if heal_result.get('healed'):
                        print(f" {C.G}✓ HEALED{C.NC}")
                        self.files_healed.inc()
                        self.healed_files.append({
                            'path': str(filepath),
                            'method': heal_result.get('method'),
                            'backup': heal_result.get('backup')
                        })
                    else:
                        print(f" {C.R}✗ FAILED: {heal_result.get('error')}{C.NC}")

        self.scan_end = datetime.now()

    def generate_report(self):
        """Generate scan report"""
        duration = (self.scan_end - self.scan_start).total_seconds() if self.scan_end else 0

        report = []
        report.append(f"\n{'=' * 70}")
        report.append(f"🐟 GOD DEEP SCAN REPORT")
        report.append(f"Fish Music Inc - CB_01")
        report.append(f"{'=' * 70}")
        report.append(f"")
        report.append(f"📊 SCAN SUMMARY:")
        report.append(f"   Scan duration: {duration:.1f} seconds")
        report.append(f"   Files scanned: {self.files_scanned.get():,}")
        report.append(f"   Total size: {self._format_size(self.total_size.get())}")
        report.append(f"   Healthy files: {self.files_healthy.get():,} ✅")
        report.append(f"   Corrupt files: {self.files_corrupt.get():,} {'⚠️' if self.files_corrupt.get() else '✅'}")
        report.append(f"   Files healed: {self.files_healed.get():,}")
        report.append(f"")

        if self.corrupt_files:
            report.append(f"⚠️  CORRUPT FILES ({len(self.corrupt_files)}):")
            report.append("-" * 50)
            for cf in self.corrupt_files[:50]:
                report.append(f"   {cf['path']}")
                report.append(f"      Error: {cf.get('error', 'Unknown')}")
            if len(self.corrupt_files) > 50:
                report.append(f"   ... and {len(self.corrupt_files) - 50} more")
            report.append("")

        if self.healed_files:
            report.append(f"🔧 HEALED FILES ({len(self.healed_files)}):")
            report.append("-" * 50)
            for hf in self.healed_files:
                report.append(f"   ✓ {hf['path']}")
            report.append("")

        # Metadata stats
        meta_count = len(self.metadata_index)
        if meta_count:
            report.append(f"📋 METADATA EXTRACTED: {meta_count:,} files")
            report.append("")

        report.append(f"{'=' * 70}")
        report.append("GORUNFREE! 🎸🔥")

        return "\n".join(report)

    def _format_size(self, bytes):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes < 1024:
                return f"{bytes:.1f}{unit}"
            bytes /= 1024
        return f"{bytes:.1f}PB"

    def save_results(self):
        """Save scan results"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save full results
        results_file = self.output_dir / f"deep_scan_{timestamp}.json"
        with open(results_file, 'w') as f:
            json.dump({
                'scan_start': self.scan_start.isoformat() if self.scan_start else None,
                'scan_end': self.scan_end.isoformat() if self.scan_end else None,
                'files_scanned': self.files_scanned.get(),
                'files_healthy': self.files_healthy.get(),
                'files_corrupt': self.files_corrupt.get(),
                'files_healed': self.files_healed.get(),
                'total_size': self.total_size.get(),
                'corrupt_files': self.corrupt_files,
                'healed_files': self.healed_files,
                'metadata_index': self.metadata_index,
                'errors': self.errors
            }, f, indent=2, default=str)

        # Save report
        report_file = self.output_dir / f"deep_scan_report_{timestamp}.txt"
        with open(report_file, 'w') as f:
            f.write(self.generate_report())

        # Save corrupt file list
        if self.corrupt_files:
            corrupt_file = self.output_dir / f"corrupt_files_{timestamp}.txt"
            with open(corrupt_file, 'w') as f:
                for cf in self.corrupt_files:
                    f.write(f"{cf['path']}\n")

        print(f"\n{C.G}✅ Results saved:{C.NC}")
        print(f"   {C.C}{results_file}{C.NC}")
        print(f"   {C.C}{report_file}{C.NC}")

        return results_file


def main():
    import argparse

    parser = argparse.ArgumentParser(description='GOD Deep Scanner - File Integrity & Metadata')
    parser.add_argument('path', nargs='?', default=None, help='Path to scan')
    parser.add_argument('--heal', '-H', action='store_true', help='Attempt to heal corrupt files')
    parser.add_argument('--threads', '-t', type=int, default=8, help='Number of threads')
    parser.add_argument('--all-fish', action='store_true', help='Scan all Fish drives')
    args = parser.parse_args()

    print(f"\n{C.BOLD}{C.M}╔{'═' * 58}╗{C.NC}")
    print(f"{C.BOLD}{C.M}║  🐟 GOD DEEP SCANNER - Metadata & Integrity Check        ║{C.NC}")
    print(f"{C.BOLD}{C.M}║  Fish Music Inc - CB_01                                  ║{C.NC}")
    print(f"{C.BOLD}{C.M}╚{'═' * 58}╝{C.NC}")

    scanner = DeepScanner()

    if args.all_fish:
        # Scan all Fish drives
        fish_drives = [
            "/Volumes/4TB Blue Fish",
            "/Volumes/4TB Big Fish",
            "/Volumes/4TB FISH SG",
            "/Volumes/12TB"
        ]
        for drive in fish_drives:
            if Path(drive).exists():
                scanner.scan_directory(drive, heal=args.heal, max_workers=args.threads)
    elif args.path:
        scanner.scan_directory(args.path, heal=args.heal, max_workers=args.threads)
    else:
        # Default: scan Blue Fish NI folder
        scanner.scan_directory("/Volumes/4TB Blue Fish/Native Instruments", heal=args.heal, max_workers=args.threads)

    # Print report
    print(scanner.generate_report())

    # Save results
    scanner.save_results()

    print(f"\n{C.BOLD}{C.M}GORUNFREE! 🎸🔥{C.NC}\n")


if __name__ == "__main__":
    main()
