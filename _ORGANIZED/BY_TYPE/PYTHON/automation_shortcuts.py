# ROB OS - AUTOMATION SHORTCUTS
# ==============================
# Make your system feel magical
# "You never touch the file system manually again"

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import json

@dataclass
class Shortcut:
    """A voice/keyboard shortcut that does real work."""
    id: str
    name: str
    trigger: str  # Voice command or keyboard shortcut
    description: str
    actions: List[str]
    category: str  # "studio", "client", "flow", "sanctuary"

# ============================================
# THE SHORTCUTS
# ============================================

SHORTCUTS: Dict[str, Shortcut] = {
    
    # ========== STUDIO SHORTCUTS ==========
    
    "summon_studio": Shortcut(
        id="summon_studio",
        name="Summon My Studio",
        trigger="Hey Siri, summon my studio",
        description="One command to start your day right.",
        actions=[
            "Open MC96 dashboard",
            "Mount GABRIEL",
            "Open today's FLOW file",
            "Start relaxing intro sound"
        ],
        category="studio"
    ),
    
    "studio_shutdown": Shortcut(
        id="studio_shutdown",
        name="Studio Shutdown",
        trigger="Hey Siri, shutdown studio",
        description="Clean end to your work day.",
        actions=[
            "Save all open documents",
            "Run quick backup check",
            "Log today's wins to FLOW file",
            "Fade out to evening world",
            "Close non-essential apps"
        ],
        category="studio"
    ),
    
    # ========== CLIENT SHORTCUTS ==========
    
    "new_client": Shortcut(
        id="new_client",
        name="New Client Setup",
        trigger="Hey Siri, new client [NAME]",
        description="Auto-create client folder with all templates.",
        actions=[
            "Create /NOIZY_OS/NOIZYLAB/Clients/[NAME]/",
            "Drop Intake.md template",
            "Drop Report.md template",
            "Drop Invoice.md template",
            "Open Intake.md for editing"
        ],
        category="client"
    ),
    
    "start_triage": Shortcut(
        id="start_triage",
        name="Start Triage Session",
        trigger="Hey Siri, start triage",
        description="Begin a focused diagnostic session.",
        actions=[
            "Start 45-minute timer",
            "Open Triage checklist",
            "Prepare new Report document",
            "Set world to MC96 Midnight",
            "When timer ends, prompt to save"
        ],
        category="client"
    ),
    
    "client_report": Shortcut(
        id="client_report",
        name="Generate Client Report",
        trigger="Hey Siri, generate report for [CLIENT]",
        description="Auto-generate report from session notes.",
        actions=[
            "Read session log",
            "Generate human summary",
            "Generate tech summary",
            "Format as Miracle Receipt",
            "Open for review"
        ],
        category="client"
    ),
    
    # ========== FLOW SHORTCUTS ==========
    
    "morning_flow": Shortcut(
        id="morning_flow",
        name="Morning Flow",
        trigger="Hey Siri, start my morning",
        description="Begin the day with intention.",
        actions=[
            "Open FLOW.md",
            "Set world to Skyroom",
            "Show today's priorities",
            "Start 30-min warm-up timer",
            "Play morning soundscape"
        ],
        category="flow"
    ),
    
    "work_block": Shortcut(
        id="work_block",
        name="Start Work Block",
        trigger="Hey Siri, work block",
        description="90-minute focused work session.",
        actions=[
            "Set world to MC96 Midnight",
            "Start 90-minute timer",
            "Enable Do Not Disturb",
            "Hide distracting apps",
            "When done, suggest recovery break"
        ],
        category="flow"
    ),
    
    "recovery_break": Shortcut(
        id="recovery_break",
        name="Recovery Break",
        trigger="Hey Siri, recovery break",
        description="Short reset between work blocks.",
        actions=[
            "Set world to Soft Tide",
            "Start 15-minute timer",
            "Offer guided breath",
            "Suggest stretch",
            "When done, ask: continue or stop?"
        ],
        category="flow"
    ),
    
    "log_win": Shortcut(
        id="log_win",
        name="Log a Win",
        trigger="Hey Siri, log win [DESCRIPTION]",
        description="Capture wins as they happen.",
        actions=[
            "Transcribe description",
            "Add to today's FLOW.md wins section",
            "Play small celebration sound"
        ],
        category="flow"
    ),
    
    "daily_log": Shortcut(
        id="daily_log",
        name="Daily Log",
        trigger="Hey Siri, daily log",
        description="End-of-day voice note capture.",
        actions=[
            "Start recording",
            "Transcribe when done",
            "Add to FLOW.md under today's date",
            "Archive audio file"
        ],
        category="flow"
    ),
    
    # ========== SANCTUARY SHORTCUTS ==========
    
    "sanctuary_now": Shortcut(
        id="sanctuary_now",
        name="Sanctuary Now",
        trigger="Hey Siri, sanctuary",
        description="Immediate calm environment.",
        actions=[
            "Set world to Rain on the Roof",
            "Lower screen brightness",
            "Enable Do Not Disturb",
            "Offer guided breath"
        ],
        category="sanctuary"
    ),
    
    "silent_mode": Shortcut(
        id="silent_mode",
        name="Silent Mode",
        trigger="Hey Siri, silent mode",
        description="Maximum quiet for sensory overload.",
        actions=[
            "Set world to Silent Shore",
            "Mute all notifications",
            "Lower brightness to minimum",
            "Display only: 'You're safe. Take your time.'"
        ],
        category="sanctuary"
    ),
    
    "breath_break": Shortcut(
        id="breath_break",
        name="Breath Break",
        trigger="Hey Siri, breath break",
        description="Quick guided breathing.",
        actions=[
            "Play 20-second NOIZY Breath",
            "Lower all other audio",
            "When done, gently return to previous state"
        ],
        category="sanctuary"
    )
}


