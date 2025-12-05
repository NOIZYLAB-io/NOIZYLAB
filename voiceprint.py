"""
NoizyID Voice Biometric Recognition
===================================
Voice-based identity verification using audio features.
"""

from typing import List, Optional, Dict
import numpy as np
from datetime import datetime


# Voiceprint database
VOICEPRINT_DB: Dict[str, Dict] = {}

# Match threshold
VOICE_MATCH_THRESHOLD = 0.85


def create_voiceprint(identity_id: str, features: List[float]) -> Dict:
    """
    Create a voiceprint from audio features.
    
    Features should be mel-spectrogram or MFCC coefficients.
    """
    voiceprint = {
        "identity_id": identity_id,
        "features": features,
        "created": datetime.now().isoformat(),
        "samples": 1,
    }
    
    VOICEPRINT_DB[identity_id] = voiceprint
    return voiceprint


def update_voiceprint(identity_id: str, new_features: List[float]) -> Optional[Dict]:
    """
    Update voiceprint with new sample (adaptive learning).
    """
    existing = VOICEPRINT_DB.get(identity_id)
    if not existing:
        return create_voiceprint(identity_id, new_features)
    
    # Rolling average for adaptive learning
    old_features = np.array(existing["features"])
    new_features = np.array(new_features)
    
    samples = existing["samples"]
    alpha = 1 / (samples + 1)  # Decreasing learning rate
    
    updated = old_features * (1 - alpha) + new_features * alpha
    
    existing["features"] = updated.tolist()
    existing["samples"] += 1
    existing["last_updated"] = datetime.now().isoformat()
    
    return existing


def match_voiceprint(identity_id: str, test_features: List[float]) -> Dict:
    """
    Match test features against stored voiceprint.
    """
    stored = VOICEPRINT_DB.get(identity_id)
    if not stored:
        return {"match": False, "error": "No voiceprint found"}
    
    stored_vec = np.array(stored["features"])
    test_vec = np.array(test_features)
    
    # Ensure same dimensions
    min_len = min(len(stored_vec), len(test_vec))
    stored_vec = stored_vec[:min_len]
    test_vec = test_vec[:min_len]
    
    # Cosine similarity
    norm_stored = np.linalg.norm(stored_vec)
    norm_test = np.linalg.norm(test_vec)
    
    if norm_stored == 0 or norm_test == 0:
        return {"match": False, "score": 0, "error": "Invalid features"}
    
    score = float(np.dot(stored_vec, test_vec) / (norm_stored * norm_test))
    
    return {
        "match": score > VOICE_MATCH_THRESHOLD,
        "score": round(score, 4),
        "threshold": VOICE_MATCH_THRESHOLD,
        "identity_id": identity_id,
    }


def identify_by_voice(test_features: List[float], candidates: List[str] = None) -> Optional[Dict]:
    """
    Identify a person by voice from all stored voiceprints.
    """
    if candidates is None:
        candidates = list(VOICEPRINT_DB.keys())
    
    best_match = None
    best_score = 0
    
    for identity_id in candidates:
        result = match_voiceprint(identity_id, test_features)
        if result.get("score", 0) > best_score:
            best_score = result["score"]
            best_match = identity_id
    
    if best_score > VOICE_MATCH_THRESHOLD:
        return {
            "identified": True,
            "identity_id": best_match,
            "score": best_score,
            "confidence": "high" if best_score > 0.95 else "medium",
        }
    
    return {
        "identified": False,
        "best_match": best_match,
        "best_score": best_score,
    }


def delete_voiceprint(identity_id: str) -> bool:
    """
    Delete a voiceprint.
    """
    if identity_id in VOICEPRINT_DB:
        del VOICEPRINT_DB[identity_id]
        return True
    return False


def get_voiceprint_stats() -> Dict:
    """
    Get voiceprint statistics.
    """
    return {
        "total_voiceprints": len(VOICEPRINT_DB),
        "avg_samples": sum(v["samples"] for v in VOICEPRINT_DB.values()) / max(1, len(VOICEPRINT_DB)),
    }

