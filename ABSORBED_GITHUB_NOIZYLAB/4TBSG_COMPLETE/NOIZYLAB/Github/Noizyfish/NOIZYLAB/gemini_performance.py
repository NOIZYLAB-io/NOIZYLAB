#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Gemini Performance Optimizer
Ultra-fast caching, batching, and parallel processing
"""

import os
import json
import time
import asyncio
from typing import List, Dict, Optional
from pathlib import Path
from functools import lru_cache
from google import genai

class GeminiPerformance:
    """High-performance Gemini with aggressive optimizations"""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('GEMINI_API_KEY', '')
        if api_key:
            os.environ['GEMINI_API_KEY'] = api_key

        self.client = genai.Client()
        self.cache_dir = Path(__file__).parent / "performance_cache"
        self.cache_dir.mkdir(exist_ok=True)
        self.cache = {}
        self.batch_queue = []
        self.max_batch_size = 10

    @lru_cache(maxsize=1000)
    def cached_generate(self, prompt_hash: str, prompt: str, model: str = "gemini-2.5-flash"):
        """Cached generation for repeated queries"""
        cache_file = self.cache_dir / f"{prompt_hash}.json"

        if cache_file.exists():
            with open(cache_file, 'r') as f:
                return json.load(f)['response']

        try:
            response = self.client.models.generate_content(
                model=model,
                contents=prompt
            )
            result = response.text

            # Cache result
            with open(cache_file, 'w') as f:
                json.dump({"prompt": prompt, "response": result}, f)

            return result
        except Exception as e:
            return f"Error: {e}"

    def batch_generate(self, prompts: List[str], model: str = "gemini-2.5-flash") -> List[str]:
        """Ultra-fast batch processing"""
        results = []

        # Process in parallel chunks
        chunk_size = self.max_batch_size
        for i in range(0, len(prompts), chunk_size):
            chunk = prompts[i:i+chunk_size]

            # Parallel processing
            tasks = []
            for prompt in chunk:
                tasks.append(self._generate_async(prompt, model))

            chunk_results = asyncio.run(asyncio.gather(*tasks))
            results.extend(chunk_results)

        return results

    async def _generate_async(self, prompt: str, model: str):
        """Async generation for parallel processing"""
        try:
            response = self.client.models.generate_content(
                model=model,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def preload_common_queries(self, queries: List[str], model: str = "gemini-2.5-flash"):
        """Preload cache with common queries"""
        print(f"🔄 Preloading {len(queries)} common queries...")
        for query in queries:
            import hashlib
            prompt_hash = hashlib.md5(query.encode()).hexdigest()
            self.cached_generate(prompt_hash, query, model)
        print("✅ Preload complete!")

    def optimize_for_m2_ultra(self):
        """M2 Ultra specific optimizations"""
        # Increase batch size for 192GB RAM
        self.max_batch_size = 50

        # Enable aggressive caching
        self.cache_dir = Path(__file__).parent / "ultra_cache"
        self.cache_dir.mkdir(exist_ok=True)

        # Preload common repair queries
        common_queries = [
            "MacBook won't turn on",
            "iPhone screen cracked",
            "Windows blue screen",
            "Printer not working",
            "WiFi connection issues",
            "Slow computer",
            "Battery not charging",
            "Keyboard not responding"
        ]

        self.preload_common_queries(common_queries)
        print("✅ M2 Ultra optimizations applied!")

