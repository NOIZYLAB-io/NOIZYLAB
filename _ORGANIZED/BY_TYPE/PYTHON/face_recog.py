"""
NoizyVision Face Recognition
============================
Face identification integrated with NoizyID.
"""

from typing import Dict, Optional, List
import numpy as np


def identify_face(embedding: np.ndarray) -> str:
    """
    Identify a face using NoizyID faceprint matching.
    """
    try:
        from ..noizyid.faceprint import match_faceprint
        from ..noizyid.store import IDENTITY_DB
    except ImportError:
        return "unknown"
    
    for ident_id, ident in IDENTITY_DB.items():
        if hasattr(ident, 'faceprint') and ident.faceprint is not None:
            if match_faceprint(ident.faceprint, embedding):
                return ident_id
    
    return "unknown"


def identify_faces(faces: List[Dict]) -> List[Dict]:
    """
    Identify all faces in a detection result.
    """
    identified = []
    
    for face in faces:
        embedding = face.get("embedding")
        if embedding is not None:
            face_id = identify_face(embedding)
        else:
            face_id = "unknown"
        
        identified.append({
            **face,
            "id": face_id,
        })
    
    return identified


def register_new_face(embedding: np.ndarray, name: str) -> Dict:
    """
    Register a new face in NoizyID.
    """
    try:
        from ..noizyid.faceprint import create_faceprint
        from ..noizyid.store import save_identity
        from ..noizyid.models import Identity
    except ImportError:
        return {"success": False, "error": "NoizyID not available"}
    
    faceprint = create_faceprint(embedding)
    
    identity = Identity(
        name=name,
        role="user",
        faceprint=faceprint,
    )
    
    save_identity(identity)
    
    return {"success": True, "identity_id": identity.id}


def get_known_faces() -> List[str]:
    """
    Get list of known face IDs.
    """
    try:
        from ..noizyid.store import IDENTITY_DB
    except ImportError:
        return []
    
    return [
        ident_id for ident_id, ident in IDENTITY_DB.items()
        if hasattr(ident, 'faceprint') and ident.faceprint is not None
    ]


def calculate_face_similarity(embedding1: np.ndarray, embedding2: np.ndarray) -> float:
    """
    Calculate similarity between two face embeddings.
    """
    try:
        dist = np.linalg.norm(np.array(embedding1) - np.array(embedding2))
        # Convert distance to similarity (0-1)
        similarity = max(0, 1 - (dist / 2))
        return similarity
    except Exception:
        return 0.0


def is_face_match(embedding1: np.ndarray, embedding2: np.ndarray, threshold: float = 0.6) -> bool:
    """
    Check if two face embeddings match.
    """
    similarity = calculate_face_similarity(embedding1, embedding2)
    return similarity >= threshold

