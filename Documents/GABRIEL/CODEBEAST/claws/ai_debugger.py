#!/usr/bin/env python3
"""
🐛 AI DEBUGGER CLAW 🐛
Intelligent bug detection and fixing powered by OpenAI

This claw helps you find and fix bugs in your code with AI-powered
analysis, error pattern recognition, and solution suggestions.
"""

import argparse
import asyncio
import sys
from pathlib import Path
from typing import Optional

# Add core to path for imports
sys.path.append(str(Path(__file__).parent.parent / "core"))

try:
    from ai_engine import get_ai_engine
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Confirm, Prompt
    from rich.syntax import Syntax
    from rich.table import Table
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

console = Console()


async def debug_code_file(file_path: str, error_message: Optional[str] = None):
    """
    🐛 Debug a code file
    """
    try:
        file_path_obj = Path(file_path)

        if not file_path_obj.exists():
            console.print(f"[red]❌ File not found: {file_path}[/red]")
            return

        # Read the file content
        with open(file_path_obj, "r", encoding="utf-8") as f:
            code_content = f.read()

        # Detect language from file extension
        language_map = {
            ".py": "python",
            ".js": "javascript",
            ".ts": "typescript",
            ".java": "java",
            ".cpp": "cpp",
            ".c": "c",
            ".cs": "csharp",
        }

        language = language_map.get(file_path_obj.suffix, "text")

        # Display the code being debugged
        console.print(
            Panel(
                Syntax(code_content, language, theme="monokai", line_numbers=True),
                title=f"🐛 Debugging: {file_path_obj.name}",
                expand=False,
            )
        )

        if error_message:
            console.print(
                Panel(error_message, title="❌ Error Message", border_style="red")
            )

        # Get AI engine and debug
        ai = get_ai_engine()
        if not ai.api_key:
            console.print("[red]❌ OpenAI API key not configured![/red]")
            return

        # Perform AI debugging
        result = await ai.debug_code(code_content, error_message, language)

        # Display results
        ai.display_response(result, f"Debug Analysis: {file_path_obj.name}")

        # Offer to save fixed code
        if result.success and "```" in result.content:
            if Confirm.ask("💾 Save the fixed code to a new file?"):
                fixed_file = (
                    file_path_obj.parent
                    / f"{file_path_obj.stem}_fixed{file_path_obj.suffix}"
                )

                # Extract code from AI response (assuming it's in markdown format)
                lines = result.content.split("\n")
                code_lines = []
                in_code_block = False

                for line in lines:
                    if line.strip().startswith("```"):
                        in_code_block = not in_code_block
                        continue
                    if in_code_block:
                        code_lines.append(line)

                if code_lines:
                    with open(fixed_file, "w", encoding="utf-8") as f:
                        f.write("\n".join(code_lines))
                    console.print(
                        f"[green]💾 Fixed code saved to: {fixed_file}[/green]"
                    )

    except Exception as e:
        console.print(f"[red]💥 Error debugging file: {e}[/red]")


async def debug_code_snippet(
    code: str, language: str = "python", error_message: Optional[str] = None
):
    """
    🔍 Debug a code snippet
    """
    try:
        # Display the code being debugged
        console.print(
            Panel(
                Syntax(code, language, theme="monokai", line_numbers=True),
                title="🐛 Debugging Code Snippet",
                expand=False,
            )
        )

        if error_message:
            console.print(
                Panel(error_message, title="❌ Error Message", border_style="red")
            )

        # Get AI engine and debug
        ai = get_ai_engine()
        if not ai.api_key:
            console.print("[red]❌ OpenAI API key not configured![/red]")
            return

        # Perform AI debugging
        result = await ai.debug_code(code, error_message, language)

        # Display results
        ai.display_response(result, "Debug Analysis")

    except Exception as e:
        console.print(f"[red]💥 Error debugging code: {e}[/red]")


