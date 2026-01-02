import requests
import sys

def main():
    url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000/handshake"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        print(f"Fleet Handshake: {data['status']} ({data['message']}) [machine: {data.get('machine', 'unknown')}]")
    except Exception as e:
        print(f"Fleet Handshake failed: {e}")

if __name__ == "__main__":
    main()
