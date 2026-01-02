#!/usr/bin/env python3
"""
⚡ Performance Predictor
Part of GABRIEL AI Dev Toolkit

Predict performance impacts:
- Identify slow code patterns
- Estimate complexity
- Memory usage analysis
- Optimization suggestions
"""

import argparse
import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import re

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class PerformancePredictor:
    """AI-powered performance analysis and prediction."""
    
    # Known slow patterns
    SLOW_PATTERNS = {
        'Python': [
            (r'for.*in.*range\(len\(', 'Inefficient iteration - use enumerate()'),
            (r'\.append\(.*\).*for', 'List building in loop - use list comprehension'),
            (r'\+\s*=\s*["\']', 'String concatenation in loop - use join()'),
            (r'import\s+re\s*$', 'Check if regex is compiled and cached'),
            (r'global\s+\w+', 'Global variable access is slower'),
            (r'try:.*except:.*pass', 'Empty except may hide performance issues'),
        ],
        'JavaScript': [
            (r'document\.querySelector.*for', 'DOM query in loop - cache outside'),
            (r'innerHTML\s*\+?=', 'innerHTML modification triggers reflow'),
            (r'\.forEach\(', 'forEach cannot break early - consider for...of'),
            (r'JSON\.parse\(JSON\.stringify', 'Deep clone is expensive'),
            (r'new RegExp\(', 'Regex in loop - compile outside'),
            (r'async.*await.*for', 'Sequential awaits - consider Promise.all'),
        ]
    }
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        
    def _detect_language(self, file_path: Path) -> str:
        """Detect programming language."""
        ext = file_path.suffix.lower()
        mapping = {
            '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
            '.jsx': 'React', '.tsx': 'React TypeScript', '.go': 'Go',
            '.rs': 'Rust', '.java': 'Java'
        }
        return mapping.get(ext, 'Unknown')
    
    def _extract_functions(self, content: str, language: str) -> List[Dict]:
        """Extract functions with their code."""
        functions = []
        
        if language == 'Python':
            pattern = r'((?:^[ \t]*(?:@\w+.*\n))*^[ \t]*(?:async\s+)?def\s+(\w+)\s*\([^)]*\).*?(?=\n(?:class|def|@|\Z)|(?=^[^\s])|\Z))'
            for match in re.finditer(pattern, content, re.MULTILINE | re.DOTALL):
                functions.append({
                    'name': match.group(2),
                    'code': match.group(1)[:2000],
                    'line': content[:match.start()].count('\n') + 1
                })
                
        elif language in ['JavaScript', 'TypeScript', 'React', 'React TypeScript']:
            # Function declarations
            pattern = r'(?:async\s+)?function\s+(\w+)\s*\([^)]*\)\s*\{[^}]*\}'
            for match in re.finditer(pattern, content):
                functions.append({
                    'name': match.group(1),
                    'code': match.group(0)[:2000],
                    'line': content[:match.start()].count('\n') + 1
                })
                
            # Arrow functions
            pattern = r'(?:const|let)\s+(\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>\s*(?:\{[^}]*\}|[^;]+)'
            for match in re.finditer(pattern, content):
                functions.append({
                    'name': match.group(1),
                    'code': match.group(0)[:2000],
                    'line': content[:match.start()].count('\n') + 1
                })
                
        return functions
    
    def _find_slow_patterns(self, content: str, language: str) -> List[Dict]:
        """Find known slow patterns."""
        issues = []
        
        patterns = self.SLOW_PATTERNS.get(language, [])
        
        for pattern, description in patterns:
            for match in re.finditer(pattern, content, re.MULTILINE):
                line_num = content[:match.start()].count('\n') + 1
                issues.append({
                    'pattern': pattern,
                    'description': description,
                    'line': line_num,
                    'snippet': content[max(0, match.start()-20):match.end()+20]
                })
                
        return issues
    
    def _estimate_complexity(self, code: str, language: str) -> Dict[str, Any]:
        """Estimate code complexity."""
        # Count loops
        loop_patterns = {
            'Python': [r'\bfor\b', r'\bwhile\b'],
            'JavaScript': [r'\bfor\b', r'\bwhile\b', r'\.forEach\(', r'\.map\(', r'\.filter\('],
        }
        
        patterns = loop_patterns.get(language, loop_patterns['Python'])
        
        loop_count = 0
        nested_loops = 0
        
        lines = code.split('\n')
        current_indent = 0
        in_loop = False
        
        for pattern in patterns:
            loop_count += len(re.findall(pattern, code))
            
        # Rough nested loop detection
        nested_loops = len(re.findall(r'for.*:\s*\n.*for', code, re.DOTALL))
        
        # Estimate complexity class
        if nested_loops >= 2:
            complexity_class = 'O(n³) - Cubic'
        elif nested_loops >= 1:
            complexity_class = 'O(n²) - Quadratic'
        elif loop_count > 0:
            complexity_class = 'O(n) - Linear'
        else:
            complexity_class = 'O(1) - Constant'
            
        return {
            'loop_count': loop_count,
            'nested_loops': nested_loops,
            'complexity_estimate': complexity_class,
            'lines_of_code': len([l for l in lines if l.strip()])
        }
    
    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """Analyze a file for performance."""
        full_path = self.repo_path / file_path
        
        if not full_path.exists():
            return {'error': f'File not found: {file_path}'}
            
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}
            
        language = self._detect_language(full_path)
        
        # Basic analysis
        functions = self._extract_functions(content, language)
        slow_patterns = self._find_slow_patterns(content, language)
        complexity = self._estimate_complexity(content, language)
        
        # AI analysis
        prompt = f"""Analyze this code for performance issues and optimization opportunities.

File: {file_path}
Language: {language}

Code:
```
{content[:10000]}
```

Static Analysis Found:
- Slow patterns: {len(slow_patterns)}
- Estimated complexity: {complexity['complexity_estimate']}
- Loop count: {complexity['loop_count']}
- Nested loops: {complexity['nested_loops']}

Analyze for:
1. Time complexity issues (loops, recursion, algorithms)
2. Memory issues (large allocations, leaks, unbounded growth)
3. I/O bottlenecks (file, network, database)
4. Caching opportunities
5. Parallelization potential
6. Hot paths (frequently executed code)

Return in JSON format:
{{
  "performance_score": 0-100,
  "issues": [
    {{
      "severity": "critical/high/medium/low",
      "type": "complexity/memory/io/algorithm",
      "description": "issue description",
      "location": "function or line",
      "impact": "estimated impact",
      "suggestion": "how to fix"
    }}
  ],
  "optimizations": [
    {{
      "type": "caching/algorithm/parallelization/lazy-loading",
      "description": "optimization opportunity",
      "location": "where to apply",
      "estimated_improvement": "% or qualitative",
      "effort": "low/medium/high"
    }}
  ],
  "memory_analysis": {{
    "potential_leaks": [],
    "large_allocations": [],
    "recommendations": []
  }},
  "summary": "brief overall assessment"
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
                
            result = json.loads(json_str.strip())
            
            # Merge with static analysis
            result['static_analysis'] = {
                'slow_patterns': slow_patterns,
                'complexity': complexity,
                'functions_analyzed': len(functions)
            }
            result['file'] = file_path
            result['language'] = language
            result['analyzed_at'] = datetime.now().isoformat()
            
            return result
            
        except Exception as e:
            return {
                'error': str(e),
                'static_analysis': {
                    'slow_patterns': slow_patterns,
                    'complexity': complexity
                }
            }
    
    def analyze_function(self, file_path: str, function_name: str) -> Dict[str, Any]:
        """Deep analysis of a specific function."""
        full_path = self.repo_path / file_path
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}
            
        language = self._detect_language(full_path)
        functions = self._extract_functions(content, language)
        
        # Find the function
        target_func = None
        for func in functions:
            if func['name'] == function_name:
                target_func = func
                break
                
        if not target_func:
            return {'error': f'Function not found: {function_name}'}
            
        prompt = f"""Deep performance analysis of this function.

