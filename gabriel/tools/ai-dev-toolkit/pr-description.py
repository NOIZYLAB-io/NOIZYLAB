#!/usr/bin/env python3
"""
📝 AI-Powered PR Description Generator
Part of GABRIEL AI Dev Toolkit

Automatically generates comprehensive PR descriptions:
- Analyzes commits and code changes
- Creates structured descriptions
- Adds testing instructions
- Links related issues
- Generates review checklists
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


class PRDescriptionGenerator:
    """AI-powered PR description generation engine."""
    
    PR_TEMPLATES = {
        'feature': """## 🚀 Feature: {title}

### Summary
{summary}

### Changes Made
{changes}

### Screenshots/Demos
<!-- Add screenshots if applicable -->

### Testing Instructions
{testing}

### Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes (or documented)

### Related Issues
{issues}

### Additional Notes
{notes}
""",
        'bugfix': """## 🐛 Bug Fix: {title}

### Problem
{problem}

### Root Cause
{root_cause}

### Solution
{solution}

### Changes Made
{changes}

### Testing Instructions
{testing}

### Regression Testing
{regression}

### Checklist
- [ ] Bug is reproducible before fix
- [ ] Bug is fixed after changes
- [ ] No new bugs introduced
- [ ] Tests added for this scenario

### Related Issues
{issues}
""",
        'refactor': """## ♻️ Refactor: {title}

### Motivation
{motivation}

### Changes Made
{changes}

### Before/After
{comparison}

### Performance Impact
{performance}

### Testing Instructions
{testing}

### Checklist
- [ ] Behavior unchanged
- [ ] Tests still pass
- [ ] No performance regression
- [ ] Code is cleaner/more maintainable

### Related Issues
{issues}
""",
        'docs': """## 📚 Documentation: {title}

### Summary
{summary}

### Changes Made
{changes}

### Preview
{preview}

### Checklist
- [ ] Grammar/spelling checked
- [ ] Links verified
- [ ] Examples tested
- [ ] Formatting correct
"""
    }
    
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
    
    def get_branch_info(self) -> Dict[str, Any]:
        """Get current branch information."""
        current_branch = self._run_git('branch', '--show-current')
        base_branch = self._detect_base_branch()
        
        # Get commits between base and current
        commits_raw = self._run_git(
            'log', f'{base_branch}..{current_branch}',
            '--format=%H|%s|%b|%an|%ai',
            '--reverse'
        )
        
        commits = []
        for line in commits_raw.split('\n'):
            if '|' in line:
                parts = line.split('|')
                commits.append({
                    'hash': parts[0][:8],
                    'subject': parts[1],
                    'body': parts[2] if len(parts) > 2 else '',
                    'author': parts[3] if len(parts) > 3 else '',
                    'date': parts[4] if len(parts) > 4 else ''
                })
        
        # Get diff stats
        diff_stat = self._run_git('diff', '--stat', f'{base_branch}...{current_branch}')
        diff_files = self._run_git('diff', '--name-status', f'{base_branch}...{current_branch}')
        
        # Get actual diff (limited)
        diff_content = self._run_git('diff', f'{base_branch}...{current_branch}')
        
        return {
            'current_branch': current_branch,
            'base_branch': base_branch,
            'commits': commits,
            'commit_count': len(commits),
            'diff_stat': diff_stat,
            'diff_files': diff_files,
            'diff_content': diff_content[:20000],  # Limit diff size
            'files_changed': len(diff_files.split('\n')) if diff_files else 0
        }
    
    def _detect_base_branch(self) -> str:
        """Detect the most likely base branch."""
        # Check common base branches
        for branch in ['main', 'master', 'develop', 'dev']:
            result = self._run_git('rev-parse', '--verify', branch)
            if 'Error' not in result and result:
                return branch
        return 'main'
    
    def _detect_pr_type(self, branch_info: Dict) -> str:
        """Detect PR type from branch name and commits."""
        branch = branch_info['current_branch'].lower()
        
        if any(prefix in branch for prefix in ['feat', 'feature', 'add']):
            return 'feature'
        elif any(prefix in branch for prefix in ['fix', 'bug', 'hotfix', 'patch']):
            return 'bugfix'
        elif any(prefix in branch for prefix in ['refactor', 'cleanup', 'improve']):
            return 'refactor'
        elif any(prefix in branch for prefix in ['docs', 'doc', 'readme']):
            return 'docs'
        
        # Check commit messages
        subjects = ' '.join([c['subject'].lower() for c in branch_info['commits']])
        if 'fix' in subjects:
            return 'bugfix'
        elif 'refactor' in subjects:
            return 'refactor'
        elif 'doc' in subjects:
            return 'docs'
        
        return 'feature'
    
    def _extract_issue_refs(self, text: str) -> List[str]:
        """Extract issue references from text."""
        import re
        patterns = [
            r'#(\d+)',
            r'([A-Z]+-\d+)',  # Jira style
            r'(?:fixes?|closes?|resolves?)\s*#?(\d+)'
        ]
        
        refs = set()
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            refs.update(matches)
        
        return list(refs)
    
    def generate_description(self, custom_title: str = None) -> Dict[str, Any]:
        """Generate comprehensive PR description using AI."""
        branch_info = self.get_branch_info()
        pr_type = self._detect_pr_type(branch_info)
        
        # Collect issue references from commits
        all_text = ' '.join([f"{c['subject']} {c['body']}" for c in branch_info['commits']])
        all_text += ' ' + branch_info['current_branch']
        issue_refs = self._extract_issue_refs(all_text)
        
        prompt = f"""Generate a comprehensive PR description for this pull request.

