#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  🔀 AI MERGE CONFLICT RESOLVER v1.0                                           ║
║  Intelligent conflict resolution using AI and context                         ║
║  Part of: NOIZYLAB AI Dev Toolkit                                             ║
║  Updated: 2026-01-02                                                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import subprocess
import os
import sys
import re
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
MODEL = "claude-sonnet-4-20250514"

# ═══════════════════════════════════════════════════════════════════════════════
# DATA CLASSES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Conflict:
    """Represents a merge conflict."""
    file: str
    start_line: int
    end_line: int
    ours: str  # Current branch version
    theirs: str  # Incoming branch version
    base: str = ""  # Common ancestor (if available)
    context_before: str = ""
    context_after: str = ""
    resolution: str = ""
    confidence: float = 0.0
    explanation: str = ""

@dataclass
class ConflictFile:
    """A file with conflicts."""
    path: str
    content: str
    conflicts: list = field(default_factory=list)
    resolved_content: str = ""

# ═══════════════════════════════════════════════════════════════════════════════
# GIT HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def get_conflicted_files() -> list[str]:
    """Get list of files with merge conflicts."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', '--diff-filter=U'],
            capture_output=True, text=True, check=True
        )
        return [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]
    except subprocess.CalledProcessError:
        return []

def get_merge_base() -> Optional[str]:
    """Get merge base commit."""
    try:
        result = subprocess.run(
            ['git', 'merge-base', 'HEAD', 'MERGE_HEAD'],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_file_at_commit(file_path: str, commit: str) -> str:
    """Get file content at specific commit."""
    try:
        result = subprocess.run(
            ['git', 'show', f'{commit}:{file_path}'],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return ""

def get_branch_names() -> tuple[str, str]:
    """Get current and merging branch names."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True, text=True, check=True
        )
        current = result.stdout.strip()
        
        # Try to get merge head branch name
        try:
            result = subprocess.run(
                ['git', 'name-rev', '--name-only', 'MERGE_HEAD'],
                capture_output=True, text=True, check=True
            )
            merging = result.stdout.strip()
        except:
            merging = "MERGE_HEAD"
        
        return current, merging
    except subprocess.CalledProcessError:
        return "HEAD", "MERGE_HEAD"

