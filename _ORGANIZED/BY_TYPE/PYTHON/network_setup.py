#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Network Setup Module for IT Genius
Handles network configuration and troubleshooting
"""

import subprocess
import platform
from typing import Dict

class NetworkSetup:
    """Network configuration wizard"""
    
    def __init__(self, config: Dict):
        self.config = config
        if "network_profiles" not in self.config:
            self.config["network_profiles"] = {}
        self.os_type = platform.system()
    
    def display_menu(self):
        """Display network setup menu"""
        print("\n" + "="*70)
        print("NETWORK CONFIGURATION")
        print("="*70)
        print("1. View Network Information")
        print("2. Test Internet Connection")
        print("3. Configure WiFi Network")
        print("4. Configure Static IP (Advanced)")
        print("5. DNS Configuration")
        print("6. Port Forwarding Guide")
        print("7. Network Troubleshooting")
        print("8. View Saved Network Profiles")
        print("0. Back to Main Menu")
        print("="*70)
    
    def view_network_info(self):
        """Display current network information"""
        print("\n" + "="*70)
        print("NETWORK INFORMATION")
        print("="*70)
        
        try:
            if self.os_type == "Darwin":  # macOS
                print("\n📡 Network Interfaces:")
                subprocess.run(["ifconfig"], check=False)
                
                print("\n🌐 Default Gateway:")
                result = subprocess.run(["route", "-n", "get", "default"], 
                                      capture_output=True, text=True, check=False)
                print(result.stdout)
                
                print("\n🔍 DNS Servers:")
                result = subprocess.run(["scutil", "--dns"], 
                                      capture_output=True, text=True, check=False)
                print(result.stdout)
                
            elif self.os_type == "Linux":
                print("\n📡 Network Interfaces:")
                subprocess.run(["ip", "addr"], check=False)
                
                print("\n🌐 Routing Table:")
                subprocess.run(["ip", "route"], check=False)
                
            elif self.os_type == "Windows":
                print("\n📡 Network Configuration:")
                subprocess.run(["ipconfig", "/all"], check=False)
        except Exception as e:
            print(f"❌ Error getting network info: {e}")
        
        print("\n" + "="*70)
    
    def test_connection(self):
        """Test internet connectivity"""
        print("\n" + "="*70)
        print("INTERNET CONNECTION TEST")
        print("="*70)
        
        test_hosts = [
            ("Google DNS", "8.8.8.8"),
            ("Cloudflare DNS", "1.1.1.1"),
            ("Google", "google.com"),
            ("Cloudflare", "cloudflare.com")
        ]
        
        print("\nTesting connectivity...\n")
        for name, host in test_hosts:
            try:
                if self.os_type == "Windows":
                    result = subprocess.run(["ping", "-n", "2", host], 
                                          capture_output=True, text=True, check=False)
                else:
                    result = subprocess.run(["ping", "-c", "2", host], 
                                          capture_output=True, text=True, check=False)
                
                if result.returncode == 0:
                    print(f"✅ {name} ({host}): Connected")
                else:
                    print(f"❌ {name} ({host}): Failed")
            except Exception as e:
                print(f"❌ {name} ({host}): Error - {e}")
        
        print("\n" + "="*70)
    
    def configure_wifi(self):
        """WiFi configuration guide"""
        print("\n" + "="*70)
        print("WIFI CONFIGURATION GUIDE")
        print("="*70)
        
        print("\n📶 Connecting to WiFi Network:")
        print("\n1. Open Network Settings:")
        if self.os_type == "Darwin":
            print("   → System Settings → Network → WiFi")
        elif self.os_type == "Linux":
            print("   → Settings → Network → WiFi")
        elif self.os_type == "Windows":
            print("   → Settings → Network & Internet → WiFi")
        
        print("\n2. Select your network from the list")
        print("3. Enter the network password (if required)")
        print("4. Click Connect")
        
        print("\n🔐 Security Tips:")
        print("   • Use WPA3 or WPA2 encryption")
        print("   • Avoid public WiFi for sensitive activities")
        print("   • Use a VPN on public networks")
        print("   • Keep your router firmware updated")
        
        print("\n" + "="*70)
    
    def configure_dns(self):
        """DNS configuration guide"""
        print("\n" + "="*70)
        print("DNS CONFIGURATION")
        print("="*70)
        
        print("\n🌐 Recommended DNS Servers:")
        print("\n1. Google DNS:")
        print("   Primary:   8.8.8.8")
        print("   Secondary: 8.8.4.4")
        
        print("\n2. Cloudflare DNS:")
        print("   Primary:   1.1.1.1")
        print("   Secondary: 1.0.0.1")
        
        print("\n3. OpenDNS:")
        print("   Primary:   208.67.222.222")
        print("   Secondary: 208.67.220.220")
        
        print("\n📝 How to Change DNS:")
        if self.os_type == "Darwin":
            print("   → System Settings → Network")
            print("   → Select connection → Details → DNS")
            print("   → Click + to add DNS servers")
        elif self.os_type == "Linux":
            print("   → Edit /etc/resolv.conf or use NetworkManager")
        elif self.os_type == "Windows":
            print("   → Settings → Network & Internet")
            print("   → Change adapter options → Properties")
            print("   → Internet Protocol Version 4 → Use custom DNS")
        
        print("\n" + "="*70)
    
    def network_troubleshooting(self):
        """Network troubleshooting guide"""
        print("\n" + "="*70)
        print("NETWORK TROUBLESHOOTING")
        print("="*70)
        
        print("\n🔧 Common Issues and Solutions:")
        
        print("\n1. No Internet Connection:")
        print("   • Check physical cable connections")
        print("   • Restart your router/modem")
        print("   • Restart your computer")
        print("   • Check if other devices can connect")
        
        print("\n2. Slow Connection:")
        print("   • Check for background downloads")
        print("   • Move closer to WiFi router")
        print("   • Check for interference")
        print("   • Update router firmware")
        print("   • Change WiFi channel")
        
        print("\n3. Can't Connect to Specific Website:")
        print("   • Clear browser cache")
        print("   • Try different DNS servers")
        print("   • Check firewall settings")
        print("   • Try incognito/private mode")
        
        print("\n4. IP Address Issues:")
        print("   • Release and renew IP (ipconfig /release /renew on Windows)")
        print("   • Check DHCP settings on router")
        print("   • Try static IP configuration")
        
        print("\n5. WiFi Keeps Disconnecting:")
        print("   • Update network drivers")
        print("   • Change WiFi channel")
        print("   • Check power management settings")
        print("   • Update router firmware")
        
        print("\n" + "="*70)
    
    def run(self):
        """Run network setup wizard"""
        while True:
            self.display_menu()
            choice = input("\nSelect an option: ").strip()
            
            if choice == "1":
                self.view_network_info()
            elif choice == "2":
                self.test_connection()
            elif choice == "3":
                self.configure_wifi()
            elif choice == "4":
                print("\n⚠️  Static IP configuration requires administrative access.")
                print("Please consult your network administrator or router documentation.")
            elif choice == "5":
                self.configure_dns()
            elif choice == "6":
                print("\n📖 Port forwarding configuration varies by router.")
                print("Access your router admin panel (usually 192.168.1.1 or 192.168.0.1)")
                print("Look for 'Port Forwarding' or 'Virtual Server' settings.")
            elif choice == "7":
                self.network_troubleshooting()
            elif choice == "8":
                if self.config["network_profiles"]:
                    print("\nSaved Network Profiles:")
                    for name, profile in self.config["network_profiles"].items():
                        print(f"  • {name}")
                else:
                    print("\nNo saved network profiles.")
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")
            
            if choice != "0":
                input("\nPress Enter to continue...")

