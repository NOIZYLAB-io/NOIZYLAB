"""NoizyMemoryVault Multimodal Encoders"""
from .embed import embed_text

def embed_image(data):
    return embed_text(f"IMAGE:{len(data) if data else 0}")

def embed_audio(data):
    return embed_text(f"AUDIO:{len(data) if data else 0}")

def embed_video(data):
    return embed_text(f"VIDEO:{len(data) if data else 0}")

def embed_vr(meta):
    name = meta.get("name", "unknown") if isinstance(meta, dict) else str(meta)
    return embed_text(f"VR:{name}")

def embed_document(text, doc_type):
    return embed_text(f"DOC:{doc_type}:{text[:500]}")

def embed_session(session_data):
    return embed_text(f"SESSION:{session_data.get('client', 'unknown')}:{session_data.get('summary', '')}")

