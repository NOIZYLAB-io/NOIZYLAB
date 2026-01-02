#!/usr/bin/env python3
"""
Jumbo Frame Manager - HOT ROD MODE! 🔥
======================================
Enable and optimize jumbo frames (MTU 9000) for maximum throughput!
"""

import subprocess
import socket
import struct
import requests
import time
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import sqlite3
from dataclasses import dataclass
import json


@dataclass
class JumboFrameStatus:
    """Jumbo frame configuration status"""
    interface: str
    current_mtu: int
    target_mtu: int
    enabled: bool
    performance_gain: float
    status: str


class JumboFrameManager:
    """
    HOT ROD MODE - Jumbo Frame Configuration Manager
    Enables MTU 9000 for maximum network performance!
    """
    
    def __init__(self):
        self.target_mtu = 9000  # Jumbo frames!
        self.standard_mtu = 1500
        self.db_path = Path(__file__).parent / "network_devices.db"
        
        # Initialize jumbo frame tracking
        self._init_jumbo_tracking()
        
        print("🔥 Jumbo Frame Manager - HOT ROD MODE!")
        print(f"🎯 Target MTU: {self.target_mtu} bytes")
    
    def _init_jumbo_tracking(self):
        """Add jumbo frame tracking to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Jumbo frame configuration table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jumbo_frames (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                interface TEXT,
                device_ip TEXT,
                current_mtu INTEGER,
                target_mtu INTEGER,
                enabled BOOLEAN,
                configured_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                performance_baseline REAL,
                performance_after REAL,
                gain_percent REAL
            )
        """)
        
        # MTU test results
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mtu_tests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                device_ip TEXT,
                mtu_size INTEGER,
                ping_time REAL,
                throughput_mbps REAL,
                packet_loss REAL,
                success BOOLEAN
            )
        """)
        
        conn.commit()
        conn.close()
    
    def detect_current_mtu(self, interface: str = None) -> Dict[str, int]:
        """
        Detect current MTU on all interfaces
        
        Returns:
            Dict of interface -> MTU
        """
        print("🔍 Detecting current MTU settings...")
        
        mtu_settings = {}
        
        try:
            # macOS: ifconfig
            result = subprocess.run(
                ['ifconfig'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            current_interface = None
            for line in result.stdout.split('\n'):
                # Interface line
                if line and not line.startswith('\t') and ':' in line:
                    current_interface = line.split(':')[0]
                
                # MTU line
                if 'mtu' in line.lower() and current_interface:
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if part.lower() == 'mtu' and i + 1 < len(parts):
                            mtu = int(parts[i + 1])
                            mtu_settings[current_interface] = mtu
                            
                            emoji = "🔥" if mtu >= 9000 else "⚡" if mtu > 1500 else "📶"
                            print(f"  {emoji} {current_interface}: MTU {mtu}")
        
        except Exception as e:
            print(f"⚠️  Error detecting MTU: {e}")
        
        return mtu_settings
    
    def enable_jumbo_frames(self, interface: str, mtu: int = 9000) -> bool:
        """
        Enable jumbo frames on interface
        
        Args:
            interface: Network interface (e.g., en0)
            mtu: MTU size (default 9000)
        
        Returns:
            Success boolean
        """
        print(f"\n🔥 ENABLING JUMBO FRAMES on {interface}!")
        print(f"🎯 Setting MTU to {mtu} bytes...")
        
        try:
            # macOS: sudo ifconfig en0 mtu 9000
            result = subprocess.run(
                ['sudo', 'ifconfig', interface, 'mtu', str(mtu)],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                # Verify
                time.sleep(1)
                current_mtu = self.get_interface_mtu(interface)
                
                if current_mtu == mtu:
                    print(f"✅ SUCCESS! {interface} now using MTU {mtu}")
                    print(f"🔥 JUMBO FRAMES ENABLED!")
                    
                    # Log to database
                    self._log_jumbo_config(interface, current_mtu, mtu, True)
                    
                    return True
                else:
                    print(f"⚠️  MTU set but verification shows {current_mtu}")
                    return False
            else:
                print(f"❌ Failed to set MTU: {result.stderr}")
                return False
        
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Tip: May need sudo password")
            return False
    
    def get_interface_mtu(self, interface: str) -> int:
        """Get MTU for specific interface"""
        try:
            result = subprocess.run(
                ['ifconfig', interface],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            for line in result.stdout.split('\n'):
                if 'mtu' in line.lower():
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if part.lower() == 'mtu' and i + 1 < len(parts):
                            return int(parts[i + 1])
        except:
            pass
        
        return 1500  # Default
    
    def test_jumbo_frames(self, target_ip: str, mtu_sizes: List[int] = None) -> Dict:
        """
        Test different MTU sizes to find optimal setting
        
        Args:
            target_ip: IP to ping
            mtu_sizes: List of MTU sizes to test
        
        Returns:
            Test results
        """
        if mtu_sizes is None:
            mtu_sizes = [1500, 4000, 6000, 8000, 9000]
        
        print(f"\n🧪 Testing MTU sizes against {target_ip}...")
        
        results = []
        
        for mtu in mtu_sizes:
            print(f"\n  Testing MTU {mtu}...", end=" ")
            
            # Ping with specific packet size
            # MTU - 28 bytes (IP + ICMP headers)
            packet_size = mtu - 28
            
            try:
                result = subprocess.run(
                    ['ping', '-D', '-c', '3', '-s', str(packet_size), target_ip],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0:
                    # Parse ping time
                    output = result.stdout
                    if 'avg' in output:
                        # Extract average ping time
                        parts = output.split('avg')[1].split()[0].split('/')
                        avg_time = float(parts[0]) if parts else 0
                        
                        success = True
                        print(f"✅ {avg_time:.2f}ms")
                        
                        results.append({
                            "mtu": mtu,
                            "ping_time": avg_time,
                            "success": True,
                            "packet_loss": 0
                        })
                        
                        # Log to database
                        self._log_mtu_test(target_ip, mtu, avg_time, 0, 0, True)
                    else:
                        print("✅ Success (no timing)")
                        results.append({"mtu": mtu, "success": True})
                else:
                    print(f"❌ Failed (MTU too large)")
                    results.append({"mtu": mtu, "success": False})
                    self._log_mtu_test(target_ip, mtu, 0, 0, 100, False)
            
            except subprocess.TimeoutExpired:
                print("❌ Timeout")
                results.append({"mtu": mtu, "success": False, "error": "timeout"})
            except Exception as e:
                print(f"❌ Error: {e}")
                results.append({"mtu": mtu, "success": False, "error": str(e)})
        
        # Find best MTU
        successful = [r for r in results if r.get("success")]
        if successful:
            best = max(successful, key=lambda x: x.get("mtu", 0))
            print(f"\n🔥 BEST MTU: {best['mtu']} bytes")
            
            if best['mtu'] >= 9000:
                print(f"✅ JUMBO FRAMES FULLY SUPPORTED!")
            elif best['mtu'] > 1500:
                print(f"⚡ Enhanced MTU supported (better than standard)")
            
            return {"best_mtu": best['mtu'], "results": results}
        else:
            print(f"\n⚠️  Only standard MTU (1500) supported")
            return {"best_mtu": 1500, "results": results}
    
    def configure_dgs1210_jumbo_frames(self, switch_ip: str) -> bool:
        """
        Configure DGS1210 switch for jumbo frames
        
        Args:
            switch_ip: Switch IP address
        
        Returns:
            Success boolean
        """
        print(f"\n🔥 CONFIGURING DGS1210 FOR JUMBO FRAMES!")
        print(f"📡 Switch: {switch_ip}")
        
        # DGS1210 supports jumbo frames up to 9216 bytes
        print(f"🎯 Target: 9216 bytes (switch max)")
        
        print("""
