#!/bin/bash

# ═══════════════════════════════════════════════════════════════════
# GLOB PATTERN PERFORMANCE TEST
# ═══════════════════════════════════════════════════════════════════
# Test VS Code glob patterns to understand performance characteristics
# Based on VS Code source: src/vs/base/common/glob.ts
# ═══════════════════════════════════════════════════════════════════

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

clear

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════════╗
║         VS CODE GLOB PATTERN PERFORMANCE TEST                    ║
║     Understanding Fast-Path vs RegExp Patterns                   ║
╚═══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}FAST-PATH PATTERNS (Optimized in VS Code)${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
These patterns are HIGHLY optimized in VS Code's glob.ts:

TYPE 1 (T1): **/*.extension
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern: **/*.txt
Implementation: Just checks path.endsWith('.txt')
Performance: ⚡⚡⚡ INSTANT (no RegExp!)

Examples:
  **/*.js      → endsWith('.js')
  **/*.py      → endsWith('.py')
  **/*.mp3     → endsWith('.mp3')
  **/*.dmg     → endsWith('.dmg')

TYPE 2 (T2): **/filename
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern: **/package.json
Implementation: Just checks basename equals 'package.json'
Performance: ⚡⚡⚡ INSTANT (no RegExp!)

Examples:
  **/node_modules      → basename check
  **/.DS_Store         → basename check
  **/package.json      → basename check
  **/wrangler.toml     → basename check

TYPE 3 (T3): {**/*.ext1,**/*.ext2}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern: {**/*.html,**/*.txt}
Implementation: Multiple endsWith() checks (no RegExp!)
Performance: ⚡⚡⚡ INSTANT

Examples:
  {**/*.js,**/*.ts}            → endsWith('.js') OR endsWith('.ts')
  {**/*.mp3,**/*.wav}          → endsWith('.mp3') OR endsWith('.wav')
  {**/package.json,**/tsconfig.json} → basename checks

TYPE 4 (T4): **/path/to/folder
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern: **/src/lib
Implementation: Just checks path.endsWith('/src/lib')
Performance: ⚡⚡⚡ INSTANT

Examples:
  **/src/lib           → endsWith('/src/lib')
  **/node_modules/pkg  → endsWith('/node_modules/pkg')

TYPE 5 (T5): relative/path
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern: src/lib
Implementation: Just checks path equals 'src/lib'
Performance: ⚡⚡⚡ INSTANT

Examples:
  src/lib              → path == 'src/lib'
  docs/README.md       → path == 'docs/README.md'

EOF

echo ""
echo -e "${RED}═══════════════════════════════════════════════════════════${NC}"
echo -e "${RED}SLOW PATTERNS (Full RegExp Parsing)${NC}"
echo -e "${RED}═══════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
These patterns require full RegExp compilation:

MIXED PATH + GLOB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern: src/**/*.txt
Reason: Starts with concrete path, then has glob
Performance: 🐌 SLOW (requires RegExp compilation)

Examples:
  src/**/*.txt         → Full RegExp: /^src[/\\].*[^/\\]*\.txt$/
  lib/**/test/*.js     → Full RegExp parsing
  gabriel/_ORGANIZED/**/*.sh → Full RegExp parsing

CHARACTER RANGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern: **/log[0-9].txt
Reason: Uses character ranges [0-9]
Performance: 🐌 SLOW (requires RegExp compilation)

Examples:
  **/file[0-9].txt     → Full RegExp
  **/backup[a-z].zip   → Full RegExp
  **/*[!0-9].log       → Full RegExp (negation)

NESTED GROUPING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern: **/{a,b}/**/*.js
Reason: Nested globs with grouping
Performance: 🐌 SLOW (requires RegExp compilation)

Examples:
  **/{foo,bar}/**/*.js → Full RegExp
  **/{src,lib}/*       → Full RegExp

WILDCARDS IN PATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern: src/*/lib/*.js
Reason: Single * in path segments
Performance: 🐌 SLOW (requires RegExp compilation)

Examples:
  src/*/lib/*.js       → Full RegExp
  gabriel/*/backup     → Full RegExp

EOF

echo ""
echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}OPTIMIZATION RECOMMENDATIONS FOR NOIZYLAB${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
REPLACE SLOW PATTERNS WITH FAST EQUIVALENTS:

❌ SLOW: src/**/*.sh
✅ FAST: **/*.sh (if you don't need src/ restriction)

❌ SLOW: **/backup[0-9].zip
✅ FAST: **/backup*.zip (if exact number match not critical)

❌ SLOW: **/{foo,bar}/**/*.js
✅ FAST: {**/foo/**/*.js,**/bar/**/*.js} (if possible)

❌ SLOW: gabriel/_ORGANIZED/**/*.py
✅ FAST: **/*.py (then filter by path in code if needed)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FOR YOUR 50TB CLEANUP:

✅ Use: **/*.mp3, **/*.wav, **/*.dmg (FAST endsWith checks)
✅ Use: **/node_modules, **/.DS_Store (FAST basename checks)
✅ Use: {**/*.mp3,**/*.wav,**/*.aiff} (FAST multiple endsWith)

❌ Avoid: gabriel/_ORGANIZED/**/*.sh (use **/*.sh instead)
❌ Avoid: **/backup[0-9].txt (use **/backup*.txt)
❌ Avoid: Complex nested patterns

CACHING BENEFIT:
VS Code caches up to 10,000 parsed patterns. Reusing patterns is FREE!

EOF

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}PRACTICAL TEST: Search for Audio Files${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo "Testing glob pattern matching on local filesystem..."
echo ""

# Test fast patterns
echo -e "${GREEN}FAST PATTERN TEST:${NC} **/*.mp3"
echo "Implementation: Just checks endsWith('.mp3')"
time find ~/NOIZYLAB -name "*.mp3" -maxdepth 3 2>/dev/null | head -5
echo ""

echo -e "${GREEN}FAST PATTERN TEST:${NC} **/*.sh"
echo "Implementation: Just checks endsWith('.sh')"
time find ~/NOIZYLAB -name "*.sh" -maxdepth 2 2>/dev/null | head -5
echo ""

# Test basename pattern
echo -e "${GREEN}FAST PATTERN TEST:${NC} **/README.md"
echo "Implementation: Just checks basename == 'README.md'"
time find ~/NOIZYLAB -name "README.md" -maxdepth 3 2>/dev/null | head -5
echo ""

echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}SOURCE CODE REFERENCE${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
From VS Code glob.ts:

// T1: Common pattern: **/*.txt just need endsWith check
const T1 = /^\*\*\/\*\.[\w\.-]+$/;

// T2: Common pattern: **/some.txt just need basename check
const T2 = /^\*\*\/([\w\.-]+)\/?$/;

// T3: Repetition of common patterns {**/*.txt,**/*.png}
const T3 = /^{\*\*\/\*?[\w\.-]+\/?(,\*\*\/\*?[\w\.-]+\/?)*}$/;

// T4: Common pattern: **/something/else just need endsWith check
const T4 = /^\*\*((\/[\w\.-]+)+)\/?$/;

// T5: Common pattern: something/else just needs equals check
const T5 = /^([\w\.-]+(\/[\w\.-]+)*)\/?$/;

If pattern doesn't match T1-T5:
→ Full RegExp compilation with parseRegExp()
→ Slower performance

CACHE:
const CACHE = new LRUCache<string, ParsedStringPattern>(10000);
→ Up to 10,000 patterns cached
→ Reusing same pattern = instant lookup!

EOF

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}🚀 OPTIMIZATION SUMMARY${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
FOR MAXIMUM PERFORMANCE IN NOIZYLAB:

1. ✅ USE SIMPLE PATTERNS: **/*.ext, **/filename
2. ✅ USE GROUPING: {**/*.ext1,**/*.ext2}
3. ✅ REUSE PATTERNS: Cached up to 10,000!
4. ❌ AVOID: Complex path + glob combinations
5. ❌ AVOID: Character ranges [0-9] unless critical
6. ❌ AVOID: Nested grouping **/{a,b}/**

PHINEAS POTTS STANDARD:
Simple patterns = MAGICAL performance! ✨

Fast patterns allow instant searches across 50TB!

EOF

echo ""
echo -e "${CYAN}Learn more:${NC}"
echo "  VS Code Docs: https://code.visualstudio.com/docs/editor/glob-patterns"
echo "  Source Code:  https://github.com/microsoft/vscode/blob/main/src/vs/base/common/glob.ts"
echo ""
