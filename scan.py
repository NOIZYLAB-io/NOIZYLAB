#!/usr/bin/env python3
"""
Metadata Scanner - Fish Music Inc
Identify original work (no metadata) vs. library content (has metadata)
"""

import os
import sys
from pathlib import Path
from mutagen import File as MutagenFile
from mutagen.id3 import ID3
from mutagen.wave import WAVE
from rich.console import Console
from rich.table import Table
from rich.progress import track
import json

console = Console()

class MetadataScanner:
    """Scan audio files for metadata to identify originals vs. library content"""
    
    def __init__(self, scan_path):
        self.scan_path = Path(scan_path)
        self.originals = []  # Files with NO metadata (ROB's work)
        self.library = []    # Files with metadata (commercial/library)
        self.errors = []
        
    def scan_file(self, filepath):
        """Scan a single audio file for metadata"""
        try:
            audio = MutagenFile(filepath)
            
            if audio is None:
                return None
            
            # Check for any metadata
            has_metadata = False
            metadata_types = []
            
            # Check ID3 tags
            if hasattr(audio, 'tags') and audio.tags:
                has_metadata = True
                metadata_types.append('ID3')
            
            # Check for BWF (Broadcast Wave Format) metadata
            if isinstance(audio, WAVE):
                if hasattr(audio, 'info') and hasattr(audio.info, 'bitrate'):
                    # Check for BWF chunks
                    if hasattr(audio, '_WaveFile__bext'):
                        has_metadata = True
                        metadata_types.append('BWF')
            
            # Check for embedded metadata in other formats
            if hasattr(audio, 'info'):
                info_dict = vars(audio.info) if hasattr(vars(audio.info), '__dict__') else {}
                if any(key for key in info_dict.keys() if 'title' in key.lower() or 'artist' in key.lower()):
                    has_metadata = True
                    metadata_types.append('Embedded')
            
            result = {
                'path': str(filepath),
                'filename': filepath.name,
                'has_metadata': has_metadata,
                'metadata_types': metadata_types,
                'size': filepath.stat().st_size,
                'format': audio.mime[0] if hasattr(audio, 'mime') else 'unknown'
            }
            
            if has_metadata:
                self.library.append(result)
            else:
                self.originals.append(result)
                
            return result
            
        except Exception as e:
            error = {'path': str(filepath), 'error': str(e)}
            self.errors.append(error)
            return None
    
    def scan_directory(self):
        """Scan entire directory recursively"""
        console.print(f"\n[bold cyan]🔍 Scanning: {self.scan_path}[/bold cyan]\n")
        
        # Supported audio extensions
        audio_extensions = {'.wav', '.aif', '.aiff', '.mp3', '.flac', '.m4a', '.aac', '.ogg'}
        
        # Find all audio files
        audio_files = []
        for ext in audio_extensions:
            audio_files.extend(self.scan_path.rglob(f'*{ext}'))
        
        console.print(f"Found [bold]{len(audio_files)}[/bold] audio files\n")
        
        # Scan each file
        for filepath in track(audio_files, description="Scanning files..."):
            self.scan_file(filepath)
        
        return self.generate_report()
    
    def generate_report(self):
        """Generate scan report"""
        console.print("\n" + "="*80)
        console.print("[bold green]📊 SCAN COMPLETE[/bold green]")
        console.print("="*80 + "\n")
        
        # Summary table
        table = Table(title="Summary")
        table.add_column("Category", style="cyan")
        table.add_column("Count", style="magenta", justify="right")
        table.add_column("Description", style="white")
        
        table.add_row(
            "ORIGINALS ✨",
            str(len(self.originals)),
            "No metadata - ROB's original work"
        )
        table.add_row(
            "LIBRARY 📚",
            str(len(self.library)),
            "Has metadata - commercial/library content"
        )
        table.add_row(
            "ERRORS ⚠️",
            str(len(self.errors)),
            "Files that couldn't be scanned"
        )
        
        console.print(table)
        console.print()
        
        # Details
        if self.originals:
            console.print(f"\n[bold green]✨ ORIGINALS ({len(self.originals)} files)[/bold green]")
            console.print("[dim]These files have NO metadata - likely ROB's original recordings/compositions[/dim]\n")
            for item in self.originals[:10]:  # Show first 10
                console.print(f"  • {item['filename']}")
            if len(self.originals) > 10:
                console.print(f"  [dim]... and {len(self.originals) - 10} more[/dim]")
        
        if self.library:
            console.print(f"\n[bold blue]📚 LIBRARY ({len(self.library)} files)[/bold blue]")
            console.print("[dim]These files have metadata - commercial/library samples[/dim]\n")
            for item in self.library[:10]:  # Show first 10
                meta_types = ", ".join(item['metadata_types'])
                console.print(f"  • {item['filename']} [{meta_types}]")
            if len(self.library) > 10:
                console.print(f"  [dim]... and {len(self.library) - 10} more[/dim]")
        
        if self.errors:
            console.print(f"\n[bold red]⚠️  ERRORS ({len(self.errors)} files)[/bold red]\n")
            for error in self.errors[:5]:
                console.print(f"  • {Path(error['path']).name}: {error['error']}")
            if len(self.errors) > 5:
                console.print(f"  [dim]... and {len(self.errors) - 5} more[/dim]")
        
        # Save results
        results = {
            'originals': self.originals,
            'library': self.library,
            'errors': self.errors,
            'summary': {
                'total_scanned': len(self.originals) + len(self.library),
                'originals_count': len(self.originals),
                'library_count': len(self.library),
                'errors_count': len(self.errors)
            }
        }
        
        return results


def main():
    if len(sys.argv) < 2:
        console.print("[red]Usage: python scan.py <directory_path>[/red]")
        console.print("\nExample:")
        console.print("  python scan.py /Volumes/4TB-Lacie/music")
        sys.exit(1)
    
    scan_path = sys.argv[1]
    
    if not os.path.exists(scan_path):
        console.print(f"[red]Error: Directory not found: {scan_path}[/red]")
        sys.exit(1)
    
    scanner = MetadataScanner(scan_path)
    results = scanner.scan_directory()
    
    # Save results to JSON
    output_file = Path('metadata_scan_results.json')
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    console.print(f"\n[green]✅ Results saved to: {output_file}[/green]\n")


if __name__ == '__main__':
    main()

