"""
═══════════════════════════════════════════════════════════════════════════════
THE NOIZYLAB WAR ROOM
═══════════════════════════════════════════════════════════════════════════════

Multi-agent consultation system where Geniuses work together behind the scenes.
One voice to the user. Many experts thinking.

This is NOT 25 skins. This is a REAL TEAM.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import asyncio

from .genius_registry import GENIUSES, find_genius_for_issue
from .genius_brain import GeniusBrain
from .doctrine import (
    SessionOutcome, 
    SafetyLevel, 
    get_safety_level,
    AuditTrail,
    DeviceProfile,
    ESCALATION_PATHS
)


@dataclass
class ConsultationNote:
    """A note from one genius to another during consultation"""
    from_genius: str
    to_genius: str
    message: str
    priority: str  # low, medium, high, critical
    timestamp: datetime
    

@dataclass
class WarRoomSession:
    """Active war room session with multiple geniuses consulting"""
    session_id: str
    device_profile: Optional[DeviceProfile]
    issue_description: str
    
    # The team
    lead_genius: str
    consulting_geniuses: List[str]
    
    # Consultation
    notes: List[ConsultationNote]
    consensus: Optional[Dict]
    
    # State
    status: str  # intake, diagnosing, consulting, resolving, complete
    confidence: float
    

class WarRoom:
    """
    The War Room — where Geniuses consult each other to solve complex issues.
    
    User sees ONE face. Behind the scenes, 5-10 experts are thinking.
    """
    
    def __init__(self):
        self.brain = GeniusBrain()
        self.active_sessions: Dict[str, WarRoomSession] = {}
        self.consultation_log: List[ConsultationNote] = []
    
    def open_session(
        self, 
        session_id: str, 
        issue: str, 
        device: Optional[DeviceProfile] = None
    ) -> WarRoomSession:
        """Open a new war room session for an issue"""
        
        # Analyze issue to find relevant geniuses
        analysis = self.brain.analyze_issue(issue)
        
        # Assemble the team
        lead = analysis["primary_genius"]["id"]
        team = [g["id"] for g in analysis["supporting_geniuses"]]
        
        # Always include certain geniuses for safety
        if "GENIUS_DATA" not in team and "GENIUS_DATA" != lead:
            team.append("GENIUS_DATA")  # Data safety always consulted
        if "GENIUS_SECURITY" not in team and "security" in issue.lower():
            team.append("GENIUS_SECURITY")
        
        session = WarRoomSession(
            session_id=session_id,
            device_profile=device,
            issue_description=issue,
            lead_genius=lead,
            consulting_geniuses=team[:5],  # Max 5 consulting
            notes=[],
            consensus=None,
            status="intake",
            confidence=analysis["primary_genius"]["confidence"]
        )
        
        self.active_sessions[session_id] = session
        
        # Initial consultation round
        self._run_consultation(session)
        
        return session
    
    def _run_consultation(self, session: WarRoomSession):
        """Run a consultation round between geniuses"""
        
        lead = GENIUSES[session.lead_genius]
        
        # Each consulting genius provides input
        for genius_id in session.consulting_geniuses:
            genius = GENIUSES.get(genius_id)
            if not genius:
                continue
            
            # Generate consultation note based on expertise
            note = self._generate_consultation(
                from_genius=genius,
                to_genius=lead,
                issue=session.issue_description,
                device=session.device_profile
            )
            
            session.notes.append(note)
        
        # Build consensus from notes
        session.consensus = self._build_consensus(session)
        session.status = "consulting"
    
    def _generate_consultation(
        self, 
        from_genius: Dict, 
        to_genius: Dict, 
        issue: str,
        device: Optional[DeviceProfile]
    ) -> ConsultationNote:
        """Generate a consultation note from one genius to another"""
        
        # Check if this genius's expertise is relevant
        issue_lower = issue.lower()
        relevance_score = 0
        relevant_expertise = []
        
        for expertise in from_genius["expertise"]:
            if any(word in expertise.lower() for word in issue_lower.split()):
                relevance_score += 1
                relevant_expertise.append(expertise)
        
        for specialty in from_genius["repair_specialties"]:
            if any(word in specialty.lower() for word in issue_lower.split()):
                relevance_score += 2
                relevant_expertise.append(specialty)
        
        # Generate message based on relevance
        if relevance_score > 3:
            priority = "high"
            message = f"I have direct experience with this. Check: {', '.join(relevant_expertise[:3])}"
        elif relevance_score > 0:
            priority = "medium"
            message = f"Possibly related to my domain. Consider: {', '.join(relevant_expertise[:2])}"
        else:
            priority = "low"
            message = f"Not my primary domain, but watch for {from_genius['repair_specialties'][0]}"
        
        # Add device-specific insights if available
        if device and device.past_issues:
            for past in device.past_issues[-3:]:
                if any(word in past["issue"].lower() for word in from_genius["domain"].lower().split()):
                    message += f" | Note: Previous {past['issue']} on this device."
                    priority = "high"
        
        return ConsultationNote(
            from_genius=from_genius["id"],
            to_genius=to_genius["id"],
            message=message,
            priority=priority,
            timestamp=datetime.now()
        )
    
    def _build_consensus(self, session: WarRoomSession) -> Dict:
        """Build consensus from all consultation notes"""
        
        high_priority = [n for n in session.notes if n.priority == "high"]
        medium_priority = [n for n in session.notes if n.priority == "medium"]
        
        # Calculate confidence based on agreement
        if len(high_priority) >= 2:
            confidence = 0.9
            consensus_level = "strong"
        elif len(high_priority) == 1:
            confidence = 0.75
            consensus_level = "moderate"
        elif len(medium_priority) >= 2:
            confidence = 0.6
            consensus_level = "tentative"
        else:
            confidence = 0.4
            consensus_level = "uncertain"
        
        # Extract key points
        key_points = []
        for note in high_priority + medium_priority[:2]:
            key_points.append({
                "from": GENIUSES[note.from_genius]["name"],
                "insight": note.message
            })
        
        return {
            "consensus_level": consensus_level,
            "confidence": confidence,
            "lead_genius": GENIUSES[session.lead_genius]["name"],
            "team_size": len(session.consulting_geniuses) + 1,
            "key_insights": key_points,
            "high_priority_count": len(high_priority),
            "recommendation": self._generate_recommendation(session, high_priority)
        }
    
    def _generate_recommendation(
        self, 
        session: WarRoomSession, 
        high_priority_notes: List[ConsultationNote]
    ) -> str:
        """Generate unified recommendation from war room"""
        
        lead = GENIUSES[session.lead_genius]
        
        if len(high_priority_notes) >= 2:
            return f"Multiple experts agree this is a {lead['domain']} issue. Proceeding with high confidence."
        elif len(high_priority_notes) == 1:
            contributor = GENIUSES[high_priority_notes[0].from_genius]
            return f"Primary diagnosis: {lead['domain']}. {contributor['name']} has additional insights."
        else:
            return f"Initial assessment points to {lead['domain']}, but more diagnostics needed."
    
    def get_unified_response(self, session_id: str) -> Dict:
        """Get the unified response for the user (one voice)"""
        
        session = self.active_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        lead = GENIUSES[session.lead_genius]
        
        return {
            "speaking_as": lead["name"],
            "symbol": lead["symbol"],
            "message": session.consensus["recommendation"],
            "confidence": f"{session.consensus['confidence'] * 100:.0f}%",
            "team_consulted": session.consensus["team_size"],
            "key_insights": session.consensus["key_insights"],
            
            # Hidden from user but available for transparency
            "_war_room": {
                "lead": session.lead_genius,
                "team": session.consulting_geniuses,
                "notes_count": len(session.notes),
                "consensus_level": session.consensus["consensus_level"]
            }
        }
    
    def request_second_opinion(self, session_id: str, genius_id: str) -> Dict:
        """Explicitly request input from a specific genius"""
        
        session = self.active_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        genius = GENIUSES.get(genius_id)
        if not genius:
            return {"error": f"Genius {genius_id} not found"}
        
        # Add to consulting team if not already
        if genius_id not in session.consulting_geniuses:
            session.consulting_geniuses.append(genius_id)
        
        # Generate specific consultation
        lead = GENIUSES[session.lead_genius]
        note = self._generate_consultation(
            from_genius=genius,
            to_genius=lead,
            issue=session.issue_description,
            device=session.device_profile
        )
        
        session.notes.append(note)
        
        # Rebuild consensus
        session.consensus = self._build_consensus(session)
        
        return {
            "genius": genius["name"],
            "symbol": genius["symbol"],
            "input": note.message,
            "priority": note.priority,
            "updated_consensus": session.consensus
        }
    
    def escalate_issue(self, session_id: str, reason: str) -> Dict:
        """Escalate when war room can't resolve"""
        
        session = self.active_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        session.status = "escalated"
        
        # Determine best escalation path
        issue_lower = session.issue_description.lower()
        
        if "board" in issue_lower or "logic" in issue_lower:
            path = ESCALATION_PATHS["board_repair"]
        elif "data" in issue_lower and "recover" in issue_lower:
            path = ESCALATION_PATHS["data_recovery_pro"]
        elif "warranty" in issue_lower:
            path = ESCALATION_PATHS["manufacturer_rma"]
        else:
            path = ESCALATION_PATHS["local_shop"]
        
        return {
            "outcome": "escalated",
            "reason": reason,
            "war_room_tried": {
                "lead": GENIUSES[session.lead_genius]["name"],
                "team_size": len(session.consulting_geniuses) + 1,
                "confidence_reached": session.consensus["confidence"]
            },
            "escalation_path": path,
            "message": f"The war room has done what it can. {path['description']}. {path['name']} is your best next step."
        }
    
    def close_session(self, session_id: str, outcome: SessionOutcome) -> Dict:
        """Close a war room session with outcome"""
        
        session = self.active_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        session.status = "complete"
        
        summary = {
            "session_id": session_id,
            "outcome": outcome.value,
            "lead_genius": GENIUSES[session.lead_genius]["name"],
            "team_consulted": [GENIUSES[g]["name"] for g in session.consulting_geniuses],
            "total_consultations": len(session.notes),
            "final_confidence": session.consensus["confidence"],
            "consensus_level": session.consensus["consensus_level"]
        }
        
        # Archive session
        del self.active_sessions[session_id]
        
        return summary


# Singleton instance
war_room = WarRoom()


def open_case(session_id: str, issue: str, device: DeviceProfile = None):
    """Quick function to open a war room case"""
    return war_room.open_session(session_id, issue, device)


def get_response(session_id: str):
    """Quick function to get unified response"""
    return war_room.get_unified_response(session_id)


def second_opinion(session_id: str, genius_id: str):
    """Quick function to request second opinion"""
    return war_room.request_second_opinion(session_id, genius_id)


def escalate(session_id: str, reason: str):
    """Quick function to escalate"""
    return war_room.escalate_issue(session_id, reason)

