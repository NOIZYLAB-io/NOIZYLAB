#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   📊 NOIZYLAB CLOUD AGENT MONITORING DASHBOARD                           ║
║                                                                           ║
║   Real-time monitoring of cloud agent performance and health             ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import sys
from datetime import datetime
from typing import Optional

try:
    from rich.console import Console
    from rich.table import Table
    from rich.live import Live
    from rich.panel import Panel
    from rich.layout import Layout
    from rich.text import Text
    from rich import box
except ImportError:
    print("❌ Error: 'rich' library required")
    print("   Install with: pip install rich")
    sys.exit(1)

from cloud_agent_client import CloudAgentClient, CloudAgentOrchestrator

console = Console()

class CloudAgentDashboard:
    """Real-time monitoring dashboard for cloud agent"""
    
    def __init__(self, endpoint: str = None, api_key: str = None):
        self.orchestrator = CloudAgentOrchestrator(
            endpoint=endpoint if endpoint else None,
            api_key=api_key if api_key else ""
        )
        self.console = Console()
        self.start_time = datetime.now()
        self.refresh_interval = 2  # seconds
    
    async def initialize(self):
        """Initialize dashboard"""
        await self.orchestrator.initialize()
    
    def create_header(self) -> Panel:
        """Create dashboard header"""
        uptime = datetime.now() - self.start_time
        uptime_str = f"{int(uptime.total_seconds())}s"
        
        header_text = Text()
        header_text.append("☁️  NOIZYLAB Cloud Agent Dashboard", style="bold cyan")
        header_text.append(f"\n🕐 Uptime: {uptime_str} | ", style="dim")
        header_text.append(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", style="dim")
        
        return Panel(header_text, box=box.DOUBLE, border_style="cyan")
    
    async def create_status_table(self) -> Table:
        """Create status table"""
        status = await self.orchestrator.get_status()
        
        table = Table(title="Cloud Agent Status", box=box.ROUNDED, show_header=False)
        table.add_column("Property", style="cyan", width=25)
        table.add_column("Value", style="white")
        
        # Cloud agent status
        cloud = status.get("cloud_agent", {})
        healthy = cloud.get("healthy", False)
        health_icon = "🟢" if healthy else "🔴"
        health_text = "HEALTHY" if healthy else "UNHEALTHY"
        
        table.add_row(
            "Status",
            f"{health_icon} {health_text}"
        )
        
        if "version" in cloud:
            table.add_row("Version", cloud.get("version", "unknown"))
        
        if "endpoint" in cloud:
            table.add_row("Endpoint", cloud.get("endpoint", "unknown"))
        
        # Circuit breaker
        cb = status.get("circuit_breaker", {})
        cb_state = cb.get("state", "unknown")
        cb_icon = "🟢" if cb_state == "closed" else "🟡" if cb_state == "half_open" else "🔴"
        
        table.add_row(
            "Circuit Breaker",
            f"{cb_icon} {cb_state.upper()}"
        )
        
        table.add_row(
            "Failures",
            str(cb.get("failure_count", 0))
        )
        
        # Capabilities
        caps = status.get("capabilities", [])
        table.add_row(
            "Capabilities",
            f"{len(caps)} task types"
        )
        
        # Queue
        queue_size = status.get("queue_size", 0)
        table.add_row(
            "Queue Size",
            str(queue_size)
        )
        
        # Fallback
        fallback = status.get("local_fallback_enabled", False)
        fallback_text = "ENABLED" if fallback else "DISABLED"
        table.add_row(
            "Local Fallback",
            fallback_text
        )
        
        return table
    
    async def create_metrics_table(self) -> Table:
        """Create metrics table"""
        try:
            status = await self.orchestrator.get_status()
            metrics = status.get("metrics", {})
            
            table = Table(title="Performance Metrics", box=box.ROUNDED, show_header=False)
            table.add_column("Metric", style="yellow", width=25)
            table.add_column("Value", style="white")
            
            total = metrics.get("total_tasks", 0)
            completed = metrics.get("completed_tasks", 0)
            failed = metrics.get("failed_tasks", 0)
            avg_duration = metrics.get("avg_duration_ms", 0)
            
            table.add_row("Total Tasks", str(total))
            table.add_row("Completed", f"✅ {completed}")
            table.add_row("Failed", f"❌ {failed}")
            
            if total > 0:
                success_rate = (completed / total) * 100
                table.add_row("Success Rate", f"{success_rate:.1f}%")
            
            table.add_row("Avg Duration", f"{avg_duration:.2f}ms")
            
            if "last_reset" in metrics:
                table.add_row("Last Reset", metrics["last_reset"])
            
            return table
        
        except Exception as e:
            table = Table(title="Performance Metrics", box=box.ROUNDED)
            table.add_column("Error", style="red")
            table.add_row(f"Could not fetch metrics: {e}")
            return table
    
    async def create_capabilities_table(self) -> Table:
        """Create capabilities table"""
        status = await self.orchestrator.get_status()
        caps = status.get("capabilities", [])
        
        table = Table(title=f"Capabilities ({len(caps)} available)", box=box.ROUNDED)
        table.add_column("Task Type", style="green")
        table.add_column("Status", style="white")
        
        for cap in sorted(caps):
            table.add_row(cap, "✅ Ready")
        
        if not caps:
            table.add_row("No capabilities", "❌")
        
        return table
    
    async def render_dashboard(self) -> Layout:
        """Render complete dashboard"""
        layout = Layout()
        
        # Create header
        header = self.create_header()
        
        # Create tables
        status_table = await self.create_status_table()
        metrics_table = await self.create_metrics_table()
        capabilities_table = await self.create_capabilities_table()
        
        # Build layout
        layout.split_column(
            Layout(header, size=5),
            Layout().split_row(
                Layout(status_table),
                Layout(metrics_table)
            ),
            Layout(capabilities_table)
        )
        
        return layout
    
    async def run(self):
        """Run dashboard with live updates"""
        self.console.clear()
        self.console.print("[bold cyan]🚀 Starting Cloud Agent Dashboard...[/bold cyan]\n")
        
        try:
            await self.initialize()
            self.console.print("[green]✅ Dashboard initialized[/green]\n")
            
            with Live(await self.render_dashboard(), refresh_per_second=0.5, console=self.console) as live:
                while True:
                    await asyncio.sleep(self.refresh_interval)
                    live.update(await self.render_dashboard())
        
        except KeyboardInterrupt:
            self.console.print("\n[yellow]⚠️  Dashboard stopped by user[/yellow]")
        except Exception as e:
            self.console.print(f"\n[red]❌ Dashboard error: {e}[/red]")

# ═══════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════

async def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="NOIZYLAB Cloud Agent Monitoring Dashboard"
    )
    parser.add_argument(
        "--endpoint",
        help="Cloud agent endpoint URL",
        default=None
    )
    parser.add_argument(
        "--api-key",
        help="API key for authentication",
        default=None
    )
    parser.add_argument(
        "--refresh",
        type=int,
        default=2,
        help="Refresh interval in seconds (default: 2)"
    )
    
    args = parser.parse_args()
    
    dashboard = CloudAgentDashboard(
        endpoint=args.endpoint,
        api_key=args.api_key
    )
    dashboard.refresh_interval = args.refresh
    
    await dashboard.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Goodbye![/yellow]")
