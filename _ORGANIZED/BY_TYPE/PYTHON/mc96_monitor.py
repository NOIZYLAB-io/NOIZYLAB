#!/usr/bin/env python3
"""
MC96ECOUNIVERSE REAL-TIME PERFORMANCE MONITOR
Live monitoring dashboard for MC96 mesh network
Created by CB_01 for ROB - GORUNFREE! 🚀
"""

import json
import subprocess
import time
import os
from datetime import datetime
from typing import Dict, List

class MC96Monitor:
    """Real-time MC96 Network Monitor"""
    
    def __init__(self):
        self.mesh_config_file = '/Users/m2ultra/CB-01-FISHMUSICINC/tools/scripts/mc96_mesh_config.json'
        self.interface = 'en0'
        self.stats_history = []
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear')
    
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
                        'timestamp': datetime.now().isoformat(),
                        'ipkts': int(parts[4]),
                        'ierrs': int(parts[5]),
                        'ibytes': int(parts[6]),
                        'opkts': int(parts[7]),
                        'oerrs': int(parts[8]),
                        'obytes': int(parts[9])
                    }
            return {}
        except Exception as e:
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
    
    def calculate_bandwidth(self, current: Dict, previous: Dict, interval: float) -> Dict:
        """Calculate bandwidth from byte deltas"""
        if not current or not previous:
            return {'rx_mbps': 0, 'tx_mbps': 0}
        
        rx_bytes = current['ibytes'] - previous['ibytes']
        tx_bytes = current['obytes'] - previous['obytes']
        
        # Convert to Mbps
        rx_mbps = (rx_bytes * 8) / (interval * 1000000)
        tx_mbps = (tx_bytes * 8) / (interval * 1000000)
        
        return {
            'rx_mbps': max(0, rx_mbps),
            'tx_mbps': max(0, tx_mbps)
        }
    
    def format_bytes(self, bytes_val: int) -> str:
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.2f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.2f} PB"
    
    def get_bar_graph(self, value: float, max_value: float, width: int = 20) -> str:
        """Create ASCII bar graph"""
        if max_value == 0:
            filled = 0
        else:
            filled = int((value / max_value) * width)
        empty = width - filled
        
        # Color based on utilization
        if value / max_value > 0.8:
            color = '\033[91m'  # Red
        elif value / max_value > 0.5:
            color = '\033[93m'  # Yellow
        else:
            color = '\033[92m'  # Green
        
        return f"{color}{'█' * filled}{'░' * empty}\033[0m"
    
    def load_mesh_config(self) -> Dict:
        """Load mesh configuration"""
        try:
            with open(self.mesh_config_file, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def monitor_loop(self, update_interval: float = 1.0):
        """Main monitoring loop"""
        print("🚀 Starting MC96ECOUNIVERSE Monitor...")
        print("   Press Ctrl+C to exit")
        time.sleep(2)
        
        previous_stats = None
        
        try:
            while True:
                self.clear_screen()
                current_stats = self.get_interface_stats()
                
                # Calculate bandwidth
                bandwidth = {'rx_mbps': 0, 'tx_mbps': 0}
                if previous_stats:
                    bandwidth = self.calculate_bandwidth(current_stats, previous_stats, update_interval)
                
                # Get MTU
                mtu = self.get_mtu()
                
                # Load mesh config
                mesh_config = self.load_mesh_config()
                
                # Display dashboard
                self.display_dashboard(current_stats, bandwidth, mtu, mesh_config)
                
                previous_stats = current_stats
                time.sleep(update_interval)
                
        except KeyboardInterrupt:
            print("\n\n👋 Monitor stopped. GORUNFREE! 🎸🔥\n")
    
    def display_dashboard(self, stats: Dict, bandwidth: Dict, mtu: int, mesh_config: Dict):
        """Display monitoring dashboard"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("╔" + "═" * 78 + "╗")
        print(f"║ 🔥 MC96ECOUNIVERSE REAL-TIME MONITOR" + " " * 41 + "║")
        print(f"║ {now}" + " " * 58 + "║")
        print("╠" + "═" * 78 + "╣")
        
        # Interface Status
        print("║ 📡 INTERFACE STATUS: en0" + " " * 53 + "║")
        hotrod = "🔥 HOT ROD MODE ACTIVE" if mtu == 9000 else "⚠️  Standard MTU"
        mtu_status = f"MTU: {mtu}"
        print(f"║    {hotrod} • {mtu_status}" + " " * (72 - len(hotrod) - len(mtu_status)) + "║")
        print("║" + " " * 78 + "║")
        
        # Current Bandwidth
        print("║ ⚡ CURRENT BANDWIDTH" + " " * 57 + "║")
        rx_bar = self.get_bar_graph(bandwidth['rx_mbps'], 1000, 30)
        tx_bar = self.get_bar_graph(bandwidth['tx_mbps'], 1000, 30)
        print(f"║    RX: {bandwidth['rx_mbps']:7.2f} Mbps {rx_bar}" + " " * 15 + "║")
        print(f"║    TX: {bandwidth['tx_mbps']:7.2f} Mbps {tx_bar}" + " " * 15 + "║")
        print("║" + " " * 78 + "║")
        
        # Lifetime Statistics
        if stats:
            print("║ 📊 LIFETIME STATISTICS" + " " * 55 + "║")
            total_rx = self.format_bytes(stats['ibytes'])
            total_tx = self.format_bytes(stats['obytes'])
            total_rx_pkts = f"{stats['ipkts']:,}"
            total_tx_pkts = f"{stats['opkts']:,}"
            print(f"║    Total RX: {total_rx:>15} ({total_rx_pkts:>15} packets)" + " " * (32 - len(total_rx) - len(total_rx_pkts)) + "║")
            print(f"║    Total TX: {total_tx:>15} ({total_tx_pkts:>15} packets)" + " " * (32 - len(total_tx) - len(total_tx_pkts)) + "║")
            
            error_status = "✅ ZERO ERRORS" if stats['ierrs'] == 0 and stats['oerrs'] == 0 else f"⚠️  {stats['ierrs']} RX / {stats['oerrs']} TX errors"
            print(f"║    Errors: {error_status}" + " " * (67 - len(error_status)) + "║")
            print("║" + " " * 78 + "║")
        
        # MC96 Mesh Network Status
        if mesh_config:
            print("║ 🕸️  MC96 MESH NETWORK STATUS" + " " * 48 + "║")
            nodes = mesh_config.get('total_nodes', 0)
            active = mesh_config.get('active_tunnels', 0)
            total = mesh_config.get('total_tunnels', 0)
            
            mesh_emoji = "🟢" if active == total else "🟡" if active > 0 else "🔴"
            print(f"║    {mesh_emoji} Nodes: {nodes}  •  Tunnels: {active}/{total} Active" + " " * (48 - len(str(nodes)) - len(str(active)) - len(str(total))) + "║")
            
            # Show node list
            if 'nodes' in mesh_config:
                print("║    " + " " * 74 + "║")
                for node in mesh_config['nodes'][:5]:  # Show top 5
                    node_info = f"{node['ip']:15} • {node['type']:20} • {node['latency_avg_ms']:.2f}ms"
                    print(f"║    {node_info}" + " " * (74 - len(node_info)) + "║")
        else:
            print("║ 🕸️  MC96 MESH NETWORK: Not Configured" + " " * 39 + "║")
            print("║    Run: python3 mc96_scan.py && python3 mc96_mesh.py" + " " * 24 + "║")
        
        print("╠" + "═" * 78 + "╣")
        print("║ 🚀 MC96ECOUNIVERSE • GORUNFREE! 🎸🔥" + " " * 43 + "║")
        print("╚" + "═" * 78 + "╝")
        print()

def main():
    """Main execution"""
    monitor = MC96Monitor()
    monitor.monitor_loop(update_interval=1.0)

if __name__ == '__main__':
    main()

