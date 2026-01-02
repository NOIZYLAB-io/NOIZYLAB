"""
setup_dlink_dashboard.py
Sets up a Flask-based D-Link Dashboard web app.
"""
import os
import sys
import subprocess

REQUIRED_PACKAGES = ["flask"]

def install_packages():
    for pkg in REQUIRED_PACKAGES:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

def create_dashboard_app():
    app_code = '''
from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>D-Link Dashboard</h1><p>Welcome! Device controls coming soon.</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
'''
    os.makedirs("dlink_dashboard", exist_ok=True)
    with open("dlink_dashboard/app.py", "w") as f:
        f.write(app_code)
    print("Dashboard scaffolded in dlink_dashboard/app.py")

def main():
    print("Installing required packages...")
    install_packages()
    print("Creating dashboard app...")
    create_dashboard_app()
    print("Setup complete. To run the dashboard: cd dlink_dashboard && python3 app.py")

if __name__ == "__main__":
    main()
