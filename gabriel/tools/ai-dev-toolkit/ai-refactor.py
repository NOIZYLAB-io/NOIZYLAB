#!/usr/bin/env python3
"""
🧬 AI Code Refactorer
Part of GABRIEL AI Dev Toolkit

Intelligent refactoring:
- Extract methods/functions
- Simplify complex code
- Apply design patterns
- Modernize legacy code
"""

import argparse
import os
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import re

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class AIRefactorer:
    """AI-powered code refactoring assistant."""
    
    REFACTORING_TYPES = [
        'extract_method',
        'extract_variable', 
        'inline_variable',
        'rename',
        'simplify_conditional',
        'decompose_function',
        'introduce_parameter_object',
        'replace_magic_numbers',
        'remove_dead_code',
        'apply_pattern',
        'modernize',
        'optimize'
    ]
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        
    def _detect_language(self, file_path: Path) -> str:
        """Detect programming language."""
        ext = file_path.suffix.lower()
        mapping = {
            '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
            '.jsx': 'React', '.tsx': 'React TypeScript', '.java': 'Java',
            '.go': 'Go', '.rs': 'Rust', '.cpp': 'C++', '.c': 'C'
        }
        return mapping.get(ext, 'Unknown')
    
    def analyze_refactoring_opportunities(self, file_path: str) -> Dict[str, Any]:
        """Analyze code for refactoring opportunities."""
        full_path = self.repo_path / file_path
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}
            
        language = self._detect_language(full_path)
        
        prompt = f"""Analyze this code for refactoring opportunities.

File: {file_path}
Language: {language}

Code:
```
{content[:12000]}
```

Find refactoring opportunities:
1. Long methods that should be split
2. Complex conditionals to simplify
3. Duplicate code to extract
4. Magic numbers/strings to name
5. Deep nesting to flatten
6. God classes/functions to decompose
7. Missing abstractions
8. Inconsistent naming
9. Code smells
10. Pattern opportunities

Return in JSON format:
{{
  "code_health": 0-100,
  "opportunities": [
    {{
      "type": "extract_method/simplify_conditional/etc",
      "priority": "high/medium/low",
      "location": "function or line range",
      "description": "what to refactor",
      "reason": "why refactor",
      "estimated_improvement": "what improves",
      "risk": "low/medium/high"
    }}
  ],
  "code_smells": [
    {{
      "smell": "name of smell",
      "location": "where",
      "severity": "high/medium/low"
    }}
  ],
  "pattern_suggestions": [
    {{
      "pattern": "design pattern name",
      "where": "where to apply",
      "benefit": "what it solves"
    }}
  ],
  "quick_wins": ["easy improvements"],
  "summary": "overall assessment"
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
            result['file'] = file_path
            result['language'] = language
            
            return result
            
        except Exception as e:
            return {'error': str(e)}
    
    def refactor(self, file_path: str, refactoring_type: str, 
                 target: str = None, options: Dict = None) -> Dict[str, Any]:
        """Perform a specific refactoring."""
        full_path = self.repo_path / file_path
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}
            
        language = self._detect_language(full_path)
        
        type_instructions = {
            'extract_method': f"Extract the code at/around '{target}' into a new well-named method",
            'extract_variable': f"Extract the expression '{target}' into a named variable",
            'simplify_conditional': f"Simplify the conditional logic at '{target}'",
            'decompose_function': f"Break down the function '{target}' into smaller, focused functions",
            'introduce_parameter_object': f"Create a parameter object for the function '{target}'",
            'replace_magic_numbers': "Replace all magic numbers/strings with named constants",
            'remove_dead_code': "Remove all dead/unreachable code",
            'modernize': f"Modernize the code using current {language} best practices",
            'optimize': "Optimize for performance while maintaining readability",
            'apply_pattern': f"Apply the {options.get('pattern', 'appropriate')} design pattern"
        }
        
        instruction = type_instructions.get(refactoring_type, f"Perform {refactoring_type} refactoring")
        
        prompt = f"""Refactor this code.

