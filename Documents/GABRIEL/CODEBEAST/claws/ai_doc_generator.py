#!/usr/bin/env python3
"""
📚 AI DOCUMENTATION GENERATOR CLAW 📚
Generate comprehensive documentation with OpenAI

This claw automatically generates high-quality documentation
for your code, APIs, and projects.
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
    from rich.markdown import Markdown
    from rich.panel import Panel
    from rich.prompt import Confirm, Prompt
    from rich.syntax import Syntax
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

console = Console()


async def generate_file_docs(file_path: str, doc_type: str = "api"):
    """
    📖 Generate documentation for a code file
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
        }

        language = language_map.get(file_path_obj.suffix, "text")

        # Display the code being documented
        console.print(
            Panel(
                Syntax(
                    (
                        code_content[:800] + "..."
                        if len(code_content) > 800
                        else code_content
                    ),
                    language,
                    theme="monokai",
                    line_numbers=True,
                ),
                title=f"📖 Documenting: {file_path_obj.name}",
                expand=False,
            )
        )

        # Get AI engine and generate documentation
        ai = get_ai_engine()
        if not ai.api_key:
            console.print("[red]❌ OpenAI API key not configured![/red]")
            return

        # Perform AI documentation generation
        result = await ai.generate_documentation(code_content, language, doc_type)

        # Display results
        ai.display_response(result, f"Documentation: {file_path_obj.name}")

        # Offer to save documentation
        if result.success and Confirm.ask("💾 Save documentation to file?"):
            doc_extension = ".md" if doc_type in ["readme", "guide"] else ".txt"
            doc_file = (
                file_path_obj.parent / f"{file_path_obj.stem}_docs{doc_extension}"
            )

            with open(doc_file, "w", encoding="utf-8") as f:
                f.write(result.content)

            console.print(f"[green]📄 Documentation saved to: {doc_file}[/green]")

    except Exception as e:
        console.print(f"[red]💥 Error generating documentation: {e}[/red]")


async def generate_project_readme(project_dir: str):
    """
    📋 Generate comprehensive README for a project
    """
    try:
        project_path = Path(project_dir)

        if not project_path.exists():
            console.print(f"[red]❌ Directory not found: {project_dir}[/red]")
            return

        # Scan project structure
        console.print(
            f"[blue]🔍 Analyzing project structure: {project_path.name}[/blue]"
        )

        # Find main files
        main_files = []
        config_files = []

        for pattern in ["*.py", "*.js", "*.ts", "*.java", "*.cpp", "*.c"]:
            main_files.extend(list(project_path.rglob(pattern)))

        for pattern in [
            "requirements.txt",
            "package.json",
            "Dockerfile",
            "*.yml",
            "*.yaml",
        ]:
            config_files.extend(list(project_path.rglob(pattern)))

        # Build project description
        project_info = f"""
        Project Name: {project_path.name}
        Main Files: {len(main_files)} code files
        Configuration Files: {len(config_files)} config files
        
        File Structure:
        """

        for file in main_files[:10]:  # Show first 10 files
            project_info += f"\n- {file.relative_to(project_path)}"

        if len(main_files) > 10:
            project_info += f"\n... and {len(main_files) - 10} more files"

        # Read main entry point if exists
        entry_points = ["main.py", "app.py", "index.js", "server.js", "main.java"]
        main_code = ""

        for entry in entry_points:
            entry_file = project_path / entry
            if entry_file.exists():
                with open(entry_file, "r", encoding="utf-8") as f:
                    main_code = f.read()[:2000]  # First 2000 chars
                break

        description = f"""
        Create a comprehensive README.md for this project:
        
        {project_info}
        
        Main code sample:
        ```
        {main_code}
        ```
        
        Include:
        1. Project title and description
        2. Features and capabilities
        3. Installation instructions
        4. Usage examples
        5. Configuration guide
        6. Contributing guidelines
        7. License information
        """

        # Generate README with AI
        ai = get_ai_engine()
        if not ai.api_key:
            console.print("[red]❌ OpenAI API key not configured![/red]")
            return

        result = await ai.generate_documentation(description, "markdown", "readme")

        # Display results
        ai.display_response(result, f"README for {project_path.name}")

        # Save README
        if result.success and Confirm.ask("💾 Save README.md to project directory?"):
            readme_file = project_path / "README.md"

            with open(readme_file, "w", encoding="utf-8") as f:
                f.write(result.content)

            console.print(f"[green]📄 README.md saved to: {readme_file}[/green]")

    except Exception as e:
        console.print(f"[red]💥 Error generating README: {e}[/red]")


async def generate_api_docs(file_path: str):
    """
    🌐 Generate API documentation
    """
    await generate_file_docs(file_path, "api")


async def interactive_doc_generator():
    """
    🎯 Interactive documentation generator
    """
    console.print("[cyan]🎯 Interactive Documentation Generator[/cyan]")

    while True:
        console.print("\n" + "=" * 60)
        console.print("1. 📖 Generate file documentation")
        console.print("2. 🌐 Generate API documentation")
        console.print("3. 📋 Generate project README")
        console.print("4. 📚 Generate user guide")
        console.print("5. 🔧 Generate developer docs")
        console.print("6. 🚪 Exit")

        choice = Prompt.ask(
            "\n🎯 Choose option", choices=["1", "2", "3", "4", "5", "6"]
        )

        if choice == "1":
            file_path = Prompt.ask("📁 Enter file path")
            doc_type = Prompt.ask(
                "📖 Documentation type",
                choices=["api", "tutorial", "reference", "guide"],
                default="api",
            )
            await generate_file_docs(file_path, doc_type)

        elif choice == "2":
            file_path = Prompt.ask("📁 Enter API file path")
            await generate_api_docs(file_path)

        elif choice == "3":
            project_dir = Prompt.ask("📂 Enter project directory")
            await generate_project_readme(project_dir)

        elif choice == "4":
            file_path = Prompt.ask("📁 Enter file path")
            await generate_file_docs(file_path, "tutorial")

        elif choice == "5":
            file_path = Prompt.ask("📁 Enter file path")
            await generate_file_docs(file_path, "developer")

        elif choice == "6":
            console.print("👋 [green]Happy documenting![/green]")
            break


async def main():
    """
    Main function for AI Documentation Generator
    """
    parser = argparse.ArgumentParser(
        description="📚 AI Documentation Generator - Comprehensive docs with AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ai_doc_generator.py --file my_script.py
  python ai_doc_generator.py --file api.py --type api
  python ai_doc_generator.py --readme ./my_project
        """,
    )

    parser.add_argument("--file", "-f", help="Path to the code file to document")

    parser.add_argument(
        "--type",
        "-t",
        choices=["api", "tutorial", "reference", "guide", "developer"],
        default="api",
        help="Type of documentation to generate",
    )

    parser.add_argument(
        "--readme", "-r", help="Generate README.md for project directory"
    )

    args = parser.parse_args()

    console.print("🦁 [bold blue]CodeBeast AI Documentation Generator[/bold blue] 📚")
    console.print("Super Strong • Smart • Helpful\n")

    if args.file:
        await generate_file_docs(args.file, args.type)
    elif args.readme:
        await generate_project_readme(args.readme)
    else:
        await interactive_doc_generator()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Documentation interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"[red]💥 Unexpected error: {e}[/red]")
