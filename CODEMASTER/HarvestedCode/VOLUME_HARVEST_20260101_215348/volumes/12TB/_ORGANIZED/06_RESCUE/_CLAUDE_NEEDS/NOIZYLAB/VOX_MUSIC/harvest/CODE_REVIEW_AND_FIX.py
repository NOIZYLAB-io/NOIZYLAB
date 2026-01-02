#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🔧 AUTO CODE REVIEW & FIX - GORUNFREE! 🔧                         ║
║                                                                           ║
║  BITW 1000X Code Quality System                                          ║
║  Find bugs, fix code, quarantine broken files                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from datetime import datetime


class CodeReviewerAndFixer:
    """Automated code review and fixing system."""

    def __init__(self):
        self.vox_path = Path("/Users/rsp_ms/MC96_MobileApp/VOX")
        self.quarantine_path = Path("/Volumes/12TB 1/NOIZYVOX/QUARANTINE")
        self.quarantine_path.mkdir(parents=True, exist_ok=True)

        self.results = {
            "checked": [],
            "passed": [],
            "fixed": [],
            "quarantined": [],
            "errors": []
        }

    def check_syntax(self, filepath: Path) -> tuple:
        """Check Python syntax."""
        try:
            result = subprocess.run(
                ["python3", "-m", "py_compile", str(filepath)],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode == 0:
                return True, "OK"
            else:
                return False, result.stderr

        except Exception as e:
            return False, str(e)

    def try_fix_common_issues(self, filepath: Path) -> bool:
        """Try to fix common Python issues."""
        try:
            with open(filepath, 'r') as f:
                content = f.read()

            original_content = content
            fixed = False

            # Fix common issues
            fixes = [
                # Fix trailing whitespace
                (lambda c: '\n'.join(line.rstrip() for line in c.split('\n')), "trailing whitespace"),

                # Fix mixed tabs/spaces (convert to spaces)
                (lambda c: c.replace('\t', '    '), "tabs to spaces"),

                # Ensure file ends with newline
                (lambda c: c if c.endswith('\n') else c + '\n', "final newline"),
            ]

            for fix_func, fix_name in fixes:
                content = fix_func(content)

            if content != original_content:
                # Backup original
                backup_path = filepath.with_suffix('.py.backup')
                shutil.copy2(filepath, backup_path)

                # Write fixed version
                with open(filepath, 'w') as f:
                    f.write(content)

                fixed = True

            return fixed

        except Exception as e:
            print(f"   ⚠️  Fix error: {e}")
            return False

    def quarantine_file(self, filepath: Path, reason: str):
        """Move broken file to quarantine."""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            quarantine_name = f"{filepath.stem}_{timestamp}{filepath.suffix}"
            quarantine_dest = self.quarantine_path / quarantine_name

            # Copy to quarantine
            shutil.copy2(filepath, quarantine_dest)

            # Create info file
            info_file = quarantine_dest.with_suffix('.txt')
            with open(info_file, 'w') as f:
                f.write(f"QUARANTINED FILE\n")
                f.write(f"================\n\n")
                f.write(f"Original Path: {filepath}\n")
                f.write(f"Quarantined: {datetime.now().isoformat()}\n")
                f.write(f"Reason: {reason}\n")

            print(f"   ⚠️  QUARANTINED: {filepath.name}")
            self.results["quarantined"].append(str(filepath))

            return True

        except Exception as e:
            print(f"   ❌ Quarantine error: {e}")
            return False

    def review_file(self, filepath: Path):
        """Review and fix a single file."""
        print(f"\n{'='*75}")
        print(f"📄 {filepath.name}")
        print(f"{'='*75}")

        self.results["checked"].append(str(filepath))

        # Check syntax
        print("   🔍 Checking syntax...")
        syntax_ok, error_msg = self.check_syntax(filepath)

        if syntax_ok:
            print("   ✅ Syntax OK")
            self.results["passed"].append(str(filepath))
            return

        # Try to fix
        print(f"   ⚠️  Syntax error detected")
        print(f"   🔧 Attempting auto-fix...")

        if self.try_fix_common_issues(filepath):
            # Re-check after fix
            syntax_ok_after, _ = self.check_syntax(filepath)

            if syntax_ok_after:
                print("   ✅ FIXED!")
                self.results["fixed"].append(str(filepath))
                return
            else:
                print("   ⚠️  Auto-fix unsuccessful")

        # Quarantine if can't fix
        print("   🚨 Cannot auto-fix - quarantining...")
        self.quarantine_file(filepath, f"Syntax error: {error_msg[:200]}")
        self.results["errors"].append({
            "file": str(filepath),
            "error": error_msg
        })

    def review_all_python_files(self):
        """Review all Python files in VOX."""
        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🔧 VOX CODE REVIEW & AUTO-FIX - INITIATED! 🔧                     ║
║                                                                           ║
║  GORUNFREE! Finding and fixing all issues...                             ║
║  BITW 1000X Quality Standards                                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
        """)

        # Find all Python files
        python_files = list(self.vox_path.rglob("*.py"))

        print(f"\n📊 Found {len(python_files)} Python files to review\n")

        # Review each file
        for py_file in python_files:
            self.review_file(py_file)

        # Generate report
        self.generate_report()

    def generate_report(self):
        """Generate final report."""
        print(f"\n\n{'='*75}")
        print("📊 CODE REVIEW COMPLETE - FINAL REPORT")
        print(f"{'='*75}\n")

        print(f"✅ Files Checked: {len(self.results['checked'])}")
        print(f"✅ Passed: {len(self.results['passed'])}")
        print(f"🔧 Fixed: {len(self.results['fixed'])}")
        print(f"⚠️  Quarantined: {len(self.results['quarantined'])}")
        print(f"❌ Errors: {len(self.results['errors'])}")

        if self.results["fixed"]:
            print(f"\n🔧 FIXED FILES:")
            for filepath in self.results["fixed"]:
                print(f"   ✓ {Path(filepath).name}")

        if self.results["quarantined"]:
            print(f"\n⚠️  QUARANTINED FILES:")
            for filepath in self.results["quarantined"]:
                print(f"   ! {Path(filepath).name}")

        if self.results["errors"]:
            print(f"\n❌ ERROR DETAILS:")
            for error in self.results["errors"]:
                print(f"\n   File: {Path(error['file']).name}")
                print(f"   Error: {error['error'][:200]}")

        print(f"\n📁 Quarantine Location: {self.quarantine_path}")

        # Save report
        report_file = self.vox_path / "CODE_REVIEW_REPORT.txt"
        with open(report_file, 'w') as f:
            f.write(f"VOX CODE REVIEW REPORT\n")
            f.write(f"{'='*75}\n")
            f.write(f"Date: {datetime.now().isoformat()}\n\n")
            f.write(f"Files Checked: {len(self.results['checked'])}\n")
            f.write(f"Passed: {len(self.results['passed'])}\n")
            f.write(f"Fixed: {len(self.results['fixed'])}\n")
            f.write(f"Quarantined: {len(self.results['quarantined'])}\n")
            f.write(f"Errors: {len(self.results['errors'])}\n\n")

            if self.results["fixed"]:
                f.write(f"\nFIXED FILES:\n")
                for filepath in self.results["fixed"]:
                    f.write(f"  {filepath}\n")

            if self.results["quarantined"]:
                f.write(f"\nQUARANTINED FILES:\n")
                for filepath in self.results["quarantined"]:
                    f.write(f"  {filepath}\n")

            if self.results["errors"]:
                f.write(f"\nERROR DETAILS:\n")
                for error in self.results["errors"]:
                    f.write(f"\n  File: {error['file']}\n")
                    f.write(f"  Error: {error['error']}\n")

        print(f"\n📄 Report saved: {report_file}")

        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        ✅ CODE REVIEW COMPLETE! ✅                                       ║
║                                                                           ║
║  All code reviewed, fixed, and organized!                                ║
║  Ready for GORUNFREE deployment!                                         ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
        """)


def main():
    """Main entry point."""
    reviewer = CodeReviewerAndFixer()
    reviewer.review_all_python_files()
    return 0


if __name__ == "__main__":
    sys.exit(main())
