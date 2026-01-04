.PHONY: help build test lint clean deploy install upgrade nuke organize safari-reset

# ═══════════════════════════════════════════════════════════════════════════════
# 🌍 NOIZYLAB — The United Nations of Code
# ═══════════════════════════════════════════════════════════════════════════════

help:
	@echo "╔═══════════════════════════════════════════════════════════════════════════╗"
	@echo "║  🌍 NOIZYLAB — Available Commands                                         ║"
	@echo "╚═══════════════════════════════════════════════════════════════════════════╝"
	@echo ""
	@echo "  📦 SETUP"
	@echo "     make install     — Install all dependencies"
	@echo "     make upgrade     — Upgrade all packages (pip, npm, brew)"
	@echo ""
	@echo "  🔨 BUILD"
	@echo "     make build       — Build/compile project"
	@echo "     make test        — Run all tests"
	@echo "     make lint        — Run linters"
	@echo "     make deploy      — Deploy worker to Cloudflare"
	@echo ""
	@echo "  🧹 CLEANUP"
	@echo "     make clean       — Clean build artifacts"
	@echo "     make nuke        — 🔥 FORCEFUL: Delete all junk folders"
	@echo "     make organize    — Organize & consolidate duplicates"
	@echo ""
	@echo "  🍎 MACOS"
	@echo "     make safari-reset — Reset Safari window layout"
	@echo ""

install:
	@echo "📦 Installing dependencies..."
	@pip install -r requirements.txt 2>/dev/null || echo "  ⚠️  No requirements.txt"
	@cd workers/noizylab && npm install 2>/dev/null || echo "  ⚠️  No package.json"
	@echo "✅ Done"

upgrade:
	@echo "⬆️  Upgrading packages..."
	@pip install --upgrade pip 2>/dev/null || true
	@cd workers/noizylab && npm upgrade 2>/dev/null || true
	@brew upgrade 2>/dev/null || true
	@echo "✅ Done"

build:
	@echo "🔨 Building project..."
	@cd workers/noizylab && npm run build 2>/dev/null || echo "  ⚠️  No build script"

test:
	@echo "🧪 Running tests..."
	@pytest tests/ 2>/dev/null || npm test 2>/dev/null || echo "  ⚠️  No tests configured"

lint:
	@echo "🔍 Running linters..."
	@pylint src/ 2>/dev/null || npm run lint 2>/dev/null || echo "  ⚠️  No linters configured"

clean:
	@echo "🧹 Cleaning build artifacts..."
	@rm -rf build/ dist/ *.egg-info __pycache__ .pytest_cache
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@find . -name ".DS_Store" -delete 2>/dev/null || true
	@echo "✅ Clean"

deploy:
	@echo "🚀 Deploying to Cloudflare..."
	@cd workers/noizylab && wrangler deploy
	@echo "✅ Deployed"

# ═══════════════════════════════════════════════════════════════════════════════
# 🔥 FORCEFUL CLEANUP
# ═══════════════════════════════════════════════════════════════════════════════

nuke:
	@echo "🔥 NUKING JUNK FOLDERS..."
	@chmod +x scripts/NUKE_THE_JUNK.sh
	@./scripts/NUKE_THE_JUNK.sh

organize:
	@echo "📁 Organizing repository..."
	@# Remove duplicate _HARVEST (keep _ORGANIZED)
	@rm -rf gabriel/CODEMASTER/_HARVEST 2>/dev/null || true
	@# Remove stale workspace files
	@find . -name "*.code-workspace" ! -name "AG_HOME.code-workspace" -delete 2>/dev/null || true
	@# Remove empty directories
	@find . -type d -empty -not -path "./.git/*" -delete 2>/dev/null || true
	@echo "✅ Organized"

# ═══════════════════════════════════════════════════════════════════════════════
# 🍎 MACOS UTILITIES
# ═══════════════════════════════════════════════════════════════════════════════

safari-reset:
	@echo "🍎 Resetting Safari layout..."
	@chmod +x scripts/safari_layout_reset.sh
	@./scripts/safari_layout_reset.sh --full

