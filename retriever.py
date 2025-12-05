"""NoizyMemoryVault Semantic Retriever"""
from .index import INDEX

def similarity(a, b):
    if len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = sum(x * x for x in a) ** 0.5
    mag_b = sum(x * x for x in b) ** 0.5
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)

def retrieve(query_vec, top=5):
    scored = [(m["id"], similarity(query_vec, m["vec"])) for m in INDEX]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top]

def retrieve_above_threshold(query_vec, threshold=0.7):
    scored = [(m["id"], similarity(query_vec, m["vec"])) for m in INDEX]
    return [(id, score) for id, score in scored if score >= threshold]

