#!/usr/bin/env python3
"""
NoizyLab CLI - Command Line Interface
======================================
Powerful CLI for managing all NoizyLab services
"""

import click
import requests
import json
import subprocess
import time
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich import print as rprint
from datetime import datetime

console = Console()

# Service configurations
SERVICES = {
    "slack-api": {"port": 8003, "health": "/health", "name": "Slack API"},
    "slack-dash": {"port": 8506, "health": "/", "name": "Slack Dashboard"},
    "network-agent": {"port": 8005, "health": "/health", "name": "Network Agent"},
    "master-dash": {"port": 8501, "health": "/", "name": "Master Dashboard"},
}


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """🎛️ NoizyLab Command Line Interface"""
    pass


@cli.command()
def status():
    """Check status of all services"""
    console.print("\n[bold cyan]🎛️ NoizyLab System Status[/bold cyan]\n")
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Service", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Port", justify="right")
    table.add_column("Response Time", justify="right")
    
    for service_id, config in SERVICES.items():
        port = config["port"]
        url = f"http://localhost:{port}{config['health']}"
        
        try:
            start = time.time()
            response = requests.get(url, timeout=2)
            elapsed = (time.time() - start) * 1000
            
            if response.status_code == 200:
                status_icon = "✅ Running"
                status_style = "green"
            else:
                status_icon = "⚠️ Warning"
                status_style = "yellow"
            
            table.add_row(
                config["name"],
                f"[{status_style}]{status_icon}[/{status_style}]",
                str(port),
                f"{elapsed:.0f}ms"
            )
        except:
            table.add_row(
                config["name"],
                "[red]🔴 Down[/red]",
                str(port),
                "—"
            )
    
    console.print(table)
    console.print()


@cli.command()
@click.option('--service', type=click.Choice(['all', 'slack', 'network', 'dashboard']), default='all')
def start(service):
    """Start NoizyLab services"""
    noizylab_root = Path("/Users/m2ultra/NOIZYLAB")
    
    if service == 'all':
        console.print("[bold green]🚀 Starting all NoizyLab services...[/bold green]\n")
        subprocess.run([str(noizylab_root / "LAUNCH_NOIZYLAB_COMPLETE.sh")])
    elif service == 'slack':
        console.print("[bold green]💬 Starting Slack services...[/bold green]\n")
        subprocess.run([str(noizylab_root / "integrations/slack/start_slack_services.sh")])
    elif service == 'network':
        console.print("[bold green]🌐 Starting Network Agent...[/bold green]\n")
        subprocess.run([str(noizylab_root / "network/start_network_agent.sh")])
    elif service == 'dashboard':
        console.print("[bold green]🎛️ Starting Master Dashboard...[/bold green]\n")
        subprocess.run(["streamlit", "run", str(noizylab_root / "master-dashboard/master-dashboard.py")])


@cli.command()
def stop():
    """Stop all NoizyLab services"""
    noizylab_root = Path("/Users/m2ultra/NOIZYLAB")
    pid_file = noizylab_root / ".noizylab_pids"
    
    if pid_file.exists():
        console.print("[bold yellow]🛑 Stopping NoizyLab services...[/bold yellow]\n")
        
        with open(pid_file) as f:
            pids = f.read().strip().split()
        
        for pid in pids:
            try:
                subprocess.run(["kill", pid], stderr=subprocess.DEVNULL)
                console.print(f"[green]✅ Stopped PID {pid}[/green]")
            except:
                pass
        
        pid_file.unlink()
        console.print("\n[bold green]✅ All services stopped[/bold green]\n")
    else:
        console.print("[yellow]⚠️ No running services found[/yellow]\n")


@cli.command()
def restart():
    """Restart all services"""
    console.print("[bold cyan]🔄 Restarting NoizyLab services...[/bold cyan]\n")
    
    ctx = click.get_current_context()
    ctx.invoke(stop)
    time.sleep(2)
    ctx.invoke(start, service='all')


