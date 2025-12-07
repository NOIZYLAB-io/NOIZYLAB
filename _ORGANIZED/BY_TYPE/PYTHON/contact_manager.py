#!/usr/bin/env python3
"""
Contact Manager - Address Book System
======================================
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Optional
from rich.console import Console
from rich.table import Table

console = Console()

class ContactManager:
    def __init__(self, contacts_path: str = "config/contacts.json"):
        """Initialize Contact Manager"""
        self.contacts_path = Path(contacts_path)
        self.contacts_path.parent.mkdir(parents=True, exist_ok=True)
        self.contacts = self.load_contacts()
    
    def load_contacts(self) -> Dict:
        """Load contacts from file"""
        if not self.contacts_path.exists():
            return {}
        
        try:
            with open(self.contacts_path, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def save_contacts(self):
        """Save contacts to file"""
        with open(self.contacts_path, 'w') as f:
            json.dump(self.contacts, f, indent=2)
    
    def add_contact(self, name: str, email: str, company: str = "", notes: str = ""):
        """Add a new contact"""
        contact_id = email.lower().strip()
        
        self.contacts[contact_id] = {
            "name": name,
            "email": email,
            "company": company,
            "notes": notes
        }
        
        self.save_contacts()
        console.print(f"[green]✅ Contact added: {name} ({email})[/green]")
    
    def get_contact(self, email: str) -> Optional[Dict]:
        """Get contact by email"""
        return self.contacts.get(email.lower().strip())
    
    def list_contacts(self) -> List[Dict]:
        """Get all contacts as list"""
        return [
            {"id": email, **info}
            for email, info in self.contacts.items()
        ]
    
    def display_contacts_table(self):
        """Display contacts in a Rich table"""
        if not self.contacts:
            console.print("[yellow]No contacts yet. Add some first![/yellow]")
            return
        
        table = Table(title="📇 Address Book", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Email", style="green")
        table.add_column("Company", style="yellow")
        
        for contact_id, contact in self.contacts.items():
            table.add_row(
                contact.get("name", ""),
                contact.get("email", ""),
                contact.get("company", "")
            )
        
        console.print(table)
    
    def search_contacts(self, query: str) -> List[Dict]:
        """Search contacts by name or email"""
        query_lower = query.lower()
        results = []
        
        for contact_id, contact in self.contacts.items():
            if (query_lower in contact.get("name", "").lower() or
                query_lower in contact.get("email", "").lower() or
                query_lower in contact.get("company", "").lower()):
                results.append({"id": contact_id, **contact})
        
        return results

