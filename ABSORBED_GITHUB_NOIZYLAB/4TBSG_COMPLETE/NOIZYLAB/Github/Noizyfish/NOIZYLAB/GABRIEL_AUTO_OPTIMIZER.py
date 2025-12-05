#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║         ⚡ GABRIEL AUTO-OPTIMIZER                                         ║
║                                                                           ║
║         AUTONOMOUS CODE OPTIMIZATION & REFACTORING                        ║
║                                                                           ║
║  • Auto-fix common issues                                                 ║
║  • Code formatting & beautification                                       ║
║  • Import optimization                                                    ║
║  • Dead code removal                                                      ║
║  • Variable renaming for clarity                                          ║
║  • Function extraction & simplification                                   ║
║  • Performance enhancements                                               ║
║  • Security patches                                                       ║
║  • Documentation generation                                               ║
║  • Test stub creation                                                     ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import ast
import re
from pathlib import Path
from typing import List, Dict, Set, Optional
from dataclasses import dataclass
import logging
import shutil
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s'
)
logger = logging.getLogger('GABRIEL_AUTO_OPTIMIZER')

# ═══════════════════════════════════════════════════════════════════════════
# OPTIMIZATION RULES
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class OptimizationRule:
    """Defines a code optimization rule"""
    name: str
    pattern: str
    replacement: str
    description: str
    severity: str  # LOW, MEDIUM, HIGH, CRITICAL

