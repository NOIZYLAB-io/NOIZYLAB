#!/usr/bin/env python3
"""
NoizyLab DGS1210-10 Auto-Handshake System
==========================================
Automatically detects device connections and initiates handshake protocols with MC96
"""

import asyncio
import time
import json
import sqlite3
import requests
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import subprocess
import socket
import struct
from dataclasses import dataclass, asdict

# SNMP libraries (install with: pip install pysnmp)
try:
    from pysnmp.hlapi import *
    SNMP_AVAILABLE = True
except ImportError:
    SNMP_AVAILABLE = False
    print("⚠️ pysnmp not installed. Install with: pip install pysnmp")

# Import Slack notifier
import sys
sys.path.append(str(Path(__file__).parent.parent / "integrations" / "slack"))
try:
    from slack_notifier import network_event, alert
    SLACK_AVAILABLE = True
except:
    SLACK_AVAILABLE = False
    print("⚠️ Slack integration not available")


@dataclass
class NetworkDevice:
    """Represents a connected network device"""
    mac_address: str
    ip_address: str
    port: int
    hostname: Optional[str] = None
    vendor: Optional[str] = None
    first_seen: datetime = None
    last_seen: datetime = None
    status: str = "connected"
    handshake_status: str = "pending"
    
    def __post_init__(self):
        if self.first_seen is None:
            self.first_seen = datetime.now()
        if self.last_seen is None:
            self.last_seen = datetime.now()


@dataclass
class HandshakeResult:
    """Result of a handshake attempt"""
    success: bool
    device: NetworkDevice
    timestamp: datetime
    mc96_response: Optional[Dict] = None
    error: Optional[str] = None


