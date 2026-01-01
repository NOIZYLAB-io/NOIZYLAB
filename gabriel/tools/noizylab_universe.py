#!/usr/bin/env python3
"""
🌌 NOIZYLAB UNIVERSE MANAGER
============================
Central command center for managing ALL NOIZYLAB repositories
Integrates with GitKraken MCP for cross-repo operations

Author: GABRIEL (MC96ECOUNIVERSE)
Version: 1.0.0
"""

import click
import subprocess
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

# NOIZYLAB Universe Configuration
NOIZYLAB_REPOS = {
    "GABRIEL": {
        "local": Path("/Users/m2ultra/NOIZYLAB/GABRIEL"),
        "remote": "NOIZYLAB-io/GABRIEL",
        "description": "Main AI Orchestration System",
        "workers": ["noizylab", "antigravity", "task-commander", "neural-gateway", "sonic-engine", "dazeflow", "command-center", "media-vault", "mc96-network", "gorunfree"]
    },
    "NOIZYLAB": {
        "local": Path("/Users/m2ultra/NOIZYLAB/NOIZYLAB"),
        "remote": "NOIZYLAB-io/NOIZYLAB",
        "description": "Development Environment & Hot-Rod Config",
        "workers": []
    },
    "NOIZYLAB_CONSOLE": {
        "local": Path("/Users/m2ultra/NOIZYLAB/NOIZYLAB_CONSOLE_v3"),
        "remote": "NOIZYLAB-io/NOIZYLAB_CONSOLE_v3",
        "description": "Console Dashboard UI",
        "workers": []
    }
}

# Known Open PRs (from GitKraken MCP discovery)
OPEN_PRS = [
    # NOIZYLAB repo
    {"repo": "NOIZYLAB-io/NOIZYLAB", "id": 20, "title": "Complete NOIZYLAB Development Environment Hot-Rod", "priority": "HIGH", "files": 50},
    {"repo": "NOIZYLAB-io/NOIZYLAB", "id": 18, "title": "GABRIEL Mission Control Portal - O(1) lookups", "priority": "MEDIUM", "files": 10},
    {"repo": "NOIZYLAB-io/NOIZYLAB", "id": 17, "title": "Comprehensive Git Hooks with Delta/Diff", "priority": "MEDIUM", "files": 5},
    {"repo": "NOIZYLAB-io/NOIZYLAB", "id": 11, "title": "Update deprecated Homebrew dependencies", "priority": "LOW", "files": 2},
    {"repo": "NOIZYLAB-io/NOIZYLAB", "id": 10, "title": "feat: Enhanced git aliases", "priority": "LOW", "files": 1},
    {"repo": "NOIZYLAB-io/NOIZYLAB", "id": 8, "title": "Comprehensive zsh functions for development", "priority": "MEDIUM", "files": 3},
    {"repo": "NOIZYLAB-io/NOIZYLAB", "id": 7, "title": "Add comprehensive .gitconfig and .gitattributes", "priority": "LOW", "files": 2},
    {"repo": "NOIZYLAB-io/NOIZYLAB", "id": 6, "title": "feat: Move all development configurations", "priority": "MEDIUM", "files": 15},
    {"repo": "NOIZYLAB-io/NOIZYLAB", "id": 5, "title": "Hot Rod Flow: Central orchestration system", "priority": "HIGH", "files": 20},
    {"repo": "NOIZYLAB-io/NOIZYLAB", "id": 4, "title": "Update README.md", "priority": "LOW", "files": 1},
    
    # GABRIEL repo
    {"repo": "NOIZYLAB-io/GABRIEL", "id": 6, "title": "Restructure repository with separation of concerns", "priority": "HIGH", "files": 30, "draft": True},
    {"repo": "NOIZYLAB-io/GABRIEL", "id": 5, "title": "Cloudflare MCP Server + D1 Database Infrastructure", "priority": "HIGH", "files": 25, "draft": True},
    
    # Noizyfish/GABRIEL (legacy fork?)
    {"repo": "Noizyfish/GABRIEL", "id": 5, "title": "Fix & Organize Repository Structure", "priority": "LOW", "files": 10},
    {"repo": "Noizyfish/GABRIEL", "id": 4, "title": "Move all GABRIEL code to CODEMASTER + Slack Bolt", "priority": "LOW", "files": 15},
    
    # NOIZYLAB_CONSOLE_v3
    {"repo": "NOIZYLAB-io/NOIZYLAB_CONSOLE_v3", "id": 5, "title": "Next.js Configuration Fixes", "priority": "MEDIUM", "files": 5},
    {"repo": "NOIZYLAB-io/NOIZYLAB_CONSOLE_v3", "id": 4, "title": "Tailwind & Components Setup", "priority": "MEDIUM", "files": 8},
    {"repo": "NOIZYLAB-io/NOIZYLAB_CONSOLE_v3", "id": 3, "title": "Layout Persistence Fix", "priority": "LOW", "files": 3},
    {"repo": "NOIZYLAB-io/NOIZYLAB_CONSOLE_v3", "id": 2, "title": "Initial Console Structure", "priority": "MEDIUM", "files": 20},
    {"repo": "NOIZYLAB-io/NOIZYLAB_CONSOLE_v3", "id": 1, "title": "Project Initialization", "priority": "LOW", "files": 5},
]

