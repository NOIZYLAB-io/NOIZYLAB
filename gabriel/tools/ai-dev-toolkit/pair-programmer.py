#!/usr/bin/env python3
"""
👥 AI Pair Programmer
Part of GABRIEL AI Dev Toolkit

Your AI coding partner:
- Real-time coding assistance
- Architecture discussions
- Problem-solving sessions
- Code review dialogue
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
import readline  # For better input handling

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class PairProgrammer:
    """AI-powered pair programming assistant."""
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        self.conversation_history = []
        self.context = {}
        self.session_start = datetime.now()
        
    def _load_file_context(self, file_paths: List[str]) -> Dict[str, str]:
        """Load files into context."""
        context = {}
        for path in file_paths:
            full_path = self.repo_path / path
            if full_path.exists():
                try:
                    content = full_path.read_text(encoding='utf-8', errors='ignore')
                    context[path] = content[:10000]  # Limit size
                except Exception as e:
                    context[path] = f"Error reading: {e}"
        return context
    
    def _get_git_context(self) -> Dict[str, Any]:
        """Get current git context."""
        context = {}
        
        try:
            # Current branch
            result = subprocess.run(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                capture_output=True, text=True, cwd=self.repo_path
            )
            if result.returncode == 0:
                context['branch'] = result.stdout.strip()
                
            # Recent commits
            result = subprocess.run(
                ['git', 'log', '--oneline', '-5'],
                capture_output=True, text=True, cwd=self.repo_path
            )
            if result.returncode == 0:
                context['recent_commits'] = result.stdout.strip()
                
            # Current status
            result = subprocess.run(
                ['git', 'status', '--short'],
                capture_output=True, text=True, cwd=self.repo_path
            )
            if result.returncode == 0:
                context['status'] = result.stdout.strip()
                
        except Exception:
            pass
            
        return context
    
    def _build_system_prompt(self) -> str:
        """Build the system prompt with context."""
        prompt = """You are an expert pair programmer working alongside a developer. Your role is to:

1. **Collaborate**: Think through problems together, offer suggestions, ask clarifying questions
2. **Teach**: Explain concepts clearly, share best practices, help them learn
3. **Review**: Catch potential bugs, suggest improvements, ensure code quality
4. **Architect**: Help design solutions, discuss trade-offs, plan implementations
5. **Debug**: Help diagnose issues, suggest debugging strategies, trace logic

Communication Style:
- Be conversational and friendly, like a real pair programming partner
- Ask questions when the problem isn't clear
- Think out loud - share your reasoning
- Offer alternatives when relevant
- Be concise but thorough
- Use code examples when helpful
- Reference specific files/functions when discussing code

Session Context:
"""
        
        if self.context.get('git'):
            git = self.context['git']
            prompt += f"\n📌 Git Branch: {git.get('branch', 'unknown')}"
            if git.get('status'):
                prompt += f"\n📝 Working Changes:\n{git['status']}"
                
        if self.context.get('files'):
            prompt += "\n\n📁 Files in Context:"
            for path, content in self.context['files'].items():
                prompt += f"\n\n--- {path} ---\n{content[:3000]}..."
                
        prompt += "\n\nBe helpful, collaborative, and focus on the developer's goals!"
        
        return prompt
    
    def add_files(self, file_paths: List[str]):
        """Add files to the context."""
        self.context['files'] = self._load_file_context(file_paths)
        print(f"📁 Added {len(self.context['files'])} file(s) to context")
    
    def refresh_git_context(self):
        """Refresh git context."""
        self.context['git'] = self._get_git_context()
        
    def chat(self, message: str) -> str:
        """Send a message and get a response."""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": message
        })
        
        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                system=self._build_system_prompt(),
                messages=self.conversation_history
            )
            
            assistant_message = response.content[0].text
            
            # Add response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            error_msg = f"Error: {e}"
            return error_msg
    
    def handle_command(self, command: str) -> Optional[str]:
        """Handle special commands."""
        parts = command.strip().split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        if cmd in ['/help', '/h']:
            return """
📚 Pair Programmer Commands:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
/file <path>     Add file(s) to context
/clear           Clear conversation history
/context         Show current context
/git             Refresh git context
/save            Save session transcript
/reset           Reset session completely
/help            Show this help

