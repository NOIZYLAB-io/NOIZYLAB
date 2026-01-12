#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
🧠 MEMCELL CHRONICLE - THE ULTIMATE CODE ORGANIZER
═══════════════════════════════════════════════════════════════════════════════

Consolidates ALL code by:
1. Chat Session Title (project name)
2. Date created
3. Calendar tracking
4. Auto-linking related files

Structure:
~/.memcell/
├── chronicle/
│   ├── 2026-01-05_MEMCELL-TimeCapule/
│   │   ├── SESSION.md
│   │   ├── MANIFEST.json
│   │   ├── code/
│   │   │   ├── memcell.py
│   │   │   ├── mc96_terminal.py
│   │   │   └── cleanspace.py
│   │   └── chat/
│   │       └── transcript.md
│   ├── 2026-01-04_GABRIEL-Voice/
│   │   └── ...
│   └── index.json
├── calendar/
│   ├── 2026-01.ics
│   └── events.json
└── projects/
    ├── MEMCELL -> ../chronicle/2026-01-05_MEMCELL-TimeCapsule/
    ├── MC96 -> ...
    └── GABRIEL -> ...

Authors: NOIZYLAB + CIRCLE OF 8
"""

import os
import sys
import json
import shutil
import hashlib
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict, field
import re

# ═══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ChatSession:
    """A chat session with AI that produced code"""
    id: str
    title: str
    date: str
    ai_model: str
    summary: str
    files_created: List[str]
    tags: List[str]
    linked_projects: List[str]

@dataclass
class Project:
    """A consolidated project from one or more chat sessions"""
    id: str
    name: str
    created: str
    updated: str
    sessions: List[str]  # Chat session IDs
    files: List[str]
    description: str
    status: str  # active, archived, completed
    calendar_events: List[str]

@dataclass
class CalendarEvent:
    """A calendar event linked to code/projects"""
    id: str
    title: str
    date: str
    time: str
    type: str  # session, deadline, deploy, review
    project_id: str
    session_id: str
    notes: str


# ═══════════════════════════════════════════════════════════════════════════════
# MEMCELL CHRONICLE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class Chronicle:
    """
    THE ULTIMATE CODE ORGANIZER
    
    Every chat session → Folder by title + date
    Every file → Linked to session + project
    Calendar → Tracks everything
    """
    
    VERSION = "1.0.0"
    
    def __init__(self, base_path: str = None):
        self.base_path = Path(base_path or os.path.expanduser("~/.memcell"))
        self.chronicle_path = self.base_path / "chronicle"
        self.calendar_path = self.base_path / "calendar"
        self.projects_path = self.base_path / "projects"
        self.index_path = self.base_path / "index.json"
        
        self._init_storage()
        self._load_index()
        
    def _init_storage(self):
        """Create directory structure"""
        for path in [self.chronicle_path, self.calendar_path, self.projects_path]:
            path.mkdir(parents=True, exist_ok=True)
            
    def _load_index(self):
        """Load master index"""
        if self.index_path.exists():
            with open(self.index_path) as f:
                self.index = json.load(f)
        else:
            self.index = {
                "sessions": {},
                "projects": {},
                "events": {},
                "files": {}
            }
            
    def _save_index(self):
        """Save master index"""
        with open(self.index_path, 'w') as f:
            json.dump(self.index, f, indent=2)
            
    # ═══════════════════════════════════════════════════════════════════════════
    # NEW SESSION - Start tracking a new chat
    # ═══════════════════════════════════════════════════════════════════════════
    
    def new_session(self, title: str, ai_model: str = "claude", 
                    tags: List[str] = None) -> ChatSession:
        """
        Start a new chat session for tracking
        
        Usage:
            chronicle new "MEMCELL Time Capsule" --tags "memory,calendar"
        """
        date = datetime.now().strftime("%Y-%m-%d")
        session_id = f"{date}_{self._slugify(title)}"
        
        session = ChatSession(
            id=session_id,
            title=title,
            date=date,
            ai_model=ai_model,
            summary="",
            files_created=[],
            tags=tags or [],
            linked_projects=[]
        )
        
        # Create session directory
        session_dir = self.chronicle_path / session_id
        session_dir.mkdir(parents=True, exist_ok=True)
        (session_dir / "code").mkdir(exist_ok=True)
        (session_dir / "chat").mkdir(exist_ok=True)
        
        # Create session manifest
        manifest = {
            "session": asdict(session),
            "created": datetime.now().isoformat(),
            "chronicle_version": self.VERSION
        }
        with open(session_dir / "MANIFEST.json", 'w') as f:
            json.dump(manifest, f, indent=2)
            
        # Create session README
        readme = f"""# {title}

**Date:** {date}
**AI Model:** {ai_model}
**Tags:** {', '.join(tags or [])}