@click.group()
def cli():
    """🌌 NOIZYLAB Universe Manager - Orchestrate All Repos"""
    pass

@cli.command()
def dashboard():
    """📊 Show complete universe dashboard"""
    click.echo("\n" + "="*70)
    click.echo("🌌 NOIZYLAB UNIVERSE DASHBOARD")
    click.echo("="*70 + "\n")
    
    # Repository Status
    click.echo("📁 REPOSITORIES\n" + "-"*40)
    for name, config in NOIZYLAB_REPOS.items():
        local_path = config["local"]
        exists = "✅" if local_path.exists() else "❌"
        workers = f"({len(config['workers'])} workers)" if config['workers'] else ""
        click.echo(f"  {exists} {name}: {config['description']} {workers}")
        click.echo(f"     Local: {local_path}")
        click.echo(f"     Remote: github.com/{config['remote']}")
        click.echo()
    
    # PR Summary
    click.echo("\n📋 OPEN PULL REQUESTS\n" + "-"*40)
    
    high_priority = [pr for pr in OPEN_PRS if pr.get("priority") == "HIGH"]
    medium_priority = [pr for pr in OPEN_PRS if pr.get("priority") == "MEDIUM"]
    low_priority = [pr for pr in OPEN_PRS if pr.get("priority") == "LOW"]
    
    click.echo(f"  🔴 HIGH Priority: {len(high_priority)}")
    click.echo(f"  🟡 MEDIUM Priority: {len(medium_priority)}")
    click.echo(f"  🟢 LOW Priority: {len(low_priority)}")
    click.echo(f"  📊 Total: {len(OPEN_PRS)} open PRs")
    
    click.echo("\n" + "="*70 + "\n")

@cli.command()
@click.option("--priority", "-p", type=click.Choice(["HIGH", "MEDIUM", "LOW", "ALL"]), default="ALL")
def prs(priority: str):
    """📋 List all open pull requests"""
    click.echo("\n🔀 OPEN PULL REQUESTS\n" + "="*70)
    
    filtered = OPEN_PRS if priority == "ALL" else [pr for pr in OPEN_PRS if pr.get("priority") == priority]
    
    # Group by repo
    repos = {}
    for pr in filtered:
        repo = pr["repo"]
        if repo not in repos:
            repos[repo] = []
        repos[repo].append(pr)
    
    for repo, prs_list in repos.items():
        click.echo(f"\n📁 {repo}")
        click.echo("-" * 50)
        for pr in sorted(prs_list, key=lambda x: x["id"], reverse=True):
            priority_icon = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(pr.get("priority", "LOW"), "⚪")
            draft = " [DRAFT]" if pr.get("draft") else ""
            click.echo(f"  {priority_icon} PR #{pr['id']}: {pr['title']}{draft}")
            click.echo(f"     Files: {pr.get('files', '?')} | Priority: {pr.get('priority', 'UNKNOWN')}")
    
    click.echo("\n" + "="*70 + "\n")

@cli.command()
def sync():
    """🔄 Sync all local repositories with origin"""
    click.echo("\n🔄 SYNCING NOIZYLAB UNIVERSE\n" + "="*70)
    
    for name, config in NOIZYLAB_REPOS.items():
        local_path = config["local"]
        click.echo(f"\n📂 {name}")
        
        if not local_path.exists():
            click.echo(f"  ❌ Local path not found: {local_path}")
            continue
        
        try:
            # Git fetch
            result = subprocess.run(
                ["git", "fetch", "--all"],
                cwd=local_path,
                capture_output=True,
                text=True
            )
            click.echo(f"  ✅ Fetched latest")
            
            # Git status
            result = subprocess.run(
                ["git", "status", "--short"],
                cwd=local_path,
                capture_output=True,
                text=True
            )
            
            if result.stdout.strip():
                click.echo(f"  ⚠️  Uncommitted changes:")
                for line in result.stdout.strip().split("\n")[:5]:
                    click.echo(f"      {line}")
            else:
                click.echo(f"  ✅ Clean working tree")
                
        except Exception as e:
            click.echo(f"  ❌ Error: {e}")
    
    click.echo("\n" + "="*70 + "\n")

