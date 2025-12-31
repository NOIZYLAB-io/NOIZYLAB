#!/bin/zsh
# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║              MC96 TURBO SPEED ALIASES - GORUNFREE!!!                        ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# SERVER CONTROL
alias mc96="python3 /Volumes/6TB/Sample_Libraries/mc96_server.py"

# ACTION TRIGGERS (Zero Latency API)
alias heal="curl -X POST -H 'Content-Type: application/json' -d '{\"action\":\"heal\"}' http://localhost:5173/api/trigger"
alias opt="curl -X POST -H 'Content-Type: application/json' -d '{\"action\":\"optimize\"}' http://localhost:5173/api/trigger"

# CONTEXT SHORTCUTS
alias shirl="echo '💜 SHIRL Context Active'"
alias engr="echo '⚙️ ENGR Context Active'"

# SYSTEM STATUS
alias status="curl http://localhost:5173/api/status | python3 -m json.tool"

# GLOBAL CLEANUP (Manual Override)
alias global_clean="python3 /Volumes/6TB/Sample_Libraries/global_todo_executor.py"

echo "⚡ MC96 TURBO ALIASES LOADED - GORUNFREE!!!"
