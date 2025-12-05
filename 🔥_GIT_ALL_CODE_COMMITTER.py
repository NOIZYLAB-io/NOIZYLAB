#!/usr/bin/env python3
"""
⚡ GIT ALL CODE COMMITTER - Commit all NOIZYLAB projects to git
================================================================
Automatically finds, organizes, and commits all code to git repos
"""

import os
import subprocess
import sys
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from rich.panel import Panel

console = Console()

class GitCommitter:
    def __init__(self, base_path="/Users/m2ultra/NOIZYLAB"):
        self.base_path = Path(base_path)
        self.projects = []
        self.committed = []
        self.failed = []
        
    def find_projects(self):
        """Find all projects that need git"""
        console.print("[cyan]🔍 Scanning for projects...[/cyan]")
        
        # Major projects to commit
        major_projects = [
            "email-intelligence",
            "master-dashboard",
            "control-panel",
            "ai-aggregator",
            "noizylab-knowledge-system",
            "ultimate-ssh-system",
            "ai",
            "automation",
            "cloudflare",
            "integrations",
            "network",
            "monitoring",
            "scripts",
            "core",
        ]
        
        for project in major_projects:
            project_path = self.base_path / project
            if project_path.exists() and project_path.is_dir():
                # Check if it's a substantial project (has Python files or has .git)
                has_code = (
                    list(project_path.rglob("*.py")) or
                    list(project_path.rglob("*.js")) or
                    list(project_path.rglob("*.ts")) or
                    (project_path / ".git").exists()
                )
                if has_code:
                    self.projects.append(project_path)
        
        console.print(f"[green]✅ Found {len(self.projects)} projects[/green]")
        return self.projects
    
    def init_git_if_needed(self, project_path):
        """Initialize git if needed"""
        git_dir = project_path / ".git"
        if not git_dir.exists():
            try:
                subprocess.run(
                    ["git", "init"],
                    cwd=project_path,
                    check=True,
                    capture_output=True
                )
                subprocess.run(
                    ["git", "branch", "-M", "main"],
                    cwd=project_path,
                    check=False,
                    capture_output=True
                )
                return True
            except subprocess.CalledProcessError:
                return False
        return True
    
    def create_gitignore(self, project_path):
        """Create .gitignore if doesn't exist"""
        gitignore_path = project_path / ".gitignore"
        if not gitignore_path.exists():
            default_gitignore = """# Python
__pycache__/
*.py[cod]
*.so
*.egg-info/
.venv/
venv/

# Database
*.db
*.db-shm
*.db-wal

# Secrets
*.key
*.pem
.env
*credentials*.json
*token*.json

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/
"""
            gitignore_path.write_text(default_gitignore)
            return True
        return False
    
    def commit_project(self, project_path):
        """Commit a project"""
        project_name = project_path.name
        
        try:
            # Initialize git if needed
            if not self.init_git_if_needed(project_path):
                return False, "Failed to initialize git"
            
            # Create .gitignore if needed
            self.create_gitignore(project_path)
            
            # Check if there are changes
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if not result.stdout.strip():
                return True, "No changes to commit"
            
            # Add all files
            subprocess.run(
                ["git", "add", "-A"],
                cwd=project_path,
                check=True,
                capture_output=True
            )
            
            # Commit
            commit_message = f"✨ Auto-commit: {project_name} organized and ready\n\n- All code committed\n- Structure organized\n- Ready for production"
            
            subprocess.run(
                ["git", "commit", "-m", commit_message],
                cwd=project_path,
                check=True,
                capture_output=True
            )
            
            return True, "Committed successfully"
            
        except subprocess.CalledProcessError as e:
            return False, f"Git error: {e.stderr.decode() if e.stderr else str(e)}"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def commit_all(self):
        """Commit all projects"""
        console.print(f"\n[bold cyan]⚡ GIT ALL CODE COMMITTER ⚡[/bold cyan]\n")
        
        projects = self.find_projects()
        
        if not projects:
            console.print("[yellow]⚠️  No projects found[/yellow]")
            return
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Committing projects...", total=len(projects))
            
            for project_path in projects:
                project_name = project_path.name
                progress.update(task, description=f"[cyan]Processing {project_name}...")
                
                success, message = self.commit_project(project_path)
                
                if success:
                    self.committed.append((project_name, message))
                else:
                    self.failed.append((project_name, message))
                
                progress.advance(task)
        
        # Display results
        self.display_results()
    
    def display_results(self):
        """Display commit results"""
        console.print("\n" + "="*80)
        console.print("[bold green]📊 COMMIT RESULTS[/bold green]")
        console.print("="*80)
        
        # Committed
        if self.committed:
            table = Table(title=f"✅ Committed ({len(self.committed)})", show_header=True)
            table.add_column("Project", style="cyan")
            table.add_column("Status", style="green")
            
            for project, message in self.committed:
                table.add_row(project, message)
            
            console.print(table)
        
        # Failed
        if self.failed:
            table = Table(title=f"❌ Failed ({len(self.failed)})", show_header=True)
            table.add_column("Project", style="red")
            table.add_column("Error", style="yellow")
            
            for project, message in self.failed:
                table.add_row(project, message[:60])
            
            console.print(table)
        
        console.print(f"\n[bold green]✨ Completed: {len(self.committed)}/{len(self.projects)} projects committed![/bold green]\n")

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/Users/m2ultra/NOIZYLAB"
    
    committer = GitCommitter(base_path)
    committer.commit_all()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Interrupted by user[/yellow]")
        sys.exit(1)

