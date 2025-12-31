---
description: Create a well-formatted git commit
---

Create a git commit for the current changes:

1. Run `git status` and `git diff --staged` to see what's being committed
2. If nothing is staged, stage all changes with `git add -A`
3. Analyze the changes to understand what was done
4. Write a commit message following Conventional Commits:
   - `feat:` new feature
   - `fix:` bug fix
   - `refactor:` code restructuring
   - `docs:` documentation
   - `test:` adding tests
   - `chore:` maintenance

Format:
```
type(scope): short description

- Bullet points for details if needed
- Keep lines under 72 characters
```

Execute the commit directly.
