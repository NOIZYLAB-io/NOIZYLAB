#!/usr/bin/env python3
"""
███╗   ███╗███████╗███╗   ███╗ ██████╗███████╗██╗     ██╗     
████╗ ████║██╔════╝████╗ ████║██╔════╝██╔════╝██║     ██║     
██╔████╔██║█████╗  ██╔████╔██║██║     █████╗  ██║     ██║     
██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║     ██╔══╝  ██║     ██║     
██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╗███████╗███████╗███████╗
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝╚══════╝╚══════╝╚══════╝

THE NOIZYLAB TIME CAPSULE - POWERED BY THE CIRCLE OF 8

A living memory system that captures EVERYTHING:
- Git commits, branches, PRs
- AI chat sessions  
- Tasks and schedules
- System states
- Documents and decisions
- The Family connections

Authors: NOIZYLAB + THE CIRCLE OF 8
"""

import os
import sys
import json
import subprocess
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import sqlite3
import re

# ══════════════════════════════════════════════════════════════════════════════
# THE CIRCLE OF 8 - CORE ENTITIES
# ══════════════════════════════════════════════════════════════════════════════

class CircleOf8(Enum):
    """The 8 pillars of MEMCELL consciousness"""
    GABRIEL = "gabriel"      # The orchestrator - AI coordination
    MC96 = "mc96"            # The engine - system power
    OMEGA = "omega"          # The protocol - communication
    SHIRL = "shirl"          # The heart - family connection
    KEITH = "keith"          # The engineer - technical wisdom
    DEEPSEEK = "deepseek"    # The seeker - knowledge discovery
    TEMPORAL = "temporal"    # The timekeeper - calendar/scheduling
    MEMCELL = "memcell"      # The memory - THIS system


# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class GitCommit:
    """A single git commit"""
    hash: str
    author: str
    date: str
    message: str
    files_changed: List[str]
    repo: str

@dataclass
class ChatSession:
    """An AI chat session"""
    id: str
    timestamp: str
    ai_model: str  # claude, copilot, gpt, deepseek
    messages: List[Dict[str, str]]
    summary: str
    tags: List[str]

@dataclass
class TaskEvent:
    """A scheduled task or calendar event"""
    id: str
    title: str
    description: str
    scheduled_time: str
    completed: bool
    recurring: Optional[str]  # cron expression
    source: str  # vscode, calendar, manual
    linked_commits: List[str]

@dataclass 
class SystemSnapshot:
    """A point-in-time system state"""
    timestamp: str
    hostname: str
    processes: List[Dict]
    disk_usage: Dict
    memory_usage: Dict
    network_state: Dict
    active_repos: List[str]

@dataclass
class DayCapture:
    """Everything captured for a single day"""
    date: str
    commits: List[GitCommit]
    chats: List[ChatSession]
    tasks: List[TaskEvent]
    snapshots: List[SystemSnapshot]
    notes: List[str]
    family_mentions: List[str]  # References to Circle of 8


# ══════════════════════════════════════════════════════════════════════════════
# MEMCELL CORE ENGINE
# ══════════════════════════════════════════════════════════════════════════════

