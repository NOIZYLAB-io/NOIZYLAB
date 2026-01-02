#!/usr/bin/env python3
"""
📚 AI-Powered Documentation Generator
Part of GABRIEL AI Dev Toolkit

Automatically generates documentation from code:
- Function/class docstrings
- API documentation
- README generation
- Usage examples
- Architecture diagrams (as text)
- Inline code comments
"""

import argparse
import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class AIDocsGenerator:
    """AI-powered documentation generation engine."""
    
    SUPPORTED_LANGUAGES = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.jsx': 'React',
        '.tsx': 'React TypeScript',
        '.java': 'Java',
        '.go': 'Go',
        '.rs': 'Rust',
        '.cpp': 'C++',
        '.c': 'C',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.swift': 'Swift',
        '.kt': 'Kotlin'
    }
    
    DOC_STYLES = {
        'Python': {
            'docstring': '"""',
            'inline': '#',
            'block_start': '"""',
            'block_end': '"""'
        },
        'JavaScript': {
            'docstring': '/**',
            'inline': '//',
            'block_start': '/**',
            'block_end': ' */'
        },
        'TypeScript': {
            'docstring': '/**',
            'inline': '//',
            'block_start': '/**',
            'block_end': ' */'
        }
    }
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        
    def detect_language(self, file_path: str) -> str:
        """Detect programming language from file extension."""
        ext = Path(file_path).suffix.lower()
        return self.SUPPORTED_LANGUAGES.get(ext, 'Unknown')
    
    def analyze_code_structure(self, content: str, language: str) -> Dict[str, Any]:
        """Analyze code to identify documentable elements."""
        structure = {
            'classes': [],
            'functions': [],
            'constants': [],
            'imports': [],
            'exports': []
        }
        
        lines = content.split('\n')
        
        if language == 'Python':
            # Classes
            for i, line in enumerate(lines):
                if line.strip().startswith('class '):
                    match = re.match(r'class\s+(\w+)', line.strip())
                    if match:
                        structure['classes'].append({
                            'name': match.group(1),
                            'line': i + 1,
                            'has_docstring': self._has_docstring(lines, i + 1, language)
                        })
                        
            # Functions
            for i, line in enumerate(lines):
                if re.match(r'\s*def\s+\w+', line):
                    match = re.match(r'\s*def\s+(\w+)\s*\(([^)]*)\)', line)
                    if match:
                        structure['functions'].append({
                            'name': match.group(1),
                            'params': match.group(2),
                            'line': i + 1,
                            'has_docstring': self._has_docstring(lines, i + 1, language)
                        })
                        
        elif language in ['JavaScript', 'TypeScript']:
            # Functions
            patterns = [
                r'function\s+(\w+)\s*\(([^)]*)\)',
                r'const\s+(\w+)\s*=\s*(?:async\s*)?\(([^)]*)\)\s*=>',
                r'(\w+)\s*:\s*(?:async\s*)?\(([^)]*)\)\s*=>'
            ]
            
            for i, line in enumerate(lines):
                for pattern in patterns:
                    match = re.search(pattern, line)
                    if match:
                        structure['functions'].append({
                            'name': match.group(1),
                            'params': match.group(2) if len(match.groups()) > 1 else '',
                            'line': i + 1,
                            'has_docstring': self._has_jsdoc(lines, i, language)
                        })
                        break
                        
            # Classes
            for i, line in enumerate(lines):
                if 'class ' in line:
                    match = re.search(r'class\s+(\w+)', line)
                    if match:
                        structure['classes'].append({
                            'name': match.group(1),
                            'line': i + 1,
                            'has_docstring': self._has_jsdoc(lines, i, language)
                        })
                        
        return structure
    
    def _has_docstring(self, lines: List[str], func_line: int, language: str) -> bool:
        """Check if a function has a docstring (Python)."""
        if func_line >= len(lines):
            return False
        next_line = lines[func_line].strip() if func_line < len(lines) else ''
        return '"""' in next_line or "'''" in next_line
    
    def _has_jsdoc(self, lines: List[str], func_line: int, language: str) -> bool:
        """Check if a function has JSDoc (JavaScript/TypeScript)."""
        if func_line <= 0:
            return False
        prev_line = lines[func_line - 1].strip()
        return '*/' in prev_line
    
    def generate_docstring(self, code_element: str, language: str, context: str = '') -> str:
        """Generate docstring for a code element."""
        style = self.DOC_STYLES.get(language, self.DOC_STYLES['Python'])
        
        prompt = f"""Generate comprehensive documentation for this {language} code element.

Code:
```{language.lower()}
{code_element}
```

Additional Context:
{context if context else 'No additional context provided'}

Generate documentation in the standard format for {language}:
- For Python: Use Google-style docstrings
- For JavaScript/TypeScript: Use JSDoc format

Include:
1. Brief description (one line)
2. Detailed description (if needed)
3. Parameters with types and descriptions
4. Return value with type and description
5. Raises/Throws (if applicable)
6. Examples (at least one)

Return ONLY the docstring/JSDoc comment, nothing else."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text.strip()
            
        except Exception as e:
            return f"# Documentation generation failed: {e}"
    
    def generate_file_docs(self, file_path: str) -> Dict[str, Any]:
        """Generate documentation for an entire file."""
        path = Path(file_path)
        if not path.exists():
            return {'error': f'File not found: {file_path}'}
            
        try:
            content = path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': f'Cannot read file: {e}'}
            
        language = self.detect_language(file_path)
        structure = self.analyze_code_structure(content, language)
        
        # Generate docs for undocumented elements
        docs_needed = []
        
        for cls in structure['classes']:
            if not cls['has_docstring']:
                docs_needed.append({
                    'type': 'class',
                    'name': cls['name'],
                    'line': cls['line']
                })
                
        for func in structure['functions']:
            if not func['has_docstring']:
                docs_needed.append({
                    'type': 'function',
                    'name': func['name'],
                    'line': func['line'],
                    'params': func.get('params', '')
                })
                
        # Use AI to generate file-level documentation
        file_doc = self._generate_file_header(content, language, path.name)
        
        return {
            'file': str(path),
            'language': language,
            'structure': structure,
            'undocumented_count': len(docs_needed),
            'undocumented_elements': docs_needed,
            'suggested_file_header': file_doc,
            'timestamp': datetime.now().isoformat()
        }
    
    def _generate_file_header(self, content: str, language: str, filename: str) -> str:
        """Generate file-level documentation header."""
        prompt = f"""Generate a file header documentation for this {language} file.