Function: {function_name}
File: {file_path}
Language: {language}

Code:
```
{target_func['code']}
```

Provide detailed analysis:
1. Time complexity with explanation
2. Space complexity with explanation
3. Best/worst/average case analysis
4. Potential bottlenecks
5. Scalability concerns
6. Optimization strategies

Return in JSON format:
{{
  "function": "{function_name}",
  "time_complexity": {{
    "notation": "O(?)",
    "best_case": "O(?)",
    "worst_case": "O(?)",
    "average_case": "O(?)",
    "explanation": "why"
  }},
  "space_complexity": {{
    "notation": "O(?)",
    "explanation": "why"
  }},
  "bottlenecks": [
    {{
      "description": "what",
      "line_hint": "where",
      "severity": "high/medium/low"
    }}
  ],
  "scalability": {{
    "handles_10_items": "good/ok/poor",
    "handles_1000_items": "good/ok/poor",
    "handles_1000000_items": "good/ok/poor",
    "breaking_point": "estimated scale where issues appear"
  }},
  "optimizations": [
    {{
      "strategy": "name",
      "description": "how",
      "complexity_after": "new O(?)",
      "trade_offs": "what you give up"
    }}
  ]
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
    
    def compare_implementations(self, file_path: str, func1: str, func2: str) -> Dict[str, Any]:
        """Compare performance of two implementations."""
        full_path = self.repo_path / file_path
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}
            
        language = self._detect_language(full_path)
        functions = self._extract_functions(content, language)
        
        func1_code = func2_code = None
        for func in functions:
            if func['name'] == func1:
                func1_code = func['code']
            if func['name'] == func2:
                func2_code = func['code']
                
        if not func1_code or not func2_code:
            return {'error': 'One or both functions not found'}
            
        prompt = f"""Compare performance of these two implementations.

Implementation A - {func1}:
```
{func1_code}
```

Implementation B - {func2}:
```
{func2_code}
```

Compare:
1. Time complexity
2. Space complexity
3. Readability/maintainability
4. Edge case handling
5. Scalability

Return JSON:
{{
  "comparison": {{
    "{func1}": {{
      "time_complexity": "O(?)",
      "space_complexity": "O(?)",
      "pros": [],
      "cons": []
    }},
    "{func2}": {{
      "time_complexity": "O(?)",
      "space_complexity": "O(?)",
      "pros": [],
      "cons": []
    }}
  }},
  "winner": "{func1} or {func2}",
  "winner_reason": "why",
  "scenarios": {{
    "small_data": "which is better",
    "large_data": "which is better",
    "memory_constrained": "which is better"
  }},
  "recommendation": "overall recommendation"
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
                
            return json.loads(json_str.strip())
            
        except Exception as e:
            return {'error': str(e)}
    
    def generate_report(self, file_path: str) -> str:
        """Generate performance analysis report."""
        print(f"⚡ Analyzing performance: {file_path}")
        
        result = self.analyze_file(file_path)
        
        report = []
        report.append("=" * 70)
        report.append("⚡ PERFORMANCE ANALYSIS REPORT")
        report.append(f"📄 {file_path}")
        report.append(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        if 'error' in result:
            report.append(f"❌ Error: {result['error']}")
            return '\n'.join(report)
            
        # Score
        score = result.get('performance_score', 0)
        score_bar = '█' * (score // 10) + '░' * (10 - score // 10)
        report.append(f"📊 PERFORMANCE SCORE: {score}/100 [{score_bar}]")
        report.append("")
        
        # Summary
        report.append("📋 SUMMARY")
        report.append("-" * 40)
        report.append(result.get('summary', 'No summary available'))
        report.append("")
        
        # Static Analysis
        static = result.get('static_analysis', {})
        if static:
            report.append("🔍 STATIC ANALYSIS")
            report.append("-" * 40)
            complexity = static.get('complexity', {})
            report.append(f"  Complexity: {complexity.get('complexity_estimate', 'Unknown')}")
            report.append(f"  Loops: {complexity.get('loop_count', 0)}")
            report.append(f"  Nested Loops: {complexity.get('nested_loops', 0)}")
            report.append(f"  Lines of Code: {complexity.get('lines_of_code', 0)}")
            report.append("")
            
            slow = static.get('slow_patterns', [])
            if slow:
                report.append("⚠️  Slow Patterns Detected:")
                for pattern in slow[:5]:
                    report.append(f"    Line {pattern['line']}: {pattern['description']}")
                report.append("")
                
        # Issues
        issues = result.get('issues', [])
        if issues:
            report.append("🚨 PERFORMANCE ISSUES")
            report.append("-" * 40)
            
            for issue in issues:
                severity_icon = {
                    'critical': '🔴',
                    'high': '🟠',
                    'medium': '🟡',
                    'low': '🟢'
                }.get(issue.get('severity'), '⚪')
                
                report.append(f"  {severity_icon} [{issue.get('severity', 'unknown').upper()}] {issue.get('type', '')}")
                report.append(f"     {issue.get('description', '')}")
                report.append(f"     📍 {issue.get('location', 'Unknown location')}")
                report.append(f"     💡 {issue.get('suggestion', '')}")
                report.append("")
                
        # Optimizations
        opts = result.get('optimizations', [])
        if opts:
            report.append("🚀 OPTIMIZATION OPPORTUNITIES")
            report.append("-" * 40)
            
            for opt in opts:
                effort_icon = {'low': '🟢', 'medium': '🟡', 'high': '🔴'}.get(opt.get('effort'), '⚪')
                report.append(f"  {effort_icon} {opt.get('type', '')} [{opt.get('effort', '')} effort]")
                report.append(f"     {opt.get('description', '')}")
                report.append(f"     📈 Improvement: {opt.get('estimated_improvement', 'Unknown')}")
                report.append("")
                
        # Memory
        memory = result.get('memory_analysis', {})
        if memory.get('potential_leaks') or memory.get('recommendations'):
            report.append("🧠 MEMORY ANALYSIS")
            report.append("-" * 40)
            
            for leak in memory.get('potential_leaks', []):
                report.append(f"  ⚠️  Potential leak: {leak}")
                
            for rec in memory.get('recommendations', []):
                report.append(f"  💡 {rec}")
            report.append("")
            
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='⚡ Performance Predictor',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s src/api.py                   Analyze file
  %(prog)s src/api.py -f process_data   Deep function analysis
  %(prog)s src/api.py --compare v1 v2   Compare implementations
        """
    )
    
    parser.add_argument('file', nargs='?', help='File to analyze')
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--function', '-f', help='Analyze specific function')
    parser.add_argument('--compare', nargs=2, help='Compare two functions')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    predictor = PerformancePredictor(args.path)
    
    if not args.file:
        parser.print_help()
        sys.exit(1)
        
    if args.compare:
        result = predictor.compare_implementations(args.file, args.compare[0], args.compare[1])
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ {result['error']}")
            else:
                print(f"\n⚖️  COMPARISON: {args.compare[0]} vs {args.compare[1]}")
                print("=" * 50)
                print(f"\n🏆 Winner: {result.get('winner')}")
                print(f"   {result.get('winner_reason')}")
                print(f"\n💡 {result.get('recommendation')}")
                
    elif args.function:
        result = predictor.analyze_function(args.file, args.function)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ {result['error']}")
            else:
                print(f"\n🔬 DEEP ANALYSIS: {args.function}")
                print("=" * 50)
                
                tc = result.get('time_complexity', {})
                print(f"\n⏱️  Time Complexity: {tc.get('notation', 'Unknown')}")
                print(f"   Best: {tc.get('best_case')} | Avg: {tc.get('average_case')} | Worst: {tc.get('worst_case')}")
                
                sc = result.get('space_complexity', {})
                print(f"\n💾 Space Complexity: {sc.get('notation', 'Unknown')}")
                
                scale = result.get('scalability', {})
                print(f"\n📈 Scalability:")
                print(f"   10 items: {scale.get('handles_10_items')}")
                print(f"   1K items: {scale.get('handles_1000_items')}")
                print(f"   1M items: {scale.get('handles_1000000_items')}")
                
    else:
        if args.json:
            result = predictor.analyze_file(args.file)
            print(json.dumps(result, indent=2))
        else:
            report = predictor.generate_report(args.file)
            print(report)


if __name__ == '__main__':
    main()
