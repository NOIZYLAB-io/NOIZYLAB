"""NoizyMemoryVault Brain - Full Pipeline"""
from .store import save_memory, load_all, load_memory
from .embed import embed_text
from .multimodal import embed_image, embed_audio, embed_video, embed_vr
from .index import add_to_index
from .graph import link

def store_text(text, meta=None):
    mem = {"type": "text", "text": text, "meta": meta or {}}
    mem_id = save_memory(mem)
    vec = embed_text(text)
    add_to_index(mem_id, vec)
    return mem_id

def store_image(data, meta=None):
    mem = {"type": "image", "size": len(data) if data else 0, "meta": meta or {}}
    mem_id = save_memory(mem)
    vec = embed_image(data)
    add_to_index(mem_id, vec)
    return mem_id

def store_audio(data, meta=None):
    mem = {"type": "audio", "size": len(data) if data else 0, "meta": meta or {}}
    mem_id = save_memory(mem)
    vec = embed_audio(data)
    add_to_index(mem_id, vec)
    return mem_id

def store_video(data, meta=None):
    mem = {"type": "video", "size": len(data) if data else 0, "meta": meta or {}}
    mem_id = save_memory(mem)
    vec = embed_video(data)
    add_to_index(mem_id, vec)
    return mem_id

def store_vr(meta):
    mem = {"type": "vr", "meta": meta}
    mem_id = save_memory(mem)
    vec = embed_vr(meta)
    add_to_index(mem_id, vec)
    return mem_id

def link_memories(a, b, relation="related"):
    link(a, b, relation)