@cli.command()
def workers():
    """⚡ Show all Cloudflare Workers status"""
    click.echo("\n⚡ CLOUDFLARE WORKERS\n" + "="*70)
    
    gabriel_workers = NOIZYLAB_REPOS["GABRIEL"]["workers"]
    
    for worker in gabriel_workers:
        click.echo(f"  🔹 {worker}")
    
    click.echo(f"\n  Total: {len(gabriel_workers)} workers")
    click.echo("\n  Deploy all: cd ANTIGRAVITY_COMPLETE && ./deploy-all.sh")
    click.echo("\n" + "="*70 + "\n")

@cli.command()
def recommend():
    """🎯 Get PR merge recommendations"""
    click.echo("\n🎯 MERGE RECOMMENDATIONS\n" + "="*70)
    
    click.echo("\n✅ RECOMMENDED TO MERGE NOW:")
    click.echo("-" * 40)
    
    # High priority non-drafts
    ready = [pr for pr in OPEN_PRS if pr.get("priority") == "HIGH" and not pr.get("draft")]
    for pr in ready:
        click.echo(f"  🔴 {pr['repo']} PR #{pr['id']}")
        click.echo(f"     {pr['title']}")
        click.echo()
    
    click.echo("\n⏳ NEED REVIEW (Drafts):")
    click.echo("-" * 40)
    drafts = [pr for pr in OPEN_PRS if pr.get("draft")]
    for pr in drafts:
        click.echo(f"  📝 {pr['repo']} PR #{pr['id']}: {pr['title']}")
    
    click.echo("\n🔄 CAN BE CONSOLIDATED:")
    click.echo("-" * 40)
    click.echo("  - NOIZYLAB PRs #4-#10 → Single 'Dev Environment' PR")
    click.echo("  - CONSOLE PRs #1-#5 → Single 'Initial Setup' PR")
    click.echo("  - Noizyfish/GABRIEL PRs → May be obsolete (check against main)")
    
    click.echo("\n" + "="*70 + "\n")

@cli.command()
@click.argument("repo")
def branches(repo: str):
    """🌿 List branches for a repository"""
    config = NOIZYLAB_REPOS.get(repo.upper())
    
    if not config:
        click.echo(f"❌ Unknown repo: {repo}")
        click.echo(f"   Available: {', '.join(NOIZYLAB_REPOS.keys())}")
        return
    
    local_path = config["local"]
    
    if not local_path.exists():
        click.echo(f"❌ Local path not found: {local_path}")
        return
    
    result = subprocess.run(
        ["git", "branch", "-a", "--sort=-committerdate"],
        cwd=local_path,
        capture_output=True,
        text=True
    )
    
    click.echo(f"\n🌿 BRANCHES: {repo}\n" + "="*50)
    click.echo(result.stdout)

@cli.command()
def report():
    """📊 Generate full universe report"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report_content = f"""# 🌌 NOIZYLAB UNIVERSE REPORT
Generated: {timestamp}

## 📁 Repositories

| Repo | Status | Workers | Description |
|------|--------|---------|-------------|
"""
    
    for name, config in NOIZYLAB_REPOS.items():
        status = "✅" if config["local"].exists() else "❌"
        workers = len(config["workers"])
        report_content += f"| {name} | {status} | {workers} | {config['description']} |\n"
    
    report_content += f"""

## 📋 Open Pull Requests

| Priority | Repo | PR | Title |
|----------|------|-----|-------|
"""
    
    for pr in sorted(OPEN_PRS, key=lambda x: ({"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(x.get("priority"), 3), x["id"])):
        priority = pr.get("priority", "?")
        draft = " [DRAFT]" if pr.get("draft") else ""
        report_content += f"| {priority} | {pr['repo']} | #{pr['id']} | {pr['title']}{draft} |\n"
    
    report_content += f"""

## 🎯 Recommendations

### Merge Now (High Priority)
"""
    
    for pr in OPEN_PRS:
        if pr.get("priority") == "HIGH" and not pr.get("draft"):
            report_content += f"- `{pr['repo']}` PR #{pr['id']}: {pr['title']}\n"
    
    report_content += """

### Review Drafts
"""
    
    for pr in OPEN_PRS:
        if pr.get("draft"):
            report_content += f"- `{pr['repo']}` PR #{pr['id']}: {pr['title']}\n"
    
    report_content += """

### Consolidate
- NOIZYLAB PRs #4-#10 → Single 'Development Environment' PR
- CONSOLE PRs #1-#5 → Single 'Initial Setup' PR

---
*Generated by NOIZYLAB Universe Manager v1.0.0*
"""
    
    # Write report
    report_path = Path("/Users/m2ultra/NOIZYLAB/GABRIEL/NOIZYLAB_UNIVERSE_REPORT.md")
    report_path.write_text(report_content)
    
    click.echo(f"\n✅ Report generated: {report_path}")
    click.echo(report_content)

if __name__ == "__main__":
    cli()
