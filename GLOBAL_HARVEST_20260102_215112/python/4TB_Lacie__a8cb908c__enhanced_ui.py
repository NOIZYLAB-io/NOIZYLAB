#!/usr/bin/env python3
"""
Enhanced UI Components - Better Visuals and Animations
======================================================
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.text import Text
from rich.align import Align
from rich import box
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import time

console = Console()

class EnhancedUI:
    """Enhanced UI components"""
    
    @staticmethod
    def create_header(title: str, subtitle: str = "") -> Panel:
        """Create enhanced header"""
        header_text = f"[bold cyan]{title}[/bold cyan]"
        if subtitle:
            header_text += f"\n[dim]{subtitle}[/dim]"
        return Panel.fit(header_text, border_style="cyan", box=box.DOUBLE)
    
    @staticmethod
    def create_stats_panel(stats: dict) -> Panel:
        """Create statistics panel"""
        stats_text = ""
        for key, value in stats.items():
            stats_text += f"[bold]{key}:[/bold] {value}\n"
        return Panel(stats_text.strip(), title="📊 Statistics", border_style="green")
    
    @staticmethod
    def create_menu_table(options: list) -> Table:
        """Create enhanced menu table"""
        table = Table.grid(padding=(0, 2), expand=True)
        for option in options:
            table.add_row(option)
        return table
    
    @staticmethod
    def show_loading(message: str, duration: float = 1.0):
        """Show loading animation"""
        with console.status(f"[bold green]{message}[/bold green]"):
            time.sleep(duration)
    
    @staticmethod
    def create_progress_bar(total: int, description: str = "Processing"):
        """Create progress bar"""
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        )
    
    @staticmethod
    def create_success_panel(message: str) -> Panel:
        """Create success message panel"""
        return Panel.fit(
            f"[bold green]✅ {message}[/bold green]",
            border_style="green",
            box=box.ROUNDED
        )
    
    @staticmethod
    def create_error_panel(message: str) -> Panel:
        """Create error message panel"""
        return Panel.fit(
            f"[bold red]❌ {message}[/bold red]",
            border_style="red",
            box=box.ROUNDED
        )
    
    @staticmethod
    def create_info_panel(message: str, title: str = "ℹ️  Information") -> Panel:
        """Create info panel"""
        return Panel(
            message,
            title=title,
            border_style="blue",
            box=box.ROUNDED
        )

