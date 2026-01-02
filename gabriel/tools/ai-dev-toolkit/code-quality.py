#!/usr/bin/env python3
"""
🔍 AI-Powered Code Quality Analyzer
Part of GABRIEL AI Dev Toolkit

Performs deep code analysis using Claude AI:
- Complexity metrics
- Code smell detection
- Refactoring suggestions
- Best practices validation
- Security vulnerability scanning
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


class CodeQualityAnalyzer:
    """AI-powered code quality analysis engine."""
    
    QUALITY_THRESHOLDS = {
        'cyclomatic_complexity': 10,
        'function_length': 50,
        'file_length': 500,
        'nesting_depth': 4,
        'parameter_count': 5
    }
    
    CODE_SMELLS = [
        'Long Method',
        'Large Class',
        'Feature Envy',
        'Data Clumps',
        'Dead Code',
        'Speculative Generality',
        'Duplicate Code',
        'Magic Numbers',
        'Shotgun Surgery',
        'Divergent Change',
        'Parallel Inheritance',
        'Lazy Class',
        'Temporary Field',
        'Message Chains',
        'Middle Man',
        'Inappropriate Intimacy',
        'Alternative Classes',
        'Incomplete Library',
        'Data Class',
        'Refused Bequest',
        'Comments (excessive)'
    ]
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        self.results = []
        
    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """Analyze a single file for code quality issues."""
        path = Path(file_path)
        if not path.exists():
            return {'error': f'File not found: {file_path}'}
            
        try:
            content = path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': f'Cannot read file: {e}'}
            
        # Get file extension for language detection
        ext = path.suffix.lower()
        language = self._detect_language(ext)
        
        # Gather basic metrics
        metrics = self._calculate_metrics(content, language)
        
        # AI-powered analysis
        ai_analysis = self._ai_analyze(content, language, path.name)
        
        return {
            'file': str(path.relative_to(self.repo_path)),
            'language': language,
            'metrics': metrics,
            'ai_analysis': ai_analysis,
            'timestamp': datetime.now().isoformat()
        }
    
    def analyze_directory(self, dir_path: str = '.', extensions: List[str] = None) -> List[Dict]:
        """Analyze all files in a directory."""
        path = Path(dir_path)
        if not path.exists():
            return [{'error': f'Directory not found: {dir_path}'}]
            
        if extensions is None:
            extensions = ['.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.go', '.rs']
            
        results = []
        for file_path in path.rglob('*'):
            if file_path.suffix.lower() in extensions:
                # Skip common non-source directories
                if any(skip in str(file_path) for skip in ['node_modules', '.git', '__pycache__', 'venv', 'dist', 'build']):
                    continue
                results.append(self.analyze_file(str(file_path)))
                
        return results
    
    def _detect_language(self, extension: str) -> str:
        """Detect programming language from file extension."""
        mapping = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.jsx': 'React JSX',
            '.tsx': 'React TSX',
            '.java': 'Java',
            '.cpp': 'C++',
            '.c': 'C',
            '.go': 'Go',
            '.rs': 'Rust',
            '.rb': 'Ruby',
            '.php': 'PHP',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.scala': 'Scala',
            '.sh': 'Shell',
            '.sql': 'SQL'
        }
        return mapping.get(extension, 'Unknown')
    
    def _calculate_metrics(self, content: str, language: str) -> Dict[str, Any]:
        """Calculate basic code metrics."""
        lines = content.split('\n')
        
        # Basic counts
        total_lines = len(lines)
        blank_lines = sum(1 for line in lines if not line.strip())
        comment_lines = self._count_comments(content, language)
        code_lines = total_lines - blank_lines - comment_lines
        
        # Complexity indicators
        nesting_depth = self._estimate_nesting(content)
        function_count = self._count_functions(content, language)
        class_count = self._count_classes(content, language)
        
        return {
            'total_lines': total_lines,
            'code_lines': code_lines,
            'blank_lines': blank_lines,
            'comment_lines': comment_lines,
            'comment_ratio': round(comment_lines / max(code_lines, 1) * 100, 2),
            'max_nesting_depth': nesting_depth,
            'function_count': function_count,
            'class_count': class_count,
            'avg_function_length': round(code_lines / max(function_count, 1), 2)
        }
    
    def _count_comments(self, content: str, language: str) -> int:
        """Count comment lines based on language."""
        lines = content.split('\n')
        count = 0
        in_block_comment = False
        
        for line in lines:
            stripped = line.strip()
            
            # Block comments
            if language in ['Python']:
                if '"""' in stripped or "'''" in stripped:
                    in_block_comment = not in_block_comment
                    count += 1
                    continue
            else:
                if '/*' in stripped:
                    in_block_comment = True
                if '*/' in stripped:
                    in_block_comment = False
                    count += 1
                    continue
                    
            if in_block_comment:
                count += 1
                continue
                
            # Single line comments
            if language == 'Python' and stripped.startswith('#'):
                count += 1
            elif language in ['JavaScript', 'TypeScript', 'Java', 'C++', 'C', 'Go', 'Rust'] and stripped.startswith('//'):
                count += 1
                
        return count
    
    def _estimate_nesting(self, content: str) -> int:
        """Estimate maximum nesting depth."""
        max_depth = 0
        current_depth = 0
        
        for char in content:
            if char in '{(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char in '})':
                current_depth = max(0, current_depth - 1)
                
        return max_depth
    
    def _count_functions(self, content: str, language: str) -> int:
        """Count function/method definitions."""
        import re
        
        patterns = {
            'Python': r'^\s*def\s+\w+',
            'JavaScript': r'(function\s+\w+|const\s+\w+\s*=\s*(?:async\s*)?\(|^\s*\w+\s*\([^)]*\)\s*{)',
            'TypeScript': r'(function\s+\w+|const\s+\w+\s*=\s*(?:async\s*)?\(|^\s*\w+\s*\([^)]*\)\s*(?::\s*\w+)?\s*{)',
            'Java': r'(public|private|protected)?\s*(static)?\s*\w+\s+\w+\s*\([^)]*\)\s*{',
            'C++': r'\w+\s+\w+\s*\([^)]*\)\s*{',
            'Go': r'func\s+\w+',
            'Rust': r'fn\s+\w+'
        }
        
        pattern = patterns.get(language, r'function|def|func|fn')
        return len(re.findall(pattern, content, re.MULTILINE))
    
    def _count_classes(self, content: str, language: str) -> int:
        """Count class definitions."""
        import re
        
        patterns = {
            'Python': r'^\s*class\s+\w+',
            'JavaScript': r'class\s+\w+',
            'TypeScript': r'class\s+\w+',
            'Java': r'(public|private)?\s*class\s+\w+',
            'C++': r'class\s+\w+',
        }
        
        pattern = patterns.get(language, r'class\s+\w+')
        return len(re.findall(pattern, content, re.MULTILINE))
    
    def _ai_analyze(self, content: str, language: str, filename: str) -> Dict[str, Any]:
        """Use Claude to perform deep code analysis."""
        # Truncate if too long
        if len(content) > 50000:
            content = content[:50000] + "\n\n... [TRUNCATED] ..."
            
        prompt = f"""Analyze this {language} code file ({filename}) for code quality issues.

```{language.lower()}
{content}
```

Provide analysis in JSON format:
{{
  "overall_score": 0-100,
  "complexity_score": 0-100,
  "maintainability_score": 0-100,
  "security_score": 0-100,
  "code_smells": [
    {{
      "type": "smell name",
      "severity": "high/medium/low",
      "location": "function/class name or line reference",
      "description": "explanation"
    }}
  ],
  "security_issues": [
    {{
      "type": "issue type",
      "severity": "critical/high/medium/low",
      "location": "location",
      "description": "explanation",
      "fix": "how to fix"
    }}
  ],
  "refactoring_suggestions": [
    {{
      "type": "refactoring type",
      "target": "what to refactor",
      "benefit": "why refactor",
      "effort": "high/medium/low"
    }}
  ],
  "best_practices_violations": [
    {{
      "practice": "practice name",
      "violation": "what's wrong",
      "suggestion": "how to fix"
    }}
  ],
  "positive_aspects": ["list of good things in the code"],
  "summary": "brief overall assessment"
}}

Focus on actionable insights. Be specific about locations and fixes."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = response.content[0].text
            
            # Extract JSON
            if '```json' in response_text:
                json_str = response_text.split('```json')[1].split('```')[0]
            elif '```' in response_text:
                json_str = response_text.split('```')[1].split('```')[0]
            else:
                json_str = response_text
                
            return json.loads(json_str.strip())
            
        except json.JSONDecodeError:
            return {
                'overall_score': 0,
                'summary': 'Analysis completed but response parsing failed',
                'raw_response': response_text[:1000] if 'response_text' in locals() else 'No response'
            }
        except Exception as e:
            return {
                'overall_score': 0,
                'summary': f'Analysis failed: {str(e)}',
                'error': str(e)
            }
    
    def generate_report(self, results: List[Dict], output_format: str = 'text') -> str:
        """Generate a quality report from analysis results."""
        if output_format == 'json':
            return json.dumps(results, indent=2)
            
        # Text report
        report = []
        report.append("=" * 70)
        report.append("🔍 CODE QUALITY ANALYSIS REPORT")
        report.append(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        # Summary scores
        total_score = 0
        file_count = 0
        all_smells = []
        all_security = []
        
        for result in results:
            if 'error' in result:
                continue
                
            ai = result.get('ai_analysis', {})
            if 'overall_score' in ai:
                total_score += ai['overall_score']
                file_count += 1
                
            all_smells.extend(ai.get('code_smells', []))
            all_security.extend(ai.get('security_issues', []))
        
        avg_score = total_score / max(file_count, 1)
        
        # Overall summary
        report.append("📊 OVERALL SUMMARY")
        report.append("-" * 40)
        report.append(f"  Files Analyzed: {file_count}")
        report.append(f"  Average Quality Score: {avg_score:.1f}/100 {self._score_emoji(avg_score)}")
        report.append(f"  Total Code Smells: {len(all_smells)}")
        report.append(f"  Security Issues: {len(all_security)}")
        report.append("")
        
        # Per-file details
        for result in results:
            if 'error' in result:
                report.append(f"❌ {result.get('file', 'Unknown')}: {result['error']}")
                continue
                
            file_name = result.get('file', 'Unknown')
            metrics = result.get('metrics', {})
            ai = result.get('ai_analysis', {})
            
            report.append(f"📄 {file_name}")
            report.append("-" * 40)
            
            # Metrics
            report.append(f"  📏 Lines: {metrics.get('code_lines', 0)} code, {metrics.get('comment_lines', 0)} comments")
            report.append(f"  🔧 Functions: {metrics.get('function_count', 0)}, Classes: {metrics.get('class_count', 0)}")
            report.append(f"  📐 Max Nesting: {metrics.get('max_nesting_depth', 0)}")
            
            # AI scores
            score = ai.get('overall_score', 0)
            report.append(f"  🎯 Quality Score: {score}/100 {self._score_emoji(score)}")
            report.append(f"  🧩 Complexity: {ai.get('complexity_score', 0)}/100")
            report.append(f"  🔒 Security: {ai.get('security_score', 0)}/100")
            report.append(f"  🛠️ Maintainability: {ai.get('maintainability_score', 0)}/100")
            
            # Code smells
            smells = ai.get('code_smells', [])
            if smells:
                report.append(f"\n  👃 Code Smells ({len(smells)}):")
                for smell in smells[:5]:  # Top 5
                    sev = smell.get('severity', 'medium')
                    sev_icon = '🔴' if sev == 'high' else '🟡' if sev == 'medium' else '🟢'
                    report.append(f"    {sev_icon} {smell.get('type', 'Unknown')}: {smell.get('description', '')[:50]}")
                    
            # Security issues
            security = ai.get('security_issues', [])
            if security:
                report.append(f"\n  🔐 Security Issues ({len(security)}):")
                for issue in security:
                    sev = issue.get('severity', 'medium')
                    sev_icon = '🔴' if sev in ['critical', 'high'] else '🟡' if sev == 'medium' else '🟢'
                    report.append(f"    {sev_icon} {issue.get('type', 'Unknown')}: {issue.get('description', '')[:50]}")
                    
            # Refactoring suggestions
            refactors = ai.get('refactoring_suggestions', [])
            if refactors:
                report.append(f"\n  🔄 Refactoring Suggestions ({len(refactors)}):")
                for ref in refactors[:3]:  # Top 3
                    report.append(f"    → {ref.get('type', 'Unknown')}: {ref.get('target', '')}")
                    
            # Positive aspects
            positives = ai.get('positive_aspects', [])
            if positives:
                report.append(f"\n  ✅ Positive Aspects:")
                for pos in positives[:3]:
                    report.append(f"    + {pos}")
                    
            report.append(f"\n  💬 {ai.get('summary', 'No summary available')}")
            report.append("")
            
        # Final recommendations
        report.append("=" * 70)
        report.append("📋 TOP RECOMMENDATIONS")
        report.append("-" * 40)
        
        # Aggregate recommendations
        if all_security:
            critical = [s for s in all_security if s.get('severity') in ['critical', 'high']]
            if critical:
                report.append(f"🔴 CRITICAL: Address {len(critical)} high-severity security issues immediately")
                
        high_smells = [s for s in all_smells if s.get('severity') == 'high']
        if high_smells:
            report.append(f"🟡 IMPORTANT: {len(high_smells)} high-severity code smells detected")
            
        if avg_score < 60:
            report.append("⚠️ ATTENTION: Overall code quality below acceptable threshold (60)")
        elif avg_score >= 80:
            report.append("✅ GOOD: Code quality is at a healthy level")
            
        report.append("")
        report.append("=" * 70)
        
        return '\n'.join(report)
    
    def _score_emoji(self, score: float) -> str:
        """Get emoji for score."""
        if score >= 90:
            return "🌟"
        elif score >= 80:
            return "✅"
        elif score >= 70:
            return "👍"
        elif score >= 60:
            return "⚠️"
        elif score >= 50:
            return "🟡"
        else:
            return "🔴"


def main():
    parser = argparse.ArgumentParser(
        description='🔍 AI-Powered Code Quality Analyzer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --path src/main.py          Analyze single file
  %(prog)s --path src/                 Analyze directory
  %(prog)s --path . --json             Output as JSON
  %(prog)s --path . --extensions .py .js  Specific extensions
        """
    )
    
    parser.add_argument('--path', '-p', default='.', help='File or directory to analyze')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--extensions', '-e', nargs='+', help='File extensions to include')
    parser.add_argument('--output', '-o', help='Output file path')
    
    args = parser.parse_args()
    
    # Check API key
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        print("   Export it or add to your shell profile")
        sys.exit(1)
        
    analyzer = CodeQualityAnalyzer()
    
    print("🔍 Starting code quality analysis...")
    print(f"   Path: {args.path}")
    
    path = Path(args.path)
    if path.is_file():
        results = [analyzer.analyze_file(str(path))]
    else:
        extensions = args.extensions if args.extensions else None
        results = analyzer.analyze_directory(str(path), extensions)
        
    # Generate report
    output_format = 'json' if args.json else 'text'
    report = analyzer.generate_report(results, output_format)
    
    if args.output:
        Path(args.output).write_text(report)
        print(f"✅ Report saved to {args.output}")
    else:
        print(report)


if __name__ == '__main__':
    main()
