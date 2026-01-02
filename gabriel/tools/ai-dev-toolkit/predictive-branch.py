#!/usr/bin/env python3
"""
🌿 AI-Powered Predictive Branching Strategy
Part of GABRIEL AI Dev Toolkit

Analyzes repository and suggests optimal branching strategies:
- Feature branch naming conventions
- Release branch planning
- Hotfix prioritization
- Branch lifecycle management
- Merge strategy recommendations
"""

import argparse
import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class PredictiveBranchingEngine:
    """AI-powered branch strategy advisor."""
    
    BRANCH_PATTERNS = {
        'feature': 'feature/{issue}-{description}',
        'bugfix': 'bugfix/{issue}-{description}',
        'hotfix': 'hotfix/{version}-{description}',
        'release': 'release/{version}',
        'experiment': 'experiment/{user}-{description}',
        'refactor': 'refactor/{scope}-{description}',
        'docs': 'docs/{description}',
        'test': 'test/{scope}-{description}'
    }
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        
    def _run_git(self, *args) -> str:
        """Run a git command and return output."""
        try:
            result = subprocess.run(
                ['git', '-C', str(self.repo_path)] + list(args),
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Error: {e}"
    
    def get_branch_context(self) -> Dict[str, Any]:
        """Gather comprehensive branch context."""
        context = {}
        
        # Current branch
        context['current_branch'] = self._run_git('branch', '--show-current')
        
        # All branches
        branches_raw = self._run_git('branch', '-a', '--format=%(refname:short)')
        context['all_branches'] = [b.strip() for b in branches_raw.split('\n') if b.strip()]
        
        # Recent branch activity
        context['recent_branches'] = self._run_git(
            'for-each-ref', '--sort=-committerdate', 
            '--format=%(refname:short)|%(committerdate:relative)|%(authorname)',
            'refs/heads/', '--count=20'
        ).split('\n')
        
        # Branch merge history
        context['merge_commits'] = self._run_git(
            'log', '--oneline', '--merges', '-20'
        ).split('\n')
        
        # Open PRs (if gh cli available)
        try:
            prs_result = subprocess.run(
                ['gh', 'pr', 'list', '--json', 'number,title,headRefName,baseRefName'],
                capture_output=True, text=True, timeout=10,
                cwd=str(self.repo_path)
            )
            if prs_result.returncode == 0:
                context['open_prs'] = json.loads(prs_result.stdout)
            else:
                context['open_prs'] = []
        except Exception:
            context['open_prs'] = []
            
        # Tags/releases
        context['recent_tags'] = self._run_git(
            'tag', '--sort=-creatordate', '-l', '-n1'
        ).split('\n')[:10]
        
        # Uncommitted changes
        context['working_tree_status'] = self._run_git('status', '--short')
        
        # Stashes
        context['stash_list'] = self._run_git('stash', 'list').split('\n')
        
        # Remote info
        context['remotes'] = self._run_git('remote', '-v').split('\n')
        
        # Recent commit authors (team size indicator)
        authors = self._run_git('log', '--format=%an', '-100')
        context['unique_authors'] = list(set(authors.split('\n')))
        
        return context
    
    def analyze_branch_health(self) -> Dict[str, Any]:
        """Analyze health of existing branches."""
        branches = self._run_git('branch', '-a', '--format=%(refname:short)').split('\n')
        
        health_report = {
            'stale_branches': [],
            'orphaned_branches': [],
            'naming_violations': [],
            'merge_candidates': [],
            'branch_stats': {}
        }
        
        for branch in branches:
            branch = branch.strip()
            if not branch or 'origin/HEAD' in branch:
                continue
                
            # Check age
            last_commit = self._run_git(
                'log', '-1', '--format=%cr|%H', branch
            )
            
            if last_commit:
                parts = last_commit.split('|')
                age_str = parts[0] if parts else ''
                
                # Detect stale (>30 days)
                if any(x in age_str for x in ['month', 'year']) or \
                   ('weeks' in age_str and int(age_str.split()[0]) > 4):
                    health_report['stale_branches'].append({
                        'branch': branch,
                        'last_activity': age_str
                    })
                    
            # Check naming convention
            if not any(branch.startswith(prefix) for prefix in 
                      ['feature/', 'bugfix/', 'hotfix/', 'release/', 'main', 'master', 'develop']):
                if branch not in ['main', 'master', 'develop'] and not branch.startswith('origin/'):
                    health_report['naming_violations'].append(branch)
                    
            # Check if merged but not deleted
            merged_to_main = self._run_git(
                'branch', '-a', '--merged', 'main'
            ).split('\n')
            
            if branch in [b.strip() for b in merged_to_main]:
                if branch not in ['main', 'master', 'develop']:
                    health_report['merge_candidates'].append(branch)
                    
        health_report['branch_stats'] = {
            'total_branches': len(branches),
            'stale_count': len(health_report['stale_branches']),
            'naming_issues': len(health_report['naming_violations']),
            'cleanup_candidates': len(health_report['merge_candidates'])
        }
        
        return health_report
    
    def suggest_branch_name(self, description: str, branch_type: str = 'feature') -> Dict[str, Any]:
        """Suggest optimal branch name based on description."""
        context = self.get_branch_context()
        
        prompt = f"""Based on the following context, suggest the optimal branch name.

Current Branches:
{json.dumps(context['all_branches'][:20], indent=2)}

Branch Naming Patterns Used:
{json.dumps(self.BRANCH_PATTERNS, indent=2)}

Request:
- Description: {description}
- Branch Type: {branch_type}

Provide suggestions in JSON format:
{{
  "recommended_name": "the best branch name",
  "alternatives": ["alt1", "alt2"],
  "naming_reasoning": "why this name",
  "related_branches": ["existing branches that might be related"],
  "suggested_base_branch": "which branch to branch from",
  "workflow_tips": ["tips for working on this branch"]
}}

Follow conventions: lowercase, hyphens for spaces, include issue numbers if available."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = response.content[0].text
            
            if '```json' in response_text:
                json_str = response_text.split('```json')[1].split('```')[0]
            elif '```' in response_text:
                json_str = response_text.split('```')[1].split('```')[0]
            else:
                json_str = response_text
                
            return json.loads(json_str.strip())
            
        except Exception as e:
            return {
                'recommended_name': f"{branch_type}/{description.lower().replace(' ', '-')}",
                'error': str(e)
            }
    
    def predict_release_strategy(self) -> Dict[str, Any]:
        """Predict optimal release branching strategy."""
        context = self.get_branch_context()
        health = self.analyze_branch_health()
        
        prompt = f"""Analyze this repository and recommend a release branching strategy.

Repository Context:
- Current Branch: {context['current_branch']}
- Total Branches: {len(context['all_branches'])}
- Recent Tags: {context['recent_tags'][:5]}
- Team Size (estimated): {len(context['unique_authors'])} contributors
- Open PRs: {len(context.get('open_prs', []))}
- Stale Branches: {health['branch_stats']['stale_count']}

Recent Merge Activity:
{chr(10).join(context['merge_commits'][:10])}

Provide strategy in JSON format:
{{
  "recommended_workflow": "gitflow/github-flow/gitlab-flow/trunk-based",
  "workflow_reasoning": "why this workflow fits",
  "branch_structure": {{
    "main_branch": "name and purpose",
    "development_branch": "name and purpose if applicable",
    "release_branches": "strategy",
    "feature_branches": "naming and lifecycle",
    "hotfix_branches": "strategy"
  }},
  "release_schedule_suggestion": "based on activity patterns",
  "cleanup_recommendations": [
    "specific branch cleanup suggestions"
  ],
  "pr_strategy": "how to handle PRs",
  "ci_cd_suggestions": "CI/CD branch triggers",
  "immediate_actions": [
    "prioritized list of actions to take now"
  ]
}}

Be specific and actionable based on the actual repository state."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2048,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = response.content[0].text
            
            if '```json' in response_text:
                json_str = response_text.split('```json')[1].split('```')[0]
            elif '```' in response_text:
                json_str = response_text.split('```')[1].split('```')[0]
            else:
                json_str = response_text
                
            return json.loads(json_str.strip())
            
        except Exception as e:
            return {
                'recommended_workflow': 'Unable to analyze',
                'error': str(e)
            }
    
    def get_next_branch_suggestions(self) -> List[Dict[str, Any]]:
        """Suggest what branches should be created next."""
        context = self.get_branch_context()
        
        prompt = f"""Based on this repository's state, suggest what branches should be created next.

Current Branch: {context['current_branch']}
Working Tree Changes: {context['working_tree_status'][:500] if context['working_tree_status'] else 'Clean'}
Stashed Changes: {len([s for s in context['stash_list'] if s])}
Open PRs: {json.dumps(context.get('open_prs', [])[:5], indent=2)}

Recent Branches:
{chr(10).join(context['recent_branches'][:10])}

Provide suggestions in JSON format:
{{
  "suggestions": [
    {{
      "branch_name": "suggested name",
      "branch_type": "feature/bugfix/release/etc",
      "reason": "why create this",
      "priority": "high/medium/low",
      "base_branch": "branch from",
      "estimated_scope": "small/medium/large"
    }}
  ],
  "immediate_recommendation": "what to do right now",
  "workflow_state": "assessment of current workflow state"
}}"""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = response.content[0].text
            
            if '```json' in response_text:
                json_str = response_text.split('```json')[1].split('```')[0]
            elif '```' in response_text:
                json_str = response_text.split('```')[1].split('```')[0]
            else:
                json_str = response_text
                
            return json.loads(json_str.strip())
            
        except Exception as e:
            return {'error': str(e)}
    
    def generate_report(self) -> str:
        """Generate comprehensive branching strategy report."""
        report = []
        report.append("=" * 70)
        report.append("🌿 PREDICTIVE BRANCHING STRATEGY REPORT")
        report.append(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        # Current state
        context = self.get_branch_context()
        report.append("📊 REPOSITORY STATE")
        report.append("-" * 40)
        report.append(f"  Current Branch: {context['current_branch']}")
        report.append(f"  Total Branches: {len(context['all_branches'])}")
        report.append(f"  Team Members: ~{len(context['unique_authors'])}")
        report.append(f"  Open PRs: {len(context.get('open_prs', []))}")
        report.append("")
        
        # Branch health
        health = self.analyze_branch_health()
        report.append("🏥 BRANCH HEALTH")
        report.append("-" * 40)
        report.append(f"  Stale Branches: {health['branch_stats']['stale_count']}")
        report.append(f"  Naming Issues: {health['branch_stats']['naming_issues']}")
        report.append(f"  Cleanup Candidates: {health['branch_stats']['cleanup_candidates']}")
        report.append("")
        
        if health['stale_branches']:
            report.append("  📦 Stale Branches (consider cleanup):")
            for sb in health['stale_branches'][:5]:
                report.append(f"    - {sb['branch']} ({sb['last_activity']})")
            report.append("")
            
        if health['naming_violations']:
            report.append("  ⚠️ Naming Convention Violations:")
            for nv in health['naming_violations'][:5]:
                report.append(f"    - {nv}")
            report.append("")
            
        # Release strategy
        print("🔍 Analyzing release strategy...")
        strategy = self.predict_release_strategy()
        
        report.append("🚀 RECOMMENDED WORKFLOW")
        report.append("-" * 40)
        report.append(f"  Strategy: {strategy.get('recommended_workflow', 'N/A')}")
        report.append(f"  Reasoning: {strategy.get('workflow_reasoning', 'N/A')}")
        report.append("")
        
        if 'branch_structure' in strategy:
            report.append("  📁 Branch Structure:")
            for key, value in strategy['branch_structure'].items():
                report.append(f"    {key}: {value}")
            report.append("")
            
        if 'immediate_actions' in strategy:
            report.append("  ⚡ Immediate Actions:")
            for action in strategy['immediate_actions']:
                report.append(f"    → {action}")
            report.append("")
            
        # Next branch suggestions
        print("🔮 Predicting next branches...")
        suggestions = self.get_next_branch_suggestions()
        
        if 'suggestions' in suggestions:
            report.append("🌱 SUGGESTED NEXT BRANCHES")
            report.append("-" * 40)
            for sug in suggestions['suggestions'][:5]:
                priority_icon = '🔴' if sug.get('priority') == 'high' else '🟡' if sug.get('priority') == 'medium' else '🟢'
                report.append(f"  {priority_icon} {sug.get('branch_name', 'N/A')}")
                report.append(f"      Type: {sug.get('branch_type', 'N/A')}")
                report.append(f"      Reason: {sug.get('reason', 'N/A')}")
                report.append("")
                
        if 'immediate_recommendation' in suggestions:
            report.append(f"💡 {suggestions['immediate_recommendation']}")
            report.append("")
            
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='🌿 AI-Powered Predictive Branching Strategy',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           Full branching analysis
  %(prog)s --suggest "user login"    Suggest branch name
  %(prog)s --health                  Branch health check only
  %(prog)s --json                    Output as JSON
        """
    )
    
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    parser.add_argument('--suggest', '-s', help='Suggest branch name for description')
    parser.add_argument('--type', '-t', default='feature', help='Branch type for suggestion')
    parser.add_argument('--health', action='store_true', help='Health check only')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    # Check API key
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    engine = PredictiveBranchingEngine(args.path)
    
    if args.suggest:
        print(f"🌿 Suggesting branch name for: {args.suggest}")
        suggestion = engine.suggest_branch_name(args.suggest, args.type)
        
        if args.json:
            print(json.dumps(suggestion, indent=2))
        else:
            print(f"\n📌 Recommended: {suggestion.get('recommended_name', 'N/A')}")
            print(f"📝 Reasoning: {suggestion.get('naming_reasoning', 'N/A')}")
            if suggestion.get('alternatives'):
                print(f"🔄 Alternatives: {', '.join(suggestion['alternatives'])}")
            print(f"📍 Base Branch: {suggestion.get('suggested_base_branch', 'main')}")
            
    elif args.health:
        print("🏥 Checking branch health...")
        health = engine.analyze_branch_health()
        
        if args.json:
            print(json.dumps(health, indent=2))
        else:
            print(f"\n📊 Total Branches: {health['branch_stats']['total_branches']}")
            print(f"📦 Stale: {health['branch_stats']['stale_count']}")
            print(f"⚠️ Naming Issues: {health['branch_stats']['naming_issues']}")
            print(f"🧹 Cleanup Candidates: {health['branch_stats']['cleanup_candidates']}")
            
    else:
        print("🌿 Generating branching strategy report...")
        report = engine.generate_report()
        print(report)


if __name__ == '__main__':
    main()
