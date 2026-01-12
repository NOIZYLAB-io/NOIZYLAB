#!/usr/bin/env python3
"""
███╗   ███╗ ██████╗ █████╗  ██████╗ 
████╗ ████║██╔════╝██╔══██║██╔════╝ 
██╔████╔██║██║     ╚██████║███████╗ 
██║╚██╔╝██║██║      ╚═══██║██╔═══██╗
██║ ╚═╝ ██║╚██████╗ █████╔╝╚██████╔╝
╚═╝     ╚═╝ ╚═════╝ ╚════╝  ╚═════╝ 

MC96 UNIFIED - THE ONE TOOL TO RULE THEM ALL

Commands:
  mc96                    Interactive terminal
  mc96 recall "monday"    Time capsule query
  mc96 new "Project"      Start tracking session
  mc96 add file.py        Add file to session
  mc96 wtf "error"        Diagnostic capture
  mc96 calendar           Show schedule
  mc96 upgrade            System maintenance
  mc96 push               Git commit + push
  mc96 status             Everything status

ONE TOOL. ALL POWER. CIRCLE OF 8.
"""

import os
import sys
import json
import subprocess
import hashlib
import sqlite3
import re
from datetime import datetime, timedelta
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════════════

HOME = Path.home()
MC96_HOME = HOME / ".mc96"
DB_PATH = MC96_HOME / "mc96.db"
NOIZYLAB_PATH = HOME / "NOIZYLAB"
CIRCLE_OF_8 = ["gabriel", "mc96", "omega", "shirl", "keith", "deepseek", "temporal", "memcell"]

# ═══════════════════════════════════════════════════════════════════════════════
# INIT
# ═══════════════════════════════════════════════════════════════════════════════

