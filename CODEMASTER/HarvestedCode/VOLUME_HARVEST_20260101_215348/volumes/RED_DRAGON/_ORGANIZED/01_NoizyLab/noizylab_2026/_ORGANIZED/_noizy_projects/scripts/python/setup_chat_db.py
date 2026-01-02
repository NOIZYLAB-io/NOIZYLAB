import sqlite3, json, os

def migrate_chat_history():
    """Migrate JSONL chat history to SQLite database"""
    conn = sqlite3.connect("noizy_logs.db")
    c = conn.cursor()
    
    # Create table if it doesn't exist
    c.execute("""CREATE TABLE IF NOT EXISTS chat(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT, 
        model TEXT, 
        text TEXT, 
        ts REAL
    )""")
    
    # Check if JSONL file exists
    if not os.path.exists("chat_history.jsonl"):
        print("No chat_history.jsonl found, creating empty database")
        conn.commit()
        return
    
    # Migrate each line from JSONL
    migrated = 0
    with open("chat_history.jsonl", "r") as f:
        for line in f:
            if line.strip():
                try:
                    rec = json.loads(line)
                    c.execute("INSERT INTO chat (role, model, text, ts) VALUES (?,?,?,strftime('%s','now'))",
                              (rec.get("role", "unknown"), 
                               rec.get("model", "unknown"), 
                               rec.get("text", "")))
                    migrated += 1
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON line: {line[:50]}...")
    
    conn.commit()
    conn.close()
    print(f"✅ Migrated {migrated} chat records to noizy_logs.db")

if __name__ == "__main__":
    migrate_chat_history()