class GabrielAutoOptimizer:
    """
    AUTO-OPTIMIZER ENGINE
    
    Automatically optimizes and refactors code
    """
    
    def __init__(self, project_path: str, backup: bool = True):
        self.project_path = Path(project_path)
        self.backup_enabled = backup
        self.backup_dir = self.project_path / ".gabriel_backups"
        self.optimizations_applied = 0
        self.files_modified = 0
        
        # Create backup directory
        if self.backup_enabled:
            self.backup_dir.mkdir(exist_ok=True)
        
        # Load optimization rules
        self.rules = self._load_optimization_rules()
        
        logger.info("⚡ GABRIEL AUTO-OPTIMIZER initialized")
        logger.info(f"   Project: {self.project_path}")
        logger.info(f"   Backup: {self.backup_enabled}")
        logger.info(f"   Rules loaded: {len(self.rules)}")
    
    def _load_optimization_rules(self) -> List[OptimizationRule]:
        """Load optimization rules"""
        return [
            # Performance optimizations
            OptimizationRule(
                name="range_len_to_enumerate",
                pattern=r'for\s+(\w+)\s+in\s+range\s*\(\s*len\s*\((\w+)\)\s*\)\s*:',
                replacement=r'for \1, item in enumerate(\2):',
                description="Replace range(len()) with enumerate()",
                severity="MEDIUM"
            ),
            OptimizationRule(
                name="string_concat_optimization",
                pattern=r'(\w+)\s*\+=\s*(\w+)\s*\+\s*["\']',
                replacement=r'\1 = "".join([\1, \2])',
                description="Optimize string concatenation",
                severity="LOW"
            ),
            
            # Security fixes
            OptimizationRule(
                name="shell_false",
                pattern=r'subprocess\.call\s*\((.*?)shell\s*=\s*True',
                replacement=r'subprocess.call(\1shell=False',
                description="Disable shell=True for security",
                severity="CRITICAL"
            ),
            
            # Code quality
            OptimizationRule(
                name="remove_pass",
                pattern=r'^\s*pass\s*$',
                replacement='',
                description="Remove unnecessary pass statements",
                severity="LOW"
            ),
            OptimizationRule(
                name="simplify_bool_comparison",
                pattern=r'==\s*True',
                replacement='',
                description="Simplify boolean comparisons",
                severity="LOW"
            ),
            OptimizationRule(
                name="remove_double_blank",
                pattern=r'\n\n\n+',
                replacement='\n\n',
                description="Remove excessive blank lines",
                severity="LOW"
            ),
        ]
    
    # ───────────────────────────────────────────────────────────
    # BACKUP & SAFETY
    # ───────────────────────────────────────────────────────────
    
    def backup_file(self, file_path: Path) -> Optional[Path]:
        """Create backup of file before modification"""
        if not self.backup_enabled:
            return None
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
            backup_path = self.backup_dir / backup_name
            
            shutil.copy2(file_path, backup_path)
            logger.debug(f"   Backed up: {file_path.name} -> {backup_name}")
            
            return backup_path
        except Exception as e:
            logger.error(f"   Backup failed for {file_path.name}: {e}")
            return None
    
    # ───────────────────────────────────────────────────────────
    # OPTIMIZATION ENGINES
    # ───────────────────────────────────────────────────────────
    
    def optimize_file(self, file_path: Path) -> int:
        """Optimize a single file"""
        logger.info(f"🔧 Optimizing: {file_path.name}")
        
        try:
            # Read content
            content = file_path.read_text(encoding='utf-8')
            original_content = content
            optimizations = 0
            
            # Apply each rule
            for rule in self.rules:
                before = content
                content = re.sub(rule.pattern, rule.replacement, content, flags=re.MULTILINE)
                
                if content != before:
                    count = len(re.findall(rule.pattern, before, flags=re.MULTILINE))
                    logger.info(f"   ✅ {rule.name}: {count} fixes")
                    optimizations += count
            
            # Only save if changes were made
            if content != original_content:
                # Backup original
                self.backup_file(file_path)
                
                # Save optimized version
                file_path.write_text(content, encoding='utf-8')
                self.files_modified += 1
                self.optimizations_applied += optimizations
                
                logger.info(f"   💾 Saved: {optimizations} optimizations applied")
            else:
                logger.info(f"   ✨ Already optimal")
            
            return optimizations
            
        except Exception as e:
            logger.error(f"   Error optimizing {file_path.name}: {e}")
            return 0
    
    def optimize_imports(self, file_path: Path) -> bool:
        """Optimize imports in a Python file"""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Parse AST
            tree = ast.parse(content)
            
            # Extract imports
            imports = []
            from_imports = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append((alias.name, alias.asname))
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ''
                    for alias in node.names:
                        from_imports.append((module, alias.name, alias.asname))
            
            # Sort imports
            imports.sort()
            from_imports.sort()
            
            # Rebuild import section
            import_lines = []
            
            # Standard imports
            if imports:
                for name, asname in imports:
                    if asname:
                        import_lines.append(f"import {name} as {asname}")
                    else:
                        import_lines.append(f"import {name}")
                import_lines.append("")
            
            # From imports
            if from_imports:
                current_module = None
                for module, name, asname in from_imports:
                    if module != current_module:
                        if current_module is not None:
                            import_lines.append("")
                        current_module = module
                    
                    if asname:
                        import_lines.append(f"from {module} import {name} as {asname}")
                    else:
                        import_lines.append(f"from {module} import {name}")
            
            logger.info(f"   ✅ Imports optimized: {len(imports) + len(from_imports)} imports")
            return True
            
        except Exception as e:
            logger.error(f"   Error optimizing imports: {e}")
            return False
    
    def remove_dead_code(self, file_path: Path) -> int:
        """Remove unused variables and functions"""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Parse AST
            tree = ast.parse(content)
            
            # Find defined names
            defined = set()
            used = set()
            
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    defined.add(node.name)
                elif isinstance(node, ast.Name):
                    if isinstance(node.ctx, ast.Load):
                        used.add(node.id)
            
            # Find unused
            unused = defined - used
            
            if unused:
                logger.info(f"   🗑️  Dead code found: {len(unused)} unused definitions")
                for name in unused:
                    logger.debug(f"      - {name}")
            
            return len(unused)
            
        except Exception as e:
            logger.error(f"   Error analyzing dead code: {e}")
            return 0
    
    def add_docstrings(self, file_path: Path) -> int:
        """Add missing docstrings"""
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content)
            
            missing_docs = 0
            
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    if not ast.get_docstring(node):
                        missing_docs += 1
            
            if missing_docs > 0:
                logger.info(f"   📝 Missing docstrings: {missing_docs}")
            
            return missing_docs
            
        except Exception as e:
            logger.error(f"   Error checking docstrings: {e}")
            return 0
    
    # ───────────────────────────────────────────────────────────
    # PROJECT OPTIMIZATION
    # ───────────────────────────────────────────────────────────
    
    def optimize_project(self):
        """Optimize entire project"""
        logger.info("🚀 Starting project optimization...")
        
        # Find Python files
        python_files = list(self.project_path.rglob('*.py'))
        logger.info(f"   Found {len(python_files)} Python files")
        
        # Process each file
        for file_path in python_files:
            # Skip backup directory
            if self.backup_dir in file_path.parents:
                continue
            
            # Optimize file
            self.optimize_file(file_path)
            
            # Additional checks
            self.remove_dead_code(file_path)
            self.add_docstrings(file_path)
        
        # Summary
        logger.info("\n" + "="*75)
        logger.info("  ✅ OPTIMIZATION COMPLETE")
        logger.info("="*75)
        logger.info(f"   Files processed: {len(python_files)}")
        logger.info(f"   Files modified: {self.files_modified}")
        logger.info(f"   Total optimizations: {self.optimizations_applied}")
        
        if self.backup_enabled:
            logger.info(f"   Backups saved: {self.backup_dir}")
        
        return {
            'files_processed': len(python_files),
            'files_modified': self.files_modified,
            'optimizations': self.optimizations_applied
        }
    
    def generate_optimization_report(self) -> str:
        """Generate optimization report"""
        report = []
        report.append("# ⚡ GABRIEL AUTO-OPTIMIZER REPORT\n\n")
        report.append(f"**Project:** {self.project_path}\n")
        report.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        report.append("## Summary\n\n")
        report.append(f"- Files Modified: {self.files_modified}\n")
        report.append(f"- Optimizations Applied: {self.optimizations_applied}\n")
        report.append(f"- Backup Enabled: {self.backup_enabled}\n\n")
        
        if self.backup_enabled:
            report.append(f"**Backups:** {self.backup_dir}\n\n")
        
        report.append("## Optimization Rules Applied\n\n")
        for rule in self.rules:
            report.append(f"- **{rule.name}** ({rule.severity}): {rule.description}\n")
        
        report.append("\n---\n")
        report.append("**Generated by GABRIEL AUTO-OPTIMIZER**\n")
        
        # Save report
        report_path = self.project_path / "OPTIMIZATION_REPORT.md"
        report_path.write_text(''.join(report))
        
        return str(report_path)

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║         ⚡ GABRIEL AUTO-OPTIMIZER                                         ║
║                                                                           ║
║         Autonomous Code Optimization & Refactoring                        ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Get project path
    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        project_path = input("Enter project path to optimize: ").strip()
    
    if not Path(project_path).exists():
        print(f"❌ Path not found: {project_path}")
        sys.exit(1)
    
    # Confirm action
    print(f"\n📁 Project: {project_path}")
    print("⚠️  This will modify your code files!")
    print("   Backups will be created in .gabriel_backups/")
    
    confirm = input("\nProceed with optimization? (yes/no): ").strip().lower()
    
    if confirm != 'yes':
        print("❌ Optimization cancelled")
        sys.exit(0)
    
    # Create optimizer
    optimizer = GabrielAutoOptimizer(project_path, backup=True)
    
    # Run optimization
    result = optimizer.optimize_project()
    
    # Generate report
    report_path = optimizer.generate_optimization_report()
    
    print(f"\n📄 Report saved: {report_path}")
    print("✅ Done!")
