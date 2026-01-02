import requests

def broadcast_ritual(ritual):
    targets = ["192.168.2.10", "192.168.2.20", "192.168.2.30"]
    for ip in targets:
        try:
            requests.get(f"http://{ip}:5050/trigger?ritual={ritual}")
        except Exception as e:
            print(f"Failed to reach {ip}: {e}")
