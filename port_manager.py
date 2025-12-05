import os
import socket
import subprocess
import time
from typing import Optional


class PortManager:
    """Static class for managing ports and freeing them up when needed."""

    @staticmethod
    def is_port_open(
        host: str = "localhost", port: int = 11434, timeout: int = 3
    ) -> bool:
        """Check if a port is open (service is running)."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout)
                result = sock.connect_ex((host, port))
                return result == 0
        except Exception:
            return False

    @staticmethod
    def find_process_using_port(port: int) -> Optional[int]:
        """Find the process ID using a specific port."""
        try:
            # Use netstat or lsof to find process using the port
            if os.name == "nt":  # Windows
                result = subprocess.run(
                    ["netstat", "-ano"], capture_output=True, text=True
                )
                for line in result.stdout.split("\n"):
                    if f":{port}" in line and "LISTENING" in line:
                        parts = line.strip().split()
                        if len(parts) >= 5:
                            return int(parts[4])  # PID is in the last column
            else:  # Unix-like systems
                result = subprocess.run(
                    ["lsof", "-ti", f":{port}"], capture_output=True, text=True
                )
                if result.stdout.strip():
                    return int(result.stdout.strip())
        except Exception:
            pass
        return None

    @staticmethod
    def kill_process(pid: int) -> bool:
        """Kill a process by its PID."""
        try:
            if os.name == "nt":  # Windows
                subprocess.run(["taskkill", "/F", "/PID", str(pid)], check=True)
            else:  # Unix-like systems
                subprocess.run(["kill", "-9", str(pid)], check=True)
            return True
        except subprocess.CalledProcessError:
            return False
        except Exception:
            return False

    @staticmethod
    def free_port(port: int, max_attempts: int = 3) -> bool:
        """Free up a port by killing any process using it."""
        for attempt in range(max_attempts):
            pid = PortManager.find_process_using_port(port)
            if pid is None:
                return True  # Port is already free

            print(
                f"Attempting to free port {port} (PID: {pid}) - attempt {attempt + 1}/{max_attempts}"
            )
            if PortManager.kill_process(pid):
                # Wait a bit for the process to actually die
                time.sleep(1)
                if PortManager.find_process_using_port(port) is None:
                    print(f"Successfully freed port {port}")
                    return True
            else:
                print(f"Failed to kill process {pid} using port {port}")

        print(f"Failed to free port {port} after {max_attempts} attempts")
        return False

    @staticmethod
    def wait_for_port(
        host: str = "localhost",
        port: int = 11434,
        timeout: int = 30,
        interval: float = 1.0,
    ) -> bool:
        """Wait for a port to become available."""
        start_time = time.time()
        while time.time() - start_time < timeout:
            if PortManager.is_port_open(host, port):
                return True
            time.sleep(interval)

        print(f"Port {port} did not become available within {timeout} seconds")
        return False

    @staticmethod
    def ensure_port_free(port: int, max_attempts: int = 3) -> bool:
        """Ensure a port is free, freeing it if necessary."""
        if not PortManager.is_port_open(port=port):
            return True  # Already free

        return PortManager.free_port(port, max_attempts)