Branch: {branch_info['current_branch']} → {branch_info['base_branch']}
PR Type: {pr_type}
Commits ({branch_info['commit_count']}):
{json.dumps(branch_info['commits'], indent=2)}

Files Changed:
{branch_info['diff_files']}

Diff Statistics:
{branch_info['diff_stat']}

Code Changes (partial):
```
{branch_info['diff_content'][:10000]}
```

Generate a PR description in JSON format:
{{
  "title": "concise PR title",
  "type": "{pr_type}",
  "summary": "2-3 sentence summary of what this PR does",
  "changes": [
    "bullet point for each significant change"
  ],
  "testing_instructions": [
    "step by step testing instructions"
  ],
  "breaking_changes": ["list any breaking changes or null"],
  "related_issues": {json.dumps(issue_refs) if issue_refs else "[]"},
  "review_focus": ["areas reviewers should focus on"],
  "additional_notes": "any other relevant info",
  
  // For bugfix type:
  "problem": "description of the bug (if bugfix)",
  "root_cause": "what caused the bug (if bugfix)",
  "solution": "how it was fixed (if bugfix)",
  
  // For refactor type:
  "motivation": "why refactoring (if refactor)",
  "comparison": "before/after comparison (if refactor)",
  "performance_impact": "any performance changes (if refactor)"
}}

