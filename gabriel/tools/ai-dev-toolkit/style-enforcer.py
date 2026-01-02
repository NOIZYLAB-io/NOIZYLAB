#!/usr/bin/env python3
"""
🎭 Code Style Enforcer
Part of GABRIEL AI Dev Toolkit

Consistent code style:
- Style detection
- Auto-formatting suggestions
- Convention enforcement
- Team style guide creation
"""

import argparse
import os
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import re
from collections import Counter

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class StyleEnforcer:
    """AI-powered code style analysis and enforcement."""
    
    STYLE_ASPECTS = [
        'naming_conventions',
        'indentation',
        'line_length',
        'imports_organization',
        'comments_style',
        'string_quotes',
        'bracket_style',
        'whitespace',
        'function_structure',
        'class_structure'
    ]
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        
    def _get_code_files(self, extensions: List[str] = None) -> List[Path]:
        """Get code files to analyze."""
        if not extensions:
            extensions = ['.py', '.js', '.ts', '.jsx', '.tsx']
            
        files = []
        for ext in extensions:
            for f in self.repo_path.rglob(f'*{ext}'):
                if any(skip in str(f) for skip in ['node_modules', '.git', '__pycache__', 'venv', 'dist']):
                    continue
                files.append(f)
        return files
    
    def _detect_language(self, file_path: Path) -> str:
        """Detect programming language."""
        ext = file_path.suffix.lower()
        mapping = {
            '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
            '.jsx': 'React', '.tsx': 'React TypeScript'
        }
        return mapping.get(ext, 'Unknown')
    
    def _analyze_basic_style(self, content: str, language: str) -> Dict[str, Any]:
        """Perform basic style analysis."""
        lines = content.split('\n')
        
        analysis = {
            'total_lines': len(lines),
            'blank_lines': sum(1 for l in lines if not l.strip()),
            'comment_lines': 0,
            'max_line_length': max(len(l) for l in lines) if lines else 0,
            'avg_line_length': sum(len(l) for l in lines) / len(lines) if lines else 0,
            'indentation': self._detect_indentation(content),
            'quotes': self._detect_quotes(content, language),
            'naming_patterns': self._detect_naming(content, language)
        }
        
        # Count comments
        if language == 'Python':
            analysis['comment_lines'] = sum(1 for l in lines if l.strip().startswith('#'))
        else:
            analysis['comment_lines'] = sum(1 for l in lines if l.strip().startswith('//'))
            
        return analysis
    
    def _detect_indentation(self, content: str) -> Dict[str, Any]:
        """Detect indentation style."""
        lines = content.split('\n')
        
        spaces_2 = 0
        spaces_4 = 0
        tabs = 0
        
        for line in lines:
            if not line or not line[0].isspace():
                continue
                
            leading = len(line) - len(line.lstrip())
            
            if '\t' in line[:leading]:
                tabs += 1
            elif leading == 2 or leading % 2 == 0:
                spaces_2 += 1
            elif leading == 4 or leading % 4 == 0:
                spaces_4 += 1
                
        if tabs > spaces_2 and tabs > spaces_4:
            style = 'tabs'
        elif spaces_2 > spaces_4:
            style = '2 spaces'
        else:
            style = '4 spaces'
            
        return {
            'detected': style,
            'tabs_count': tabs,
            'spaces_2_count': spaces_2,
            'spaces_4_count': spaces_4,
            'consistent': max(tabs, spaces_2, spaces_4) > 0.8 * (tabs + spaces_2 + spaces_4)
        }
    
    def _detect_quotes(self, content: str, language: str) -> Dict[str, Any]:
        """Detect quote style preference."""
        if language == 'Python':
            single = len(re.findall(r"'[^']*'", content))
            double = len(re.findall(r'"[^"]*"', content))
        else:
            single = len(re.findall(r"'[^']*'", content))
            double = len(re.findall(r'"[^"]*"', content))
            backtick = len(re.findall(r'`[^`]*`', content))
            
        return {
            'single_quotes': single,
            'double_quotes': double,
            'preferred': 'single' if single > double else 'double',
            'consistent': abs(single - double) > 0.7 * (single + double)
        }
    
    def _detect_naming(self, content: str, language: str) -> Dict[str, Any]:
        """Detect naming conventions."""
        patterns = {
            'snake_case': re.findall(r'\b[a-z]+(?:_[a-z]+)+\b', content),
            'camelCase': re.findall(r'\b[a-z]+(?:[A-Z][a-z]+)+\b', content),
            'PascalCase': re.findall(r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)+\b', content),
            'SCREAMING_SNAKE': re.findall(r'\b[A-Z]+(?:_[A-Z]+)+\b', content)
        }
        
        counts = {k: len(v) for k, v in patterns.items()}
        dominant = max(counts, key=counts.get) if counts else 'mixed'
        
        return {
            'counts': counts,
            'dominant': dominant,
            'mixed': sum(1 for v in counts.values() if v > 10) > 1
        }
    
    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """Analyze style of a single file."""
        full_path = self.repo_path / file_path
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}
            
        language = self._detect_language(full_path)
        basic = self._analyze_basic_style(content, language)
        
        prompt = f"""Analyze the code style of this file.

File: {file_path}
Language: {language}

Basic Analysis:
{json.dumps(basic, indent=2)}

Code:
```{language.lower()}
{content[:8000]}
```

Analyze:
1. Naming conventions (variables, functions, classes)
2. Code organization (imports, structure, grouping)
3. Formatting (spacing, alignment, line breaks)
4. Documentation style (comments, docstrings)
5. Consistency throughout the file
6. Adherence to {language} best practices

Return JSON:
{{
  "style_score": 0-100,
  "style_profile": {{
    "naming": "snake_case/camelCase/etc",
    "indentation": "2 spaces/4 spaces/tabs",
    "quotes": "single/double",
    "imports_style": "grouped/alphabetical/by-type",
    "docstring_style": "Google/NumPy/JSDoc/none"
  }},
  "strengths": ["what's done well"],
  "issues": [
    {{
      "type": "naming/formatting/organization/documentation",
      "severity": "high/medium/low",
      "description": "what's wrong",
      "line": line_number,
      "suggestion": "how to fix"
    }}
  ],
  "inconsistencies": ["where style varies"],
  "recommendation": "overall style recommendation"
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
            result['basic_analysis'] = basic
            
            return result
            
        except Exception as e:
            return {'error': str(e), 'basic_analysis': basic}
    
    def analyze_project_style(self) -> Dict[str, Any]:
        """Analyze style consistency across project."""
        files = self._get_code_files()[:30]  # Limit for performance
        
        if not files:
            return {'error': 'No code files found'}
            
        # Gather basic stats from all files
        all_stats = []
        by_language = {}
        
        print(f"📊 Analyzing {len(files)} files...")
        
        for f in files:
            try:
                content = f.read_text(encoding='utf-8', errors='ignore')
                language = self._detect_language(f)
                
                stats = self._analyze_basic_style(content, language)
                stats['file'] = str(f.relative_to(self.repo_path))
                stats['language'] = language
                all_stats.append(stats)
                
                if language not in by_language:
                    by_language[language] = []
                by_language[language].append(stats)
                
            except Exception:
                continue
                
        # Aggregate stats
        indent_styles = Counter(s['indentation']['detected'] for s in all_stats)
        quote_styles = Counter(s['quotes']['preferred'] for s in all_stats)
        
        # Create sample for AI analysis
        sample_files = {}
        for lang, stats in by_language.items():
            if stats:
                sample_files[lang] = stats[0]['file']
                
        prompt = f"""Analyze style consistency across this project.

