#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  🔍 AI-POWERED CODE REVIEW v1.0                                               ║
║  Automatically analyze PRs, commits, and code for issues                      ║
║  Part of: NOIZYLAB AI Dev Toolkit                                             ║
║  Updated: 2026-01-02                                                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import subprocess
import json
import os
import sys
import re
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
MODEL = "claude-sonnet-4-20250514"  # Fast + smart for code review

# Code quality patterns to detect
SMELL_PATTERNS = {
    'python': {
        'long_function': (r'def \w+\([^)]*\):', 50),  # Functions > 50 lines
        'magic_numbers': r'(?<!["\'])\b(?<!\.)\d{2,}(?!\.\d)(?!["\'])',
        'bare_except': r'except\s*:',
        'mutable_default': r'def \w+\([^)]*=\s*(\[\]|\{\})',
        'print_debug': r'\bprint\s*\(',
        'todo_fixme': r'#\s*(TODO|FIXME|XXX|HACK)',
        'hardcoded_secrets': r'(api_key|password|secret|token)\s*=\s*["\'][^"\']+["\']',
    },
    'javascript': {
        'console_log': r'console\.(log|debug|info)',
        'var_usage': r'\bvar\s+',
        'callback_hell': r'}\s*\)\s*;?\s*}\s*\)\s*;?\s*}',
        'magic_numbers': r'(?<!["\'])\b(?<!\.)\d{2,}(?!\.\d)(?!["\'])',
        'any_type': r':\s*any\b',
        'todo_fixme': r'//\s*(TODO|FIXME|XXX|HACK)',
    },
    'sql': {
        'select_star': r'SELECT\s+\*',
        'no_where': r'DELETE\s+FROM\s+\w+\s*(?!WHERE)',
        'sql_injection': r'"\s*\+\s*\w+\s*\+\s*"',
    }
}

SECURITY_PATTERNS = [
    (r'eval\s*\(', 'CRITICAL: eval() is dangerous'),
    (r'exec\s*\(', 'CRITICAL: exec() is dangerous'),
    (r'__import__\s*\(', 'WARNING: Dynamic import'),
    (r'subprocess\.call\([^)]*shell\s*=\s*True', 'CRITICAL: Shell injection risk'),
    (r'os\.system\s*\(', 'WARNING: Prefer subprocess'),
    (r'pickle\.loads?\s*\(', 'WARNING: Pickle can execute arbitrary code'),
    (r'yaml\.load\s*\([^)]*(?!Loader)', 'CRITICAL: Use yaml.safe_load'),
    (r'password\s*=\s*["\'][^"\']+["\']', 'CRITICAL: Hardcoded password'),
    (r'api_key\s*=\s*["\'][^"\']+["\']', 'CRITICAL: Hardcoded API key'),
]

# ═══════════════════════════════════════════════════════════════════════════════
# DATA CLASSES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Issue:
    """Represents a code issue found during review."""
    file: str
    line: int
    severity: str  # CRITICAL, WARNING, INFO, STYLE
    category: str
    message: str
    suggestion: str = ""
    
    def to_dict(self) -> dict:
        return {
            'file': self.file,
            'line': self.line,
            'severity': self.severity,
            'category': self.category,
            'message': self.message,
            'suggestion': self.suggestion
        }

@dataclass
class ReviewResult:
    """Complete code review result."""
    files_reviewed: int = 0
    issues: list = field(default_factory=list)
    score: int = 100
    summary: str = ""
    ai_suggestions: list = field(default_factory=list)
    
    def add_issue(self, issue: Issue):
        self.issues.append(issue)
        # Deduct points based on severity
        if issue.severity == 'CRITICAL':
            self.score -= 15
        elif issue.severity == 'WARNING':
            self.score -= 5
        elif issue.severity == 'INFO':
            self.score -= 2
        self.score = max(0, self.score)

# ═══════════════════════════════════════════════════════════════════════════════
# GIT HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def get_changed_files(base_branch: str = "main") -> list[str]:
    """Get list of changed files compared to base branch."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', base_branch],
            capture_output=True, text=True, check=True
        )
        return [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]
    except subprocess.CalledProcessError:
        return []

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

def get_diff(file_path: str, base_branch: str = "main") -> str:
    """Get diff for a specific file."""
    try:
        result = subprocess.run(
            ['git', 'diff', base_branch, '--', file_path],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return ""

def get_file_content(file_path: str) -> str:
    """Read file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return ""

