#!/usr/bin/env python3
"""
Code Fixer - Automatically fixes common Python code issues
==========================================================
"""

import re
import ast
from pathlib import Path
from rich.console import Console

console = Console()

class CodeFixer:
    def __init__(self, base_path):
        self.base = Path(base_path)
        self.fixed_files = []
        self.errors = []
    
    def fix_indentation(self, file_path):
        """Fix indentation errors"""
        try:
            content = file_path.read_text()
            lines = content.split('\n')
            fixed_lines = []
            
            for i, line in enumerate(lines):
                # Fix common indentation issues
                if line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                    # Check if it should be indented (previous line ends with :)
                    if i > 0 and lines[i-1].rstrip().endswith(':'):
                        fixed_lines.append('    ' + line)
                    else:
                        fixed_lines.append(line)
                else:
                    fixed_lines.append(line)
            
            # Try to compile to verify
            try:
                ast.parse('\n'.join(fixed_lines))
                file_path.write_text('\n'.join(fixed_lines))
                return True
            except:
                return False
        except Exception as e:
            self.errors.append(f"{file_path}: {e}")
            return False
    
    def fix_common_issues(self, file_path):
        """Fix common code issues"""
        try:
            content = file_path.read_text()
            original = content
            
            # Fix common issues
            # Remove trailing whitespace
            content = '\n'.join(line.rstrip() for line in content.split('\n'))
            
            # Ensure file ends with newline
            if content and not content.endswith('\n'):
                content += '\n'
            
            if content != original:
                file_path.write_text(content)
                return True
            return False
        except Exception as e:
            self.errors.append(f"{file_path}: {e}")
            return False
    
    def fix_all(self):
        """Fix all Python files"""
        console.print("[cyan]🔧 Fixing code issues...[/cyan]")
        
        python_files = list(self.base.rglob("*.py"))
        fixed = 0
        
        for py_file in python_files:
            if "__pycache__" in str(py_file) or "test" in str(py_file).lower():
                continue
            
            try:
                # Try to compile first
                compile(py_file.read_text(), str(py_file), 'exec')
            except SyntaxError as e:
                console.print(f"  🔧 Fixing {py_file.relative_to(self.base)}...")
                if self.fix_indentation(py_file) or self.fix_common_issues(py_file):
                    fixed += 1
                    self.fixed_files.append(str(py_file))
        
        console.print(f"  ✅ Fixed {fixed} files")
        return fixed

if __name__ == "__main__":
    fixer = CodeFixer("/Users/m2ultra/NOIZYLAB")
    fixer.fix_all()

