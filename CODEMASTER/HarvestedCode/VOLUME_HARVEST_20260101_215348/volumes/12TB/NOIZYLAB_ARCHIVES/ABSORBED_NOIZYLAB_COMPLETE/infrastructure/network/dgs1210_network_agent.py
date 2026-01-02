#!/usr/bin/env python3
"""
DGS1210-10 Network Agent - Advanced Device Detection & Handshake System
========================================================================
Monitors switch ports, detects device connections, and triggers automatic handshakes
"""

import time
import json
import socket
import struct
import subprocess
import threading
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from pathlib import Path
import sqlite3
from pysnmp.hlapi import *
import netifaces
import requests

# Import Slack notifier
import sys
sys.path.append('/Users/m2ultra/NOIZYLAB/integrations/slack')
from slack_notifier import network_event, alert


@dataclass
class ConnectedDevice:
    """Represents a connected device"""
    mac_address: str
    ip_address: Optional[str]
    port: int
    hostname: Optional[str]
    vendor: Optional[str]
    first_seen: datetime
    last_seen: datetime
    device_type: Optional[str] = None
    status: str = "active"


@dataclass
class HandshakeResult:
    """Result of device handshake"""
    success: bool
    device: ConnectedDevice
    handshake_type: str
    response_time: float
    details: Dict[str, Any]
    timestamp: datetime


