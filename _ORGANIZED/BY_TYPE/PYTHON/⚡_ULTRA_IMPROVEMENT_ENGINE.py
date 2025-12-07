#!/usr/bin/env python3
"""
⚡ ULTRA IMPROVEMENT ENGINE - Maximum Velocity Upgrades
========================================================
Automatically upgrades, optimizes, and improves all NOIZYLAB code
"""

import os
import subprocess
import sys
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from rich.panel import Panel
import json
import re

console = Console()

class UltraImprovementEngine:
    def __init__(self, base_path="/Users/m2ultra/NOIZYLAB"):
        self.base_path = Path(base_path)
        self.improvements = []
        self.optimizations = []
        self.fixes = []
        
    def analyze_code_quality(self, file_path):
        """Analyze code quality and suggest improvements"""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                
            # Check for common issues
            if not content.strip():
                return issues
                
            # Check for shebang in Python files
            if file_path.suffix == '.py' and not content.startswith('#!/usr/bin/env python3'):
                if content.strip():  # Only if file has content
                    issues.append({
                        'type': 'missing_shebang',
                        'file': str(file_path),
                        'fix': 'Add shebang: #!/usr/bin/env python3'
                    })
            
            # Check for very long lines
            for i, line in enumerate(lines, 1):
                if len(line) > 120:
                    issues.append({
                        'type': 'long_line',
                        'file': str(file_path),
                        'line': i,
                        'fix': f'Line {i} exceeds 120 characters'
                    })
            
            # Check for TODO/FIXME comments
            for i, line in enumerate(lines, 1):
                if re.search(r'\b(TODO|FIXME|XXX|HACK)\b', line, re.IGNORECASE):
                    issues.append({
                        'type': 'todo',
                        'file': str(file_path),
                        'line': i,
                        'note': line.strip()[:60]
                    })
            
            # Check for missing docstrings in Python
            if file_path.suffix == '.py' and len(lines) > 10:
                # Check if first non-comment/non-empty line after imports is a function/class
                has_docstring = False
                for i, line in enumerate(lines):
                    stripped = line.strip()
                    if stripped and not stripped.startswith('#') and not stripped.startswith('"""'):
                        if stripped.startswith('def ') or stripped.startswith('class '):
                            # Check next few lines for docstring
                            if i + 1 < len(lines):
                                next_lines = '\n'.join(lines[i+1:i+4])
                                if '"""' in next_lines or "'''" in next_lines:
                                    has_docstring = True
                                    break
                            if not has_docstring and stripped.startswith('def '):
                                issues.append({
                                    'type': 'missing_docstring',
                                    'file': str(file_path),
                                    'line': i + 1,
                                    'fix': 'Add docstring to function'
                                })
                            break
            
        except Exception as e:
            pass
        
        return issues
    
    def improve_file(self, file_path):
        """Apply improvements to a file"""
        improvements = []
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            original_content = content
            
            # Add shebang if missing for Python files
            if file_path.suffix == '.py' and content.strip() and not content.startswith('#!/'):
                content = '#!/usr/bin/env python3\n' + content
                improvements.append('Added shebang')
            
            # Fix common Python issues
            if file_path.suffix == '.py':
                # Remove duplicate shebangs
                lines = content.split('\n')
                if len(lines) > 1 and lines[0].startswith('#!') and lines[1].startswith('#!'):
                    lines = [lines[0]] + lines[2:]
                    content = '\n'.join(lines)
                    improvements.append('Removed duplicate shebang')
            
            # Only write if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return improvements
        
        except Exception as e:
            pass
        
        return []
    
    def scan_and_improve(self):
        """Scan all code and apply improvements"""
        console.print(Panel.fit(
            "[bold cyan]⚡ ULTRA IMPROVEMENT ENGINE ⚡[/bold cyan]\n"
            "[dim]Maximum Velocity Code Upgrades[/dim]",
            border_style="cyan"
        ))
        
        # Find all Python files
        python_files = list(self.base_path.rglob("*.py"))
        # Exclude certain directories
        python_files = [
            f for f in python_files
            if '.git' not in str(f) and
            'node_modules' not in str(f) and
            '__pycache__' not in str(f) and
            'venv' not in str(f) and
            '.venv' not in str(f)
        ]
        
        console.print(f"\n[cyan]📊 Found {len(python_files)} Python files to analyze...[/cyan]\n")
        
        all_issues = []
        improved_count = 0
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Analyzing and improving...", total=len(python_files))
            
            for file_path in python_files:
                # Analyze
                issues = self.analyze_code_quality(file_path)
                all_issues.extend(issues)
                
                # Improve
                improvements = self.improve_file(file_path)
                if improvements:
                    improved_count += 1
                    self.improvements.append({
                        'file': str(file_path),
                        'improvements': improvements
                    })
                
                progress.advance(task)
        
        # Display results
        self.display_results(all_issues, improved_count, len(python_files))
        
        return all_issues
    
    def display_results(self, issues, improved_count, total_files):
        """Display improvement results"""
        console.print("\n" + "="*80)
        console.print("[bold green]📊 IMPROVEMENT RESULTS[/bold green]")
        console.print("="*80)
        
        # Summary
        table = Table(title="Summary", show_header=True, header_style="bold magenta")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Files Analyzed", f"{total_files:,}")
        table.add_row("Files Improved", f"{improved_count:,}")
        table.add_row("Issues Found", f"{len(issues):,}")
        
        console.print(table)
        
        # Group issues by type
        issue_types = {}
        for issue in issues:
            issue_type = issue['type']
            if issue_type not in issue_types:
                issue_types[issue_type] = []
            issue_types[issue_type].append(issue)
        
        if issue_types:
            console.print("\n[bold yellow]🔍 ISSUES BY TYPE[/bold yellow]")
            issues_table = Table(show_header=True, header_style="bold magenta")
            issues_table.add_column("Type", style="cyan")
            issues_table.add_column("Count", style="yellow")
            issues_table.add_column("Example", style="dim")
            
            for issue_type, type_issues in sorted(issue_types.items(), key=lambda x: len(x[1]), reverse=True):
                example = type_issues[0].get('note', type_issues[0].get('fix', ''))[:40]
                issues_table.add_row(issue_type, str(len(type_issues)), example)
            
            console.print(issues_table)
        
        # Improvements made
        if self.improvements:
            console.print("\n[bold green]✨ IMPROVEMENTS APPLIED[/bold green]")
            for imp in self.improvements[:10]:  # Show first 10
                file_name = Path(imp['file']).name
                console.print(f"  ✅ {file_name}: {', '.join(imp['improvements'])}")
            
            if len(self.improvements) > 10:
                console.print(f"  ... and {len(self.improvements) - 10} more")
        
        console.print("\n[bold green]✨ Analysis complete![/bold green]\n")

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/Users/m2ultra/NOIZYLAB"
    
    engine = UltraImprovementEngine(base_path)
    engine.scan_and_improve()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Interrupted by user[/yellow]")
        sys.exit(1)