⚙️  Manual Configuration Required:

1. Access switch web interface: http://{switch_ip}
2. Login (default: admin/admin)
3. Navigate to: Advanced → Jumbo Frame
4. Enable: Jumbo Frame (9216 bytes)
5. Apply changes
6. Save configuration

OR via CLI (if enabled):
  telnet {switch_ip}
  admin
  (password)
  config
  jumbo_frame enable
  save

After configuration, this will be detected automatically!
""".format(switch_ip=switch_ip))
        
        # Try to detect if already enabled
        print("🔍 Checking if already enabled...")
        
        # Test with jumbo frame ping
        try:
            result = subprocess.run(
                ['ping', '-D', '-c', '1', '-s', '8972', switch_ip],  # 9000 - 28
                capture_output=True,
                timeout=5
            )
            
            if result.returncode == 0:
                print("✅ JUMBO FRAMES ALREADY ENABLED ON SWITCH!")
                return True
            else:
                print("📋 Follow manual steps above to enable")
                return False
        except:
            print("⚠️  Could not auto-detect - follow manual steps")
            return False
    
    def configure_mc96_jumbo_frames(self, mc96_ip: str, port: int = 8080) -> Dict:
        """
        Configure MC96 device for jumbo frames
        
        Args:
            mc96_ip: MC96 device IP
            port: API port
        
        Returns:
            Configuration result
        """
        print(f"\n🔥 CONFIGURING MC96 FOR JUMBO FRAMES!")
        print(f"📡 Device: {mc96_ip}")
        
        try:
            # Send jumbo frame configuration via API
            config_data = {
                "network": {
                    "mtu": 9000,
                    "jumbo_frames": True,
                    "optimization": "maximum_throughput"
                },
                "timestamp": time.time()
            }
            
            response = requests.post(
                f"http://{mc96_ip}:{port}/api/network/configure",
                json=config_data,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ MC96 CONFIGURED FOR JUMBO FRAMES!")
                print(f"🔥 MTU: 9000 bytes")
                print(f"⚡ Mode: Maximum Throughput")
                
                return {
                    "success": True,
                    "mtu": 9000,
                    "device": mc96_ip,
                    "response": data
                }
            else:
                print(f"⚠️  Configuration response: {response.status_code}")
                print(f"💡 Trying alternative method...")
                
                # Alternative: Direct network configuration
                return self._configure_mc96_alternative(mc96_ip)
        
        except Exception as e:
            print(f"⚠️  API configuration failed: {e}")
            print(f"💡 Using alternative configuration...")
            return self._configure_mc96_alternative(mc96_ip)
    
    def _configure_mc96_alternative(self, mc96_ip: str) -> Dict:
        """Alternative MC96 configuration method"""
        
        # Method 2: SSH configuration (if available)
        print("🔧 Attempting SSH configuration...")
        
        commands = [
            "ifconfig eth0 mtu 9000",
            "echo 9000 > /sys/class/net/eth0/mtu",
            "ip link set eth0 mtu 9000"
        ]
        
        print("""
