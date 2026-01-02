#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  🧪 AI TEST SUGGESTION ENGINE v1.0                                            ║
║  Recommend tests based on changes and coverage analysis                       ║
║  Part of: NOIZYLAB AI Dev Toolkit                                             ║
║  Updated: 2026-01-02                                                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import subprocess
import os
import sys
import re
import json
import ast
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field
from collections import defaultdict

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
MODEL = "claude-sonnet-4-20250514"

# ═══════════════════════════════════════════════════════════════════════════════
# DATA CLASSES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Function:
    """Represents a function/method to test."""
    name: str
    file: str
    line: int
    signature: str
    docstring: str = ""
    complexity: int = 1
    is_public: bool = True
    has_tests: bool = False
    coverage: float = 0.0

@dataclass
class TestSuggestion:
    """A suggested test case."""
    function: str
    test_name: str
    test_type: str  # unit, integration, edge_case, error_handling
    description: str
    test_code: str
    priority: str  # high, medium, low
    reason: str

@dataclass
class CoverageReport:
    """Code coverage information."""
    file: str
    covered_lines: set = field(default_factory=set)
    uncovered_lines: set = field(default_factory=set)
    coverage_percent: float = 0.0

# ═══════════════════════════════════════════════════════════════════════════════
# CODE ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

def parse_python_file(file_path: str) -> list[Function]:
    """Extract functions from Python file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        functions = []
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Get signature
                args = []
                for arg in node.args.args:
                    args.append(arg.arg)
                signature = f"{node.name}({', '.join(args)})"
                
                # Get docstring
                docstring = ast.get_docstring(node) or ""
                
                # Calculate complexity (simple estimate)
                complexity = 1
                for child in ast.walk(node):
                    if isinstance(child, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                        complexity += 1
                    elif isinstance(child, (ast.And, ast.Or)):
                        complexity += 1
                
                functions.append(Function(
                    name=node.name,
                    file=file_path,
                    line=node.lineno,
                    signature=signature,
                    docstring=docstring[:200],
                    complexity=complexity,
                    is_public=not node.name.startswith('_')
                ))
        
        return functions
    except Exception as e:
        return []

def parse_javascript_file(file_path: str) -> list[Function]:
    """Extract functions from JavaScript/TypeScript file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        functions = []
        
        # Function declarations
        for match in re.finditer(r'(?:async\s+)?function\s+(\w+)\s*\(([^)]*)\)', content):
            line = content[:match.start()].count('\n') + 1
            functions.append(Function(
                name=match.group(1),
                file=file_path,
                line=line,
                signature=f"{match.group(1)}({match.group(2)})",
                is_public=not match.group(1).startswith('_')
            ))
        
        # Arrow functions and methods
        for match in re.finditer(r'(?:const|let|var)?\s*(\w+)\s*[=:]\s*(?:async\s+)?\(?([^)=]*)\)?\s*=>', content):
            line = content[:match.start()].count('\n') + 1
            functions.append(Function(
                name=match.group(1),
                file=file_path,
                line=line,
                signature=f"{match.group(1)}({match.group(2)})",
                is_public=not match.group(1).startswith('_')
            ))
        
        # Class methods
        for match in re.finditer(r'(?:async\s+)?(\w+)\s*\(([^)]*)\)\s*{', content):
            if match.group(1) not in ('if', 'for', 'while', 'switch', 'catch', 'function'):
                line = content[:match.start()].count('\n') + 1
                functions.append(Function(
                    name=match.group(1),
                    file=file_path,
                    line=line,
                    signature=f"{match.group(1)}({match.group(2)})",
                    is_public=not match.group(1).startswith('_')
                ))
        
        return functions
    except Exception as e:
        return []

