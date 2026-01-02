#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  📝 SMART COMMIT MESSAGE GENERATOR v1.0                                       ║
║  AI-powered context-aware commit messages                                     ║
║  Part of: NOIZYLAB AI Dev Toolkit                                             ║
║  Updated: 2026-01-02                                                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import subprocess
import os
import sys
import re
import json
from pathlib import Path
from typing import Optional
from dataclasses import dataclass

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
MODEL = "claude-sonnet-4-20250514"

# Conventional commit types with emojis
COMMIT_TYPES = {
    'feat': ('🚀', 'A new feature'),
    'fix': ('🐛', 'A bug fix'),
    'docs': ('📚', 'Documentation only changes'),
    'style': ('💎', 'Code style changes (formatting, semicolons)'),
    'refactor': ('♻️', 'Code refactoring'),
    'perf': ('⚡', 'Performance improvements'),
    'test': ('🧪', 'Adding or fixing tests'),
    'build': ('📦', 'Build system or dependencies'),
    'ci': ('🔧', 'CI/CD configuration'),
    'chore': ('🧹', 'Other changes (maintenance)'),
    'revert': ('⏪', 'Revert previous commit'),
    'security': ('🔒', 'Security fixes'),
    'cleanup': ('🧹', 'Code cleanup'),
    'wip': ('🚧', 'Work in progress'),
}

# ═══════════════════════════════════════════════════════════════════════════════
# GIT HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def get_staged_diff() -> str:
    """Get diff of staged changes."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--cached', '--stat'],
            capture_output=True, text=True, check=True
        )
        stat = result.stdout
        
        result = subprocess.run(
            ['git', 'diff', '--cached'],
            capture_output=True, text=True, check=True
        )
        diff = result.stdout
        
        return f"Stats:\n{stat}\n\nDiff:\n{diff}"
    except subprocess.CalledProcessError:
        return ""

def get_staged_files() -> list[str]:
    """Get list of staged files."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--cached', '--name-only'],
            capture_output=True, text=True, check=True
        )
        return [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]
    except subprocess.CalledProcessError:
        return []