# ═══════════════════════════════════════════════════════════════════════════════
# STATIC ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

def detect_language(file_path: str) -> str:
    """Detect programming language from file extension."""
    ext_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'javascript',
        '.jsx': 'javascript',
        '.tsx': 'javascript',
        '.sql': 'sql',
        '.sh': 'bash',
        '.bash': 'bash',
    }
    ext = Path(file_path).suffix.lower()
    return ext_map.get(ext, 'unknown')

def analyze_code_smells(file_path: str, content: str) -> list[Issue]:
    """Detect code smells and anti-patterns."""
    issues = []
    language = detect_language(file_path)
    patterns = SMELL_PATTERNS.get(language, {})
    
    lines = content.split('\n')
    
    for pattern_name, pattern_data in patterns.items():
        if isinstance(pattern_data, tuple):
            pattern, threshold = pattern_data
        else:
            pattern = pattern_data
            threshold = None
        
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line):
                issues.append(Issue(
                    file=file_path,
                    line=i,
                    severity='INFO',
                    category='code_smell',
                    message=f"Detected: {pattern_name.replace('_', ' ')}",
                    suggestion=get_smell_suggestion(pattern_name)
                ))
    
    return issues

def analyze_security(file_path: str, content: str) -> list[Issue]:
    """Detect security vulnerabilities."""
    issues = []
    lines = content.split('\n')
    
    for pattern, message in SECURITY_PATTERNS:
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                severity = 'CRITICAL' if 'CRITICAL' in message else 'WARNING'
                issues.append(Issue(
                    file=file_path,
                    line=i,
                    severity=severity,
                    category='security',
                    message=message,
                    suggestion="Review and fix this security issue immediately"
                ))
    
    return issues

def analyze_complexity(file_path: str, content: str) -> list[Issue]:
    """Analyze code complexity."""
    issues = []
    language = detect_language(file_path)
    lines = content.split('\n')
    
    # Check function length
    if language == 'python':
        in_function = False
        func_start = 0
        func_name = ""
        indent_level = 0
        
        for i, line in enumerate(lines, 1):
            match = re.match(r'^(\s*)def (\w+)\(', line)
            if match:
                if in_function and (i - func_start) > 50:
                    issues.append(Issue(
                        file=file_path,
                        line=func_start,
                        severity='WARNING',
                        category='complexity',
                        message=f"Function '{func_name}' is {i - func_start} lines (> 50)",
                        suggestion="Consider breaking into smaller functions"
                    ))
                in_function = True
                func_start = i
                func_name = match.group(2)
                indent_level = len(match.group(1))
    
    # Check file length
    if len(lines) > 500:
        issues.append(Issue(
            file=file_path,
            line=1,
            severity='INFO',
            category='complexity',
            message=f"File has {len(lines)} lines (> 500)",
            suggestion="Consider splitting into multiple modules"
        ))
    
    return issues

def get_smell_suggestion(smell_name: str) -> str:
    """Get suggestion for a code smell."""
    suggestions = {
        'magic_numbers': "Extract to named constant",
        'bare_except': "Catch specific exceptions",
        'mutable_default': "Use None as default, create in function body",
        'print_debug': "Use logging module instead",
        'todo_fixme': "Create issue to track this",
        'hardcoded_secrets': "Use environment variables",
        'console_log': "Remove debug logging",
        'var_usage': "Use const or let instead",
        'callback_hell': "Use async/await or Promises",
        'any_type': "Use specific types",
        'select_star': "Specify columns explicitly",
        'no_where': "Add WHERE clause to prevent full table operation",
        'sql_injection': "Use parameterized queries",
    }
    return suggestions.get(smell_name, "Review and refactor")

# ═══════════════════════════════════════════════════════════════════════════════
# AI ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

