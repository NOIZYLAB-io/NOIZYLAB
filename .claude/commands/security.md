---
description: Security audit - find vulnerabilities and issues
argument-hint: <file_or_directory>
---

Perform a security audit on: $ARGUMENTS

Check for:
1. **Injection** - SQL, command, XSS, template injection
2. **Authentication** - Weak auth, session issues, credential exposure
3. **Authorization** - Missing access controls, privilege escalation
4. **Data Exposure** - Sensitive data in logs, errors, or responses
5. **Secrets** - Hardcoded keys, passwords, tokens
6. **Dependencies** - Known vulnerable packages
7. **Configuration** - Insecure defaults, debug mode in production

Output format:
```
## Critical
[issues that must be fixed immediately]

## High
[serious issues to fix soon]

## Medium
[should be addressed]

## Low/Informational
[nice to fix]

## Recommendations
[specific fixes with code]
```

Be thorough. Security issues matter.