Filename: {filename}

Code (first 100 lines):
```{language.lower()}
{chr(10).join(content.split(chr(10))[:100])}
```

Generate a comprehensive file header that includes:
1. File description
2. Author placeholder
3. Date placeholder
4. Module/Package purpose
5. Key classes/functions overview
6. Dependencies
7. Usage example

Use the appropriate comment style for {language}."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text.strip()
            
        except Exception as e:
            return f"# File header generation failed: {e}"
    
    def generate_readme(self, dir_path: str = '.') -> str:
        """Generate README.md for a project directory."""
        path = Path(dir_path)
        
        # Gather project info
        files = list(path.rglob('*'))
        code_files = [f for f in files if f.suffix in self.SUPPORTED_LANGUAGES and 'node_modules' not in str(f)]
        
        # Read key files
        key_content = {}
        
        # Package files
        for pkg_file in ['package.json', 'setup.py', 'pyproject.toml', 'Cargo.toml', 'go.mod']:
            pkg_path = path / pkg_file
            if pkg_path.exists():
                try:
                    key_content[pkg_file] = pkg_path.read_text(encoding='utf-8')[:2000]
                except Exception:
                    pass
                    
        # Main entry points
        for entry in ['index.js', 'main.py', 'app.py', 'server.js', 'src/index.js', 'src/main.py']:
            entry_path = path / entry
            if entry_path.exists():
                try:
                    key_content[entry] = entry_path.read_text(encoding='utf-8')[:2000]
                except Exception:
                    pass
                    
        prompt = f"""Generate a comprehensive README.md for this project.

Project Directory: {path.name}

Code Files Found ({len(code_files)}):
{chr(10).join([str(f.relative_to(path)) for f in code_files[:30]])}

Key File Contents:
{json.dumps(key_content, indent=2)}

Generate a professional README.md including:
1. Project title and badges
2. Brief description
3. Features list
4. Installation instructions
5. Usage examples
6. Configuration (if applicable)
7. API documentation (if applicable)
8. Contributing guidelines
9. License placeholder

Use proper Markdown formatting with code blocks, headers, and lists."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text.strip()
            
        except Exception as e:
            return f"# README generation failed: {e}"
    
    def generate_api_docs(self, file_path: str) -> str:
        """Generate API documentation for a file."""
        path = Path(file_path)
        if not path.exists():
            return f"File not found: {file_path}"
            
        try:
            content = path.read_text(encoding='utf-8')
        except Exception as e:
            return f"Cannot read file: {e}"
            
        language = self.detect_language(file_path)
        
        prompt = f"""Generate comprehensive API documentation for this {language} file.