Project Stats:
- Files analyzed: {len(files)}
- Languages: {list(by_language.keys())}
- Indentation styles: {dict(indent_styles)}
- Quote styles: {dict(quote_styles)}

File Samples:
{json.dumps([s for s in all_stats[:10]], indent=2)}

Determine:
1. Project-wide style patterns
2. Inconsistencies between files
3. Language-specific conventions
4. Suggested unified style guide

Return JSON:
{{
  "consistency_score": 0-100,
  "detected_style": {{
    "indentation": "most common",
    "quotes": "most common",
    "naming": "dominant pattern",
    "imports": "detected organization"
  }},
  "language_styles": {{
    "Python": {{}},
    "JavaScript": {{}}
  }},
  "inconsistencies": [
    {{
      "aspect": "what varies",
      "files_affected": number,
      "variants": ["style A", "style B"]
    }}
  ],
  "style_guide_recommendation": {{
    "indentation": "recommended",
    "quotes": "recommended", 
    "naming_functions": "recommended",
    "naming_classes": "recommended",
    "naming_constants": "recommended",
    "imports": "recommended",
    "max_line_length": number,
    "documentation": "recommended style"
  }},
  "priority_fixes": ["most important consistency issues to fix"]
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
            result['files_analyzed'] = len(files)
            result['raw_stats'] = {
                'indentation': dict(indent_styles),
                'quotes': dict(quote_styles)
            }
            
            return result
            
        except Exception as e:
            return {'error': str(e)}
    
    def generate_style_guide(self, output_file: str = None) -> str:
        """Generate a style guide for the project."""
        print("📚 Generating style guide...")
        
        analysis = self.analyze_project_style()
        
        if 'error' in analysis:
            return f"Error: {analysis['error']}"
            
        rec = analysis.get('style_guide_recommendation', {})
        
        guide = []
        guide.append("# Project Style Guide")
        guide.append(f"\n_Generated: {datetime.now().strftime('%Y-%m-%d')}_")
        guide.append(f"\n_Consistency Score: {analysis.get('consistency_score', 'N/A')}/100_")
        guide.append("")
        guide.append("## General Rules")
        guide.append("")
        guide.append(f"- **Indentation**: {rec.get('indentation', '4 spaces')}")
        guide.append(f"- **Quotes**: {rec.get('quotes', 'single quotes')}")
        guide.append(f"- **Max Line Length**: {rec.get('max_line_length', 100)} characters")
        guide.append("")
        guide.append("## Naming Conventions")
        guide.append("")
        guide.append(f"- **Functions/Methods**: `{rec.get('naming_functions', 'snake_case')}`")
        guide.append(f"- **Classes**: `{rec.get('naming_classes', 'PascalCase')}`")
        guide.append(f"- **Constants**: `{rec.get('naming_constants', 'SCREAMING_SNAKE_CASE')}`")
        guide.append("")
        guide.append("## Imports")
        guide.append("")
        guide.append(f"- Organization: {rec.get('imports', 'Grouped by type (stdlib, third-party, local)')}")
        guide.append("")
        guide.append("## Documentation")
        guide.append("")
        guide.append(f"- Style: {rec.get('documentation', 'Docstrings for public APIs')}")
        guide.append("")
        
        # Language-specific sections
        lang_styles = analysis.get('language_styles', {})
        for lang, style in lang_styles.items():
            if style:
                guide.append(f"## {lang} Specific")
                guide.append("")
                for key, value in style.items():
                    guide.append(f"- **{key}**: {value}")
                guide.append("")
                
        # Priority fixes
        fixes = analysis.get('priority_fixes', [])
        if fixes:
            guide.append("## Priority Fixes")
            guide.append("")
            for fix in fixes:
                guide.append(f"- [ ] {fix}")
            guide.append("")
            
        guide_text = '\n'.join(guide)
        
        if output_file:
            output_path = self.repo_path / output_file
            output_path.write_text(guide_text)
            print(f"✅ Style guide saved to: {output_file}")
            
        return guide_text
    
    def fix_style(self, file_path: str, style_guide: Dict = None) -> Dict[str, Any]:
        """Auto-fix style issues in a file."""
        full_path = self.repo_path / file_path
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}
            
        language = self._detect_language(full_path)
        
        style_rules = style_guide or {
            'indentation': '4 spaces',
            'quotes': 'single',
            'max_line_length': 100
        }
        
        prompt = f"""Fix the code style according to these rules.

File: {file_path}
Language: {language}

Style Rules:
{json.dumps(style_rules, indent=2)}

Original Code:
```{language.lower()}
{content[:10000]}
```

Fix:
1. Consistent indentation
2. Consistent quote style
3. Proper spacing
4. Import organization
5. Line length issues
6. Naming consistency (where possible without breaking code)

Return JSON:
{{
  "fixed_code": "the complete fixed code",
  "changes": [
    {{
      "type": "indentation/quotes/spacing/imports/etc",
      "count": number,
      "description": "what was fixed"
    }}
  ],
  "total_changes": number,
  "could_not_fix": ["things that need manual review"]
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
    
    def generate_report(self, file_path: str = None) -> str:
        """Generate style analysis report."""
        report = []
        report.append("=" * 70)
        report.append("🎭 CODE STYLE ANALYSIS")
        report.append(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        if file_path:
            print(f"🔍 Analyzing: {file_path}")
            result = self.analyze_file(file_path)
            
            if 'error' in result:
                report.append(f"❌ Error: {result['error']}")
                return '\n'.join(report)
                
            # Score
            score = result.get('style_score', 0)
            score_bar = '█' * (score // 10) + '░' * (10 - score // 10)
            report.append(f"📊 STYLE SCORE: {score}/100 [{score_bar}]")
            report.append("")
            
            # Profile
            profile = result.get('style_profile', {})
            report.append("📋 DETECTED STYLE")
            report.append("-" * 40)
            for key, value in profile.items():
                report.append(f"  {key}: {value}")
            report.append("")
            
            # Strengths
            strengths = result.get('strengths', [])
            if strengths:
                report.append("✅ STRENGTHS")
                report.append("-" * 40)
                for s in strengths:
                    report.append(f"  • {s}")
                report.append("")
                
            # Issues
            issues = result.get('issues', [])
            if issues:
                report.append("⚠️  ISSUES")
                report.append("-" * 40)
                for issue in issues:
                    severity_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(issue.get('severity'), '⚪')
                    report.append(f"  {severity_icon} [{issue.get('type')}] Line {issue.get('line', '?')}")
                    report.append(f"     {issue.get('description')}")
                    report.append(f"     💡 {issue.get('suggestion')}")
                report.append("")
                
        else:
            # Project-wide analysis
            result = self.analyze_project_style()
            
            if 'error' in result:
                report.append(f"❌ Error: {result['error']}")
                return '\n'.join(report)
                
            score = result.get('consistency_score', 0)
            score_bar = '█' * (score // 10) + '░' * (10 - score // 10)
            report.append(f"📊 CONSISTENCY SCORE: {score}/100 [{score_bar}]")
            report.append(f"📁 Files Analyzed: {result.get('files_analyzed', 0)}")
            report.append("")
            
            detected = result.get('detected_style', {})
            report.append("📋 DETECTED PROJECT STYLE")
            report.append("-" * 40)
            for key, value in detected.items():
                report.append(f"  {key}: {value}")
            report.append("")
            
            inconsistencies = result.get('inconsistencies', [])
            if inconsistencies:
                report.append("⚠️  INCONSISTENCIES")
                report.append("-" * 40)
                for inc in inconsistencies:
                    report.append(f"  • {inc.get('aspect')}: {inc.get('files_affected', '?')} files")
                    report.append(f"    Variants: {', '.join(inc.get('variants', []))}")
                report.append("")
                
            fixes = result.get('priority_fixes', [])
            if fixes:
                report.append("🔧 PRIORITY FIXES")
                report.append("-" * 40)
                for fix in fixes:
                    report.append(f"  • {fix}")
            report.append("")
            
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='🎭 Code Style Enforcer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                            Analyze project style
  %(prog)s src/api.py                 Analyze single file
  %(prog)s --guide                    Generate style guide
  %(prog)s src/api.py --fix           Auto-fix style issues
        """
    )
    
    parser.add_argument('file', nargs='?', help='File to analyze')
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--guide', '-g', action='store_true', help='Generate style guide')
    parser.add_argument('--output', '-o', help='Output file for style guide')
    parser.add_argument('--fix', action='store_true', help='Auto-fix style issues')
    parser.add_argument('--apply', action='store_true', help='Apply fixes to file')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    enforcer = StyleEnforcer(args.path)
    
    if args.guide:
        guide = enforcer.generate_style_guide(args.output or 'STYLE_GUIDE.md')
        if not args.output:
            print(guide)
            
    elif args.file and args.fix:
        result = enforcer.fix_style(args.file)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ {result['error']}")
            else:
                print(f"\n🎭 STYLE FIXES for {args.file}")
                print("=" * 50)
                print(f"\n📊 Total Changes: {result.get('total_changes', 0)}")
                
                for change in result.get('changes', []):
                    print(f"  • {change.get('type')}: {change.get('count')} ({change.get('description')})")
                    
                if result.get('could_not_fix'):
                    print("\n⚠️  Manual Review Needed:")
                    for item in result['could_not_fix']:
                        print(f"  • {item}")
                        
                if args.apply:
                    full_path = Path(args.path) / args.file
                    full_path.write_text(result.get('fixed_code', ''))
                    print(f"\n✅ Applied fixes to {args.file}")
                else:
                    print("\n💡 Add --apply to write changes")
                    
    else:
        if args.json:
            if args.file:
                result = enforcer.analyze_file(args.file)
            else:
                result = enforcer.analyze_project_style()
            print(json.dumps(result, indent=2))
        else:
            report = enforcer.generate_report(args.file)
            print(report)


if __name__ == '__main__':
    main()
