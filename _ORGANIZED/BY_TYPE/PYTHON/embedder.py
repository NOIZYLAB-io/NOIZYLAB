"""
NoizyDrive File Embedding Engine
================================
Understands the semantic meaning of files through embeddings.
Powers natural language file search and smart organization.
"""

from typing import List, Optional
import os
import hashlib
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    EMBEDDINGS_AVAILABLE = True
except ImportError:
    model = None
    EMBEDDINGS_AVAILABLE = False


# Embedding cache
EMBEDDING_CACHE = {}


def embed_file(path: str, content_preview: str = None) -> np.ndarray:
    """
    Generate semantic embedding for a file.
    
    Uses:
    - Filename
    - Extension
    - Path structure
    - Content preview (if provided)
    """
    # Check cache
    cache_key = hashlib.md5(path.encode()).hexdigest()
    if cache_key in EMBEDDING_CACHE:
        return EMBEDDING_CACHE[cache_key]
    
    # Build text representation
    filename = os.path.basename(path)
    dirname = os.path.dirname(path)
    ext = os.path.splitext(filename)[1]
    
    # Construct semantic text
    text_parts = [
        filename,
        f"extension: {ext}",
        f"folder: {dirname}",
    ]
    
    if content_preview:
        text_parts.append(f"content: {content_preview[:500]}")
    
    text = " | ".join(text_parts)
    
    # Generate embedding
    if EMBEDDINGS_AVAILABLE and model:
        embedding = model.encode([text])[0]
    else:
        # Fallback: hash-based pseudo-embedding
        h = hashlib.sha256(text.encode()).hexdigest()
        embedding = np.array([int(h[i:i+2], 16) / 255.0 for i in range(0, 64, 2)])
    
    # Cache it
    EMBEDDING_CACHE[cache_key] = embedding
    
    return embedding


def embed_query(query: str) -> np.ndarray:
    """
    Embed a search query for similarity matching.
    """
    if EMBEDDINGS_AVAILABLE and model:
        return model.encode([query])[0]
    else:
        h = hashlib.sha256(query.encode()).hexdigest()
        return np.array([int(h[i:i+2], 16) / 255.0 for i in range(0, 64, 2)])


def similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors.
    """
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    return float(np.dot(vec1, vec2) / (norm1 * norm2))


def search_by_embedding(
    query_vec: np.ndarray,
    file_embeddings: dict,
    top_k: int = 10
) -> List[tuple]:
    """
    Search files by embedding similarity.
    Returns list of (path, similarity_score) tuples.
    """
    results = []
    
    for path, vec in file_embeddings.items():
        if isinstance(vec, list):
            vec = np.array(vec)
        sim = similarity(query_vec, vec)
        results.append((path, sim))
    
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_k]


def clear_cache() -> int:
    """
    Clear embedding cache.
    Returns number of entries cleared.
    """
    count = len(EMBEDDING_CACHE)
    EMBEDDING_CACHE.clear()
    return count


def get_cache_stats() -> dict:
    """
    Get embedding cache statistics.
    """
    return {
        "entries": len(EMBEDDING_CACHE),
        "embeddings_available": EMBEDDINGS_AVAILABLE,
    }