def get_commit_messages(file_path: str, n: int = 5) -> list[str]:
    """Get recent commit messages for a file."""
    try:
        result = subprocess.run(
            ['git', 'log', f'-{n}', '--oneline', '--', file_path],
            capture_output=True, text=True, check=True
        )
        return [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
    except subprocess.CalledProcessError:
        return []

# ═══════════════════════════════════════════════════════════════════════════════
# CONFLICT PARSING
# ═══════════════════════════════════════════════════════════════════════════════

def parse_conflicts(file_path: str) -> ConflictFile:
    """Parse a file for merge conflicts."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return ConflictFile(path=file_path, content="", conflicts=[])
    
    conflict_file = ConflictFile(path=file_path, content=content)
    
    # Pattern for merge conflicts (handles both diff3 and standard)
    # <<<<<<< HEAD
    # our changes
    # ||||||| base (optional in diff3)
    # base content
    # =======
    # their changes
    # >>>>>>> branch
    
    pattern = r'<<<<<<< ([^\n]+)\n(.*?)(?:\|\|\|\|\|\|\| ([^\n]+)\n(.*?))?=======(.*?)>>>>>>> ([^\n]+)'
    
    lines = content.split('\n')
    line_num = 1
    
    for match in re.finditer(pattern, content, re.DOTALL):
        # Calculate line numbers
        start_pos = match.start()
        start_line = content[:start_pos].count('\n') + 1
        end_line = start_line + match.group(0).count('\n')
        
        conflict = Conflict(
            file=file_path,
            start_line=start_line,
            end_line=end_line,
            ours=match.group(2).strip(),
            theirs=match.group(5).strip(),
            base=match.group(4).strip() if match.group(4) else ""
        )
        
        # Get context
        context_lines = 5
        start_idx = max(0, start_line - context_lines - 1)
        end_idx = min(len(lines), end_line + context_lines)
        
        conflict.context_before = '\n'.join(lines[start_idx:start_line-1])
        conflict.context_after = '\n'.join(lines[end_line:end_idx])
        
        conflict_file.conflicts.append(conflict)
    
    return conflict_file

# ═══════════════════════════════════════════════════════════════════════════════
# RESOLUTION STRATEGIES
# ═══════════════════════════════════════════════════════════════════════════════

def simple_resolve(conflict: Conflict, strategy: str) -> str:
    """Simple resolution strategies."""
    if strategy == 'ours':
        return conflict.ours
    elif strategy == 'theirs':
        return conflict.theirs
    elif strategy == 'both':
        return f"{conflict.ours}\n{conflict.theirs}"
    elif strategy == 'both-reversed':
        return f"{conflict.theirs}\n{conflict.ours}"
    else:
        return conflict.ours

def analyze_conflict(conflict: Conflict) -> dict:
    """Analyze conflict to suggest resolution."""
    analysis = {
        'type': 'unknown',
        'suggested_strategy': 'manual',
        'confidence': 0.0,
        'reason': ''
    }
    
    ours_lines = conflict.ours.strip().split('\n')
    theirs_lines = conflict.theirs.strip().split('\n')
    
    # Check if one is empty
    if not conflict.ours.strip():
        analysis['type'] = 'deletion_ours'
        analysis['suggested_strategy'] = 'theirs'
        analysis['confidence'] = 0.8
        analysis['reason'] = 'Our version deleted this code'
        return analysis
    
    if not conflict.theirs.strip():
        analysis['type'] = 'deletion_theirs'
        analysis['suggested_strategy'] = 'ours'
        analysis['confidence'] = 0.8
        analysis['reason'] = 'Their version deleted this code'
        return analysis
    
    # Check if they're very similar (formatting changes)
    ours_normalized = re.sub(r'\s+', ' ', conflict.ours.strip())
    theirs_normalized = re.sub(r'\s+', ' ', conflict.theirs.strip())
    
    if ours_normalized == theirs_normalized:
        analysis['type'] = 'formatting'
        analysis['suggested_strategy'] = 'ours'
        analysis['confidence'] = 0.95
        analysis['reason'] = 'Only whitespace/formatting differences'
        return analysis
    
    # Check if one is a superset of the other
    if conflict.ours in conflict.theirs:
        analysis['type'] = 'extension'
        analysis['suggested_strategy'] = 'theirs'
        analysis['confidence'] = 0.7
        analysis['reason'] = 'Their version extends our changes'
        return analysis
    
    if conflict.theirs in conflict.ours:
        analysis['type'] = 'extension'
        analysis['suggested_strategy'] = 'ours'
        analysis['confidence'] = 0.7
        analysis['reason'] = 'Our version extends their changes'
        return analysis
    
    # Check for import/require statements
    if re.match(r'^(import|from|require|#include)', conflict.ours) and \
       re.match(r'^(import|from|require|#include)', conflict.theirs):
        analysis['type'] = 'imports'
        analysis['suggested_strategy'] = 'both'
        analysis['confidence'] = 0.85
        analysis['reason'] = 'Both adding imports - likely need both'
        return analysis
    
    # Default to manual
    analysis['type'] = 'semantic'
    analysis['suggested_strategy'] = 'ai'
    analysis['confidence'] = 0.0
    analysis['reason'] = 'Semantic differences require careful review'
    
    return analysis

# ═══════════════════════════════════════════════════════════════════════════════
# AI RESOLUTION
# ═══════════════════════════════════════════════════════════════════════════════

def ai_resolve_conflict(conflict: Conflict, file_path: str) -> tuple[str, float, str]:
    """Use AI to resolve conflict."""
    if not ANTHROPIC_API_KEY:
        return conflict.ours, 0.0, "AI not available"
    
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        current_branch, merging_branch = get_branch_names()
        recent_commits = get_commit_messages(file_path)
        
        prompt = f"""Resolve this merge conflict intelligently.

FILE: {file_path}
CURRENT BRANCH: {current_branch}
MERGING BRANCH: {merging_branch}

CONTEXT BEFORE:
```
{conflict.context_before}
```

CURRENT BRANCH VERSION (ours):
```
{conflict.ours}
```

{f"COMMON ANCESTOR (base):{chr(10)}```{chr(10)}{conflict.base}{chr(10)}```{chr(10)}{chr(10)}" if conflict.base else ""}

MERGING BRANCH VERSION (theirs):
```
{conflict.theirs}
```

CONTEXT AFTER:
```
{conflict.context_after}
```

RECENT COMMITS:
{chr(10).join(recent_commits)}

INSTRUCTIONS:
1. Analyze both versions and their intent
2. Produce a merged result that:
   - Preserves functionality from both branches where appropriate
   - Maintains code consistency and style
   - Doesn't introduce bugs or duplicates
3. If one version is clearly better, use it
4. If they're independent changes, combine them properly

Respond with EXACTLY this format:
CONFIDENCE: <0.0-1.0>
EXPLANATION: <brief explanation>
RESOLUTION:
```
<resolved code>
```"""

        response = client.messages.create(
            model=MODEL,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        result = response.content[0].text.strip()
        
        # Parse response
        confidence_match = re.search(r'CONFIDENCE:\s*([\d.]+)', result)
        explanation_match = re.search(r'EXPLANATION:\s*(.+?)(?=RESOLUTION:|$)', result, re.DOTALL)
        resolution_match = re.search(r'RESOLUTION:\s*```[^\n]*\n(.*?)```', result, re.DOTALL)
        
        confidence = float(confidence_match.group(1)) if confidence_match else 0.5
        explanation = explanation_match.group(1).strip() if explanation_match else "AI resolution"
        resolution = resolution_match.group(1).strip() if resolution_match else conflict.ours
        
        return resolution, confidence, explanation
        
    except Exception as e:
        return conflict.ours, 0.0, f"AI error: {str(e)}"

# ═══════════════════════════════════════════════════════════════════════════════
# RESOLUTION APPLICATION
# ═══════════════════════════════════════════════════════════════════════════════

def resolve_file(conflict_file: ConflictFile, auto_resolve: bool = False, use_ai: bool = True) -> str:
    """Resolve all conflicts in a file."""
    content = conflict_file.content
    
    # Process conflicts in reverse order to maintain line numbers
    for conflict in reversed(conflict_file.conflicts):
        # Analyze conflict
        analysis = analyze_conflict(conflict)
        
        if analysis['confidence'] >= 0.8 and auto_resolve:
            # High confidence automatic resolution
            resolution = simple_resolve(conflict, analysis['suggested_strategy'])
            conflict.resolution = resolution
            conflict.confidence = analysis['confidence']
            conflict.explanation = analysis['reason']
        elif use_ai and analysis['suggested_strategy'] == 'ai':
            # Use AI for complex conflicts
            resolution, confidence, explanation = ai_resolve_conflict(conflict, conflict_file.path)
            conflict.resolution = resolution
            conflict.confidence = confidence
            conflict.explanation = explanation
        else:
            # Use suggested strategy
            conflict.resolution = simple_resolve(conflict, analysis['suggested_strategy'])
            conflict.confidence = analysis['confidence']
            conflict.explanation = analysis['reason']
        
        # Replace conflict markers with resolution
        pattern = r'<<<<<<< [^\n]+\n.*?>>>>>>> [^\n]+'
        
        # Find the specific conflict in content
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content[:match.start()] + conflict.resolution + content[match.end():]
    
    conflict_file.resolved_content = content
    return content

def write_resolved_file(conflict_file: ConflictFile):
    """Write resolved content back to file."""
    with open(conflict_file.path, 'w', encoding='utf-8') as f:
        f.write(conflict_file.resolved_content)

# ═══════════════════════════════════════════════════════════════════════════════
# INTERACTIVE MODE
# ═══════════════════════════════════════════════════════════════════════════════

def interactive_resolve():
    """Interactive conflict resolution."""
    conflicted = get_conflicted_files()
    
    if not conflicted:
        print("✅ No merge conflicts found!")
        return
    
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  🔀 AI MERGE CONFLICT RESOLVER v1.0                                           ║
╚═══════════════════════════════════════════════════════════════════════════════╝

📁 Files with conflicts ({len(conflicted)}):
""")
    
    for f in conflicted:
        print(f"   • {f}")
    
    current, merging = get_branch_names()
    print(f"\n🔀 Merging: {merging} → {current}\n")
    
    for file_path in conflicted:
        print(f"\n{'='*60}")
        print(f"📄 {file_path}")
        print('='*60)
        
        conflict_file = parse_conflicts(file_path)
        
        if not conflict_file.conflicts:
            print("  No parseable conflicts found")
            continue
        
        for i, conflict in enumerate(conflict_file.conflicts, 1):
            print(f"\n  Conflict {i}/{len(conflict_file.conflicts)} (lines {conflict.start_line}-{conflict.end_line})")
            print(f"\n  OURS ({current}):")
            for line in conflict.ours.split('\n')[:10]:
                print(f"    + {line}")
            
            print(f"\n  THEIRS ({merging}):")
            for line in conflict.theirs.split('\n')[:10]:
                print(f"    - {line}")
            
            # Analyze
            analysis = analyze_conflict(conflict)
            print(f"\n  📊 Analysis: {analysis['type']}")
            print(f"  💡 Suggestion: {analysis['suggested_strategy']} ({analysis['confidence']*100:.0f}% confidence)")
            print(f"  📝 Reason: {analysis['reason']}")
            
            print("\n  Options:")
            print("    [o] Use ours")
            print("    [t] Use theirs")
            print("    [b] Use both")
            print("    [a] AI resolve")
            print("    [s] Skip (keep conflict)")
            print("    [e] Edit manually")
            
            choice = input("\n  Choice: ").strip().lower()
            
            if choice == 'o':
                conflict.resolution = conflict.ours
                conflict.explanation = "Manual: chose ours"
            elif choice == 't':
                conflict.resolution = conflict.theirs
                conflict.explanation = "Manual: chose theirs"
            elif choice == 'b':
                conflict.resolution = f"{conflict.ours}\n{conflict.theirs}"
                conflict.explanation = "Manual: combined both"
            elif choice == 'a':
                print("  🤖 AI resolving...")
                resolution, confidence, explanation = ai_resolve_conflict(conflict, file_path)
                print(f"\n  AI Resolution (confidence: {confidence*100:.0f}%):")
                for line in resolution.split('\n')[:15]:
                    print(f"    {line}")
                print(f"\n  Explanation: {explanation}")
                
                accept = input("\n  Accept? [Y/n]: ").strip().lower()
                if accept in ('', 'y', 'yes'):
                    conflict.resolution = resolution
                    conflict.explanation = explanation
                else:
                    conflict.resolution = None
            elif choice == 'e':
                print("  Opening in editor...")
                # Could integrate with VS Code here
                conflict.resolution = None
            else:
                conflict.resolution = None
        
        # Apply resolutions
        resolved = [c for c in conflict_file.conflicts if c.resolution is not None]
        if resolved:
            resolve_file(conflict_file, auto_resolve=False, use_ai=False)
            
            confirm = input(f"\n  💾 Save resolved file? [Y/n]: ").strip().lower()
            if confirm in ('', 'y', 'yes'):
                write_resolved_file(conflict_file)
                print(f"  ✅ Saved {file_path}")
                
                # Stage file
                stage = input("  📤 Stage for commit? [Y/n]: ").strip().lower()
                if stage in ('', 'y', 'yes'):
                    subprocess.run(['git', 'add', file_path])
                    print(f"  ✅ Staged {file_path}")

# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='AI Merge Conflict Resolver')
    parser.add_argument('--auto', '-a', action='store_true', help='Auto-resolve high-confidence conflicts')
    parser.add_argument('--no-ai', action='store_true', help='Skip AI resolution')
    parser.add_argument('--file', '-f', help='Resolve specific file')
    parser.add_argument('--dry-run', '-n', action='store_true', help='Show resolutions without saving')
    
    args = parser.parse_args()
    
    if args.file:
        conflict_file = parse_conflicts(args.file)
        if conflict_file.conflicts:
            resolve_file(conflict_file, auto_resolve=args.auto, use_ai=not args.no_ai)
            
            if args.dry_run:
                print(conflict_file.resolved_content)
            else:
                write_resolved_file(conflict_file)
                print(f"✅ Resolved {args.file}")
        else:
            print(f"No conflicts in {args.file}")
    elif args.auto:
        # Auto mode
        conflicted = get_conflicted_files()
        for file_path in conflicted:
            conflict_file = parse_conflicts(file_path)
            if conflict_file.conflicts:
                resolve_file(conflict_file, auto_resolve=True, use_ai=not args.no_ai)
                
                if not args.dry_run:
                    write_resolved_file(conflict_file)
                    subprocess.run(['git', 'add', file_path])
                    print(f"✅ Resolved and staged: {file_path}")
                else:
                    print(f"Would resolve: {file_path}")
    else:
        interactive_resolve()

if __name__ == '__main__':
    main()
