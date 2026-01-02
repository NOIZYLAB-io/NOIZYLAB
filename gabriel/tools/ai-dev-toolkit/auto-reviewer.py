#!/usr/bin/env python3
"""
🤖 Auto-Reviewer
Part of GABRIEL AI Dev Toolkit

Automated code review:
- CI/CD integration
- PR auto-comments
- Quality gates
- Review summaries
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


class AutoReviewer:
    """Automated code review for CI/CD integration."""
    
    # Severity levels for exit codes
    SEVERITY_CODES = {
        'critical': 4,
        'high': 3,
        'medium': 2,
        'low': 1,
        'info': 0
    }
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        
    def _get_git_diff(self, base: str = None, head: str = None) -> str:
        """Get git diff between commits."""
        if base and head:
            cmd = ['git', 'diff', f'{base}...{head}']
        elif base:
            cmd = ['git', 'diff', base]
        else:
            cmd = ['git', 'diff', 'HEAD~1', 'HEAD']
            
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=self.repo_path
        )
        return result.stdout if result.returncode == 0 else ""
    
    def _get_changed_files(self, base: str = None, head: str = None) -> List[str]:
        """Get list of changed files."""
        if base and head:
            cmd = ['git', 'diff', '--name-only', f'{base}...{head}']
        elif base:
            cmd = ['git', 'diff', '--name-only', base]
        else:
            cmd = ['git', 'diff', '--name-only', 'HEAD~1', 'HEAD']
            
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=self.repo_path
        )
        
        if result.returncode == 0:
            return [f for f in result.stdout.strip().split('\n') if f]
        return []
    
    def _get_file_content(self, file_path: str, ref: str = None) -> str:
        """Get file content, optionally at a specific ref."""
        if ref:
            cmd = ['git', 'show', f'{ref}:{file_path}']
            result = subprocess.run(
                cmd, capture_output=True, text=True, cwd=self.repo_path
            )
            if result.returncode == 0:
                return result.stdout
                
        full_path = self.repo_path / file_path
        if full_path.exists():
            return full_path.read_text(encoding='utf-8', errors='ignore')
        return ""
    
    def review_diff(self, base: str = None, head: str = None, 
                    strict: bool = False) -> Dict[str, Any]:
        """Review git diff."""
        diff = self._get_git_diff(base, head)
        changed_files = self._get_changed_files(base, head)
        
        if not diff:
            return {
                'status': 'no_changes',
                'message': 'No changes to review'
            }
            
        prompt = f"""Review this code diff for a pull request.

Changed Files: {', '.join(changed_files[:20])}

Diff:
```diff
{diff[:15000]}
```

Review for:
1. **Bugs**: Logic errors, null pointers, edge cases
2. **Security**: Vulnerabilities, injection risks, auth issues
3. **Performance**: N+1 queries, memory leaks, inefficient code
4. **Code Quality**: Naming, structure, DRY violations
5. **Testing**: Missing tests, untested edge cases
6. **Documentation**: Missing docs, outdated comments

Strictness: {'HIGH - flag all issues' if strict else 'NORMAL - focus on important issues'}

Return JSON:
{{
  "summary": "brief overall assessment",
  "recommendation": "approve/request_changes/comment",
  "issues": [
    {{
      "severity": "critical/high/medium/low/info",
      "category": "bug/security/performance/quality/testing/docs",
      "file": "filename",
      "line": "line number or range",
      "title": "short title",
      "description": "detailed description",
      "suggestion": "how to fix",
      "code_suggestion": "optional code fix"
    }}
  ],
  "highlights": ["positive aspects of the change"],
  "stats": {{
    "files_changed": number,
    "total_issues": number,
    "critical": number,
    "high": number,
    "medium": number,
    "low": number
  }}
}}"""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=8192,
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
            result['reviewed_at'] = datetime.now().isoformat()
            result['base'] = base
            result['head'] = head
            
            # Calculate exit code based on worst severity
            max_severity = 0
            for issue in result.get('issues', []):
                severity_code = self.SEVERITY_CODES.get(issue.get('severity', 'info'), 0)
                max_severity = max(max_severity, severity_code)
            result['exit_code'] = max_severity
            
            return result
            
        except Exception as e:
            return {'error': str(e)}
    
    def review_file(self, file_path: str, context: str = None) -> Dict[str, Any]:
        """Review a specific file."""
        content = self._get_file_content(file_path)
        
        if not content:
            return {'error': f'File not found: {file_path}'}
            
        prompt = f"""Review this file for code quality and issues.

File: {file_path}
{f'Context: {context}' if context else ''}

Code:
```
{content[:12000]}
```

Provide a thorough review covering:
1. Correctness and potential bugs
2. Security vulnerabilities
3. Performance issues
4. Code quality and maintainability
5. Best practices adherence
6. Documentation quality

