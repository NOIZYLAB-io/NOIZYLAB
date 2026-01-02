#!/usr/bin/env python3
"""
🗣️ Natural Language Git Interface
Part of GABRIEL AI Dev Toolkit

Execute git commands using plain English:
- "Undo my last 3 commits but keep changes"
- "Show me what Sarah changed last week"
- "Create a branch for the new auth feature"
- Explains commands before executing
"""

import argparse
import os
import sys
import json
import subprocess
import shlex
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class NaturalLanguageGit:
    """AI-powered natural language git interface."""
    
    SAFE_COMMANDS = [
        'status', 'log', 'diff', 'show', 'branch', 'tag',
        'remote', 'fetch', 'stash list', 'reflog', 'blame',
        'shortlog', 'describe', 'ls-files', 'ls-tree'
    ]
    
    DANGEROUS_COMMANDS = [
        'push --force', 'reset --hard', 'clean -fd',
        'branch -D', 'rebase', 'filter-branch'
    ]
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        self.history = []
        
    def _run_git(self, *args, capture: bool = True) -> str:
        """Run a git command."""
        try:
            result = subprocess.run(
                ['git', '-C', str(self.repo_path)] + list(args),
                capture_output=capture, text=True, timeout=60
            )
            return result.stdout.strip() if capture else ''
        except Exception as e:
            return f"Error: {e}"
    
    def get_repo_context(self) -> Dict[str, Any]:
        """Get current repository context."""
        return {
            'current_branch': self._run_git('branch', '--show-current'),
            'branches': self._run_git('branch', '-a').split('\n')[:20],
            'remotes': self._run_git('remote', '-v').split('\n'),
            'status': self._run_git('status', '--short'),
            'recent_commits': self._run_git('log', '--oneline', '-10').split('\n'),
            'tags': self._run_git('tag', '-l').split('\n')[:10],
            'stashes': self._run_git('stash', 'list').split('\n')[:5]
        }
    
    def translate_to_git(self, natural_language: str) -> Dict[str, Any]:
        """Translate natural language to git command."""
        context = self.get_repo_context()
        
        prompt = f"""Translate this natural language request into git command(s).

Request: "{natural_language}"

Repository Context:
- Current Branch: {context['current_branch']}
- Branches: {', '.join([b.strip() for b in context['branches'][:10]])}
- Status: {context['status'][:500] or 'Clean'}
- Recent Commits: {chr(10).join(context['recent_commits'][:5])}

Respond in JSON format:
{{
  "commands": [
    {{
      "git_command": "the full git command",
      "explanation": "what this command does",
      "is_safe": true/false,
      "is_destructive": true/false,
      "can_undo": true/false,
      "undo_command": "command to undo if applicable"
    }}
  ],
  "summary": "brief summary of what will happen",
  "warnings": ["any warnings about these commands"],
  "alternatives": ["alternative approaches if any"],
  "confidence": 0.0-1.0
}}

Rules:
1. Be precise - use exact branch names from context
2. Mark dangerous operations clearly
3. Prefer safe alternatives when possible
4. Include undo commands for destructive operations
5. If request is ambiguous, ask for clarification"""

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
                
            result = json.loads(json_str.strip())
            result['original_request'] = natural_language
            result['timestamp'] = datetime.now().isoformat()
            
            return result
            
        except Exception as e:
            return {
                'error': str(e),
                'original_request': natural_language
            }
    
    def execute_command(self, git_command: str, force: bool = False) -> Dict[str, Any]:
        """Execute a git command with safety checks."""
        # Check for dangerous commands
        cmd_lower = git_command.lower()
        
        is_dangerous = any(danger in cmd_lower for danger in self.DANGEROUS_COMMANDS)
        is_safe = any(safe in cmd_lower for safe in self.SAFE_COMMANDS)
        
        if is_dangerous and not force:
            return {
                'status': 'blocked',
                'reason': 'Dangerous command detected',
                'command': git_command,
                'suggestion': 'Use --force flag to execute dangerous commands'
            }
        
        # Parse and execute
        try:
            # Remove 'git ' prefix if present
            if git_command.startswith('git '):
                git_command = git_command[4:]
                
            args = shlex.split(git_command)
            output = self._run_git(*args)
            
            # Record in history
            self.history.append({
                'command': f'git {git_command}',
                'output': output[:1000],
                'timestamp': datetime.now().isoformat()
            })
            
            return {
                'status': 'success',
                'command': f'git {git_command}',
                'output': output
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'command': git_command,
                'error': str(e)
            }
    
    def interactive_mode(self):
        """Run interactive natural language git session."""
        print("🗣️ Natural Language Git Interface")
        print("=" * 50)
        print("Type git commands in plain English!")
        print("Examples:")
        print("  • 'show my recent commits'")
        print("  • 'undo last commit but keep changes'")
        print("  • 'what did I change today?'")
        print("  • 'create branch for login feature'")
        print("\nType 'exit' or 'quit' to leave, 'history' to see command history")
        print("=" * 50)
        print()
        
        while True:
            try:
                request = input("🗣️ > ").strip()
                
                if not request:
                    continue
                    
                if request.lower() in ['exit', 'quit', 'q']:
                    print("👋 Goodbye!")
                    break
                    
                if request.lower() == 'history':
                    for h in self.history[-10:]:
                        print(f"  $ {h['command']}")
                    continue
                    
                # Translate
                print("🤔 Thinking...")
                result = self.translate_to_git(request)
                
                if 'error' in result:
                    print(f"❌ Error: {result['error']}")
                    continue
                    
                # Show translation
                print(f"\n📋 {result.get('summary', 'Commands to execute:')}")
                print()
                
                for i, cmd in enumerate(result.get('commands', []), 1):
                    safe_icon = '✅' if cmd.get('is_safe') else '⚠️' if not cmd.get('is_destructive') else '🔴'
                    print(f"  {i}. {safe_icon} $ {cmd['git_command']}")
                    print(f"      └─ {cmd['explanation']}")
                    
                if result.get('warnings'):
                    print(f"\n⚠️ Warnings:")
                    for warn in result['warnings']:
                        print(f"   - {warn}")
                        
                # Ask for confirmation
                print()
                confirm = input("Execute? [y/N/1-9 to run specific] > ").strip().lower()
                
                if confirm == 'y':
                    # Execute all
                    for cmd in result.get('commands', []):
                        exec_result = self.execute_command(
                            cmd['git_command'],
                            force=cmd.get('is_destructive', False)
                        )
                        
                        if exec_result['status'] == 'success':
                            print(f"✅ {cmd['git_command']}")
                            if exec_result['output']:
                                print(exec_result['output'][:500])
                        else:
                            print(f"❌ {exec_result.get('error', exec_result.get('reason'))}")
                            
                elif confirm.isdigit():
                    # Execute specific command
                    idx = int(confirm) - 1
                    commands = result.get('commands', [])
                    if 0 <= idx < len(commands):
                        cmd = commands[idx]
                        exec_result = self.execute_command(cmd['git_command'])
                        
                        if exec_result['status'] == 'success':
                            print(f"✅ {cmd['git_command']}")
                            if exec_result['output']:
                                print(exec_result['output'])
                        else:
                            print(f"❌ {exec_result.get('error', exec_result.get('reason'))}")
                    else:
                        print("Invalid command number")
                else:
                    print("Cancelled")
                    
                print()
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    def single_command(self, request: str, execute: bool = False, force: bool = False) -> Dict[str, Any]:
        """Process a single natural language request."""
        result = self.translate_to_git(request)
        
        if execute and 'commands' in result:
            result['execution_results'] = []
            for cmd in result['commands']:
                exec_result = self.execute_command(cmd['git_command'], force)
                result['execution_results'].append(exec_result)
                
        return result


