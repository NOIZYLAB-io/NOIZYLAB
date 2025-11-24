#!/usr/bin/env python3
"""
NOIZYLAB Code Extraction & Migration Tool (Python Version)
More powerful handling of edge cases, better duplicate detection,
and smarter project organization.
"""

import os
import sys
import hashlib
import shutil
import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse

# Configuration
SOURCE_DIR = Path("/Volumes/4TBSG")
DEST_DIR = Path("/Users/m2ultra/NOIZYLAB")

# Code file extensions
CODE_EXTENSIONS = {
    # Web Frontend
    '.js', '.jsx', '.ts', '.tsx', '.mjs', '.cjs',
    '.html', '.htm', '.css', '.scss', '.sass', '.less',
    '.vue', '.svelte', '.astro',
    # Backend
    '.py', '.pyw', '.pyx', '.pxd',
    '.rb', '.erb', '.rake',
    '.php', '.phtml',
    '.go',
    '.rs',
    '.java', '.kt', '.kts', '.scala', '.clj', '.cljs',
    '.cs', '.fs', '.vb',
    '.swift', '.m', '.mm', '.h',
    '.c', '.cpp', '.cc', '.cxx', '.hpp', '.hxx',
    # Shell & Scripts
    '.sh', '.bash', '.zsh', '.fish', '.ps1', '.psm1', '.bat', '.cmd',
    # Config
    '.yml', '.yaml', '.json', '.jsonc', '.json5',
    '.xml', '.xsl', '.xslt',
    '.ini', '.cfg', '.conf', '.config',
    '.toml', '.env',
    # Data & DB
    '.sql', '.prisma', '.graphql', '.gql',
    # Docs
    '.md', '.mdx', '.rst', '.txt', '.tex',
    # DevOps
    '.tf', '.tfvars', '.hcl',
    # Mobile
    '.dart', '.gradle',
    # Other
    '.r', '.R', '.jl', '.lua', '.pl', '.pm',
    '.ex', '.exs', '.erl', '.hrl',
    '.hs', '.lhs', '.elm', '.ml', '.mli',
    '.nim', '.zig', '.v',
    '.sol', '.vy',  # Blockchain
}

# Special files without extensions
SPECIAL_FILES = {
    'Dockerfile', 'Makefile', 'Rakefile', 'Gemfile', 'Podfile',
    'Vagrantfile', 'Procfile', 'Brewfile', 'Justfile',
    '.gitignore', '.gitattributes', '.gitmodules',
    '.dockerignore', '.npmignore', '.eslintrc', '.prettierrc',
    '.babelrc', '.editorconfig', '.nvmrc', '.node-version',
    '.python-version', '.ruby-version', '.tool-versions',
}

# Directories to skip
SKIP_DIRS = {
    'node_modules', '.git', '__pycache__', '.pytest_cache',
    'venv', '.venv', 'env', '.env', 'virtualenv',
    '.idea', '.vscode', '.vs',
    'dist', 'build', 'out', 'target', 'bin', 'obj',
    '.next', '.nuxt', '.svelte-kit', '.astro',
    'vendor', 'packages', '.pub-cache',
    '.Trash', '.Spotlight-V100', '.fseventsd',
    'System Volume Information', '$RECYCLE.BIN',
    '.cache', 'cache', 'tmp', 'temp',
    'coverage', '.nyc_output',
    '.DS_Store',
}

# Project markers
PROJECT_MARKERS = {
    'package.json': 'node',
    'requirements.txt': 'python',
    'setup.py': 'python',
    'pyproject.toml': 'python',
    'Cargo.toml': 'rust',
    'go.mod': 'go',
    'Gemfile': 'ruby',
    'composer.json': 'php',
    'pom.xml': 'java',
    'build.gradle': 'java',
    'CMakeLists.txt': 'cpp',
    'Makefile': 'general',
    '.git': 'git-repo',
}


class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'


