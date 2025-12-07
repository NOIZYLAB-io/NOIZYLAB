#!/usr/bin/env python3
"""
🔊 NOIZYLAB - System Health Monitor
Fish Music Inc - CB_01
🔥 GORUNFREE! 🎸🔥
"""

import psutil
import subprocess
import socket
import time
import json
from datetime import datetime
from pathlib import Path


class SystemHealth:
    """Real-time system health monitoring for GOD (Mac Studio M2 Ultra)"""

    def __init__(self):
        self.history = []
        self.alerts = []

    def cpu(self) -> float:
        """Get CPU usage percentage"""
        return psutil.cpu_percent(interval=0.1)

    def cpu_per_core(self) -> list:
        """Get CPU usage per core"""
        return psutil.cpu_percent(interval=0.1, percpu=True)

    def ram(self) -> dict:
        """Get RAM usage details"""
        mem = psutil.virtual_memory()
        return {
            "percent": mem.percent,
            "used_gb": round(mem.used / (1024**3), 2),
            "total_gb": round(mem.total / (1024**3), 2),
            "available_gb": round(mem.available / (1024**3), 2)
        }

    def disk(self, path: str = "/") -> dict:
        """Get disk usage for specified path"""
        disk = psutil.disk_usage(path)
        return {
            "percent": disk.percent,
            "used_gb": round(disk.used / (1024**3), 2),
            "total_gb": round(disk.total / (1024**3), 2),
            "free_gb": round(disk.free / (1024**3), 2)
        }

    def network_latency(self, host: str = "8.8.8.8", port: int = 53, timeout: float = 3.0) -> float:
        """Measure network latency to host in milliseconds"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            start = time.perf_counter()
            sock.connect((host, port))
            end = time.perf_counter()
            sock.close()
            return round((end - start) * 1000, 2)
        except Exception:
            return -1

    def ping(self, host: str = "8.8.8.8", count: int = 1) -> float:
        """Ping host and return average latency in ms"""
        try:
            result = subprocess.run(
                ["ping", "-c", str(count), host],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                # Parse avg from "min/avg/max/stddev"
                for line in result.stdout.split("\n"):
                    if "avg" in line:
                        parts = line.split("=")[-1].strip().split("/")
                        return float(parts[1])
            return -1
        except Exception:
            return -1

    def network_io(self) -> dict:
        """Get network I/O statistics"""
        io = psutil.net_io_counters()
        return {
            "bytes_sent": io.bytes_sent,
            "bytes_recv": io.bytes_recv,
            "packets_sent": io.packets_sent,
            "packets_recv": io.packets_recv,
            "mb_sent": round(io.bytes_sent / (1024**2), 2),
            "mb_recv": round(io.bytes_recv / (1024**2), 2)
        }

    def disk_io(self) -> dict:
        """Get disk I/O statistics"""
        try:
            io = psutil.disk_io_counters()
            return {
                "read_mb": round(io.read_bytes / (1024**2), 2),
                "write_mb": round(io.write_bytes / (1024**2), 2),
                "read_count": io.read_count,
                "write_count": io.write_count
            }
        except Exception:
            return {}

    def top_processes(self, n: int = 5) -> list:
        """Get top N processes by CPU usage"""
        procs = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                procs.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return sorted(procs, key=lambda x: x.get('cpu_percent', 0), reverse=True)[:n]

    def uptime(self) -> str:
        """Get system uptime"""
        boot_time = psutil.boot_time()
        uptime_seconds = time.time() - boot_time
        days = int(uptime_seconds // 86400)
        hours = int((uptime_seconds % 86400) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        return f"{days}d {hours}h {minutes}m"

    def temperatures(self) -> dict:
        """Get CPU temperatures (if available)"""
        try:
            temps = psutil.sensors_temperatures()
            return temps
        except Exception:
            return {}

    def battery(self) -> dict:
        """Get battery status (for laptops)"""
        try:
            battery = psutil.sensors_battery()
            if battery:
                return {
                    "percent": battery.percent,
                    "plugged": battery.power_plugged,
                    "time_left": battery.secsleft
                }
        except Exception:
            pass
        return {"percent": 100, "plugged": True, "time_left": -1}

    def snapshot(self) -> dict:
        """Get complete system snapshot"""
        return {
            "timestamp": datetime.now().isoformat(),
            "cpu_percent": self.cpu(),
            "cpu_cores": self.cpu_per_core(),
            "ram": self.ram(),
            "disk": self.disk(),
            "network_latency_ms": self.network_latency(),
            "network_io": self.network_io(),
            "top_processes": self.top_processes(),
            "uptime": self.uptime()
        }

    def quick_status(self) -> str:
        """Get quick one-line status"""
        cpu = self.cpu()
        ram = self.ram()
        disk = self.disk()
        latency = self.network_latency()
        
        status = f"CPU: {cpu}% | RAM: {ram['percent']}% | Disk: {disk['percent']}% | Latency: {latency}ms"
        return status

    def health_check(self) -> dict:
        """Run health check with alerts"""
        snap = self.snapshot()
        alerts = []
        
        if snap['cpu_percent'] > 80:
            alerts.append(f"⚠️ HIGH CPU: {snap['cpu_percent']}%")
        if snap['ram']['percent'] > 85:
            alerts.append(f"⚠️ HIGH RAM: {snap['ram']['percent']}%")
        if snap['disk']['percent'] > 90:
            alerts.append(f"⚠️ LOW DISK: {snap['disk']['free_gb']}GB free")
        if snap['network_latency_ms'] > 100 or snap['network_latency_ms'] < 0:
            alerts.append(f"⚠️ NETWORK ISSUE: {snap['network_latency_ms']}ms")
        
        return {
            "status": "OK" if not alerts else "WARNING",
            "alerts": alerts,
            "snapshot": snap
        }

    def monitor(self, interval: float = 1.0, duration: float = None):
        """Continuous monitoring with live output"""
        start = time.time()
        try:
            while True:
                if duration and (time.time() - start) > duration:
                    break
                
                status = self.quick_status()
                print(f"\r{status}    ", end="", flush=True)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n✅ Monitoring stopped")


# 🐟 Fish Drive Health
class FishDriveHealth:
    """Monitor Fish Music external drives"""
    
    FISH_DRIVES = [
        "/Volumes/4TB Blue Fish",
        "/Volumes/4TB Big Fish",
        "/Volumes/4TB FISH SG",
        "/Volumes/12TB"
    ]

    def check_drives(self) -> list:
        """Check all Fish drives"""
        results = []
        for drive in self.FISH_DRIVES:
            path = Path(drive)
            if path.exists():
                try:
                    disk = psutil.disk_usage(str(path))
                    results.append({
                        "name": path.name,
                        "path": str(path),
                        "mounted": True,
                        "percent": disk.percent,
                        "used_tb": round(disk.used / (1024**4), 2),
                        "total_tb": round(disk.total / (1024**4), 2),
                        "free_tb": round(disk.free / (1024**4), 2)
                    })
                except Exception as e:
                    results.append({
                        "name": path.name,
                        "path": str(path),
                        "mounted": True,
                        "error": str(e)
                    })
            else:
                results.append({
                    "name": Path(drive).name,
                    "path": drive,
                    "mounted": False
                })
        return results

    def status(self) -> str:
        """Quick status of all Fish drives"""
        drives = self.check_drives()
        lines = ["🐟 FISH DRIVES:"]
        for d in drives:
            if d.get('mounted') and 'percent' in d:
                lines.append(f"  {d['name']}: {d['percent']}% ({d['free_tb']}TB free)")
            elif d.get('mounted'):
                lines.append(f"  {d['name']}: ⚠️ {d.get('error', 'Error')}")
            else:
                lines.append(f"  {d['name']}: ❌ NOT MOUNTED")
        return "\n".join(lines)


def main():
    """CLI interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description='NOIZYLAB System Health Monitor')
    parser.add_argument('--snapshot', action='store_true', help='Full system snapshot')
    parser.add_argument('--quick', action='store_true', help='Quick status line')
    parser.add_argument('--fish', action='store_true', help='Fish drives status')
    parser.add_argument('--monitor', type=float, nargs='?', const=1.0, help='Continuous monitor')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    args = parser.parse_args()
    
    health = SystemHealth()
    fish = FishDriveHealth()
    
    if args.snapshot:
        snap = health.snapshot()
        if args.json:
            print(json.dumps(snap, indent=2))
        else:
            print(f"🖥️  SYSTEM SNAPSHOT - {snap['timestamp']}")
            print(f"   CPU: {snap['cpu_percent']}%")
            print(f"   RAM: {snap['ram']['percent']}% ({snap['ram']['used_gb']}/{snap['ram']['total_gb']} GB)")
            print(f"   Disk: {snap['disk']['percent']}% ({snap['disk']['free_gb']} GB free)")
            print(f"   Network: {snap['network_latency_ms']}ms")
            print(f"   Uptime: {snap['uptime']}")
    
    elif args.fish:
        if args.json:
            print(json.dumps(fish.check_drives(), indent=2))
        else:
            print(fish.status())
    
    elif args.monitor is not None:
        print("🔥 MONITORING (Ctrl+C to stop)...")
        health.monitor(interval=args.monitor)
    
    else:
        # Default: quick status + health check
        check = health.health_check()
        print(f"🔥 GOD STATUS: {check['status']}")
        print(f"   {health.quick_status()}")
        if check['alerts']:
            for alert in check['alerts']:
                print(f"   {alert}")
        print(f"\n{fish.status()}")
        print("\n🔥 GORUNFREE! 🎸🔥")


if __name__ == "__main__":
    main()
