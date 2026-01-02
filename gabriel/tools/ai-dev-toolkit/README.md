# 🔧 NOIZYLAB AI Dev Toolkit

**AI-Powered Development Tools for Maximum Productivity**

A comprehensive suite of 10 AI-powered development tools that integrate with VS Code, GitLens, and GitKraken to supercharge your development workflow.

## 🚀 Tools Included (10 Total)

| Tool | Description | Command |
|------|-------------|---------|
| **AI Code Review** | Automated PR/commit analysis | `python ai-code-review.py` |
| **Smart Commit** | AI-powered commit messages | `python smart-commit.py` |
| **Changelog Generator** | Automated changelog from commits | `python changelog-generator.py` |
| **Merge Resolver** | AI conflict resolution | `python merge-resolver.py` |
| **Test Suggester** | AI test recommendations | `python test-suggester.py` |
| **Code Quality** | Deep quality analysis & scoring | `python code-quality.py` |
| **Predictive Branch** | Branch strategy optimization | `python predictive-branch.py` |
| **Issue Linker** | Auto-link commits to issues | `python issue-linker.py` |
| **AI Docs** | Auto documentation generator | `python ai-docs.py` |
| **Context Suggest** | Intelligent code suggestions | `python context-suggest.py` |

## 📦 Installation

```bash
# Install dependencies
pip install anthropic

# Set API key
export ANTHROPIC_API_KEY="your-key-here"
```

## 🔍 AI Code Review

Automatically analyze code for issues, security vulnerabilities, and improvements.

```bash
# Review changes vs main branch
python ai-code-review.py

# Review against different branch
python ai-code-review.py --base develop

# Skip AI analysis (static only)
python ai-code-review.py --no-ai

# Output as JSON
python ai-code-review.py --json
```

**Features:**
- 🔒 Security vulnerability detection
- 🐛 Code smell identification
- 📊 Complexity analysis
- 🤖 AI-powered suggestions
- 📈 Quality scoring (0-100)

## 📝 Smart Commit

Generate context-aware, conventional commit messages.

```bash
# Interactive mode
python smart-commit.py

# Auto-commit (no confirmation)
python smart-commit.py --auto

# Dry run (show message only)
python smart-commit.py --dry-run

# Force commit type
python smart-commit.py --type feat
```

**Commit Format:**
```
🚀 feat(scope): add new feature
🐛 fix(scope): fix bug
📚 docs: update documentation
♻️ refactor: improve code structure
🧪 test: add tests
🧹 chore: maintenance
```

## 📋 Changelog Generator

Create structured changelogs from commit history.

```bash
# Generate from last tag to HEAD
python changelog-generator.py

# Full changelog from all tags
python changelog-generator.py --full

# Release notes format
python changelog-generator.py --release-notes --version v2.0.0

# Enhance with AI
python changelog-generator.py --enhance

# Output to file
python changelog-generator.py --output CHANGELOG.md
```

**Output Format:**
```markdown
## [v2.0.0] - 2026-01-02

### 🚀 Features
- **api:** Add new endpoint for user data ([#123](link))

### 🐛 Bug Fixes  
- **auth:** Fix token refresh issue ([abc123](link))
```

## 🔀 Merge Resolver

AI-powered merge conflict resolution.

```bash
# Interactive mode
python merge-resolver.py

# Auto-resolve high-confidence conflicts
python merge-resolver.py --auto

# Resolve specific file
python merge-resolver.py --file path/to/file.py

# Dry run
python merge-resolver.py --dry-run
```

**Resolution Strategies:**
- `ours` - Keep current branch version
- `theirs` - Keep incoming branch version
- `both` - Combine both versions
- `ai` - Let AI merge intelligently

## 🧪 Test Suggester

Get AI-powered test recommendations based on code changes.

```bash
# Analyze all files
python test-suggester.py

# Only changed files
python test-suggester.py --changed

# Specific file
python test-suggester.py --file src/module.py

# Generate test file
python test-suggester.py --generate tests/test_module.py

# With coverage analysis
python test-suggester.py --coverage

# AI-enhanced suggestions
python test-suggester.py --ai
```

**Test Types Generated:**
- Unit tests
- Edge case tests
- Error handling tests
- Integration tests

## ⚙️ VS Code Integration

Add to `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "AI Code Review",
            "type": "shell",
            "command": "python",
            "args": ["${workspaceFolder}/tools/ai-dev-toolkit/ai-code-review.py"],
            "problemMatcher": []
        },
        {
            "label": "Smart Commit",
            "type": "shell", 
            "command": "python",
            "args": ["${workspaceFolder}/tools/ai-dev-toolkit/smart-commit.py"],
            "problemMatcher": []
        },
        {
            "label": "Generate Changelog",
            "type": "shell",
            "command": "python",
            "args": ["${workspaceFolder}/tools/ai-dev-toolkit/changelog-generator.py", "--output", "CHANGELOG.md"],
            "problemMatcher": []
        }
    ]
}
```