## Files Created

_No files yet_

## Summary

_Session in progress..._

---
*Tracked by MEMCELL Chronicle*
"""
        with open(session_dir / "SESSION.md", 'w') as f:
            f.write(readme)
            
        # Add to index
        self.index["sessions"][session_id] = asdict(session)
        self._save_index()
        
        # Create calendar event
        self._add_calendar_event(
            title=f"📝 {title}",
            date=date,
            time=datetime.now().strftime("%H:%M"),
            event_type="session",
            project_id="",
            session_id=session_id,
            notes=f"Chat session started: {title}"
        )
        
        print(f"✅ Session created: {session_id}")
        print(f"📁 Location: {session_dir}")
        return session
        
    def _slugify(self, text: str) -> str:
        """Convert text to slug for folder names"""
        slug = re.sub(r'[^\w\s-]', '', text.lower())
        slug = re.sub(r'[-\s]+', '-', slug).strip('-')
        return slug[:50]  # Limit length
        
    # ═══════════════════════════════════════════════════════════════════════════
    # ADD FILE - Track a file created in session
    # ═══════════════════════════════════════════════════════════════════════════
    
    def add_file(self, session_id: str, file_path: str, 
                 copy: bool = True, description: str = "") -> str:
        """
        Add a file to a session
        
        Usage:
            chronicle add-file "2026-01-05_memcell" ~/code/memcell.py
        """
        if session_id not in self.index["sessions"]:
            # Try to find by partial match
            matches = [s for s in self.index["sessions"] if session_id in s]
            if matches:
                session_id = matches[0]
            else:
                print(f"❌ Session not found: {session_id}")
                return None
                
        session_dir = self.chronicle_path / session_id / "code"
        source = Path(file_path).expanduser()
        
        if not source.exists():
            print(f"❌ File not found: {source}")
            return None
            
        dest = session_dir / source.name
        
        if copy:
            shutil.copy2(source, dest)
            print(f"📄 Copied: {source.name}")
        else:
            # Create symlink
            dest.symlink_to(source.absolute())
            print(f"🔗 Linked: {source.name}")
            
        # Update index
        self.index["sessions"][session_id]["files_created"].append(str(source))
        self.index["files"][str(source)] = {
            "session": session_id,
            "added": datetime.now().isoformat(),
            "description": description
        }
        self._save_index()
        
        # Update session README
        self._update_session_readme(session_id)
        
        return str(dest)
        
    def _update_session_readme(self, session_id: str):
        """Update session README with file list"""
        session = self.index["sessions"].get(session_id, {})
        session_dir = self.chronicle_path / session_id
        readme_path = session_dir / "SESSION.md"
        
        files_section = "## Files Created\n\n"
        for f in session.get("files_created", []):
            name = Path(f).name
            files_section += f"- `{name}`\n"
            
        if not session.get("files_created"):
            files_section += "_No files yet_\n"
            
        # Read and update README
        if readme_path.exists():
            content = readme_path.read_text()
            # Replace files section
            content = re.sub(
                r'## Files Created\n\n.*?(?=\n## |\n---|\Z)',
                files_section + "\n",
                content,
                flags=re.DOTALL
            )
            readme_path.write_text(content)
            
    # ═══════════════════════════════════════════════════════════════════════════
    # CONSOLIDATE - Merge sessions into project
    # ═══════════════════════════════════════════════════════════════════════════
    
    def consolidate(self, project_name: str, session_ids: List[str], 
                    description: str = "") -> Project:
        """
        Consolidate multiple sessions into a single project
        
        Usage:
            chronicle consolidate "MEMCELL" --sessions "2026-01-05_memcell,2026-01-04_memory"
        """
        project_id = self._slugify(project_name)
        
        # Collect all files from sessions
        all_files = []
        for sid in session_ids:
            if sid in self.index["sessions"]:
                all_files.extend(self.index["sessions"][sid].get("files_created", []))
                
        project = Project(
            id=project_id,
            name=project_name,
            created=datetime.now().strftime("%Y-%m-%d"),
            updated=datetime.now().strftime("%Y-%m-%d"),
            sessions=session_ids,
            files=all_files,
            description=description,
            status="active",
            calendar_events=[]
        )
        
        # Create project symlink
        project_link = self.projects_path / project_name
        if project_link.exists():
            project_link.unlink()
            
        # Link to most recent session
        if session_ids:
            latest_session = sorted(session_ids)[-1]
            target = self.chronicle_path / latest_session
            if target.exists():
                project_link.symlink_to(target)
                
        # Update index
        self.index["projects"][project_id] = asdict(project)
        self._save_index()
        
        print(f"✅ Project consolidated: {project_name}")
        print(f"📁 Sessions: {len(session_ids)}")
        print(f"📄 Files: {len(all_files)}")
        
        return project
        
    # ═══════════════════════════════════════════════════════════════════════════
    # CALENDAR - Track everything in time
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _add_calendar_event(self, title: str, date: str, time: str,
                           event_type: str, project_id: str, 
                           session_id: str, notes: str) -> str:
        """Add event to calendar"""
        event_id = hashlib.md5(f"{title}{date}{time}".encode()).hexdigest()[:12]
        
        event = CalendarEvent(
            id=event_id,
            title=title,
            date=date,
            time=time,
            type=event_type,
            project_id=project_id,
            session_id=session_id,
            notes=notes
        )
        
        # Save to index
        self.index["events"][event_id] = asdict(event)
        self._save_index()
        
        # Generate ICS file
        self._generate_ics()
        
        # Optionally add to Apple Calendar
        self._add_to_apple_calendar(event)
        
        return event_id
        
    def _generate_ics(self):
        """Generate ICS calendar file"""
        ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//MEMCELL Chronicle//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:MEMCELL Chronicle
"""
        for event_id, event in self.index.get("events", {}).items():
            dt = f"{event['date'].replace('-', '')}T{event['time'].replace(':', '')}00"
            ics_content += f"""BEGIN:VEVENT
UID:{event_id}@memcell
DTSTART:{dt}
DTEND:{dt}
SUMMARY:{event['title']}
DESCRIPTION:{event['notes']}
CATEGORIES:{event['type']}
END:VEVENT
"""
        ics_content += "END:VCALENDAR"
        
        # Save monthly ICS
        month = datetime.now().strftime("%Y-%m")
        ics_path = self.calendar_path / f"{month}.ics"
        with open(ics_path, 'w') as f:
            f.write(ics_content)
            
    def _add_to_apple_calendar(self, event: CalendarEvent):
        """Add event to Apple Calendar"""
        try:
            script = f'''
            tell application "Calendar"
                tell calendar "MEMCELL"
                    make new event with properties {{
                        summary: "{event.title}",
                        start date: date "{event.date} {event.time}",
                        end date: date "{event.date} {event.time}" + 1 * hours,
                        description: "{event.notes}"
                    }}
                end tell
            end tell
            '''
            subprocess.run(["osascript", "-e", script], 
                          capture_output=True, timeout=5)
        except:
            pass  # Silent fail if Calendar not available
            
    def calendar(self, days: int = 7) -> str:
        """
        Show calendar view of sessions and events
        
        Usage:
            chronicle calendar        # Next 7 days
            chronicle calendar 30     # Next 30 days
        """
        output = []
        output.append("🗓️  MEMCELL CHRONICLE CALENDAR")
        output.append("═" * 60)
        
        today = datetime.now()
        
        for i in range(days):
            date = (today + timedelta(days=i)).strftime("%Y-%m-%d")
            day_name = (today + timedelta(days=i)).strftime("%A")
            
            # Find sessions on this date
            sessions = [s for s in self.index.get("sessions", {}).values() 
                       if s.get("date") == date]
            
            # Find events on this date
            events = [e for e in self.index.get("events", {}).values()
                     if e.get("date") == date]
            
            marker = "▶" if i == 0 else " "
            
            if sessions or events:
                output.append(f"\n{marker} {date} ({day_name})")
                for s in sessions:
                    output.append(f"   📝 {s['title']}")
                for e in events:
                    output.append(f"   {self._event_emoji(e['type'])} {e['time']} {e['title']}")
            elif i == 0:
                output.append(f"\n{marker} {date} ({day_name}) - No events")
                
        output.append("\n" + "═" * 60)
        return '\n'.join(output)
        
    def _event_emoji(self, event_type: str) -> str:
        """Get emoji for event type"""
        emojis = {
            "session": "💬",
            "deadline": "🔴",
            "deploy": "🚀",
            "review": "👀",
            "meeting": "📞"
        }
        return emojis.get(event_type, "📌")
        
    # ═══════════════════════════════════════════════════════════════════════════
    # LIST - Show all sessions and projects
    # ═══════════════════════════════════════════════════════════════════════════
    
    def list_sessions(self) -> str:
        """List all tracked sessions"""
        output = []
        output.append("📚 MEMCELL CHRONICLE - SESSIONS")
        output.append("═" * 60)
        
        sessions = sorted(
            self.index.get("sessions", {}).items(),
            key=lambda x: x[0],
            reverse=True
        )
        
        for session_id, session in sessions[:20]:
            files_count = len(session.get("files_created", []))
            output.append(f"\n📁 {session_id}")
            output.append(f"   Title: {session['title']}")
            output.append(f"   Files: {files_count}")
            output.append(f"   Tags: {', '.join(session.get('tags', []))}")
            
        output.append("\n" + "═" * 60)
        output.append(f"Total: {len(sessions)} sessions")
        return '\n'.join(output)
        
    def list_projects(self) -> str:
        """List all consolidated projects"""
        output = []
        output.append("🚀 MEMCELL CHRONICLE - PROJECTS")
        output.append("═" * 60)
        
        for project_id, project in self.index.get("projects", {}).items():
            output.append(f"\n📦 {project['name']}")
            output.append(f"   Status: {project['status']}")
            output.append(f"   Sessions: {len(project['sessions'])}")
            output.append(f"   Files: {len(project['files'])}")
            
        output.append("\n" + "═" * 60)
        return '\n'.join(output)
        
    # ═══════════════════════════════════════════════════════════════════════════
    # IMPORT - Bulk import existing files
    # ═══════════════════════════════════════════════════════════════════════════
    
    def import_folder(self, folder_path: str, session_title: str,
                      pattern: str = "*.py") -> int:
        """
        Import existing folder of code into a session
        
        Usage:
            chronicle import ~/NOIZYLAB/gabriel/memcell "MEMCELL Import" --pattern "*.py"
        """
        import glob
        
        folder = Path(folder_path).expanduser()
        if not folder.exists():
            print(f"❌ Folder not found: {folder}")
            return 0
            
        # Create new session
        session = self.new_session(session_title, tags=["import"])
        
        # Find and add files
        files = list(folder.glob(f"**/{pattern}"))
        for f in files:
            self.add_file(session.id, str(f), copy=True)
            
        print(f"✅ Imported {len(files)} files")
        return len(files)


