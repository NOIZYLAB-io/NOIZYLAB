#!/usr/bin/env python3
"""
📦 AI-Powered Smart Stash Manager
Part of GABRIEL AI Dev Toolkit

Intelligently manage git stashes:
- AI-generated stash descriptions
- Smart stash categorization
- Context-aware stash restore
- Stash search and organization
- Auto-cleanup old stashes
"""

import argparse
import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class SmartStashManager:
    """AI-powered stash management assistant."""
    
    STASH_CATEGORIES = [
        'work-in-progress',
        'experiment',
        'hotfix-prep',
        'context-switch',
        'backup',
        'review-changes',
        'debug-state',
        'feature-partial'
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
    
    def get_stashes(self) -> List[Dict[str, Any]]:
        """Get all stashes with details."""
        stash_list = self._run_git('stash', 'list', '--format=%gd|%gs|%ci')
        
        stashes = []
        for line in stash_list.split('\n'):
            if '|' not in line:
                continue
            parts = line.split('|')
            
            ref = parts[0]
            message = parts[1] if len(parts) > 1 else ''
            date = parts[2] if len(parts) > 2 else ''
            
            # Get stash diff stats
            stats = self._run_git('stash', 'show', '--stat', ref)
            diff = self._run_git('stash', 'show', '-p', ref)
            
            stashes.append({
                'ref': ref,
                'message': message,
                'date': date,
                'stats': stats,
                'diff_preview': diff[:2000] if diff else '',
                'files': self._extract_files(stats)
            })
            
        return stashes
    
    def _extract_files(self, stats: str) -> List[str]:
        """Extract file names from diff stats."""
        files = []
        for line in stats.split('\n'):
            if '|' in line:
                file_part = line.split('|')[0].strip()
                if file_part:
                    files.append(file_part)
        return files
    
    def get_working_changes(self) -> Dict[str, Any]:
        """Get current working directory changes."""
        status = self._run_git('status', '--porcelain')
        diff = self._run_git('diff')
        diff_staged = self._run_git('diff', '--staged')
        
        files = {
            'modified': [],
            'added': [],
            'deleted': [],
            'untracked': []
        }
        
        for line in status.split('\n'):
            if not line:
                continue
            status_code = line[:2]
            file_path = line[3:]
            
            if 'M' in status_code:
                files['modified'].append(file_path)
            elif 'A' in status_code:
                files['added'].append(file_path)
            elif 'D' in status_code:
                files['deleted'].append(file_path)
            elif '?' in status_code:
                files['untracked'].append(file_path)
                
        return {
            'files': files,
            'diff': diff[:5000],
            'diff_staged': diff_staged[:5000],
            'total_changes': sum(len(v) for v in files.values())
        }
    
    def generate_stash_message(self, include_untracked: bool = False) -> str:
        """Generate AI-powered stash message."""
        changes = self.get_working_changes()
        
        if changes['total_changes'] == 0:
            return "No changes to stash"
            
        current_branch = self._run_git('branch', '--show-current')
        
        prompt = f"""Generate a descriptive stash message for these changes.

Branch: {current_branch}

Changed Files:
- Modified: {', '.join(changes['files']['modified'][:10]) or 'None'}
- Added: {', '.join(changes['files']['added'][:10]) or 'None'}  
- Deleted: {', '.join(changes['files']['deleted'][:10]) or 'None'}
- Untracked: {', '.join(changes['files']['untracked'][:10]) or 'None'}

Diff Preview:
```
{changes['diff'][:3000]}
```

Generate a stash message that:
1. Starts with a category: WIP|EXPERIMENT|HOTFIX|BACKUP|FEATURE|DEBUG
2. Describes what was being worked on
3. Is concise but informative (max 80 chars)

Format: [CATEGORY] description

Return ONLY the message, nothing else."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=100,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text.strip()
        except Exception as e:
            # Fallback
            return f"[WIP] Changes on {current_branch} ({changes['total_changes']} files)"
    
    def smart_stash(self, message: str = None, include_untracked: bool = True) -> Dict[str, Any]:
        """Create a stash with AI-generated message."""
        if message is None:
            print("🤖 Generating smart stash message...")
            message = self.generate_stash_message(include_untracked)
            
        args = ['stash', 'push', '-m', message]
        if include_untracked:
            args.append('-u')
            
        result = self._run_git(*args)
        
        return {
            'status': 'success' if 'Saved' in result or not result else 'no_changes',
            'message': message,
            'result': result
        }
    
    def find_relevant_stash(self, context: str = None) -> Dict[str, Any]:
        """Find most relevant stash for current context."""
        stashes = self.get_stashes()
        
        if not stashes:
            return {'error': 'No stashes found'}
            
        current_branch = self._run_git('branch', '--show-current')
        working_changes = self.get_working_changes()
        
        prompt = f"""Find the most relevant stash for the current context.

Current Branch: {current_branch}
Current Changes: {json.dumps(working_changes['files'], indent=2)}
User Context: {context or 'None provided'}

Available Stashes:
{json.dumps([{
    'ref': s['ref'],
    'message': s['message'],
    'date': s['date'],
    'files': s['files'][:5]
} for s in stashes], indent=2)}

Return analysis in JSON format:
{{
  "recommended_stash": "stash@{{n}}" or null,
  "confidence": 0.0-1.0,
  "reason": "why this stash is relevant",
  "alternatives": [
    {{"ref": "stash@{{n}}", "reason": "why relevant"}}
  ],
  "warnings": ["any warnings about applying this stash"]
}}"""

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
    
    def organize_stashes(self) -> Dict[str, Any]:
        """Analyze and organize stashes by category."""
        stashes = self.get_stashes()
        
        if not stashes:
            return {'categories': {}, 'total': 0}
            
        prompt = f"""Categorize these stashes:

{json.dumps([{
    'ref': s['ref'],
    'message': s['message'],
    'date': s['date'],
    'files': s['files'][:5]
} for s in stashes], indent=2)}

Categories: {self.STASH_CATEGORIES}

Return in JSON format:
{{
  "categorized": {{
    "category_name": [
      {{"ref": "stash@{{n}}", "message": "...", "summary": "brief desc"}}
    ]
  }},
  "cleanup_candidates": [
    {{"ref": "stash@{{n}}", "reason": "why it can be cleaned up"}}
  ],
  "important": [
    {{"ref": "stash@{{n}}", "reason": "why this is important to keep"}}
  ]
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
                
            result = json.loads(json_str.strip())
            result['total'] = len(stashes)
            return result
            
        except Exception as e:
            return {'error': str(e)}
    
    def search_stashes(self, query: str) -> List[Dict[str, Any]]:
        """Search stashes using AI understanding."""
        stashes = self.get_stashes()
        
        if not stashes:
            return []
            
        prompt = f"""Search these stashes for: "{query}"

Stashes:
{json.dumps([{
    'ref': s['ref'],
    'message': s['message'],
    'files': s['files'],
    'diff_preview': s['diff_preview'][:500]
} for s in stashes], indent=2)}

Return matching stashes in JSON format:
{{
  "matches": [
    {{
      "ref": "stash@{{n}}",
      "relevance": 0.0-1.0,
      "match_reason": "why this matches the query"
    }}
  ]
}}

Consider semantic meaning, not just exact text matches."""

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
                
            result = json.loads(json_str.strip())
            return result.get('matches', [])
            
        except Exception as e:
            return [{'error': str(e)}]
    
    def cleanup_old_stashes(self, days: int = 30, dry_run: bool = True) -> Dict[str, Any]:
        """Identify and optionally remove old stashes."""
        stashes = self.get_stashes()
        cutoff = datetime.now() - timedelta(days=days)
        
        old_stashes = []
        for stash in stashes:
            try:
                # Parse date
                date_str = stash['date'].split('+')[0].strip()
                stash_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                if stash_date < cutoff:
                    old_stashes.append(stash)
            except Exception:
                continue
                
        results = {
            'old_stashes': len(old_stashes),
            'cutoff_days': days,
            'dry_run': dry_run,
            'stashes': []
        }
        
        for stash in old_stashes:
            if dry_run:
                results['stashes'].append({
                    'ref': stash['ref'],
                    'message': stash['message'],
                    'action': 'would_delete'
                })
            else:
                # Actually delete
                self._run_git('stash', 'drop', stash['ref'])
                results['stashes'].append({
                    'ref': stash['ref'],
                    'action': 'deleted'
                })
                
        return results
    
    def generate_report(self) -> str:
        """Generate stash management report."""
        stashes = self.get_stashes()
        
        report = []
        report.append("=" * 70)
        report.append("📦 SMART STASH MANAGER REPORT")
        report.append(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        if not stashes:
            report.append("✅ No stashes found - working directory clean!")
            return '\n'.join(report)
            
        report.append(f"📊 Total Stashes: {len(stashes)}")
        report.append("")
        
        # List stashes
        report.append("📋 STASH LIST")
        report.append("-" * 40)
        
        for stash in stashes[:15]:
            report.append(f"\n  {stash['ref']}")
            report.append(f"  📝 {stash['message'][:60]}")
            report.append(f"  📅 {stash['date'][:19]}")
            report.append(f"  📁 Files: {len(stash['files'])}")
            
        if len(stashes) > 15:
            report.append(f"\n  ... and {len(stashes) - 15} more")
            
        report.append("")
        
        # Organization
        print("🔍 Analyzing stash organization...")
        org = self.organize_stashes()
        
        if 'categorized' in org:
            report.append("📂 CATEGORIES")
            report.append("-" * 40)
            
            for category, items in org['categorized'].items():
                if items:
                    report.append(f"\n  {category.upper()} ({len(items)})")
                    for item in items[:3]:
                        report.append(f"    • {item.get('ref')}: {item.get('summary', '')[:40]}")
                        
        if org.get('cleanup_candidates'):
            report.append("\n🧹 CLEANUP CANDIDATES")
            report.append("-" * 40)
            
            for item in org['cleanup_candidates'][:5]:
                report.append(f"  • {item.get('ref')}: {item.get('reason', '')[:50]}")
                
        if org.get('important'):
            report.append("\n⭐ IMPORTANT STASHES")
            report.append("-" * 40)
            
            for item in org['important'][:5]:
                report.append(f"  • {item.get('ref')}: {item.get('reason', '')[:50]}")
                
        report.append("")
        report.append("=" * 70)
        report.append("💡 Use --search 'query' to find specific stashes")
        report.append("💡 Use --smart to create stashes with AI descriptions")
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='📦 AI-Powered Smart Stash Manager',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          Show stash report
  %(prog)s --smart                  Create stash with AI message
  %(prog)s --find                   Find relevant stash for context
  %(prog)s --search "auth"          Search stashes
  %(prog)s --organize               Organize stashes by category
  %(prog)s --cleanup --days 30      Find old stashes to cleanup
        """
    )
    
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--smart', action='store_true', help='Create smart stash')
    parser.add_argument('--message', '-m', help='Custom stash message')
    parser.add_argument('--find', action='store_true', help='Find relevant stash')
    parser.add_argument('--context', help='Context for finding stash')
    parser.add_argument('--search', help='Search stashes')
    parser.add_argument('--organize', action='store_true', help='Organize stashes')
    parser.add_argument('--cleanup', action='store_true', help='Cleanup old stashes')
    parser.add_argument('--days', type=int, default=30, help='Days for cleanup cutoff')
    parser.add_argument('--execute', action='store_true', help='Execute cleanup (not dry run)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    manager = SmartStashManager(args.path)
    
    if args.smart:
        print("📦 Creating smart stash...")
        result = manager.smart_stash(args.message)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if result['status'] == 'success':
                print(f"✅ Stashed: {result['message']}")
            else:
                print(f"ℹ️ {result.get('result', 'No changes to stash')}")
                
    elif args.find:
        print("🔍 Finding relevant stash...")
        result = manager.find_relevant_stash(args.context)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if result.get('recommended_stash'):
                conf = result.get('confidence', 0) * 100
                print(f"\n📌 Recommended: {result['recommended_stash']} ({conf:.0f}% confidence)")
                print(f"   Reason: {result.get('reason', 'N/A')}")
                
                if result.get('warnings'):
                    print(f"\n⚠️ Warnings:")
                    for warn in result['warnings']:
                        print(f"   - {warn}")
            else:
                print("❌ No relevant stash found")
                
    elif args.search:
        print(f"🔍 Searching stashes for: {args.search}")
        matches = manager.search_stashes(args.search)
        
        if args.json:
            print(json.dumps(matches, indent=2))
        else:
            if matches:
                print(f"\n📋 Found {len(matches)} matches:")
                for match in matches:
                    rel = match.get('relevance', 0) * 100
                    print(f"  • {match.get('ref')} ({rel:.0f}%): {match.get('match_reason', '')[:50]}")
            else:
                print("No matches found")
                
    elif args.organize:
        print("📂 Organizing stashes...")
        result = manager.organize_stashes()
        print(json.dumps(result, indent=2) if args.json else str(result))
        
    elif args.cleanup:
        print(f"🧹 Finding stashes older than {args.days} days...")
        result = manager.cleanup_old_stashes(args.days, dry_run=not args.execute)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"\n{'Would delete' if result['dry_run'] else 'Deleted'} {result['old_stashes']} stashes:")
            for stash in result['stashes']:
                print(f"  • {stash['ref']}: {stash.get('message', '')[:40]}")
                
            if result['dry_run'] and result['old_stashes'] > 0:
                print("\n💡 Add --execute to actually delete")
                
    else:
        output = manager.generate_report()
        print(output)


if __name__ == '__main__':
    main()
