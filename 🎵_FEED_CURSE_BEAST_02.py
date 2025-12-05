#!/usr/bin/env python3
"""
🎵🔥 FEED CURSE_BEAST_02 - CODE INGESTION SYSTEM 🔥🎵
====================================================
Give CURSE_BEAST_02 code, knowledge, or anything!
The beast EATS it, LEARNS it, and USES it!
"""

import json
import sqlite3
from pathlib import Path
from datetime import datetime


class BeastFeeder:
    """Feed code and knowledge to CURSE_BEAST_02"""
    
    def __init__(self):
        self.db_path = Path("/Users/m2ultra/NOIZYLAB/curse_beast_02_brain.db")
        self._init_brain()
        
        print("🎵 CURSE_BEAST_02 - READY TO EAT CODE!")
        print("🔥 Feed me anything - I'll learn it INSTANTLY!")
    
    def _init_brain(self):
        """Initialize CURSE_BEAST_02's brain database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Code knowledge base
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS beast_code (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                code_type TEXT,
                language TEXT,
                code_content TEXT,
                description TEXT,
                tags TEXT,
                source TEXT,
                learned BOOLEAN DEFAULT 1
            )
        """)
        
        # Knowledge base
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS beast_knowledge (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                category TEXT,
                subject TEXT,
                knowledge_content TEXT,
                tags TEXT,
                learned BOOLEAN DEFAULT 1
            )
        """)
        
        # Skills acquired
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS beast_skills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                skill_name TEXT UNIQUE,
                skill_level TEXT,
                acquired_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                practice_count INTEGER DEFAULT 0
            )
        """)
        
        conn.commit()
        conn.close()
    
    def feed_code(self, code: str, language: str = "python", 
                 description: str = "", tags: List[str] = None):
        """
        🔥 FEED CODE TO CURSE_BEAST_02!
        
        Args:
            code: The code to feed
            language: Programming language
            description: What this code does
            tags: Tags for categorization
        """
        print(f"\n🔥 EATING CODE...")
        print(f"   Language: {language}")
        print(f"   Size: {len(code)} characters")
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO beast_code (code_type, language, code_content, description, tags)
            VALUES (?, ?, ?, ?, ?)
        """, (
            "direct_feed",
            language,
            code,
            description,
            ','.join(tags) if tags else ""
        ))
        
        conn.commit()
        conn.close()
        
        print(f"✅ CODE EATEN AND LEARNED!")
        print(f"🧠 CURSE_BEAST_02 now knows this code!")
    
    def feed_knowledge(self, category: str, subject: str, 
                      knowledge: str, tags: List[str] = None):
        """
        🧠 FEED KNOWLEDGE TO CURSE_BEAST_02!
        
        Args:
            category: Knowledge category (music, production, tech, etc.)
            subject: Specific subject
            knowledge: The knowledge content
            tags: Tags for organization
        """
        print(f"\n🧠 ABSORBING KNOWLEDGE...")
        print(f"   Category: {category}")
        print(f"   Subject: {subject}")
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO beast_knowledge (category, subject, knowledge_content, tags)
            VALUES (?, ?, ?, ?)
        """, (
            category,
            subject,
            knowledge,
            ','.join(tags) if tags else ""
        ))
        
        conn.commit()
        conn.close()
        
        print(f"✅ KNOWLEDGE ABSORBED!")
        print(f"🌟 CURSE_BEAST_02 is now smarter!")
    
    def feed_from_file(self, file_path: str):
        """
        📁 FEED FROM FILE - Eats entire files!
        
        Args:
            file_path: Path to file
        """
        file = Path(file_path)
        
        if not file.exists():
            print(f"❌ File not found: {file_path}")
            return
        
        print(f"\n📁 EATING FILE: {file.name}")
        
        # Read content
        try:
            with open(file, 'r') as f:
                content = f.read()
            
            # Determine language
            ext = file.suffix.lower()
            lang_map = {
                '.py': 'python',
                '.js': 'javascript',
                '.ts': 'typescript',
                '.sh': 'bash',
                '.md': 'markdown',
                '.yaml': 'yaml',
                '.json': 'json'
            }
            
            language = lang_map.get(ext, 'text')
            
            # Feed it!
            self.feed_code(
                content,
                language,
                f"Loaded from {file.name}",
                [ext[1:], file.parent.name]
            )
            
            print(f"✅ FILE EATEN! {len(content)} characters absorbed!")
            
        except Exception as e:
            print(f"❌ Error eating file: {e}")
    
    def feed_from_directory(self, directory: str, pattern: str = "*.py"):
        """
        📂 FEED FROM DIRECTORY - Eats all matching files!
        
        Args:
            directory: Directory to scan
            pattern: File pattern (*.py, *.js, etc.)
        """
        print(f"\n📂 EATING DIRECTORY: {directory}")
        print(f"   Pattern: {pattern}")
        
        path = Path(directory)
        files = list(path.glob(pattern))
        
        print(f"   Found {len(files)} files to eat!")
        
        for file in files:
            self.feed_from_file(str(file))
        
        print(f"\n✅ DIRECTORY EATEN! {len(files)} files absorbed!")
    
    def learn_skill(self, skill_name: str, skill_level: str = "expert"):
        """
        💪 LEARN NEW SKILL!
        
        Args:
            skill_name: Name of skill
            skill_level: Level (beginner, intermediate, expert, genius)
        """
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO beast_skills (skill_name, skill_level, practice_count)
            VALUES (?, ?, COALESCE((SELECT practice_count + 1 FROM beast_skills WHERE skill_name = ?), 1))
        """, (skill_name, skill_level, skill_name))
        
        conn.commit()
        conn.close()
        
        print(f"💪 SKILL ACQUIRED: {skill_name} ({skill_level})")
    
    def what_i_know(self):
        """Show what CURSE_BEAST_02 has learned"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Code learned
        cursor.execute("SELECT COUNT(*), language FROM beast_code GROUP BY language")
        code_counts = cursor.fetchall()
        
        # Knowledge learned
        cursor.execute("SELECT COUNT(*), category FROM beast_knowledge GROUP BY category")
        knowledge_counts = cursor.fetchall()
        
        # Skills
        cursor.execute("SELECT skill_name, skill_level FROM beast_skills ORDER BY practice_count DESC")
        skills = cursor.fetchall()
        
        conn.close()
        
        print(f"\n🧠 CURSE_BEAST_02 BRAIN CONTENTS:")
        print(f"="*50)
        
        if code_counts:
            print(f"\n📝 Code Learned:")
            for count, lang in code_counts:
                print(f"  {lang}: {count} pieces")
        
        if knowledge_counts:
            print(f"\n🌟 Knowledge Absorbed:")
            for count, cat in knowledge_counts:
                print(f"  {cat}: {count} entries")
        
        if skills:
            print(f"\n💪 Skills Acquired:")
            for skill, level in skills[:10]:
                print(f"  {skill}: {level}")
        
        print(f"\n🎵 CURSE_BEAST_02 is LEARNING and GROWING! 🎵")


