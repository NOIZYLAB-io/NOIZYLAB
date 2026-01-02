import sqlite3, json, os, time

def migrate_chat_history():
    """Convert chat_history.jsonl to SQLite database"""
    conn = sqlite3.connect("noizy_logs.db")
    c = conn.cursor()
    
    # Create chat table
    c.execute("""CREATE TABLE IF NOT EXISTS chat(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT, 
        model TEXT, 
        text TEXT, 
        ts REAL
    )""")
    
    # Check if JSONL file exists
    jsonl_file = "chat_history.jsonl"
    if not os.path.exists(jsonl_file):
        print(f"📝 No {jsonl_file} found, creating empty database")
        conn.commit()
        conn.close()
        return
    
    # Migrate existing records
    migrated = 0
    try:
        with open(jsonl_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    rec = json.loads(line.strip())
                    if not rec:  # Skip empty lines
                        continue
                        
                    role = rec.get("role", "unknown")
                    model = rec.get("model", "unknown")
                    text = rec.get("text", "")
                    timestamp = rec.get("timestamp", time.time())
                    
                    c.execute("INSERT INTO chat (role, model, text, ts) VALUES (?,?,?,?)",
                              (role, model, text, timestamp))
                    migrated += 1
                    
                except json.JSONDecodeError as e:
                    print(f"⚠️  Skipping malformed JSON at line {line_num}: {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"📝 {jsonl_file} not found")
    
    conn.commit()
    conn.close()
    
    print(f"✅ Migrated {migrated} chat records to SQLite database")
    
    # Optionally backup the JSONL file
    if migrated > 0 and os.path.exists(jsonl_file):
        backup_name = f"{jsonl_file}.backup"
        os.rename(jsonl_file, backup_name)
        print(f"📦 Backed up original file to {backup_name}")

def query_chat_history(limit=10, model=None):
    """Query recent chat history"""
    conn = sqlite3.connect("noizy_logs.db")
    c = conn.cursor()
    
    if model:
        c.execute("SELECT role, model, text, ts FROM chat WHERE model=? ORDER BY ts DESC LIMIT ?", (model, limit))
    else:
        c.execute("SELECT role, model, text, ts FROM chat ORDER BY ts DESC LIMIT ?", (limit,))
    
    results = c.fetchall()
    conn.close()
    
    return results

if __name__ == "__main__":
    print("🔄 Starting chat history migration...")
    migrate_chat_history()
    
    # Show recent entries
    recent = query_chat_history(5)
    if recent:
        print("\n📚 Recent chat entries:")
        for role, model, text, ts in recent:
            print(f"  {role} ({model}): {text[:50]}...")
    else:
        print("📭 No chat history found")