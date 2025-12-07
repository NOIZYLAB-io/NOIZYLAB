# ROB OS - CLIENT SESSION WIZARD
# ===============================
# The complete pipeline for any new human
# From arrival to wrap-up

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

class SessionType(Enum):
    ESPRESSO = "espresso"       # Quick tune-up
    DEEP_DIVE = "deep_dive"     # Full repair session
    DATA_RESCUE = "data_rescue" # Data-first emergency
    MIGRATION = "migration"     # Old to new machine
    SANCTUARY_ONLY = "sanctuary_only"  # Just calm, no tech

class SessionPhase(Enum):
    ARRIVAL = "arrival"
    EMOTIONAL_CHECK = "emotional_check"
    SANCTUARY_SETUP = "sanctuary_setup"
    DEVICE_INTAKE = "device_intake"
    READBACK = "readback"
    SESSION_TYPE_SELECT = "session_type_select"
    CONFIRMATION = "confirmation"
    EXECUTION = "execution"
    WRAP_UP = "wrap_up"
    FOLLOW_UP = "follow_up"

@dataclass
class ClientSession:
    """A complete client session record."""
    session_id: str
    client_name: str
    started_at: str
    
    # Emotional context
    initial_state: str  # "chill", "stressed", "crisis", "burned_out"
    sanctuary_used: bool = False
    world_used: Optional[str] = None
    voice_enabled: bool = True
    breath_offered: bool = False
    
    # Device info
    device_type: Optional[str] = None
    device_os: Optional[str] = None
    problem_description: Optional[str] = None
    critical_data: bool = False
    
    # Session
    session_type: Optional[SessionType] = None
    current_phase: SessionPhase = SessionPhase.ARRIVAL
    
    # Actions taken
    actions: List[Dict[str, Any]] = field(default_factory=list)
    
    # Outcome
    diagnosis: Optional[str] = None
    recommendations: List[str] = field(default_factory=list)
    completed_at: Optional[str] = None
    follow_up_scheduled: bool = False

@dataclass
class SessionAction:
    """A single action taken during a session."""
    timestamp: str
    action_type: str
    description: str
    result: str
    notes: str = ""

