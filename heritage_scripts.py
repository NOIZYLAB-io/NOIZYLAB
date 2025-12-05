# ROB OS - HERITAGE SCRIPTS
# ==========================
# Voice preservation and family legacy recording
# "Voices that never vanish"

from typing import Dict, Any, List
from dataclasses import dataclass, field

@dataclass
class HeritageSection:
    """A section of the Heritage interview script."""
    id: str
    title: str
    purpose: str
    prompts: List[str]
    duration_estimate: str
    notes: str = ""

# ============================================
# HERITAGE INTERVIEW SCRIPT v1
# ============================================

HERITAGE_INTERVIEW_SCRIPT = {
    "title": "Heritage Voice Recording Session",
    "version": "1.0",
    "total_duration": "90-120 minutes",
    "purpose": "Capture voice, stories, and messages for future generations",
    
    "sections": [
        HeritageSection(
            id="warmup",
            title="Section A: Warm-Up & Voice Quality",
            purpose="Get comfortable and capture clean voice samples for AI training",
            prompts=[
                "Tell me your full name and where you were born.",
                "What's your favorite meal? Describe it like you're telling a friend about it.",
                "Count from 1 to 20, nice and slow.",
                "Read this paragraph: [provide neutral text with varied phonemes]",
                "Say these phrases naturally: 'Hello, how are you?', 'I love you', 'Everything will be okay', 'I'm so proud of you'",
                "Laugh naturally - think of something funny that happened recently.",
                "Hum a tune you love."
            ],
            duration_estimate="15-20 minutes",
            notes="This section captures the technical voice samples needed for AI training."
        ),
        
        HeritageSection(
            id="family_tree",
            title="Section B: Family Tree & History",
            purpose="Document family history and connections",
            prompts=[
                "Tell me about your parents. What were their names? What do you remember most about them?",
                "Did you have siblings? What was your relationship like?",
                "What was your childhood home like? Describe it to me.",
                "What was the neighborhood like where you grew up?",
                "What did your parents do for work?",
                "What traditions did your family have?",
                "Is there a family recipe that's been passed down?",
                "What's a story about your grandparents that you want remembered?",
                "How did you meet your spouse/partner?",
                "Tell me about your children. What makes each of them special?",
                "What do you hope your grandchildren will remember about you?"
            ],
            duration_estimate="30-40 minutes",
            notes="Let them ramble. The stories between the questions are often the gold."
        ),
        
        HeritageSection(
            id="life_lessons",
            title="Section C: Life Lessons & Wisdom",
            purpose="Capture hard-won wisdom and advice",
            prompts=[
                "What's the best advice you ever received?",
                "What's the hardest thing you've ever been through, and what did it teach you?",
                "If you could go back and tell your 20-year-old self one thing, what would it be?",
                "What do you wish more people understood about life?",
                "What's something you're proud of that not many people know about?",
                "What mistake taught you the most?",
                "What do you believe about love?",
                "What do you believe about work?",
                "What do you believe about family?",
                "What brings you peace?"
            ],
            duration_estimate="20-30 minutes",
            notes="These answers become the 'voice of wisdom' for future generations."
        ),
        
        HeritageSection(
            id="messages",
            title="Section D: Messages to Future Generations",
            purpose="Direct messages to specific people or future descendants",
            prompts=[
                "Is there a message you want to leave for your children?",
                "Is there a message you want to leave for your grandchildren?",
                "Is there a message for someone who hasn't been born yet?",
                "If someone in the family is going through a hard time, what would you want to tell them?",
                "If someone in the family is celebrating something wonderful, what would you want to say?",
                "What do you want people to remember about you?",
                "Is there anything you've never said that you want to say now?",
                "How do you want to be remembered?"
            ],
            duration_estimate="15-20 minutes",
            notes="These are the most precious recordings. Give them time and space."
        ),
        
        HeritageSection(
            id="closing",
            title="Section E: Closing & Free Expression",
            purpose="Capture anything else and end with love",
            prompts=[
                "Is there anything else you want to say that we haven't covered?",
                "Is there a song you'd like to sing or hum?",
                "Is there a poem or prayer that's meaningful to you?",
                "Say 'I love you' to whoever might be listening in the future.",
                "Any final words?"
            ],
            duration_estimate="10-15 minutes",
            notes="End with love. Always end with love."
        )
    ],
    
    "technical_notes": {
        "recording_format": "WAV, 48kHz, 24-bit",
        "microphone": "Best available, positioned 15-20cm from speaker",
        "environment": "Quiet room, minimal echo",
        "backup": "Record to two devices simultaneously if possible",
        "session_breaks": "Offer breaks every 30 minutes - hydration, rest"
    },
    
    "ethical_notes": {
        "consent": "Explicit written consent required before recording",
        "ownership": "Family owns all recordings and any AI models",
        "usage_restrictions": "Voice cannot be used for commercial purposes without family consent",
        "storage": "Encrypted storage with family-controlled access",
        "ai_training": "Optional - family decides if voice model is created"
    }
}