def main():
    parser = argparse.ArgumentParser(
        description='🗣️ Natural Language Git Interface',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "show my recent commits"
  %(prog)s "undo last commit" --execute
  %(prog)s --interactive
  %(prog)s "what changed today" --json
        """
    )
    
    parser.add_argument('request', nargs='?', help='Natural language git request')
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode')
    parser.add_argument('--execute', '-x', action='store_true', help='Execute commands')
    parser.add_argument('--force', '-f', action='store_true', help='Force dangerous commands')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    nlg = NaturalLanguageGit(args.path)
    
    if args.interactive or not args.request:
        nlg.interactive_mode()
    else:
        result = nlg.single_command(args.request, args.execute, args.force)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"❌ Error: {result['error']}")
            else:
                print(f"\n📋 {result.get('summary', 'Translation:')}")
                print(f"🎯 Confidence: {result.get('confidence', 0) * 100:.0f}%")
                print()
                
                for cmd in result.get('commands', []):
                    safe = '✅' if cmd.get('is_safe') else '⚠️'
                    print(f"  {safe} $ git {cmd['git_command']}")
                    print(f"      {cmd['explanation']}")
                    
                if result.get('warnings'):
                    print(f"\n⚠️ {', '.join(result['warnings'])}")
                    
                if args.execute and 'execution_results' in result:
                    print(f"\n📊 Execution Results:")
                    for er in result['execution_results']:
                        status = '✅' if er['status'] == 'success' else '❌'
                        print(f"  {status} {er.get('command', 'N/A')}")
                        if er.get('output'):
                            print(f"      {er['output'][:200]}")


if __name__ == '__main__':
    main()
