#!/usr/bin/env python3
"""
🤖 AI SMART ASSISTANT CLAW 🤖
Your intelligent coding companion powered by OpenAI

This is your go-to AI assistant for coding questions, explanations,
best practices, and general development guidance.
"""

import argparse
import asyncio
import sys
from pathlib import Path
from typing import List, Optional

# Add core to path for imports
sys.path.append(str(Path(__file__).parent.parent / "core"))

try:
    import json
    from datetime import datetime

    from ai_engine import get_ai_engine
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.panel import Panel
    from rich.prompt import Confirm, Prompt
    from rich.table import Table
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

console = Console()


class ConversationHistory:
    """Manage conversation history for context"""

    def __init__(self):
        self.history: List[dict] = []
        self.max_history = 10

    def add_message(self, role: str, content: str):
        """Add message to history"""
        self.history.append(
            {"role": role, "content": content, "timestamp": datetime.now().isoformat()}
        )

        # Keep only recent messages
        if len(self.history) > self.max_history * 2:  # user + assistant pairs
            self.history = self.history[-self.max_history * 2 :]

    def get_context(self) -> List[dict]:
        """Get conversation context for AI"""
        return [
            {"role": msg["role"], "content": msg["content"]}
            for msg in self.history[-6:]
        ]  # Last 3 exchanges


async def ask_coding_question(
    question: str, context: Optional[str] = None, language: str = "python"
) -> str:
    """
    🤔 Ask a coding question to AI
    """
    try:
        ai = get_ai_engine()
        if not ai.api_key:
            console.print("[red]❌ OpenAI API key not configured![/red]")
            return ""

        # Build the prompt
        system_prompt = f"""You are CodeBeast AI, a super helpful coding assistant.
        You are:
        - STRONG: Can handle complex technical questions
        - SMART: Provide intelligent, accurate answers with examples  
        - HELPFUL: Always ready to explain concepts clearly
        
        Focus on {language} development unless specified otherwise.
        Always provide practical examples and best practices.
        """

        user_prompt = question
        if context:
            user_prompt = f"Context: {context}\n\nQuestion: {question}"

        console.print(f"[blue]🤖 Processing your {language} question...[/blue]")

        # Get AI response
        response = await asyncio.to_thread(
            ai.client.chat.completions.create,
            model=ai.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=ai.max_tokens,
            temperature=0.7,
        )

        answer = response.choices[0].message.content or ""

        # Display the answer
        console.print(
            Panel(
                Markdown(answer),
                title="🤖 CodeBeast AI Assistant",
                border_style="green",
            )
        )

        return answer

    except Exception as e:
        console.print(f"[red]💥 Error getting AI response: {e}[/red]")
        return ""


async def explain_concept(concept: str, level: str = "intermediate"):
    """
    📖 Explain a programming concept
    """
    levels = {
        "beginner": "Explain this for someone new to programming",
        "intermediate": "Explain this for someone with some programming experience",
        "advanced": "Provide a detailed technical explanation",
    }

    question = f"{levels[level]}: {concept}"
    await ask_coding_question(question)


async def code_review_assistant(code: str, language: str = "python"):
    """
    👀 Get AI code review
    """
    question = f"""Please review this {language} code and provide feedback:

```{language}
{code}
```

Focus on:
1. Code quality and style
2. Performance optimization
3. Security considerations  
4. Best practices
5. Potential bugs
"""

    await ask_coding_question(question, language=language)


async def get_best_practices(topic: str, language: str = "python"):
    """
    ⭐ Get best practices for a topic
    """
    question = f"What are the best practices for {topic} in {language}? Include examples and explain why these practices are important."
    await ask_coding_question(question, language=language)


