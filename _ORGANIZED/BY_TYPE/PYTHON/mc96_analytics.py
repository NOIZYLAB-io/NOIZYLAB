#!/usr/bin/env python3
"""
MC96ECOUNIVERSE ANALYTICS & REPORTING
Generate detailed performance reports and analytics
Created by CB_01 for ROB - GORUNFREE! 🚀
"""

import json
import subprocess
import time
import os
from datetime import datetime, timedelta
from typing import Dict, List
import statistics

class MC96Analytics:
    """Network Analytics and Reporting System"""
    
    def __init__(self):
        self.interface = 'en0'
        self.scan_file = '/Users/m2ultra/CB-01-FISHMUSICINC/tools/scripts/mc96_scan_results.json'
        self.mesh_file = '/Users/m2ultra/CB-01-FISHMUSICINC/tools/scripts/mc96_mesh_config.json'
        self.report_dir = '/Users/m2ultra/CB-01-FISHMUSICINC/tools/scripts/reports/'
        
        # Create reports directory
        os.makedirs(self.report_dir, exist_ok=True)
    
    def load_scan_data(self) -> Dict:
        """Load scan results"""
        try:
            with open(self.scan_file, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def load_mesh_data(self) -> Dict:
        """Load mesh configuration"""
        try:
            with open(self.mesh_file, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def get_interface_stats(self) -> Dict:
        """Get current interface statistics"""
        try:
            result = subprocess.run(
                ['netstat', '-I', self.interface, '-b'],
                capture_output=True,
                text=True
            )
            lines = result.stdout.strip().split('\n')
            if len(lines) >= 2:
                parts = lines[1].split()
                if len(parts) >= 10:
                    return {
                        'ipkts': int(parts[4]),
                        'ierrs': int(parts[5]),
                        'ibytes': int(parts[6]),
                        'opkts': int(parts[7]),
                        'oerrs': int(parts[8]),
                        'obytes': int(parts[9])
                    }
            return {}
        except:
            return {}
    
    def get_mtu(self) -> int:
        """Get current MTU"""
        try:
            result = subprocess.run(
                ['ifconfig', self.interface],
                capture_output=True,
                text=True
            )
            import re
            match = re.search(r'mtu (\d+)', result.stdout)
            return int(match.group(1)) if match else 0
        except:
            return 0
    
    def format_bytes(self, bytes_val: int) -> str:
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.2f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.2f} PB"
    
    def calculate_network_efficiency(self, stats: Dict) -> Dict:
        """Calculate network efficiency metrics"""
        total_packets = stats.get('ipkts', 0) + stats.get('opkts', 0)
        total_errors = stats.get('ierrs', 0) + stats.get('oerrs', 0)
        
        error_rate = (total_errors / total_packets * 100) if total_packets > 0 else 0
        efficiency = 100 - error_rate
        
        return {
            'total_packets': total_packets,
            'total_errors': total_errors,
            'error_rate_pct': error_rate,
            'efficiency_pct': efficiency
        }
    
    def analyze_device_performance(self, scan_data: Dict) -> Dict:
        """Analyze device performance statistics"""
        devices = scan_data.get('devices', [])
        responsive = [d for d in devices if d['responsive']]
        
        if not responsive:
            return {}
        
        latencies = [d['latency_avg_ms'] for d in responsive]
        
        return {
            'total_devices': len(devices),
            'responsive_devices': len(responsive),
            'responsiveness_pct': len(responsive) / len(devices) * 100 if devices else 0,
            'latency_min': min(latencies),
            'latency_max': max(latencies),
            'latency_avg': statistics.mean(latencies),
            'latency_median': statistics.median(latencies),
            'latency_stdev': statistics.stdev(latencies) if len(latencies) > 1 else 0
        }
    
    def analyze_mesh_health(self, mesh_data: Dict) -> Dict:
        """Analyze mesh network health"""
        total_tunnels = mesh_data.get('total_tunnels', 0)
        active_tunnels = mesh_data.get('active_tunnels', 0)
        
        if total_tunnels == 0:
            return {'configured': False}
        
        tunnels = mesh_data.get('tunnels', [])
        active = [t for t in tunnels if t.get('status') == 'active']
        
        if not active:
            return {
                'configured': True,
                'health': 'critical',
                'active_pct': 0
            }
        
        # Calculate performance metrics
        latencies = [t['performance']['latency_ms'] for t in active if 'performance' in t]
        bandwidths = [t['performance']['bandwidth_estimate'] for t in active if 'performance' in t]
        
        health_pct = (active_tunnels / total_tunnels * 100) if total_tunnels > 0 else 0
        
        if health_pct >= 90:
            health = 'excellent'
        elif health_pct >= 75:
            health = 'good'
        elif health_pct >= 50:
            health = 'fair'
        else:
            health = 'poor'
        
        return {
            'configured': True,
            'health': health,
            'active_pct': health_pct,
            'total_bandwidth_mbps': sum(bandwidths) if bandwidths else 0,
            'avg_latency_ms': statistics.mean(latencies) if latencies else 0,
            'total_nodes': mesh_data.get('total_nodes', 0),
            'total_tunnels': total_tunnels,
            'active_tunnels': active_tunnels
        }
    
    def generate_report(self) -> Dict:
        """Generate comprehensive analytics report"""
        print("📊 MC96ECOUNIVERSE ANALYTICS ENGINE")
        print("=" * 70)
        print()
        
        report = {
            'generated_at': datetime.now().isoformat(),
            'system': 'MC96ECOUNIVERSE',
            'interface': self.interface
        }
        
        # Get interface stats
        print("📡 Analyzing interface statistics...")
        stats = self.get_interface_stats()
        mtu = self.get_mtu()
        
        report['interface_stats'] = stats
        report['mtu'] = mtu
        report['hotrod_mode'] = mtu == 9000
        
        if stats:
            efficiency = self.calculate_network_efficiency(stats)
            report['efficiency'] = efficiency
            print(f"   ✅ Efficiency: {efficiency['efficiency_pct']:.4f}%")
        
        print()
        
        # Analyze devices
        print("🔍 Analyzing device performance...")
        scan_data = self.load_scan_data()
        if scan_data:
            device_perf = self.analyze_device_performance(scan_data)
            report['device_performance'] = device_perf
            if device_perf:
                print(f"   ✅ Responsive: {device_perf['responsive_devices']}/{device_perf['total_devices']}")
                print(f"   ✅ Avg Latency: {device_perf['latency_avg']:.2f}ms")
        else:
            print("   ⚠️  No scan data available")
        
        print()
        
        # Analyze mesh
        print("🕸️  Analyzing mesh network...")
        mesh_data = self.load_mesh_data()
        if mesh_data:
            mesh_health = self.analyze_mesh_health(mesh_data)
            report['mesh_health'] = mesh_health
            if mesh_health.get('configured'):
                print(f"   ✅ Health: {mesh_health['health'].upper()}")
                print(f"   ✅ Active Tunnels: {mesh_health.get('active_tunnels', 0)}/{mesh_health.get('total_tunnels', 0)}")
        else:
            print("   ⚠️  No mesh data available")
        
        print()
        
        return report
    
    def print_report(self, report: Dict):
        """Print formatted report"""
        print()
        print("╔" + "═" * 68 + "╗")
        print("║" + " " * 15 + "MC96ECOUNIVERSE ANALYTICS REPORT" + " " * 21 + "║")
        print("╠" + "═" * 68 + "╣")
        
        # System Info
        print("║ 🖥️  SYSTEM INFORMATION" + " " * 45 + "║")
        print(f"║    Interface: {report['interface']}" + " " * 54 + "║")
        mtu_status = "🔥 HOT ROD MODE" if report['hotrod_mode'] else f"MTU {report['mtu']}"
        print(f"║    MTU: {mtu_status}" + " " * (63 - len(mtu_status)) + "║")
        print(f"║    Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" + " " * 39 + "║")
        print("║" + " " * 68 + "║")
        
        # Interface Statistics
        if 'interface_stats' in report and report['interface_stats']:
            stats = report['interface_stats']
            print("║ 📊 INTERFACE STATISTICS" + " " * 44 + "║")
            print(f"║    Total RX: {self.format_bytes(stats['ibytes']):>15} ({stats['ipkts']:>12,} packets)  ║")
            print(f"║    Total TX: {self.format_bytes(stats['obytes']):>15} ({stats['opkts']:>12,} packets)  ║")
            
            if 'efficiency' in report:
                eff = report['efficiency']
                print(f"║    Efficiency: {eff['efficiency_pct']:.4f}% ({eff['total_errors']} errors)     " + " " * 15 + "║")
            print("║" + " " * 68 + "║")
        
        # Device Performance
        if 'device_performance' in report and report['device_performance']:
            perf = report['device_performance']
            print("║ 🎯 DEVICE PERFORMANCE" + " " * 46 + "║")
            print(f"║    Devices: {perf['responsive_devices']}/{perf['total_devices']} responsive ({perf['responsiveness_pct']:.1f}%)" + " " * 30 + "║")
            print(f"║    Latency: min={perf['latency_min']:.2f}ms avg={perf['latency_avg']:.2f}ms max={perf['latency_max']:.2f}ms" + " " * 15 + "║")
            print(f"║    Std Dev: {perf['latency_stdev']:.2f}ms" + " " * 48 + "║")
            print("║" + " " * 68 + "║")
        
        # Mesh Health
        if 'mesh_health' in report and report['mesh_health'].get('configured'):
            mesh = report['mesh_health']
            health_emoji = {
                'excellent': '🔥',
                'good': '✅',
                'fair': '⚠️',
                'poor': '❌',
                'critical': '🔴'
            }.get(mesh['health'], '❓')
            
            print("║ 🕸️  MESH NETWORK HEALTH" + " " * 43 + "║")
            print(f"║    Status: {health_emoji} {mesh['health'].upper()}" + " " * (57 - len(mesh['health'])) + "║")
            print(f"║    Nodes: {mesh['total_nodes']}" + " " * 57 + "║")
            print(f"║    Tunnels: {mesh['active_tunnels']}/{mesh['total_tunnels']} active ({mesh['active_pct']:.1f}%)" + " " * 32 + "║")
            if mesh.get('total_bandwidth_mbps'):
                print(f"║    Bandwidth: ~{mesh['total_bandwidth_mbps']} Mbps" + " " * 40 + "║")
            if mesh.get('avg_latency_ms'):
                print(f"║    Avg Latency: {mesh['avg_latency_ms']:.2f}ms" + " " * 43 + "║")
            print("║" + " " * 68 + "║")
        
        print("╠" + "═" * 68 + "╣")
        print("║ 🚀 MC96ECOUNIVERSE • GORUNFREE! 🎸🔥" + " " * 32 + "║")
        print("╚" + "═" * 68 + "╝")
        print()
    
    def save_report(self, report: Dict) -> str:
        """Save report to JSON file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"mc96_report_{timestamp}.json"
        filepath = os.path.join(self.report_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)
        
        return filepath

def main():
    """Main execution"""
    analytics = MC96Analytics()
    report = analytics.generate_report()
    analytics.print_report(report)
    
    # Save report
    filepath = analytics.save_report(report)
    print(f"💾 Report saved: {filepath}")
    print()
    print("GORUNFREE! 🎸🔥")

if __name__ == '__main__':
    main()