def init():
    MC96_HOME.mkdir(exist_ok=True)
    (MC96_HOME / "sessions").mkdir(exist_ok=True)
    (MC96_HOME / "captures").mkdir(exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS commits (hash TEXT PRIMARY KEY, date TEXT, msg TEXT, repo TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS sessions (id TEXT PRIMARY KEY, title TEXT, date TEXT, files TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS events (id TEXT PRIMARY KEY, title TEXT, date TEXT, time TEXT, type TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS captures (id TEXT PRIMARY KEY, date TEXT, error TEXT, context TEXT)')
    conn.commit()
    conn.close()

def parse_date(query):
    q = query.lower()
    today = datetime.now()
    if "today" in q: return today.strftime("%Y-%m-%d")
    if "yesterday" in q: return (today - timedelta(days=1)).strftime("%Y-%m-%d")
    if "monday" in q: return (today - timedelta(days=today.weekday())).strftime("%Y-%m-%d")
    match = re.search(r'(\d{4}-\d{2}-\d{2})', q)
    return match.group(1) if match else today.strftime("%Y-%m-%d")

# ═══════════════════════════════════════════════════════════════════════════════
# COMMANDS
# ═══════════════════════════════════════════════════════════════════════════════

def recall(query):
    date = parse_date(query)
    next_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
    out = [f"🧠 RECALL: {date}", "═" * 50]
    
    for repo in [NOIZYLAB_PATH, HOME / "GABRIEL"]:
        if repo.exists():
            try:
                r = subprocess.run(["git", "log", f"--since={date}", f"--until={next_date}", 
                                   "--pretty=format:%h %s"], cwd=repo, capture_output=True, text=True)
                if r.stdout.strip():
                    out.append(f"\n📝 GIT ({repo.name}):")
                    for line in r.stdout.strip().split('\n')[:10]:
                        out.append(f"   {line}")
            except: pass
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT title, files FROM sessions WHERE date = ?", (date,))
    for row in c.fetchall():
        out.append(f"\n📁 SESSION: {row[0]}")
    conn.close()
    return '\n'.join(out)

def new_session(title):
    date = datetime.now().strftime("%Y-%m-%d")
    slug = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')[:30]
    session_id = f"{date}_{slug}"
    session_dir = MC96_HOME / "sessions" / session_id
    session_dir.mkdir(parents=True, exist_ok=True)
    (session_dir / "code").mkdir(exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO sessions VALUES (?, ?, ?, ?)", (session_id, title, date, "[]"))
    conn.commit()
    conn.close()
    
    (MC96_HOME / ".current").write_text(session_id)
    return f"✅ Session: {session_id}\n📁 {session_dir}"

def add_file(file_path):
    current = MC96_HOME / ".current"
    if not current.exists(): return "❌ No session. Run: mc96 new 'Title'"
    
    session_id = current.read_text().strip()
    src = Path(file_path).expanduser().absolute()
    if not src.exists(): return f"❌ Not found: {src}"
    
    import shutil
    dest = MC96_HOME / "sessions" / session_id / "code" / src.name
    shutil.copy2(src, dest)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT files FROM sessions WHERE id = ?", (session_id,))
    row = c.fetchone()
    files = json.loads(row[0]) if row and row[0] else []
    files.append(str(src))
    c.execute("UPDATE sessions SET files = ? WHERE id = ?", (json.dumps(files), session_id))
    conn.commit()
    conn.close()
    return f"✅ Added: {src.name}"

def wtf(error):
    cap_id = hashlib.md5(f"{error}{datetime.now()}".encode()).hexdigest()[:12]
    date = datetime.now().strftime("%Y-%m-%d")
    ctx = {"error": error, "ts": datetime.now().isoformat(), "cwd": os.getcwd()}
    
    path = MC96_HOME / "captures" / f"{date}_{cap_id}.json"
    with open(path, 'w') as f: json.dump(ctx, f, indent=2, default=str)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO captures VALUES (?, ?, ?, ?)", (cap_id, date, error, str(path)))
    conn.commit()
    conn.close()
    return f"🔧 CAPTURED: {cap_id}\n📄 {path}"

def calendar(days=7):
    out = ["🗓️  MC96 CALENDAR", "═" * 50]
    today = datetime.now()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    for i in range(days):
        date = (today + timedelta(days=i)).strftime("%Y-%m-%d")
        day = (today + timedelta(days=i)).strftime("%a")
        c.execute("SELECT title FROM sessions WHERE date = ?", (date,))
        sessions = c.fetchall()
        c.execute("SELECT title, time FROM events WHERE date = ?", (date,))
        events = c.fetchall()
        
        if sessions or events or i == 0:
            m = "▶" if i == 0 else " "
            out.append(f"\n{m} {date} ({day})")
            for s in sessions: out.append(f"   📝 {s[0]}")
            for e in events: out.append(f"   📌 {e[1]} {e[0]}")
            if not sessions and not events: out.append("   (clear)")
    conn.close()
    return '\n'.join(out)

def schedule(title, when):
    date = parse_date(when)
    time_match = re.search(r'(\d{1,2})(am|pm)?', when.lower())
    time = "09:00"
    if time_match:
        h = int(time_match.group(1))
        if time_match.group(2) == 'pm' and h < 12: h += 12
        time = f"{h:02d}:00"
    
    eid = hashlib.md5(f"{title}{date}{time}".encode()).hexdigest()[:8]
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO events VALUES (?, ?, ?, ?, ?)", (eid, title, date, time, "task"))
    conn.commit()
    conn.close()
    return f"✅ Scheduled: {title}\n📅 {date} {time}"

def push(msg=None):
    if not msg: msg = f"mc96 auto {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    out = []
    try:
        subprocess.run(["git", "add", "-A"], capture_output=True)
        out.append("📦 Staged")
        r = subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)
        out.append(f"✅ Committed" if "nothing to commit" not in r.stdout+r.stderr else "ℹ️ Nothing to commit")
        r = subprocess.run(["git", "push"], capture_output=True, text=True)
        out.append("🚀 Pushed" if r.returncode == 0 else f"⚠️ {r.stderr[:50]}")
    except Exception as e:
        out.append(f"❌ {e}")
    return '\n'.join(out)

def status():
    out = ["", "█▀▄▀█ █▀▀ █▀▀ █▀▀", "█ ▀ █ █   ▀▀█ █▀▀", "▀   ▀ ▀▀▀ ▀▀▀ ▀▀▀", "═" * 40]
    
    cur = MC96_HOME / ".current"
    out.append(f"📝 Session: {cur.read_text().strip() if cur.exists() else 'None'}")
    
    try:
        r = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
        n = len(r.stdout.strip().split('\n')) if r.stdout.strip() else 0
        out.append(f"📦 Git: {n} changes")
    except: pass
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM sessions"); s = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM captures"); cap = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM events"); e = c.fetchone()[0]
    conn.close()
    
    out.append(f"📚 {s} sessions | {cap} captures | {e} events")
    out.append(f"\n🔮 {' → '.join(CIRCLE_OF_8)}")
    out.append("\n═" * 40)
    out.append("recall new add wtf calendar schedule push upgrade")
    return '\n'.join(out)

def upgrade():
    out = ["🔧 UPGRADING...", "═" * 40]
    for cmd, name in [("brew update && brew upgrade", "Brew"), ("pip3 install -U pip", "Pip")]:
        try:
            r = subprocess.run(cmd, shell=True, capture_output=True, timeout=300)
            out.append(f"{'✅' if r.returncode == 0 else '⚠️'} {name}")
        except Exception as e:
            out.append(f"❌ {name}: {e}")
    return '\n'.join(out)

# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    init()
    if len(sys.argv) < 2: print(status()); return
    
    cmd, args = sys.argv[1].lower(), sys.argv[2:]
    
    cmds = {
        "recall": lambda: recall(' '.join(args) or "today"),
        "new": lambda: new_session(' '.join(args) or "Untitled"),
        "add": lambda: add_file(args[0]) if args else "❌ mc96 add <file>",
        "wtf": lambda: wtf(' '.join(args) or "error"),
        "calendar": lambda: calendar(int(args[0]) if args else 7),
        "cal": lambda: calendar(int(args[0]) if args else 7),
        "schedule": lambda: schedule(args[0], ' '.join(args[1:])) if len(args) >= 2 else "❌ mc96 schedule 'Task' 'when'",
        "sched": lambda: schedule(args[0], ' '.join(args[1:])) if len(args) >= 2 else "❌ mc96 schedule 'Task' 'when'",
        "push": lambda: push(' '.join(args) if args else None),
        "upgrade": upgrade,
        "status": status,
        "s": status,
    }
    
    print(cmds.get(cmd, lambda: f"❌ Unknown: {cmd}\n{status()}")())

if __name__ == "__main__":
    main()