class DGS1210Monitor:
    """Monitor for D-Link DGS1210-10 Switch"""
    
    def __init__(self, switch_ip: str = "192.168.1.1", community: str = "public"):
        """
        Initialize DGS1210 Monitor
        
        Args:
            switch_ip: IP address of the DGS1210-10 switch
            community: SNMP community string
        """
        self.switch_ip = switch_ip
        self.community = community
        self.mc96_url = "http://localhost:8096"  # MC96 API endpoint
        
        # Database for tracking devices
        self.db_path = Path(__file__).parent / "network_devices.db"
        self._init_database()
        
        # Current device state
        self.devices: Dict[str, NetworkDevice] = {}
        self.monitoring = False
        
        # Load previous state
        self._load_devices_from_db()
    
    def _init_database(self):
        """Initialize SQLite database for device tracking"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS network_devices (
                mac_address TEXT PRIMARY KEY,
                ip_address TEXT,
                port INTEGER,
                hostname TEXT,
                vendor TEXT,
                first_seen DATETIME,
                last_seen DATETIME,
                status TEXT,
                handshake_status TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS handshake_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mac_address TEXT,
                ip_address TEXT,
                success BOOLEAN,
                mc96_response TEXT,
                error TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS port_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                port INTEGER,
                event_type TEXT,
                mac_address TEXT,
                ip_address TEXT,
                details TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def _load_devices_from_db(self):
        """Load previously known devices from database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT mac_address, ip_address, port, hostname, vendor, 
                   first_seen, last_seen, status, handshake_status
            FROM network_devices
        """)
        
        for row in cursor.fetchall():
            device = NetworkDevice(
                mac_address=row[0],
                ip_address=row[1],
                port=row[2],
                hostname=row[3],
                vendor=row[4],
                first_seen=datetime.fromisoformat(row[5]) if row[5] else None,
                last_seen=datetime.fromisoformat(row[6]) if row[6] else None,
                status=row[7],
                handshake_status=row[8]
            )
            self.devices[device.mac_address] = device
        
        conn.close()
        print(f"📚 Loaded {len(self.devices)} known devices from database")
    
    def _save_device_to_db(self, device: NetworkDevice):
        """Save device to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO network_devices 
            (mac_address, ip_address, port, hostname, vendor, first_seen, last_seen, status, handshake_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            device.mac_address,
            device.ip_address,
            device.port,
            device.hostname,
            device.vendor,
            device.first_seen.isoformat() if device.first_seen else None,
            device.last_seen.isoformat() if device.last_seen else None,
            device.status,
            device.handshake_status
        ))
        
        conn.commit()
        conn.close()
    
    def _log_port_event(self, port: int, event_type: str, mac: str = "", ip: str = "", details: Dict = None):
        """Log port event to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO port_events (port, event_type, mac_address, ip_address, details)
            VALUES (?, ?, ?, ?, ?)
        """, (port, event_type, mac, ip, json.dumps(details) if details else None))
        
        conn.commit()
        conn.close()
    
    def _log_handshake(self, result: HandshakeResult):
        """Log handshake result to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO handshake_history (mac_address, ip_address, success, mc96_response, error)
            VALUES (?, ?, ?, ?, ?)
        """, (
            result.device.mac_address,
            result.device.ip_address,
            result.success,
            json.dumps(result.mc96_response) if result.mc96_response else None,
            result.error
        ))
        
        conn.commit()
        conn.close()
    
    async def get_switch_port_status(self) -> Dict[int, Dict]:
        """Get status of all switch ports via SNMP"""
        if not SNMP_AVAILABLE:
            print("⚠️ SNMP not available, using fallback method")
            return await self._fallback_port_scan()
        
        port_status = {}
        
        # OIDs for DGS1210-10
        port_status_oid = '1.3.6.1.2.1.2.2.1.8'  # ifOperStatus
        port_speed_oid = '1.3.6.1.2.1.2.2.1.5'   # ifSpeed
        
        try:
            # Get port operational status
            for port in range(1, 11):  # DGS1210-10 has 10 ports
                iterator = getCmd(
                    SnmpEngine(),
                    CommunityData(self.community),
                    UdpTransportTarget((self.switch_ip, 161)),
                    ContextData(),
                    ObjectType(ObjectIdentity(port_status_oid + f'.{port}'))
                )
                
                errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
                
                if errorIndication or errorStatus:
                    continue
                
                for varBind in varBinds:
                    status_value = int(varBind[1])
                    port_status[port] = {
                        'status': 'up' if status_value == 1 else 'down',
                        'link': status_value == 1
                    }
        
        except Exception as e:
            print(f"⚠️ SNMP error: {e}, falling back to scan")
            return await self._fallback_port_scan()
        
        return port_status
    
    async def _fallback_port_scan(self) -> Dict[int, Dict]:
        """Fallback method when SNMP is not available"""
        # Scan local network for connected devices
        port_status = {}
        
        # Use ARP to discover devices
        try:
            result = subprocess.run(
                ['arp', '-a'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                active_count = 0
                
                for line in lines:
                    if '192.168.' in line or '10.' in line:
                        active_count += 1
                
                # Simulate port distribution
                for port in range(1, 11):
                    port_status[port] = {
                        'status': 'up' if port <= active_count else 'down',
                        'link': port <= active_count
                    }
        
        except Exception as e:
            print(f"⚠️ Fallback scan error: {e}")
        
        return port_status
    
    async def get_port_mac_addresses(self) -> Dict[int, str]:
        """Get MAC addresses for each port"""
        port_macs = {}
        
        # Use ARP table to get MAC addresses
        try:
            result = subprocess.run(
                ['arp', '-a'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                port = 1
                
                for line in lines:
                    # Parse ARP output
                    parts = line.split()
                    if len(parts) >= 4:
                        ip = parts[1].strip('()')
                        mac = parts[3]
                        
                        if ':' in mac or '-' in mac:
                            port_macs[port] = {
                                'mac': mac.replace('-', ':').lower(),
                                'ip': ip
                            }
                            port = (port % 10) + 1
        
        except Exception as e:
            print(f"⚠️ Error getting MAC addresses: {e}")
        
        return port_macs
    
    async def detect_new_device(self, port: int, mac: str, ip: str) -> NetworkDevice:
        """Detect and register a new device"""
        # Check if device is already known
        if mac in self.devices:
            device = self.devices[mac]
            device.last_seen = datetime.now()
            device.status = "connected"
            return device
        
        # Create new device
        hostname = await self._resolve_hostname(ip)
        vendor = self._identify_vendor(mac)
        
        device = NetworkDevice(
            mac_address=mac,
            ip_address=ip,
            port=port,
            hostname=hostname,
            vendor=vendor
        )
        
        self.devices[mac] = device
        self._save_device_to_db(device)
        
        print(f"🆕 New device detected: {mac} on port {port}")
        
        return device
    
    async def _resolve_hostname(self, ip: str) -> Optional[str]:
        """Resolve hostname from IP address"""
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except:
            return None
    
    def _identify_vendor(self, mac: str) -> Optional[str]:
        """Identify device vendor from MAC address"""
        # MAC address OUI lookup (first 6 characters)
        oui = mac[:8].upper().replace(':', '')
        
        # Common vendors (expandable)
        oui_database = {
            '001122': 'Cisco',
            'A4C494': 'Apple',
            '00D861': 'Apple',
            'D89695': 'Raspberry Pi',
            'B827EB': 'Raspberry Pi',
            'DC233A': 'Raspberry Pi',
            '001E58': 'D-Link',
            '00055D': 'D-Link',
            '74DA38': 'Espressif (ESP32)',
            '30AEA4': 'Espressif (ESP32)'
        }
        
        return oui_database.get(oui)
    
    async def initiate_mc96_handshake(self, device: NetworkDevice) -> HandshakeResult:
        """
        Initiate handshake with MC96 system for new device
        
        Args:
            device: NetworkDevice object
        
        Returns:
            HandshakeResult with success status and response
        """
        print(f"🤝 Initiating MC96 handshake for {device.mac_address}...")
        
        result = HandshakeResult(
            success=False,
            device=device,
            timestamp=datetime.now()
        )
        
        try:
            # Prepare handshake payload
            payload = {
                'action': 'device_handshake',
                'device': {
                    'mac_address': device.mac_address,
                    'ip_address': device.ip_address,
                    'port': device.port,
                    'hostname': device.hostname,
                    'vendor': device.vendor,
                    'timestamp': datetime.now().isoformat()
                },
                'switch': {
                    'ip': self.switch_ip,
                    'model': 'DGS1210-10'
                }
            }
            
            # Send handshake request to MC96
            response = requests.post(
                f"{self.mc96_url}/api/handshake",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                result.success = True
                result.mc96_response = response.json()
                device.handshake_status = "completed"
                
                print(f"✅ Handshake successful with {device.mac_address}")
                
                # Notify via Slack
                if SLACK_AVAILABLE:
                    network_event(
                        "handshake",
                        device.hostname or device.mac_address,
                        {
                            "IP Address": device.ip_address,
                            "MAC Address": device.mac_address,
                            "Port": f"Port {device.port}",
                            "Vendor": device.vendor or "Unknown",
                            "Status": "✅ Handshake Successful"
                        }
                    )
            
            else:
                result.error = f"MC96 returned status {response.status_code}"
                device.handshake_status = "failed"
                print(f"❌ Handshake failed: {result.error}")
        
        except requests.exceptions.ConnectionError:
            result.error = "MC96 not reachable"
            device.handshake_status = "pending"
            print(f"⚠️ MC96 not available, will retry later")
        
        except Exception as e:
            result.error = str(e)
            device.handshake_status = "error"
            print(f"❌ Handshake error: {e}")
        
        # Update device in database
        self._save_device_to_db(device)
        
        # Log handshake attempt
        self._log_handshake(result)
        
        return result
    
    async def handle_device_connection(self, port: int, mac: str, ip: str):
        """Handle a new device connection event"""
        print(f"🔌 Device connected on port {port}: {mac} ({ip})")
        
        # Log event
        self._log_port_event(port, "connected", mac, ip)
        
        # Detect/register device
        device = await self.detect_new_device(port, mac, ip)
        
        # Send Slack notification
        if SLACK_AVAILABLE:
            network_event(
                "connected",
                device.hostname or device.mac_address,
                {
                    "IP Address": device.ip_address,
                    "MAC Address": device.mac_address,
                    "Port": f"Port {device.port}",
                    "Vendor": device.vendor or "Unknown",
                    "First Seen": device.first_seen.strftime("%Y-%m-%d %H:%M:%S")
                }
            )
        
        # Initiate MC96 handshake
        handshake_result = await self.initiate_mc96_handshake(device)
        
        # Additional device-specific initialization
        await self._initialize_device_services(device, handshake_result)
    
    async def _initialize_device_services(self, device: NetworkDevice, handshake: HandshakeResult):
        """Initialize device-specific services after handshake"""
        if not handshake.success:
            return
        
        print(f"🚀 Initializing services for {device.mac_address}...")
        
        # Device-specific initialization based on vendor or type
        if device.vendor == "Raspberry Pi":
            await self._init_raspberry_pi(device)
        elif device.vendor == "Apple":
            await self._init_apple_device(device)
        elif "ESP" in str(device.vendor):
            await self._init_iot_device(device)
        
        print(f"✅ Services initialized for {device.mac_address}")
    
    async def _init_raspberry_pi(self, device: NetworkDevice):
        """Initialize Raspberry Pi specific services"""
        # SSH availability check
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((device.ip_address, 22))
            sock.close()
            
            if result == 0:
                print(f"  🔐 SSH available on {device.ip_address}")
        except:
            pass
    
    async def _init_apple_device(self, device: NetworkDevice):
        """Initialize Apple device specific services"""
        print(f"  🍎 Apple device detected: {device.hostname or device.ip_address}")
    
    async def _init_iot_device(self, device: NetworkDevice):
        """Initialize IoT device specific services"""
        # Check for common IoT ports
        ports_to_check = [80, 443, 8080, 1883]  # HTTP, HTTPS, Alt HTTP, MQTT
        
        for port in ports_to_check:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((device.ip_address, port))
                sock.close()
                
                if result == 0:
                    print(f"  🌐 IoT service on port {port}")
            except:
                pass
    
    async def handle_device_disconnection(self, port: int, mac: str):
        """Handle device disconnection event"""
        if mac in self.devices:
            device = self.devices[mac]
            device.status = "disconnected"
            device.last_seen = datetime.now()
            
            self._save_device_to_db(device)
            self._log_port_event(port, "disconnected", mac, device.ip_address)
            
            print(f"🔴 Device disconnected from port {port}: {mac}")
            
            # Send Slack notification
            if SLACK_AVAILABLE:
                network_event(
                    "disconnected",
                    device.hostname or device.mac_address,
                    {
                        "IP Address": device.ip_address,
                        "MAC Address": device.mac_address,
                        "Port": f"Port {port}",
                        "Duration": str(device.last_seen - device.first_seen)
                    }
                )
    
    async def monitor_loop(self, interval: int = 5):
        """Main monitoring loop"""
        print(f"🎛️ Starting DGS1210 monitor (checking every {interval}s)...")
        print(f"📡 Switch IP: {self.switch_ip}")
        print(f"🔗 MC96 URL: {self.mc96_url}")
        
        self.monitoring = True
        previous_state = {}
        
        # Send startup notification
        if SLACK_AVAILABLE:
            alert(
                f"🚀 DGS1210-10 Monitor started\nSwitch: {self.switch_ip}\nInterval: {interval}s",
                level="info"
            )
        
        while self.monitoring:
            try:
                # Get current port status
                port_status = await self.get_switch_port_status()
                port_macs = await self.get_port_mac_addresses()
                
                # Check for changes
                for port, status in port_status.items():
                    current_link = status.get('link', False)
                    previous_link = previous_state.get(port, {}).get('link', False)
                    
                    # Device connected (link up)
                    if current_link and not previous_link:
                        if port in port_macs:
                            mac_info = port_macs[port]
                            await self.handle_device_connection(
                                port,
                                mac_info['mac'],
                                mac_info['ip']
                            )
                    
                    # Device disconnected (link down)
                    elif not current_link and previous_link:
                        if port in port_macs:
                            mac_info = port_macs[port]
                            await self.handle_device_disconnection(port, mac_info['mac'])
                
                previous_state = port_status
                
                # Wait for next check
                await asyncio.sleep(interval)
            
            except KeyboardInterrupt:
                print("\n🛑 Monitor stopped by user")
                break
            
            except Exception as e:
                print(f"❌ Monitor error: {e}")
                await asyncio.sleep(interval)
        
        # Send shutdown notification
        if SLACK_AVAILABLE:
            alert("🛑 DGS1210-10 Monitor stopped", level="warning")
    
    def stop_monitoring(self):
        """Stop the monitoring loop"""
        self.monitoring = False
    
    def get_all_devices(self) -> List[NetworkDevice]:
        """Get all known devices"""
        return list(self.devices.values())
    
    def get_active_devices(self) -> List[NetworkDevice]:
        """Get currently connected devices"""
        return [d for d in self.devices.values() if d.status == "connected"]
    
    def get_device_by_mac(self, mac: str) -> Optional[NetworkDevice]:
        """Get device by MAC address"""
        return self.devices.get(mac)


async def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="DGS1210-10 Auto-Handshake Monitor")
    parser.add_argument("--switch-ip", default="192.168.1.1", help="Switch IP address")
    parser.add_argument("--community", default="public", help="SNMP community string")
    parser.add_argument("--interval", type=int, default=5, help="Check interval in seconds")
    parser.add_argument("--mc96-url", default="http://localhost:8096", help="MC96 API URL")
    
    args = parser.parse_args()
    
    # Create monitor
    monitor = DGS1210Monitor(switch_ip=args.switch_ip, community=args.community)
    monitor.mc96_url = args.mc96_url
    
    # Start monitoring
    try:
        await monitor.monitor_loop(interval=args.interval)
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
        monitor.stop_monitoring()


if __name__ == "__main__":
    asyncio.run(main())

