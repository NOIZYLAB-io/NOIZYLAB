# ROB OS - LAYER 3: ADAPTIVE CALM ENGINE
# ========================================
# Drift + Tide - Automatic sanctuary adjustment
# Learns what calms each person and adapts in real-time

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from .state_detector import EmotionalState, get_state_detector

@dataclass
class CalmSession:
    """Tracks a single calming session."""
    session_id: str
    user_id: str
    start_state: EmotionalState
    world_used: str
    initial_levels: Dict[str, int]  # music, ambience, voice
    
    # Adjustments made during session
    adjustments: List[Dict[str, Any]] = field(default_factory=list)
    
    # Outcome
    end_state: Optional[EmotionalState] = None
    user_feedback: Optional[str] = None  # "helped", "neutral", "too_much"
    duration_seconds: int = 0

@dataclass
class UserCalmProfile:
    """Learned calm preferences for a user."""
    user_id: str
    
    # Preferred worlds by state
    preferred_worlds: Dict[str, str] = field(default_factory=dict)
    
    # Preferred levels
    preferred_music_level: int = 40
    preferred_ambience_level: int = 60
    preferred_voice_level: int = 30
    
    # What works
    responds_to_breath: bool = True
    responds_to_asmr: bool = False
    responds_to_binaural: bool = False
    
    # What doesn't work / to avoid
    avoid_sounds: List[str] = field(default_factory=list)
    avoid_worlds: List[str] = field(default_factory=list)
    
    # Session history for learning
    session_count: int = 0
    successful_sessions: int = 0


