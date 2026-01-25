#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   🔧 NOIZYLAB CLOUD AGENT CLI                                            ║
║                                                                           ║
║   Full-featured command-line interface for managing and monitoring      ║
║   the NOIZYLAB Cloud Agent system                                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional

import click

# ═══════════════════════════════════════════════════════════════════════════
# GLOBAL CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

CONFIG_FILE = Path.home() / ".cloudagent" / "config.json"
DEFAULT_CONFIG = {
    "endpoint": "https://noizylab.rsplowman.workers.dev",
    "api_key": "",
    "timeout": 30
}

def load_config() -> dict:
    """Load configuration from file"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return DEFAULT_CONFIG.copy()

def save_config(config: dict):
    """Save configuration to file"""
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

# ═══════════════════════════════════════════════════════════════════════════
# CLI GROUP
# ═══════════════════════════════════════════════════════════════════════════

@click.group()
@click.version_option(version="3.0.0", prog_name="cloudagent")
def cli():
    """
    🚀 NOIZYLAB Cloud Agent CLI - Enterprise Edition
    
    Manage and monitor your cloud agent infrastructure with ease.
    """
    pass

# ═══════════════════════════════════════════════════════════════════════════
# INIT COMMAND
# ═══════════════════════════════════════════════════════════════════════════

@cli.command()
@click.option("--endpoint", prompt="Cloud Agent Endpoint", help="Worker endpoint URL")
@click.option("--api-key", prompt="API Key", hide_input=True, help="Authentication API key")
@click.option("--timeout", default=30, help="Request timeout in seconds")
def init(endpoint: str, api_key: str, timeout: int):
    """
    Initialize cloud agent configuration
    
    Sets up the configuration file with your endpoint and credentials.
    """
    config = {
        "endpoint": endpoint.rstrip("/"),
        "api_key": api_key,
        "timeout": timeout
    }
    
    save_config(config)
    
    click.echo("✅ Configuration saved!")
    click.echo(f"📁 Config file: {CONFIG_FILE}")
    click.echo(f"🔗 Endpoint: {endpoint}")
    click.echo(f"⏱️  Timeout: {timeout}s")

# ═══════════════════════════════════════════════════════════════════════════
# TEST COMMAND
# ═══════════════════════════════════════════════════════════════════════════

@cli.command()
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
def test(verbose: bool):
    """
    Run comprehensive test suite
    
    Executes all cloud agent tests and displays results.
    """
    click.echo("🧪 Running test suite...")
    click.echo()
    
    # Import and run tests
    try:
        import test_cloud_agent
        
        # Set verbose mode
        if verbose:
            import logging
            logging.basicConfig(level=logging.DEBUG)
        
        # Run async tests
        import asyncio
        
        async def run_all_tests():
            results = []
            
            # List of test functions
            tests = [
                ("Health Check", test_cloud_agent.test_health),
                ("Capabilities", test_cloud_agent.test_capabilities),
                ("Echo Task", test_cloud_agent.test_echo),
                ("Batch Operations", test_cloud_agent.test_batch),
            ]
            
            for name, test_func in tests:
                try:
                    click.echo(f"Running: {name}...", nl=False)
                    result = await test_func()
                    if result:
                        click.echo(" ✅")
                        results.append((name, True))
                    else:
                        click.echo(" ❌")
                        results.append((name, False))
                except Exception as e:
                    click.echo(f" ❌ ({e})")
                    results.append((name, False))
            
            return results
        
        results = asyncio.run(run_all_tests())
        
        # Summary
        click.echo()
        passed = sum(1 for _, success in results if success)
        total = len(results)
        
        if passed == total:
            click.echo(f"✅ All {total} tests passed!")
        else:
            click.echo(f"⚠️  {passed}/{total} tests passed")
            sys.exit(1)
    
    except ImportError:
        click.echo("❌ test_cloud_agent.py not found")
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ Test suite failed: {e}")
        sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════
# MONITOR COMMAND
# ═══════════════════════════════════════════════════════════════════════════

@cli.command()
@click.option("--refresh", "-r", default=2, help="Refresh interval in seconds")
def monitor(refresh: int):
    """
    Launch real-time monitoring dashboard
    
    Opens an interactive terminal dashboard showing live metrics.
    """
    click.echo("📊 Launching monitoring dashboard...")
    
    try:
        import subprocess
        subprocess.run([sys.executable, "cloud_agent_dashboard.py", "--refresh", str(refresh)])
    except FileNotFoundError:
        click.echo("❌ cloud_agent_dashboard.py not found")
        sys.exit(1)
    except KeyboardInterrupt:
        click.echo("\n👋 Dashboard closed")

# ═══════════════════════════════════════════════════════════════════════════
# ANALYTICS COMMAND
# ═══════════════════════════════════════════════════════════════════════════

@cli.command()
@click.option("--days", "-d", default=1, help="Number of days to analyze")
@click.option("--format", "-f", type=click.Choice(["text", "json", "html"]), default="text")
@click.option("--output", "-o", help="Output file (for json/html formats)")
def analytics(days: int, format: str, output: Optional[str]):
    """
    Show analytics and performance insights
    
    Analyzes task execution patterns and provides optimization recommendations.
    """
    click.echo(f"📊 Analyzing last {days} day(s)...")
    
    try:
        from cloud_agent_analytics import CloudAgentAnalytics
        from datetime import datetime, timedelta
        
        analytics_engine = CloudAgentAnalytics()
        end_time = datetime.now()
        start_time = end_time - timedelta(days=days)
        
        summary = analytics_engine.get_summary(start_time, end_time)
        
        if format == "text":
            click.echo("\n" + "="*70)
            click.echo("ANALYTICS SUMMARY")
            click.echo("="*70)
            click.echo(f"Period: {summary.period_start} to {summary.period_end}")
            click.echo(f"\nTotal Tasks: {summary.total_tasks}")
            click.echo(f"Successful: {summary.successful_tasks} ({summary.successful_tasks/summary.total_tasks*100 if summary.total_tasks > 0 else 0:.1f}%)")
            click.echo(f"Failed: {summary.failed_tasks}")
            click.echo(f"\nAvg Duration: {summary.avg_duration_ms}ms")
            click.echo(f"Median Duration: {summary.median_duration_ms}ms")
            click.echo(f"P95 Duration: {summary.p95_duration_ms}ms")
            click.echo(f"Tasks/Hour: {summary.tasks_per_hour:.1f}")
            
            if summary.most_common_task_types:
                click.echo(f"\nMost Common Task Types:")
                for task_type, count in summary.most_common_task_types:
                    click.echo(f"  - {task_type}: {count}")
            
            # Cost estimation
            costs = analytics_engine.get_cost_estimation(start_time, end_time)
            click.echo(f"\nCost Estimation:")
            click.echo(f"  Monthly (Projected): ${costs['monthly_cost_usd']:.2f}")
            click.echo(f"  Cost per Task: ${costs['cost_per_task_usd']:.6f}")
            
            if costs['recommendations']:
                click.echo(f"\n💡 Recommendations:")
                for rec in costs['recommendations']:
                    click.echo(f"  - {rec}")
        
        elif format == "json":
            output_file = output or f"analytics_{int(time.time())}.json"
            analytics_engine.export_to_json(output_file, start_time, end_time)
            click.echo(f"✅ Analytics exported to {output_file}")
        
        elif format == "html":
            output_file = output or f"analytics_{int(time.time())}.html"
            analytics_engine.generate_html_report(output_file, start_time, end_time)
            click.echo(f"✅ HTML report generated: {output_file}")
    
    except ImportError as e:
        click.echo(f"❌ Analytics module not available: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ Analytics failed: {e}")
        sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════
# BENCHMARK COMMAND
# ═══════════════════════════════════════════════════════════════════════════

@cli.command()
@click.option("--concurrent", "-c", default=10, help="Number of concurrent requests")
@click.option("--total", "-t", default=100, help="Total number of requests")
@click.option("--task-type", default="echo", help="Task type to benchmark")
def benchmark(concurrent: int, total: int, task_type: str):
    """
    Run performance benchmarks
    
    Stress-test the cloud agent with concurrent requests.
    """
    click.echo(f"🏎️  Running benchmark...")
    click.echo(f"  Concurrent: {concurrent}")
    click.echo(f"  Total Requests: {total}")
    click.echo(f"  Task Type: {task_type}")
    click.echo()
    
    config = load_config()
    
    try:
        from cloud_agent_client import CloudAgentClient
        import asyncio
        import time
        
        async def run_benchmark():
            client = CloudAgentClient(
                endpoint=config["endpoint"],
                api_key=config["api_key"],
                timeout=config["timeout"]
            )
            
            start_time = time.time()
            
            # Create task batches
            tasks = []
            for i in range(total):
                task = client.delegate_task(
                    task_type=task_type,
                    task_data={"message": f"Benchmark request {i}"}
                )
                tasks.append(task)
                
                # Execute in batches
                if len(tasks) >= concurrent:
                    await asyncio.gather(*tasks, return_exceptions=True)
                    tasks = []
            
            # Execute remaining tasks
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)
            
            duration = time.time() - start_time
            
            click.echo(f"\n📊 Benchmark Results:")
            click.echo(f"  Duration: {duration:.2f}s")
            click.echo(f"  Throughput: {total/duration:.2f} req/s")
            click.echo(f"  Avg Latency: {(duration/total)*1000:.2f}ms")
        
        asyncio.run(run_benchmark())
    
    except Exception as e:
        click.echo(f"❌ Benchmark failed: {e}")
        sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════
# DEPLOY COMMAND
# ═══════════════════════════════════════════════════════════════════════════

@cli.command()
@click.option("--env", default="production", help="Deployment environment")
def deploy(env: str):
    """
    Deploy worker to Cloudflare
    
    Deploys the worker using wrangler CLI.
    """
    click.echo(f"🚀 Deploying to {env}...")
    
    try:
        import subprocess
        
        # Check if wrangler is installed
        result = subprocess.run(["wrangler", "--version"], capture_output=True)
        if result.returncode != 0:
            click.echo("❌ Wrangler CLI not found. Install with: npm install -g wrangler")
            sys.exit(1)
        
        # Deploy
        click.echo("📦 Building and deploying worker...")
        result = subprocess.run(
            ["wrangler", "deploy", "--env", env],
            cwd="workers/noizylab"
        )
        
        if result.returncode == 0:
            click.echo("✅ Deployment successful!")
        else:
            click.echo("❌ Deployment failed")
            sys.exit(1)
    
    except Exception as e:
        click.echo(f"❌ Deployment error: {e}")
        sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════
# EXPORT COMMAND
# ═══════════════════════════════════════════════════════════════════════════

@cli.command()
@click.option("--format", "-f", type=click.Choice(["json", "csv"]), default="json")
@click.option("--output", "-o", required=True, help="Output file path")
@click.option("--days", "-d", default=7, help="Number of days to export")
def export(format: str, output: str, days: int):
    """
    Export analytics data
    
    Exports historical data in JSON or CSV format.
    """
    click.echo(f"📤 Exporting {days} days of data...")
    
    try:
        from cloud_agent_analytics import CloudAgentAnalytics
        from datetime import datetime, timedelta
        
        analytics = CloudAgentAnalytics()
        end_time = datetime.now()
        start_time = end_time - timedelta(days=days)
        
        if format == "json":
            analytics.export_to_json(output, start_time, end_time)
        else:
            analytics.export_to_csv(output, start_time, end_time)
        
        click.echo(f"✅ Data exported to {output}")
    
    except Exception as e:
        click.echo(f"❌ Export failed: {e}")
        sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════
# DOCS COMMAND
# ═══════════════════════════════════════════════════════════════════════════

@cli.command()
def docs():
    """
    Open documentation in browser
    
    Opens the comprehensive cloud agent documentation.
    """
    import webbrowser
    
    # Check for local docs
    docs_path = Path("CLOUD_AGENT_GUIDE.md")
    if docs_path.exists():
        click.echo("📚 Opening documentation...")
        webbrowser.open(f"file://{docs_path.absolute()}")
    else:
        click.echo("📚 Documentation not found locally")
        click.echo("Check: CLOUD_AGENT_GUIDE.md")

# ═══════════════════════════════════════════════════════════════════════════
# STATUS COMMAND
# ═══════════════════════════════════════════════════════════════════════════

@cli.command()
def status():
    """
    Show current system status
    
    Displays health and configuration information.
    """
    config = load_config()
    
    click.echo("🔍 Cloud Agent Status")
    click.echo("="*70)
    click.echo(f"\n📍 Configuration:")
    click.echo(f"  Endpoint: {config.get('endpoint', 'Not configured')}")
    click.echo(f"  API Key: {'***' + config.get('api_key', '')[-4:] if config.get('api_key') else 'Not set'}")
    click.echo(f"  Timeout: {config.get('timeout', 30)}s")
    
    # Check connectivity
    click.echo(f"\n🏥 Health Check:")
    
    try:
        from cloud_agent_client import CloudAgentClient
        import asyncio
        
        async def check_health():
            client = CloudAgentClient(
                endpoint=config["endpoint"],
                api_key=config["api_key"]
            )
            return await client.health_check()
        
        health = asyncio.run(check_health())
        
        if health.get("status") == "healthy":
            click.echo("  ✅ Cloud agent is healthy")
            click.echo(f"  Version: {health.get('version', 'unknown')}")
            click.echo(f"  Agent: {health.get('agent', 'unknown')}")
        else:
            click.echo("  ⚠️  Cloud agent status unknown")
    
    except Exception as e:
        click.echo(f"  ❌ Cannot reach cloud agent: {e}")

# ═══════════════════════════════════════════════════════════════════════════
# MAIN ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Main CLI entry point"""
    try:
        cli()
    except KeyboardInterrupt:
        click.echo("\n👋 Interrupted by user")
        sys.exit(130)
    except Exception as e:
        click.echo(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