Be specific and technical. Reference actual file names and function names from the diff."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = response.content[0].text
            
            if '```json' in response_text:
                json_str = response_text.split('```json')[1].split('```')[0]
            elif '```' in response_text:
                json_str = response_text.split('```')[1].split('```')[0]
            else:
                json_str = response_text
                
            ai_response = json.loads(json_str.strip())
            
            # Override title if provided
            if custom_title:
                ai_response['title'] = custom_title
                
            return {
                'branch_info': branch_info,
                'ai_response': ai_response,
                'pr_type': pr_type,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                'error': str(e),
                'branch_info': branch_info
            }
    
    def format_description(self, result: Dict[str, Any]) -> str:
        """Format the AI response into a PR description."""
        if 'error' in result:
            return f"Error generating description: {result['error']}"
            
        ai = result['ai_response']
        pr_type = result['pr_type']
        
        # Build changes list
        changes = '\n'.join([f"- {change}" for change in ai.get('changes', [])])
        
        # Build testing instructions
        testing = '\n'.join([f"{i+1}. {step}" for i, step in enumerate(ai.get('testing_instructions', []))])
        
        # Build issues list
        issues = ai.get('related_issues', [])
        if issues:
            issues_str = ', '.join([f"#{i}" if i.isdigit() else i for i in issues])
        else:
            issues_str = "None"
        
        # Build additional notes
        notes = ai.get('additional_notes', '')
        if ai.get('breaking_changes'):
            notes += "\n\n⚠️ **Breaking Changes:**\n" + '\n'.join([f"- {bc}" for bc in ai['breaking_changes']])
        
        if ai.get('review_focus'):
            notes += "\n\n👀 **Review Focus:**\n" + '\n'.join([f"- {rf}" for rf in ai['review_focus']])
        
        if pr_type == 'feature':
            return self.PR_TEMPLATES['feature'].format(
                title=ai.get('title', 'Feature'),
                summary=ai.get('summary', ''),
                changes=changes,
                testing=testing,
                issues=issues_str,
                notes=notes
            )
        elif pr_type == 'bugfix':
            return self.PR_TEMPLATES['bugfix'].format(
                title=ai.get('title', 'Bug Fix'),
                problem=ai.get('problem', 'Bug description'),
                root_cause=ai.get('root_cause', 'Investigation needed'),
                solution=ai.get('solution', 'Fix applied'),
                changes=changes,
                testing=testing,
                regression=ai.get('regression', 'Standard regression testing'),
                issues=issues_str
            )
        elif pr_type == 'refactor':
            return self.PR_TEMPLATES['refactor'].format(
                title=ai.get('title', 'Refactor'),
                motivation=ai.get('motivation', 'Code improvement'),
                changes=changes,
                comparison=ai.get('comparison', 'See diff for details'),
                performance=ai.get('performance_impact', 'No significant impact expected'),
                testing=testing,
                issues=issues_str
            )
        else:
            return self.PR_TEMPLATES['docs'].format(
                title=ai.get('title', 'Documentation Update'),
                summary=ai.get('summary', ''),
                changes=changes,
                preview=ai.get('preview', 'See changed files')
            )
    
    def create_pr(self, description: str, title: str = None, draft: bool = False) -> Dict[str, Any]:
        """Create PR using gh CLI."""
        try:
            cmd = ['gh', 'pr', 'create', '--body', description]
            
            if title:
                cmd.extend(['--title', title])
            if draft:
                cmd.append('--draft')
                
            result = subprocess.run(
                cmd,
                capture_output=True, text=True, timeout=60,
                cwd=str(self.repo_path)
            )
            
            if result.returncode == 0:
                return {
                    'status': 'created',
                    'url': result.stdout.strip(),
                    'output': result.stdout
                }
            else:
                return {
                    'status': 'error',
                    'error': result.stderr
                }
                
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e)
            }
    
    def generate_quick_description(self) -> str:
        """Generate a quick one-liner PR description."""
        branch_info = self.get_branch_info()
        
        commits = branch_info['commits']
        if not commits:
            return "No commits found"
            
        if len(commits) == 1:
            return commits[0]['subject']
            
        # Summarize multiple commits
        subjects = [c['subject'] for c in commits[:10]]
        
        prompt = f"""Summarize these commits into a single PR title (max 72 chars):

{chr(10).join(subjects)}

Return ONLY the title, nothing else."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=100,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text.strip()
        except Exception:
            return f"Multiple changes ({len(commits)} commits)"


def main():
    parser = argparse.ArgumentParser(
        description='📝 AI-Powered PR Description Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                      Generate PR description
  %(prog)s --create             Generate and create PR
  %(prog)s --create --draft     Create as draft PR
  %(prog)s --title "My PR"      Use custom title
  %(prog)s --quick              Quick one-liner title only
  %(prog)s --json               Output as JSON
        """
    )
    
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--title', '-t', help='Custom PR title')
    parser.add_argument('--create', action='store_true', help='Create PR after generating')
    parser.add_argument('--draft', action='store_true', help='Create as draft PR')
    parser.add_argument('--quick', action='store_true', help='Quick one-liner only')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--output', '-o', help='Save to file')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    generator = PRDescriptionGenerator(args.path)
    
    if args.quick:
        print("📝 Generating quick PR title...")
        title = generator.generate_quick_description()
        print(f"\n📌 {title}")
        return
        
    print("📝 Analyzing branch and generating PR description...")
    result = generator.generate_description(args.title)
    
    if args.json:
        output = json.dumps(result, indent=2)
    else:
        output = generator.format_description(result)
        
        # Print branch info
        bi = result.get('branch_info', {})
        print(f"\n📊 Branch: {bi.get('current_branch')} → {bi.get('base_branch')}")
        print(f"📈 Commits: {bi.get('commit_count')}, Files: {bi.get('files_changed')}")
        print("\n" + "=" * 60)
        
    if args.output:
        Path(args.output).write_text(output)
        print(f"✅ Saved to {args.output}")
    else:
        print(output)
        
    if args.create:
        print("\n🚀 Creating PR...")
        title = result.get('ai_response', {}).get('title', args.title)
        pr_result = generator.create_pr(output, title, args.draft)
        
        if pr_result['status'] == 'created':
            print(f"✅ PR created: {pr_result['url']}")
        else:
            print(f"❌ Error: {pr_result.get('error')}")


if __name__ == '__main__':
    main()