class AdaptiveCalmEngine:
    """
    Drift + Tide - The adaptive calming engine.
    Learns what works for each person and adjusts in real-time.
    """
    
    def __init__(self):
        self.state_detector = get_state_detector()
        self.user_profiles: Dict[str, UserCalmProfile] = {}
        self.active_sessions: Dict[str, CalmSession] = {}
        
        # Default calm strategies by state
        self.calm_strategies = {
            EmotionalState.CRISIS: {
                "approach": "minimal_input",
                "start_world": "rain_on_the_roof",
                "music_level": 25,
                "ambience_level": 70,
                "voice_level": 40,
                "offer_breath": True,
                "breath_duration": 30,
                "message_length": "very_short",
                "pause_between_messages": 5  # seconds
            },
            EmotionalState.OVERLOADED: {
                "approach": "near_silence",
                "start_world": "silent_shore",
                "music_level": 0,
                "ambience_level": 15,
                "voice_level": 0,
                "offer_breath": False,  # Even breath might be too much
                "message_length": "minimal",
                "pause_between_messages": 8
            },
            EmotionalState.STRESSED: {
                "approach": "gentle_presence",
                "start_world": "fish_forest",
                "music_level": 35,
                "ambience_level": 65,
                "voice_level": 30,
                "offer_breath": True,
                "breath_duration": 20,
                "message_length": "short",
                "pause_between_messages": 3
            },
            EmotionalState.BURNED_OUT: {
                "approach": "nurturing_rest",
                "start_world": "soft_tide",
                "music_level": 50,
                "ambience_level": 50,
                "voice_level": 25,
                "offer_breath": True,
                "breath_duration": 20,
                "message_length": "short",
                "pause_between_messages": 4
            },
            EmotionalState.CHILL: {
                "approach": "light_background",
                "start_world": "mc96_midnight",
                "music_level": 45,
                "ambience_level": 35,
                "voice_level": 20,
                "offer_breath": False,
                "message_length": "normal",
                "pause_between_messages": 1
            }
        }
    
    def start_calm_session(self, user_id: str, initial_state: EmotionalState,
                           session_id: str) -> Dict[str, Any]:
        """
        Start a calming session for a user.
        Returns the recommended initial setup.
        """
        # Get or create user profile
        profile = self.user_profiles.get(user_id)
        if not profile:
            profile = UserCalmProfile(user_id=user_id)
            self.user_profiles[user_id] = profile
        
        # Get base strategy for this state
        strategy = self.calm_strategies.get(
            initial_state, 
            self.calm_strategies[EmotionalState.STRESSED]
        )
        
        # Personalize based on user profile
        world = profile.preferred_worlds.get(
            initial_state.value, 
            strategy["start_world"]
        )
        
        music_level = profile.preferred_music_level if profile.session_count > 3 else strategy["music_level"]
        ambience_level = profile.preferred_ambience_level if profile.session_count > 3 else strategy["ambience_level"]
        voice_level = profile.preferred_voice_level if profile.session_count > 3 else strategy["voice_level"]
        
        # Create session record
        session = CalmSession(
            session_id=session_id,
            user_id=user_id,
            start_state=initial_state,
            world_used=world,
            initial_levels={"music": music_level, "ambience": ambience_level, "voice": voice_level}
        )
        self.active_sessions[session_id] = session
        
        return {
            "session_id": session_id,
            "world": world,
            "levels": {
                "music": music_level,
                "ambience": ambience_level,
                "voice": voice_level
            },
            "offer_breath": strategy["offer_breath"] and profile.responds_to_breath,
            "breath_duration": strategy.get("breath_duration", 20),
            "message_settings": {
                "length": strategy["message_length"],
                "pause_between": strategy["pause_between_messages"]
            },
            "personalized": profile.session_count > 3
        }
    
    def record_adjustment(self, session_id: str, adjustment_type: str,
                          old_value: Any, new_value: Any) -> None:
        """Record an adjustment made during a session."""
        session = self.active_sessions.get(session_id)
        if session:
            session.adjustments.append({
                "type": adjustment_type,
                "old": old_value,
                "new": new_value
            })
    
    def end_calm_session(self, session_id: str, end_state: EmotionalState,
                         user_feedback: str = None, duration: int = 0) -> Dict[str, Any]:
        """
        End a calming session and learn from it.
        """
        session = self.active_sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        session.end_state = end_state
        session.user_feedback = user_feedback
        session.duration_seconds = duration
        
        # Learn from this session
        profile = self.user_profiles.get(session.user_id)
        if profile:
            profile.session_count += 1
            
            # Determine if session was successful
            state_improved = self._state_improved(session.start_state, end_state)
            positive_feedback = user_feedback in ["helped", "good", "better"]
            
            if state_improved or positive_feedback:
                profile.successful_sessions += 1
                
                # Learn preferred world for this state
                profile.preferred_worlds[session.start_state.value] = session.world_used
                
                # Learn preferred levels (weighted average)
                final_levels = session.initial_levels.copy()
                for adj in session.adjustments:
                    if adj["type"] in ["music", "ambience", "voice"]:
                        final_levels[adj["type"]] = adj["new"]
                
                # Update preferences with 20% weight to new data
                weight = 0.2
                profile.preferred_music_level = int(
                    profile.preferred_music_level * (1 - weight) + 
                    final_levels.get("music", profile.preferred_music_level) * weight
                )
                profile.preferred_ambience_level = int(
                    profile.preferred_ambience_level * (1 - weight) + 
                    final_levels.get("ambience", profile.preferred_ambience_level) * weight
                )
                profile.preferred_voice_level = int(
                    profile.preferred_voice_level * (1 - weight) + 
                    final_levels.get("voice", profile.preferred_voice_level) * weight
                )
        
        # Clean up
        del self.active_sessions[session_id]
        
        return {
            "session_id": session_id,
            "start_state": session.start_state.value,
            "end_state": end_state.value,
            "improved": self._state_improved(session.start_state, end_state),
            "duration": duration,
            "adjustments_made": len(session.adjustments)
        }
    
    def _state_improved(self, start: EmotionalState, end: EmotionalState) -> bool:
        """Check if emotional state improved."""
        state_order = [
            EmotionalState.CRISIS,
            EmotionalState.OVERLOADED,
            EmotionalState.STRESSED,
            EmotionalState.BURNED_OUT,
            EmotionalState.CHILL,
            EmotionalState.CURIOUS
        ]
        
        start_idx = state_order.index(start) if start in state_order else 2
        end_idx = state_order.index(end) if end in state_order else 2
        
        return end_idx > start_idx
    
    def get_breath_script(self, duration_seconds: int = 20) -> Dict[str, Any]:
        """
        Get the NOIZY Breath script for guided breathing.
        """
        if duration_seconds <= 20:
            return {
                "type": "short_breath",
                "duration": 20,
                "script": [
                    {"time": 0, "text": "Let's take one breath together.", "voice": "sanctuary"},
                    {"time": 3, "text": "Breathe in slowly...", "voice": "sanctuary"},
                    {"time": 8, "text": "Hold gently...", "voice": "sanctuary"},
                    {"time": 11, "text": "And let it go...", "voice": "sanctuary"},
                    {"time": 17, "text": "That's it. You're here.", "voice": "sanctuary"}
                ]
            }
        else:
            return {
                "type": "extended_breath",
                "duration": 30,
                "script": [
                    {"time": 0, "text": "Let's slow everything down for a moment.", "voice": "sanctuary"},
                    {"time": 4, "text": "Breathe in slowly... 2... 3... 4...", "voice": "sanctuary"},
                    {"time": 10, "text": "Hold gently... 2... 3...", "voice": "sanctuary"},
                    {"time": 14, "text": "And let it all go... 2... 3... 4... 5...", "voice": "sanctuary"},
                    {"time": 21, "text": "One more time. In...", "voice": "sanctuary"},
                    {"time": 25, "text": "And out...", "voice": "sanctuary"},
                    {"time": 29, "text": "You're here. You're okay.", "voice": "sanctuary"}
                ]
            }
    
    def get_user_profile(self, user_id: str) -> Optional[UserCalmProfile]:
        """Get a user's calm profile."""
        return self.user_profiles.get(user_id)


# Singleton instance
_adaptive_calm = None

def get_adaptive_calm() -> AdaptiveCalmEngine:
    global _adaptive_calm
    if _adaptive_calm is None:
        _adaptive_calm = AdaptiveCalmEngine()
    return _adaptive_calm

