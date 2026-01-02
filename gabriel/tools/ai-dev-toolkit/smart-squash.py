#!/usr/bin/env python3
"""
🗜️ AI-Powered Smart Squash Assistant
Part of GABRIEL AI Dev Toolkit

Intelligently squash commits:
- Identifies related commits to squash
- Generates combined commit messages
- Preserves important atomic commits
- Interactive and auto modes
"""

import argparse
import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class SmartSquashAssistant:
    """AI-powered commit squashing assistant."""
    
    # Commits that should typically stay atomic
    ATOMIC_PATTERNS = [
        'breaking change',
        'security fix',
        'hotfix',
        'revert',
        'release',
        'version bump'
    ]
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        
    def _run_git(self, *args) -> str:
        """Run a git command."""
        try:
            result = subprocess.run(
                ['git', '-C', str(self.repo_path)] + list(args),
                capture_output=True, text=True, timeout=30
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Error: {e}"
    
    def get_commits(self, count: int = 20, base_branch: str = None) -> List[Dict[str, Any]]:
        """Get recent commits for analysis."""
        if base_branch:
            current = self._run_git('branch', '--show-current')
            range_spec = f'{base_branch}..{current}'
        else:
            range_spec = f'-{count}'
            
        commits_raw = self._run_git(
            'log', range_spec,
            '--format=%H|%h|%s|%b|%an|%ai|%P'
        )
        
        commits = []
        for line in commits_raw.split('\n'):
            if '|' not in line:
                continue
            parts = line.split('|')
            
            commit = {
                'hash': parts[0],
                'short_hash': parts[1],
                'subject': parts[2],
                'body': parts[3] if len(parts) > 3 else '',
                'author': parts[4] if len(parts) > 4 else '',
                'date': parts[5] if len(parts) > 5 else '',
                'parents': parts[6].split() if len(parts) > 6 else []
            }
            
            # Get files changed
            files = self._run_git('diff-tree', '--no-commit-id', '--name-only', '-r', commit['hash'])
            commit['files'] = files.split('\n') if files else []
            
            commits.append(commit)
            
        return commits
    
    def _is_atomic_commit(self, commit: Dict) -> bool:
        """Check if commit should stay atomic."""
        subject_lower = commit['subject'].lower()
        body_lower = commit.get('body', '').lower()
        full_text = f"{subject_lower} {body_lower}"
        
        for pattern in self.ATOMIC_PATTERNS:
            if pattern in full_text:
                return True
                
        # Merge commits should stay
        if len(commit.get('parents', [])) > 1:
            return True
            
        return False
    
    def analyze_squash_opportunities(self, commits: List[Dict]) -> Dict[str, Any]:
        """Use AI to analyze which commits should be squashed."""
        if not commits:
            return {'error': 'No commits to analyze'}
            
        # Mark atomic commits
        for commit in commits:
            commit['is_atomic'] = self._is_atomic_commit(commit)
            
        prompt = f"""Analyze these commits and suggest which ones should be squashed together.

Commits (oldest to newest):
{json.dumps([{
    'hash': c['short_hash'],
    'subject': c['subject'],
    'body': c['body'][:200],
    'files': c['files'][:10],
    'is_atomic': c['is_atomic']
} for c in commits], indent=2)}

Rules:
1. Commits marked is_atomic=true should NOT be squashed
2. Group related commits that form a single logical change
3. Preserve commits that are good atomic units
4. WIP/fixup/temp commits should be squashed
5. Don't create huge squashed commits - max 5-7 commits per group

Return analysis in JSON format:
{{
  "squash_groups": [
    {{
      "commits": ["hash1", "hash2", "hash3"],
      "reason": "why these should be squashed",
      "suggested_message": "combined commit message"
    }}
  ],
  "keep_separate": [
    {{
      "commit": "hash",
      "reason": "why keep separate"
    }}
  ],
  "summary": "overall squash strategy",
  "commands": ["git commands to execute the squash"]
}}"""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2048,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = response.content[0].text
            
            if '```json' in response_text:
                json_str = response_text.split('```json')[1].split('```')[0]
            elif '```' in response_text:
                json_str = response_text.split('```')[1].split('```')[0]
            else:
                json_str = response_text
                
            analysis = json.loads(json_str.strip())
            analysis['commits_analyzed'] = len(commits)
            analysis['timestamp'] = datetime.now().isoformat()
            
            return analysis
            
        except Exception as e:
            return {'error': str(e)}
    
    def generate_squash_message(self, commit_hashes: List[str]) -> str:
        """Generate a combined commit message for squashed commits."""
        commits = []
        for hash_val in commit_hashes:
            info = self._run_git('log', '-1', '--format=%s|%b', hash_val)
            if info and '|' in info:
                parts = info.split('|')
                commits.append({
                    'subject': parts[0],
                    'body': parts[1] if len(parts) > 1 else ''
                })
        
        if not commits:
            return "Squashed commits"
            
        prompt = f"""Generate a single commit message that summarizes these commits being squashed:

{json.dumps(commits, indent=2)}

Requirements:
1. Follow conventional commit format (type: description)
2. Include emoji if appropriate
3. Be concise but comprehensive
4. Include bullet points for significant changes if needed
5. Max 72 chars for first line

Return ONLY the commit message, nothing else."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text.strip()
        except Exception as e:
            # Fallback to simple combination
            return f"Squash: {commits[0]['subject']} (+{len(commits)-1} more)"
    
    def execute_squash(self, squash_groups: List[Dict], dry_run: bool = True) -> Dict[str, Any]:
        """Execute the squash operations."""
        results = []
        
        for group in squash_groups:
            commits = group['commits']
            if len(commits) < 2:
                continue
                
            message = group.get('suggested_message') or self.generate_squash_message(commits)
            
            if dry_run:
                results.append({
                    'action': 'would_squash',
                    'commits': commits,
                    'message': message,
                    'command': f"git rebase -i {commits[-1]}^"
                })
            else:
                # For actual squash, we'd need to do interactive rebase
                # This is complex and risky, so we generate the commands instead
                results.append({
                    'action': 'command_ready',
                    'commits': commits,
                    'message': message,
                    'instructions': [
                        f"1. Run: git rebase -i {commits[-1]}^",
                        f"2. Change 'pick' to 'squash' for: {', '.join(commits[:-1])}",
                        f"3. Use this message:\n{message}"
                    ]
                })
                
        return {
            'dry_run': dry_run,
            'operations': results,
            'timestamp': datetime.now().isoformat()
        }
    
    def auto_squash_fixups(self) -> Dict[str, Any]:
        """Automatically squash fixup!/squash! commits."""
        # Find fixup commits
        commits = self.get_commits(50)
        fixups = [c for c in commits if c['subject'].startswith(('fixup!', 'squash!'))]
        
        if not fixups:
            return {'message': 'No fixup/squash commits found'}
            
        # Run git's auto-squash
        result = self._run_git('rebase', '-i', '--autosquash', 'HEAD~' + str(len(commits)))
        
        return {
            'fixups_found': len(fixups),
            'result': result
        }
    
    def generate_report(self, commits: List[Dict] = None) -> str:
        """Generate squash analysis report."""
        if commits is None:
            commits = self.get_commits(30)
            
        analysis = self.analyze_squash_opportunities(commits)
        
        report = []
        report.append("=" * 70)
        report.append("🗜️ SMART SQUASH ANALYSIS REPORT")
        report.append(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        if 'error' in analysis:
            report.append(f"❌ Error: {analysis['error']}")
            return '\n'.join(report)
            
        report.append(f"📊 Commits Analyzed: {analysis.get('commits_analyzed', 0)}")
        report.append(f"📝 Strategy: {analysis.get('summary', 'N/A')}")
        report.append("")
        
        # Squash groups
        squash_groups = analysis.get('squash_groups', [])
        if squash_groups:
            report.append("🗜️ RECOMMENDED SQUASHES")
            report.append("-" * 40)
            
            for i, group in enumerate(squash_groups, 1):
                commits_list = group.get('commits', [])
                report.append(f"\n  Group {i}: {len(commits_list)} commits")
                report.append(f"  Commits: {' → '.join(commits_list)}")
                report.append(f"  Reason: {group.get('reason', 'N/A')}")
                report.append(f"  📝 New Message:")
                for line in group.get('suggested_message', 'N/A').split('\n'):
                    report.append(f"     {line}")
            report.append("")
            
        # Keep separate
        keep_separate = analysis.get('keep_separate', [])
        if keep_separate:
            report.append("✅ KEEP SEPARATE (Atomic Commits)")
            report.append("-" * 40)
            
            for item in keep_separate:
                report.append(f"  • {item.get('commit', 'N/A')}: {item.get('reason', '')[:50]}")
            report.append("")
            
        # Commands
        commands = analysis.get('commands', [])
        if commands:
            report.append("⚡ EXECUTION COMMANDS")
            report.append("-" * 40)
            for cmd in commands:
                report.append(f"  $ {cmd}")
            report.append("")
            
        # Summary stats
        total_squashable = sum(len(g.get('commits', [])) for g in squash_groups)
        report.append("📈 SUMMARY")
        report.append("-" * 40)
        report.append(f"  Commits to squash: {total_squashable}")
        report.append(f"  Resulting commits: {len(squash_groups)}")
        report.append(f"  Commits to keep: {len(keep_separate)}")
        report.append(f"  Reduction: {total_squashable - len(squash_groups)} commits")
        report.append("")
        
        report.append("=" * 70)
        report.append("⚠️  Review carefully before executing! Use --dry-run first.")
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='🗜️ AI-Powered Smart Squash Assistant',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          Analyze squash opportunities
  %(prog)s --base main              Analyze commits since main
  %(prog)s --count 50               Analyze last 50 commits
  %(prog)s --execute                Generate squash commands
  %(prog)s --auto-fixup             Auto-squash fixup! commits
  %(prog)s --json                   Output as JSON
        """
    )
    
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--base', '-b', help='Base branch to compare against')
    parser.add_argument('--count', '-c', type=int, default=20, help='Number of commits to analyze')
    parser.add_argument('--execute', action='store_true', help='Generate execution commands')
    parser.add_argument('--auto-fixup', action='store_true', help='Auto-squash fixup commits')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--output', '-o', help='Save to file')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    assistant = SmartSquashAssistant(args.path)
    
    if args.auto_fixup:
        print("🗜️ Auto-squashing fixup commits...")
        result = assistant.auto_squash_fixups()
        print(json.dumps(result, indent=2) if args.json else str(result))
        return
        
    print(f"🗜️ Analyzing commits for squash opportunities...")
    commits = assistant.get_commits(args.count, args.base)
    
    if args.json:
        analysis = assistant.analyze_squash_opportunities(commits)
        output = json.dumps(analysis, indent=2)
    else:
        output = assistant.generate_report(commits)
        
    if args.output:
        Path(args.output).write_text(output)
        print(f"✅ Saved to {args.output}")
    else:
        print(output)
        
    if args.execute and not args.json:
        analysis = assistant.analyze_squash_opportunities(commits)
        squash_groups = analysis.get('squash_groups', [])
        
        if squash_groups:
            print("\n⚡ EXECUTION MODE")
            print("-" * 40)
            exec_result = assistant.execute_squash(squash_groups, dry_run=True)
            
            for op in exec_result['operations']:
                print(f"\n📝 Squash {len(op['commits'])} commits:")
                for inst in op.get('instructions', []):
                    print(f"   {inst}")


if __name__ == '__main__':
    main()
