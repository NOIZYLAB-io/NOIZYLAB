#!/usr/bin/env python3
"""
Network Performance Monitor
============================
Real-time network performance monitoring with auto-tuning
"""

import time
import subprocess
import psutil
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path
import sqlite3
import json


class NetworkPerformanceMonitor:
    """Monitor and optimize network performance in real-time"""
    
    def __init__(self):
        self.db_path = Path(__file__).parent / "network_devices.db"
        self._init_database()
        
        # Baseline metrics
        self.baseline = None
        
        print("📊 Network Performance Monitor initialized")
    
    def _init_database(self):
        """Initialize performance database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS network_performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                interface TEXT,
                mtu INTEGER,
                throughput_mbps REAL,
                latency_ms REAL,
                packet_loss REAL,
                cpu_usage REAL,
                retransmissions INTEGER,
                quality_score REAL
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS performance_optimizations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                optimization_type TEXT,
                parameter TEXT,
                old_value TEXT,
                new_value TEXT,
                improvement_percent REAL,
                success BOOLEAN
            )
        """)
        
        conn.commit()
        conn.close()
    
    def measure_throughput(self, interface: str = "en0") -> Dict:
        """Measure current network throughput"""
        
        # Get network stats
        net_io_start = psutil.net_io_counters(pernic=True).get(interface)
        
        if not net_io_start:
            return {"error": "Interface not found"}
        
        time.sleep(1)  # Measure over 1 second
        
        net_io_end = psutil.net_io_counters(pernic=True).get(interface)
        
        # Calculate throughput
        bytes_sent = net_io_end.bytes_sent - net_io_start.bytes_sent
        bytes_recv = net_io_end.bytes_recv - net_io_start.bytes_recv
        
        # Convert to Mbps
        throughput_sent = (bytes_sent * 8) / (1024 * 1024)  # Mbps
        throughput_recv = (bytes_recv * 8) / (1024 * 1024)
        
        # Get errors and drops
        errors = net_io_end.errin + net_io_end.errout
        drops = net_io_end.dropin + net_io_end.dropout
        
        return {
            "interface": interface,
            "throughput_sent_mbps": throughput_sent,
            "throughput_recv_mbps": throughput_recv,
            "total_throughput_mbps": throughput_sent + throughput_recv,
            "errors": errors,
            "drops": drops,
            "packets_sent": net_io_end.packets_sent - net_io_start.packets_sent,
            "packets_recv": net_io_end.packets_recv - net_io_start.packets_recv
        }
    
    def measure_latency(self, target: str = "192.168.1.1") -> Dict:
        """Measure network latency"""
        try:
            result = subprocess.run(
                ['ping', '-c', '10', target],
                capture_output=True,
                text=True,
                timeout=15
            )
            
            if result.returncode == 0:
                output = result.stdout
                
                # Extract statistics
                if 'avg' in output:
                    parts = output.split('avg')[1].split()[0].split('/')
                    min_time = float(parts[0]) if len(parts) > 0 else 0
                    avg_time = float(parts[1]) if len(parts) > 1 else 0
                    max_time = float(parts[2]) if len(parts) > 2 else 0
                    
                    # Packet loss
                    loss = 0
                    if 'packet loss' in output:
                        loss_str = output.split('packet loss')[0].split()[-1]
                        loss = float(loss_str.strip('%'))
                    
                    return {
                        "target": target,
                        "min_ms": min_time,
                        "avg_ms": avg_time,
                        "max_ms": max_time,
                        "packet_loss": loss,
                        "quality": "excellent" if avg_time < 2 else "good" if avg_time < 5 else "fair"
                    }
        except:
            pass
        
        return {"error": "Latency test failed"}
    
    def get_network_quality_score(self, interface: str = "en0", target: str = "192.168.1.1") -> Dict:
        """Calculate overall network quality score (0-100)"""
        
        score = 100
        factors = []
        
        # Get MTU
        try:
            result = subprocess.run(['ifconfig', interface], capture_output=True, text=True, timeout=2)
            mtu = 1500
            for line in result.stdout.split('\n'):
                if 'mtu' in line.lower():
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if part.lower() == 'mtu':
                            mtu = int(parts[i + 1])
                            break
            
            # MTU scoring
            if mtu >= 9000:
                factors.append(("MTU", 100, "🔥 Jumbo frames enabled!"))
            elif mtu > 1500:
                score -= 5
                factors.append(("MTU", 95, "Enhanced MTU"))
            else:
                score -= 15
                factors.append(("MTU", 85, "Standard MTU (upgrade recommended)"))
        except:
            score -= 10
        
        # Throughput
        throughput = self.measure_throughput(interface)
        if "error" not in throughput:
            total_mbps = throughput["total_throughput_mbps"]
            
            if total_mbps > 100:
                factors.append(("Throughput", 100, f"{total_mbps:.1f} Mbps"))
            elif total_mbps > 10:
                factors.append(("Throughput", 90, f"{total_mbps:.1f} Mbps"))
            else:
                score -= 10
                factors.append(("Throughput", 80, f"{total_mbps:.1f} Mbps (low)"))
        
        # Latency
        latency = self.measure_latency(target)
        if "error" not in latency:
            avg_ms = latency["avg_ms"]
            loss = latency["packet_loss"]
            
            if avg_ms < 2 and loss == 0:
                factors.append(("Latency", 100, f"{avg_ms:.1f}ms (excellent)"))
            elif avg_ms < 5 and loss < 1:
                factors.append(("Latency", 90, f"{avg_ms:.1f}ms (good)"))
            else:
                score -= 10
                factors.append(("Latency", 80, f"{avg_ms:.1f}ms"))
            
            if loss > 0:
                score -= loss * 5
                factors.append(("Packet Loss", 100 - (loss * 5), f"{loss}%"))
        
        # CPU usage
        cpu = psutil.cpu_percent(interval=0.5)
        if cpu < 50:
            factors.append(("CPU", 100, f"{cpu:.1f}%"))
        elif cpu < 80:
            score -= 5
            factors.append(("CPU", 95, f"{cpu:.1f}%"))
        else:
            score -= 15
            factors.append(("CPU", 85, f"{cpu:.1f}% (high)"))
        
        score = max(0, min(100, score))
        
        return {
            "overall_score": score,
            "grade": "A+" if score >= 95 else "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D",
            "factors": factors,
            "recommendations": self._get_recommendations(factors, mtu)
        }
    
    def _get_recommendations(self, factors: List, current_mtu: int) -> List[str]:
        """Get performance recommendations"""
        recommendations = []
        
        # MTU recommendations
        if current_mtu < 9000:
            recommendations.append("🔥 Enable jumbo frames (MTU 9000) for 15-20% improvement!")
        
        # Check for packet loss
        for factor in factors:
            if factor[0] == "Packet Loss" and factor[1] < 95:
                recommendations.append("⚠️ High packet loss detected - check cables/connections")
        
        # Check latency
        for factor in factors:
            if factor[0] == "Latency" and factor[1] < 90:
                recommendations.append("⚡ High latency - check network congestion")
        
        # Check CPU
        for factor in factors:
            if factor[0] == "CPU" and factor[1] < 90:
                recommendations.append("💻 High CPU - enable jumbo frames to reduce overhead")
        
        if not recommendations:
            recommendations.append("✅ Network performance is excellent!")
        
        return recommendations
    
    def auto_tune_network(self, interface: str = "en0") -> Dict:
        """Automatically tune network for best performance"""
        
        print(f"🎛️ Auto-tuning network interface: {interface}")
        
        optimizations = []
        
        # Get current state
        current_score = self.get_network_quality_score(interface)
        
        print(f"\n📊 Current Quality Score: {current_score['overall_score']}/100 ({current_score['grade']})")
        
        # Recommendations
        print(f"\n💡 Recommendations:")
        for rec in current_score['recommendations']:
            print(f"  {rec}")
        
        # Auto-apply safe optimizations
        
        # 1. Increase socket buffers
        try:
            subprocess.run(['sysctl', '-w', 'net.inet.tcp.sendspace=131072'], 
                         capture_output=True, timeout=2)
            subprocess.run(['sysctl', '-w', 'net.inet.tcp.recvspace=131072'],
                         capture_output=True, timeout=2)
            optimizations.append("Increased TCP buffers")
        except:
            pass
        
        # 2. Enable TCP window scaling
        try:
            subprocess.run(['sysctl', '-w', 'net.inet.tcp.rfc1323=1'],
                         capture_output=True, timeout=2)
            optimizations.append("Enabled TCP window scaling")
        except:
            pass
        
        if optimizations:
            print(f"\n✅ Applied {len(optimizations)} optimizations:")
            for opt in optimizations:
                print(f"  • {opt}")
        
        return {
            "original_score": current_score['overall_score'],
            "optimizations": optimizations
        }
    
    def monitor_continuously(self, interval: int = 60, interface: str = "en0"):
        """Monitor network performance continuously"""
        
        print(f"📊 Starting continuous network monitoring")
        print(f"⏱️  Interval: {interval}s")
        print(f"🔍 Interface: {interface}")
        print()
        
        iteration = 0
        
        while True:
            try:
                iteration += 1
                print(f"\n🔄 Iteration {iteration} - {datetime.now().strftime('%H:%M:%S')}")
                print("-" * 60)
                
                # Get quality score
                quality = self.get_network_quality_score(interface)
                
                print(f"📊 Quality Score: {quality['overall_score']}/100 ({quality['grade']})")
                
                # Show factors
                for factor_name, factor_score, factor_value in quality['factors']:
                    emoji = "✅" if factor_score >= 95 else "⚡" if factor_score >= 85 else "⚠️"
                    print(f"  {emoji} {factor_name}: {factor_value}")
                
                # Show recommendations
                if quality['recommendations']:
                    print(f"\n💡 Recommendations:")
                    for rec in quality['recommendations'][:3]:
                        print(f"  {rec}")
                
                # Log to database
                self._log_performance(interface, quality)
                
                # Alert if quality drops
                if quality['overall_score'] < 70:
                    self._send_performance_alert(interface, quality)
                
                time.sleep(interval)
                
            except KeyboardInterrupt:
                print("\n\n🛑 Monitoring stopped")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                time.sleep(interval)
    
    def _log_performance(self, interface: str, quality: Dict):
        """Log performance to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Extract metrics from factors
        mtu = 1500
        latency = 0
        throughput = 0
        
        for factor_name, _, factor_value in quality.get('factors', []):
            if factor_name == "Latency":
                try:
                    latency = float(factor_value.split('ms')[0])
                except:
                    pass
        
        cursor.execute("""
            INSERT INTO network_performance
            (interface, mtu, throughput_mbps, latency_ms, quality_score)
            VALUES (?, ?, ?, ?, ?)
        """, (interface, mtu, throughput, latency, quality['overall_score']))
        
        conn.commit()
        conn.close()
    
    def _send_performance_alert(self, interface: str, quality: Dict):
        """Send alert for poor performance"""
        try:
            import sys
            sys.path.append('/Users/m2ultra/NOIZYLAB/integrations/slack')
            from slack_notifier import alert
            
            alert(
                f"Network performance degraded on {interface}\n" + 
                f"Score: {quality['overall_score']}/100\n" +
                f"Recommendations: {quality['recommendations'][0] if quality['recommendations'] else 'Check network'}",
                "warning"
            )
        except:
            pass


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Network Performance Monitor")
    parser.add_argument("action", choices=["test", "monitor", "tune", "score"])
    parser.add_argument("--interface", default="en0", help="Network interface")
    parser.add_argument("--interval", type=int, default=60, help="Monitor interval")
    
    args = parser.parse_args()
    
    monitor = NetworkPerformanceMonitor()
    
    if args.action == "test":
        print(f"📊 Testing {args.interface}...\n")
        throughput = monitor.measure_throughput(args.interface)
        print(f"Throughput: {throughput.get('total_throughput_mbps', 0):.2f} Mbps")
        
        latency = monitor.measure_latency()
        if 'avg_ms' in latency:
            print(f"Latency: {latency['avg_ms']:.2f}ms")
            print(f"Packet Loss: {latency['packet_loss']}%")
    
    elif args.action == "score":
        print(f"📊 Network Quality Assessment\n")
        quality = monitor.get_network_quality_score(args.interface)
        
        print(f"Overall Score: {quality['overall_score']}/100 ({quality['grade']})")
        print(f"\nFactors:")
        for name, score, value in quality['factors']:
            print(f"  {name}: {value} (Score: {score})")
        
        print(f"\nRecommendations:")
        for rec in quality['recommendations']:
            print(f"  {rec}")
    
    elif args.action == "tune":
        monitor.auto_tune_network(args.interface)
    
    elif args.action == "monitor":
        monitor.monitor_continuously(args.interval, args.interface)

