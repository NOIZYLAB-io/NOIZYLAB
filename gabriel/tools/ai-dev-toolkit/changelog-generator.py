#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  📋 AUTOMATED CHANGELOG GENERATOR v1.0                                        ║
║  Generate structured changelogs from commit history                           ║
║  Part of: NOIZYLAB AI Dev Toolkit                                             ║
║  Updated: 2026-01-02                                                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import subprocess
import os
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field
from collections import defaultdict

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
MODEL = "claude-sonnet-4-20250514"

# Conventional commit type mapping
CHANGELOG_SECTIONS = {
    'feat': '🚀 Features',
    'fix': '🐛 Bug Fixes',
    'perf': '⚡ Performance',
    'docs': '📚 Documentation',
    'refactor': '♻️ Refactoring',
    'test': '🧪 Tests',
    'build': '📦 Build',
    'ci': '🔧 CI/CD',
    'chore': '🧹 Maintenance',
    'security': '🔒 Security',
    'breaking': '💥 Breaking Changes',
    'deprecate': '⚠️ Deprecations',
}

# ═══════════════════════════════════════════════════════════════════════════════
# DATA CLASSES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Commit:
    """Represents a parsed commit."""
    hash: str
    short_hash: str
    author: str
    email: str
    date: datetime
    message: str
    type: str = 'other'
    scope: str = ''
    description: str = ''
    body: str = ''
    breaking: bool = False
    pr_number: Optional[int] = None
    
    def parse_conventional(self):
        """Parse conventional commit format."""
        # Pattern: type(scope)!: description
        pattern = r'^(\w+)(?:\(([^)]+)\))?(!)?\s*:\s*(.+)$'
        match = re.match(pattern, self.message.split('\n')[0])
        
        if match:
            self.type = match.group(1).lower()
            self.scope = match.group(2) or ''
            self.breaking = match.group(3) == '!'
            self.description = match.group(4)
        else:
            self.description = self.message.split('\n')[0]
        
        # Check for PR reference
        pr_match = re.search(r'#(\d+)', self.message)
        if pr_match:
            self.pr_number = int(pr_match.group(1))
        
        # Check for breaking change in body
        if 'BREAKING CHANGE' in self.message:
            self.breaking = True

@dataclass
class Release:
    """Represents a release/version."""
    version: str
    date: datetime
    commits: list = field(default_factory=list)
    
    def add_commit(self, commit: Commit):
        self.commits.append(commit)
    
    def get_grouped_commits(self) -> dict:
        """Group commits by type."""
        groups = defaultdict(list)
        for commit in self.commits:
            groups[commit.type].append(commit)
        return dict(groups)

# ═══════════════════════════════════════════════════════════════════════════════
# GIT HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def get_commits(since: str = None, until: str = None, tag_range: str = None) -> list[Commit]:
    """Get commits from git history."""
    cmd = ['git', 'log', '--format=%H|%h|%an|%ae|%aI|%B%x00']
    
    if tag_range:
        cmd.append(tag_range)
    elif since:
        cmd.extend(['--since', since])
    if until:
        cmd.extend(['--until', until])
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        raw_commits = result.stdout.strip().split('\x00')
        
        commits = []
        for raw in raw_commits:
            if not raw.strip():
                continue
            
            parts = raw.strip().split('|', 5)
            if len(parts) < 6:
                continue
            
            commit = Commit(
                hash=parts[0],
                short_hash=parts[1],
                author=parts[2],
                email=parts[3],
                date=datetime.fromisoformat(parts[4]),
                message=parts[5]
            )
            commit.parse_conventional()
            commits.append(commit)
        
        return commits
    except subprocess.CalledProcessError:
        return []

def get_tags() -> list[tuple[str, datetime]]:
    """Get all tags with dates."""
    try:
        result = subprocess.run(
            ['git', 'tag', '-l', '--sort=-creatordate', '--format=%(refname:short)|%(creatordate:iso)'],
            capture_output=True, text=True, check=True
        )
        
        tags = []
        for line in result.stdout.strip().split('\n'):
            if not line.strip():
                continue
            parts = line.split('|')
            if len(parts) == 2:
                tag = parts[0]
                try:
                    date = datetime.fromisoformat(parts[1].strip())
                except:
                    date = datetime.now()
                tags.append((tag, date))
        
        return tags
    except subprocess.CalledProcessError:
        return []

