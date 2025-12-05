import threading
import time
import requests
import socket
from typing import Callable, Optional
from ipc import IPC


ipc_ = IPC.connect()


class NetworkChecker:
    def __init__(self, check_interval: int = 10, timeout: int = 5):
        """
        Initialize network checker.
        
        Args:
            check_interval: Seconds between connectivity checks
            timeout: Timeout for network requests in seconds
        """
        self.check_interval = check_interval
        self.timeout = timeout
        self.is_connected = False
        self.is_running = False
        self.check_thread = None
        self.callback: Optional[Callable[[bool], None]] = None
        
    def set_callback(self, callback: Callable[[bool], None]):
        """Set callback function to be called when connectivity status changes."""
        self.callback = callback
        
    def check_internet_connection(self) -> bool:
        """
        Check internet connectivity using multiple methods.
        
        Returns:
            bool: True if connected to internet, False otherwise
        """
        # Method 1: Try DNS resolution
        try:
            socket.setdefaulttimeout(self.timeout)
            socket.gethostbyname("google.com")
            return True
        except socket.error:
            pass
            
        # Method 2: Try HTTP request to reliable endpoints
        test_urls = [
            "https://www.google.com",
            "https://www.cloudflare.com"
        ]
        
        for url in test_urls:
            try:
                response = requests.get(url, timeout=self.timeout)
                if response.status_code == 200:
                    return True
            except (requests.RequestException, requests.ConnectionError, requests.Timeout):
                continue
                
        return False
        
    def _monitor_loop(self):
        """Main monitoring loop that runs in a separate thread."""
        while self.is_running:
            current_status = self.check_internet_connection()
            
            # If status changed, update and call callback
            if current_status != self.is_connected:
                self.is_connected = current_status
                if self.callback:
                    self.callback(self.is_connected)
                    
            time.sleep(self.check_interval)
            
    def start_monitoring(self):
        """Start continuous network monitoring."""
        if self.is_running:
            return
            
        self.is_running = True
        self.check_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.check_thread.start()
        
    def stop_monitoring(self):
        """Stop network monitoring."""
        self.is_running = False
        if self.check_thread and self.check_thread.is_alive():
            self.check_thread.join(timeout=1)
            
    def get_status(self) -> bool:
        """Get current connectivity status."""
        return self.is_connected


# Global instance for easy access
network_checker = NetworkChecker()


def start_network_monitoring(callback: Optional[Callable[[bool], None]] = None, check_interval: int = 10):
    """
    Start network monitoring with optional callback.
    
    Args:
        callback: Function to call when connectivity status changes
        check_interval: Seconds between checks
    """
    if callback:
        network_checker.set_callback(callback)
    network_checker.check_interval = check_interval
    network_checker.start_monitoring()


def stop_network_monitoring():
    """Stop network monitoring."""
    network_checker.stop_monitoring()


def is_connected() -> bool:
    """Check current connectivity status."""
    return network_checker.get_status()


def check_connection_once() -> bool:
    """Perform a single connectivity check."""
    return network_checker.check_internet_connection()


if __name__ == "__main__":
    def connection_callback(connected: bool):
        status = "CONNECTED" if connected else "DISCONNECTED"
        print(f"Network status changed: {status}")
        if status == "CONNECTED":
            ipc_.set("internet_connected", True)
        else:
            ipc_.set("internet_connected", False)
        
    print("Starting network monitoring...")
    start_network_monitoring(connection_callback, check_interval=5)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping network monitoring...")
        stop_network_monitoring()
