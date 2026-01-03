#!/usr/bin/env python3
"""
Template Engine - Smart Email Templates
========================================
"""

import json
from pathlib import Path
from typing import Dict, List
from rich.console import Console
from rich.panel import Panel

console = Console()

class TemplateEngine:
    def __init__(self, templates_path: str = "config/templates.json"):
        """Initialize Template Engine"""
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
                "subject": "Meeting Request: {topic}",
                "body": """Hi {name},

I hope this email finds you well. I would like to schedule a meeting to discuss {topic}.

Please let me know your availability for the following times:
- {date1}
- {date2}
- {date3}

Looking forward to hearing from you.

Best regards,
{your_name}"""
            },
            "invoice": {
                "name": "Invoice",
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
{your_name}"""
            },
            "follow_up": {
                "name": "Follow-up",
                "subject": "Following up on {topic}",
                "body": """Hi {name},

I wanted to follow up on our previous conversation regarding {topic}.

{follow_up_message}

Please let me know if you have any questions or need further information.

Best regards,
{your_name}"""
            },
            "thank_you": {
                "name": "Thank You",
                "subject": "Thank You - {topic}",
                "body": """Dear {name},

Thank you for {reason}.

{additional_message}

I truly appreciate your {appreciation_reason}.

Best regards,
{your_name}"""
            },
            "introduction": {
                "name": "Introduction",
                "subject": "Introduction: {your_name}",
                "body": """Hi {name},

I hope this email finds you well. My name is {your_name} and I'm reaching out because {reason}.

{introduction_message}

I would love to connect and discuss how we might {collaboration_idea}.

Best regards,
{your_name}"""
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
    
    def list_templates(self) -> List[Dict]:
        """Get all templates"""
        return [
            {"key": key, **info}
            for key, info in self.templates.items()
        ]
    
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
        
        return {"subject": subject, "body": body}
    
    def display_templates(self):
        """Display available templates"""
        if not self.templates:
            console.print("[yellow]No templates available[/yellow]")
            return
        
        for key, template in self.templates.items():
            console.print(Panel(
                f"[bold]{template.get('name', key)}[/bold]\n\n"
                f"Subject: {template.get('subject', 'N/A')}\n"
                f"Preview: {template.get('body', '')[:100]}...",
                title=f"📝 {key}",
                border_style="blue"
            ))

