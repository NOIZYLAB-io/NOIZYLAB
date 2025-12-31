---
description: Generate tests for code
argument-hint: <file_or_function>
---

Generate comprehensive tests for $ARGUMENTS:

1. **Unit Tests** - Test individual functions/methods in isolation
2. **Edge Cases** - Empty inputs, nulls, boundary values, error conditions
3. **Integration Points** - If applicable, test how components interact

Requirements:
- Use the testing framework already in this project (detect from package.json, pytest, etc.)
- Include both positive and negative test cases
- Add clear test descriptions
- Mock external dependencies appropriately

Write the tests directly - don't just describe them.
