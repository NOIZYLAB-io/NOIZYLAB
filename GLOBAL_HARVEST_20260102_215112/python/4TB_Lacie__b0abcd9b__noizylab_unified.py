#!/usr/bin/env python3
"""
🌟 NOIZYLAB - Unified Command Router
Routes commands to TypeScript CLI or Python CLI automatically!
"""

import sys
import subprocess

# TypeScript commands
TS_COMMANDS = ["setup", "dns", "email", "users", "alerts", "remote", 
               "subs", "archive", "reports", "webhooks"]

# Python commands  
PY_COMMANDS = ["status", "health", "ai", "network", "slack", 
               "jumbo", "universe", "doctor"]

def main():
    if len(sys.argv) < 2:
        print("Usage: noizylab <command> [args]")
        print("\nTypeScript Commands:", ", ".join(TS_COMMANDS))
        print("Python Commands:", ", ".join(PY_COMMANDS))
        return
    
    command = sys.argv[1]
    args = sys.argv[2:]
    
    if command in TS_COMMANDS:
        # Route to TypeScript
        subprocess.run(["npx", "tsx", "noizylab-cli/src/index.ts", command] + args)
    
    elif command in PY_COMMANDS:
        # Route to Python
        subprocess.run(["python3", "noizylab_cli.py", command] + args)
    
    else:
        print(f"Unknown command: {command}")
        print("Try: noizylab setup (TypeScript) or noizylab status (Python)")

if __name__ == "__main__":
    main()
