#!/usr/bin/env python3
"""
🔍 AI CODE ANALYZER CLAW 🔍
Super smart code analysis powered by OpenAI

This claw provides intelligent code analysis, security scanning,
performance optimization suggestions, and best practices recommendations.
"""

import argparse
import asyncio
import sys
from pathlib import Path

# Add core to path for imports
sys.path.append(str(Path(__file__).parent.parent / "core"))

from ai_engine import get_ai_engine
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

console = Console()


async def analyze_file(file_path: str, analysis_type: str = "comprehensive"):
    """
    🔍 Analyze a code file with AI
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
            ".php": "php",
            ".rb": "ruby",
            ".go": "go",
            ".rs": "rust",
            ".swift": "swift",
        }

        language = language_map.get(file_path_obj.suffix, "text")

        # Display the code being analyzed
        console.print(
            Panel(
                Syntax(
                    (
                        code_content[:500] + "..."
                        if len(code_content) > 500
                        else code_content
                    ),
                    language,
                    theme="monokai",
                    line_numbers=True,
                ),
                title=f"📁 Analyzing: {file_path_obj.name}",
                expand=False,
            )
        )

        # Get AI engine and analyze
        ai = get_ai_engine()
        if not ai.api_key:
            console.print("[red]❌ OpenAI API key not configured![/red]")
            return

        # Perform AI analysis
        result = await ai.analyze_code(code_content, language, analysis_type)

        # Display results
        ai.display_response(result, f"Code Analysis: {file_path_obj.name}")

    except Exception as e:
        console.print(f"[red]💥 Error analyzing file: {e}[/red]")


async def analyze_directory(dir_path: str, file_extensions: list = None):
    """
    🗂️ Analyze all code files in a directory
    """
    if file_extensions is None:
        file_extensions = [".py", ".js", ".ts", ".java", ".cpp", ".c"]

    dir_path_obj = Path(dir_path)

    if not dir_path_obj.exists():
        console.print(f"[red]❌ Directory not found: {dir_path}[/red]")
        return

    # Find all code files
    code_files = []
    for ext in file_extensions:
        code_files.extend(list(dir_path_obj.rglob(f"*{ext}")))

    if not code_files:
        console.print(f"[yellow]⚠️ No code files found in {dir_path}[/yellow]")
        return

    console.print(f"[green]📂 Found {len(code_files)} code files to analyze[/green]")

    # Analyze each file
    for file_path in code_files:
        if file_path.stat().st_size > 50000:  # Skip files larger than 50KB
            console.print(f"[yellow]⏭️ Skipping large file: {file_path.name}[/yellow]")
            continue

        console.print(
            f"\n[blue]🔍 Analyzing: {file_path.relative_to(dir_path_obj)}[/blue]"
        )
        await analyze_file(str(file_path), "quick")


async def main():
    """
    Main function for AI Code Analyzer
    """
    parser = argparse.ArgumentParser(
        description="🔍 AI Code Analyzer - Super smart code analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ai_code_analyzer.py --file my_script.py
  python ai_code_analyzer.py --directory ./src --type security
  python ai_code_analyzer.py --file app.py --type performance
        """,
    )

    parser.add_argument("--file", "-f", help="Path to the code file to analyze")

    parser.add_argument(
        "--directory", "-d", help="Path to directory containing code files"
    )

    parser.add_argument(
        "--type",
        "-t",
        choices=["comprehensive", "security", "performance", "quality", "quick"],
        default="comprehensive",
        help="Type of analysis to perform",
    )

    parser.add_argument(
        "--extensions",
        "-e",
        nargs="+",
        default=[".py", ".js", ".ts", ".java", ".cpp", ".c"],
        help="File extensions to include when analyzing directories",
    )

    args = parser.parse_args()

    console.print("🦁 [bold blue]CodeBeast AI Code Analyzer[/bold blue] 🔍")
    console.print("Super Strong • Smart • Helpful\n")

    if args.file:
        await analyze_file(args.file, args.type)
    elif args.directory:
        await analyze_directory(args.directory, args.extensions)
    else:
        # Interactive mode
        console.print("[cyan]🎯 Interactive Code Analysis Mode[/cyan]")

        while True:
            console.print("\n" + "=" * 50)
            console.print("1. 📁 Analyze a file")
            console.print("2. 📂 Analyze a directory")
            console.print("3. 🚪 Exit")

            choice = console.input("\n🎯 Choose option: ").strip()

            if choice == "1":
                file_path = console.input("📁 Enter file path: ").strip()
                analysis_type = (
                    console.input(
                        "🔍 Analysis type (comprehensive/security/performance/quality/quick) [comprehensive]: "
                    ).strip()
                    or "comprehensive"
                )
                await analyze_file(file_path, analysis_type)

            elif choice == "2":
                dir_path = console.input("📂 Enter directory path: ").strip()
                await analyze_directory(dir_path)

            elif choice == "3":
                console.print("👋 [green]Happy coding![/green]")
                break

            else:
                console.print("[red]❓ Invalid choice[/red]")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Analysis interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"[red]💥 Unexpected error: {e}[/red]")