Filename: {path.name}

Code:
```{language.lower()}
{content[:10000]}
```

Generate API documentation in Markdown format including:
1. Overview
2. All exported classes with their methods
3. All exported functions
4. Type definitions (if TypeScript)
5. Constants and configuration options
6. Error handling
7. Example usage for each public API

Format as clean Markdown suitable for documentation sites."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text.strip()
            
        except Exception as e:
            return f"# API docs generation failed: {e}"
    
    def add_inline_comments(self, file_path: str) -> Dict[str, Any]:
        """Generate inline comments for complex code sections."""
        path = Path(file_path)
        if not path.exists():
            return {'error': f'File not found: {file_path}'}
            
        try:
            content = path.read_text(encoding='utf-8')
        except Exception as e:
            return {'error': f'Cannot read file: {e}'}
            
        language = self.detect_language(file_path)
        
        prompt = f"""Analyze this {language} code and add helpful inline comments.

Code:
```{language.lower()}
{content[:8000]}
```

Return the code with added inline comments that explain:
1. Complex logic
2. Non-obvious decisions
3. Important edge cases
4. Algorithm explanations
5. Performance considerations

Keep existing comments. Use {self.DOC_STYLES.get(language, {}).get('inline', '#')} for inline comments.
Return the complete code with comments added."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=8192,
                messages=[{"role": "user", "content": prompt}]
            )
            
            commented_code = response.content[0].text.strip()
            
            # Extract code from markdown if present
            if '```' in commented_code:
                parts = commented_code.split('```')
                for i, part in enumerate(parts):
                    if i % 2 == 1:  # Code blocks are odd indices
                        if '\n' in part:
                            commented_code = '\n'.join(part.split('\n')[1:])
                            break
                            
            return {
                'original_file': str(path),
                'language': language,
                'commented_code': commented_code,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def generate_report(self, path: str = '.') -> str:
        """Generate documentation coverage report."""
        target = Path(path)
        
        report = []
        report.append("=" * 70)
        report.append("📚 DOCUMENTATION COVERAGE REPORT")
        report.append(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        if target.is_file():
            files = [target]
        else:
            files = [f for f in target.rglob('*') 
                    if f.suffix in self.SUPPORTED_LANGUAGES
                    and 'node_modules' not in str(f)
                    and '.git' not in str(f)]
        
        total_elements = 0
        undocumented_elements = 0
        
        for file_path in files[:50]:  # Limit to 50 files
            try:
                result = self.generate_file_docs(str(file_path))
                
                if 'error' in result:
                    continue
                    
                structure = result.get('structure', {})
                classes = structure.get('classes', [])
                functions = structure.get('functions', [])
                
                file_total = len(classes) + len(functions)
                file_undoc = len([c for c in classes if not c['has_docstring']]) + \
                            len([f for f in functions if not f['has_docstring']])
                
                total_elements += file_total
                undocumented_elements += file_undoc
                
                if file_undoc > 0:
                    coverage = ((file_total - file_undoc) / max(file_total, 1)) * 100
                    icon = '🔴' if coverage < 50 else '🟡' if coverage < 80 else '🟢'
                    
                    rel_path = file_path.relative_to(target) if target.is_dir() else file_path.name
                    report.append(f"{icon} {rel_path}")
                    report.append(f"   Coverage: {coverage:.0f}% ({file_total - file_undoc}/{file_total})")
                    
                    for item in result.get('undocumented_elements', [])[:3]:
                        report.append(f"   ⚠️ {item['type']} '{item['name']}' (line {item['line']})")
                    report.append("")
                    
            except Exception as e:
                report.append(f"❌ {file_path}: {e}")
                
        # Summary
        report.append("-" * 40)
        total_coverage = ((total_elements - undocumented_elements) / max(total_elements, 1)) * 100
        report.append(f"\n📊 OVERALL COVERAGE: {total_coverage:.1f}%")
        report.append(f"   Total Elements: {total_elements}")
        report.append(f"   Documented: {total_elements - undocumented_elements}")
        report.append(f"   Undocumented: {undocumented_elements}")
        
        if total_coverage < 60:
            report.append("\n⚠️ RECOMMENDATION: Documentation coverage is low. Consider running:")
            report.append("   python ai-docs.py --file <path> --add-docs")
            
        report.append("")
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='📚 AI-Powered Documentation Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --file src/main.py          Analyze file documentation
  %(prog)s --file src/main.py --api    Generate API docs
  %(prog)s --readme                    Generate README.md
  %(prog)s --comments src/complex.py   Add inline comments
  %(prog)s --report                    Documentation coverage report
        """
    )
    
    parser.add_argument('--file', '-f', help='Target file to document')
    parser.add_argument('--path', '-p', default='.', help='Project path')
    parser.add_argument('--api', action='store_true', help='Generate API documentation')
    parser.add_argument('--readme', action='store_true', help='Generate README.md')
    parser.add_argument('--comments', action='store_true', help='Add inline comments')
    parser.add_argument('--report', action='store_true', help='Coverage report')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    # Check API key
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    generator = AIDocsGenerator(args.path)
    
    output = None
    
    if args.readme:
        print("📚 Generating README.md...")
        output = generator.generate_readme(args.path)
        
    elif args.api and args.file:
        print(f"📖 Generating API documentation for {args.file}...")
        output = generator.generate_api_docs(args.file)
        
    elif args.comments and args.file:
        print(f"💬 Adding inline comments to {args.file}...")
        result = generator.add_inline_comments(args.file)
        if args.json:
            output = json.dumps(result, indent=2)
        else:
            output = result.get('commented_code', str(result))
            
    elif args.report:
        print("📊 Generating documentation coverage report...")
        output = generator.generate_report(args.path)
        
    elif args.file:
        print(f"📄 Analyzing {args.file}...")
        result = generator.generate_file_docs(args.file)
        
        if args.json:
            output = json.dumps(result, indent=2)
        else:
            output = f"""
📄 File: {result.get('file', 'Unknown')}
🔤 Language: {result.get('language', 'Unknown')}
📊 Undocumented Elements: {result.get('undocumented_count', 0)}

📝 Suggested File Header:
{result.get('suggested_file_header', 'N/A')}
"""
            
    else:
        print("📊 Generating documentation coverage report...")
        output = generator.generate_report(args.path)
        
    if output:
        if args.output:
            Path(args.output).write_text(output)
            print(f"✅ Output saved to {args.output}")
        else:
            print(output)


if __name__ == '__main__':
    main()