@cli.group()
def slack():
    """Slack integration commands"""
    pass


@slack.command('send')
@click.argument('message')
@click.option('--channel', default='#general', help='Slack channel')
@click.option('--level', type=click.Choice(['info', 'success', 'warning', 'error']), default='info')
def slack_send(message, channel, level):
    """Send a message to Slack"""
    try:
        response = requests.post(
            "http://localhost:8003/notify/system-alert",
            json={
                "channel": channel,
                "title": f"{level.upper()} Alert",
                "message": message,
                "level": level
            },
            timeout=5
        )
        
        if response.status_code == 200:
            console.print(f"[green]✅ Message sent to {channel}[/green]")
        else:
            console.print(f"[red]❌ Failed to send message[/red]")
    except:
        console.print("[red]❌ Slack service not available[/red]")


@slack.command('channels')
def slack_channels():
    """List Slack channels"""
    import sqlite3
    
    db_path = Path("/Users/m2ultra/NOIZYLAB/integrations/slack/slack_data.db")
    
    if not db_path.exists():
        console.print("[red]❌ Slack database not found[/red]")
        return
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, member_count, is_private FROM slack_channels ORDER BY member_count DESC")
    channels = cursor.fetchall()
    conn.close()
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Channel", style="cyan")
    table.add_column("Members", justify="right")
    table.add_column("Type")
    
    for name, members, is_private in channels:
        channel_type = "🔒 Private" if is_private else "🌐 Public"
        table.add_row(f"#{name}", str(members), channel_type)
    
    console.print("\n[bold cyan]📺 Slack Channels[/bold cyan]\n")
    console.print(table)
    console.print()


@slack.command('stats')
def slack_stats():
    """Show Slack statistics"""
    import sqlite3
    
    db_path = Path("/Users/m2ultra/NOIZYLAB/integrations/slack/slack_data.db")
    
    if not db_path.exists():
        console.print("[red]❌ Slack database not found[/red]")
        return
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Get stats
    cursor.execute("SELECT COUNT(*) FROM slack_notifications")
    total_notifications = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM slack_notifications WHERE sent_at > datetime('now', '-24 hours')")
    notifications_24h = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM slack_channels")
    channels = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM slack_users WHERE is_bot = 0")
    users = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM slack_commands")
    commands = cursor.fetchone()[0]
    
    conn.close()
    
    panel = Panel(
        f"""[cyan]Total Notifications:[/cyan] [bold]{total_notifications}[/bold]
[cyan]Last 24 Hours:[/cyan] [bold]{notifications_24h}[/bold]
[cyan]Channels:[/cyan] [bold]{channels}[/bold]
[cyan]Users:[/cyan] [bold]{users}[/bold]
[cyan]Commands Executed:[/cyan] [bold]{commands}[/bold]""",
        title="[bold magenta]💬 Slack Statistics[/bold magenta]",
        border_style="cyan"
    )
    
    console.print("\n")
    console.print(panel)
    console.print()


@cli.group()
def network():
    """Network monitoring commands"""
    pass


@network.command('ports')
def network_ports():
    """Show port status"""
    try:
        response = requests.get("http://localhost:8005/ports", timeout=5)
        
        if response.status_code != 200:
            console.print("[red]❌ Network agent not available[/red]")
            return
        
        ports = response.json().get("ports", {})
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Port", justify="center")
        table.add_column("Status", style="green")
        table.add_column("Device")
        table.add_column("IP Address")
        
        for port_num, port_data in sorted(ports.items(), key=lambda x: int(x[0])):
            status = port_data.get("link_status", "down")
            device_data = port_data.get("device")
            
            status_icon = "🟢 Up" if status == "up" else "⚪ Down"
            device_name = device_data.get("hostname", "—") if device_data else "—"
            device_ip = device_data.get("ip", "—") if device_data else "—"
            
            table.add_row(
                str(port_num),
                status_icon,
                device_name,
                device_ip
            )
        
        console.print("\n[bold cyan]🔌 DGS1210 Port Status[/bold cyan]\n")
        console.print(table)
        console.print()
        
    except:
        console.print("[red]❌ Network agent not available[/red]")