async def interactive_assistant():
    """
    💬 Interactive AI assistant chat
    """
    console.print("[cyan]🤖 Interactive CodeBeast AI Assistant[/cyan]")
    console.print("Type 'exit' to quit, 'help' for commands\n")

    conversation = ConversationHistory()
    current_language = "python"

    while True:
        try:
            # Get user input
            user_input = Prompt.ask(
                f"[bold blue]{current_language}>[/bold blue]", default=""
            )

            if not user_input:
                continue

            # Handle special commands
            if user_input.lower() == "exit":
                console.print("👋 [green]Happy coding![/green]")
                break

            elif user_input.lower() == "help":
                show_help()
                continue

            elif user_input.startswith("/language"):
                parts = user_input.split()
                if len(parts) > 1:
                    current_language = parts[1]
                    console.print(
                        f"[green]🔧 Language set to: {current_language}[/green]"
                    )
                else:
                    console.print(
                        f"[yellow]Current language: {current_language}[/yellow]"
                    )
                continue

            elif user_input.startswith("/explain"):
                concept = user_input.replace("/explain", "").strip()
                if concept:
                    await explain_concept(concept)
                continue

            elif user_input.startswith("/best"):
                topic = user_input.replace("/best", "").strip()
                if topic:
                    await get_best_practices(topic, current_language)
                continue

            elif user_input.startswith("/review"):
                console.print("📝 Enter your code (press Ctrl+D when done):")
                code_lines = []
                try:
                    while True:
                        line = input()
                        code_lines.append(line)
                except EOFError:
                    pass

                if code_lines:
                    code = "\n".join(code_lines)
                    await code_review_assistant(code, current_language)
                continue

            # Regular question
            conversation.add_message("user", user_input)

            # Build context from conversation history
            context_messages = conversation.get_context()
            context_str = "\n".join(
                [f"{msg['role']}: {msg['content']}" for msg in context_messages[:-1]]
            )  # Exclude current message

            # Get AI response
            answer = await ask_coding_question(
                user_input, context_str, current_language
            )

            if answer:
                conversation.add_message("assistant", answer)

        except KeyboardInterrupt:
            console.print("\n[yellow]👋 Chat interrupted[/yellow]")
            break
        except Exception as e:
            console.print(f"[red]💥 Error: {e}[/red]")


def show_help():
    """Show available commands"""
    help_table = Table(title="🤖 AI Assistant Commands")
    help_table.add_column("Command", style="cyan")
    help_table.add_column("Description", style="white")

    commands = [
        ("/language <lang>", "Set programming language (python, javascript, etc.)"),
        ("/explain <concept>", "Explain a programming concept"),
        ("/best <topic>", "Get best practices for a topic"),
        ("/review", "Get AI code review (enter code after command)"),
        ("help", "Show this help message"),
        ("exit", "Exit the assistant"),
    ]

    for cmd, desc in commands:
        help_table.add_row(cmd, desc)

    console.print(help_table)


async def main():
    """
    Main function for AI Smart Assistant
    """
    parser = argparse.ArgumentParser(
        description="🤖 AI Smart Assistant - Your intelligent coding companion",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ai_assistant.py --question "How do I handle exceptions in Python?"
  python ai_assistant.py --explain "decorators" --language python
  python ai_assistant.py --best "API design" --language python
        """,
    )

    parser.add_argument("--question", "-q", help="Ask a specific coding question")

    parser.add_argument("--explain", "-e", help="Explain a programming concept")

    parser.add_argument("--best", "-b", help="Get best practices for a topic")

    parser.add_argument(
        "--language",
        "-l",
        default="python",
        help="Programming language context (default: python)",
    )

    parser.add_argument(
        "--level",
        choices=["beginner", "intermediate", "advanced"],
        default="intermediate",
        help="Explanation level (use with --explain)",
    )

    args = parser.parse_args()

    console.print("🦁 [bold blue]CodeBeast AI Smart Assistant[/bold blue] 🤖")
    console.print("Super Strong • Smart • Helpful\n")

    if args.question:
        await ask_coding_question(args.question, language=args.language)
    elif args.explain:
        await explain_concept(args.explain, args.level)
    elif args.best:
        await get_best_practices(args.best, args.language)
    else:
        await interactive_assistant()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Assistant interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"[red]💥 Unexpected error: {e}[/red]")
