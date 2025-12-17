#!/usr/bin/env python3
"""
🛠️ AI CODE GENERATOR CLAW 🛠️
Generate high-quality code from natural language descriptions

This claw uses OpenAI to generate complete, production-ready code
from simple descriptions or requirements.
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
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

console = Console()


async def generate_code(
    description: str,
    language: str = "python",
    framework: Optional[str] = None,
    output_file: Optional[str] = None,
) -> str:
    """
    🛠️ Generate code from description
    """
    try:
        # Get AI engine and generate code
        ai = get_ai_engine()
        if not ai.api_key:
            console.print("[red]❌ OpenAI API key not configured![/red]")
            return ""

        console.print(f"[blue]🛠️ Generating {language} code...[/blue]")
        if framework:
            console.print(f"[dim]Framework: {framework}[/dim]")

        result = await ai.generate_code(description, language, framework)

        if not result.success:
            console.print(f"[red]❌ Generation failed: {result.error}[/red]")
            return ""

        # Display the generated code
        ai.display_response(result, f"Generated {language.title()} Code")

        # Save to file if requested
        if output_file:
            try:
                output_path = Path(output_file)
                output_path.parent.mkdir(parents=True, exist_ok=True)

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result.content)

                console.print(f"[green]💾 Code saved to: {output_file}[/green]")
            except Exception as e:
                console.print(f"[red]❌ Error saving file: {e}[/red]")

        return result.content

    except Exception as e:
        console.print(f"[red]💥 Error generating code: {e}[/red]")
        return ""


async def generate_project_structure(project_name: str, project_type: str):
    """
    🏗️ Generate complete project structure
    """
    console.print(f"[blue]🏗️ Generating {project_type} project: {project_name}[/blue]")

    project_templates = {
        "web_app": "Create a complete web application with frontend (HTML/CSS/JS), backend API, database models, authentication, and deployment configuration",
        "cli_tool": "Create a command-line interface tool with argument parsing, configuration management, logging, and help documentation",
        "api": "Create a RESTful API with endpoints, models, authentication, error handling, and documentation",
        "library": "Create a reusable library with well-documented functions, classes, tests, and packaging configuration",
        "data_pipeline": "Create a data processing pipeline with ingestion, transformation, validation, and output modules",
        "microservice": "Create a microservice with health checks, metrics, logging, containerization, and service communication",
    }

    description = project_templates.get(
        project_type, f"Create a {project_type} project"
    )
    description += f"\n\nProject name: {project_name}"

    # Generate project code
    code = await generate_code(description, "python", None, None)

    if code and Confirm.ask("💾 Save project files to directory?"):
        project_dir = Path(project_name)
        project_dir.mkdir(exist_ok=True)

        # Save main project file
        main_file = project_dir / f"{project_name.lower()}.py"
        with open(main_file, "w", encoding="utf-8") as f:
            f.write(code)

        console.print(f"[green]📁 Project created in: {project_dir}[/green]")


async def interactive_generator():
    """
    🎯 Interactive code generation mode
    """
    console.print("[cyan]🎯 Interactive Code Generator[/cyan]")

    while True:
        console.print("\n" + "=" * 60)
        console.print("1. 🛠️  Generate code from description")
        console.print("2. 🏗️  Generate complete project")
        console.print("3. 📝  Generate specific component")
        console.print("4. 🔧  Generate utility functions")
        console.print("5. 🚪  Exit")

        choice = Prompt.ask("\n🎯 Choose option", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            description = Prompt.ask("📝 Describe what you want to build")
            language = Prompt.ask("💻 Programming language", default="python")
            framework = Prompt.ask("🔧 Framework (optional)", default="")
            output_file = Prompt.ask("💾 Output file (optional)", default="")

            await generate_code(
                description,
                language,
                framework if framework else None,
                output_file if output_file else None,
            )

        elif choice == "2":
            project_name = Prompt.ask("📁 Project name")
            project_type = Prompt.ask(
                "🏗️ Project type",
                choices=[
                    "web_app",
                    "cli_tool",
                    "api",
                    "library",
                    "data_pipeline",
                    "microservice",
                ],
                default="web_app",
            )
            await generate_project_structure(project_name, project_type)

        elif choice == "3":
            component_types = {
                "class": "Create a Python class with methods and properties",
                "function": "Create a utility function with error handling",
                "api_endpoint": "Create an API endpoint with request/response handling",
                "database_model": "Create a database model with relationships",
                "test": "Create comprehensive unit tests",
            }

            component = Prompt.ask(
                "🧩 Component type", choices=list(component_types.keys())
            )

            description = Prompt.ask("📝 Component description")
            full_description = f"{component_types[component]}. {description}"

            await generate_code(full_description)

        elif choice == "4":
            utility_types = [
                "File operations (read, write, copy, move)",
                "Data validation and sanitization",
                "Configuration management",
                "Logging and error handling",
                "API client with retry logic",
                "Data transformation and processing",
            ]

            console.print("\n🔧 Available utility types:")
            for i, util in enumerate(utility_types, 1):
                console.print(f"{i}. {util}")

            util_choice = int(
                Prompt.ask(
                    "Select utility type",
                    choices=[str(i) for i in range(1, len(utility_types) + 1)],
                )
            )
            util_description = utility_types[util_choice - 1]

            custom_desc = Prompt.ask(
                "📝 Additional requirements (optional)", default=""
            )
            full_desc = f"Create utility functions for {util_description.lower()}. {custom_desc}"

            await generate_code(full_desc)

        elif choice == "5":
            console.print("👋 [green]Happy coding![/green]")
            break


async def main():
    """
    Main function for AI Code Generator
    """
    parser = argparse.ArgumentParser(
        description="🛠️ AI Code Generator - Generate code from natural language",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ai_code_generator.py --description "Create a REST API for user management"
  python ai_code_generator.py --description "Build a file encryption utility" --language python
  python ai_code_generator.py --project "MyAPI" --type "api"
        """,
    )

    parser.add_argument("--description", "-d", help="Description of what to build")

    parser.add_argument(
        "--language",
        "-l",
        default="python",
        help="Programming language (default: python)",
    )

    parser.add_argument("--framework", "-f", help="Framework to use (optional)")

    parser.add_argument("--output", "-o", help="Output file path")

    parser.add_argument(
        "--project", "-p", help="Generate complete project with this name"
    )

    parser.add_argument(
        "--type",
        "-t",
        choices=[
            "web_app",
            "cli_tool",
            "api",
            "library",
            "data_pipeline",
            "microservice",
        ],
        help="Project type (use with --project)",
    )

    args = parser.parse_args()

    console.print("🦁 [bold blue]CodeBeast AI Code Generator[/bold blue] 🛠️")
    console.print("Super Strong • Smart • Helpful\n")

    if args.description:
        await generate_code(
            args.description, args.language, args.framework, args.output
        )
    elif args.project:
        project_type = args.type or "web_app"
        await generate_project_structure(args.project, project_type)
    else:
        await interactive_generator()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Generation interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"[red]💥 Unexpected error: {e}[/red]")
