#!/usr/bin/env python3
"""
GOD Health Monitor - Continuous Background Health Tracking
CB_01 - Fish Music Inc
Logs system health to file for historical analysis
GORUNFREE! 🎸🔥
"""

import subprocess
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

class GODHealth:
    """System health monitor with logging"""

    def __init__(self, log_dir: Optional[Path] = None):
        self.log_dir = log_dir or Path.home() / ".god-health"
        self.log_dir.mkdir(exist_ok=True)
        self.log_file = self.log_dir / f"health_{datetime.now().strftime('%Y%m%d')}.jsonl"

    def run_cmd(self, cmd: str) -> str:
        """Run shell command safely"""
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
            return result.stdout.strip()
        except:
            return ""

    def get_cpu_load(self) -> list:
        """Get load averages"""
        load = self.run_cmd("sysctl -n vm.loadavg").replace("{ ", "").replace(" }", "")
        try:
            return [float(x) for x in load.split()[:3]]
        except:
            return [0.0, 0.0, 0.0]

    def get_memory(self) -> dict:
        """Get memory stats"""
        total = int(self.run_cmd("sysctl -n hw.memsize"))
        total_gb = total / (1024**3)

        vm = self.run_cmd("vm_stat")
        free_pages = 0
        for line in vm.split('\n'):
            if 'Pages free' in line:
                try:
                    free_pages = int(line.split(':')[1].strip().replace('.', ''))
                except:
                    pass

        free_gb = (free_pages * 4096) / (1024**3)
        used_gb = total_gb - free_gb

        return {
            "total_gb": round(total_gb, 1),
            "used_gb": round(used_gb, 1),
            "free_gb": round(free_gb, 1),
            "percent": round((used_gb / total_gb) * 100, 1) if total_gb > 0 else 0
        }

    def get_disk(self) -> dict:
        """Get disk usage"""
        df = self.run_cmd("df -h / | tail -1").split()
        if len(df) >= 5:
            return {
                "total": df[1],
                "used": df[2],
                "available": df[3],
                "percent": int(df[4].replace('%', ''))
            }
        return {}

    def get_top_cpu_process(self) -> str:
        """Get highest CPU process"""
        ps = self.run_cmd("ps -Aceo %cpu,comm | sort -rn | head -2 | tail -1")
        return ps.strip() if ps else "unknown"

    def snapshot(self) -> dict:
        """Take full system snapshot"""
        return {
            "timestamp": datetime.now().isoformat(),
            "load": self.get_cpu_load(),
            "memory": self.get_memory(),
            "disk": self.get_disk(),
            "top_process": self.get_top_cpu_process()
        }

    def log_snapshot(self, data: dict):
        """Append snapshot to daily log"""
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(data) + '\n')

    def check_alerts(self, data: dict) -> list:
        """Check for alert conditions"""
        alerts = []

        # High memory
        if data['memory']['percent'] > 90:
            alerts.append(f"🚨 CRITICAL: Memory at {data['memory']['percent']}%")
        elif data['memory']['percent'] > 80:
            alerts.append(f"⚠️  HIGH: Memory at {data['memory']['percent']}%")

        # High CPU load
        if data['load'][0] > 20:
            alerts.append(f"🚨 CRITICAL: CPU load {data['load'][0]}")
        elif data['load'][0] > 10:
            alerts.append(f"⚠️  HIGH: CPU load {data['load'][0]}")

        # Disk space
        if data['disk'].get('percent', 0) > 95:
            alerts.append(f"🚨 CRITICAL: Disk at {data['disk']['percent']}%")
        elif data['disk'].get('percent', 0) > 90:
            alerts.append(f"⚠️  LOW: Disk space at {data['disk']['percent']}%")

        return alerts

    def run_daemon(self, interval: int = 60):
        """Run as background daemon, logging every interval seconds"""
        print(f"🔥 GOD Health Monitor started")
        print(f"📁 Logging to: {self.log_file}")
        print(f"⏱️  Interval: {interval}s")
        print(f"Press Ctrl+C to stop\n")

        while True:
            try:
                data = self.snapshot()
                self.log_snapshot(data)

                # Check alerts
                alerts = self.check_alerts(data)

                # Status line
                mem = data['memory']
                load = data['load']
                ts = datetime.now().strftime("%H:%M:%S")

                status = f"[{ts}] Load: {load[0]:.1f} | RAM: {mem['percent']}% | "

                if alerts:
                    print(f"\033[1;33m{status}{alerts[0]}\033[0m")
                else:
                    print(f"\033[0;32m{status}✅ Healthy\033[0m")

                time.sleep(interval)

            except KeyboardInterrupt:
                print(f"\n\n✅ Health monitor stopped")
                print(f"📁 Logs saved to: {self.log_file}")
                break

    def report(self, hours: int = 24) -> dict:
        """Generate health report from logs"""
        snapshots = []

        # Read today's log
        if self.log_file.exists():
            with open(self.log_file, 'r') as f:
                for line in f:
                    try:
                        snapshots.append(json.loads(line))
                    except:
                        pass

        if not snapshots:
            return {"error": "No data available"}

        # Calculate stats
        loads = [s['load'][0] for s in snapshots]
        mems = [s['memory']['percent'] for s in snapshots]

        return {
            "period": f"Last {len(snapshots)} snapshots",
            "cpu_load": {
                "avg": round(sum(loads) / len(loads), 2),
                "max": round(max(loads), 2),
                "min": round(min(loads), 2)
            },
            "memory": {
                "avg": round(sum(mems) / len(mems), 1),
                "max": round(max(mems), 1),
                "min": round(min(mems), 1)
            },
            "snapshots": len(snapshots)
        }