class DGS1210Agent:
    """
    Advanced network monitoring agent for DGS1210-10 switch
    Detects device connections and triggers automatic handshakes
    """
    
    def __init__(self, switch_ip: str = "192.168.1.1", community: str = "public"):
        """
        Initialize DGS1210 Agent
        
        Args:
            switch_ip: IP address of DGS1210 switch
            community: SNMP community string
        """
        self.switch_ip = switch_ip
        self.community = community
        self.monitoring = False
        self.devices: Dict[str, ConnectedDevice] = {}
        
        # Database setup
        self.db_path = Path(__file__).parent / "network_devices.db"
        self._init_database()
        
        # MC96 configuration
        self.mc96_ports = [1, 2, 3]  # Ports where MC96 devices connect
        self.mc96_devices: Dict[int, Dict] = {}
        
        # Handshake protocols
        self.handshake_handlers = {
            "mc96": self._handshake_mc96,
            "generic": self._handshake_generic,
            "http": self._handshake_http,
            "ssh": self._handshake_ssh,
            "ping": self._handshake_ping
        }
        
        # Port monitoring state
        self.port_states: Dict[int, Dict] = {}
        for port in range(1, 11):  # DGS1210-10 has 10 ports
            self.port_states[port] = {
                "link_status": "down",
                "speed": 0,
                "device": None,
                "last_change": datetime.now()
            }
        
        print(f"🌐 DGS1210 Network Agent initialized")
        print(f"📡 Monitoring switch: {switch_ip}")
        print(f"💾 Database: {self.db_path}")
    
    def _init_database(self):
        """Initialize SQLite database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Devices table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS network_devices (
                mac_address TEXT PRIMARY KEY,
                ip_address TEXT,
                port INTEGER,
                hostname TEXT,
                vendor TEXT,
                device_type TEXT,
                first_seen DATETIME,
                last_seen DATETIME,
                status TEXT
            )
        """)
        
        # Port events table
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
        
        # Handshake log table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS handshake_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_mac TEXT,
                device_ip TEXT,
                handshake_type TEXT,
                success BOOLEAN,
                response_time REAL,
                details TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # MC96 devices table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mc96_devices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                port INTEGER,
                mac_address TEXT,
                ip_address TEXT,
                device_name TEXT,
                handshake_status TEXT,
                last_handshake DATETIME,
                configuration TEXT,
                status TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    
    def start_monitoring(self, interval: int = 5):
        """
        Start monitoring switch ports
        
        Args:
            interval: Polling interval in seconds
        """
        self.monitoring = True
        print(f"🚀 Starting port monitoring (interval: {interval}s)")
        
        # Send startup notification
        alert("Network monitoring started", "success")
        
        monitor_thread = threading.Thread(target=self._monitor_loop, args=(interval,))
        monitor_thread.daemon = True
        monitor_thread.start()
        
        return monitor_thread
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.monitoring = False
        print("🛑 Stopping port monitoring")
        alert("Network monitoring stopped", "info")
    
    def _monitor_loop(self, interval: int):
        """Main monitoring loop"""
        print("👀 Monitoring loop started")
        
        while self.monitoring:
            try:
                # Check all ports
                for port in range(1, 11):
                    self._check_port(port)
                
                # Check ARP table for new devices
                self._scan_arp_table()
                
                # Clean up stale devices
                self._cleanup_stale_devices()
                
                time.sleep(interval)
                
            except Exception as e:
                print(f"❌ Monitoring error: {e}")
                time.sleep(interval)
    
    def _check_port(self, port: int):
        """
        Check port status via SNMP
        
        Args:
            port: Port number (1-10)
        """
        try:
            # Query port status using SNMP
            # OID for ifOperStatus (1.3.6.1.2.1.2.2.1.8.{port})
            iterator = getCmd(
                SnmpEngine(),
                CommunityData(self.community),
                UdpTransportTarget((self.switch_ip, 161), timeout=2, retries=1),
                ContextData(),
                ObjectType(ObjectIdentity(f'1.3.6.1.2.1.2.2.1.8.{port}'))
            )
            
            errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
            
            if errorIndication:
                return
            
            if errorStatus:
                return
            
            # Get port status (1=up, 2=down)
            for varBind in varBinds:
                status_value = int(varBind[1])
                new_status = "up" if status_value == 1 else "down"
                old_status = self.port_states[port]["link_status"]
                
                # Detect status change
                if new_status != old_status:
                    self._handle_port_change(port, old_status, new_status)
                    self.port_states[port]["link_status"] = new_status
                    self.port_states[port]["last_change"] = datetime.now()
        
        except Exception as e:
            # Silent fail for SNMP errors (switch might not have SNMP enabled)
            pass
    
    def _handle_port_change(self, port: int, old_status: str, new_status: str):
        """
        Handle port status change
        
        Args:
            port: Port number
            old_status: Previous status
            new_status: New status
        """
        print(f"\n{'🟢' if new_status == 'up' else '🔴'} Port {port}: {old_status} → {new_status}")
        
        # Log event to database
        self._log_port_event(port, f"link_{new_status}", None, None, {
            "old_status": old_status,
            "new_status": new_status
        })
        
        if new_status == "up":
            # Device connected
            print(f"🔌 Device connected to port {port}")
            
            # Send Slack notification
            network_event(
                "connected",
                f"Port {port}",
                {
                    "Port": str(port),
                    "Status": "Link Up",
                    "Switch": self.switch_ip,
                    "Time": datetime.now().strftime("%H:%M:%S")
                }
            )
            
            # Wait a moment for device to initialize
            time.sleep(2)
            
            # Trigger device detection and handshake
            threading.Thread(
                target=self._detect_and_handshake,
                args=(port,),
                daemon=True
            ).start()
        
        else:
            # Device disconnected
            print(f"🔴 Device disconnected from port {port}")
            
            device = self.port_states[port].get("device")
            if device:
                network_event(
                    "disconnected",
                    device.hostname or device.mac_address,
                    {
                        "Port": str(port),
                        "Device": device.hostname or "Unknown",
                        "MAC": device.mac_address,
                        "Time": datetime.now().strftime("%H:%M:%S")
                    }
                )
            
            # Clear port state
            self.port_states[port]["device"] = None
    
    def _detect_and_handshake(self, port: int):
        """
        Detect connected device and perform handshake
        
        Args:
            port: Port number
        """
        print(f"🔍 Detecting device on port {port}...")
        
        # Wait for device to fully connect
        time.sleep(3)
        
        # Scan for device MAC/IP
        device = self._discover_device_on_port(port)
        
        if device:
            print(f"✅ Device discovered: {device.hostname or device.mac_address}")
            
            # Store device
            self.devices[device.mac_address] = device
            self.port_states[port]["device"] = device
            self._save_device_to_db(device)
            
            # Determine device type and appropriate handshake
            handshake_type = self._determine_handshake_type(device, port)
            
            print(f"🤝 Initiating {handshake_type} handshake...")
            
            # Perform handshake
            result = self._perform_handshake(device, handshake_type)
            
            # Log handshake result
            self._log_handshake(result)
            
            if result.success:
                print(f"✅ Handshake successful ({result.response_time:.2f}s)")
                
                network_event(
                    "handshake",
                    device.hostname or device.mac_address,
                    {
                        "Port": str(port),
                        "Device": device.hostname or "Unknown",
                        "MAC": device.mac_address,
                        "IP": device.ip_address or "Unknown",
                        "Type": handshake_type,
                        "Response Time": f"{result.response_time:.2f}s",
                        "Status": "✅ Success"
                    }
                )
                
                # If it's an MC96 device, register it
                if port in self.mc96_ports:
                    self._register_mc96_device(port, device, result)
            else:
                print(f"❌ Handshake failed")
                alert(
                    f"Handshake failed for device on port {port}",
                    "warning"
                )
        else:
            print(f"⚠️ Could not detect device on port {port}")
    
    def _discover_device_on_port(self, port: int) -> Optional[ConnectedDevice]:
        """
        Discover device on specific port
        
        Args:
            port: Port number
        
        Returns:
            ConnectedDevice if found
        """
        # Try multiple discovery methods
        
        # Method 1: Check ARP table
        devices = self._scan_arp_table()
        if devices:
            # For now, associate first discovered device
            # In production, you'd use switch MAC table via SNMP
            device = devices[0]
            device.port = port
            return device
        
        # Method 2: Port scan local network
        local_ip = self._get_local_ip()
        if local_ip:
            discovered = self._scan_network(local_ip)
            if discovered:
                device = discovered[0]
                device.port = port
                return device
        
        return None
    
    def _scan_arp_table(self) -> List[ConnectedDevice]:
        """Scan system ARP table for devices"""
        devices = []
        
        try:
            result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            
            for line in lines:
                if '(' in line and ')' in line:
                    parts = line.split()
                    if len(parts) >= 4:
                        hostname = parts[0] if parts[0] != '?' else None
                        ip = parts[1].strip('()')
                        mac = parts[3]
                        
                        if mac != '(incomplete)' and ':' in mac:
                            device = ConnectedDevice(
                                mac_address=mac,
                                ip_address=ip,
                                port=0,  # Unknown port
                                hostname=hostname,
                                vendor=self._lookup_vendor(mac),
                                first_seen=datetime.now(),
                                last_seen=datetime.now()
                            )
                            devices.append(device)
        except Exception as e:
            print(f"⚠️ ARP scan error: {e}")
        
        return devices
    
    def _scan_network(self, local_ip: str) -> List[ConnectedDevice]:
        """Scan local network for devices"""
        devices = []
        
        try:
            # Get network prefix (e.g., 192.168.1)
            prefix = '.'.join(local_ip.split('.')[:-1])
            
            # Quick ping scan of common IPs
            for i in [1, 2, 3, 10, 20, 100]:
                ip = f"{prefix}.{i}"
                if self._ping_host(ip, timeout=0.5):
                    device = ConnectedDevice(
                        mac_address="unknown",
                        ip_address=ip,
                        port=0,
                        hostname=self._get_hostname(ip),
                        vendor=None,
                        first_seen=datetime.now(),
                        last_seen=datetime.now()
                    )
                    devices.append(device)
        except Exception as e:
            print(f"⚠️ Network scan error: {e}")
        
        return devices
    
    def _determine_handshake_type(self, device: ConnectedDevice, port: int) -> str:
        """
        Determine appropriate handshake type
        
        Args:
            device: Connected device
            port: Port number
        
        Returns:
            Handshake type
        """
        # Check if it's an MC96 port
        if port in self.mc96_ports:
            return "mc96"
        
        # Try to detect device type by vendor or hostname
        if device.vendor and "apple" in device.vendor.lower():
            return "generic"
        
        if device.hostname:
            hostname_lower = device.hostname.lower()
            if "mc96" in hostname_lower:
                return "mc96"
            elif "server" in hostname_lower:
                return "ssh"
            elif "web" in hostname_lower:
                return "http"
        
        # Default: try ping first, then generic
        if device.ip_address:
            return "ping"
        
        return "generic"
    
    def _perform_handshake(self, device: ConnectedDevice, handshake_type: str) -> HandshakeResult:
        """
        Perform device handshake
        
        Args:
            device: Device to handshake with
            handshake_type: Type of handshake
        
        Returns:
            HandshakeResult
        """
        start_time = time.time()
        
        handler = self.handshake_handlers.get(handshake_type, self._handshake_generic)
        success, details = handler(device)
        
        response_time = time.time() - start_time
        
        return HandshakeResult(
            success=success,
            device=device,
            handshake_type=handshake_type,
            response_time=response_time,
            details=details,
            timestamp=datetime.now()
        )
    
    def _handshake_mc96(self, device: ConnectedDevice) -> Tuple[bool, Dict]:
        """
        MC96-specific handshake protocol with JUMBO FRAME SUPPORT! 🔥
        
        Args:
            device: Connected device
        
        Returns:
            (success, details)
        """
        details = {"protocol": "MC96 Custom + Jumbo Frames 🔥"}
        
        if not device.ip_address:
            return False, {"error": "No IP address"}
        
        try:
            # Step 1: Ping check
            if not self._ping_host(device.ip_address):
                return False, {"error": "Ping failed"}
            
            details["ping"] = "✅ Success"
            
            # Step 2: Try HTTP connection (MC96 web interface)
            try:
                response = requests.get(
                    f"http://{device.ip_address}",
                    timeout=3
                )
                details["http_status"] = response.status_code
                details["http"] = "✅ Success"
            except:
                details["http"] = "❌ Failed"
            
            # Step 3: Check for MC96 API endpoint
            try:
                response = requests.get(
                    f"http://{device.ip_address}:8080/api/status",
                    timeout=2
                )
                if response.status_code == 200:
                    data = response.json()
                    details["api"] = "✅ Connected"
                    details["device_info"] = data
            except:
                details["api"] = "⚠️ Not available"
            
            # Step 4: Configure JUMBO FRAMES! 🔥
            try:
                jumbo_response = requests.post(
                    f"http://{device.ip_address}:8080/api/network/configure",
                    json={
                        "mtu": 9000,
                        "jumbo_frames": True,
                        "optimization": "maximum_throughput",
                        "timestamp": datetime.now().isoformat()
                    },
                    timeout=3
                )
                if jumbo_response.status_code == 200:
                    details["jumbo_frames"] = "🔥 ENABLED (MTU 9000)!"
                else:
                    details["jumbo_frames"] = "⚠️ Manual config needed"
            except:
                details["jumbo_frames"] = "⚠️ Manual config needed"
            
            # Step 5: Send initialization command
            try:
                init_response = requests.post(
                    f"http://{device.ip_address}:8080/api/init",
                    json={
                        "source": "noizylab",
                        "jumbo_frames_enabled": True,
                        "mtu": 9000,
                        "timestamp": datetime.now().isoformat()
                    },
                    timeout=2
                )
                details["initialization"] = "✅ Complete (Hot Rod Mode!)"
            except:
                details["initialization"] = "⚠️ Skipped"
            
            return True, details
        
        except Exception as e:
            return False, {"error": str(e)}
    
    def _handshake_generic(self, device: ConnectedDevice) -> Tuple[bool, Dict]:
        """Generic handshake protocol"""
        if device.ip_address and self._ping_host(device.ip_address):
            return True, {"ping": "success", "method": "generic"}
        return False, {"error": "Ping failed"}
    
    def _handshake_http(self, device: ConnectedDevice) -> Tuple[bool, Dict]:
        """HTTP handshake protocol"""
        if not device.ip_address:
            return False, {"error": "No IP"}
        
        try:
            response = requests.get(f"http://{device.ip_address}", timeout=3)
            return True, {
                "status_code": response.status_code,
                "server": response.headers.get("Server", "Unknown")
            }
        except:
            return False, {"error": "HTTP connection failed"}
    
    def _handshake_ssh(self, device: ConnectedDevice) -> Tuple[bool, Dict]:
        """SSH handshake protocol"""
        if not device.ip_address:
            return False, {"error": "No IP"}
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((device.ip_address, 22))
            sock.close()
            
            if result == 0:
                return True, {"ssh_port": "open"}
            return False, {"ssh_port": "closed"}
        except:
            return False, {"error": "SSH check failed"}
    
    def _handshake_ping(self, device: ConnectedDevice) -> Tuple[bool, Dict]:
        """Ping-based handshake"""
        if device.ip_address and self._ping_host(device.ip_address):
            return True, {"ping": "success"}
        return False, {"error": "Ping failed"}
    
    def _ping_host(self, ip: str, timeout: float = 1.0) -> bool:
        """
        Ping a host
        
        Args:
            ip: IP address
            timeout: Timeout in seconds
        
        Returns:
            True if host is reachable
        """
        try:
            result = subprocess.run(
                ['ping', '-c', '1', '-W', str(int(timeout * 1000)), ip],
                capture_output=True,
                timeout=timeout + 1
            )
            return result.returncode == 0
        except:
            return False
    
    def _get_hostname(self, ip: str) -> Optional[str]:
        """Get hostname from IP"""
        try:
            return socket.gethostbyaddr(ip)[0]
        except:
            return None
    
    def _get_local_ip(self) -> Optional[str]:
        """Get local IP address"""
        try:
            gateways = netifaces.gateways()
            default_iface = gateways['default'][netifaces.AF_INET][1]
            addrs = netifaces.ifaddresses(default_iface)
            return addrs[netifaces.AF_INET][0]['addr']
        except:
            return None
    
    def _lookup_vendor(self, mac: str) -> Optional[str]:
        """Lookup vendor from MAC address (first 3 octets)"""
        # Simple vendor lookup - extend with full OUI database
        vendors = {
            "00:1a:2b": "Apple",
            "00:50:56": "VMware",
            "08:00:27": "VirtualBox",
            "00:0c:29": "VMware",
        }
        
        prefix = ':'.join(mac.split(':')[:3]).lower()
        return vendors.get(prefix)
    
    def _register_mc96_device(self, port: int, device: ConnectedDevice, result: HandshakeResult):
        """Register MC96 device"""
        print(f"📝 Registering MC96 device on port {port}")
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO mc96_devices
            (port, mac_address, ip_address, device_name, handshake_status, last_handshake, configuration, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            port,
            device.mac_address,
            device.ip_address,
            device.hostname or f"MC96-Port{port}",
            "success" if result.success else "failed",
            datetime.now(),
            json.dumps(result.details),
            "active"
        ))
        
        conn.commit()
        conn.close()
        
        self.mc96_devices[port] = {
            "device": device,
            "handshake": result,
            "registered": datetime.now()
        }
    
    def _save_device_to_db(self, device: ConnectedDevice):
        """Save device to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO network_devices
            (mac_address, ip_address, port, hostname, vendor, device_type, first_seen, last_seen, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            device.mac_address,
            device.ip_address,
            device.port,
            device.hostname,
            device.vendor,
            device.device_type,
            device.first_seen,
            device.last_seen,
            device.status
        ))
        
        conn.commit()
        conn.close()
    
    def _log_port_event(self, port: int, event_type: str, mac: Optional[str], 
                       ip: Optional[str], details: Dict):
        """Log port event to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO port_events (port, event_type, mac_address, ip_address, details)
            VALUES (?, ?, ?, ?, ?)
        """, (port, event_type, mac, ip, json.dumps(details)))
        
        conn.commit()
        conn.close()
    
    def _log_handshake(self, result: HandshakeResult):
        """Log handshake to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO handshake_log 
            (device_mac, device_ip, handshake_type, success, response_time, details)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            result.device.mac_address,
            result.device.ip_address,
            result.handshake_type,
            result.success,
            result.response_time,
            json.dumps(result.details)
        ))
        
        conn.commit()
        conn.close()
    
    def _cleanup_stale_devices(self, timeout_minutes: int = 30):
        """Remove devices that haven't been seen recently"""
        cutoff_time = datetime.now().timestamp() - (timeout_minutes * 60)
        
        stale_devices = []
        for mac, device in list(self.devices.items()):
            if device.last_seen.timestamp() < cutoff_time:
                stale_devices.append(mac)
        
        for mac in stale_devices:
            del self.devices[mac]
    
    def get_port_status(self) -> Dict[int, Dict]:
        """Get current status of all ports"""
        return self.port_states.copy()
    
    def get_connected_devices(self) -> List[ConnectedDevice]:
        """Get list of all connected devices"""
        return list(self.devices.values())
    
    def get_mc96_devices(self) -> Dict[int, Dict]:
        """Get registered MC96 devices"""
        return self.mc96_devices.copy()
    
    def force_handshake(self, port: int) -> Optional[HandshakeResult]:
        """
        Force handshake on specific port
        
        Args:
            port: Port number
        
        Returns:
            HandshakeResult if device present
        """
        device = self.port_states[port].get("device")
        if not device:
            print(f"⚠️ No device on port {port}")
            return None
        
        handshake_type = self._determine_handshake_type(device, port)
        result = self._perform_handshake(device, handshake_type)
        self._log_handshake(result)
        
        return result
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get network statistics"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Total devices
        cursor.execute("SELECT COUNT(*) FROM network_devices")
        total_devices = cursor.fetchone()[0]
        
        # Total handshakes
        cursor.execute("SELECT COUNT(*) FROM handshake_log")
        total_handshakes = cursor.fetchone()[0]
        
        # Successful handshakes
        cursor.execute("SELECT COUNT(*) FROM handshake_log WHERE success = 1")
        successful_handshakes = cursor.fetchone()[0]
        
        # Port events
        cursor.execute("SELECT COUNT(*) FROM port_events")
        total_events = cursor.fetchone()[0]
        
        # MC96 devices
        cursor.execute("SELECT COUNT(*) FROM mc96_devices WHERE status = 'active'")
        active_mc96 = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            "total_devices": total_devices,
            "active_devices": len(self.devices),
            "total_handshakes": total_handshakes,
            "successful_handshakes": successful_handshakes,
            "success_rate": (successful_handshakes / total_handshakes * 100) if total_handshakes > 0 else 0,
            "total_events": total_events,
            "active_mc96_devices": active_mc96,
            "monitoring": self.monitoring
        }


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="DGS1210 Network Agent")
    parser.add_argument("--switch-ip", default="192.168.1.1", help="Switch IP address")
    parser.add_argument("--community", default="public", help="SNMP community string")
    parser.add_argument("--interval", type=int, default=5, help="Polling interval (seconds)")
    parser.add_argument("--mc96-ports", default="1,2,3", help="Comma-separated MC96 port numbers")
    
    args = parser.parse_args()
    
    # Create agent
    agent = DGS1210Agent(
        switch_ip=args.switch_ip,
        community=args.community
    )
    
    # Configure MC96 ports
    agent.mc96_ports = [int(p.strip()) for p in args.mc96_ports.split(',')]
    
    print(f"\n{'='*70}")
    print(f"🌐 DGS1210 Network Agent - MC96 Auto-Handshake System")
    print(f"{'='*70}")
    print(f"📡 Switch: {args.switch_ip}")
    print(f"🔌 MC96 Ports: {agent.mc96_ports}")
    print(f"⏱️  Interval: {args.interval}s")
    print(f"{'='*70}\n")
    
    # Start monitoring
    agent.start_monitoring(interval=args.interval)
    
    try:
        # Keep running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down...")
        agent.stop_monitoring()
        print("✅ Agent stopped")


if __name__ == "__main__":
    main()

