# Debug Mode

You are now in **DEEP DEBUG MODE**. Your task is to find and fix the issue.

## Debug Protocol

1. **Reproduce**: Understand exactly what's happening vs what should happen
2. **Isolate**: Narrow down where the problem originates
3. **Trace**: Follow the data/control flow to the root cause
4. **Fix**: Implement the minimal fix
5. **Verify**: Confirm the fix works and doesn't break anything else

## Analysis Approach

- Read error messages carefully - they often tell you exactly what's wrong
- Check recent changes - bugs often come from recent modifications
- Look at the stack trace from bottom to top
- Consider edge cases and null/undefined values
- Check types and interfaces match
- Verify async/await and promise handling
- Look for race conditions in concurrent code

## Output Format

```
## Problem
[What's happening]

## Root Cause
[Why it's happening]

## Fix
[Code changes needed]

## Verification
[How to confirm the fix works]
```

Begin debugging. Be methodical and thorough.
