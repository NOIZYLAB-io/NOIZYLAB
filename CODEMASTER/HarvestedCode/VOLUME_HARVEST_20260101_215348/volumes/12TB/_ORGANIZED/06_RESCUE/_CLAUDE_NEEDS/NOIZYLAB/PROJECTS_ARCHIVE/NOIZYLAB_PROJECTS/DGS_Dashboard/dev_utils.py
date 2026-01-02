#!/usr/bin/env python3
"""
Development Utilities for AutoGo Token Automation
Speed up development with quick commands and utilities.
"""

import argparse
import os
import subprocess
import sys


def run_command(cmd: str, description: str = ""):
    """Run shell command with pretty output."""
    print(f"🔧 {description or cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ Success: {description}")
        if result.stdout:
            print(result.stdout)
    else:
        print(f"❌ Failed: {description}")
        if result.stderr:
            print(result.stderr)
    return result.returncode == 0


def quick_format():
    """Format code quickly."""
    commands = [
        ("python3 -m black token_automation.py", "Formatting with Black"),
        (
            "python3 -m autopep8 --in-place --aggressive token_automation.py",
            "Auto PEP8 fixes",
        ),
    ]

    for cmd, desc in commands:
        if not run_command(cmd, desc):
            return False
    return True


def quick_lint():
    """Run linting checks."""
    commands = [
        (
            "python3 -m flake8 token_automation.py --max-line-length=88",
            "Flake8 linting",
        ),
        ("python3 -m py_compile token_automation.py", "Syntax check"),
    ]

    for cmd, desc in commands:
        if not run_command(cmd, desc):
            return False
    return True


def quick_test():
    """Run quick tests."""
    print("🧪 Running quick tests...")

    # Test import
    try:
        import token_automation

        print("✅ Import test passed")
    except Exception as e:
        print(f"❌ Import test failed: {e}")
        return False

    # Test environment loading
    from dotenv import load_dotenv

    load_dotenv()

    if not os.getenv("TELEGRAM_BOT_TOKEN"):
        print("⚠️  Warning: TELEGRAM_BOT_TOKEN not set")
    else:
        print("✅ Environment variables loaded")

    return True


def quick_setup():
    """Quick project setup."""
    print("⚡ Quick setup...")

    commands = [
        ("pip install -r requirements.txt", "Installing dependencies"),
        ("pip install black autopep8 flake8", "Installing dev tools"),
    ]

    for cmd, desc in commands:
        run_command(cmd, desc)

    print("🎉 Setup complete!")


def quick_clean():
    """Clean up development files."""
    print("🧹 Cleaning up...")

    patterns = ["__pycache__", "*.pyc", "*.pyo", "*.log", ".pytest_cache"]

    for pattern in patterns:
        run_command(
            f"find . -name '{pattern}' -exec rm -rf {{}} +", f"Removing {pattern}"
        )

    print("✅ Cleanup complete!")


def quick_run():
    """Run the automation with timing."""
    import time

    print("🚀 Running automation...")
    start_time = time.time()

    success = run_command("python3 token_automation.py", "Token automation")

    end_time = time.time()
    duration = end_time - start_time

    print(f"⏱️  Execution time: {duration:.2f} seconds")
    return success


def main():
    parser = argparse.ArgumentParser(
        description="Development utilities for faster coding"
    )
    parser.add_argument(
        "command",
        choices=["format", "lint", "test", "setup", "clean", "run", "all"],
        help="Command to execute",
    )

    args = parser.parse_args()

    print(f"⚡ AutoGo Dev Utils - {args.command.upper()}")
    print("=" * 50)

    if args.command == "format":
        quick_format()
    elif args.command == "lint":
        quick_lint()
    elif args.command == "test":
        quick_test()
    elif args.command == "setup":
        quick_setup()
    elif args.command == "clean":
        quick_clean()
    elif args.command == "run":
        quick_run()
    elif args.command == "all":
        print("🔥 Running full pipeline...")
        steps = [
            ("Cleaning", quick_clean),
            ("Formatting", quick_format),
            ("Linting", quick_lint),
            ("Testing", quick_test),
            ("Running", quick_run),
        ]

        for step_name, step_func in steps:
            print(f"\n📋 Step: {step_name}")
            if not step_func():
                print(f"❌ Pipeline failed at: {step_name}")
                sys.exit(1)

        print("\n🎉 Full pipeline completed successfully!")


if __name__ == "__main__":
    main()