def main():
    """Interactive feeder"""
    import argparse
    
    parser = argparse.ArgumentParser(description="🎵 Feed CURSE_BEAST_02")
    parser.add_argument("action", choices=["code", "knowledge", "file", "directory", "show"])
    parser.add_argument("--content", help="Code or knowledge content")
    parser.add_argument("--file", help="File path")
    parser.add_argument("--dir", help="Directory path")
    parser.add_argument("--pattern", default="*.py", help="File pattern")
    parser.add_argument("--language", default="python", help="Language")
    parser.add_argument("--category", help="Knowledge category")
    parser.add_argument("--subject", help="Knowledge subject")
    parser.add_argument("--description", default="", help="Description")
    
    args = parser.parse_args()
    
    feeder = BeastFeeder()
    
    if args.action == "code":
        if args.content:
            feeder.feed_code(args.content, args.language, args.description)
        else:
            print("❌ Please provide --content")
    
    elif args.action == "knowledge":
        if args.content and args.category and args.subject:
            feeder.feed_knowledge(args.category, args.subject, args.content)
        else:
            print("❌ Please provide --content --category --subject")
    
    elif args.action == "file":
        if args.file:
            feeder.feed_from_file(args.file)
        else:
            print("❌ Please provide --file")
    
    elif args.action == "directory":
        if args.dir:
            feeder.feed_from_directory(args.dir, args.pattern)
        else:
            print("❌ Please provide --dir")
    
    elif args.action == "show":
        feeder.what_i_know()


if __name__ == "__main__":
    print("\n🎵🔥 CURSE_BEAST_02 - CODE FEEDER! 🔥🎵")
    print("⚡ Feed me code and I'll learn it INSTANTLY!")
    print()
    
    main()