## 🔗 Git Hooks

Add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Run AI code review before commit
python tools/ai-dev-toolkit/ai-code-review.py --no-ai
if [ $? -ne 0 ]; then
    echo "❌ Code review failed. Fix issues before committing."
    exit 1
fi
```

Add to `.git/hooks/prepare-commit-msg`:

```bash
#!/bin/bash
# Generate smart commit message
MSG=$(python tools/ai-dev-toolkit/smart-commit.py --dry-run --auto 2>/dev/null)
if [ -n "$MSG" ]; then
    echo "$MSG" > "$1"
fi
```

## 🎯 GitLens Integration

These tools complement GitLens features:
- Use **Smart Commit** with GitLens commit interface
- Use **Changelog Generator** with GitLens Graph view
- Use **AI Code Review** before GitLens PR creation

## 📊 Code Quality Analyzer

Deep code analysis with complexity metrics and smell detection.

```bash
# Analyze single file
python code-quality.py --path src/main.py

# Analyze directory
python code-quality.py --path src/

# Specific extensions
python code-quality.py --path . --extensions .py .js

# Output as JSON
python code-quality.py --path . --json
```

**Analysis Includes:**
- 📊 Complexity metrics
- 👃 Code smell detection
- 🔒 Security vulnerability scanning
- 🔄 Refactoring suggestions
- ✅ Best practices validation

## 🌿 Predictive Branching

AI-powered branch strategy optimization.

```bash
# Full branching analysis
python predictive-branch.py

# Suggest branch name
python predictive-branch.py --suggest "user authentication feature"

# Health check only
python predictive-branch.py --health

# JSON output
python predictive-branch.py --json
```

**Features:**
- 📊 Branch health monitoring
- 🏷️ Smart branch naming
- 📋 Release strategy recommendations
- 🧹 Cleanup candidate detection

## 🔗 Issue Linker

Automatic commit-to-issue linking.

```bash
# Full linkage report
python issue-linker.py

# Analyze specific commit
python issue-linker.py --commit HEAD

# Find commits for issue
python issue-linker.py --issue 123

# List unlinked commits
python issue-linker.py --unlinked
```

**Supports:**
- GitHub Issues (#123)
- Jira Issues (ABC-123)
- GitLab Issues
- Azure DevOps

## 📚 AI Documentation Generator

Auto-generate comprehensive documentation.

```bash
# Analyze file docs
python ai-docs.py --file src/main.py

# Generate API docs
python ai-docs.py --file src/api.py --api

# Generate README
python ai-docs.py --readme

# Add inline comments
python ai-docs.py --file src/complex.py --comments

# Coverage report
python ai-docs.py --report
```

**Generates:**
- 📝 Function/class docstrings
- 📖 API documentation
- 📄 README files
- 💬 Inline code comments

## 💡 Contextual Code Suggestions

Real-time intelligent code suggestions.

```bash
# Full analysis
python context-suggest.py --file src/main.py

# Code completions at line
python context-suggest.py --file src/main.py --complete --line 42

# Refactoring suggestions
python context-suggest.py --file src/main.py --refactor

# Performance optimizations
python context-suggest.py --file src/main.py --optimize

# Security audit
python context-suggest.py --file src/main.py --security
```

**Suggestion Types:**
- 🔄 Refactoring opportunities
- ⚡ Performance optimizations
- 🔒 Security improvements
- 📋 Best practice alignment

## 📊 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Anthropic API key for AI features | Required |
| `AI_MODEL` | Claude model to use | `claude-sonnet-4-20250514` |
| `AI_TIMEOUT` | API timeout in seconds | `30` |

## 🔧 Configuration

Create `~/.ai-dev-toolkit.json`:

```json
{
    "model": "claude-sonnet-4-20250514",
    "commit_style": "conventional",
    "emoji_commits": true,
    "auto_stage": false,
    "review_on_commit": true,
    "test_framework": "pytest"
}
```

## 📈 Roadmap

- [x] Core AI tools (10/10 complete)
- [ ] VS Code extension packaging
- [ ] GitHub Actions integration
- [ ] GitKraken Workspaces support
- [ ] Multi-language support expansion
- [ ] Custom rule definitions
- [ ] Team collaboration features

---

**Made with 🤖 + ❤️ by NOIZYLAB**
---

**Part of NOIZYLAB GABRIEL Ecosystem**  
*Updated: 2026-01-02*