Return JSON:
{{
  "file": "{file_path}",
  "overall_quality": 0-100,
  "issues": [
    {{
      "severity": "critical/high/medium/low/info",
      "category": "bug/security/performance/quality/docs",
      "line": line_number,
      "title": "issue title",
      "description": "detailed description",
      "suggestion": "fix suggestion"
    }}
  ],
  "strengths": ["good things about the code"],
  "recommendations": ["overall improvements"],
  "verdict": "pass/needs_work/fail"
}}"""

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
                
            return json.loads(json_str.strip())
            
        except Exception as e:
            return {'error': str(e)}
    
    def quality_gate(self, base: str = None, head: str = None,
                     max_critical: int = 0, max_high: int = 2,
                     min_quality: int = 70) -> Dict[str, Any]:
        """Quality gate for CI/CD."""
        review = self.review_diff(base, head, strict=True)
        
        if 'error' in review:
            return review
            
        stats = review.get('stats', {})
        critical = stats.get('critical', 0)
        high = stats.get('high', 0)
        
        # Check gates
        gates = {
            'critical_issues': {
                'passed': critical <= max_critical,
                'actual': critical,
                'threshold': max_critical,
                'message': f'{critical} critical issues (max: {max_critical})'
            },
            'high_issues': {
                'passed': high <= max_high,
                'actual': high,
                'threshold': max_high,
                'message': f'{high} high issues (max: {max_high})'
            }
        }
        
        all_passed = all(g['passed'] for g in gates.values())
        
        return {
            'passed': all_passed,
            'gates': gates,
            'review': review,
            'exit_code': 0 if all_passed else 1
        }
    
    def generate_pr_comment(self, base: str = None, head: str = None) -> str:
        """Generate a PR comment in markdown."""
        review = self.review_diff(base, head)
        
        if 'error' in review:
            return f"❌ Review failed: {review['error']}"
            
        comment = []
        
        # Header
        rec = review.get('recommendation', 'comment')
        if rec == 'approve':
            comment.append("## ✅ AI Review: Approved")
        elif rec == 'request_changes':
            comment.append("## ⚠️ AI Review: Changes Requested")
        else:
            comment.append("## 💬 AI Review: Comments")
            
        comment.append("")
        comment.append(f"_{review.get('summary', '')}_")
        comment.append("")
        
        # Stats
        stats = review.get('stats', {})
        if stats:
            comment.append("### 📊 Summary")
            comment.append(f"- Files changed: {stats.get('files_changed', 0)}")
            comment.append(f"- 🔴 Critical: {stats.get('critical', 0)}")
            comment.append(f"- 🟠 High: {stats.get('high', 0)}")
            comment.append(f"- 🟡 Medium: {stats.get('medium', 0)}")
            comment.append(f"- 🟢 Low: {stats.get('low', 0)}")
            comment.append("")
            
        # Issues
        issues = review.get('issues', [])
        if issues:
            comment.append("### 🔍 Issues Found")
            comment.append("")
            
            # Group by severity
            for severity in ['critical', 'high', 'medium', 'low']:
                severity_issues = [i for i in issues if i.get('severity') == severity]
                if severity_issues:
                    icon = {'critical': '🔴', 'high': '🟠', 'medium': '🟡', 'low': '🟢'}[severity]
                    comment.append(f"#### {icon} {severity.title()}")
                    comment.append("")
                    
                    for issue in severity_issues:
                        comment.append(f"**{issue.get('file', 'Unknown')}:{issue.get('line', '?')}** - {issue.get('title', '')}")
                        comment.append(f"> {issue.get('description', '')}")
                        if issue.get('suggestion'):
                            comment.append(f"> 💡 {issue.get('suggestion')}")
                        if issue.get('code_suggestion'):
                            comment.append(f"```suggestion\n{issue['code_suggestion']}\n```")
                        comment.append("")
                        
        # Highlights
        highlights = review.get('highlights', [])
        if highlights:
            comment.append("### ✨ Highlights")
            for h in highlights:
                comment.append(f"- {h}")
            comment.append("")
            
        # Footer
        comment.append("---")
        comment.append("_Automated review by GABRIEL AI Dev Toolkit_")
        
        return '\n'.join(comment)
    
    def generate_report(self, base: str = None, head: str = None) -> str:
        """Generate terminal report."""
        review = self.review_diff(base, head)
        
        report = []
        report.append("=" * 70)
        report.append("🤖 AUTO-REVIEW REPORT")
        report.append(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        if 'error' in review:
            report.append(f"❌ Error: {review['error']}")
            return '\n'.join(report)
            
        # Recommendation
        rec = review.get('recommendation', 'comment')
        rec_icons = {
            'approve': '✅ APPROVED',
            'request_changes': '⚠️  CHANGES REQUESTED',
            'comment': '💬 COMMENTS'
        }
        report.append(f"📋 RECOMMENDATION: {rec_icons.get(rec, rec)}")
        report.append("")
        report.append(f"📝 {review.get('summary', '')}")
        report.append("")
        
        # Stats
        stats = review.get('stats', {})
        report.append("📊 STATISTICS")
        report.append("-" * 40)
        report.append(f"  Files Changed: {stats.get('files_changed', 0)}")
        report.append(f"  Total Issues:  {stats.get('total_issues', 0)}")
        report.append(f"    🔴 Critical: {stats.get('critical', 0)}")
        report.append(f"    🟠 High:     {stats.get('high', 0)}")
        report.append(f"    🟡 Medium:   {stats.get('medium', 0)}")
        report.append(f"    🟢 Low:      {stats.get('low', 0)}")
        report.append("")
        
        # Issues
        issues = review.get('issues', [])
        if issues:
            report.append("🔍 ISSUES")
            report.append("-" * 40)
            
            for issue in issues[:15]:  # Limit output
                severity_icon = {
                    'critical': '🔴',
                    'high': '🟠',
                    'medium': '🟡',
                    'low': '🟢',
                    'info': '💬'
                }.get(issue.get('severity'), '⚪')
                
                report.append(f"\n{severity_icon} [{issue.get('severity', '?').upper()}] {issue.get('title', 'Issue')}")
                report.append(f"   📁 {issue.get('file', '?')}:{issue.get('line', '?')}")
                report.append(f"   📝 {issue.get('description', '')[:80]}")
                if issue.get('suggestion'):
                    report.append(f"   💡 {issue.get('suggestion')[:80]}")
                    
            if len(issues) > 15:
                report.append(f"\n   ... and {len(issues) - 15} more issues")
            report.append("")
            
        # Highlights
        highlights = review.get('highlights', [])
        if highlights:
            report.append("✨ HIGHLIGHTS")
            report.append("-" * 40)
            for h in highlights:
                report.append(f"  ✅ {h}")
            report.append("")
            
        # Exit code info
        report.append(f"🚪 Exit Code: {review.get('exit_code', 0)}")
        report.append("")
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='🤖 Auto-Reviewer for CI/CD',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           Review last commit
  %(prog)s --base main               Review changes since main
  %(prog)s --base abc123 --head def456
  %(prog)s --file src/api.py         Review specific file
  %(prog)s --gate                    Run quality gate
  %(prog)s --pr-comment              Generate PR comment
        """
    )
    
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--base', '-b', help='Base commit/branch')
    parser.add_argument('--head', help='Head commit/branch')
    parser.add_argument('--file', '-f', help='Review specific file')
    parser.add_argument('--strict', action='store_true', help='Strict review mode')
    parser.add_argument('--gate', action='store_true', help='Quality gate mode')
    parser.add_argument('--max-critical', type=int, default=0, help='Max critical issues')
    parser.add_argument('--max-high', type=int, default=2, help='Max high issues')
    parser.add_argument('--pr-comment', action='store_true', help='Output PR comment')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    reviewer = AutoReviewer(args.path)
    
    if args.file:
        result = reviewer.review_file(args.file)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ {result['error']}")
            else:
                print(f"\n📄 REVIEW: {args.file}")
                print("=" * 50)
                print(f"📊 Quality: {result.get('overall_quality', '?')}/100")
                print(f"📋 Verdict: {result.get('verdict', '?')}")
                
                for issue in result.get('issues', [])[:10]:
                    print(f"\n[{issue.get('severity', '?').upper()}] Line {issue.get('line', '?')}: {issue.get('title', '')}")
                    print(f"  {issue.get('description', '')[:60]}")
                    
        exit_code = 1 if result.get('verdict') == 'fail' else 0
        sys.exit(exit_code)
        
    elif args.gate:
        result = reviewer.quality_gate(
            args.base, args.head,
            max_critical=args.max_critical,
            max_high=args.max_high
        )
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print("\n🚦 QUALITY GATE")
            print("=" * 50)
            
            if result.get('passed'):
                print("✅ PASSED")
            else:
                print("❌ FAILED")
                
            for name, gate in result.get('gates', {}).items():
                icon = '✅' if gate['passed'] else '❌'
                print(f"  {icon} {name}: {gate['message']}")
                
        sys.exit(result.get('exit_code', 1))
        
    elif args.pr_comment:
        comment = reviewer.generate_pr_comment(args.base, args.head)
        print(comment)
        
    else:
        if args.json:
            result = reviewer.review_diff(args.base, args.head, args.strict)
            print(json.dumps(result, indent=2))
            sys.exit(result.get('exit_code', 0))
        else:
            report = reviewer.generate_report(args.base, args.head)
            print(report)
            
            # Get exit code from review
            review = reviewer.review_diff(args.base, args.head)
            sys.exit(review.get('exit_code', 0))


if __name__ == '__main__':
    main()