Just type normally to chat with your AI pair!
"""
        
        elif cmd == '/file':
            if args:
                files = args.split()
                self.add_files(files)
                return f"✅ Added files to context: {', '.join(files)}"
            return "❌ Usage: /file <path> [path2...]"
            
        elif cmd == '/clear':
            self.conversation_history = []
            return "🧹 Conversation history cleared"
            
        elif cmd == '/context':
            ctx_info = []
            ctx_info.append("📋 Current Context:")
            
            if self.context.get('git'):
                ctx_info.append(f"  🔀 Branch: {self.context['git'].get('branch')}")
                
            if self.context.get('files'):
                ctx_info.append(f"  📁 Files: {len(self.context['files'])}")
                for f in self.context['files'].keys():
                    ctx_info.append(f"     • {f}")
                    
            ctx_info.append(f"  💬 Messages: {len(self.conversation_history)}")
            return '\n'.join(ctx_info)
            
        elif cmd == '/git':
            self.refresh_git_context()
            return "🔄 Git context refreshed"
            
        elif cmd == '/save':
            return self.save_session()
            
        elif cmd == '/reset':
            self.conversation_history = []
            self.context = {}
            return "🔄 Session reset completely"
            
        return None
    
    def save_session(self) -> str:
        """Save session transcript."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = self.repo_path / f'.pair_session_{timestamp}.md'
        
        content = []
        content.append("# Pair Programming Session")
        content.append(f"\n📅 {self.session_start.strftime('%Y-%m-%d %H:%M')}")
        content.append(f"\n## Context")
        
        if self.context.get('git'):
            content.append(f"\n- Branch: `{self.context['git'].get('branch')}`")
            
        if self.context.get('files'):
            content.append("\n- Files:")
            for f in self.context['files'].keys():
                content.append(f"  - `{f}`")
                
        content.append("\n## Conversation\n")
        
        for msg in self.conversation_history:
            role = "👤 You" if msg['role'] == 'user' else "🤖 AI"
            content.append(f"### {role}\n")
            content.append(msg['content'])
            content.append("\n---\n")
            
        filename.write_text('\n'.join(content))
        return f"💾 Session saved to: {filename}"
    
    def quick_review(self, file_path: str) -> str:
        """Quick review a file."""
        self.add_files([file_path])
        return self.chat(f"Please review {file_path} and give me feedback on code quality, potential bugs, and suggestions for improvement.")
    
    def explain(self, file_path: str, concept: str = None) -> str:
        """Explain code or concept."""
        self.add_files([file_path])
        
        if concept:
            return self.chat(f"Looking at {file_path}, please explain {concept}")
        return self.chat(f"Please explain what {file_path} does and how it works.")
    
    def debug_help(self, file_path: str, error: str) -> str:
        """Get help debugging an error."""
        self.add_files([file_path])
        return self.chat(f"I'm getting this error in {file_path}:\n\n{error}\n\nCan you help me debug this?")
    
    def implement(self, file_path: str, feature: str) -> str:
        """Get help implementing a feature."""
        self.add_files([file_path])
        return self.chat(f"I want to implement this feature in {file_path}:\n\n{feature}\n\nHow should I approach this?")
    
    def run_interactive(self):
        """Run interactive pair programming session."""
        print("=" * 60)
        print("👥 AI PAIR PROGRAMMER")
        print("=" * 60)
        print("Your AI coding partner is ready!")
        print("Type /help for commands, or just start chatting.")
        print("Press Ctrl+C or type 'exit' to end session.")
        print("=" * 60)
        print()
        
        # Initialize git context
        self.refresh_git_context()
        
        if self.context.get('git', {}).get('branch'):
            print(f"📌 Working on branch: {self.context['git']['branch']}")
            print()
            
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['exit', 'quit', '/quit', '/exit']:
                    print("\n👋 Ending pair programming session. Happy coding!")
                    break
                    
                # Check for commands
                if user_input.startswith('/'):
                    result = self.handle_command(user_input)
                    if result:
                        print(f"\n{result}")
                        continue
                        
                # Regular chat
                print("\n🤖 AI: ", end="", flush=True)
                response = self.chat(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\n👋 Session ended. Happy coding!")
                break
            except EOFError:
                break


def main():
    parser = argparse.ArgumentParser(
        description='👥 AI Pair Programmer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              Start interactive session
  %(prog)s --review src/api.py          Quick code review
  %(prog)s --explain src/utils.py       Explain code
  %(prog)s --debug src/app.py -e "Error"  Debug help
  %(prog)s --implement src/api.py -f "Add caching"
        """
    )
    
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--file', '-f', action='append', help='Files to load')
    parser.add_argument('--review', help='Quick review a file')
    parser.add_argument('--explain', help='Explain a file')
    parser.add_argument('--concept', '-c', help='Concept to explain (with --explain)')
    parser.add_argument('--debug', help='Get debug help for a file')
    parser.add_argument('--error', '-e', help='Error message (with --debug)')
    parser.add_argument('--implement', help='File for implementation help')
    parser.add_argument('--feature', help='Feature to implement (with --implement)')
    parser.add_argument('--ask', '-a', help='One-off question (non-interactive)')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    pair = PairProgrammer(args.path)
    
    # Load initial files if specified
    if args.file:
        pair.add_files(args.file)
        
    # Handle quick actions
    if args.review:
        print(pair.quick_review(args.review))
        
    elif args.explain:
        print(pair.explain(args.explain, args.concept))
        
    elif args.debug:
        error = args.error or "Unknown error"
        print(pair.debug_help(args.debug, error))
        
    elif args.implement:
        feature = args.feature or "the feature"
        print(pair.implement(args.implement, feature))
        
    elif args.ask:
        print(pair.chat(args.ask))
        
    else:
        # Interactive mode
        pair.run_interactive()


if __name__ == '__main__':
    main()
