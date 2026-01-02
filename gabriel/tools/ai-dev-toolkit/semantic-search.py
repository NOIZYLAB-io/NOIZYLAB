#!/usr/bin/env python3
"""
🔍 AI-Powered Semantic Code Search
Part of GABRIEL AI Dev Toolkit

Natural language code search:
- Find code by intent, not just text
- Understand what code does
- Cross-file relationship discovery
- Concept-based searching
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


class SemanticCodeSearch:
    """AI-powered semantic code search engine."""
    
    SUPPORTED_EXTENSIONS = [
        '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.go', '.rs',
        '.cpp', '.c', '.h', '.hpp', '.rb', '.php', '.swift', '.kt',
        '.scala', '.cs', '.vue', '.svelte'
    ]
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        self.index = None
        
    def _get_code_files(self, max_files: int = 500) -> List[Path]:
        """Get all code files in the repository."""
        files = []
        
        for ext in self.SUPPORTED_EXTENSIONS:
            for f in self.repo_path.rglob(f'*{ext}'):
                # Skip common non-source directories
                if any(skip in str(f) for skip in [
                    'node_modules', '.git', '__pycache__', 'venv', 
                    'dist', 'build', '.next', 'vendor', 'target'
                ]):
                    continue
                files.append(f)
                
                if len(files) >= max_files:
                    break
                    
        return files
    
    def _extract_code_elements(self, file_path: Path) -> Dict[str, Any]:
        """Extract meaningful code elements from a file."""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            return None
            
        lines = content.split('\n')
        elements = {
            'file': str(file_path.relative_to(self.repo_path)),
            'language': self._detect_language(file_path),
            'functions': [],
            'classes': [],
            'imports': [],
            'comments': [],
            'content_preview': content[:2000]
        }
        
        # Extract based on language
        lang = elements['language']
        
        if lang == 'Python':
            elements['functions'] = self._extract_python_functions(content)
            elements['classes'] = self._extract_python_classes(content)
            elements['imports'] = re.findall(r'^(?:from|import)\s+[\w.]+', content, re.MULTILINE)
            
        elif lang in ['JavaScript', 'TypeScript']:
            elements['functions'] = self._extract_js_functions(content)
            elements['classes'] = self._extract_js_classes(content)
            elements['imports'] = re.findall(r'^import\s+.*?from\s+[\'"]([^\'"]+)', content, re.MULTILINE)
            
        # Extract comments (universal)
        elements['comments'] = self._extract_comments(content, lang)
        
        return elements
    
    def _detect_language(self, file_path: Path) -> str:
        """Detect programming language from file extension."""
        ext = file_path.suffix.lower()
        mapping = {
            '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
            '.jsx': 'React', '.tsx': 'React TypeScript', '.java': 'Java',
            '.go': 'Go', '.rs': 'Rust', '.cpp': 'C++', '.c': 'C',
            '.rb': 'Ruby', '.php': 'PHP', '.swift': 'Swift', '.kt': 'Kotlin'
        }
        return mapping.get(ext, 'Unknown')
    
    def _extract_python_functions(self, content: str) -> List[Dict]:
        """Extract Python function definitions."""
        pattern = r'^\s*(?:async\s+)?def\s+(\w+)\s*\(([^)]*)\).*?(?:->.*?)?:'
        matches = re.finditer(pattern, content, re.MULTILINE)
        
        functions = []
        for match in matches:
            functions.append({
                'name': match.group(1),
                'params': match.group(2).strip(),
                'line': content[:match.start()].count('\n') + 1
            })
        return functions
    
    def _extract_python_classes(self, content: str) -> List[Dict]:
        """Extract Python class definitions."""
        pattern = r'^\s*class\s+(\w+)(?:\s*\(([^)]*)\))?\s*:'
        matches = re.finditer(pattern, content, re.MULTILINE)
        
        classes = []
        for match in matches:
            classes.append({
                'name': match.group(1),
                'bases': match.group(2) if match.group(2) else '',
                'line': content[:match.start()].count('\n') + 1
            })
        return classes
    
    def _extract_js_functions(self, content: str) -> List[Dict]:
        """Extract JavaScript/TypeScript function definitions."""
        patterns = [
            r'function\s+(\w+)\s*\(([^)]*)\)',
            r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?\(([^)]*)\)\s*=>',
            r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?function\s*\(([^)]*)\)'
        ]
        
        functions = []
        for pattern in patterns:
            matches = re.finditer(pattern, content, re.MULTILINE)
            for match in matches:
                functions.append({
                    'name': match.group(1),
                    'params': match.group(2).strip(),
                    'line': content[:match.start()].count('\n') + 1
                })
        return functions
    
    def _extract_js_classes(self, content: str) -> List[Dict]:
        """Extract JavaScript/TypeScript class definitions."""
        pattern = r'class\s+(\w+)(?:\s+extends\s+(\w+))?\s*{'
        matches = re.finditer(pattern, content, re.MULTILINE)
        
        classes = []
        for match in matches:
            classes.append({
                'name': match.group(1),
                'extends': match.group(2) or '',
                'line': content[:match.start()].count('\n') + 1
            })
        return classes
    
    def _extract_comments(self, content: str, language: str) -> List[str]:
        """Extract meaningful comments."""
        comments = []
        
        # Single line comments
        if language == 'Python':
            comments.extend(re.findall(r'#\s*(.+)$', content, re.MULTILINE))
        else:
            comments.extend(re.findall(r'//\s*(.+)$', content, re.MULTILINE))
            
        # Multi-line comments
        if language == 'Python':
            docstrings = re.findall(r'"""(.+?)"""', content, re.DOTALL)
            comments.extend([d.strip()[:200] for d in docstrings])
        else:
            block_comments = re.findall(r'/\*(.+?)\*/', content, re.DOTALL)
            comments.extend([c.strip()[:200] for c in block_comments])
            
        return comments[:20]  # Limit comments
    
    def build_index(self) -> Dict[str, Any]:
        """Build searchable index of codebase."""
        print("📚 Building code index...")
        files = self._get_code_files()
        
        self.index = {
            'files': [],
            'timestamp': datetime.now().isoformat(),
            'stats': {
                'total_files': len(files),
                'total_functions': 0,
                'total_classes': 0
            }
        }
        
        for file_path in files:
            elements = self._extract_code_elements(file_path)
            if elements:
                self.index['files'].append(elements)
                self.index['stats']['total_functions'] += len(elements.get('functions', []))
                self.index['stats']['total_classes'] += len(elements.get('classes', []))
                
        print(f"✅ Indexed {len(self.index['files'])} files")
        return self.index
    
    def search(self, query: str, max_results: int = 10) -> Dict[str, Any]:
        """Search codebase using natural language."""
        if not self.index:
            self.build_index()
            
        # First, do a quick text search for potential matches
        text_matches = self._text_search(query)
        
        # Then use AI to find semantic matches
        prompt = f"""Search this codebase for: "{query}"