class HeritageScriptManager:
    """
    Manages Heritage interview scripts and sessions.
    """
    
    def __init__(self):
        self.script = HERITAGE_INTERVIEW_SCRIPT
    
    def get_full_script(self) -> Dict[str, Any]:
        """Get the complete Heritage interview script."""
        return self.script
    
    def get_section(self, section_id: str) -> HeritageSection:
        """Get a specific section of the script."""
        for section in self.script["sections"]:
            if section.id == section_id:
                return section
        return None
    
    def get_all_sections(self) -> List[HeritageSection]:
        """Get all sections."""
        return self.script["sections"]
    
    def get_session_checklist(self) -> Dict[str, Any]:
        """Get a pre-session checklist."""
        return {
            "before_session": [
                "☐ Written consent form signed",
                "☐ Recording equipment tested",
                "☐ Quiet room prepared",
                "☐ Water and tissues available",
                "☐ Backup recording device ready",
                "☐ Family photos available (for memory prompts)",
                "☐ 2-3 hours blocked with no interruptions"
            ],
            "during_session": [
                "☐ Start with warm-up section",
                "☐ Let them ramble - don't rush",
                "☐ Offer breaks every 30 minutes",
                "☐ Watch for fatigue",
                "☐ Note timestamps for key moments"
            ],
            "after_session": [
                "☐ Backup all recordings immediately",
                "☐ Label files clearly with date and section",
                "☐ Send thank you note",
                "☐ Schedule follow-up if needed",
                "☐ Begin transcription process"
            ]
        }
    
    def get_consent_template(self) -> str:
        """Get the consent form template."""
        return """
# HERITAGE VOICE RECORDING CONSENT FORM

**Date:** _______________

**Participant Name:** _______________

## Purpose
This recording session is being conducted to preserve your voice, stories, and messages for your family and future generations.

## What Will Happen
- We will record your voice answering questions about your life, family, and wisdom
- The session will last approximately 90-120 minutes with breaks
- All recordings will be made in high quality audio format

## Ownership & Rights
- You and your designated family members own all recordings
- Recordings will not be shared publicly without your written consent
- You may request deletion of any or all recordings at any time

## Optional: AI Voice Model
- [ ] I consent to my voice being used to train an AI voice model
- [ ] I do NOT consent to AI voice model training

If you consent to AI training:
- The voice model will be owned by your designated family members
- The voice model cannot be used for commercial purposes
- The voice model cannot be used to say things you would not have said

## Signature

I have read and understood this consent form.

**Signature:** _______________

**Date:** _______________

**Witness:** _______________
"""
    
    def get_service_pitch(self) -> Dict[str, Any]:
        """Get the Heritage service pitch."""
        return {
            "headline": "Heritage Voice Recording Session",
            "tagline": "Preserve the voices that matter.",
            "description": """
            Some voices are too precious to lose to time.
            
            A Heritage session captures not just words, but the way someone laughs,
            the pauses they take when they're thinking, the warmth in their voice
            when they say 'I love you.'
            
            We guide your loved one through a gentle, structured conversation
            that captures their stories, wisdom, and messages for future generations.
            
            Optional: We can prepare their voice for AI preservation,
            so future family members can hear their voice say new things -
            birthday wishes, words of comfort, messages they couldn't have known
            they'd need to leave.
            """,
            "includes": [
                "Guided 2-hour recording session",
                "Family tree and history capture",
                "Life lessons and wisdom",
                "Messages to future generations",
                "High-quality audio archive",
                "Full transcription",
                "Optional: AI voice model preparation"
            ],
            "price": "$499 (Standard) / $2,999 (with AI Voice Model)",
            "who_its_for": [
                "Families wanting to preserve elder voices",
                "Anyone facing end-of-life situations",
                "People who value legacy",
                "Families with aging parents",
                "Anyone who's ever wished they had more recordings of someone they lost"
            ]
        }


# Singleton instance
_heritage = None

def get_heritage_manager() -> HeritageScriptManager:
    global _heritage
    if _heritage is None:
        _heritage = HeritageScriptManager()
    return _heritage

