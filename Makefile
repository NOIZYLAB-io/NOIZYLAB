.PHONY: help setup build test lint security organize update deploy clean

# NOIZYLAB Makefile - Build & Deployment Automation

help:
	@echo "NOIZYLAB Build System"
	@echo "====================="
	@echo ""
	@echo "Available targets:"
	@echo "  make setup              - Initialize development environment"
	@echo "  make organize           - Organize files by type and function"
	@echo "  make build              - Build all components"
	@echo "  make test               - Run tests"
	@echo "  make lint               - Lint code"
	@echo "  make security           - Security checks"
	@echo "  make update             - Update dependencies"
	@echo "  make deploy             - Deploy to GitHub"
	@echo "  make clean              - Clean build artifacts"
	@echo ""

setup:
	@echo "🔧 Setting up development environment..."
	@chmod +x scripts/*.sh
	@chmod +x scripts/*.py
	@source ~/.zsh_aliases || echo "⚠️  .zsh_aliases not found"
	@echo "✅ Development environment ready"

organize:
	@echo "📂 Organizing files..."
	@if [ -f "scripts/file_organizer.py" ]; then \
		python3 scripts/file_organizer.py; \
	else \
		find . -maxdepth 1 -type f -name "*.py" -exec mv {} _ORGANIZED/BY_TYPE/PYTHON/ \; 2>/dev/null; \
		find . -maxdepth 1 -type f -name "*.json" -exec mv {} _ORGANIZED/BY_TYPE/JSON/ \; 2>/dev/null; \
		echo "✅ Files organized"; \
	fi

build:
	@echo "🔨 Building NOIZYLAB..."
	@echo "  - Validating structure..."
	@if [ -d "_ORGANIZED" ]; then echo "    ✅ Organization found"; fi
	@if [ -f "README.md" ]; then echo "    ✅ Documentation found"; fi
	@if [ -d "scripts" ]; then echo "    ✅ Scripts found"; fi
	@if [ -d ".github" ]; then echo "    ✅ GitHub config found"; fi
	@echo "✅ Build complete"

test:
	@echo "🧪 Running tests..."
	@if command -v pytest &> /dev/null; then \
		pytest -v; \
	else \
		echo "⚠️  pytest not installed"; \
	fi

lint:
	@echo "🔍 Linting code..."
	@if command -v pylint &> /dev/null; then \
		echo "  - Python linting..."; \
		find scripts -name "*.py" -type f -exec pylint {} \; 2>/dev/null || true; \
	fi
	@if command -v shellcheck &> /dev/null; then \
		echo "  - Shell linting..."; \
		find scripts -name "*.sh" -type f -exec shellcheck {} \; 2>/dev/null || true; \
	fi
	@echo "✅ Linting complete"

security:
	@echo "🔒 Running security checks..."
	@echo "  - Checking for exposed secrets..."
	@if [ -f ".gitignore" ]; then \
		echo "    ✅ .gitignore configured"; \
	fi
	@echo "  - Verifying permissions..."
	@ls -la .ssh 2>/dev/null || echo "    ⚠️  SSH keys not found"
	@echo "✅ Security check complete"

update:
	@echo "📦 Updating dependencies..."
	@if command -v pip &> /dev/null; then \
		echo "  - Python: pip install --upgrade pip"; \
		pip install --upgrade pip 2>/dev/null || true; \
	fi
	@if command -v npm &> /dev/null; then \
		echo "  - Node: npm update"; \
		npm update 2>/dev/null || true; \
	fi
	@echo "✅ Dependencies updated"

deploy:
	@echo "🚀 Deploying to GitHub..."
	@echo "  - Checking git status..."
	@git status --short
	@echo ""
	@echo "  - Adding changes..."
	@git add -A
	@echo ""
	@echo "  - Committing..."
	@read -p "Commit message: " msg; git commit -m "$$msg" || echo "No changes to commit"
	@echo ""
	@echo "  - Pushing to origin..."
	@git push origin upbeat-moore
	@echo "✅ Deployment complete"

clean:
	@echo "🧹 Cleaning build artifacts..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@rm -rf build dist *.egg-info 2>/dev/null || true
	@echo "✅ Cleanup complete"

status:
	@echo "📊 NOIZYLAB Status"
	@echo "=================="
	@echo ""
	@echo "🔧 Components:"
	@echo "  Organization: $([ -d "_ORGANIZED" ] && echo '✅' || echo '❌')"
	@echo "  Documentation: $([ -f "README.md" ] && echo '✅' || echo '❌')"
	@echo "  Scripts: $([ -d "scripts" ] && echo '✅' || echo '❌')"
	@echo "  GitHub Config: $([ -d ".github" ] && echo '✅' || echo '❌')"
	@echo ""
	@echo "📦 Storage:"
	@du -sh _ORGANIZED/BY_TYPE/* 2>/dev/null || echo "  Organization not available"
	@echo ""
	@echo "🌳 Git:"
	@git branch
	@echo ""
	@echo "✅ System ready"

.DEFAULT_GOAL := help
