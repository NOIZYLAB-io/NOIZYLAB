"""
NOIZYLAB SOVEREIGN SANCTUARY - CORE SYSTEMS
============================================

The unified command center for AI-powered repair operations,
voice synthesis, biometric authentication, and legacy preservation.

Components:
- SovereignKernel: Master orchestrator
- NoizyVoxEngine: Voice synthesis and cloning
- ManifestGenerator: PDF success manifest generation
- AuraPulse: Biometric authentication
- GhostVision: Predictive stabilization
- SecondLifeEngine: Analog gear preservation

GORUNFREE.
"""

from .sovereign_kernel import (
    SovereignKernel,
    SovereignConfig,
    AuthState,
    BiometricProfile,
    AuraPulse,
    GhostVision,
    SecondLifeEngine,
    SovereignHUD,
)

from .noizyvox_engine import (
    NoizyVoxEngine,
    VoiceProvider,
    EmotionalMode,
    NoizyVoxVoice,
    NOIZYVOX_ROSTER,
    EMOTIONAL_SETTINGS,
)

__all__ = [
    # Kernel
    "SovereignKernel",
    "SovereignConfig",
    "AuthState",
    "BiometricProfile",

    # Subsystems
    "AuraPulse",
    "GhostVision",
    "SecondLifeEngine",
    "SovereignHUD",

    # Voice
    "NoizyVoxEngine",
    "VoiceProvider",
    "EmotionalMode",
    "NoizyVoxVoice",
    "NOIZYVOX_ROSTER",
    "EMOTIONAL_SETTINGS",
]

__version__ = "2.0.0"
__author__ = "NOIZYLAB"
__signature__ = "GORUNFREE"
