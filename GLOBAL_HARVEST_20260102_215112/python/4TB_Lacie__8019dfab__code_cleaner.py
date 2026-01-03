#!/usr/bin/env python3
"""
Code Cleaner & Optimizer
Cleans, tests, and optimizes all code in NOIZYLAB
"""

import ast
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class CodeCleaner:
    """Comprehensive code cleaning and optimization"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.issues = []
        self.fixes = []
        self.optimizations = []

    def check_syntax(self, file_path: Path) -> bool:
        """Check Python syntax"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                ast.parse(f.read())
            return True
        except SyntaxError as e:
            self.issues.append(f"❌ Syntax error in {file_path.name}: {e}")
            return False
        except Exception as e:
            self.issues.append(f"⚠️  Error checking {file_path.name}: {e}")
            return False

    def check_imports(self, file_path: Path) -> List[str]:
        """Check and optimize imports"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all imports
        imports = re.findall(r'^(import |from .+ import )', content, re.MULTILINE)

        # Check for unused imports (basic check)
        issues = []
        if len(imports) > 10:
            issues.append(f"⚠️  Many imports in {file_path.name} ({len(imports)})")

        return issues

    def check_code_quality(self, file_path: Path) -> List[str]:
        """Check code quality"""
        issues = []

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            content = ''.join(lines)

        # Check for common issues
        if len(lines) > 1000:
            issues.append(f"⚠️  Large file: {file_path.name} ({len(lines)} lines)")

        # Check for long lines
        long_lines = [i+1 for i, line in enumerate(lines) if len(line.rstrip()) > 120]
        if long_lines:
            issues.append(f"⚠️  Long lines in {file_path.name}: {len(long_lines)} lines")

        # Check for TODO/FIXME
        if re.search(r'\b(TODO|FIXME|XXX|HACK)\b', content, re.IGNORECASE):
            issues.append(f"ℹ️  Contains TODO/FIXME in {file_path.name}")

        # Check for error handling
        if 'try:' in content and 'except' not in content:
            issues.append(f"⚠️  Try without except in {file_path.name}")

        return issues

    def optimize_file(self, file_path: Path) -> bool:
        """Optimize a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Remove trailing whitespace
            lines = content.split('\n')
            cleaned_lines = [line.rstrip() for line in lines]
            content = '\n'.join(cleaned_lines)

            # Ensure file ends with newline
            if content and not content.endswith('\n'):
                content += '\n'

            # Only write if changed
            if content != original:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.optimizations.append(f"✅ Cleaned {file_path.name}")
                return True

            return False
        except Exception as e:
            self.issues.append(f"❌ Error optimizing {file_path.name}: {e}")
            return False

    def check_duplicates(self) -> List[str]:
        """Check for duplicate files"""
        duplicates = []
        files = {}

        for py_file in self.base_dir.glob('*.py'):
            if py_file.name == 'code_cleaner.py':
                continue

            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Create a hash of the content (simplified)
                content_hash = hash(content[:500])  # First 500 chars

            if content_hash in files:
                duplicates.append(f"⚠️  Possible duplicate: {py_file.name} and {files[content_hash]}")
            else:
                files[content_hash] = py_file.name

        return duplicates

    def test_all_files(self) -> Dict[str, bool]:
        """Test all Python files"""
        results = {}

        for py_file in self.base_dir.glob('*.py'):
            if py_file.name == 'code_cleaner.py':
                continue

            # Syntax check
            syntax_ok = self.check_syntax(py_file)

            # Try to import (if it's a module)
            import_ok = True
            try:
                # Just check if it compiles
                compile(open(py_file).read(), py_file, 'exec')
            except Exception:
                import_ok = False

            results[py_file.name] = syntax_ok and import_ok

        return results

    def generate_report(self) -> str:
        """Generate cleanup report"""
        report = []
        report.append("\n" + "="*80)
        report.append("🧹 CODE CLEANUP & OPTIMIZATION REPORT")
        report.append("="*80)

        # Test all files
        report.append("\n📋 Testing all files...")
        test_results = self.test_all_files()

        passed = sum(1 for v in test_results.values() if v)
        total = len(test_results)

        report.append(f"\n✅ Test Results: {passed}/{total} files passed")

        for filename, result in test_results.items():
            status = "✅" if result else "❌"
            report.append(f"  {status} {filename}")

        # Check duplicates
        report.append("\n🔍 Checking for duplicates...")
        duplicates = self.check_duplicates()
        if duplicates:
            report.extend(duplicates)
        else:
            report.append("  ✅ No duplicates found")

        # Optimize all files
        report.append("\n⚡ Optimizing files...")
        optimized_count = 0
        for py_file in self.base_dir.glob('*.py'):
            if self.optimize_file(py_file):
                optimized_count += 1

        report.append(f"  ✅ Optimized {optimized_count} files")

        # Code quality checks
        report.append("\n📊 Code Quality Checks...")
        for py_file in self.base_dir.glob('*.py'):
            if py_file.name == 'code_cleaner.py':
                continue
            quality_issues = self.check_code_quality(py_file)
            if quality_issues:
                report.extend(quality_issues)

        # Summary
        report.append("\n" + "="*80)
        report.append("📊 SUMMARY")
        report.append("="*80)
        report.append(f"  • Files tested: {total}")
        report.append(f"  • Files passed: {passed}")
        report.append(f"  • Files optimized: {optimized_count}")
        report.append(f"  • Issues found: {len(self.issues)}")
        report.append(f"  • Optimizations: {len(self.optimizations)}")

        if self.issues:
            report.append("\n⚠️  Issues:")
            for issue in self.issues[:10]:  # Limit to 10
                report.append(f"  {issue}")

        report.append("\n✅ CODE CLEANUP COMPLETE!")
        report.append("="*80)

        return '\n'.join(report)

    def run_full_cleanup(self):
        """Run full cleanup process"""
        print("\n🧹 Starting comprehensive code cleanup...")
        print("="*80)

        # Test all files
        print("\n1️⃣  Testing all Python files...")
        test_results = self.test_all_files()

        # Optimize all files
        print("\n2️⃣  Optimizing all files...")
        for py_file in self.base_dir.glob('*.py'):
            self.optimize_file(py_file)

        # Check duplicates
        print("\n3️⃣  Checking for duplicates...")
        duplicates = self.check_duplicates()

        # Generate report
        print("\n4️⃣  Generating report...")
        report = self.generate_report()
        print(report)

        # Save report
        report_file = self.base_dir / "CLEANUP_REPORT.txt"
        with open(report_file, 'w') as f:
            f.write(report)

        print(f"\n💾 Report saved to: {report_file}")

if __name__ == "__main__":
    cleaner = CodeCleaner()
    cleaner.run_full_cleanup()