Codebase Index:
{json.dumps(self.index['files'][:50], indent=2)}

Text Search Matches (pre-filtered):
{json.dumps(text_matches[:10], indent=2)}

Find the most relevant code for the search query. Consider:
1. Semantic meaning (code that does what the query describes)
2. Function/class names that relate to the query
3. Comments that describe relevant functionality
4. Import patterns that suggest relevant modules

Return results in JSON format:
{{
  "results": [
    {{
      "file": "path/to/file.ext",
      "relevance": 0.0-1.0,
      "match_type": "function/class/file/comment",
      "match_name": "name of matched element",
      "line": line_number,
      "explanation": "why this matches the query",
      "code_snippet": "relevant code snippet if available"
    }}
  ],
  "summary": "brief summary of what was found",
  "suggestions": ["related searches to try"]
}}

Rank by relevance. Include up to {max_results} results."""

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
            result['query'] = query
            result['timestamp'] = datetime.now().isoformat()
            
            return result
            
        except Exception as e:
            return {
                'error': str(e),
                'query': query,
                'text_matches': text_matches[:5]
            }
    
    def _text_search(self, query: str) -> List[Dict]:
        """Quick text-based search for pre-filtering."""
        matches = []
        query_lower = query.lower()
        keywords = query_lower.split()
        
        if not self.index:
            return matches
            
        for file_info in self.index['files']:
            score = 0
            match_info = {
                'file': file_info['file'],
                'matches': []
            }
            
            # Check functions
            for func in file_info.get('functions', []):
                if any(kw in func['name'].lower() for kw in keywords):
                    score += 3
                    match_info['matches'].append(f"function:{func['name']}")
                    
            # Check classes
            for cls in file_info.get('classes', []):
                if any(kw in cls['name'].lower() for kw in keywords):
                    score += 3
                    match_info['matches'].append(f"class:{cls['name']}")
                    
            # Check file name
            if any(kw in file_info['file'].lower() for kw in keywords):
                score += 2
                match_info['matches'].append(f"filename")
                
            # Check comments
            for comment in file_info.get('comments', []):
                if any(kw in comment.lower() for kw in keywords):
                    score += 1
                    match_info['matches'].append(f"comment")
                    break
                    
            if score > 0:
                match_info['score'] = score
                matches.append(match_info)
                
        # Sort by score
        matches.sort(key=lambda x: x['score'], reverse=True)
        return matches
    
    def find_related(self, file_path: str) -> Dict[str, Any]:
        """Find files related to the given file."""
        if not self.index:
            self.build_index()
            
        # Find the file in index
        target_file = None
        for f in self.index['files']:
            if f['file'] == file_path or file_path in f['file']:
                target_file = f
                break
                
        if not target_file:
            return {'error': f'File not found: {file_path}'}
            
        prompt = f"""Find files related to this file in the codebase.

Target File:
{json.dumps(target_file, indent=2)}

Other Files:
{json.dumps([f for f in self.index['files'] if f['file'] != target_file['file']][:40], indent=2)}

Find related files based on:
1. Import relationships
2. Similar functionality
3. Same domain/feature area
4. Shared patterns