File: {file_path}
Language: {language}
Refactoring: {refactoring_type}
Target: {target or 'entire file'}
Instruction: {instruction}

Original Code:
```{language.lower()}
{content[:10000]}
```

Requirements:
1. Preserve all functionality
2. Improve code quality
3. Follow {language} best practices
4. Maintain consistent style
5. Add/update comments where helpful

Return in JSON format:
{{
  "refactored_code": "the complete refactored code",
  "changes_made": [
    {{
      "type": "change type",
      "description": "what changed",
      "before": "snippet before",
      "after": "snippet after"
    }}
  ],
  "new_functions": ["list of new function names created"],
  "removed_lines": number,
  "added_lines": number,
  "quality_improvement": "description of improvements",
  "warnings": ["any concerns or manual review needed"]
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
            result['original_file'] = file_path
            result['refactoring_type'] = refactoring_type
            
            return result
            
        except Exception as e:
            return {'error': str(e)}
    
    def suggest_extract(self, file_path: str, start_line: int, end_line: int) -> Dict[str, Any]:
        """Suggest extraction for selected code."""
        full_path = self.repo_path / file_path
        
        try:
            lines = full_path.read_text(encoding='utf-8').split('\n')
            selected = '\n'.join(lines[start_line-1:end_line])
            context_before = '\n'.join(lines[max(0, start_line-10):start_line-1])
            context_after = '\n'.join(lines[end_line:end_line+5])
        except Exception as e:
            return {'error': str(e)}
            
        language = self._detect_language(full_path)
        
        prompt = f"""Suggest how to extract this code into a reusable function/method.

File: {file_path}
Language: {language}
Lines: {start_line}-{end_line}

Context Before:
```
{context_before}
```

Selected Code:
```
{selected}
```

Context After:
```
{context_after}
```

Provide:
1. A good function name
2. Required parameters
3. Return type/value
4. The extracted function
5. How to call it from original location

Return JSON:
{{
  "suggested_name": "functionName",
  "parameters": [
    {{"name": "param", "type": "type", "description": "what it is"}}
  ],
  "return_type": "type",
  "extracted_function": "complete function code",
  "replacement_call": "how to call from original",
  "rationale": "why this extraction makes sense",
  "alternatives": ["other extraction options"]
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
    
    def rename_suggestions(self, file_path: str, current_name: str) -> Dict[str, Any]:
        """Suggest better names for a symbol."""
        full_path = self.repo_path / file_path
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}
            
        language = self._detect_language(full_path)
        
        # Find context around the name
        pattern = rf'\b{re.escape(current_name)}\b'
        matches = list(re.finditer(pattern, content))
        
        contexts = []
        for match in matches[:5]:
            start = max(0, match.start() - 100)
            end = min(len(content), match.end() + 100)
            contexts.append(content[start:end])
            
        prompt = f"""Suggest better names for this identifier.

File: {file_path}
Language: {language}
Current Name: {current_name}
Usage Count: {len(matches)}

Usage Contexts:
{chr(10).join(f'```{c}```' for c in contexts)}

Provide naming suggestions following {language} conventions:
1. More descriptive names
2. Consistent with code style
3. Clear intent

Return JSON:
{{
  "suggestions": [
    {{
      "name": "suggested_name",
      "rationale": "why this name is better",
      "convention": "camelCase/snake_case/etc"
    }}
  ],
  "naming_issues": ["problems with current name"],
  "best_choice": "top recommendation",
  "rename_scope": "local/file/project"
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
    
    def apply_pattern(self, file_path: str, pattern: str) -> Dict[str, Any]:
        """Apply a design pattern to code."""
        full_path = self.repo_path / file_path
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}
            
        language = self._detect_language(full_path)
        
        prompt = f"""Refactor this code to apply the {pattern} design pattern.

File: {file_path}
Language: {language}
Pattern: {pattern}

Original Code:
```{language.lower()}
{content[:10000]}
```

Apply the {pattern} pattern:
1. Identify where the pattern fits
2. Restructure the code appropriately
3. Preserve all functionality
4. Explain the transformation

Return JSON:
{{
  "refactored_code": "complete refactored code",
  "pattern_components": {{
    "component_name": "code/explanation"
  }},
  "before_after": {{
    "structure_before": "brief description",
    "structure_after": "brief description"
  }},
  "benefits": ["benefits of applying pattern"],
  "new_files_needed": ["if pattern requires new files"],
  "usage_example": "how to use the refactored code"
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
                
            return json.loads(json_str.strip())
            
        except Exception as e:
            return {'error': str(e)}
    
    def generate_report(self, file_path: str) -> str:
        """Generate refactoring analysis report."""
        print(f"🧬 Analyzing refactoring opportunities: {file_path}")
        
        result = self.analyze_refactoring_opportunities(file_path)
        
        report = []
        report.append("=" * 70)
        report.append("🧬 REFACTORING ANALYSIS REPORT")
        report.append(f"📄 {file_path}")
        report.append(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        if 'error' in result:
            report.append(f"❌ Error: {result['error']}")
            return '\n'.join(report)
            
        # Health Score
        health = result.get('code_health', 0)
        health_bar = '█' * (health // 10) + '░' * (10 - health // 10)
        report.append(f"🏥 CODE HEALTH: {health}/100 [{health_bar}]")
        report.append("")
        
        # Summary
        report.append("📋 SUMMARY")
        report.append("-" * 40)
        report.append(result.get('summary', 'No summary'))
        report.append("")
        
        # Quick Wins
        quick_wins = result.get('quick_wins', [])
        if quick_wins:
            report.append("⚡ QUICK WINS")
            report.append("-" * 40)
            for win in quick_wins:
                report.append(f"  ✅ {win}")
            report.append("")
            
        # Code Smells
        smells = result.get('code_smells', [])
        if smells:
            report.append("👃 CODE SMELLS")
            report.append("-" * 40)
            for smell in smells:
                severity_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(smell.get('severity'), '⚪')
                report.append(f"  {severity_icon} {smell.get('smell')}")
                report.append(f"     📍 {smell.get('location')}")
            report.append("")
            
        # Opportunities
        opps = result.get('opportunities', [])
        if opps:
            report.append("🔧 REFACTORING OPPORTUNITIES")
            report.append("-" * 40)
            
            for opp in opps:
                priority_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(opp.get('priority'), '⚪')
                report.append(f"\n  {priority_icon} [{opp.get('type')}] {opp.get('priority', '').upper()}")
                report.append(f"     📍 {opp.get('location')}")
                report.append(f"     📝 {opp.get('description')}")
                report.append(f"     💡 {opp.get('reason')}")
                report.append(f"     ⚠️  Risk: {opp.get('risk', 'unknown')}")
            report.append("")
            
        # Pattern Suggestions
        patterns = result.get('pattern_suggestions', [])
        if patterns:
            report.append("🎨 DESIGN PATTERN SUGGESTIONS")
            report.append("-" * 40)
            for pat in patterns:
                report.append(f"  📐 {pat.get('pattern')}")
                report.append(f"     📍 {pat.get('where')}")
                report.append(f"     💡 {pat.get('benefit')}")
            report.append("")
            
        report.append("=" * 70)
        report.append("💡 Run with --refactor <type> to apply a refactoring")
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='🧬 AI Code Refactorer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Refactoring Types:
  extract_method          Extract code into a new method
  simplify_conditional    Simplify complex conditionals
  decompose_function      Break large functions into smaller ones
  replace_magic_numbers   Replace magic values with constants
  modernize              Apply modern language features
  apply_pattern          Apply a design pattern

Examples:
  %(prog)s src/api.py                          Analyze opportunities
  %(prog)s src/api.py --refactor modernize     Modernize code
  %(prog)s src/api.py --extract 10-25          Extract lines 10-25
  %(prog)s src/api.py --rename old_func        Suggest new name
  %(prog)s src/api.py --pattern factory        Apply Factory pattern
        """
    )
    
    parser.add_argument('file', help='File to refactor')
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--refactor', '-r', help='Refactoring type to apply')
    parser.add_argument('--target', '-t', help='Target (function name, line, etc)')
    parser.add_argument('--extract', help='Lines to extract (start-end)')
    parser.add_argument('--rename', help='Symbol to rename')
    parser.add_argument('--pattern', help='Design pattern to apply')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--apply', action='store_true', help='Apply changes to file')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    refactorer = AIRefactorer(args.path)
    
    if args.extract:
        parts = args.extract.split('-')
        start = int(parts[0])
        end = int(parts[1]) if len(parts) > 1 else start + 10
        
        result = refactorer.suggest_extract(args.file, start, end)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ {result['error']}")
            else:
                print(f"\n🧬 EXTRACTION SUGGESTION")
                print("=" * 50)
                print(f"\n📛 Suggested Name: {result.get('suggested_name')}")
                print(f"\n📝 Parameters:")
                for p in result.get('parameters', []):
                    print(f"   • {p['name']}: {p['type']}")
                print(f"\n↩️  Returns: {result.get('return_type')}")
                print(f"\n📞 Call As: {result.get('replacement_call')}")
                print(f"\n💡 {result.get('rationale')}")
                
    elif args.rename:
        result = refactorer.rename_suggestions(args.file, args.rename)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ {result['error']}")
            else:
                print(f"\n📛 RENAME SUGGESTIONS for '{args.rename}'")
                print("=" * 50)
                print(f"\n🏆 Best: {result.get('best_choice')}")
                print(f"\n📋 All Suggestions:")
                for s in result.get('suggestions', []):
                    print(f"   • {s['name']}: {s['rationale']}")
                    
    elif args.pattern:
        result = refactorer.apply_pattern(args.file, args.pattern)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ {result['error']}")
            else:
                print(f"\n🎨 APPLYING {args.pattern.upper()} PATTERN")
                print("=" * 50)
                print(f"\n📋 Benefits:")
                for b in result.get('benefits', []):
                    print(f"   ✅ {b}")
                    
                if args.apply:
                    # Write refactored code
                    full_path = Path(args.path) / args.file
                    full_path.write_text(result.get('refactored_code', ''))
                    print(f"\n✅ Applied to {args.file}")
                else:
                    print("\n💡 Add --apply to write changes")
                    
    elif args.refactor:
        result = refactorer.refactor(args.file, args.refactor, args.target)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ {result['error']}")
            else:
                print(f"\n🧬 REFACTORING: {args.refactor}")
                print("=" * 50)
                
                print(f"\n📊 Changes:")
                print(f"   - Lines removed: {result.get('removed_lines', 0)}")
                print(f"   + Lines added: {result.get('added_lines', 0)}")
                
                for change in result.get('changes_made', [])[:5]:
                    print(f"\n   • {change.get('type')}: {change.get('description')}")
                    
                if result.get('warnings'):
                    print(f"\n⚠️  Warnings:")
                    for w in result['warnings']:
                        print(f"   • {w}")
                        
                if args.apply:
                    full_path = Path(args.path) / args.file
                    full_path.write_text(result.get('refactored_code', ''))
                    print(f"\n✅ Applied to {args.file}")
                else:
                    print("\n💡 Add --apply to write changes")
                    
    else:
        if args.json:
            result = refactorer.analyze_refactoring_opportunities(args.file)
            print(json.dumps(result, indent=2))
        else:
            report = refactorer.generate_report(args.file)
            print(report)


if __name__ == '__main__':
    main()
