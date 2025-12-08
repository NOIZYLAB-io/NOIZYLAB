#!/usr/bin/env python3
"""
🚀 AUTO OPTIMIZER - Automatic Code Optimization
================================================
Optimizes imports, removes unused code, improves performance
"""

import os
import ast
import sys
from pathlib import Path
from rich.console import Console
from rich.progress import Progress
import subprocess

console = Console()

class AutoOptimizer:
    def __init__(self, base_path="/Users/m2ultra/NOIZYLAB"):
        self.base_path = Path(base_path)
        self.optimizations = []
        
    def optimize_imports(self, file_path):
        """Optimize imports using isort and autoflake"""
        try:
            # Try to use isort if available
            result = subprocess.run(
                ["isort", "--check-only", "--diff", str(file_path)],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                # Run isort to fix
                subprocess.run(
                    ["isort", str(file_path)],
                    capture_output=True
                )
                return True
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass
        return False
    
    def make_executable(self, file_path):
        """Make Python scripts executable"""
        if file_path.suffix == '.py':
            try:
                os.chmod(file_path, 0o755)
                return True
            except:
                pass
        return False
    
    def optimize_all(self):
        """Optimize all Python files"""
        console.print("[bold cyan]🚀 AUTO OPTIMIZER[/bold cyan]\n")
        
        python_files = list(self.base_path.rglob("*.py"))
        python_files = [
            f for f in python_files
            if '.git' not in str(f) and
            '__pycache__' not in str(f) and
            'venv' not in str(f)
        ]
        
        console.print(f"[cyan]📊 Found {len(python_files)} files to optimize...[/cyan]\n")
        
        optimized = 0
        executable = 0
        
        with Progress(console=console) as progress:
            task = progress.add_task("[cyan]Optimizing...", total=len(python_files))
            
            for file_path in python_files:
                # Make executable
                if self.make_executable(file_path):
                    executable += 1
                
                # Optimize imports
                if self.optimize_imports(file_path):
                    optimized += 1
                    self.optimizations.append(str(file_path))
                
                progress.advance(task)
        
        console.print(f"\n[green]✅ Made {executable} files executable[/green]")
        console.print(f"[green]✅ Optimized imports in {optimized} files[/green]\n")

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/Users/m2ultra/NOIZYLAB"
    
    optimizer = AutoOptimizer(base_path)
    optimizer.optimize_all()

if __name__ == "__main__":
    main()