def find_existing_tests(test_dir: str = "tests") -> dict[str, list[str]]:
    """Find existing test functions."""
    existing = defaultdict(list)
    
    for pattern in ['test_*.py', '*_test.py', '*.test.js', '*.spec.js', '*.test.ts', '*.spec.ts']:
        for test_file in Path('.').rglob(pattern):
            try:
                with open(test_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find test functions
                for match in re.finditer(r'(?:def|function|it|test)\s*[(\s][\'"]*(?:test_)?(\w+)', content):
                    existing[match.group(1).lower()].append(str(test_file))
            except:
                pass
    
    return existing

def get_changed_functions(base_branch: str = "main") -> list[str]:
    """Get functions changed in current branch."""
    try:
        result = subprocess.run(
            ['git', 'diff', base_branch, '--unified=0'],
            capture_output=True, text=True, check=True
        )
        
        changed = set()
        current_file = None
        
        for line in result.stdout.split('\n'):
            if line.startswith('+++'):
                current_file = line[6:]
            elif line.startswith('+') and not line.startswith('+++'):
                # Look for function definitions in added lines
                if match := re.search(r'def\s+(\w+)|function\s+(\w+)|(\w+)\s*[=:]\s*(?:async\s+)?\(', line):
                    func_name = match.group(1) or match.group(2) or match.group(3)
                    if func_name:
                        changed.add(func_name)
        
        return list(changed)
    except:
        return []

# ═══════════════════════════════════════════════════════════════════════════════
# COVERAGE ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

def parse_coverage_report(coverage_file: str = "coverage.json") -> dict[str, CoverageReport]:
    """Parse coverage report."""
    if not os.path.exists(coverage_file):
        return {}
    
    try:
        with open(coverage_file, 'r') as f:
            data = json.load(f)
        
        reports = {}
        
        # Handle different coverage formats
        if 'files' in data:
            for file_path, file_data in data['files'].items():
                report = CoverageReport(file=file_path)
                
                if 'executed_lines' in file_data:
                    report.covered_lines = set(file_data['executed_lines'])
                if 'missing_lines' in file_data:
                    report.uncovered_lines = set(file_data['missing_lines'])
                
                total = len(report.covered_lines) + len(report.uncovered_lines)
                if total > 0:
                    report.coverage_percent = len(report.covered_lines) / total * 100
                
                reports[file_path] = report
        
        return reports
    except Exception as e:
        return {}

def run_coverage_analysis() -> dict[str, CoverageReport]:
    """Run coverage analysis."""
    try:
        # Try pytest with coverage
        subprocess.run(
            ['python', '-m', 'pytest', '--cov=.', '--cov-report=json', '-q'],
            capture_output=True, timeout=300
        )
        return parse_coverage_report('coverage.json')
    except:
        return {}

# ═══════════════════════════════════════════════════════════════════════════════
# TEST GENERATION
# ═══════════════════════════════════════════════════════════════════════════════

def generate_test_suggestions(functions: list[Function], existing_tests: dict, coverage: dict) -> list[TestSuggestion]:
    """Generate test suggestions for functions."""
    suggestions = []
    
    for func in functions:
        # Skip private functions unless complex
        if not func.is_public and func.complexity < 3:
            continue
        
        # Check if already has tests
        func_lower = func.name.lower()
        if func_lower in existing_tests:
            func.has_tests = True
            continue
        
        # Get coverage info
        file_coverage = coverage.get(func.file)
        if file_coverage:
            func.coverage = file_coverage.coverage_percent
        
        # Determine priority
        if func.complexity > 5:
            priority = 'high'
        elif func.complexity > 2 or func.coverage < 50:
            priority = 'medium'
        else:
            priority = 'low'
        
        # Generate basic test suggestion
        suggestions.append(TestSuggestion(
            function=func.name,
            test_name=f"test_{func.name}_basic",
            test_type='unit',
            description=f"Basic functionality test for {func.name}",
            test_code=generate_basic_test(func),
            priority=priority,
            reason=f"Complexity: {func.complexity}, Coverage: {func.coverage:.0f}%"
        ))
        
        # Add edge case tests for complex functions
        if func.complexity > 3:
            suggestions.append(TestSuggestion(
                function=func.name,
                test_name=f"test_{func.name}_edge_cases",
                test_type='edge_case',
                description=f"Edge case tests for {func.name}",
                test_code=generate_edge_case_test(func),
                priority='high' if func.complexity > 5 else 'medium',
                reason=f"High complexity ({func.complexity}) requires edge case coverage"
            ))
        
        # Add error handling tests
        suggestions.append(TestSuggestion(
            function=func.name,
            test_name=f"test_{func.name}_error_handling",
            test_type='error_handling',
            description=f"Error handling test for {func.name}",
            test_code=generate_error_test(func),
            priority='medium',
            reason="All functions should handle errors gracefully"
        ))
    
    return suggestions

def generate_basic_test(func: Function) -> str:
    """Generate basic test code."""
    if func.file.endswith('.py'):
        return f'''def test_{func.name}_basic():
    """Test basic functionality of {func.name}."""
    # Arrange
    # TODO: Set up test data
    
    # Act
    result = {func.name}()  # TODO: Add arguments
    
    # Assert
    assert result is not None  # TODO: Add specific assertions
'''
    else:
        return f'''test('{func.name} basic functionality', () => {{
    // Arrange
    // TODO: Set up test data
    
    // Act
    const result = {func.name}();  // TODO: Add arguments
    
    // Assert
    expect(result).toBeDefined();  // TODO: Add specific assertions
}});
'''

def generate_edge_case_test(func: Function) -> str:
    """Generate edge case test code."""
    if func.file.endswith('.py'):
        return f'''@pytest.mark.parametrize("input,expected", [
    (None, None),  # TODO: Define edge cases
    ("", ""),
    ([], []),
])
def test_{func.name}_edge_cases(input, expected):
    """Test edge cases for {func.name}."""
    result = {func.name}(input)  # TODO: Adjust
    assert result == expected
'''
    else:
        return f'''describe('{func.name} edge cases', () => {{
    test.each([
        [null, null],
        ['', ''],
        [[], []],
    ])('{func.name}(%s) should return %s', (input, expected) => {{
        expect({func.name}(input)).toEqual(expected);
    }});
}});
'''

def generate_error_test(func: Function) -> str:
    """Generate error handling test code."""
    if func.file.endswith('.py'):
        return f'''def test_{func.name}_error_handling():
    """Test error handling in {func.name}."""
    with pytest.raises(ValueError):  # TODO: Adjust exception type
        {func.name}(invalid_input)  # TODO: Define invalid input
'''
    else:
        return f'''test('{func.name} error handling', () => {{
    expect(() => {{
        {func.name}(invalidInput);  // TODO: Define invalid input
    }}).toThrow();  // TODO: Specify error type
}});
'''

# ═══════════════════════════════════════════════════════════════════════════════
# AI ENHANCEMENT
# ═══════════════════════════════════════════════════════════════════════════════

def ai_generate_tests(func: Function, source_code: str) -> list[TestSuggestion]:
    """Use AI to generate comprehensive tests."""
    if not ANTHROPIC_API_KEY:
        return []
    
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        prompt = f"""Generate comprehensive test cases for this function.

FILE: {func.file}
FUNCTION: {func.signature}
DOCSTRING: {func.docstring}

SOURCE CODE:
```
{source_code[:3000]}
```

Generate:
1. Happy path test
2. Edge case tests (empty input, null, boundary values)
3. Error handling tests
4. Integration test if applicable

For each test provide:
- Test name (test_function_scenario format)
- Test type (unit/edge_case/error_handling/integration)
- Brief description
- Complete test code

Use {'pytest' if func.file.endswith('.py') else 'jest'} framework.
Format as JSON array of objects with keys: test_name, test_type, description, code"""

        response = client.messages.create(
            model=MODEL,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        result = response.content[0].text.strip()
        
        # Parse JSON from response
        json_match = re.search(r'\[.*\]', result, re.DOTALL)
        if json_match:
            tests = json.loads(json_match.group())
            return [
                TestSuggestion(
                    function=func.name,
                    test_name=t.get('test_name', f"test_{func.name}"),
                    test_type=t.get('test_type', 'unit'),
                    description=t.get('description', ''),
                    test_code=t.get('code', ''),
                    priority='high',
                    reason='AI-generated comprehensive test'
                )
                for t in tests
            ]
        
        return []
        
    except Exception as e:
        print(f"AI error: {e}")
        return []

# ═══════════════════════════════════════════════════════════════════════════════
# OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

def print_suggestions(suggestions: list[TestSuggestion], output_file: str = None):
    """Print test suggestions."""
    if not suggestions:
        print("✅ No additional tests needed!")
        return
    
    # Group by priority
    high = [s for s in suggestions if s.priority == 'high']
    medium = [s for s in suggestions if s.priority == 'medium']
    low = [s for s in suggestions if s.priority == 'low']
    
    output = [f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  🧪 TEST SUGGESTIONS                                                          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  High Priority:   {len(high):3}                                                        ║
║  Medium Priority: {len(medium):3}                                                        ║
║  Low Priority:    {len(low):3}                                                        ║
║  Total:           {len(suggestions):3}                                                        ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""]
    
    for priority, tests in [('🔴 HIGH', high), ('🟡 MEDIUM', medium), ('🟢 LOW', low)]:
        if tests:
            output.append(f"\n{priority} PRIORITY:\n")
            for test in tests:
                output.append(f"  📋 {test.test_name}")
                output.append(f"     Function: {test.function}")
                output.append(f"     Type: {test.test_type}")
                output.append(f"     Reason: {test.reason}")
                output.append(f"     Description: {test.description}")
                output.append("")
    
    result = '\n'.join(output)
    print(result)
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write(result)
        print(f"\n📄 Saved to {output_file}")

def generate_test_file(suggestions: list[TestSuggestion], output_file: str):
    """Generate a test file from suggestions."""
    is_python = output_file.endswith('.py')
    
    if is_python:
        header = '''"""
Auto-generated test file by AI Test Suggestion Engine
Generated: {date}
"""

import pytest
from typing import Any

# TODO: Import modules to test
# from mymodule import function_to_test

'''
    else:
        header = '''/**
 * Auto-generated test file by AI Test Suggestion Engine
 * Generated: {date}
 */

// TODO: Import modules to test
// import {{ functionToTest }} from './mymodule';

'''
    
    content = header.format(date=__import__('datetime').datetime.now().isoformat())
    
    for suggestion in suggestions:
        content += f"\n# {suggestion.description}\n" if is_python else f"\n// {suggestion.description}\n"
        content += suggestion.test_code
        content += "\n"
    
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Generated {output_file}")

# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='AI Test Suggestion Engine')
    parser.add_argument('--file', '-f', help='Analyze specific file')
    parser.add_argument('--changed', '-c', action='store_true', help='Only analyze changed files')
    parser.add_argument('--generate', '-g', help='Generate test file')
    parser.add_argument('--ai', action='store_true', help='Use AI for comprehensive tests')
    parser.add_argument('--coverage', action='store_true', help='Run coverage analysis first')
    parser.add_argument('--output', '-o', help='Output file for suggestions')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  🧪 AI TEST SUGGESTION ENGINE v1.0                                            ║
╚═══════════════════════════════════════════════════════════════════════════════╝
""")
    
    # Find existing tests
    print("🔍 Finding existing tests...")
    existing_tests = find_existing_tests()
    print(f"   Found {sum(len(v) for v in existing_tests.values())} existing tests")
    
    # Get coverage
    coverage = {}
    if args.coverage:
        print("📊 Running coverage analysis...")
        coverage = run_coverage_analysis()
    
    # Find files to analyze
    if args.file:
        files = [args.file]
    elif args.changed:
        try:
            result = subprocess.run(
                ['git', 'diff', '--name-only', 'main'],
                capture_output=True, text=True
            )
            files = [f for f in result.stdout.strip().split('\n') 
                    if f.endswith(('.py', '.js', '.ts'))]
        except:
            files = []
    else:
        # Find all source files
        files = []
        for ext in ['*.py', '*.js', '*.ts']:
            files.extend([str(f) for f in Path('.').rglob(ext) 
                         if 'test' not in str(f).lower() 
                         and 'node_modules' not in str(f)
                         and '.git' not in str(f)])
    
    # Parse functions
    print(f"📂 Analyzing {len(files)} files...")
    all_functions = []
    for file_path in files:
        if file_path.endswith('.py'):
            all_functions.extend(parse_python_file(file_path))
        else:
            all_functions.extend(parse_javascript_file(file_path))
    
    print(f"   Found {len(all_functions)} functions")
    
    # Generate suggestions
    suggestions = generate_test_suggestions(all_functions, existing_tests, coverage)
    
    # AI enhancement
    if args.ai and suggestions:
        print("🤖 Enhancing with AI...")
        for func in all_functions[:5]:  # Limit AI calls
            if func.complexity > 2:
                try:
                    with open(func.file, 'r') as f:
                        source = f.read()
                    ai_tests = ai_generate_tests(func, source)
                    suggestions.extend(ai_tests)
                except:
                    pass
    
    # Output
    if args.json:
        output = [
            {
                'function': s.function,
                'test_name': s.test_name,
                'test_type': s.test_type,
                'description': s.description,
                'priority': s.priority,
                'reason': s.reason,
                'code': s.test_code
            }
            for s in suggestions
        ]
        print(json.dumps(output, indent=2))
    elif args.generate:
        generate_test_file(suggestions, args.generate)
    else:
        print_suggestions(suggestions, args.output)

if __name__ == '__main__':
    main()
