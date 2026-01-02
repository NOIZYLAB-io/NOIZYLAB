#!/usr/bin/env python3
"""
💡 AI-Powered Contextual Code Suggestions
Part of GABRIEL AI Dev Toolkit

Real-time intelligent code suggestions based on context:
- Auto-completion enhancement
- Code pattern recognition
- Refactoring suggestions
- Best practice recommendations
- Security fix suggestions
- Performance optimizations
"""

import argparse
import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import subprocess

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class ContextualCodeSuggester:
    """AI-powered contextual code suggestion engine."""
    
    SUGGESTION_TYPES = [
        'completion',      # Complete current code
        'refactor',        # Suggest refactoring
        'optimize',        # Performance optimization
        'security',        # Security improvements
        'best_practice',   # Best practice alignment
        'error_fix',       # Fix potential errors
        'documentation',   # Add/improve docs
        'test'            # Suggest tests
    ]
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        
    def _detect_language(self, file_path: str) -> str:
        """Detect programming language from file extension."""
        ext = Path(file_path).suffix.lower()
        mapping = {
            '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
            '.jsx': 'React', '.tsx': 'React TypeScript', '.java': 'Java',
            '.go': 'Go', '.rs': 'Rust', '.cpp': 'C++', '.c': 'C',
            '.rb': 'Ruby', '.php': 'PHP', '.swift': 'Swift', '.kt': 'Kotlin'
        }
        return mapping.get(ext, 'Unknown')
    
    def get_file_context(self, file_path: str, line_number: int = None, context_lines: int = 50) -> Dict[str, Any]:
        """Get context around a specific location in a file."""
        path = Path(file_path)
        if not path.exists():
            return {'error': f'File not found: {file_path}'}
            
        try:
            content = path.read_text(encoding='utf-8')
            lines = content.split('\n')
        except Exception as e:
            return {'error': f'Cannot read file: {e}'}
            
        language = self._detect_language(file_path)
        
        if line_number:
            start = max(0, line_number - context_lines)
            end = min(len(lines), line_number + context_lines)
            context_content = '\n'.join(lines[start:end])
            cursor_offset = line_number - start
        else:
            context_content = content
            cursor_offset = len(lines) // 2
            
        # Gather related files
        related = self._find_related_files(path)
        
        return {
            'file': str(path),
            'language': language,
            'content': context_content,
            'full_content': content,
            'line_number': line_number,
            'cursor_offset': cursor_offset,
            'total_lines': len(lines),
            'related_files': related
        }
    
    def _find_related_files(self, file_path: Path) -> List[str]:
        """Find files that might be related to the current file."""
        related = []
        
        # Same directory
        for f in file_path.parent.iterdir():
            if f.is_file() and f.suffix == file_path.suffix and f != file_path:
                related.append(str(f.name))
                
        # Import analysis would go here
        
        return related[:10]
    
    def suggest_completion(self, file_path: str, line_number: int, partial_code: str = '') -> Dict[str, Any]:
        """Suggest code completions based on context."""
        context = self.get_file_context(file_path, line_number)
        
        if 'error' in context:
            return context
            
        prompt = f"""Analyze this {context['language']} code and suggest completions.

Current File: {Path(file_path).name}

Code Context (cursor at line {context['cursor_offset']}):
```{context['language'].lower()}
{context['content']}
```

Partial Code Being Typed:
{partial_code if partial_code else '[No partial code - suggest based on context]'}

Provide completions in JSON format:
{{
  "completions": [
    {{
      "code": "suggested code",
      "description": "what this completion does",
      "confidence": 0.0-1.0,
      "type": "completion/method/variable/import/snippet"
    }}
  ],
  "context_analysis": "what the code appears to be doing",
  "potential_issues": ["any issues detected"],
  "suggested_imports": ["imports that might be needed"]
}}

Suggest 3-5 most likely completions based on the context."""

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
                
            return json.loads(json_str.strip())
            
        except Exception as e:
            return {'error': str(e)}
    
    def suggest_refactoring(self, file_path: str, start_line: int = None, end_line: int = None) -> Dict[str, Any]:
        """Suggest refactoring opportunities."""
        context = self.get_file_context(file_path)
        
        if 'error' in context:
            return context
            
        # Get specific section if lines specified
        if start_line and end_line:
            lines = context['full_content'].split('\n')
            selected_code = '\n'.join(lines[start_line-1:end_line])
        else:
            selected_code = context['full_content']
            
        prompt = f"""Analyze this {context['language']} code for refactoring opportunities.

File: {Path(file_path).name}

Code to Analyze:
```{context['language'].lower()}
{selected_code[:8000]}
```

Provide refactoring suggestions in JSON format:
{{
  "refactorings": [
    {{
      "type": "extract_method/extract_class/simplify/rename/inline/move",
      "target": "what to refactor",
      "location": "line or function name",
      "reason": "why this refactoring helps",
      "before": "code before (snippet)",
      "after": "code after (snippet)",
      "effort": "low/medium/high",
      "impact": "low/medium/high"
    }}
  ],
  "code_smells_detected": ["list of detected code smells"],
  "complexity_assessment": "overall complexity level",
  "priority_order": ["ordered list of refactoring IDs by priority"]
}}

Focus on actionable, high-impact refactorings."""

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
    
    def suggest_optimization(self, file_path: str) -> Dict[str, Any]:
        """Suggest performance optimizations."""
        context = self.get_file_context(file_path)
        
        if 'error' in context:
            return context
            
        prompt = f"""Analyze this {context['language']} code for performance optimization opportunities.

File: {Path(file_path).name}

Code:
```{context['language'].lower()}
{context['full_content'][:10000]}
```

Provide optimization suggestions in JSON format:
{{
  "optimizations": [
    {{
      "type": "algorithm/data_structure/caching/lazy_loading/async/memory",
      "location": "line or function name",
      "current_issue": "what's inefficient",
      "suggestion": "how to optimize",
      "expected_improvement": "estimated improvement",
      "code_before": "current code snippet",
      "code_after": "optimized code snippet",
      "trade_offs": ["any trade-offs to consider"]
    }}
  ],
  "hotspots": ["potential performance bottlenecks"],
  "memory_concerns": ["memory-related issues"],
  "scalability_notes": "scalability assessment"
}}

Focus on practical optimizations with measurable impact."""

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
    
    def suggest_security_fixes(self, file_path: str) -> Dict[str, Any]:
        """Suggest security improvements."""
        context = self.get_file_context(file_path)
        
        if 'error' in context:
            return context
            
        prompt = f"""Perform a security audit on this {context['language']} code.

File: {Path(file_path).name}

Code:
```{context['language'].lower()}
{context['full_content'][:10000]}
```

Provide security analysis in JSON format:
{{
  "vulnerabilities": [
    {{
      "type": "injection/xss/csrf/auth/crypto/exposure/etc",
      "severity": "critical/high/medium/low",
      "location": "line or function",
      "description": "what the vulnerability is",
      "exploit_scenario": "how it could be exploited",
      "fix": "how to fix it",
      "code_before": "vulnerable code",
      "code_after": "secure code"
    }}
  ],
  "security_best_practices": [
    {{
      "practice": "practice name",
      "status": "implemented/missing/partial",
      "recommendation": "what to do"
    }}
  ],
  "sensitive_data": ["detected sensitive data handling"],
  "overall_security_score": 0-100,
  "priority_fixes": ["ordered list of fixes by priority"]
}}

Be thorough but avoid false positives."""

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
    
    def analyze_and_suggest_all(self, file_path: str) -> Dict[str, Any]:
        """Run all suggestion types and compile comprehensive report."""
        results = {
            'file': file_path,
            'timestamp': datetime.now().isoformat(),
            'analyses': {}
        }
        
        print("  🔍 Analyzing completions...")
        results['analyses']['completion'] = self.suggest_completion(file_path, None)
        
        print("  🔄 Analyzing refactoring...")
        results['analyses']['refactoring'] = self.suggest_refactoring(file_path)
        
        print("  ⚡ Analyzing performance...")
        results['analyses']['optimization'] = self.suggest_optimization(file_path)
        
        print("  🔒 Analyzing security...")
        results['analyses']['security'] = self.suggest_security_fixes(file_path)
        
        return results
    
    def generate_report(self, file_path: str) -> str:
        """Generate comprehensive suggestion report."""
        print(f"🔍 Analyzing {file_path}...")
        results = self.analyze_and_suggest_all(file_path)
        
        report = []
        report.append("=" * 70)
        report.append("💡 CONTEXTUAL CODE SUGGESTIONS REPORT")
        report.append(f"📄 File: {file_path}")
        report.append(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        # Refactoring
        refactor = results['analyses'].get('refactoring', {})
        if 'refactorings' in refactor:
            report.append("🔄 REFACTORING SUGGESTIONS")
            report.append("-" * 40)
            for ref in refactor['refactorings'][:5]:
                effort_icon = '🔴' if ref.get('effort') == 'high' else '🟡' if ref.get('effort') == 'medium' else '🟢'
                report.append(f"  {effort_icon} {ref.get('type', 'Unknown').replace('_', ' ').title()}")
                report.append(f"     Target: {ref.get('target', 'N/A')}")
                report.append(f"     Reason: {ref.get('reason', 'N/A')[:60]}")
                report.append("")
                
        # Optimization
        optim = results['analyses'].get('optimization', {})
        if 'optimizations' in optim:
            report.append("⚡ PERFORMANCE OPTIMIZATIONS")
            report.append("-" * 40)
            for opt in optim['optimizations'][:5]:
                report.append(f"  • {opt.get('type', 'Unknown').replace('_', ' ').title()}")
                report.append(f"    Issue: {opt.get('current_issue', 'N/A')[:50]}")
                report.append(f"    Fix: {opt.get('suggestion', 'N/A')[:50]}")
                report.append("")
                
        if 'hotspots' in optim:
            report.append("  🔥 Hotspots:")
            for hs in optim['hotspots'][:3]:
                report.append(f"    - {hs}")
            report.append("")
                
        # Security
        security = results['analyses'].get('security', {})
        if 'vulnerabilities' in security:
            vulns = security['vulnerabilities']
            if vulns:
                report.append("🔒 SECURITY ISSUES")
                report.append("-" * 40)
                for vuln in vulns[:5]:
                    sev = vuln.get('severity', 'medium')
                    sev_icon = '🔴' if sev in ['critical', 'high'] else '🟡' if sev == 'medium' else '🟢'
                    report.append(f"  {sev_icon} [{sev.upper()}] {vuln.get('type', 'Unknown')}")
                    report.append(f"     Location: {vuln.get('location', 'N/A')}")
                    report.append(f"     Issue: {vuln.get('description', 'N/A')[:60]}")
                    report.append("")
                    
                score = security.get('overall_security_score', 0)
                score_icon = '🟢' if score >= 80 else '🟡' if score >= 60 else '🔴'
                report.append(f"  {score_icon} Security Score: {score}/100")
                report.append("")
            else:
                report.append("🔒 SECURITY: ✅ No vulnerabilities detected")
                report.append("")
                
        # Best practices
        if 'security_best_practices' in security:
            missing = [p for p in security['security_best_practices'] if p.get('status') == 'missing']
            if missing:
                report.append("📋 MISSING BEST PRACTICES")
                report.append("-" * 40)
                for practice in missing[:5]:
                    report.append(f"  ⚠️ {practice.get('practice', 'Unknown')}")
                    report.append(f"     → {practice.get('recommendation', 'N/A')[:60]}")
                report.append("")
                
        # Code smells
        if 'code_smells_detected' in refactor:
            smells = refactor['code_smells_detected']
            if smells:
                report.append("👃 CODE SMELLS DETECTED")
                report.append("-" * 40)
                for smell in smells[:5]:
                    report.append(f"  • {smell}")
                report.append("")
                
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='💡 AI-Powered Contextual Code Suggestions',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --file src/main.py           Full analysis
  %(prog)s --file src/main.py --complete --line 42    Completions at line 42
  %(prog)s --file src/main.py --refactor              Refactoring suggestions
  %(prog)s --file src/main.py --optimize              Performance optimizations
  %(prog)s --file src/main.py --security              Security audit
        """
    )
    
    parser.add_argument('--file', '-f', required=True, help='File to analyze')
    parser.add_argument('--line', '-l', type=int, help='Line number for context')
    parser.add_argument('--complete', action='store_true', help='Code completions')
    parser.add_argument('--refactor', action='store_true', help='Refactoring suggestions')
    parser.add_argument('--optimize', action='store_true', help='Performance optimizations')
    parser.add_argument('--security', action='store_true', help='Security audit')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--output', '-o', help='Output file path')
    
    args = parser.parse_args()
    
    # Check API key
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    suggester = ContextualCodeSuggester()
    
    output = None
    
    if args.complete:
        print(f"💡 Suggesting completions for {args.file}...")
        result = suggester.suggest_completion(args.file, args.line)
        
        if args.json:
            output = json.dumps(result, indent=2)
        else:
            if 'completions' in result:
                output = ["💡 Completion Suggestions:", ""]
                for comp in result['completions']:
                    conf = comp.get('confidence', 0) * 100
                    output.append(f"  [{conf:.0f}%] {comp.get('description', '')}")
                    output.append(f"  ```")
                    output.append(f"  {comp.get('code', '')}")
                    output.append(f"  ```")
                    output.append("")
                output = '\n'.join(output)
            else:
                output = str(result)
                
    elif args.refactor:
        print(f"🔄 Analyzing refactoring for {args.file}...")
        result = suggester.suggest_refactoring(args.file)
        
        if args.json:
            output = json.dumps(result, indent=2)
        else:
            if 'refactorings' in result:
                output = ["🔄 Refactoring Suggestions:", ""]
                for ref in result['refactorings']:
                    output.append(f"  • {ref.get('type', '').replace('_', ' ').title()}")
                    output.append(f"    Target: {ref.get('target', 'N/A')}")
                    output.append(f"    Reason: {ref.get('reason', 'N/A')}")
                    output.append("")
                output = '\n'.join(output)
            else:
                output = str(result)
                
    elif args.optimize:
        print(f"⚡ Analyzing performance for {args.file}...")
        result = suggester.suggest_optimization(args.file)
        output = json.dumps(result, indent=2) if args.json else str(result)
        
    elif args.security:
        print(f"🔒 Security audit for {args.file}...")
        result = suggester.suggest_security_fixes(args.file)
        output = json.dumps(result, indent=2) if args.json else str(result)
        
    else:
        output = suggester.generate_report(args.file)
        
    if output:
        if args.output:
            Path(args.output).write_text(output)
            print(f"✅ Output saved to {args.output}")
        else:
            print(output)


if __name__ == '__main__':
    main()