class ClientSessionWizard:
    """
    The complete client session pipeline.
    From first contact to wrap-up and follow-up.
    """
    
    def __init__(self):
        self.active_sessions: Dict[str, ClientSession] = {}
        self.completed_sessions: List[ClientSession] = []
    
    def start_session(self, client_name: str) -> ClientSession:
        """
        Start a new client session.
        """
        session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        session = ClientSession(
            session_id=session_id,
            client_name=client_name,
            started_at=datetime.now().isoformat(),
            initial_state="unknown"
        )
        
        self.active_sessions[session_id] = session
        return session
    
    def record_emotional_state(self, session_id: str, state: str) -> ClientSession:
        """
        Record the client's emotional state.
        """
        session = self.active_sessions.get(session_id)
        if session:
            session.initial_state = state
            session.current_phase = SessionPhase.EMOTIONAL_CHECK
            
            # Auto-offer sanctuary for stressed states
            if state in ["stressed", "crisis", "burned_out", "overloaded"]:
                session.sanctuary_used = True
        
        return session
    
    def setup_sanctuary(self, session_id: str, world: str, 
                        voice_enabled: bool, breath: bool) -> ClientSession:
        """
        Set up the sanctuary environment for the session.
        """
        session = self.active_sessions.get(session_id)
        if session:
            session.world_used = world
            session.voice_enabled = voice_enabled
            session.breath_offered = breath
            session.current_phase = SessionPhase.SANCTUARY_SETUP
        
        return session
    
    def record_device_info(self, session_id: str, device_type: str,
                           os: str, problem: str, critical_data: bool) -> ClientSession:
        """
        Record device information.
        """
        session = self.active_sessions.get(session_id)
        if session:
            session.device_type = device_type
            session.device_os = os
            session.problem_description = problem
            session.critical_data = critical_data
            session.current_phase = SessionPhase.DEVICE_INTAKE
        
        return session
    
    def generate_readback(self, session_id: str) -> Dict[str, Any]:
        """
        Generate the readback summary for the client.
        """
        session = self.active_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        # Generate hypothesis based on problem description
        hypothesis = self._generate_hypothesis(session)
        
        readback = {
            "device_summary": f"{session.device_type} running {session.device_os}",
            "symptom_summary": session.problem_description,
            "critical_data": "Yes - we'll be extra careful" if session.critical_data else "No critical data flagged",
            "hypothesis": hypothesis["diagnosis"],
            "confidence": hypothesis["confidence"],
            "risk_level": hypothesis["risk_level"],
            "voice_script": f"""Here's what I'm hearing:

You've got a {session.device_type} running {session.device_os}.
The main issue is: {session.problem_description}
{"You've got important data we need to protect." if session.critical_data else ""}

That sounds like it could be {hypothesis["diagnosis"]}.
Risk to your files: {hypothesis["risk_level"]}.

I'm about {hypothesis["confidence"]}% confident in that assessment,
but we'll know more once we dig in."""
        }
        
        session.diagnosis = hypothesis["diagnosis"]
        session.current_phase = SessionPhase.READBACK
        
        return readback
    
    def _generate_hypothesis(self, session: ClientSession) -> Dict[str, Any]:
        """
        Generate a hypothesis based on symptoms.
        """
        problem = (session.problem_description or "").lower()
        
        # Simple pattern matching for common issues
        if "slow" in problem:
            return {
                "diagnosis": "performance issues - likely startup bloat or background processes",
                "confidence": 70,
                "risk_level": "low"
            }
        elif "crash" in problem or "freeze" in problem:
            return {
                "diagnosis": "stability issues - could be software conflicts or early hardware warning",
                "confidence": 60,
                "risk_level": "medium"
            }
        elif "won't start" in problem or "boot" in problem:
            return {
                "diagnosis": "boot failure - could be OS corruption or drive issues",
                "confidence": 50,
                "risk_level": "high"
            }
        elif "lost" in problem or "deleted" in problem:
            return {
                "diagnosis": "data loss situation - need to assess recovery options",
                "confidence": 40,
                "risk_level": "high"
            }
        else:
            return {
                "diagnosis": "unknown issue - we'll need to investigate further",
                "confidence": 30,
                "risk_level": "unknown"
            }
    
    def select_session_type(self, session_id: str, 
                            session_type: SessionType) -> ClientSession:
        """
        Select the session type.
        """
        session = self.active_sessions.get(session_id)
        if session:
            session.session_type = session_type
            session.current_phase = SessionPhase.SESSION_TYPE_SELECT
        
        return session
    
    def get_session_plan(self, session_id: str) -> Dict[str, Any]:
        """
        Get the session plan based on selected type.
        """
        session = self.active_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        plans = {
            SessionType.ESPRESSO: {
                "name": "Espresso Tune-Up",
                "duration": "30-45 minutes",
                "actions": [
                    "Safe health check (drive, temps, basic OS)",
                    "Startup bloat cleanup",
                    "Background CPU-hogs identified",
                    "Safe junk/temp files cleared"
                ],
                "will_not": [
                    "Wipe drives or reinstall OS",
                    "Run anything that risks your files",
                    "Make changes without explaining first"
                ]
            },
            SessionType.DEEP_DIVE: {
                "name": "Deep Dive Repair",
                "duration": "2-3 hours",
                "actions": [
                    "Full diagnostic deep dive",
                    "System logs analysis",
                    "Drive health assessment",
                    "Software conflict investigation",
                    "Stability-first fixes"
                ],
                "will_not": [
                    "Format or wipe without explicit consent",
                    "Run risky scripts without sandbox testing",
                    "Rush to conclusions"
                ]
            },
            SessionType.DATA_RESCUE: {
                "name": "Data-First Rescue",
                "duration": "Variable",
                "actions": [
                    "Assess data risk level",
                    "Stop any actions that could worsen damage",
                    "Plan safest extraction path",
                    "Coordinate with recovery labs if needed"
                ],
                "will_not": [
                    "Touch the drive without a plan",
                    "Attempt risky recovery without consent",
                    "Give false hope about recovery chances"
                ]
            }
        }
        
        plan = plans.get(session.session_type, plans[SessionType.ESPRESSO])
        plan["session_id"] = session_id
        plan["client_name"] = session.client_name
        
        return plan
    
    def confirm_session(self, session_id: str) -> Dict[str, Any]:
        """
        Confirm and start the session.
        """
        session = self.active_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        session.current_phase = SessionPhase.EXECUTION
        
        return {
            "status": "confirmed",
            "message": "Session started. Let's take care of this together.",
            "session_id": session_id,
            "phase": "execution"
        }
    
    def record_action(self, session_id: str, action_type: str,
                      description: str, result: str, notes: str = "") -> ClientSession:
        """
        Record an action taken during the session.
        """
        session = self.active_sessions.get(session_id)
        if session:
            session.actions.append({
                "timestamp": datetime.now().isoformat(),
                "action_type": action_type,
                "description": description,
                "result": result,
                "notes": notes
            })
        
        return session
    
    def wrap_up_session(self, session_id: str, 
                        recommendations: List[str]) -> Dict[str, Any]:
        """
        Wrap up the session and generate summary.
        """
        session = self.active_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        session.recommendations = recommendations
        session.completed_at = datetime.now().isoformat()
        session.current_phase = SessionPhase.WRAP_UP
        
        # Generate wrap-up summary
        summary = {
            "session_id": session_id,
            "client_name": session.client_name,
            "duration": self._calculate_duration(session),
            "what_we_found": session.diagnosis,
            "what_we_did": [a["description"] for a in session.actions],
            "recommendations": recommendations,
            "voice_script": f"""Here's what we found:
{session.diagnosis}

Here's what we did:
{chr(10).join('- ' + a["description"] for a in session.actions[:3])}

My recommendations:
{chr(10).join('- ' + r for r in recommendations[:3])}

If this were my machine, I'd focus on that first recommendation.
But it's your call. What feels right?"""
        }
        
        # Move to completed
        self.completed_sessions.append(session)
        del self.active_sessions[session_id]
        
        return summary
    
    def _calculate_duration(self, session: ClientSession) -> str:
        """Calculate session duration."""
        if session.completed_at:
            start = datetime.fromisoformat(session.started_at)
            end = datetime.fromisoformat(session.completed_at)
            duration = end - start
            minutes = int(duration.total_seconds() / 60)
            return f"{minutes} minutes"
        return "ongoing"
    
    def generate_client_report(self, session_id: str) -> Dict[str, Any]:
        """
        Generate the client report (Miracle Receipt).
        """
        # Find session in completed
        session = next((s for s in self.completed_sessions if s.session_id == session_id), None)
        if not session:
            return {"error": "Session not found"}
        
        return {
            "title": f"NOIZYLAB Care Summary – {session.client_name}",
            "sections": {
                "human_summary": {
                    "title": "You",
                    "content": f"You came to NOIZYLAB feeling {session.initial_state} about your {session.device_type}. Our goals were to reduce your anxiety, understand what's really going on, and choose the smartest next step together."
                },
                "tech_summary": {
                    "title": "Your Device",
                    "what_was_happening": session.problem_description,
                    "what_we_found": session.diagnosis
                },
                "what_we_did": {
                    "title": "What We Did",
                    "actions": [a["description"] for a in session.actions]
                },
                "sanctuary_care": {
                    "title": "Nervous System Care",
                    "content": f"We used {session.world_used or 'a calm environment'} to give your brain a calmer background. We kept explanations in short, clear steps and checked in on your stress level."
                },
                "recommendations": {
                    "title": "My Honest Recommendation",
                    "content": session.recommendations
                },
                "closing": {
                    "content": "Whatever happens with this machine, your value doesn't change. You're not 'bad with computers.' You're a human being whose life runs on them. NOIZYLAB is here so you don't have to face this stuff alone."
                }
            },
            "signed": "Rob – NOIZYLAB / MC96 Mission Control"
        }


# Singleton instance
_session_wizard = None

def get_session_wizard() -> ClientSessionWizard:
    global _session_wizard
    if _session_wizard is None:
        _session_wizard = ClientSessionWizard()
    return _session_wizard

