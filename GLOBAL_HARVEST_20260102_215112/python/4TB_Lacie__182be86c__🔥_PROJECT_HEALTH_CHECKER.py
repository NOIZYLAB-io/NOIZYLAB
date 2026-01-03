#!/usr/bin/env python3
"""
🔥 PROJECT HEALTH CHECKER - Comprehensive Health Analysis
=========================================================
Checks all projects for health, completeness, and best practices
"""

import os
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
import json

console = Console()

class ProjectHealthChecker:
    def __init__(self, base_path="/Users/m2ultra/NOIZYLAB"):
        self.base_path = Path(base_path)
        self.projects = []
        
    def check_project(self, project_path):
        """Check health of a project"""
        health = {
            'name': project_path.name,
            'path': str(project_path),
            'score': 100,
            'issues': [],
            'strengths': []
        }
        
        # Check for README
        if (project_path / "README.md").exists():
            health['strengths'].append("Has README.md")
        else:
            health['score'] -= 10
            health['issues'].append("Missing README.md")
        
        # Check for requirements.txt or package.json
        has_deps = (
            (project_path / "requirements.txt").exists() or
            (project_path / "package.json").exists() or
            (project_path / "pyproject.toml").exists()
        )
        if has_deps:
            health['strengths'].append("Has dependency file")
        else:
            health['score'] -= 5
            health['issues'].append("Missing dependency file")
        
        # Check for .gitignore
        if (project_path / ".gitignore").exists():
            health['strengths'].append("Has .gitignore")
        else:
            health['score'] -= 5
            health['issues'].append("Missing .gitignore")
        
        # Check for git repo
        if (project_path / ".git").exists():
            health['strengths'].append("Has git repository")
        else:
            health['score'] -= 10
            health['issues'].append("Not a git repository")
        
        # Check for main entry point
        has_entry = (
            (project_path / "main.py").exists() or
            (project_path / "app.py").exists() or
            (project_path / "index.js").exists() or
            (project_path / "index.ts").exists()
        )
        if has_entry:
            health['strengths'].append("Has main entry point")
        else:
            # Not always required
            pass
        
        # Check code files
        py_files = list(project_path.rglob("*.py"))
        js_files = list(project_path.rglob("*.js"))
        ts_files = list(project_path.rglob("*.ts"))
        
        total_code_files = len(py_files) + len(js_files) + len(ts_files)
        if total_code_files > 0:
            health['strengths'].append(f"{total_code_files} code files")
            health['code_files'] = total_code_files
        else:
            health['score'] -= 20
            health['issues'].append("No code files found")
        
        return health
    
    def scan_projects(self):
        """Scan all projects"""
        console.print(Panel.fit(
            "[bold cyan]🔥 PROJECT HEALTH CHECKER 🔥[/bold cyan]\n"
            "[dim]Comprehensive Health Analysis[/dim]",
            border_style="cyan"
        ))
        
        # Find major project directories
        project_dirs = [
            d for d in self.base_path.iterdir()
            if d.is_dir() and not d.name.startswith('.') and not d.name.startswith('_')
        ]
        
        console.print(f"\n[cyan]📊 Scanning {len(project_dirs)} projects...[/cyan]\n")
        
        with Progress(console=console) as progress:
            task = progress.add_task("[cyan]Checking projects...", total=len(project_dirs))
            
            for project_dir in project_dirs:
                # Skip certain directories
                if any(skip in str(project_dir) for skip in ['.git', 'node_modules', '__pycache__']):
                    progress.advance(task)
                    continue
                
                # Only check substantial projects (have code files)
                code_files = list(project_dir.rglob("*.py")) + list(project_dir.rglob("*.js")) + list(project_dir.rglob("*.ts"))
                if len(code_files) > 0 or (project_dir / ".git").exists():
                    health = self.check_project(project_dir)
                    self.projects.append(health)
                
                progress.advance(task)
        
        self.display_results()
    
    def display_results(self):
        """Display health check results"""
        console.print("\n" + "="*80)
        console.print("[bold green]📊 PROJECT HEALTH REPORT[/bold green]")
        console.print("="*80)
        
        # Sort by score
        self.projects.sort(key=lambda x: x['score'], reverse=True)
        
        # Overall stats
        avg_score = sum(p['score'] for p in self.projects) / len(self.projects) if self.projects else 0
        
        console.print(f"\n[cyan]Overall Average Health Score: {avg_score:.1f}/100[/cyan]\n")
        
        # Health table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Project", style="cyan", width=30)
        table.add_column("Score", style="green", justify="right")
        table.add_column("Issues", style="yellow", justify="right")
        table.add_column("Strengths", style="green", justify="right")
        table.add_column("Status", style="magenta")
        
        for project in self.projects[:20]:  # Top 20
            score = project['score']
            issues_count = len(project['issues'])
            strengths_count = len(project['strengths'])
            
            if score >= 90:
                status = "✅ Excellent"
            elif score >= 75:
                status = "✅ Good"
            elif score >= 60:
                status = "⚠️  Fair"
            else:
                status = "❌ Needs Work"
            
            table.add_row(
                project['name'][:28],
                f"{score}/100",
                str(issues_count),
                str(strengths_count),
                status
            )
        
        console.print(table)
        
        # Projects needing attention
        needs_work = [p for p in self.projects if p['score'] < 60]
        if needs_work:
            console.print("\n[bold yellow]⚠️  PROJECTS NEEDING ATTENTION[/bold yellow]")
            for project in needs_work:
                console.print(f"\n  [red]{project['name']}[/red] (Score: {project['score']}/100)")
                for issue in project['issues']:
                    console.print(f"    • {issue}")

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/Users/m2ultra/NOIZYLAB"
    
    checker = ProjectHealthChecker(base_path)
    checker.scan_projects()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Interrupted by user[/yellow]")
        sys.exit(1)