async def analyze_common_bugs(language: str = "python"):
    """
    📋 Show common bugs and how to avoid them
    """
    bug_patterns = {
        "python": [
            "IndentationError - Mixed tabs and spaces",
            "NameError - Using undefined variables",
            "TypeError - Incorrect data types",
            "IndexError - List index out of range",
            "KeyError - Dictionary key not found",
            "AttributeError - Object has no attribute",
            "ImportError - Module not found",
            "ValueError - Invalid value passed to function",
        ],
        "javascript": [
            "ReferenceError - Variable not defined",
            "TypeError - Cannot read property of undefined",
            "SyntaxError - Missing semicolons or brackets",
            "RangeError - Number out of range",
            "URIError - Invalid URI encoding",
            "EvalError - Error in eval() function",
        ],
        "java": [
            "NullPointerException - Accessing null object",
            "ArrayIndexOutOfBoundsException - Invalid array index",
            "ClassCastException - Invalid type casting",
            "NumberFormatException - Invalid number format",
            "IllegalArgumentException - Invalid method argument",
        ],
    }

    bugs = bug_patterns.get(language, bug_patterns["python"])

    table = Table(title=f"🐛 Common {language.title()} Bugs")
    table.add_column("Bug Type", style="red")
    table.add_column("Description", style="cyan")

    for bug in bugs:
        bug_type, description = bug.split(" - ", 1)
        table.add_row(bug_type, description)

    console.print(table)


async def interactive_debugger():
    """
    🎯 Interactive debugging mode
    """
    console.print("[cyan]🎯 Interactive AI Debugger[/cyan]")

    while True:
        console.print("\n" + "=" * 50)
        console.print("1. 🐛 Debug a file")
        console.print("2. 🔍 Debug code snippet")
        console.print("3. 📋 Show common bugs")
        console.print("4. 🚪 Exit")

        choice = Prompt.ask("\n🎯 Choose option", choices=["1", "2", "3", "4"])

        if choice == "1":
            file_path = Prompt.ask("📁 Enter file path")
            error_msg = Prompt.ask("❌ Error message (optional)", default="")
            await debug_code_file(file_path, error_msg if error_msg else None)

        elif choice == "2":
            console.print("\n📝 Enter your code (press Ctrl+D when done):")
            code_lines = []
            try:
                while True:
                    line = input()
                    code_lines.append(line)
            except EOFError:
                pass

            if code_lines:
                code = "\n".join(code_lines)
                language = Prompt.ask("💻 Programming language", default="python")
                error_msg = Prompt.ask("❌ Error message (optional)", default="")
                await debug_code_snippet(
                    code, language, error_msg if error_msg else None
                )

        elif choice == "3":
            language = Prompt.ask(
                "💻 Language",
                choices=["python", "javascript", "java"],
                default="python",
            )
            await analyze_common_bugs(language)

        elif choice == "4":
            console.print("👋 [green]Happy debugging![/green]")
            break


async def main():
    """
    Main function for AI Debugger
    """
    parser = argparse.ArgumentParser(
        description="🐛 AI Debugger - Intelligent bug detection and fixing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ai_debugger.py --file my_script.py
  python ai_debugger.py --file app.py --error "ValueError: invalid literal"
  python ai_debugger.py --snippet "print(x)" --language python
        """,
    )

    parser.add_argument("--file", "-f", help="Path to the code file to debug")

    parser.add_argument("--error", "-e", help="Error message to help with debugging")

    parser.add_argument("--snippet", "-s", help="Code snippet to debug")

    parser.add_argument(
        "--language",
        "-l",
        default="python",
        help="Programming language (default: python)",
    )

    parser.add_argument(
        "--common-bugs",
        "-c",
        action="store_true",
        help="Show common bugs for the specified language",
    )

    args = parser.parse_args()

    console.print("🦁 [bold blue]CodeBeast AI Debugger[/bold blue] 🐛")
    console.print("Super Strong • Smart • Helpful\n")

    if args.file:
        await debug_code_file(args.file, args.error)
    elif args.snippet:
        await debug_code_snippet(args.snippet, args.language, args.error)
    elif args.common_bugs:
        await analyze_common_bugs(args.language)
    else:
        await interactive_debugger()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Debugging interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"[red]💥 Unexpected error: {e}[/red]")
