#!/usr/bin/env python3
"""
Performance Optimizations - Caching and Async Operations
========================================================
"""

import functools
import time
from typing import Any, Callable
from rich.console import Console

console = Console()

class Cache:
    """Simple in-memory cache with TTL"""
    def __init__(self, ttl: int = 300):
        self.cache = {}
        self.ttl = ttl
    
    def get(self, key: str) -> Any:
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None
    
    def set(self, key: str, value: Any):
        self.cache[key] = (value, time.time())
    
    def clear(self):
        self.cache.clear()

# Global cache instance
cache = Cache(ttl=300)

def cached(ttl: int = 300):
    """Decorator for caching function results"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key from function name and arguments
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # Check cache
            cached_result = cache.get(cache_key)
            if cached_result is not None:
                return cached_result
            
            # Execute function
            result = func(*args, **kwargs)
            
            # Store in cache
            cache.set(cache_key, result)
            
            return result
        return wrapper
    return decorator

def performance_monitor(func: Callable) -> Callable:
    """Decorator to monitor function performance"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            if elapsed > 1.0:  # Log slow operations
                console.print(f"[dim]⏱️  {func.__name__} took {elapsed:.2f}s[/dim]")
            return result
        except Exception as e:
            elapsed = time.time() - start_time
            console.print(f"[red]❌ {func.__name__} failed after {elapsed:.2f}s: {e}[/red]")
            raise
    return wrapper