# ═══════════════════════════════════════════════════════════════════════════════
# CLI INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """Chronicle CLI"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="🧠 MEMCELL Chronicle - Code Organization System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  chronicle new "MEMCELL Time Capsule" --tags memory,calendar
  chronicle add-file 2026-01-05_memcell ~/code/memcell.py
  chronicle consolidate "MEMCELL" --sessions "session1,session2"
  chronicle calendar 14
  chronicle list
  chronicle import ~/code/project "Legacy Import"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # new
    new_parser = subparsers.add_parser('new', help='Start new session')
    new_parser.add_argument('title', help='Session title')
    new_parser.add_argument('--tags', help='Comma-separated tags')
    new_parser.add_argument('--model', default='claude', help='AI model')
    
    # add-file
    add_parser = subparsers.add_parser('add-file', help='Add file to session')
    add_parser.add_argument('session', help='Session ID')
    add_parser.add_argument('file', help='File path')
    add_parser.add_argument('--link', action='store_true', help='Symlink instead of copy')
    
    # consolidate
    cons_parser = subparsers.add_parser('consolidate', help='Consolidate sessions')
    cons_parser.add_argument('name', help='Project name')
    cons_parser.add_argument('--sessions', required=True, help='Comma-separated session IDs')
    
    # calendar
    cal_parser = subparsers.add_parser('calendar', help='Show calendar')
    cal_parser.add_argument('days', nargs='?', type=int, default=7)
    
    # list
    list_parser = subparsers.add_parser('list', help='List sessions')
    list_parser.add_argument('--projects', action='store_true', help='List projects instead')
    
    # import
    imp_parser = subparsers.add_parser('import', help='Import folder')
    imp_parser.add_argument('folder', help='Folder path')
    imp_parser.add_argument('title', help='Session title')
    imp_parser.add_argument('--pattern', default='*.py', help='File pattern')
    
    args = parser.parse_args()
    
    # Show banner if no command
    if not args.command:
        print("""
🧠 MEMCELL CHRONICLE - Code Organization System
═══════════════════════════════════════════════════════════════

Organize ALL code by:
  • Chat session title
  • Date created  
  • Calendar tracking
  • Project consolidation

Commands:
  new          Start tracking a new chat session
  add-file     Add file to current session
  consolidate  Merge sessions into project
  calendar     View calendar of sessions
  list         List all sessions/projects
  import       Import existing code folder

Usage: chronicle <command> --help
        """)
        return
        
    # Execute
    c = Chronicle()
    
    if args.command == 'new':
        tags = args.tags.split(',') if args.tags else []
        c.new_session(args.title, args.model, tags)
        
    elif args.command == 'add-file':
        c.add_file(args.session, args.file, copy=not args.link)
        
    elif args.command == 'consolidate':
        sessions = args.sessions.split(',')
        c.consolidate(args.name, sessions)
        
    elif args.command == 'calendar':
        print(c.calendar(args.days))
        
    elif args.command == 'list':
        if args.projects:
            print(c.list_projects())
        else:
            print(c.list_sessions())
            
    elif args.command == 'import':
        c.import_folder(args.folder, args.title, args.pattern)


if __name__ == "__main__":
    main()