class AutomationEngine:
    """
    The Automation Engine - Makes shortcuts actually work.
    """
    
    def __init__(self):
        self.shortcuts = SHORTCUTS
        self.base_path = Path("/Users/m2ultra/NOIZYLAB")
        self.clients_path = self.base_path / "Clients"
    
    def get_shortcut(self, shortcut_id: str) -> Optional[Shortcut]:
        return self.shortcuts.get(shortcut_id)
    
    def get_all_shortcuts(self) -> Dict[str, Shortcut]:
        return self.shortcuts
    
    def get_by_category(self, category: str) -> List[Shortcut]:
        return [s for s in self.shortcuts.values() if s.category == category]
    
    def create_client_folder(self, client_name: str) -> Dict[str, Any]:
        """
        Create a new client folder with all templates.
        """
        client_path = self.clients_path / client_name
        
        # Create folder structure
        folders_created = []
        files_created = []
        
        try:
            client_path.mkdir(parents=True, exist_ok=True)
            folders_created.append(str(client_path))
            
            # Create template files
            templates = {
                "Intake.md": self._get_intake_template(client_name),
                "Report.md": self._get_report_template(client_name),
                "Invoice.md": self._get_invoice_template(client_name)
            }
            
            for filename, content in templates.items():
                file_path = client_path / filename
                file_path.write_text(content)
                files_created.append(str(file_path))
            
            return {
                "success": True,
                "client_path": str(client_path),
                "folders_created": folders_created,
                "files_created": files_created
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _get_intake_template(self, client_name: str) -> str:
        return f"""# Client Intake: {client_name}

**Date:** {datetime.now().strftime('%Y-%m-%d')}
**Session Type:** [ ] Espresso | [ ] Deep Dive | [ ] Data Rescue | [ ] Migration

## Emotional Check-In
- How are they doing? 
- Stress level: [ ] Chill | [ ] Stressed | [ ] Overwhelmed | [ ] Crisis

## Device Information
- **Device Type:** 
- **OS:** 
- **Problem Description:** 

## Critical Data
- [ ] Has critical data that can't be lost
- **What specifically:** 

## Initial Hypothesis
- 

## Sanctuary Setup
- **World:** 
- **Voice:** [ ] On | [ ] Off
- **Breath offered:** [ ] Yes | [ ] No

---
*NOIZYLAB - Calm in the Chaos*
"""
    
    def _get_report_template(self, client_name: str) -> str:
        return f"""# NOIZYLAB Care Summary

**Client:** {client_name}
**Date:** {datetime.now().strftime('%Y-%m-%d')}
**Session Type:** 

---

## You (Human Summary)

You came to NOIZYLAB feeling [emotional state] about your [device].

Our goals were:
- Reduce your anxiety
- Understand what's really going on
- Choose the smartest next step together

---

## Your Device (Tech Summary)

**What was happening:**


**What we found:**


---

## What We Did

- [ ] 
- [ ] 
- [ ] 

---

## What Should Feel Different Now

- 
- 

---

## My Honest Recommendation

If this were my machine, I would:

**Short term (1-3 months):**


**Medium term (3-12 months):**


---

## What to Watch For

Please reach out if you notice:
- 
- 

---

## Nervous System Care

We also cared for your nervous system during this session.

- **World used:** 
- **Voice:** On/Off
- **Approach:** 

---

*Whatever happens with this machine, your value doesn't change.*

*You're not "bad with computers." You're a human being whose life runs on them.*

*NOIZYLAB is here so you don't have to face this stuff alone.*

---

**Rob – NOIZYLAB / MC96 Mission Control**
"""
    
    def _get_invoice_template(self, client_name: str) -> str:
        return f"""# NOIZYLAB Invoice

**Invoice #:** NL-{datetime.now().strftime('%Y%m%d')}-001
**Date:** {datetime.now().strftime('%Y-%m-%d')}

---

**Bill To:**
{client_name}

---

## Services Rendered

| Service | Description | Amount |
|---------|-------------|--------|
|         |             | $      |

---

**Subtotal:** $
**Tax (if applicable):** $
**Total:** $

---

## Payment Methods

- **E-Transfer:** rsp@noizyfish.com
- **PayPal:** rsp@noizyfish.com

---

*Thank you for trusting NOIZYLAB with your tech.*

*Questions? Reply to this email or book a follow-up.*

---

**Fish Music Inc. / NOIZYLAB**
"""
    
    def get_shortcut_menu(self) -> Dict[str, Any]:
        """Get the shortcut menu for UI display."""
        return {
            "studio": {
                "title": "Studio",
                "shortcuts": [
                    {"name": s.name, "trigger": s.trigger, "description": s.description}
                    for s in self.get_by_category("studio")
                ]
            },
            "client": {
                "title": "Client",
                "shortcuts": [
                    {"name": s.name, "trigger": s.trigger, "description": s.description}
                    for s in self.get_by_category("client")
                ]
            },
            "flow": {
                "title": "Flow",
                "shortcuts": [
                    {"name": s.name, "trigger": s.trigger, "description": s.description}
                    for s in self.get_by_category("flow")
                ]
            },
            "sanctuary": {
                "title": "Sanctuary",
                "shortcuts": [
                    {"name": s.name, "trigger": s.trigger, "description": s.description}
                    for s in self.get_by_category("sanctuary")
                ]
            }
        }


# Singleton instance
_automation = None

def get_automation_engine() -> AutomationEngine:
    global _automation
    if _automation is None:
        _automation = AutomationEngine()
    return _automation