def get_recent_commits(n: int = 10) -> list[str]:
    """Get recent commit messages for context."""
    try:
        result = subprocess.run(
            ['git', 'log', f'-{n}', '--oneline'],
            capture_output=True, text=True, check=True
        )
        return [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
    except subprocess.CalledProcessError:
        return []

def get_branch_name() -> str:
    """Get current branch name."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""

def commit_with_message(message: str, dry_run: bool = False) -> bool:
    """Create commit with message."""
    if dry_run:
        print(f"\n[DRY RUN] Would commit with message:\n{message}")
        return True
    
    try:
        subprocess.run(
            ['git', 'commit', '-m', message],
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

# ═══════════════════════════════════════════════════════════════════════════════
# ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

def analyze_changes(diff: str, files: list[str]) -> dict:
    """Analyze changes to determine commit type."""
    analysis = {
        'type': 'chore',
        'scope': None,
        'files': files,
        'additions': 0,
        'deletions': 0,
        'keywords': [],
    }
    
    # Count additions/deletions
    for line in diff.split('\n'):
        if line.startswith('+') and not line.startswith('+++'):
            analysis['additions'] += 1
        elif line.startswith('-') and not line.startswith('---'):
            analysis['deletions'] += 1
    
    # Detect type from files
    file_patterns = {
        'docs': ['.md', '.rst', '.txt', 'README', 'CHANGELOG', 'LICENSE'],
        'test': ['test_', '_test.py', '.test.', 'spec.'],
        'ci': ['.yml', '.yaml', 'Jenkinsfile', '.github/'],
        'build': ['package.json', 'setup.py', 'requirements', 'Dockerfile', 'Makefile'],
        'style': ['.css', '.scss', '.less'],
    }
    
    for file in files:
        for commit_type, patterns in file_patterns.items():
            if any(p in file.lower() for p in patterns):
                analysis['type'] = commit_type
                break
    
    # Detect scope from file paths
    if files:
        common_dir = os.path.commonpath([Path(f).parent for f in files if '/' in f] or ['.'])
        if common_dir and common_dir != '.':
            analysis['scope'] = Path(common_dir).name
    
    # Detect keywords in diff
    keywords = ['fix', 'add', 'remove', 'update', 'refactor', 'improve', 'optimize']
    diff_lower = diff.lower()
    analysis['keywords'] = [k for k in keywords if k in diff_lower]
    
    # Infer type from keywords
    if 'fix' in analysis['keywords']:
        analysis['type'] = 'fix'
    elif 'add' in analysis['keywords'] and analysis['additions'] > analysis['deletions'] * 2:
        analysis['type'] = 'feat'
    elif 'refactor' in analysis['keywords']:
        analysis['type'] = 'refactor'
    elif analysis['deletions'] > analysis['additions'] * 2:
        analysis['type'] = 'cleanup'
    
    return analysis

def generate_local_message(analysis: dict, diff: str) -> str:
    """Generate commit message without AI."""
    commit_type = analysis['type']
    emoji, _ = COMMIT_TYPES.get(commit_type, ('', ''))
    scope = f"({analysis['scope']})" if analysis['scope'] else ""
    
    # Generate description from changes
    files = analysis['files']
    if len(files) == 1:
        action = "update" if analysis['additions'] and analysis['deletions'] else \
                 "add" if analysis['additions'] > analysis['deletions'] else "remove"
        desc = f"{action} {Path(files[0]).name}"
    else:
        desc = f"update {len(files)} files"
    
    return f"{emoji} {commit_type}{scope}: {desc}"

# ═══════════════════════════════════════════════════════════════════════════════
# AI GENERATION
# ═══════════════════════════════════════════════════════════════════════════════

def generate_ai_message(diff: str, files: list[str], recent_commits: list[str]) -> str:
    """Use AI to generate smart commit message."""
    if not ANTHROPIC_API_KEY:
        return None
    
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        commit_types_str = "\n".join([f"  {t}: {emoji} - {desc}" for t, (emoji, desc) in COMMIT_TYPES.items()])
        
        prompt = f"""Generate a conventional commit message for these changes.

COMMIT FORMAT:
<emoji> <type>(<scope>): <description>

<optional body>

AVAILABLE TYPES:
{commit_types_str}

RECENT COMMITS (for style reference):
{chr(10).join(recent_commits[:5])}

CHANGED FILES:
{chr(10).join(files)}

DIFF (truncated):
```
{diff[:6000]}
```

RULES:
1. Use conventional commit format
2. Start with appropriate emoji
3. Scope is optional but helpful
4. Description should be imperative mood ("add" not "added")
5. Keep first line under 72 characters
6. Add body only if changes are complex
7. Be specific but concise

Generate ONLY the commit message, nothing else."""

        response = client.messages.create(
            model=MODEL,
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text.strip()
        
    except Exception as e:
        print(f"AI error: {e}")
        return None

# ═══════════════════════════════════════════════════════════════════════════════
# INTERACTIVE MODE
# ═══════════════════════════════════════════════════════════════════════════════

def interactive_commit():
    """Interactive commit message generation."""
    staged_files = get_staged_files()
    
    if not staged_files:
        print("❌ No staged changes. Use 'git add' first.")
        sys.exit(1)
    
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  📝 SMART COMMIT MESSAGE GENERATOR v1.0                                       ║
╚═══════════════════════════════════════════════════════════════════════════════╝

📁 Staged files ({len(staged_files)}):
""")
    for f in staged_files[:10]:
        print(f"   • {f}")
    if len(staged_files) > 10:
        print(f"   ... and {len(staged_files) - 10} more")
    
    diff = get_staged_diff()
    analysis = analyze_changes(diff, staged_files)
    recent = get_recent_commits()
    
    print(f"\n🔍 Analysis:")
    print(f"   Type: {analysis['type']}")
    print(f"   Scope: {analysis['scope'] or 'none'}")
    print(f"   +{analysis['additions']} / -{analysis['deletions']} lines")
    
    # Generate messages
    print("\n⏳ Generating commit messages...\n")
    
    local_msg = generate_local_message(analysis, diff)
    ai_msg = generate_ai_message(diff, staged_files, recent)
    
    messages = []
    
    if ai_msg:
        messages.append(('AI Generated', ai_msg))
    messages.append(('Auto Generated', local_msg))
    
    # Show options
    print("📋 SUGGESTED MESSAGES:\n")
    for i, (source, msg) in enumerate(messages, 1):
        print(f"  [{i}] {source}:")
        for line in msg.split('\n'):
            print(f"      {line}")
        print()
    
    print("  [c] Custom message")
    print("  [q] Cancel\n")
    
    # Get choice
    choice = input("Choose option: ").strip().lower()
    
    if choice == 'q':
        print("Cancelled.")
        sys.exit(0)
    elif choice == 'c':
        message = input("Enter commit message: ").strip()
    else:
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(messages):
                message = messages[idx][1]
            else:
                print("Invalid choice.")
                sys.exit(1)
        except ValueError:
            print("Invalid choice.")
            sys.exit(1)
    
    # Confirm
    print(f"\n📝 Final message:\n")
    for line in message.split('\n'):
        print(f"   {line}")
    
    confirm = input("\nCommit? [Y/n]: ").strip().lower()
    
    if confirm in ('', 'y', 'yes'):
        if commit_with_message(message):
            print("\n✅ Committed successfully!")
        else:
            print("\n❌ Commit failed.")
            sys.exit(1)
    else:
        print("Cancelled.")

# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Smart Commit Message Generator')
    parser.add_argument('--auto', '-a', action='store_true', help='Auto-commit without confirmation')
    parser.add_argument('--dry-run', '-n', action='store_true', help='Show message without committing')
    parser.add_argument('--no-ai', action='store_true', help='Skip AI generation')
    parser.add_argument('--type', '-t', choices=COMMIT_TYPES.keys(), help='Force commit type')
    
    args = parser.parse_args()
    
    if args.auto or args.dry_run:
        staged_files = get_staged_files()
        if not staged_files:
            print("❌ No staged changes.")
            sys.exit(1)
        
        diff = get_staged_diff()
        analysis = analyze_changes(diff, staged_files)
        
        if args.type:
            analysis['type'] = args.type
        
        if args.no_ai:
            message = generate_local_message(analysis, diff)
        else:
            recent = get_recent_commits()
            message = generate_ai_message(diff, staged_files, recent)
            if not message:
                message = generate_local_message(analysis, diff)
        
        if args.dry_run:
            print(f"Message: {message}")
        else:
            commit_with_message(message)
            print(f"✅ Committed: {message.split(chr(10))[0]}")
    else:
        interactive_commit()

if __name__ == '__main__':
    main()