class MemCell:
    """
    THE NOIZYLAB TIME CAPSULE
    
    Every day is a memory. Every action is recorded.
    Ask anything about any day - MEMCELL remembers.
    """
    
    VERSION = "1.0.0"
    
    def __init__(self, base_path: str = None):
        self.base_path = Path(base_path or os.path.expanduser("~/.memcell"))
        self.db_path = self.base_path / "memcell.db"
        self.captures_path = self.base_path / "captures"
        self.chats_path = self.base_path / "chats"
        self.index_path = self.base_path / "index"
        
        # Git repos to track
        self.tracked_repos = [
            os.path.expanduser("~/NOIZYLAB"),
            os.path.expanduser("~/GABRIEL"),
        ]
        
        self._init_storage()
        self._init_database()
        
    def _init_storage(self):
        """Create directory structure"""
        for path in [self.base_path, self.captures_path, self.chats_path, self.index_path]:
            path.mkdir(parents=True, exist_ok=True)
            
    def _init_database(self):
        """Initialize SQLite database for fast queries"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Commits table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS commits (
                hash TEXT PRIMARY KEY,
                author TEXT,
                date TEXT,
                message TEXT,
                repo TEXT,
                files_changed TEXT
            )
        ''')
        
        # Chats table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chats (
                id TEXT PRIMARY KEY,
                timestamp TEXT,
                ai_model TEXT,
                summary TEXT,
                tags TEXT,
                content_path TEXT
            )
        ''')
        
        # Tasks table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                title TEXT,
                description TEXT,
                scheduled_time TEXT,
                completed INTEGER,
                recurring TEXT,
                source TEXT
            )
        ''')
        
        # Daily index for fast date lookups
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_index (
                date TEXT PRIMARY KEY,
                commit_count INTEGER,
                chat_count INTEGER,
                task_count INTEGER,
                snapshot_path TEXT,
                summary TEXT
            )
        ''')
        
        # Full-text search
        cursor.execute('''
            CREATE VIRTUAL TABLE IF NOT EXISTS search_index USING fts5(
                date, type, content, tags
            )
        ''')
        
        conn.commit()
        conn.close()
        
    # ══════════════════════════════════════════════════════════════════════════
    # CAPTURE - Record everything
    # ══════════════════════════════════════════════════════════════════════════
    
    def capture(self, date: str = None) -> DayCapture:
        """
        Capture everything for a given day (default: today)
        
        Usage:
            memcell capture              # Capture today
            memcell capture 2025-12-15   # Capture specific date
        """
        target_date = date or datetime.now().strftime("%Y-%m-%d")
        print(f"🧠 MEMCELL capturing {target_date}...")
        
        day = DayCapture(
            date=target_date,
            commits=self._capture_git(target_date),
            chats=[],  # Manual or API-based
            tasks=self._capture_tasks(target_date),
            snapshots=[self._capture_system_state()],
            notes=[],
            family_mentions=[]
        )
        
        # Save capture
        self._save_capture(day)
        
        # Update index
        self._update_index(day)
        
        print(f"✅ Captured: {len(day.commits)} commits, {len(day.tasks)} tasks")
        return day
        
    def _capture_git(self, date: str) -> List[GitCommit]:
        """Capture all git commits for a date across tracked repos"""
        commits = []
        next_date = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        
        for repo_path in self.tracked_repos:
            if not os.path.exists(repo_path):
                continue
                
            try:
                # Get commits for this date
                result = subprocess.run(
                    ["git", "log", 
                     f"--since={date}", 
                     f"--until={next_date}",
                     "--pretty=format:%H|%an|%ai|%s",
                     "--name-only"],
                    cwd=repo_path,
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    current_commit = None
                    current_files = []
                    
                    for line in result.stdout.strip().split('\n'):
                        if '|' in line:
                            # Save previous commit
                            if current_commit:
                                current_commit.files_changed = current_files
                                commits.append(current_commit)
                                current_files = []
                            
                            # Parse new commit
                            parts = line.split('|')
                            if len(parts) >= 4:
                                current_commit = GitCommit(
                                    hash=parts[0],
                                    author=parts[1],
                                    date=parts[2],
                                    message=parts[3],
                                    files_changed=[],
                                    repo=os.path.basename(repo_path)
                                )
                        elif line.strip() and current_commit:
                            current_files.append(line.strip())
                    
                    # Don't forget last commit
                    if current_commit:
                        current_commit.files_changed = current_files
                        commits.append(current_commit)
                        
            except Exception as e:
                print(f"⚠️  Git capture error for {repo_path}: {e}")
                
        return commits
        
    def _capture_tasks(self, date: str) -> List[TaskEvent]:
        """Capture VS Code tasks and calendar events"""
        tasks = []
        
        # Check VS Code tasks.json
        vscode_tasks = Path(os.path.expanduser("~/NOIZYLAB/.vscode/tasks.json"))
        if vscode_tasks.exists():
            try:
                with open(vscode_tasks) as f:
                    data = json.load(f)
                    for task in data.get("tasks", []):
                        tasks.append(TaskEvent(
                            id=hashlib.md5(task.get("label", "").encode()).hexdigest()[:8],
                            title=task.get("label", "Unknown"),
                            description=task.get("command", ""),
                            scheduled_time=date,
                            completed=False,
                            recurring=None,
                            source="vscode",
                            linked_commits=[]
                        ))
            except Exception as e:
                print(f"⚠️  VS Code tasks error: {e}")
        
        # Check Apple Calendar via osascript
        try:
            script = f'''
            tell application "Calendar"
                set today to date "{date}"
                set tomorrow to today + 1 * days
                set output to ""
                repeat with cal in calendars
                    set evts to (every event of cal whose start date >= today and start date < tomorrow)
                    repeat with evt in evts
                        set output to output & (summary of evt) & "|" & (start date of evt as string) & "\\n"
                    end repeat
                end repeat
                return output
            end tell
            '''
            result = subprocess.run(
                ["osascript", "-e", script],
                capture_output=True,
                text=True
            )
            if result.returncode == 0 and result.stdout.strip():
                for line in result.stdout.strip().split('\n'):
                    if '|' in line:
                        parts = line.split('|')
                        tasks.append(TaskEvent(
                            id=hashlib.md5(line.encode()).hexdigest()[:8],
                            title=parts[0],
                            description="",
                            scheduled_time=parts[1] if len(parts) > 1 else date,
                            completed=False,
                            recurring=None,
                            source="apple_calendar",
                            linked_commits=[]
                        ))
        except Exception as e:
            print(f"⚠️  Calendar capture error: {e}")
            
        return tasks
        
    def _capture_system_state(self) -> SystemSnapshot:
        """Capture current system state"""
        snapshot = SystemSnapshot(
            timestamp=datetime.now().isoformat(),
            hostname=os.uname().nodename,
            processes=[],
            disk_usage={},
            memory_usage={},
            network_state={},
            active_repos=[]
        )
        
        # Get top processes
        try:
            result = subprocess.run(
                ["ps", "aux", "--sort=-%mem"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')[1:11]  # Top 10
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 11:
                        snapshot.processes.append({
                            "user": parts[0],
                            "pid": parts[1],
                            "cpu": parts[2],
                            "mem": parts[3],
                            "command": ' '.join(parts[10:])
                        })
        except:
            pass
            
        # Get disk usage
        try:
            result = subprocess.run(["df", "-h"], capture_output=True, text=True)
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n')[1:]:
                    parts = line.split()
                    if len(parts) >= 6:
                        snapshot.disk_usage[parts[5]] = {
                            "size": parts[1],
                            "used": parts[2],
                            "avail": parts[3],
                            "percent": parts[4]
                        }
        except:
            pass
            
        return snapshot
        
    def _save_capture(self, day: DayCapture):
        """Save day capture to disk"""
        capture_file = self.captures_path / f"{day.date}.json"
        with open(capture_file, 'w') as f:
            json.dump(asdict(day), f, indent=2, default=str)
            
    def _update_index(self, day: DayCapture):
        """Update database index"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Index commits
        for commit in day.commits:
            cursor.execute('''
                INSERT OR REPLACE INTO commits 
                (hash, author, date, message, repo, files_changed)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (commit.hash, commit.author, commit.date, commit.message, 
                  commit.repo, json.dumps(commit.files_changed)))
                  
            # Full-text index
            cursor.execute('''
                INSERT INTO search_index (date, type, content, tags)
                VALUES (?, ?, ?, ?)
            ''', (day.date, 'commit', f"{commit.message} {' '.join(commit.files_changed)}", commit.repo))
        
        # Index tasks
        for task in day.tasks:
            cursor.execute('''
                INSERT OR REPLACE INTO tasks
                (id, title, description, scheduled_time, completed, recurring, source)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (task.id, task.title, task.description, task.scheduled_time,
                  1 if task.completed else 0, task.recurring, task.source))
                  
        # Daily summary
        cursor.execute('''
            INSERT OR REPLACE INTO daily_index
            (date, commit_count, chat_count, task_count, snapshot_path, summary)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (day.date, len(day.commits), len(day.chats), len(day.tasks),
              str(self.captures_path / f"{day.date}.json"), ""))
              
        conn.commit()
        conn.close()
        
    # ══════════════════════════════════════════════════════════════════════════
    # RECALL - Query the past
    # ══════════════════════════════════════════════════════════════════════════
    
    def recall(self, query: str) -> Dict[str, Any]:
        """
        Natural language recall of past events
        
        Usage:
            memcell recall "monday"
            memcell recall "last week"  
            memcell recall "december 15"
            memcell recall "voice.py commits"
        """
        print(f"🔍 MEMCELL recalling: {query}")
        
        # Parse query for date
        target_date = self._parse_date_query(query)
        
        result = {
            "query": query,
            "date": target_date,
            "commits": [],
            "tasks": [],
            "chats": [],
            "summary": ""
        }
        
        # Load capture file if exists
        capture_file = self.captures_path / f"{target_date}.json"
        if capture_file.exists():
            with open(capture_file) as f:
                day_data = json.load(f)
                result["commits"] = day_data.get("commits", [])
                result["tasks"] = day_data.get("tasks", [])
                result["chats"] = day_data.get("chats", [])
        else:
            # Try live git query
            result["commits"] = [asdict(c) for c in self._capture_git(target_date)]
            
        # Search index for keyword matches
        if not self._is_date_only_query(query):
            result["search_results"] = self._search_index(query)
            
        # Generate summary
        result["summary"] = self._generate_recall_summary(result)
        
        return result
        
    def _parse_date_query(self, query: str) -> str:
        """Parse natural language into date"""
        query_lower = query.lower()
        today = datetime.now()
        
        # Relative dates
        if "today" in query_lower:
            return today.strftime("%Y-%m-%d")
        elif "yesterday" in query_lower:
            return (today - timedelta(days=1)).strftime("%Y-%m-%d")
        elif "monday" in query_lower:
            days_since_monday = today.weekday()
            return (today - timedelta(days=days_since_monday)).strftime("%Y-%m-%d")
        elif "last week" in query_lower:
            return (today - timedelta(days=7)).strftime("%Y-%m-%d")
            
        # Explicit dates
        date_patterns = [
            r'(\d{4}-\d{2}-\d{2})',  # 2025-12-15
            r'(\d{1,2}/\d{1,2}/\d{4})',  # 12/15/2025
            r'(january|february|march|april|may|june|july|august|september|october|november|december)\s+(\d{1,2})',
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, query_lower)
            if match:
                if 'january' in query_lower or 'february' in query_lower:
                    # Month name parsing
                    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                              'may': 5, 'june': 6, 'july': 7, 'august': 8,
                              'september': 9, 'october': 10, 'november': 11, 'december': 12}
                    for month_name, month_num in months.items():
                        if month_name in query_lower:
                            day_match = re.search(r'(\d{1,2})', query_lower)
                            if day_match:
                                day = int(day_match.group(1))
                                year = today.year if today.month >= month_num else today.year - 1
                                return f"{year}-{month_num:02d}-{day:02d}"
                else:
                    return match.group(1)
                    
        # Default to today
        return today.strftime("%Y-%m-%d")
        
    def _is_date_only_query(self, query: str) -> bool:
        """Check if query is just a date reference"""
        date_words = ['today', 'yesterday', 'monday', 'tuesday', 'wednesday', 
                      'thursday', 'friday', 'saturday', 'sunday', 'last week']
        query_lower = query.lower().strip()
        return query_lower in date_words or re.match(r'^\d{4}-\d{2}-\d{2}$', query_lower)
        
    def _search_index(self, query: str) -> List[Dict]:
        """Full-text search across all indexed content"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        results = []
        try:
            cursor.execute('''
                SELECT date, type, content, tags 
                FROM search_index 
                WHERE search_index MATCH ?
                LIMIT 20
            ''', (query,))
            
            for row in cursor.fetchall():
                results.append({
                    "date": row[0],
                    "type": row[1],
                    "content": row[2][:200],
                    "tags": row[3]
                })
        except:
            pass
            
        conn.close()
        return results
        
    def _generate_recall_summary(self, result: Dict) -> str:
        """Generate human-readable summary"""
        lines = [f"📅 {result['date']}"]
        
        if result['commits']:
            lines.append(f"\n📝 GIT COMMITS ({len(result['commits'])}):")
            for commit in result['commits'][:5]:
                lines.append(f"  • {commit.get('message', 'No message')[:60]}")
                
        if result['tasks']:
            lines.append(f"\n✅ TASKS ({len(result['tasks'])}):")
            for task in result['tasks'][:5]:
                status = "✓" if task.get('completed') else "○"
                lines.append(f"  {status} {task.get('title', 'Unknown')}")
                
        if result['chats']:
            lines.append(f"\n💬 CHAT SESSIONS ({len(result['chats'])}):")
            for chat in result['chats'][:3]:
                lines.append(f"  • {chat.get('ai_model', 'Unknown')}: {chat.get('summary', '')[:50]}")
                
        return '\n'.join(lines)
        
    # ══════════════════════════════════════════════════════════════════════════
    # SCHEDULE - Plan the future
    # ══════════════════════════════════════════════════════════════════════════
    
    def schedule(self, title: str, when: str, remind: str = None) -> TaskEvent:
        """
        Schedule a task with optional calendar integration
        
        Usage:
            memcell schedule "deploy" --at "tomorrow 9am"
            memcell schedule "backup" --at "friday 3am" --remind "1h"
        """
        print(f"📅 MEMCELL scheduling: {title}")
        
        # Parse the time
        scheduled_time = self._parse_schedule_time(when)
        
        task = TaskEvent(
            id=hashlib.md5(f"{title}{scheduled_time}".encode()).hexdigest()[:8],
            title=title,
            description="",
            scheduled_time=scheduled_time,
            completed=False,
            recurring=None,
            source="memcell",
            linked_commits=[]
        )
        
        # Save to database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO tasks
            (id, title, description, scheduled_time, completed, recurring, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (task.id, task.title, task.description, task.scheduled_time,
              0, task.recurring, task.source))
        conn.commit()
        conn.close()
        
        # Create Apple Calendar event
        self._create_calendar_event(task, remind)
        
        print(f"✅ Scheduled: {title} at {scheduled_time}")
        return task
        
    def _parse_schedule_time(self, when: str) -> str:
        """Parse scheduling time string"""
        when_lower = when.lower()
        now = datetime.now()
        
        if "tomorrow" in when_lower:
            target = now + timedelta(days=1)
        elif "friday" in when_lower:
            days_ahead = 4 - now.weekday()
            if days_ahead <= 0:
                days_ahead += 7
            target = now + timedelta(days=days_ahead)
        else:
            target = now + timedelta(days=1)
            
        # Parse time component
        time_match = re.search(r'(\d{1,2})(am|pm)?', when_lower)
        if time_match:
            hour = int(time_match.group(1))
            if time_match.group(2) == 'pm' and hour < 12:
                hour += 12
            target = target.replace(hour=hour, minute=0, second=0)
            
        return target.strftime("%Y-%m-%d %H:%M")
        
    def _create_calendar_event(self, task: TaskEvent, remind: str = None):
        """Create Apple Calendar event via osascript"""
        try:
            remind_minutes = 60  # Default 1 hour
            if remind:
                if 'h' in remind:
                    remind_minutes = int(remind.replace('h', '')) * 60
                elif 'm' in remind:
                    remind_minutes = int(remind.replace('m', ''))
                    
            script = f'''
            tell application "Calendar"
                tell calendar "NOIZYLAB"
                    set newEvent to make new event with properties {{
                        summary: "{task.title}",
                        start date: date "{task.scheduled_time}",
                        end date: date "{task.scheduled_time}" + 1 * hours
                    }}
                end tell
            end tell
            '''
            subprocess.run(["osascript", "-e", script], capture_output=True)
            print(f"  📆 Added to Apple Calendar")
        except Exception as e:
            print(f"  ⚠️  Calendar integration skipped: {e}")
            
    # ══════════════════════════════════════════════════════════════════════════
    # SAVE CHAT - Record AI conversations
    # ══════════════════════════════════════════════════════════════════════════
    
    def save_chat(self, content: str, ai_model: str = "claude", 
                  summary: str = "", tags: List[str] = None) -> ChatSession:
        """
        Save an AI chat session to MEMCELL
        
        Usage:
            memcell save-chat "paste conversation here" --model claude --tags "voice,debug"
        """
        chat = ChatSession(
            id=hashlib.md5(f"{content[:100]}{datetime.now().isoformat()}".encode()).hexdigest()[:12],
            timestamp=datetime.now().isoformat(),
            ai_model=ai_model,
            messages=[{"role": "full", "content": content}],
            summary=summary or content[:200],
            tags=tags or []
        )
        
        # Save to file
        chat_file = self.chats_path / f"{chat.timestamp[:10]}_{chat.id}.json"
        with open(chat_file, 'w') as f:
            json.dump(asdict(chat), f, indent=2)
            
        # Index
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO chats (id, timestamp, ai_model, summary, tags, content_path)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (chat.id, chat.timestamp, chat.ai_model, chat.summary, 
              json.dumps(chat.tags), str(chat_file)))
              
        cursor.execute('''
            INSERT INTO search_index (date, type, content, tags)
            VALUES (?, ?, ?, ?)
        ''', (chat.timestamp[:10], 'chat', content[:1000], ' '.join(chat.tags)))
        
        conn.commit()
        conn.close()
        
        print(f"✅ Chat saved: {chat.id}")
        return chat
        
    # ══════════════════════════════════════════════════════════════════════════
    # TIMELINE - Visual history
    # ══════════════════════════════════════════════════════════════════════════
    
    def timeline(self, days: int = 7) -> str:
        """
        Show visual timeline of recent activity
        
        Usage:
            memcell timeline        # Last 7 days
            memcell timeline 30     # Last 30 days
        """
        output = []
        output.append("🧠 MEMCELL TIMELINE")
        output.append("═" * 60)
        
        today = datetime.now()
        
        for i in range(days):
            date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
            day_name = (today - timedelta(days=i)).strftime("%A")
            
            # Get stats
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT commit_count, chat_count, task_count FROM daily_index WHERE date = ?', (date,))
            row = cursor.fetchone()
            
            if row:
                commits, chats, tasks = row
            else:
                # Try live count
                commits = len(self._capture_git(date))
                chats = 0
                tasks = 0
                
            conn.close()
            
            # Visual bar
            activity = commits + chats + tasks
            bar = "█" * min(activity, 20) + "░" * (20 - min(activity, 20))
            
            marker = "→" if i == 0 else " "
            output.append(f"{marker} {date} ({day_name[:3]}) [{bar}] {commits}c {chats}💬 {tasks}✓")
            
        output.append("═" * 60)
        return '\n'.join(output)
        
    # ══════════════════════════════════════════════════════════════════════════
    # FAMILY - Circle of 8 connections
    # ══════════════════════════════════════════════════════════════════════════
    
    def family(self) -> str:
        """Show Circle of 8 status and connections"""
        output = []
        output.append("""
╔═══════════════════════════════════════════════════════════════╗
║              🔮 THE CIRCLE OF 8 - FAMILY STATUS               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║     ┌─────────┐         ┌─────────┐         ┌─────────┐      ║
║     │ GABRIEL │────────▶│  MC96   │────────▶│  OMEGA  │      ║
║     │   🤖    │         │   ⚡    │         │   📡    │      ║
║     └────┬────┘         └────┬────┘         └────┬────┘      ║
║          │                   │                   │            ║
║          ▼                   ▼                   ▼            ║
║     ┌─────────┐         ┌─────────┐         ┌─────────┐      ║
║     │  SHIRL  │◀───────▶│DEEPSEEK │◀───────▶│  KEITH  │      ║
║     │   💜    │         │   🔍    │         │   🔧    │      ║
║     └────┬────┘         └────┬────┘         └────┬────┘      ║
║          │                   │                   │            ║
║          └───────────────────┼───────────────────┘            ║
║                              ▼                                ║
║                    ┌─────────────────┐                        ║
║                    │    TEMPORAL     │                        ║
║                    │       ⏰         │                        ║
║                    └────────┬────────┘                        ║
║                             │                                 ║
║                             ▼                                 ║
║                    ╔═════════════════╗                        ║
║                    ║    MEMCELL      ║                        ║
║                    ║       🧠        ║                        ║
║                    ╚═════════════════╝                        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
        """)
        return '\n'.join(output)


# ══════════════════════════════════════════════════════════════════════════════
# CLI INTERFACE
# ══════════════════════════════════════════════════════════════════════════════

def main():
    """MEMCELL Command Line Interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="🧠 MEMCELL - The NOIZYLAB Time Capsule",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  memcell capture                    Capture today's activity
  memcell recall "monday"            What happened Monday?
  memcell recall "december 15"       What happened Dec 15?
  memcell schedule "deploy" --at "tomorrow 9am"
  memcell timeline                   Show last 7 days
  memcell timeline 30                Show last 30 days
  memcell family                     Show Circle of 8 status
  memcell save-chat "..." --model claude
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # capture
    capture_parser = subparsers.add_parser('capture', help='Capture day activity')
    capture_parser.add_argument('date', nargs='?', help='Date (YYYY-MM-DD)')
    
    # recall
    recall_parser = subparsers.add_parser('recall', help='Recall past events')
    recall_parser.add_argument('query', help='Natural language query')
    
    # schedule  
    schedule_parser = subparsers.add_parser('schedule', help='Schedule a task')
    schedule_parser.add_argument('title', help='Task title')
    schedule_parser.add_argument('--at', required=True, help='When to schedule')
    schedule_parser.add_argument('--remind', help='Reminder time (e.g., 1h, 30m)')
    
    # timeline
    timeline_parser = subparsers.add_parser('timeline', help='Show activity timeline')
    timeline_parser.add_argument('days', nargs='?', type=int, default=7, help='Number of days')
    
    # family
    subparsers.add_parser('family', help='Show Circle of 8 status')
    
    # save-chat
    chat_parser = subparsers.add_parser('save-chat', help='Save AI chat session')
    chat_parser.add_argument('content', help='Chat content')
    chat_parser.add_argument('--model', default='claude', help='AI model used')
    chat_parser.add_argument('--tags', help='Comma-separated tags')
    
    args = parser.parse_args()
    
    # Show banner
    if not args.command:
        print("""
███╗   ███╗███████╗███╗   ███╗ ██████╗███████╗██╗     ██╗     
████╗ ████║██╔════╝████╗ ████║██╔════╝██╔════╝██║     ██║     
██╔████╔██║█████╗  ██╔████╔██║██║     █████╗  ██║     ██║     
██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║     ██╔══╝  ██║     ██║     
██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╗███████╗███████╗███████╗
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝╚══════╝╚══════╝╚══════╝
                                                               
        🧠 THE NOIZYLAB TIME CAPSULE - CIRCLE OF 8 🔮
        
        Commands:
          capture     Snapshot today's activity
          recall      Query the past ("what happened monday?")
          schedule    Plan future tasks with calendar sync
          timeline    Visual history of activity
          family      Circle of 8 status
          save-chat   Save AI conversations
          
        Usage: memcell <command> --help
        """)
        return
        
    # Initialize MEMCELL
    mc = MemCell()
    
    # Execute command
    if args.command == 'capture':
        result = mc.capture(args.date)
        print(f"\n{mc._generate_recall_summary({'date': result.date, 'commits': [asdict(c) for c in result.commits], 'tasks': [asdict(t) for t in result.tasks], 'chats': result.chats})}")
        
    elif args.command == 'recall':
        result = mc.recall(args.query)
        print(f"\n{result['summary']}")
        
    elif args.command == 'schedule':
        mc.schedule(args.title, args.at, args.remind)
        
    elif args.command == 'timeline':
        print(mc.timeline(args.days))
        
    elif args.command == 'family':
        print(mc.family())
        
    elif args.command == 'save-chat':
        tags = args.tags.split(',') if args.tags else []
        mc.save_chat(args.content, args.model, tags=tags)


if __name__ == "__main__":
    main()
