# {PROJECT_NAME}

## Project Type
Command-Line Interface Application

## Tech Stack
- **Language**: {PYTHON|RUST|GO|NODE}
- **CLI Framework**: {CLICK|TYPER|CLAP|COBRA|COMMANDER}
- **Packaging**: {UV|CARGO|GO|NPM}

## Project Structure (Python/Typer)
```
src/
├── {package_name}/
│   ├── __init__.py
│   ├── __main__.py       # Entry point
│   ├── cli.py            # CLI definition
│   ├── commands/         # Command modules
│   │   ├── __init__.py
│   │   ├── init.py
│   │   └── run.py
│   ├── core/             # Business logic
│   └── utils/
│       ├── config.py     # Configuration
│       ├── output.py     # Rich output
│       └── prompts.py    # User prompts
├── tests/
└── pyproject.toml
```

## Project Structure (Rust/Clap)
```
src/
├── main.rs               # Entry point
├── cli.rs                # CLI definition
├── commands/             # Command modules
│   ├── mod.rs
│   ├── init.rs
│   └── run.rs
└── lib.rs                # Library code

Cargo.toml
```

## CLI Patterns

### Python (Typer)
```python
import typer
from rich.console import Console

app = typer.Typer(help="My awesome CLI")
console = Console()

@app.command()
def init(
    name: str = typer.Argument(..., help="Project name"),
    template: str = typer.Option("default", "--template", "-t"),
    force: bool = typer.Option(False, "--force", "-f"),
):
    """Initialize a new project."""
    console.print(f"[green]Creating {name}...[/green]")

@app.command()
def run(
    config: Path = typer.Option("config.yaml", "--config", "-c"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Run the application."""
    ...

if __name__ == "__main__":
    app()
```

### Rust (Clap)
```rust
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name = "mycli", about = "My awesome CLI")]
struct Cli {
    #[command(subcommand)]
    command: Commands,

    #[arg(short, long)]
    verbose: bool,
}

#[derive(Subcommand)]
enum Commands {
    Init {
        #[arg(help = "Project name")]
        name: String,

        #[arg(short, long, default_value = "default")]
        template: String,
    },
    Run {
        #[arg(short, long, default_value = "config.yaml")]
        config: PathBuf,
    },
}

fn main() {
    let cli = Cli::parse();
    match cli.command {
        Commands::Init { name, template } => init(&name, &template),
        Commands::Run { config } => run(&config),
    }
}
```

## Output Patterns

### Rich (Python)
```python
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel

console = Console()

# Colored output
console.print("[green]Success![/green]")
console.print("[red]Error:[/red] Something went wrong")
console.print("[yellow]Warning:[/yellow] Be careful")

# Tables
table = Table(title="Results")
table.add_column("Name", style="cyan")
table.add_column("Status", style="green")
table.add_row("Item 1", "OK")
console.print(table)

# Progress
with Progress() as progress:
    task = progress.add_task("Processing...", total=100)
    for i in range(100):
        progress.update(task, advance=1)
```

### Colored (Rust)
```rust
use colored::*;

println!("{}", "Success!".green());
println!("{}", "Error!".red().bold());
println!("{}", "Warning".yellow());
```

## Configuration

### YAML Config
```python
from pathlib import Path
import yaml
from pydantic import BaseModel

class Config(BaseModel):
    debug: bool = False
    output_dir: Path = Path("./output")

def load_config(path: Path) -> Config:
    if path.exists():
        with open(path) as f:
            data = yaml.safe_load(f)
            return Config(**data)
    return Config()
```

### Environment Variables
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    debug: bool = False

    class Config:
        env_prefix = "MYAPP_"
        env_file = ".env"
```

## Interactive Prompts

### Python (Questionary)
```python
import questionary

# Confirm
if questionary.confirm("Continue?").ask():
    ...

# Select
choice = questionary.select(
    "Choose an option:",
    choices=["Option 1", "Option 2", "Option 3"]
).ask()

# Text input
name = questionary.text("Enter name:").ask()

# Password
password = questionary.password("Enter password:").ask()
```

## Error Handling
```python
import sys
from rich.console import Console

console = Console(stderr=True)

def error(message: str, code: int = 1) -> None:
    console.print(f"[red]Error:[/red] {message}")
    sys.exit(code)

def warn(message: str) -> None:
    console.print(f"[yellow]Warning:[/yellow] {message}")
```

## Testing CLI
```python
from typer.testing import CliRunner
from myapp.cli import app

runner = CliRunner()

def test_init():
    result = runner.invoke(app, ["init", "myproject"])
    assert result.exit_code == 0
    assert "Creating myproject" in result.output

def test_run_with_config():
    result = runner.invoke(app, ["run", "--config", "test.yaml"])
    assert result.exit_code == 0
```

## Packaging

### Python (pyproject.toml)
```toml
[project.scripts]
mycli = "myapp.cli:app"
```

### Rust (Cargo.toml)
```toml
[[bin]]
name = "mycli"
path = "src/main.rs"
```

## Shell Completion
```python
# Typer generates completions automatically
# Install with: mycli --install-completion
```

## Best Practices
- Use subcommands for complex CLIs
- Provide sensible defaults
- Support both short and long flags
- Use colors for better UX
- Show progress for long operations
- Support quiet/verbose modes
- Handle Ctrl+C gracefully
- Return proper exit codes
