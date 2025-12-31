---
description: Performance analysis - find bottlenecks and optimize
argument-hint: <file_or_function>
---

Analyze performance of: $ARGUMENTS

Look for:
1. **Algorithmic** - O(n²) when O(n) is possible, unnecessary iterations
2. **I/O** - Excessive disk/network calls, missing batching
3. **Memory** - Large allocations, memory leaks, missing cleanup
4. **Caching** - Missing cache opportunities, cache invalidation issues
5. **Concurrency** - Blocking operations, underutilized parallelism
6. **Database** - N+1 queries, missing indexes, unoptimized queries

Output:
```
## Bottlenecks Found
[ranked by impact]

## Quick Wins
[easy fixes with big impact]

## Optimization Suggestions
[specific code changes with before/after]
```

Focus on measurable improvements, not micro-optimizations.
