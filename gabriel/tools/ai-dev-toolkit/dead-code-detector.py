#!/usr/bin/env python3
"""
💀 Dead Code Detector
Part of GABRIEL AI Dev Toolkit

Find unused code:
- Unused functions/methods
- Unreachable code paths
- Dead imports
- Orphaned files
"""

import argparse
import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Set
import re
from collections import defaultdict

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class DeadCodeDetector:
    """AI-powered dead code detection."""
    
    SUPPORTED_EXTENSIONS = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.jsx': 'React',
        '.tsx': 'React TypeScript'
    }
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        
    def _get_code_files(self) -> List[Path]:
        """Get all code files in the repository."""
        files = []
        
        for ext in self.SUPPORTED_EXTENSIONS:
            for f in self.repo_path.rglob(f'*{ext}'):
                if any(skip in str(f) for skip in [
                    'node_modules', '.git', '__pycache__', 'venv', 
                    'dist', 'build', '.next', 'vendor'
                ]):
                    continue
                files.append(f)
                
        return files
    
    def _extract_definitions(self, file_path: Path) -> Dict[str, Any]:
        """Extract function, class, and variable definitions."""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            return None
            
        ext = file_path.suffix
        definitions = {
            'file': str(file_path.relative_to(self.repo_path)),
            'functions': [],
            'classes': [],
            'exports': [],
            'imports': []
        }
        
        if ext == '.py':
            # Python functions
            for match in re.finditer(r'^\s*def\s+(\w+)', content, re.MULTILINE):
                name = match.group(1)
                if not name.startswith('_') or name.startswith('__'):  # Include dunder methods
                    definitions['functions'].append({
                        'name': name,
                        'line': content[:match.start()].count('\n') + 1,
                        'is_private': name.startswith('_')
                    })
                    
            # Python classes
            for match in re.finditer(r'^class\s+(\w+)', content, re.MULTILINE):
                definitions['classes'].append({
                    'name': match.group(1),
                    'line': content[:match.start()].count('\n') + 1
                })
                
            # Python imports
            for match in re.finditer(r'^(?:from\s+[\w.]+\s+)?import\s+(.+)$', content, re.MULTILINE):
                imports = match.group(1)
                # Parse import names
                for name in re.findall(r'(\w+)(?:\s+as\s+\w+)?', imports):
                    definitions['imports'].append(name)
                    
        elif ext in ['.js', '.ts', '.jsx', '.tsx']:
            # JS/TS functions
            patterns = [
                r'function\s+(\w+)',
                r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?\(',
                r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?function',
            ]
            for pattern in patterns:
                for match in re.finditer(pattern, content, re.MULTILINE):
                    definitions['functions'].append({
                        'name': match.group(1),
                        'line': content[:match.start()].count('\n') + 1
                    })
                    
            # JS/TS classes
            for match in re.finditer(r'class\s+(\w+)', content, re.MULTILINE):
                definitions['classes'].append({
                    'name': match.group(1),
                    'line': content[:match.start()].count('\n') + 1
                })
                
            # Exports
            for match in re.finditer(r'export\s+(?:default\s+)?(?:function|class|const|let|var)?\s*(\w+)', content):
                definitions['exports'].append(match.group(1))
                
            # Imports
            for match in re.finditer(r'import\s+.*?from\s+[\'"]([^\'"]+)', content):
                definitions['imports'].append(match.group(1))
                
        return definitions
    
    def _find_usages(self, name: str, files: List[Path], exclude_file: str = None) -> List[Dict]:
        """Find usages of a name across files."""
        usages = []
        
        # Create regex pattern for the name
        pattern = re.compile(r'\b' + re.escape(name) + r'\b')
        
        for file_path in files:
            rel_path = str(file_path.relative_to(self.repo_path))
            if exclude_file and rel_path == exclude_file:
                continue
                
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                matches = list(pattern.finditer(content))
                
                if matches:
                    usages.append({
                        'file': rel_path,
                        'count': len(matches),
                        'lines': [content[:m.start()].count('\n') + 1 for m in matches[:5]]
                    })
            except Exception:
                continue
                
        return usages
    
    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """Analyze a single file for dead code."""
        full_path = self.repo_path / file_path
        
        if not full_path.exists():
            return {'error': f'File not found: {file_path}'}
            
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': str(e)}
            
        prompt = f"""Analyze this code for dead code, unused elements, and potential cleanup opportunities.

File: {file_path}
Language: {self.SUPPORTED_EXTENSIONS.get(full_path.suffix, 'Unknown')}

Code:
```
{content[:12000]}
```

Find:
1. Unused functions (defined but never called)
2. Unused variables (assigned but never read)
3. Unreachable code (after return/break/raise)
4. Dead imports (imported but never used)
5. Commented-out code blocks that should be removed
6. TODO/FIXME items that may indicate incomplete code
7. Deprecated patterns or old code

Return in JSON format:
{{
  "dead_code": [
    {{
      "type": "unused_function/unused_variable/unreachable/dead_import/commented_code/todo",
      "name": "element name",
      "line": line_number,
      "reason": "why it's dead",
      "confidence": "high/medium/low",
      "suggestion": "what to do"
    }}
  ],
  "cleanup_suggestions": ["general cleanup suggestions"],
  "estimated_removable_lines": number,
  "code_health_score": 0-100
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
            result['analyzed_at'] = datetime.now().isoformat()
            
            return result
            
        except Exception as e:
            return {'error': str(e), 'file': file_path}
    
    def analyze_codebase(self, deep: bool = False) -> Dict[str, Any]:
        """Analyze entire codebase for dead code."""
        files = self._get_code_files()
        
        # Gather all definitions
        all_definitions = []
        for f in files:
            defs = self._extract_definitions(f)
            if defs:
                all_definitions.append(defs)
                
        # Find potentially unused definitions
        potentially_dead = []
        
        for file_defs in all_definitions:
            file_path = file_defs['file']
            
            # Check functions
            for func in file_defs.get('functions', []):
                if func.get('is_private'):
                    continue  # Skip private functions in quick scan
                    
                usages = self._find_usages(func['name'], files, file_path)
                
                if not usages:
                    potentially_dead.append({
                        'type': 'unused_function',
                        'name': func['name'],
                        'file': file_path,
                        'line': func['line'],
                        'confidence': 'medium'
                    })
                    
            # Check classes
            for cls in file_defs.get('classes', []):
                usages = self._find_usages(cls['name'], files, file_path)
                
                if not usages:
                    potentially_dead.append({
                        'type': 'unused_class',
                        'name': cls['name'],
                        'file': file_path,
                        'line': cls['line'],
                        'confidence': 'medium'
                    })
                    
        result = {
            'potentially_dead': potentially_dead,
            'files_analyzed': len(files),
            'total_functions': sum(len(d.get('functions', [])) for d in all_definitions),
            'total_classes': sum(len(d.get('classes', [])) for d in all_definitions),
            'analyzed_at': datetime.now().isoformat()
        }
        
        # Deep analysis with AI
        if deep and potentially_dead:
            result['ai_analysis'] = self._deep_analyze(potentially_dead[:20])
            
        return result
    
    def _deep_analyze(self, candidates: List[Dict]) -> Dict:
        """Use AI for deep analysis of dead code candidates."""
        # Group by file
        by_file = defaultdict(list)
        for item in candidates:
            by_file[item['file']].append(item)
            
        prompt = f"""Analyze these potentially dead code elements and verify if they're actually unused.

Candidates:
{json.dumps(candidates, indent=2)}

Consider:
1. Could they be called dynamically (getattr, eval, decorators)?
2. Are they public APIs that external code might use?
3. Are they test fixtures or utilities?
4. Are they entry points (main, CLI commands)?
5. Are they callback handlers or event listeners?

Return JSON:
{{
  "confirmed_dead": [
    {{
      "name": "name",
      "file": "file",
      "line": line,
      "reason": "why definitely dead",
      "safe_to_remove": true/false
    }}
  ],
  "false_positives": [
    {{
      "name": "name",
      "file": "file",
      "reason": "why it's actually used"
    }}
  ],
  "needs_investigation": [
    {{
      "name": "name",
      "file": "file", 
      "reason": "why uncertain"
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
    
    def find_orphan_files(self) -> List[Dict]:
        """Find files that aren't imported anywhere."""
        files = self._get_code_files()
        
        # Build import graph
        imports = defaultdict(set)
        all_files_base = set()
        
        for f in files:
            rel_path = str(f.relative_to(self.repo_path))
            base_name = f.stem
            all_files_base.add(base_name)
            
            try:
                content = f.read_text(encoding='utf-8', errors='ignore')
                
                # Find imports
                if f.suffix == '.py':
                    for match in re.finditer(r'(?:from|import)\s+([\w.]+)', content):
                        imports[rel_path].add(match.group(1).split('.')[-1])
                else:
                    for match in re.finditer(r'import\s+.*?from\s+[\'"]\.?\/?([^\'"]+)', content):
                        imports[rel_path].add(Path(match.group(1)).stem)
                        
            except Exception:
                continue
                
        # Find files never imported
        all_imported = set()
        for file_imports in imports.values():
            all_imported.update(file_imports)
            
        orphans = []
        for f in files:
            base_name = f.stem
            rel_path = str(f.relative_to(self.repo_path))
            
            # Skip entry points
            if base_name in ['main', 'index', '__init__', 'setup', 'app', 'server']:
                continue
                
            if base_name not in all_imported:
                orphans.append({
                    'file': rel_path,
                    'name': base_name,
                    'reason': 'Not imported by any other file'
                })
                
        return orphans
    
    def generate_report(self, deep: bool = False) -> str:
        """Generate dead code report."""
        print("🔍 Scanning codebase for dead code...")
        
        report = []
        report.append("=" * 70)
        report.append("💀 DEAD CODE DETECTION REPORT")
        report.append(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        # Analyze codebase
        analysis = self.analyze_codebase(deep=deep)
        
        report.append("📊 CODEBASE STATS")
        report.append("-" * 40)
        report.append(f"  📁 Files analyzed: {analysis.get('files_analyzed', 0)}")
        report.append(f"  🔧 Functions found: {analysis.get('total_functions', 0)}")
        report.append(f"  📦 Classes found: {analysis.get('total_classes', 0)}")
        report.append("")
        
        # Potentially dead code
        dead = analysis.get('potentially_dead', [])
        if dead:
            report.append("⚠️  POTENTIALLY UNUSED CODE")
            report.append("-" * 40)
            
            # Group by file
            by_file = defaultdict(list)
            for item in dead:
                by_file[item['file']].append(item)
                
            for file_path, items in by_file.items():
                report.append(f"\n  📄 {file_path}")
                for item in items:
                    icon = "🔧" if item['type'] == 'unused_function' else "📦"
                    report.append(f"    {icon} {item['name']} (line {item['line']})")
                    
            report.append("")
        else:
            report.append("✅ No obviously unused code found")
            report.append("")
            
        # AI deep analysis
        if deep and 'ai_analysis' in analysis:
            ai = analysis['ai_analysis']
            
            if ai.get('confirmed_dead'):
                report.append("❌ CONFIRMED DEAD CODE (AI verified)")
                report.append("-" * 40)
                for item in ai['confirmed_dead']:
                    safe = "✅ Safe" if item.get('safe_to_remove') else "⚠️  Careful"
                    report.append(f"  • {item['name']} in {item['file']}")
                    report.append(f"    {item['reason']} [{safe}]")
                report.append("")
                
            if ai.get('needs_investigation'):
                report.append("🔍 NEEDS INVESTIGATION")
                report.append("-" * 40)
                for item in ai['needs_investigation']:
                    report.append(f"  • {item['name']} in {item['file']}")
                    report.append(f"    {item['reason']}")
                report.append("")
                
        # Orphan files
        print("🔍 Finding orphan files...")
        orphans = self.find_orphan_files()
        
        if orphans:
            report.append("📁 ORPHAN FILES (never imported)")
            report.append("-" * 40)
            for orphan in orphans[:15]:
                report.append(f"  • {orphan['file']}")
            if len(orphans) > 15:
                report.append(f"  ... and {len(orphans) - 15} more")
            report.append("")
            
        # Summary
        report.append("📋 SUMMARY")
        report.append("-" * 40)
        total_issues = len(dead) + len(orphans)
        report.append(f"  Total potential dead code: {len(dead)}")
        report.append(f"  Orphan files: {len(orphans)}")
        report.append(f"  Total issues: {total_issues}")
        report.append("")
        
        if total_issues > 0:
            report.append("💡 RECOMMENDATIONS:")
            report.append("  1. Review each item before removing")
            report.append("  2. Check for dynamic usage (reflection, config)")
            report.append("  3. Ensure tests still pass after removal")
            report.append("  4. Consider marking private (_prefix) instead of removing")
            
        report.append("")
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='💀 Dead Code Detector',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                        Quick scan
  %(prog)s --deep                 Deep AI analysis
  %(prog)s --file src/utils.py    Analyze single file
  %(prog)s --orphans              Find orphan files only
        """
    )
    
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--file', '-f', help='Analyze single file')
    parser.add_argument('--deep', '-d', action='store_true', help='Deep AI analysis')
    parser.add_argument('--orphans', action='store_true', help='Find orphan files only')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    detector = DeadCodeDetector(args.path)
    
    if args.file:
        print(f"🔍 Analyzing: {args.file}")
        result = detector.analyze_file(args.file)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ Error: {result['error']}")
            else:
                print(f"\n📄 {args.file}")
                print(f"🏥 Code Health Score: {result.get('code_health_score', 'N/A')}/100")
                print(f"🗑️  Removable Lines: ~{result.get('estimated_removable_lines', 0)}")
                
                for item in result.get('dead_code', []):
                    icon = {'high': '❌', 'medium': '⚠️', 'low': '❓'}.get(item.get('confidence'), '•')
                    print(f"\n{icon} [{item['type']}] {item.get('name', 'N/A')} (line {item.get('line', '?')})")
                    print(f"   {item.get('reason', '')}")
                    print(f"   💡 {item.get('suggestion', '')}")
                    
    elif args.orphans:
        orphans = detector.find_orphan_files()
        
        if args.json:
            print(json.dumps(orphans, indent=2))
        else:
            print("📁 ORPHAN FILES (never imported)")
            print("-" * 40)
            for orphan in orphans:
                print(f"  • {orphan['file']}")
            print(f"\nTotal: {len(orphans)} orphan files")
            
    else:
        if args.json:
            result = detector.analyze_codebase(deep=args.deep)
            print(json.dumps(result, indent=2))
        else:
            report = detector.generate_report(deep=args.deep)
            print(report)


if __name__ == '__main__':
    main()