Return in JSON format:
{{
  "related_files": [
    {{
      "file": "path",
      "relationship": "imports/imported-by/similar/same-domain",
      "confidence": 0.0-1.0,
      "reason": "why related"
    }}
  ],
  "dependency_graph": ["list of import relationships"],
  "feature_area": "identified feature/domain area"
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
    
    def explain_code(self, file_path: str, line_start: int = None, line_end: int = None) -> str:
        """Explain what code does using AI."""
        full_path = self.repo_path / file_path
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            return f"Error reading file: {e}"
            
        if line_start and line_end:
            lines = content.split('\n')
            content = '\n'.join(lines[line_start-1:line_end])
            
        prompt = f"""Explain what this code does in plain English.

File: {file_path}
Language: {self._detect_language(full_path)}

Code:
```
{content[:8000]}
```

Provide a clear explanation including:
1. Overall purpose
2. Key functions/classes and what they do
3. Important logic flows
4. External dependencies
5. How it fits into a larger system (if apparent)

Be concise but comprehensive."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2048,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text.strip()
        except Exception as e:
            return f"Error: {e}"
    
    def generate_report(self, query: str = None) -> str:
        """Generate search report or codebase overview."""
        if not self.index:
            self.build_index()
            
        report = []
        report.append("=" * 70)
        report.append("🔍 SEMANTIC CODE SEARCH")
        report.append(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        # Codebase stats
        stats = self.index.get('stats', {})
        report.append("📊 CODEBASE OVERVIEW")
        report.append("-" * 40)
        report.append(f"  📁 Files: {stats.get('total_files', 0)}")
        report.append(f"  🔧 Functions: {stats.get('total_functions', 0)}")
        report.append(f"  📦 Classes: {stats.get('total_classes', 0)}")
        report.append("")
        
        if query:
            print(f"🔍 Searching for: {query}")
            results = self.search(query)
            
            report.append(f"🔎 SEARCH: '{query}'")
            report.append("-" * 40)
            
            if 'error' in results:
                report.append(f"❌ Error: {results['error']}")
            else:
                report.append(f"📋 {results.get('summary', 'Results found')}")
                report.append("")
                
                for i, result in enumerate(results.get('results', [])[:10], 1):
                    rel = result.get('relevance', 0) * 100
                    report.append(f"  {i}. [{rel:.0f}%] {result.get('file')}")
                    report.append(f"      Type: {result.get('match_type')} - {result.get('match_name', 'N/A')}")
                    report.append(f"      {result.get('explanation', '')[:60]}")
                    report.append("")
                    
                if results.get('suggestions'):
                    report.append("💡 Related searches:")
                    for sug in results['suggestions']:
                        report.append(f"   • {sug}")
                        
        report.append("")
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='🔍 AI-Powered Semantic Code Search',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "authentication logic"     Search for auth code
  %(prog)s "database queries"         Find DB operations
  %(prog)s --related src/api.js       Find related files
  %(prog)s --explain src/utils.py     Explain code
  %(prog)s --index                    Build/rebuild index
        """
    )
    
    parser.add_argument('query', nargs='?', help='Search query')
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--related', help='Find files related to this file')
    parser.add_argument('--explain', help='Explain code in file')
    parser.add_argument('--lines', help='Line range for explain (start-end)')
    parser.add_argument('--index', action='store_true', help='Build index only')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--max-results', type=int, default=10, help='Max results')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    searcher = SemanticCodeSearch(args.path)
    
    if args.index:
        index = searcher.build_index()
        if args.json:
            print(json.dumps(index['stats'], indent=2))
        else:
            print(f"✅ Indexed {index['stats']['total_files']} files")
            print(f"   {index['stats']['total_functions']} functions")
            print(f"   {index['stats']['total_classes']} classes")
            
    elif args.related:
        print(f"🔗 Finding files related to: {args.related}")
        result = searcher.find_related(args.related)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ {result['error']}")
            else:
                print(f"\n📂 Feature Area: {result.get('feature_area', 'Unknown')}")
                print("\n🔗 Related Files:")
                for rel in result.get('related_files', []):
                    conf = rel.get('confidence', 0) * 100
                    print(f"  • [{conf:.0f}%] {rel.get('file')}")
                    print(f"    {rel.get('relationship')}: {rel.get('reason', '')[:50]}")
                    
    elif args.explain:
        line_start = line_end = None
        if args.lines:
            parts = args.lines.split('-')
            line_start = int(parts[0])
            line_end = int(parts[1]) if len(parts) > 1 else line_start + 50
            
        print(f"📖 Explaining: {args.explain}")
        explanation = searcher.explain_code(args.explain, line_start, line_end)
        print(f"\n{explanation}")
        
    elif args.query:
        if args.json:
            result = searcher.search(args.query, args.max_results)
            print(json.dumps(result, indent=2))
        else:
            output = searcher.generate_report(args.query)
            print(output)
            
    else:
        output = searcher.generate_report()
        print(output)


if __name__ == '__main__':
    main()
