#!/usr/bin/env python3
"""
Advanced Template Engine - Smart Email Templates with Variables
==================================================================
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

class AdvancedTemplateEngine:
    def __init__(self, templates_path: str = "config/templates.json"):
        """Initialize Advanced Template Engine"""
        self.templates_path = Path(templates_path)
        self.templates_path.parent.mkdir(parents=True, exist_ok=True)
        self.templates = self.load_templates()
        self.ensure_default_templates()
    
    def load_templates(self) -> Dict:
        """Load templates from file"""
        if not self.templates_path.exists():
            return {}
        
        try:
            with open(self.templates_path, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def save_templates(self):
        """Save templates to file"""
        with open(self.templates_path, 'w') as f:
            json.dump(self.templates, f, indent=2)
    
    def ensure_default_templates(self):
        """Ensure default templates exist"""
        defaults = {
            "meeting_request": {
                "name": "Meeting Request",
                "category": "Business",
                "subject": "Meeting Request: {topic}",
                "body": """Hi {name},

I hope this email finds you well. I would like to schedule a meeting to discuss {topic}.

Please let me know your availability for the following times:
- {date1}
- {date2}
- {date3}

Looking forward to hearing from you.

Best regards,
{your_name}""",
                "variables": ["name", "topic", "date1", "date2", "date3", "your_name"]
            },
            "invoice": {
                "name": "Invoice",
                "category": "Business",
                "subject": "Invoice #{invoice_number} - {company}",
                "body": """Dear {name},

Please find attached invoice #{invoice_number} for services rendered.

Invoice Details:
- Amount: ${amount}
- Due Date: {due_date}
- Description: {description}

Payment can be made via {payment_method}.

Thank you for your business.

Best regards,
{your_name}""",
                "variables": ["name", "invoice_number", "company", "amount", "due_date", "description", "payment_method", "your_name"]
            },
            "follow_up": {
                "name": "Follow-up",
                "category": "Business",
                "subject": "Following up on {topic}",
                "body": """Hi {name},

I wanted to follow up on our previous conversation regarding {topic}.

{follow_up_message}

Please let me know if you have any questions or need further information.

Best regards,
{your_name}""",
                "variables": ["name", "topic", "follow_up_message", "your_name"]
            },
            "thank_you": {
                "name": "Thank You",
                "category": "Personal",
                "subject": "Thank You - {topic}",
                "body": """Dear {name},

Thank you for {reason}.

{additional_message}

I truly appreciate your {appreciation_reason}.

Best regards,
{your_name}""",
                "variables": ["name", "topic", "reason", "additional_message", "appreciation_reason", "your_name"]
            },
            "introduction": {
                "name": "Introduction",
                "category": "Business",
                "subject": "Introduction: {your_name}",
                "body": """Hi {name},

I hope this email finds you well. My name is {your_name} and I'm reaching out because {reason}.

{introduction_message}

I would love to connect and discuss how we might {collaboration_idea}.

Best regards,
{your_name}""",
                "variables": ["name", "your_name", "reason", "introduction_message", "collaboration_idea"]
            },
            "proposal": {
                "name": "Project Proposal",
                "category": "Business",
                "subject": "Project Proposal: {project_name}",
                "body": """Dear {name},

I'm excited to present a proposal for {project_name}.

Project Overview:
{project_overview}

Key Benefits:
{key_benefits}

Timeline: {timeline}
Budget: ${budget}

I'd love to discuss this further. Would you be available for a call this week?

Best regards,
{your_name}""",
                "variables": ["name", "project_name", "project_overview", "key_benefits", "timeline", "budget", "your_name"]
            }
        }
        
        updated = False
        for key, template in defaults.items():
            if key not in self.templates:
                self.templates[key] = template
                updated = True
        
        if updated:
            self.save_templates()
    
    def get_template(self, template_key: str) -> Dict:
        """Get template by key"""
        return self.templates.get(template_key, {})
    
    def list_templates(self, category: Optional[str] = None) -> List[Dict]:
        """Get all templates, optionally filtered by category"""
        templates = [
            {"key": key, **info}
            for key, info in self.templates.items()
        ]
        
        if category:
            templates = [t for t in templates if t.get('category', '').lower() == category.lower()]
        
        return templates
    
    def render_template(self, template_key: str, variables: Dict) -> Dict:
        """Render template with variables"""
        template = self.get_template(template_key)
        if not template:
            return {"subject": "", "body": ""}
        
        subject = template.get("subject", "")
        body = template.get("body", "")
        
        # Replace variables
        for key, value in variables.items():
            subject = subject.replace(f"{{{key}}}", str(value))
            body = body.replace(f"{{{key}}}", str(value))
        
        # Replace any remaining variables with empty string
        subject = re.sub(r'\{[^}]+\}', '', subject)
        body = re.sub(r'\{[^}]+\}', '', body)
        
        return {"subject": subject, "body": body}
    
    def get_template_variables(self, template_key: str) -> List[str]:
        """Get list of variables needed for a template"""
        template = self.get_template(template_key)
        return template.get("variables", [])
    
    def create_custom_template(self, key: str, name: str, subject: str, body: str, 
                               category: str = "Custom", variables: Optional[List[str]] = None):
        """Create a custom template"""
        if variables is None:
            # Auto-detect variables
            var_pattern = r'\{(\w+)\}'
            variables = list(set(re.findall(var_pattern, subject + body)))
        
        self.templates[key] = {
            "name": name,
            "category": category,
            "subject": subject,
            "body": body,
            "variables": variables
        }
        
        self.save_templates()
        console.print(f"[green]✅ Template '{name}' created![/green]")
    
    def display_templates(self, category: Optional[str] = None):
        """Display available templates"""
        templates = self.list_templates(category)
        
        if not templates:
            console.print("[yellow]No templates available[/yellow]")
            return
        
        table = Table(title="📝 Email Templates", show_header=True, header_style="bold magenta")
        table.add_column("Key", style="cyan", width=15)
        table.add_column("Name", style="green")
        table.add_column("Category", style="yellow")
        table.add_column("Variables", style="dim")
        
        for template in templates:
            vars_str = ", ".join(template.get("variables", []))[:30]
            table.add_row(
                template['key'],
                template.get('name', ''),
                template.get('category', ''),
                vars_str + "..." if len(vars_str) > 30 else vars_str
            )
        
        console.print(table)