def get_latest_tag() -> Optional[str]:
    """Get latest tag."""
    try:
        result = subprocess.run(
            ['git', 'describe', '--tags', '--abbrev=0'],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_repo_url() -> Optional[str]:
    """Get repository URL."""
    try:
        result = subprocess.run(
            ['git', 'remote', 'get-url', 'origin'],
            capture_output=True, text=True, check=True
        )
        url = result.stdout.strip()
        # Convert SSH to HTTPS
        if url.startswith('git@'):
            url = url.replace(':', '/').replace('git@', 'https://').replace('.git', '')
        return url.replace('.git', '')
    except subprocess.CalledProcessError:
        return None

# ═══════════════════════════════════════════════════════════════════════════════
# CHANGELOG GENERATION
# ═══════════════════════════════════════════════════════════════════════════════

def generate_changelog_section(commits: list[Commit], repo_url: str = None) -> str:
    """Generate changelog section for a list of commits."""
    grouped = defaultdict(list)
    
    for commit in commits:
        grouped[commit.type].append(commit)
    
    sections = []
    
    # Process in order
    for commit_type, section_title in CHANGELOG_SECTIONS.items():
        if commit_type in grouped:
            section_commits = grouped[commit_type]
            lines = [f"\n### {section_title}\n"]
            
            for commit in section_commits:
                scope = f"**{commit.scope}:** " if commit.scope else ""
                pr_link = f" ([#{commit.pr_number}]({repo_url}/pull/{commit.pr_number}))" if commit.pr_number and repo_url else ""
                commit_link = f" ([{commit.short_hash}]({repo_url}/commit/{commit.hash}))" if repo_url else f" ({commit.short_hash})"
                breaking = " ⚠️ BREAKING" if commit.breaking else ""
                
                lines.append(f"- {scope}{commit.description}{breaking}{pr_link}{commit_link}")
            
            sections.append('\n'.join(lines))
    
    # Handle uncategorized
    uncategorized = [c for c in commits if c.type not in CHANGELOG_SECTIONS]
    if uncategorized:
        lines = ["\n### 📝 Other Changes\n"]
        for commit in uncategorized:
            commit_link = f" ([{commit.short_hash}]({repo_url}/commit/{commit.hash}))" if repo_url else f" ({commit.short_hash})"
            lines.append(f"- {commit.description}{commit_link}")
        sections.append('\n'.join(lines))
    
    return '\n'.join(sections)

def generate_full_changelog(releases: list[Release], repo_url: str = None) -> str:
    """Generate full changelog document."""
    lines = [
        "# Changelog",
        "",
        "All notable changes to this project will be documented in this file.",
        "",
        "The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),",
        "and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).",
        "",
    ]
    
    for release in releases:
        date_str = release.date.strftime('%Y-%m-%d')
        
        if release.version == 'Unreleased':
            lines.append(f"## [{release.version}]")
        else:
            if repo_url:
                lines.append(f"## [{release.version}]({repo_url}/releases/tag/{release.version}) - {date_str}")
            else:
                lines.append(f"## [{release.version}] - {date_str}")
        
        lines.append(generate_changelog_section(release.commits, repo_url))
        lines.append("")
    
    return '\n'.join(lines)

def generate_release_notes(commits: list[Commit], version: str, repo_url: str = None) -> str:
    """Generate release notes for a specific version."""
    lines = [
        f"# Release {version}",
        "",
        f"📅 Released: {datetime.now().strftime('%Y-%m-%d')}",
        "",
    ]
    
    # Summary stats
    feat_count = len([c for c in commits if c.type == 'feat'])
    fix_count = len([c for c in commits if c.type == 'fix'])
    breaking_count = len([c for c in commits if c.breaking])
    
    lines.extend([
        "## 📊 Summary",
        "",
        f"- 🚀 **{feat_count}** new features",
        f"- 🐛 **{fix_count}** bug fixes",
        f"- 💥 **{breaking_count}** breaking changes" if breaking_count else "",
        f"- 📝 **{len(commits)}** total commits",
        "",
    ])
    
    # Breaking changes first
    breaking = [c for c in commits if c.breaking]
    if breaking:
        lines.append("## 💥 Breaking Changes\n")
        for commit in breaking:
            lines.append(f"- **{commit.scope or 'core'}:** {commit.description}")
        lines.append("")
    
    # Then features, fixes, etc.
    lines.append(generate_changelog_section(commits, repo_url))
    
    # Contributors
    authors = set(c.author for c in commits)
    if authors:
        lines.extend([
            "",
            "## 👥 Contributors",
            "",
        ])
        for author in sorted(authors):
            lines.append(f"- {author}")
    
    return '\n'.join(lines)

# ═══════════════════════════════════════════════════════════════════════════════
# AI ENHANCEMENT
# ═══════════════════════════════════════════════════════════════════════════════

def ai_enhance_changelog(changelog: str, commits: list[Commit]) -> str:
    """Use AI to enhance changelog with better descriptions."""
    if not ANTHROPIC_API_KEY:
        return changelog
    
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        prompt = f"""Enhance this changelog to be more user-friendly and readable.

CURRENT CHANGELOG:
{changelog[:8000]}

INSTRUCTIONS:
1. Keep the same structure and format
2. Make descriptions clearer and more user-focused
3. Add brief context where helpful
4. Group related changes if any
5. Keep technical accuracy
6. Don't change links or commit references

Return ONLY the enhanced changelog, maintaining markdown format."""

        response = client.messages.create(
            model=MODEL,
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text.strip()
        
    except Exception as e:
        print(f"AI enhancement error: {e}")
        return changelog

# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Automated Changelog Generator')
    parser.add_argument('--since', '-s', help='Generate from date (YYYY-MM-DD) or tag')
    parser.add_argument('--until', '-u', help='Generate until date or tag')
    parser.add_argument('--version', '-v', help='Version for release notes')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--full', action='store_true', help='Generate full changelog from all tags')
    parser.add_argument('--release-notes', action='store_true', help='Generate release notes format')
    parser.add_argument('--enhance', action='store_true', help='Use AI to enhance descriptions')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown')
    
    args = parser.parse_args()
    
    print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  📋 AUTOMATED CHANGELOG GENERATOR v1.0                                        ║
╚═══════════════════════════════════════════════════════════════════════════════╝
""", file=sys.stderr)
    
    repo_url = get_repo_url()
    
    if args.full:
        # Generate full changelog from tags
        tags = get_tags()
        releases = []
        
        # Add unreleased
        latest_tag = get_latest_tag()
        if latest_tag:
            unreleased = get_commits(tag_range=f'{latest_tag}..HEAD')
            if unreleased:
                releases.append(Release(
                    version='Unreleased',
                    date=datetime.now(),
                    commits=unreleased
                ))
        
        # Add tagged releases
        for i, (tag, date) in enumerate(tags):
            if i + 1 < len(tags):
                commits = get_commits(tag_range=f'{tags[i+1][0]}..{tag}')
            else:
                commits = get_commits(tag_range=tag)
            
            releases.append(Release(version=tag, date=date, commits=commits))
        
        output = generate_full_changelog(releases, repo_url)
        
    elif args.release_notes:
        # Generate release notes
        version = args.version or 'Next Release'
        
        if args.since:
            commits = get_commits(tag_range=f'{args.since}..HEAD')
        else:
            latest_tag = get_latest_tag()
            if latest_tag:
                commits = get_commits(tag_range=f'{latest_tag}..HEAD')
            else:
                commits = get_commits()[:50]  # Last 50 commits
        
        output = generate_release_notes(commits, version, repo_url)
        
    else:
        # Generate changelog for a range
        if args.since and '..' not in args.since:
            commits = get_commits(since=args.since, until=args.until)
        elif args.since:
            commits = get_commits(tag_range=args.since)
        else:
            latest_tag = get_latest_tag()
            if latest_tag:
                commits = get_commits(tag_range=f'{latest_tag}..HEAD')
            else:
                commits = get_commits()[:50]
        
        output = generate_changelog_section(commits, repo_url)
    
    # AI enhancement
    if args.enhance:
        print("🤖 Enhancing with AI...", file=sys.stderr)
        output = ai_enhance_changelog(output, commits if 'commits' in dir() else [])
    
    # Output
    if args.format == 'json':
        import json
        output = json.dumps({
            'changelog': output,
            'generated': datetime.now().isoformat(),
            'repo': repo_url
        }, indent=2)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"✅ Written to {args.output}", file=sys.stderr)
    else:
        print(output)

if __name__ == '__main__':
    main()