@network.command('devices')
def network_devices():
    """Show connected devices"""
    try:
        response = requests.get("http://localhost:8005/devices", timeout=5)
        
        if response.status_code != 200:
            console.print("[red]❌ Network agent not available[/red]")
            return
        
        data = response.json()
        devices = data.get("devices", [])
        
        if not devices:
            console.print("[yellow]⚠️ No devices connected[/yellow]")
            return
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Hostname")
        table.add_column("IP Address")
        table.add_column("Port", justify="center")
        table.add_column("MAC Address")
        table.add_column("Vendor")
        
        for device in devices:
            table.add_row(
                device.get("hostname", "Unknown"),
                device.get("ip_address", "—"),
                str(device.get("port", "—")),
                device.get("mac_address", "—"),
                device.get("vendor", "—")
            )
        
        console.print(f"\n[bold cyan]🌐 Connected Devices ({len(devices)})[/bold cyan]\n")
        console.print(table)
        console.print()
        
    except:
        console.print("[red]❌ Network agent not available[/red]")


@network.command('mc96')
def network_mc96():
    """Show MC96 devices"""
    try:
        response = requests.get("http://localhost:8005/mc96/devices", timeout=5)
        
        if response.status_code != 200:
            console.print("[red]❌ Network agent not available[/red]")
            return
        
        data = response.json()
        devices = data.get("devices", {})
        
        if not devices:
            console.print("[yellow]⚠️ No MC96 devices connected[/yellow]")
            return
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Port", justify="center")
        table.add_column("Hostname")
        table.add_column("IP Address")
        table.add_column("Handshake")
        table.add_column("Response Time")
        
        for port, device_data in devices.items():
            device = device_data.get("device", {})
            handshake = device_data.get("handshake", {})
            
            success = handshake.get("success", False)
            handshake_status = "✅ Success" if success else "❌ Failed"
            response_time = f"{handshake.get('response_time', 0):.2f}s"
            
            table.add_row(
                port,
                device.get("hostname", "Unknown"),
                device.get("ip", "—"),
                handshake_status,
                response_time
            )
        
        console.print(f"\n[bold cyan]🔌 MC96 Devices ({len(devices)})[/bold cyan]\n")
        console.print(table)
        console.print()
        
    except:
        console.print("[red]❌ Network agent not available[/red]")


@network.command('universe')
@click.argument('action', type=click.Choice(['enable', 'status', 'visualize', 'list']))
def network_universe(action):
    """🌐 MC96 Universe mesh network management"""
    import sys
    sys.path.append('/Users/m2ultra/NOIZYLAB')
    from network.mc96_tunnel_manager import MC96TunnelManager
    
    manager = MC96TunnelManager()
    
    if action == 'enable':
        console.print("[bold cyan]🌐✨ ENABLING MC96 UNIVERSE! ✨🌐[/bold cyan]\n")
        result = manager.enable_universe_communication()
        
        if result.get("success"):
            console.print(f"\n[bold green]✅ MC96 Universe is ONLINE![/bold green]")
            console.print(f"   Devices: {result['device_count']}")
            console.print(f"   Tunnels: {result['tunnel_count']}")
        else:
            console.print("[yellow]⚠️  Could not create universe[/yellow]")
    
    elif action == 'status':
        console.print("[cyan]🌐 MC96 Universe Status:[/cyan]\n")
        status = manager.get_universe_status()
        
        console.print(f"Status: {status['status']}")
        console.print(f"Devices: {status['total_devices']}")
        console.print(f"Tunnels: {status['active_tunnels']}")
        console.print(f"Avg Latency: {status['avg_latency_ms']:.2f}ms")
        console.print()
    
    elif action == 'visualize':
        manager.visualize_mesh()
    
    elif action == 'list':
        tunnels = manager.list_tunnels()
        
        if not tunnels:
            console.print("[yellow]No active tunnels[/yellow]")
            return
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Source")
        table.add_column("Destination")
        table.add_column("Type")
        table.add_column("Latency")
        table.add_column("Status")
        
        for tunnel in tunnels:
            table.add_row(
                tunnel['source'],
                tunnel['destination'],
                tunnel['type'],
                f"{tunnel['latency_ms']:.2f}ms" if tunnel['latency_ms'] > 0 else "—",
                "🟢 Active" if tunnel['status'] == 'active' else "🔴 Inactive"
            )
        
        console.print(f"\n[bold cyan]🌐 MC96 Universe Tunnels ({len(tunnels)})[/bold cyan]\n")
        console.print(table)
        console.print()


