#!/usr/bin/env python3
"""
⚡ LIGHTNING FAST DUPLICATE FILE SCANNER
========================================
Optimized for maximum speed on large drives (4TB+)
Uses multi-threading, fast hashing, and smart pre-filtering
"""

import os
import sys
import hashlib
import threading
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.table import Table

console = Console()

# Try to use xxhash for speed (much faster than md5)
try:
    import xxhash
    HAS_XXHASH = True
    def fast_hash(filepath, chunk_size=65536):
        """Ultra-fast hash using xxhash"""
        hasher = xxhash.xxh64()
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
except ImportError:
    HAS_XXHASH = False
    def fast_hash(filepath, chunk_size=65536):
        """Fallback to md5"""
        md5 = hashlib.md5()
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                md5.update(chunk)
        return md5.hexdigest()

class DuplicateScanner:
    def __init__(self, root_path, max_workers=None):
        self.root_path = Path(root_path)
        self.max_workers = max_workers or min(32, (os.cpu_count() or 1) + 4)
        self.file_sizes = defaultdict(list)
        self.file_hashes = defaultdict(list)
        self.lock = threading.Lock()
        self.scanned = 0
        self.hashed = 0
        self.duplicates_found = 0
        self.total_size_duplicates = 0
        
    def scan_files(self, progress):
        """Phase 1: Scan all files and group by size"""
        console.print(f"[cyan]⚡ Phase 1: Scanning files (max {self.max_workers} threads)...[/cyan]")
        
        def process_file(filepath):
            try:
                size = filepath.stat().st_size
                if size > 0:  # Ignore empty files
                    with self.lock:
                        self.file_sizes[size].append(filepath)
                        self.scanned += 1
            except (OSError, PermissionError):
                pass
        
        # Walk directory tree in parallel
        task = progress.add_task("[cyan]Scanning files...", total=None)
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for root, dirs, files in os.walk(self.root_path):
                # Skip hidden/system directories for speed
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['System Volume Information', '$RECYCLE.BIN']]
                
                for file in files:
                    if file.startswith('.'):
                        continue
                    filepath = Path(root) / file
                    futures.append(executor.submit(process_file, filepath))
                    
                    if len(futures) >= 1000:
                        # Process in batches
                        for future in as_completed(futures[:100]):
                            future.result()
                        futures = futures[100:]
                        progress.update(task, advance=100)
            
            # Process remaining
            for future in as_completed(futures):
                future.result()
                progress.update(task, advance=1)
        
        progress.update(task, completed=self.scanned)
        console.print(f"[green]✅ Scanned {self.scanned:,} files[/green]")
        
    def hash_files(self, progress):
        """Phase 2: Hash files with same size (potential duplicates)"""
        console.print(f"[cyan]⚡ Phase 2: Hashing potential duplicates (max {self.max_workers} threads)...[/cyan]")
        
        # Only hash files that have size matches (potential duplicates)
        files_to_hash = []
        for size, filepaths in self.file_sizes.items():
            if len(filepaths) > 1:  # Multiple files with same size = potential duplicates
                files_to_hash.extend(filepaths)
        
        if not files_to_hash:
            console.print("[yellow]No potential duplicates found[/yellow]")
            return
        
        console.print(f"[cyan]Hashing {len(files_to_hash):,} potential duplicate files...[/cyan]")
        
        task = progress.add_task("[cyan]Hashing files...", total=len(files_to_hash))
        
        def hash_file(filepath):
            try:
                file_hash = fast_hash(filepath)
                file_size = filepath.stat().st_size
                with self.lock:
                    self.file_hashes[file_hash].append((filepath, file_size))
                    self.hashed += 1
                progress.update(task, advance=1)
            except (OSError, PermissionError) as e:
                progress.update(task, advance=1)
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(hash_file, files_to_hash)
        
        console.print(f"[green]✅ Hashed {self.hashed:,} files[/green]")
        
    def find_duplicates(self):
        """Phase 3: Find actual duplicates"""
        console.print("[cyan]⚡ Phase 3: Identifying duplicates...[/cyan]")
        
        duplicates = []
        for file_hash, filepaths in self.file_hashes.items():
            if len(filepaths) > 1:  # Multiple files with same hash = duplicates
                # Sort by path length (usually shorter = original)
                filepaths.sort(key=lambda x: (len(str(x[0])), str(x[0])))
                duplicates.append({
                    'hash': file_hash,
                    'files': filepaths,
                    'count': len(filepaths),
                    'size': filepaths[0][1]  # Size of one file
                })
                self.duplicates_found += len(filepaths) - 1  # One is original, rest are duplicates
                self.total_size_duplicates += filepaths[0][1] * (len(filepaths) - 1)
        
        return sorted(duplicates, key=lambda x: x['size'] * (x['count'] - 1), reverse=True)
    
    def scan(self):
        """Run complete scan"""
        start_time = time.time()
        
        console.print(f"\n[bold cyan]⚡ LIGHTNING FAST DUPLICATE SCANNER ⚡[/bold cyan]")
        console.print(f"[dim]Scanning: {self.root_path}[/dim]")
        console.print(f"[dim]Using {'xxhash' if HAS_XXHASH else 'md5'} for fast hashing[/dim]")
        console.print(f"[dim]Max workers: {self.max_workers}[/dim]\n")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            # Phase 1: Scan files
            self.scan_files(progress)
            
            # Phase 2: Hash potential duplicates
            if self.file_sizes:
                self.hash_files(progress)
            
            # Phase 3: Find duplicates
            duplicates = self.find_duplicates()
        
        elapsed = time.time() - start_time
        
        # Display results
        self.display_results(duplicates, elapsed)
        
        return duplicates
    
    def display_results(self, duplicates, elapsed):
        """Display scan results"""
        console.print("\n" + "="*80)
        console.print("[bold green]📊 SCAN RESULTS[/bold green]")
        console.print("="*80)
        
        # Summary
        table = Table(title="Summary", show_header=True, header_style="bold magenta")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Files Scanned", f"{self.scanned:,}")
        table.add_row("Files Hashed", f"{self.hashed:,}")
        table.add_row("Duplicate Groups", f"{len(duplicates):,}")
        table.add_row("Duplicate Files", f"{self.duplicates_found:,}")
        
        size_gb = self.total_size_duplicates / (1024**3)
        size_tb = size_gb / 1024
        if size_tb >= 1:
            size_str = f"{size_tb:.2f} TB"
        else:
            size_str = f"{size_gb:.2f} GB"
        table.add_row("Wasted Space", size_str)
        table.add_row("Scan Time", f"{elapsed:.2f} seconds")
        table.add_row("Speed", f"{self.scanned/elapsed:,.0f} files/sec")
        
        console.print(table)
        
        # Top duplicates
        if duplicates:
            console.print("\n[bold yellow]🔝 TOP 10 DUPLICATE GROUPS (by wasted space)[/bold yellow]")
            top_table = Table(show_header=True, header_style="bold magenta")
            top_table.add_column("Rank", style="cyan")
            top_table.add_column("File Count", style="yellow")
            top_table.add_column("Size Each", style="green")
            top_table.add_column("Wasted Space", style="red")
            top_table.add_column("First File", style="dim")
            
            for i, dup in enumerate(duplicates[:10], 1):
                size_gb = dup['size'] / (1024**3)
                wasted_gb = size_gb * (dup['count'] - 1)
                first_file = str(dup['files'][0][0])
                if len(first_file) > 60:
                    first_file = "..." + first_file[-57:]
                
                size_str = f"{size_gb:.2f} GB" if size_gb >= 1 else f"{dup['size']/(1024**2):.2f} MB"
                wasted_str = f"{wasted_gb:.2f} GB" if wasted_gb >= 1 else f"{wasted_gb*1024:.2f} MB"
                
                top_table.add_row(
                    str(i),
                    str(dup['count']),
                    size_str,
                    wasted_str,
                    first_file
                )
            
            console.print(top_table)
            
            # Save report
            report_path = Path.home() / "duplicate_scan_report.txt"
            self.save_report(duplicates, report_path, elapsed)
            console.print(f"\n[green]✅ Full report saved to: {report_path}[/green]")
    
    def save_report(self, duplicates, report_path, elapsed):
        """Save detailed report to file"""
        with open(report_path, 'w') as f:
            f.write("="*80 + "\n")
            f.write("DUPLICATE FILE SCAN REPORT\n")
            f.write("="*80 + "\n\n")
            f.write(f"Scan Path: {self.root_path}\n")
            f.write(f"Scan Time: {elapsed:.2f} seconds\n")
            f.write(f"Files Scanned: {self.scanned:,}\n")
            f.write(f"Files Hashed: {self.hashed:,}\n")
            f.write(f"Duplicate Groups: {len(duplicates):,}\n")
            f.write(f"Duplicate Files: {self.duplicates_found:,}\n")
            f.write(f"Wasted Space: {self.total_size_duplicates / (1024**3):.2f} GB\n\n")
            
            f.write("="*80 + "\n")
            f.write("ALL DUPLICATES\n")
            f.write("="*80 + "\n\n")
            
            for i, dup in enumerate(duplicates, 1):
                wasted_gb = (dup['size'] * (dup['count'] - 1)) / (1024**3)
                f.write(f"\n[Group {i}] {dup['count']} duplicates - Wasted: {wasted_gb:.2f} GB\n")
                f.write(f"Hash: {dup['hash']}\n")
                for j, (filepath, size) in enumerate(dup['files'], 1):
                    marker = " [ORIGINAL]" if j == 1 else " [DUPLICATE]"
                    f.write(f"  {j}. {filepath}{marker}\n")
                f.write("\n")

def main():
    if len(sys.argv) > 1:
        scan_path = sys.argv[1]
    else:
        scan_path = "/Volumes/MAG 4TB"
    
    if not os.path.exists(scan_path):
        console.print(f"[red]❌ Error: Path not found: {scan_path}[/red]")
        sys.exit(1)
    
    # Use maximum workers for speed
    max_workers = min(64, (os.cpu_count() or 8) * 4)
    
    scanner = DuplicateScanner(scan_path, max_workers=max_workers)
    duplicates = scanner.scan()
    
    console.print(f"\n[bold green]✨ Scan complete![/bold green]\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Scan interrupted by user[/yellow]")
        sys.exit(1)

