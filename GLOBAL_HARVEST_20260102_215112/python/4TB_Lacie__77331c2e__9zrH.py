#!/usr/bin/env python3
"""
VS Buddy Full Code Check
- Recursively checks all Python files in the current directory and subdirectories
- Runs syntax check, linting (flake8, pylint), and type checking (mypy)
- Reports results and errors
"""
import os
import sys
import subprocess
from pathlib import Path

# Ensure we're in the project root
BASE = Path.cwd()

# Helper to run a shell command and print output
def run_cmd(cmd, desc):
    print(f"\n🔎 {desc}:")
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.output)
        print(f"❌ {desc} failed.")

# Find all Python files recursively
def find_py_files():
    return [str(p) for p in BASE.rglob("*.py")]

# Main check routine
def main():
    py_files = find_py_files()
    if not py_files:
        print("No Python files found.")
        sys.exit(0)
    print(f"Found {len(py_files)} Python files.")

    # Syntax check
    for f in py_files:
        print(f"\n📝 Syntax check: {f}")
        try:
            subprocess.run([sys.executable, "-m", "py_compile", f], check=True)
            print("✅ Syntax OK")
        except subprocess.CalledProcessError:
            print("❌ Syntax error!")

    # Install/check flake8, pylint, mypy
    for pkg in ["flake8", "pylint", "mypy"]:
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", pkg], check=True)
        except subprocess.CalledProcessError:
            print(f"❌ Could not install {pkg}")

    # Run flake8
    run_cmd(f"flake8 {BASE}", "Flake8 linting")
    # Run pylint
    run_cmd(f"pylint {' '.join(py_files)}", "Pylint linting")
    # Run mypy
    run_cmd(f"mypy {BASE}", "Mypy type checking")

    print("\n✅ Full code check complete.")

if __name__ == "__main__":
    main()