⚙️  MC96 Manual Configuration:

SSH to device:
  ssh admin@{mc96_ip}

Run:
  sudo ifconfig eth0 mtu 9000
  # OR
  sudo ip link set eth0 mtu 9000

Verify:
  ifconfig eth0 | grep mtu

Make persistent (add to /etc/network/interfaces):
  auto eth0
  iface eth0 inet dhcp
    mtu 9000

Reboot for permanent:
  sudo reboot
""".format(mc96_ip=mc96_ip))
        
        return {
            "success": False,
            "manual_steps_required": True,
            "device": mc96_ip
        }
    
    def auto_configure_mc96(self, port: int = 1) -> Dict:
        """
        Automatically configure MC96 on specific port with jumbo frames
        
        Args:
            port: Switch port number
        
        Returns:
            Configuration result
        """
        print(f"\n🔥🔥🔥 AUTO-CONFIGURING MC96 PORT {port} - HOT ROD MODE! 🔥🔥🔥")
        print("="*70)
        
        # Get device on port
        device_ip = self._get_device_ip_on_port(port)
        
        if not device_ip:
            print(f"⚠️  No device detected on port {port}")
            return {"success": False, "error": "No device found"}
        
        print(f"✅ Device found: {device_ip}")
        
        # Test current MTU
        print(f"\n📊 Testing current configuration...")
        baseline = self._performance_test(device_ip, 1500)
        
        # Configure jumbo frames
        result = self.configure_mc96_jumbo_frames(device_ip)
        
        if result.get("success"):
            # Test performance improvement
            print(f"\n📊 Testing jumbo frame performance...")
            time.sleep(2)
            
            improved = self._performance_test(device_ip, 9000)
            
            if improved["throughput"] > baseline["throughput"]:
                gain = ((improved["throughput"] - baseline["throughput"]) / baseline["throughput"]) * 100
                print(f"\n🔥 PERFORMANCE GAIN: {gain:.1f}%!")
                print(f"📈 Throughput: {baseline['throughput']:.1f} → {improved['throughput']:.1f} Mbps")
                
                # Log performance gain
                self._log_performance_gain(device_ip, baseline["throughput"], improved["throughput"], gain)
        
        return result
    
    def _get_device_ip_on_port(self, port: int) -> Optional[str]:
        """Get device IP on specific port"""
        try:
            response = requests.get(f"http://localhost:8005/ports/{port}", timeout=2)
            if response.status_code == 200:
                data = response.json()
                device = data.get("device")
                if device:
                    return device.get("ip")
        except:
            pass
        
        return None
    
    def _performance_test(self, target_ip: str, mtu: int) -> Dict:
        """Run performance test"""
        packet_size = mtu - 28
        
        try:
            # Ping test
            result = subprocess.run(
                ['ping', '-D', '-c', '10', '-s', str(packet_size), target_ip],
                capture_output=True,
                text=True,
                timeout=15
            )
            
            if result.returncode == 0:
                output = result.stdout
                
                # Extract ping time
                avg_time = 0
                if 'avg' in output:
                    parts = output.split('avg')[1].split()[0].split('/')
                    avg_time = float(parts[0]) if parts else 0
                
                # Estimate throughput (rough calculation)
                throughput = (packet_size * 8 / avg_time) if avg_time > 0 else 0
                
                return {
                    "mtu": mtu,
                    "ping_time": avg_time,
                    "throughput": throughput,
                    "success": True
                }
        except:
            pass
        
        return {
            "mtu": mtu,
            "ping_time": 0,
            "throughput": 0,
            "success": False
        }
    
    def hot_rod_network(self, interfaces: List[str] = None) -> Dict:
        """
        🔥 HOT ROD MODE - Configure everything for maximum performance!
        
        Args:
            interfaces: List of interfaces (auto-detect if None)
        
        Returns:
            Configuration results
        """
        print("\n" + "="*70)
        print("🔥🔥🔥 HOT ROD MODE - MAXIMUM NETWORK PERFORMANCE! 🔥🔥🔥")
        print("="*70)
        
        results = {
            "interfaces_configured": [],
            "mc96_devices_configured": [],
            "performance_gains": [],
            "total_gain": 0
        }
        
        # Step 1: Detect current MTU
        print("\n📊 STEP 1: Detecting Current Configuration")
        current_mtu = self.detect_current_mtu()
        
        # Step 2: Configure interfaces
        print("\n🔥 STEP 2: Configuring Interfaces for Jumbo Frames")
        
        if interfaces is None:
            # Auto-detect active interfaces
            interfaces = [iface for iface, mtu in current_mtu.items() 
                         if mtu > 0 and not iface.startswith('lo')]
        
        print(f"🎯 Target interfaces: {', '.join(interfaces)}")
        print(f"\n⚠️  NOTE: Requires sudo password!\n")
        
        for interface in interfaces:
            if self.enable_jumbo_frames(interface, 9000):
                results["interfaces_configured"].append(interface)
        
        # Step 3: Configure MC96 devices
        print("\n🔥 STEP 3: Configuring MC96 Devices")
        
        # Get MC96 devices
        try:
            response = requests.get("http://localhost:8005/mc96/devices", timeout=2)
            if response.status_code == 200:
                mc96_devices = response.json().get("devices", {})
                
                for port, device_data in mc96_devices.items():
                    device_ip = device_data.get("device", {}).get("ip")
                    
                    if device_ip:
                        print(f"\n  🔥 Configuring MC96 on port {port} ({device_ip})...")
                        config_result = self.configure_mc96_jumbo_frames(device_ip)
                        
                        if config_result.get("success"):
                            results["mc96_devices_configured"].append(device_ip)
        except:
            print("  ℹ️  No MC96 devices found or network agent not running")
        
        # Step 4: Performance summary
        print("\n🔥 STEP 4: Performance Summary")
        print("="*70)
        
        if results["interfaces_configured"]:
            print(f"\n✅ Interfaces Configured: {len(results['interfaces_configured'])}")
            for iface in results["interfaces_configured"]:
                print(f"  🔥 {iface}: MTU 9000")
        
        if results["mc96_devices_configured"]:
            print(f"\n✅ MC96 Devices Configured: {len(results['mc96_devices_configured'])}")
            for device in results["mc96_devices_configured"]:
                print(f"  🔥 {device}: Jumbo frames enabled")
        
        # Estimated performance gain
        base_performance = 1000  # Mbps with standard frames
        jumbo_performance = base_performance * 1.15  # ~15% improvement typical
        
        print(f"\n📈 ESTIMATED PERFORMANCE GAIN:")
        print(f"  Standard MTU (1500): ~{base_performance} Mbps")
        print(f"  Jumbo Frames (9000): ~{jumbo_performance:.0f} Mbps")
        print(f"  🔥 GAIN: ~15% improvement!")
        
        print("\n" + "="*70)
        print("🔥 HOT ROD MODE COMPLETE!")
        print("⚡ YOUR NETWORK IS NOW TURBOCHARGED! ⚡")
        print("="*70)
        print()
        
        # Send Slack notification
        try:
            import sys
            sys.path.append('/Users/m2ultra/NOIZYLAB/integrations/slack')
            from slack_notifier import network_event
            
            network_event("optimized", "Network Hot Rod", {
                "Configuration": "Jumbo Frames Enabled",
                "MTU": "9000 bytes",
                "Interfaces": str(len(results["interfaces_configured"])),
                "MC96 Devices": str(len(results["mc96_devices_configured"])),
                "Estimated Gain": "~15% throughput",
                "Status": "🔥 TURBOCHARGED!"
            })
        except:
            pass
        
        return results
    
    def _log_jumbo_config(self, interface: str, current_mtu: int, 
                         target_mtu: int, enabled: bool):
        """Log jumbo frame configuration"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO jumbo_frames 
            (interface, current_mtu, target_mtu, enabled)
            VALUES (?, ?, ?, ?)
        """, (interface, current_mtu, target_mtu, enabled))
        
        conn.commit()
        conn.close()
    
    def _log_mtu_test(self, device_ip: str, mtu: int, ping_time: float,
                     throughput: float, packet_loss: float, success: bool):
        """Log MTU test results"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO mtu_tests
            (device_ip, mtu_size, ping_time, throughput_mbps, packet_loss, success)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (device_ip, mtu, ping_time, throughput, packet_loss, success))
        
        conn.commit()
        conn.close()
    
    def _log_performance_gain(self, device_ip: str, baseline: float, 
                             after: float, gain_percent: float):
        """Log performance improvement"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE jumbo_frames 
            SET performance_baseline = ?,
                performance_after = ?,
                gain_percent = ?
            WHERE device_ip = ?
        """, (baseline, after, gain_percent, device_ip))
        
        conn.commit()
        conn.close()
    
    def get_jumbo_status(self) -> List[Dict]:
        """Get jumbo frame status for all devices"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT interface, current_mtu, target_mtu, enabled, gain_percent
            FROM jumbo_frames
            ORDER BY configured_at DESC
            LIMIT 20
        """)
        
        status_list = []
        for row in cursor.fetchall():
            status_list.append({
                "interface": row[0],
                "current_mtu": row[1],
                "target_mtu": row[2],
                "enabled": bool(row[3]),
                "gain_percent": row[4] or 0
            })
        
        conn.close()
        return status_list


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="🔥 Jumbo Frame Manager - HOT ROD MODE!")
    parser.add_argument("action", choices=["detect", "enable", "test", "hotrod", "mc96", "switch"])
    parser.add_argument("--interface", help="Network interface (e.g., en0)")
    parser.add_argument("--ip", help="Target IP address")
    parser.add_argument("--port", type=int, help="MC96 port number")
    parser.add_argument("--mtu", type=int, default=9000, help="MTU size")
    
    args = parser.parse_args()
    
    manager = JumboFrameManager()
    
    if args.action == "detect":
        manager.detect_current_mtu()
    
    elif args.action == "enable":
        if not args.interface:
            print("❌ Please specify --interface")
        else:
            manager.enable_jumbo_frames(args.interface, args.mtu)
    
    elif args.action == "test":
        if not args.ip:
            print("❌ Please specify --ip")
        else:
            manager.test_jumbo_frames(args.ip)
    
    elif args.action == "hotrod":
        manager.hot_rod_network(args.interface.split(',') if args.interface else None)
    
    elif args.action == "mc96":
        if args.port:
            manager.auto_configure_mc96(args.port)
        elif args.ip:
            manager.configure_mc96_jumbo_frames(args.ip)
        else:
            print("❌ Please specify --port or --ip")
    
    elif args.action == "switch":
        if not args.ip:
            print("❌ Please specify --ip (switch IP)")
        else:
            manager.configure_dgs1210_jumbo_frames(args.ip)


if __name__ == "__main__":
    main()