def main():
    import sys

    health = GODHealth()

    if len(sys.argv) > 1:
        cmd = sys.argv[1]

        if cmd in ['-d', '--daemon']:
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 60
            health.run_daemon(interval)

        elif cmd in ['-r', '--report']:
            report = health.report()
            print("\n🔥 GOD HEALTH REPORT")
            print("=" * 40)
            print(json.dumps(report, indent=2))
            print("\nGORUNFREE! 🎸🔥\n")

        elif cmd in ['-s', '--snapshot']:
            data = health.snapshot()
            alerts = health.check_alerts(data)
            print("\n🔥 GOD HEALTH SNAPSHOT")
            print("=" * 40)
            print(json.dumps(data, indent=2))
            if alerts:
                print("\n⚠️  ALERTS:")
                for a in alerts:
                    print(f"  {a}")
            print("\nGORUNFREE! 🎸🔥\n")

        elif cmd in ['-h', '--help']:
            print("""
🔥 GOD Health Monitor - CB_01

Usage:
  python3 god-health.py              # Single snapshot with alerts
  python3 god-health.py -s           # Same as above
  python3 god-health.py -d [secs]    # Daemon mode (default 60s interval)
  python3 god-health.py -r           # Generate report from logs

Options:
  -s, --snapshot    Take single health snapshot
  -d, --daemon      Run as daemon (Ctrl+C to stop)
  -r, --report      Generate report from today's logs
  -h, --help        Show this help

GORUNFREE! 🎸🔥
""")
        else:
            print(f"Unknown command: {cmd}")
            print("Use -h for help")
    else:
        # Default: single snapshot
        data = health.snapshot()
        alerts = health.check_alerts(data)

        print("\n🔥 GOD HEALTH SNAPSHOT")
        print("=" * 40)
        print(f"Time: {data['timestamp']}")
        print(f"Load: {data['load'][0]:.1f}, {data['load'][1]:.1f}, {data['load'][2]:.1f}")
        print(f"Memory: {data['memory']['used_gb']}GB / {data['memory']['total_gb']}GB ({data['memory']['percent']}%)")
        print(f"Disk: {data['disk'].get('used', '?')} / {data['disk'].get('total', '?')} ({data['disk'].get('percent', '?')}%)")
        print(f"Top Process: {data['top_process']}")

        if alerts:
            print("\n⚠️  ALERTS:")
            for a in alerts:
                print(f"  {a}")
        else:
            print("\n✅ All systems healthy")

        print("\nGORUNFREE! 🎸🔥\n")


if __name__ == "__main__":
    main()
