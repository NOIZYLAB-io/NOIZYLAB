import requests
from getpass import getpass

# CONFIGURATION
ROUTER_IP = "192.168.0.1"  # Change to your D-Link router's IP
USERNAME = "admin"          # Change to your router's username
PASSWORD = None             # Will prompt securely

# Endpoints and headers (generic, may need adjustment for your model)
LOGIN_URL = f"http://{ROUTER_IP}/login.cgi"
DEVICE_LIST_URL = f"http://{ROUTER_IP}/status.cgi"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Main logic
def main():
    global PASSWORD
    print("D-Link Router Control Script")
    if PASSWORD is None:
        PASSWORD = getpass("Enter router password: ")

    session = requests.Session()
    # Login (may need to adjust payload for your model)
    login_payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    print("Logging in...")
    resp = session.post(LOGIN_URL, data=login_payload, headers=HEADERS)
    if resp.status_code != 200 or "logout" not in resp.text:
        print("Login failed. Check credentials and router IP.")
        return
    print("Login successful.")

    # Fetch device list (may need to adjust endpoint for your model)
    print("Fetching connected devices...")
    resp = session.get(DEVICE_LIST_URL, headers=HEADERS)
    if resp.status_code == 200:
        print("Device List Response:")
        print(resp.text)
    else:
        print(f"Failed to fetch device list. Status code: {resp.status_code}")

if __name__ == "__main__":
    main()
