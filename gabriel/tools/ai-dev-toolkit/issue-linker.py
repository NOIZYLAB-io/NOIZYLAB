#!/usr/bin/env python3
"""
🔗 AI-Powered Issue Linker
Part of GABRIEL AI Dev Toolkit

Automatically links commits to issues:
- Parses commit messages for issue references
- Suggests issue links for commits
- Updates issue status based on commits
- Creates issue-commit relationship reports
- Integrates with GitHub/GitLab/Jira
"""

import argparse
import os
import sys
import json
import re
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class IssueLinker:
    """AI-powered issue-commit linking engine."""
    
    # Common issue reference patterns
    ISSUE_PATTERNS = [
        r'#(\d+)',                           # GitHub style #123
        r'GH-(\d+)',                          # GH-123
        r'fixes?\s*#(\d+)',                   # fixes #123
        r'closes?\s*#(\d+)',                  # closes #123
        r'resolves?\s*#(\d+)',                # resolves #123
        r'refs?\s*#(\d+)',                    # ref #123
        r'relates?\s+to\s*#(\d+)',            # relates to #123
        r'([A-Z]+-\d+)',                      # Jira style ABC-123
        r'issue[:\s]*(\d+)',                  # issue: 123
        r'\[(\d+)\]',                         # [123]
    ]
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        self.provider = self._detect_provider()
        
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
    
    def _detect_provider(self) -> str:
        """Detect issue tracking provider from remote URL."""
        remote = self._run_git('remote', 'get-url', 'origin')
        
        if 'github.com' in remote:
            return 'github'
        elif 'gitlab' in remote:
            return 'gitlab'
        elif 'bitbucket' in remote:
            return 'bitbucket'
        elif 'dev.azure' in remote:
            return 'azure'
        else:
            return 'generic'
    
    def extract_issue_refs(self, text: str) -> List[Dict[str, Any]]:
        """Extract issue references from text."""
        refs = []
        
        for pattern in self.ISSUE_PATTERNS:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                ref = {
                    'raw': match.group(0),
                    'number': match.group(1),
                    'pattern': pattern,
                    'position': match.start()
                }
                
                # Determine action type
                full_match = text[max(0, match.start()-20):match.end()].lower()
                if any(word in full_match for word in ['fix', 'close', 'resolve']):
                    ref['action'] = 'closes'
                elif 'ref' in full_match or 'relate' in full_match:
                    ref['action'] = 'references'
                else:
                    ref['action'] = 'mentions'
                    
                refs.append(ref)
                
        # Deduplicate by issue number
        seen = set()
        unique_refs = []
        for ref in refs:
            if ref['number'] not in seen:
                seen.add(ref['number'])
                unique_refs.append(ref)
                
        return unique_refs
    
    def analyze_commit_for_issues(self, commit_hash: str = 'HEAD') -> Dict[str, Any]:
        """Analyze a commit and find/suggest issue links."""
        # Get commit details
        commit_info = self._run_git(
            'show', commit_hash,
            '--format=%H|%s|%b|%an|%ae|%ai',
            '--stat'
        )
        
        if not commit_info or 'Error' in commit_info:
            return {'error': f'Cannot get commit info: {commit_info}'}
            
        lines = commit_info.split('\n')
        header = lines[0].split('|')
        
        commit_data = {
            'hash': header[0] if len(header) > 0 else '',
            'subject': header[1] if len(header) > 1 else '',
            'body': header[2] if len(header) > 2 else '',
            'author': header[3] if len(header) > 3 else '',
            'email': header[4] if len(header) > 4 else '',
            'date': header[5] if len(header) > 5 else '',
            'files_changed': '\n'.join(lines[1:])
        }
        
        # Extract existing issue references
        full_message = f"{commit_data['subject']} {commit_data['body']}"
        existing_refs = self.extract_issue_refs(full_message)
        
        # Use AI to suggest additional issue links
        suggestions = self._ai_suggest_issues(commit_data)
        
        return {
            'commit': commit_data,
            'existing_references': existing_refs,
            'ai_suggestions': suggestions,
            'timestamp': datetime.now().isoformat()
        }
    
    def _ai_suggest_issues(self, commit_data: Dict) -> Dict[str, Any]:
        """Use Claude to suggest issue links based on commit content."""
        # Get recent issues if gh cli available
        recent_issues = []
        try:
            result = subprocess.run(
                ['gh', 'issue', 'list', '--json', 'number,title,labels', '--limit', '20'],
                capture_output=True, text=True, timeout=10,
                cwd=str(self.repo_path)
            )
            if result.returncode == 0:
                recent_issues = json.loads(result.stdout)
        except Exception:
            pass
            
        prompt = f"""Analyze this commit and suggest which issues it might relate to.

Commit Subject: {commit_data['subject']}
Commit Body: {commit_data['body']}
Files Changed:
{commit_data['files_changed'][:500]}

Recent Open Issues:
{json.dumps(recent_issues, indent=2) if recent_issues else 'No issues available'}

Provide analysis in JSON format:
{{
  "likely_related_issues": [
    {{
      "issue_number": "number or null if new issue needed",
      "confidence": 0.0-1.0,
      "relationship": "fixes/references/relates-to",
      "reasoning": "why this issue is related"
    }}
  ],
  "suggested_new_issues": [
    {{
      "title": "suggested issue title",
      "type": "bug/feature/task/docs",
      "reasoning": "why create this issue"
    }}
  ],
  "commit_type": "feature/bugfix/refactor/docs/test/chore",
  "better_message_suggestion": "improved commit message with issue refs if applicable",
  "breaking_change": true/false,
  "scope": "what part of codebase affected"
}}

Be conservative - only suggest high-confidence matches."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = response.content[0].text
            
            if '```json' in response_text:
                json_str = response_text.split('```json')[1].split('```')[0]
            elif '```' in response_text:
                json_str = response_text.split('```')[1].split('```')[0]
            else:
                json_str = response_text
                
            return json.loads(json_str.strip())
            
        except Exception as e:
            return {'error': str(e)}
    
    def scan_unlinked_commits(self, count: int = 20) -> List[Dict[str, Any]]:
        """Scan recent commits for missing issue links."""
        commits_raw = self._run_git(
            'log', f'-{count}', '--format=%H|%s'
        )
        
        unlinked = []
        for line in commits_raw.split('\n'):
            if not line or '|' not in line:
                continue
                
            hash_val, subject = line.split('|', 1)
            refs = self.extract_issue_refs(subject)
            
            if not refs:
                unlinked.append({
                    'hash': hash_val,
                    'subject': subject,
                    'short_hash': hash_val[:8]
                })
                
        return unlinked
    
    def generate_issue_commit_map(self) -> Dict[str, List[Dict]]:
        """Generate a map of issues to their related commits."""
        # Get all commits with issue references
        commits_raw = self._run_git(
            'log', '-100', '--format=%H|%s|%ai'
        )
        
        issue_map = {}
        
        for line in commits_raw.split('\n'):
            if not line or '|' not in line:
                continue
                
            parts = line.split('|')
            hash_val, subject = parts[0], parts[1]
            date = parts[2] if len(parts) > 2 else ''
            
            refs = self.extract_issue_refs(subject)
            
            for ref in refs:
                issue_num = ref['number']
                if issue_num not in issue_map:
                    issue_map[issue_num] = []
                    
                issue_map[issue_num].append({
                    'hash': hash_val[:8],
                    'subject': subject,
                    'date': date,
                    'action': ref['action']
                })
                
        return issue_map
    
    def link_commit_to_issue(self, commit_hash: str, issue_number: str, action: str = 'references') -> Dict[str, Any]:
        """Create a link between commit and issue (updates commit message or adds comment)."""
        # This would typically update the issue via API
        # For now, we'll generate the amended commit message
        
        current_message = self._run_git('log', '-1', '--format=%B', commit_hash)
        
        # Check if already linked
        existing_refs = self.extract_issue_refs(current_message)
        if any(ref['number'] == issue_number for ref in existing_refs):
            return {
                'status': 'already_linked',
                'message': f'Commit already references #{issue_number}'
            }
            
        # Generate new message
        action_text = {
            'fixes': f'Fixes #{issue_number}',
            'closes': f'Closes #{issue_number}',
            'references': f'Refs #{issue_number}',
            'relates': f'Relates to #{issue_number}'
        }.get(action, f'Refs #{issue_number}')
        
        new_message = f"{current_message.strip()}\n\n{action_text}"
        
        return {
            'status': 'ready',
            'original_message': current_message,
            'new_message': new_message,
            'command': f'git commit --amend -m "{new_message}"',
            'note': 'Use --force-with-lease when pushing if already pushed'
        }
    
    def generate_report(self) -> str:
        """Generate issue-commit relationship report."""
        report = []
        report.append("=" * 70)
        report.append("🔗 ISSUE-COMMIT LINKAGE REPORT")
        report.append(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"📦 Provider: {self.provider.upper()}")
        report.append("=" * 70)
        report.append("")
        
        # Issue-commit map
        issue_map = self.generate_issue_commit_map()
        
        report.append("📊 ISSUE-COMMIT MAP")
        report.append("-" * 40)
        
        if issue_map:
            for issue_num, commits in sorted(issue_map.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 0, reverse=True):
                report.append(f"\n  Issue #{issue_num} ({len(commits)} commits)")
                for commit in commits[:5]:
                    action_icon = '✅' if commit['action'] == 'closes' else '📎' if commit['action'] == 'references' else '💬'
                    report.append(f"    {action_icon} {commit['hash']} - {commit['subject'][:50]}")
        else:
            report.append("  No issue references found in recent commits")
        report.append("")
        
        # Unlinked commits
        unlinked = self.scan_unlinked_commits()
        
        report.append("⚠️ UNLINKED COMMITS")
        report.append("-" * 40)
        
        if unlinked:
            report.append(f"  Found {len(unlinked)} commits without issue references:")
            for commit in unlinked[:10]:
                report.append(f"    • {commit['short_hash']} - {commit['subject'][:50]}")
        else:
            report.append("  ✅ All recent commits have issue references!")
        report.append("")
        
        # Statistics
        total_commits_with_refs = sum(len(commits) for commits in issue_map.values())
        unique_issues = len(issue_map)
        
        report.append("📈 STATISTICS")
        report.append("-" * 40)
        report.append(f"  Unique Issues Referenced: {unique_issues}")
        report.append(f"  Commits with Issue Refs: {total_commits_with_refs}")
        report.append(f"  Unlinked Commits: {len(unlinked)}")
        report.append(f"  Linkage Rate: {total_commits_with_refs / max(total_commits_with_refs + len(unlinked), 1) * 100:.1f}%")
        report.append("")
        
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='🔗 AI-Powered Issue Linker',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              Full linkage report
  %(prog)s --commit HEAD                Analyze specific commit  
  %(prog)s --issue 123                  Find commits for issue
  %(prog)s --unlinked                   List unlinked commits
  %(prog)s --link HEAD 123              Link commit to issue
        """
    )
    
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--commit', '-c', help='Analyze specific commit')
    parser.add_argument('--issue', '-i', help='Find commits for issue number')
    parser.add_argument('--unlinked', action='store_true', help='List unlinked commits')
    parser.add_argument('--link', nargs=2, metavar=('COMMIT', 'ISSUE'), help='Link commit to issue')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    # Check API key
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    linker = IssueLinker(args.path)
    
    if args.commit:
        print(f"🔍 Analyzing commit: {args.commit}")
        analysis = linker.analyze_commit_for_issues(args.commit)
        
        if args.json:
            print(json.dumps(analysis, indent=2))
        else:
            commit = analysis.get('commit', {})
            print(f"\n📝 Commit: {commit.get('hash', '')[:8]}")
            print(f"   Subject: {commit.get('subject', '')}")
            
            existing = analysis.get('existing_references', [])
            if existing:
                print(f"\n🔗 Existing References:")
                for ref in existing:
                    print(f"   • #{ref['number']} ({ref['action']})")
                    
            suggestions = analysis.get('ai_suggestions', {})
            if 'likely_related_issues' in suggestions:
                print(f"\n💡 AI Suggested Links:")
                for sug in suggestions['likely_related_issues']:
                    conf = sug.get('confidence', 0) * 100
                    print(f"   • #{sug.get('issue_number', 'N/A')} ({conf:.0f}% confidence) - {sug.get('reasoning', '')[:50]}")
                    
    elif args.issue:
        print(f"🔍 Finding commits for issue #{args.issue}")
        issue_map = linker.generate_issue_commit_map()
        
        commits = issue_map.get(args.issue, [])
        if commits:
            print(f"\n📎 Found {len(commits)} commits for #{args.issue}:")
            for commit in commits:
                print(f"   • {commit['hash']} - {commit['subject'][:50]} ({commit['action']})")
        else:
            print(f"\n⚠️ No commits found referencing #{args.issue}")
            
    elif args.unlinked:
        print("🔍 Scanning for unlinked commits...")
        unlinked = linker.scan_unlinked_commits()
        
        if args.json:
            print(json.dumps(unlinked, indent=2))
        else:
            print(f"\n⚠️ Found {len(unlinked)} unlinked commits:")
            for commit in unlinked:
                print(f"   • {commit['short_hash']} - {commit['subject'][:50]}")
                
    elif args.link:
        commit_hash, issue_num = args.link
        print(f"🔗 Linking {commit_hash} to #{issue_num}...")
        result = linker.link_commit_to_issue(commit_hash, issue_num)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"\n📋 Status: {result.get('status', 'unknown')}")
            if result.get('command'):
                print(f"🔧 Run: {result['command']}")
                
    else:
        print("🔗 Generating issue-commit report...")
        report = linker.generate_report()
        print(report)


if __name__ == '__main__':
    main()