class CodeExtractor:
    def __init__(self, source: Path, dest: Path, dry_run: bool = False):
        self.source = source
        self.dest = dest
        self.dry_run = dry_run
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_dir = dest / ".migration-logs"
        self.stats = {
            'total_files': 0,
            'total_size': 0,
            'healed': 0,
            'duplicates': 0,
            'moved': 0,
            'errors': 0,
            'projects_found': 0,
        }
        self.file_hashes = {}
        self.duplicates = []
        self.projects = []
        self.files_to_process = []

    def log(self, msg: str, color: str = Colors.NC):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Colors.CYAN}[{timestamp}]{color} {msg}{Colors.NC}")

    def log_success(self, msg: str):
        print(f"{Colors.GREEN}[✓]{Colors.NC} {msg}")

    def log_warning(self, msg: str):
        print(f"{Colors.YELLOW}[!]{Colors.NC} {msg}")

    def log_error(self, msg: str):
        print(f"{Colors.RED}[✗]{Colors.NC} {msg}")
        self.stats['errors'] += 1

    def print_banner(self):
        print(f"{Colors.PURPLE}")
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║              NOIZYLAB CODE EXTRACTOR (Python)                     ║")
        print("║              Scan • Heal • Optimize • Migrate                     ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print(f"{Colors.NC}")

    def print_section(self, title: str):
        print(f"\n{Colors.PURPLE}{'━' * 70}")
        print(f"  {title}")
        print(f"{'━' * 70}{Colors.NC}\n")

    def validate_paths(self) -> bool:
        self.print_section("VALIDATING PATHS")

        if not self.source.exists():
            self.log_error(f"Source not found: {self.source}")
            return False
        self.log_success(f"Source found: {self.source}")

        if not self.dest.exists():
            if not self.dry_run:
                self.dest.mkdir(parents=True, exist_ok=True)
            self.log_success(f"Created destination: {self.dest}")
        else:
            self.log_success(f"Destination exists: {self.dest}")

        if not self.dry_run:
            self.log_dir.mkdir(parents=True, exist_ok=True)

        return True

    def should_skip_dir(self, path: Path) -> bool:
        return path.name in SKIP_DIRS

    def is_code_file(self, path: Path) -> bool:
        if path.name in SPECIAL_FILES:
            return True
        return path.suffix.lower() in CODE_EXTENSIONS

    def scan_for_projects(self):
        """Find all project roots based on markers."""
        self.print_section("SCANNING FOR PROJECTS")
        self.log("Looking for project markers...")

        for marker, project_type in PROJECT_MARKERS.items():
            for marker_file in self.source.rglob(marker):
                if any(skip in marker_file.parts for skip in SKIP_DIRS):
                    continue

                project_root = marker_file.parent
                if marker == '.git':
                    project_root = marker_file.parent

                self.projects.append({
                    'path': project_root,
                    'type': project_type,
                    'marker': marker,
                })

        # Deduplicate projects (prefer more specific markers)
        seen_paths = set()
        unique_projects = []
        for proj in sorted(self.projects, key=lambda x: len(str(x['path'])), reverse=True):
            if proj['path'] not in seen_paths:
                seen_paths.add(proj['path'])
                unique_projects.append(proj)

        self.projects = unique_projects
        self.stats['projects_found'] = len(self.projects)
        self.log_success(f"Found {len(self.projects)} projects")

        # Show top projects
        for proj in self.projects[:10]:
            print(f"  {Colors.CYAN}•{Colors.NC} [{proj['type']}] {proj['path'].name}")
        if len(self.projects) > 10:
            print(f"  ... and {len(self.projects) - 10} more")

    def scan_files(self):
        """Scan for all code files."""
        self.print_section("SCANNING FILES")
        self.log("Scanning for code files (this may take a while)...")

        count = 0
        for item in self.source.rglob('*'):
            if item.is_file() and self.is_code_file(item):
                if not any(skip in item.parts for skip in SKIP_DIRS):
                    self.files_to_process.append(item)
                    count += 1
                    if count % 1000 == 0:
                        print(f"\r{Colors.CYAN}Files found: {count}{Colors.NC}", end='')

        print()
        self.stats['total_files'] = len(self.files_to_process)
        self.log_success(f"Found {self.stats['total_files']} code files")

        # Calculate total size
        for f in self.files_to_process:
            try:
                self.stats['total_size'] += f.stat().st_size
            except:
                pass

        self.log(f"Total size: {self.human_size(self.stats['total_size'])}")

    def human_size(self, size: int) -> str:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} PB"

    def compute_hash(self, filepath: Path) -> str:
        """Compute MD5 hash of file."""
        try:
            hasher = hashlib.md5()
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(65536), b''):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            return None

    def find_duplicates(self):
        """Find duplicate files based on content hash."""
        self.print_section("FINDING DUPLICATES")
        self.log("Computing file hashes...")

        hash_to_files = defaultdict(list)
        count = 0
        total = len(self.files_to_process)

        for filepath in self.files_to_process:
            count += 1
            if count % 100 == 0:
                print(f"\r{Colors.CYAN}Hashing: {count}/{total}{Colors.NC}", end='')

            file_hash = self.compute_hash(filepath)
            if file_hash:
                hash_to_files[file_hash].append(filepath)

        print()

        # Find duplicates
        for hash_val, files in hash_to_files.items():
            if len(files) > 1:
                self.duplicates.append(files)
                self.stats['duplicates'] += len(files) - 1

        self.log_success(f"Found {self.stats['duplicates']} duplicate files")

    def heal_file(self, filepath: Path) -> bool:
        """Fix common issues in a file."""
        healed = False

        try:
            # Check if binary
            with open(filepath, 'rb') as f:
                chunk = f.read(1024)
                if b'\x00' in chunk:
                    return False  # Binary file

            # Read content
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            original = content

            # Fix CRLF -> LF
            content = content.replace('\r\n', '\n')

            # Fix trailing whitespace (for code files)
            if filepath.suffix in {'.py', '.js', '.ts', '.go', '.rs', '.java', '.rb'}:
                lines = content.split('\n')
                content = '\n'.join(line.rstrip() for line in lines)

            # Fix missing final newline
            if content and not content.endswith('\n'):
                content += '\n'

            if content != original and not self.dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                healed = True

        except Exception as e:
            pass

        return healed

    def heal_files(self):
        """Heal all files."""
        self.print_section("HEALING FILES")
        self.log("Fixing line endings, whitespace, encoding...")

        count = 0
        total = len(self.files_to_process)

        for filepath in self.files_to_process:
            count += 1
            if count % 100 == 0:
                print(f"\r{Colors.CYAN}Progress: {count}/{total}{Colors.NC}", end='')

            if self.heal_file(filepath):
                self.stats['healed'] += 1

        print()
        self.log_success(f"Healed {self.stats['healed']} files")

    def organize_and_move(self):
        """Move files to destination with organization."""
        self.print_section("ORGANIZING & MOVING FILES")

        # Create directory structure
        code_dir = self.dest / "code"
        dirs_to_create = [
            code_dir / "projects",
            code_dir / "scripts",
            code_dir / "configs",
            code_dir / "docs",
            code_dir / "misc",
        ]

        if not self.dry_run:
            for d in dirs_to_create:
                d.mkdir(parents=True, exist_ok=True)

        self.log("Moving files...")
        count = 0
        total = len(self.files_to_process)

        for filepath in self.files_to_process:
            count += 1
            if count % 100 == 0:
                print(f"\r{Colors.CYAN}Progress: {count}/{total} (moved: {self.stats['moved']}){Colors.NC}", end='')

            try:
                rel_path = filepath.relative_to(self.source)
                dest_path = code_dir / "projects" / rel_path

                if not self.dry_run:
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(filepath, dest_path)

                self.stats['moved'] += 1

            except Exception as e:
                self.stats['errors'] += 1

        print()
        self.log_success(f"Moved {self.stats['moved']} files")

    def generate_report(self):
        """Generate migration report."""
        self.print_section("GENERATING REPORT")

        report_path = self.log_dir / f"report_{self.timestamp}.md"
        report = f"""# NOIZYLAB Code Migration Report

**Generated:** {datetime.now().isoformat()}
**Source:** {self.source}
**Destination:** {self.dest}
**Mode:** {'DRY RUN' if self.dry_run else 'LIVE'}

## Summary

| Metric | Value |
|--------|-------|
| Total Files | {self.stats['total_files']:,} |
| Total Size | {self.human_size(self.stats['total_size'])} |
| Projects Found | {self.stats['projects_found']} |
| Files Healed | {self.stats['healed']} |
| Duplicates Found | {self.stats['duplicates']} |
| Files Moved | {self.stats['moved']} |
| Errors | {self.stats['errors']} |

## Projects Found

"""
        for proj in self.projects[:50]:
            report += f"- [{proj['type']}] `{proj['path'].name}`\n"

        if len(self.projects) > 50:
            report += f"\n... and {len(self.projects) - 50} more\n"

        if not self.dry_run:
            with open(report_path, 'w') as f:
                f.write(report)
            self.log_success(f"Report saved to: {report_path}")
        else:
            print(report)

    def run(self):
        """Run full extraction pipeline."""
        self.print_banner()

        if self.dry_run:
            self.log_warning("DRY RUN MODE - No files will be modified")

        if not self.validate_paths():
            return False

        self.scan_for_projects()
        self.scan_files()
        self.find_duplicates()
        self.heal_files()
        self.organize_and_move()
        self.generate_report()

        self.print_section("COMPLETE")
        print(f"{Colors.GREEN}")
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║                    MIGRATION COMPLETE!                            ║")
        print("╠═══════════════════════════════════════════════════════════════════╣")
        print(f"║  Files Processed: {self.stats['total_files']:<10}                                 ║")
        print(f"║  Projects Found:  {self.stats['projects_found']:<10}                                 ║")
        print(f"║  Files Healed:    {self.stats['healed']:<10}                                 ║")
        print(f"║  Duplicates:      {self.stats['duplicates']:<10}                                 ║")
        print(f"║  Errors:          {self.stats['errors']:<10}                                 ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print(f"{Colors.NC}")

        return True


def main():
    parser = argparse.ArgumentParser(description='NOIZYLAB Code Extractor')
    parser.add_argument('--source', '-s', type=Path, default=SOURCE_DIR,
                        help='Source directory')
    parser.add_argument('--dest', '-d', type=Path, default=DEST_DIR,
                        help='Destination directory')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Preview without making changes')

    args = parser.parse_args()

    extractor = CodeExtractor(args.source, args.dest, args.dry_run)
    success = extractor.run()

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
