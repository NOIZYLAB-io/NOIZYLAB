---
description: Code review - analyze code quality and suggest improvements
argument-hint: <file_or_directory>
---

Review the code at $ARGUMENTS with a focus on:

1. **Security** - Look for vulnerabilities (injection, XSS, hardcoded secrets, etc.)
2. **Performance** - Identify bottlenecks, unnecessary computations, memory leaks
3. **Maintainability** - Check for code smells, complexity, naming issues
4. **Best Practices** - Verify patterns match language/framework conventions

Format your response as:
## Summary
Brief overview of code quality (1-2 sentences)

## Issues Found
List issues by severity (Critical > High > Medium > Low)

## Suggestions
Actionable improvements with code examples

Keep it concise. Don't rewrite the entire file - focus on the important changes.
