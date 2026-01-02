#!/usr/bin/env python3
# ===========================================================
#  NOIZYLAB | Master Dashboard (read-only local monitor)
# ===========================================================

import psutil, time, threading, paramiko
from flask import Flask, render_template_string

# ---------- CONFIG ----------
REFRESH = 10
HOSTS = [
    {"name":"MacStudio","ip":"127.0.0.1","user":None,"pwd":None},
    {"name":"HP OMEN","ip":"192.168.0.121","user":"omenuser","pwd":"password"},
    {"name":"Mac Pro","ip":"192.168.0.130","user":"macuser","pwd":"password"},
    {"name":"Inspiron","ip":"192.168.0.140","user":"inspironuser","pwd":"password"}
]

data = {h["name"]: {} for h in HOSTS}

# ---------- FUNCTIONS ----------
def local_metrics():
    return {
        "CPU": psutil.cpu_percent(),
        "RAM": psutil.virtual_memory().percent,
        "Disk": psutil.disk_usage("/").percent
    }

def remote_metrics(h):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(h["ip"], username=h["user"], password=h["pwd"], timeout=5)
        cmds = {
            "CPU": "wmic cpu get loadpercentage | findstr [0-9]",
            "RAM": "powershell -command \"(Get-Counter '\\\\Memory\\\\Available MBytes').CounterSamples.CookedValue\"",
            "Disk": "powershell -command \"(Get-PSDrive C).Used / (Get-PSDrive C).Free * 100\""
        }
        result = {}
        for k, c in cmds.items():
            _, o, _ = ssh.exec_command(c)
            out = o.read().decode().strip().splitlines()
            if out:
                result[k] = out[-1]
        ssh.close()
        return result
    except Exception as e:
        return {"Error": str(e)}

def refresh():
    while True:
        for h in HOSTS:
            data[h["name"]] = local_metrics() if h["ip"] == "127.0.0.1" else remote_metrics(h)
        time.sleep(REFRESH)

threading.Thread(target=refresh, daemon=True).start()

# ---------- WEB ----------
HTML = """
<!DOCTYPE html><html><head>
<meta charset="utf-8"><title>NoizyLab Master Dashboard</title>
<style>
body{background:#000;color:#eee;font-family:'Segoe UI',sans-serif;}
h1{background:#d4af37;color:#000;padding:10px 20px;}
.grid{display:flex;flex-wrap:wrap;justify-content:center;}
.card{background:#111;border-radius:14px;margin:15px;padding:20px;width:270px;
box-shadow:0 0 10px #333;}
h2{color:#d4af37;margin-top:0;}
.value{font-size:1.6em;}
.error{color:#f44;}
</style>
<meta http-equiv="refresh" content="10">
</head><body>
<h1>NOIZYLAB MASTER DASHBOARD</h1>
<div class="grid">
{% for name,vals in data.items() %}
  <div class="card"><h2>{{name}}</h2>
  {% if vals.Error %}
     <div class="error">{{vals.Error}}</div>
  {% else %}
     {% for k,v in vals.items() %}
       <div>{{k}}: <span class="value">{{v}}</span></div>
     {% endfor %}
  {% endif %}
  </div>
{% endfor %}
</div></body></html>
"""

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string(HTML, data=data)

if __name__ == "__main__":
    print("🌍 Dashboard running → http://localhost:8500")
    app.run(host="0.0.0.0", port=8500, debug=False)