@network.command('handshake')
@click.argument('port', type=int)
def network_handshake(port):
    """Force handshake on port"""
    console.print(f"[cyan]🤝 Initiating handshake on port {port}...[/cyan]")
    
    try:
        response = requests.post(
            "http://localhost:8005/handshake",
            json={"port": port},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get("success"):
                console.print(f"[green]✅ Handshake successful![/green]")
                console.print(f"   Device: {data.get('device', {}).get('hostname', 'Unknown')}")
                console.print(f"   IP: {data.get('device', {}).get('ip', '—')}")
                console.print(f"   Type: {data.get('handshake_type', '—')}")
                console.print(f"   Response Time: {data.get('response_time', 0):.2f}s")
            else:
                console.print(f"[red]❌ Handshake failed[/red]")
        else:
            console.print(f"[red]❌ No device on port {port}[/red]")
            
    except:
        console.print("[red]❌ Network agent not available[/red]")


@network.command('jumbo')
@click.argument('action', type=click.Choice(['detect', 'enable', 'test', 'hotrod']))
@click.option('--interface', help='Network interface (e.g., en0)')
@click.option('--ip', help='Target IP address')
def network_jumbo(action, interface, ip):
    """🔥 Jumbo frame management (HOT ROD MODE!)"""
    import sys
    sys.path.append('/Users/m2ultra/NOIZYLAB')
    from network.jumbo_frame_manager import JumboFrameManager
    
    manager = JumboFrameManager()
    
    if action == 'detect':
        console.print("[cyan]🔍 Detecting MTU settings...[/cyan]\n")
        manager.detect_current_mtu()
    
    elif action == 'enable':
        if not interface:
            console.print("[red]❌ Please specify --interface[/red]")
        else:
            console.print(f"[cyan]🔥 Enabling jumbo frames on {interface}...[/cyan]\n")
            manager.enable_jumbo_frames(interface)
    
    elif action == 'test':
        if not ip:
            console.print("[red]❌ Please specify --ip[/red]")
        else:
            console.print(f"[cyan]🧪 Testing MTU against {ip}...[/cyan]\n")
            manager.test_jumbo_frames(ip)
    
    elif action == 'hotrod':
        console.print("[bold red]🔥🔥🔥 HOT ROD MODE ACTIVATED! 🔥🔥🔥[/bold red]\n")
        result = manager.hot_rod_network()
        
        if result['interfaces_configured'] or result['mc96_devices_configured']:
            console.print("\n[bold green]✅ NETWORK TURBOCHARGED![/bold green]")
        else:
            console.print("\n[yellow]⚠️  Manual configuration may be needed[/yellow]")


@cli.command()
def dashboard():
    """Open Master Dashboard in browser"""
    console.print("[cyan]🎛️ Opening Master Dashboard...[/cyan]")
    subprocess.run(["open", "http://localhost:8501"])


@cli.command()
def logs():
    """View recent logs"""
    import sqlite3
    
    # Slack logs
    slack_db = Path("/Users/m2ultra/NOIZYLAB/integrations/slack/slack_data.db")
    
    console.print("\n[bold cyan]📋 Recent Slack Notifications[/bold cyan]\n")
    
    if slack_db.exists():
        conn = sqlite3.connect(str(slack_db))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT channel, message, status, sent_at 
            FROM slack_notifications 
            ORDER BY sent_at DESC 
            LIMIT 10
        """)
        
        for channel, message, status, sent_at in cursor.fetchall():
            timestamp = sent_at.split('.')[0] if sent_at else '—'
            console.print(f"[dim]{timestamp}[/dim] [{channel}] {message[:60]}...")
        
        conn.close()
    else:
        console.print("[yellow]No Slack logs found[/yellow]")
    
    console.print()


@cli.command()
def health():
    """Detailed health check"""
    console.print("\n[bold cyan]🏥 System Health Check[/bold cyan]\n")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        
        task = progress.add_task("Checking services...", total=None)
        
        all_healthy = True
        
        for service_id, config in SERVICES.items():
            port = config["port"]
            url = f"http://localhost:{port}{config['health']}"
            
            try:
                response = requests.get(url, timeout=2)
                if response.status_code == 200:
                    console.print(f"[green]✅ {config['name']} - Healthy[/green]")
                else:
                    console.print(f"[yellow]⚠️ {config['name']} - Responding with errors[/yellow]")
                    all_healthy = False
            except:
                console.print(f"[red]❌ {config['name']} - Not responding[/red]")
                all_healthy = False
        
        progress.stop()
    
    if all_healthy:
        console.print("\n[bold green]🎉 All systems healthy![/bold green]\n")
    else:
        console.print("\n[bold yellow]⚠️ Some systems need attention[/bold yellow]\n")


@cli.command()
def config():
    """Show current configuration"""
    import os
    
    panel_content = []
    
    # Slack config
    slack_token = os.getenv("SLACK_BOT_TOKEN")
    slack_secret = os.getenv("SLACK_SIGNING_SECRET")
    
    panel_content.append("[bold]Slack Configuration:[/bold]")
    panel_content.append(f"  Token: {'✅ Set' if slack_token else '❌ Not set'}")
    panel_content.append(f"  Secret: {'✅ Set' if slack_secret else '❌ Not set'}")
    panel_content.append(f"  Alerts Channel: {os.getenv('SLACK_ALERTS_CHANNEL', '#noizylab-alerts')}")
    panel_content.append(f"  Network Channel: {os.getenv('SLACK_NETWORK_CHANNEL', '#noizylab-network')}")
    panel_content.append("")
    
    # Network config
    panel_content.append("[bold]Network Configuration:[/bold]")
    panel_content.append(f"  Switch IP: {os.getenv('DGS1210_IP', '192.168.1.1')}")
    panel_content.append(f"  SNMP Community: {os.getenv('SNMP_COMMUNITY', 'public')}")
    panel_content.append(f"  MC96 Ports: {os.getenv('MC96_PORTS', '1,2,3')}")
    
    panel = Panel(
        "\n".join(panel_content),
        title="[bold magenta]⚙️ Configuration[/bold magenta]",
        border_style="cyan"
    )
    
    console.print("\n")
    console.print(panel)
    console.print()


@cli.group()
def ai():
    """AI-powered features"""
    pass


@ai.command('chat')
def ai_chat():
    """Start AI chat session"""
    console.print("[bold cyan]🤖 Starting AI Chat...[/bold cyan]\n")
    
    import sys
    sys.path.append('/Users/m2ultra/NOIZYLAB')
    from ai.ai_chat_interface import interactive_chat
    
    interactive_chat()


@ai.command('analyze-logs')
@click.argument('log_file', default='/Users/m2ultra/NOIZYLAB/logs/noizylab.log')
def ai_analyze_logs(log_file):
    """AI-powered log analysis"""
    console.print(f"[bold cyan]🔍 Analyzing {log_file}...[/bold cyan]\n")
    
    import sys
    sys.path.append('/Users/m2ultra/NOIZYLAB')
    from ai.intelligent_log_analyzer import IntelligentLogAnalyzer
    
    analyzer = IntelligentLogAnalyzer()
    results = analyzer.analyze_logs(log_file)
    
    console.print(f"[cyan]Critical:[/cyan] {results['critical_count']}")
    console.print(f"[yellow]Errors:[/yellow] {results['error_count']}")
    console.print(f"[blue]Warnings:[/blue] {results['warning_count']}")
    
    if "ai_analysis" in results:
        console.print("\n[bold green]🤖 AI Analysis:[/bold green]")
        ai = results['ai_analysis']
        console.print(f"  Root Cause: {ai.get('root_cause', 'Unknown')}")
        console.print(f"  Severity: {ai.get('severity', 'Unknown')}")


@ai.command('capacity')
def ai_capacity():
    """AI capacity planning"""
    console.print("[bold cyan]🔮 Running capacity analysis...[/bold cyan]\n")
    
    import sys
    sys.path.append('/Users/m2ultra/NOIZYLAB')
    from ai.predictive_capacity_planner import PredictiveCapacityPlanner
    
    planner = PredictiveCapacityPlanner()
    report = planner.generate_capacity_report()
    
    console.print(report)


@ai.command('ask')
@click.argument('question')
def ai_ask(question):
    """Ask AI a question"""
    import sys
    sys.path.append('/Users/m2ultra/NOIZYLAB')
    from ai.ai_operations_agent import ai_agent
    
    console.print(f"\n[dim]Asking: {question}[/dim]\n")
    
    with console.status("[bold green]Thinking..."):
        answer = ai_agent.natural_query(question)
    
    console.print(f"[bold cyan]🤖 AI:[/bold cyan] {answer}\n")


@cli.command()
def doctor():
    """Run diagnostic check"""
    console.print("\n[bold cyan]👨‍⚕️ Running NoizyLab Doctor...[/bold cyan]\n")
    
    issues = []
    warnings = []
    
    # Check Python
    import sys
    if sys.version_info < (3, 8):
        issues.append("Python version too old (need 3.8+)")
    else:
        console.print("[green]✅ Python version OK[/green]")
    
    # Check environment variables
    import os
    if not os.getenv("SLACK_BOT_TOKEN"):
        warnings.append("SLACK_BOT_TOKEN not set - Slack features disabled")
    else:
        console.print("[green]✅ Slack token configured[/green]")
    
    # Check services
    services_up = 0
    for service_id, config in SERVICES.items():
        try:
            response = requests.get(f"http://localhost:{config['port']}{config['health']}", timeout=1)
            if response.status_code == 200:
                services_up += 1
        except:
            pass
    
    console.print(f"[{'green' if services_up > 0 else 'yellow'}]📊 {services_up}/{len(SERVICES)} services running[/{'green' if services_up > 0 else 'yellow'}]")
    
    # Check databases
    slack_db = Path("/Users/m2ultra/NOIZYLAB/integrations/slack/slack_data.db")
    network_db = Path("/Users/m2ultra/NOIZYLAB/network/network_devices.db")
    
    if slack_db.exists():
        console.print("[green]✅ Slack database exists[/green]")
    else:
        warnings.append("Slack database not found")
    
    if network_db.exists():
        console.print("[green]✅ Network database exists[/green]")
    else:
        warnings.append("Network database not found")
    
    # Summary
    console.print()
    if issues:
        console.print("[bold red]❌ Issues Found:[/bold red]")
        for issue in issues:
            console.print(f"  • {issue}")
    
    if warnings:
        console.print("[bold yellow]⚠️ Warnings:[/bold yellow]")
        for warning in warnings:
            console.print(f"  • {warning}")
    
    if not issues and not warnings:
        console.print("[bold green]🎉 No issues found! System is healthy.[/bold green]")
    
    console.print()


if __name__ == "__main__":
    cli()

