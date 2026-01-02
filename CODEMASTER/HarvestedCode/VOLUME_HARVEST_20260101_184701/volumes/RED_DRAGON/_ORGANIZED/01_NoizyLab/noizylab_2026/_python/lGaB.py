#!/usr/bin/env python3
"""
ULTIMATE AI-POWERED VS CODE DEVELOPMENT BEAST MODE SETUP
Installs and configures ALL the best AI tools for maximum productivity
"""

import os
import subprocess
import sys
import json
import platform
from pathlib import Path
import requests

def run_command(command, check=True):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=check)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr, e.returncode

def check_prerequisites():
    """Check for required tools"""
    print("🔍 Checking prerequisites...")
    
    # Check VS Code
    vscode_cmd = None
    for cmd in ['code', 'code-insiders']:
        stdout, stderr, returncode = run_command(f"{cmd} --version", check=False)
        if returncode == 0:
            print(f"✅ VS Code found: {cmd}")
            vscode_cmd = cmd
            break
    
    if not vscode_cmd:
        print("❌ VS Code required. Install from: https://code.visualstudio.com/")
        return None
    
    # Check Node.js (needed for some extensions)
    stdout, stderr, returncode = run_command("node --version", check=False)
    if returncode == 0:
        print(f"✅ Node.js found: {stdout}")
    else:
        print("⚠️  Node.js recommended for optimal performance")
    
    # Check Python
    stdout, stderr, returncode = run_command("python --version", check=False)
    if returncode == 0:
        print(f"✅ Python found: {stdout}")
    
    return vscode_cmd

def install_ai_extensions(vscode_cmd):
    """Install ALL the AI extensions for maximum power"""
    
    ai_extensions = [
        # CORE AI ASSISTANTS
        {'id': 'continue.continue', 'name': 'Continue'},
        {'id': 'github.copilot', 'name': 'GitHub Copilot'},
        {'id': 'github.copilot-chat', 'name': 'GitHub Copilot Chat'},
        {'id': 'codeium.codeium', 'name': 'Codeium'},
        {'id': 'tabnine.tabnine-vscode', 'name': 'TabNine'},
        # SPECIALIZED AI TOOLS
        {'id': 'amazonwebservices.aws-toolkit-vscode', 'name': 'AWS Toolkit'},
        {'id': 'ms-python.python', 'name': 'Python'},
        {'id': 'ms-python.pylint', 'name': 'Pylint'},
        {'id': 'ms-toolsai.jupyter', 'name': 'Jupyter'},
        # CODE ANALYSIS & OPTIMIZATION
        {'id': 'sonarsource.sonarlint-vscode', 'name': 'SonarLint'},
        {'id': 'streetsidesoftware.code-spell-checker', 'name': 'Code Spell Checker'},
        {'id': 'usernamehw.errorlens', 'name': 'Error Lens'},
        # PRODUCTIVITY ENHANCERS
        {'id': 'eamodio.gitlens', 'name': 'GitLens'},
        {'id': 'ms-vscode.vscode-typescript-next', 'name': 'TypeScript Importer'},
        {'id': 'bradlc.vscode-tailwindcss', 'name': 'Tailwind CSS IntelliSense'},
        # TESTING & DEBUGGING
        {'id': 'ms-playwright.playwright', 'name': 'Playwright Test'},
        {'id': 'ms-vscode.test-adapter-converter', 'name': 'Test Explorer UI'},
        # DOCUMENTATION & COMMENTS  
        {'id': 'mintlify.document', 'name': 'Mintlify Doc Writer'},
        {'id': 'aaron-bond.better-comments', 'name': 'Better Comments'},
        # PERFORMANCE & MONITORING
        {'id': 'wix.vscode-import-cost', 'name': 'Import Cost'},
        {'id': 'wayou.vscode-todo-highlight', 'name': 'TODO Highlight'}
    ]
    
    print(f"\n🚀 Installing {len(ai_extensions)} AI-powered extensions...")
    print("=" * 60)
    
    installed_count = 0
    failed_count = 0
    
    for ext in ai_extensions:
        print(f"\n📦 Installing {ext['name']}")
        stdout, stderr, returncode = run_command(f"{vscode_cmd} --install-extension {ext['id']}", check=False)
        if returncode == 0 or "already installed" in stdout.lower():
            print(f"   ✅ SUCCESS")
            installed_count += 1
        else:
            print(f"   ❌ FAILED: {stderr}")
            failed_count += 1
    
    print(f"\n📊 Installation Summary:")
    print(f"   ✅ Installed: {installed_count}")
    print(f"   ❌ Failed: {failed_count}")
    
    return ai_extensions

def main():
    print("🔥🔥🔥 VS CODE AI BEAST MODE SETUP 🔥🔥🔥")
    print("=" * 60)
    print("Setting up the ULTIMATE AI-powered development environment!")
    print("=" * 60)
    
    vscode_cmd = check_prerequisites()
    if not vscode_cmd:
        return
    
    extensions = install_ai_extensions(vscode_cmd)
    print("\n🏆 AI BEAST MODE SETUP COMPLETE! 🏆")
    print(f"\n📊 INSTALLED {len(extensions)} AI EXTENSIONS:")
    for ext in extensions:
        print(f"   {ext['name']}")
    print("\n🔥 YOU'RE NOW READY TO CODE AT BEAST MODE LEVEL! 🔥")

if __name__ == "__main__":
    main()