def ai_review_code(diff: str, file_path: str) -> list[str]:
    """Use AI to review code changes."""
    if not ANTHROPIC_API_KEY:
        return ["⚠️ ANTHROPIC_API_KEY not set - AI review skipped"]
    
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        prompt = f"""Review this code diff and provide specific, actionable feedback.
Focus on:
1. Potential bugs or logic errors
2. Security vulnerabilities
3. Performance issues
4. Code clarity and maintainability
5. Missing error handling

File: {file_path}

Diff:
```
{diff[:8000]}  # Truncate for API limits
```

Provide 3-5 specific suggestions. Be concise. Format as bullet points."""

        response = client.messages.create(
            model=MODEL,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        suggestions = response.content[0].text.strip().split('\n')
        return [s.strip() for s in suggestions if s.strip()]
        
    except Exception as e:
        return [f"AI review error: {str(e)}"]

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN REVIEW FUNCTION
# ═══════════════════════════════════════════════════════════════════════════════

def review_pr(base_branch: str = "main", use_ai: bool = True) -> ReviewResult:
    """Perform comprehensive PR review."""
    result = ReviewResult()
    
    changed_files = get_changed_files(base_branch)
    if not changed_files:
        changed_files = get_staged_files()
    
    print(f"\n🔍 Reviewing {len(changed_files)} files...\n")
    
    for file_path in changed_files:
        if not os.path.exists(file_path):
            continue
            
        result.files_reviewed += 1
        content = get_file_content(file_path)
        
        if not content:
            continue
        
        print(f"  📄 {file_path}")
        
        # Static analysis
        result.issues.extend(analyze_code_smells(file_path, content))
        result.issues.extend(analyze_security(file_path, content))
        result.issues.extend(analyze_complexity(file_path, content))
        
        # AI review (if enabled)
        if use_ai:
            diff = get_diff(file_path, base_branch)
            if diff:
                suggestions = ai_review_code(diff, file_path)
                result.ai_suggestions.extend(suggestions)
    
    # Calculate final score
    for issue in result.issues:
        if issue.severity == 'CRITICAL':
            result.score -= 15
        elif issue.severity == 'WARNING':
            result.score -= 5
        elif issue.severity == 'INFO':
            result.score -= 2
    result.score = max(0, result.score)
    
    # Generate summary
    critical = len([i for i in result.issues if i.severity == 'CRITICAL'])
    warnings = len([i for i in result.issues if i.severity == 'WARNING'])
    info = len([i for i in result.issues if i.severity == 'INFO'])
    
    result.summary = f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  📊 CODE REVIEW SUMMARY                                                       ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  Files Reviewed: {result.files_reviewed:3}                                                     ║
║  Quality Score:  {result.score:3}/100 {'🟢' if result.score >= 80 else '🟡' if result.score >= 60 else '🔴'}                                                    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  🔴 Critical:    {critical:3}                                                         ║
║  🟡 Warnings:    {warnings:3}                                                         ║
║  🔵 Info:        {info:3}                                                         ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
    
    return result

def print_review(result: ReviewResult):
    """Print formatted review results."""
    print(result.summary)
    
    if result.issues:
        print("\n📋 ISSUES FOUND:\n")
        for issue in sorted(result.issues, key=lambda x: (x.severity != 'CRITICAL', x.severity != 'WARNING', x.file)):
            icon = {'CRITICAL': '🔴', 'WARNING': '🟡', 'INFO': '🔵', 'STYLE': '⚪'}.get(issue.severity, '⚪')
            print(f"  {icon} [{issue.severity}] {issue.file}:{issue.line}")
            print(f"     {issue.message}")
            if issue.suggestion:
                print(f"     💡 {issue.suggestion}")
            print()
    
    if result.ai_suggestions:
        print("\n🤖 AI SUGGESTIONS:\n")
        for suggestion in result.ai_suggestions:
            print(f"  • {suggestion}")
        print()

# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='AI-Powered Code Review')
    parser.add_argument('--base', '-b', default='main', help='Base branch for comparison')
    parser.add_argument('--no-ai', action='store_true', help='Skip AI analysis')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--file', '-f', help='Review specific file')
    
    args = parser.parse_args()
    
    print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  🔍 AI-POWERED CODE REVIEW v1.0                                               ║
║  NOIZYLAB Dev Toolkit                                                         ║
╚═══════════════════════════════════════════════════════════════════════════════╝
""")
    
    result = review_pr(base_branch=args.base, use_ai=not args.no_ai)
    
    if args.json:
        output = {
            'files_reviewed': result.files_reviewed,
            'score': result.score,
            'issues': [i.to_dict() for i in result.issues],
            'ai_suggestions': result.ai_suggestions
        }
        print(json.dumps(output, indent=2))
    else:
        print_review(result)
    
    # Exit with error code if critical issues found
    critical = len([i for i in result.issues if i.severity == 'CRITICAL'])
    sys.exit(1 if critical > 0 else 0)

if __name__ == '__main__':
    main()
