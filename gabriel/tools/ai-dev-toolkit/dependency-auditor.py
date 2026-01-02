#!/usr/bin/env python3
"""
🔒 AI-Powered Dependency Auditor
Part of GABRIEL AI Dev Toolkit

Comprehensive dependency security scanning:
- Vulnerability detection (CVE database)
- License compliance checking
- Update recommendations
- Breaking change warnings
- Migration guides generation
"""

import argparse
import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import urllib.request
import urllib.error

try:
    import anthropic
except ImportError:
    print("❌ Install anthropic: pip install anthropic")
    sys.exit(1)


class DependencyAuditor:
    """AI-powered dependency security and compliance auditor."""
    
    LICENSE_COMPATIBILITY = {
        'permissive': ['MIT', 'Apache-2.0', 'BSD-2-Clause', 'BSD-3-Clause', 'ISC', 'Unlicense'],
        'copyleft': ['GPL-2.0', 'GPL-3.0', 'LGPL-2.1', 'LGPL-3.0', 'AGPL-3.0'],
        'weak_copyleft': ['MPL-2.0', 'EPL-1.0', 'EPL-2.0'],
        'proprietary_risk': ['SSPL-1.0', 'BSL-1.0', 'Elastic-2.0']
    }
    
    def __init__(self, repo_path: str = '.'):
        self.repo_path = Path(repo_path).resolve()
        self.client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        
    def detect_package_manager(self) -> Dict[str, Any]:
        """Detect which package managers are in use."""
        managers = {}
        
        # Node.js
        if (self.repo_path / 'package.json').exists():
            managers['npm'] = {
                'file': 'package.json',
                'lock': 'package-lock.json' if (self.repo_path / 'package-lock.json').exists() else 'yarn.lock' if (self.repo_path / 'yarn.lock').exists() else None
            }
            
        # Python
        if (self.repo_path / 'requirements.txt').exists():
            managers['pip'] = {'file': 'requirements.txt'}
        if (self.repo_path / 'pyproject.toml').exists():
            managers['poetry'] = {'file': 'pyproject.toml'}
        if (self.repo_path / 'Pipfile').exists():
            managers['pipenv'] = {'file': 'Pipfile'}
            
        # Ruby
        if (self.repo_path / 'Gemfile').exists():
            managers['bundler'] = {'file': 'Gemfile'}
            
        # Go
        if (self.repo_path / 'go.mod').exists():
            managers['go'] = {'file': 'go.mod'}
            
        # Rust
        if (self.repo_path / 'Cargo.toml').exists():
            managers['cargo'] = {'file': 'Cargo.toml'}
            
        return managers
    
    def parse_package_json(self) -> Dict[str, Any]:
        """Parse package.json for dependencies."""
        pkg_path = self.repo_path / 'package.json'
        if not pkg_path.exists():
            return {}
            
        try:
            with open(pkg_path) as f:
                pkg = json.load(f)
                
            return {
                'name': pkg.get('name', 'unknown'),
                'version': pkg.get('version', '0.0.0'),
                'dependencies': pkg.get('dependencies', {}),
                'devDependencies': pkg.get('devDependencies', {}),
                'peerDependencies': pkg.get('peerDependencies', {}),
                'license': pkg.get('license', 'UNKNOWN')
            }
        except Exception as e:
            return {'error': str(e)}
    
    def parse_requirements_txt(self) -> List[Dict[str, str]]:
        """Parse requirements.txt for dependencies."""
        req_path = self.repo_path / 'requirements.txt'
        if not req_path.exists():
            return []
            
        deps = []
        try:
            with open(req_path) as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                        
                    # Parse package==version or package>=version etc
                    for sep in ['==', '>=', '<=', '~=', '!=', '<', '>']:
                        if sep in line:
                            name, version = line.split(sep, 1)
                            deps.append({
                                'name': name.strip(),
                                'version': version.strip(),
                                'constraint': sep
                            })
                            break
                    else:
                        deps.append({'name': line, 'version': 'any', 'constraint': None})
                        
        except Exception as e:
            return [{'error': str(e)}]
            
        return deps
    
    def run_npm_audit(self) -> Dict[str, Any]:
        """Run npm audit and parse results."""
        try:
            result = subprocess.run(
                ['npm', 'audit', '--json'],
                capture_output=True, text=True, timeout=120,
                cwd=str(self.repo_path)
            )
            
            if result.stdout:
                return json.loads(result.stdout)
            return {'error': result.stderr}
            
        except subprocess.TimeoutExpired:
            return {'error': 'npm audit timed out'}
        except FileNotFoundError:
            return {'error': 'npm not found'}
        except Exception as e:
            return {'error': str(e)}
    
    def run_pip_audit(self) -> Dict[str, Any]:
        """Run pip-audit if available."""
        try:
            result = subprocess.run(
                ['pip-audit', '--format', 'json'],
                capture_output=True, text=True, timeout=120,
                cwd=str(self.repo_path)
            )
            
            if result.stdout:
                return json.loads(result.stdout)
            return {'vulnerabilities': [], 'note': 'No vulnerabilities found or pip-audit not available'}
            
        except FileNotFoundError:
            # Fallback to safety check
            try:
                result = subprocess.run(
                    ['safety', 'check', '--json'],
                    capture_output=True, text=True, timeout=120,
                    cwd=str(self.repo_path)
                )
                if result.stdout:
                    return json.loads(result.stdout)
            except Exception:
                pass
                
            return {'note': 'Install pip-audit or safety for Python vulnerability scanning'}
        except Exception as e:
            return {'error': str(e)}
    
    def check_outdated_npm(self) -> Dict[str, Any]:
        """Check for outdated npm packages."""
        try:
            result = subprocess.run(
                ['npm', 'outdated', '--json'],
                capture_output=True, text=True, timeout=120,
                cwd=str(self.repo_path)
            )
            
            if result.stdout:
                return json.loads(result.stdout)
            return {}
            
        except Exception as e:
            return {'error': str(e)}
    
    def analyze_licenses(self) -> Dict[str, Any]:
        """Analyze dependency licenses for compliance."""
        managers = self.detect_package_manager()
        license_info = {
            'project_license': 'UNKNOWN',
            'dependencies': [],
            'issues': [],
            'summary': {}
        }
        
        if 'npm' in managers:
            pkg = self.parse_package_json()
            license_info['project_license'] = pkg.get('license', 'UNKNOWN')
            
            # Try to get license info from npm
            try:
                result = subprocess.run(
                    ['npx', 'license-checker', '--json'],
                    capture_output=True, text=True, timeout=60,
                    cwd=str(self.repo_path)
                )
                
                if result.stdout:
                    licenses = json.loads(result.stdout)
                    for pkg_name, info in licenses.items():
                        lic = info.get('licenses', 'UNKNOWN')
                        license_info['dependencies'].append({
                            'package': pkg_name,
                            'license': lic,
                            'category': self._categorize_license(lic)
                        })
            except Exception:
                pass
                
        # Summarize
        categories = {}
        for dep in license_info['dependencies']:
            cat = dep.get('category', 'unknown')
            categories[cat] = categories.get(cat, 0) + 1
            
            # Flag potential issues
            if cat == 'proprietary_risk':
                license_info['issues'].append({
                    'package': dep['package'],
                    'license': dep['license'],
                    'severity': 'high',
                    'issue': 'Potentially problematic license'
                })
            elif cat == 'copyleft' and license_info['project_license'] in self.LICENSE_COMPATIBILITY['permissive']:
                license_info['issues'].append({
                    'package': dep['package'],
                    'license': dep['license'],
                    'severity': 'medium',
                    'issue': 'Copyleft license may conflict with project license'
                })
                
        license_info['summary'] = categories
        
        return license_info
    
    def _categorize_license(self, license_str: str) -> str:
        """Categorize a license string."""
        if not license_str:
            return 'unknown'
            
        license_upper = license_str.upper()
        
        for category, licenses in self.LICENSE_COMPATIBILITY.items():
            for lic in licenses:
                if lic.upper() in license_upper:
                    return category
                    
        return 'other'
    
    def generate_update_plan(self, outdated: Dict) -> Dict[str, Any]:
        """Use AI to generate safe update plan."""
        if not outdated:
            return {'message': 'All dependencies are up to date'}
            
        prompt = f"""Analyze these outdated dependencies and create a safe update plan.

Outdated Packages:
{json.dumps(outdated, indent=2)}

Generate an update plan in JSON format:
{{
  "immediate_updates": [
    {{
      "package": "name",
      "from": "version",
      "to": "version",
      "type": "patch/minor/major",
      "risk": "low/medium/high",
      "breaking_changes": ["list any known breaking changes"],
      "command": "npm update command"
    }}
  ],
  "deferred_updates": [
    {{
      "package": "name",
      "reason": "why to defer",
      "migration_needed": true/false
    }}
  ],
  "update_order": ["recommended order of updates"],
  "test_recommendations": ["what to test after updates"],
  "rollback_plan": "how to rollback if issues"
}}

Prioritize security patches, then minor updates, be cautious with major versions."""

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
            return {'error': str(e)}
    
    def full_audit(self) -> Dict[str, Any]:
        """Run comprehensive dependency audit."""
        print("🔍 Detecting package managers...")
        managers = self.detect_package_manager()
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'managers_detected': list(managers.keys()),
            'vulnerabilities': {},
            'outdated': {},
            'licenses': {},
            'summary': {}
        }
        
        # NPM audit
        if 'npm' in managers:
            print("📦 Running npm audit...")
            results['vulnerabilities']['npm'] = self.run_npm_audit()
            
            print("📦 Checking outdated packages...")
            results['outdated']['npm'] = self.check_outdated_npm()
            
        # Python audit
        if any(m in managers for m in ['pip', 'poetry', 'pipenv']):
            print("🐍 Running Python audit...")
            results['vulnerabilities']['python'] = self.run_pip_audit()
            
        # License check
        print("📜 Analyzing licenses...")
        results['licenses'] = self.analyze_licenses()
        
        # Generate summary
        vuln_count = 0
        for source, data in results['vulnerabilities'].items():
            if isinstance(data, dict):
                if 'vulnerabilities' in data:
                    vuln_count += len(data['vulnerabilities'])
                elif 'metadata' in data and 'vulnerabilities' in data['metadata']:
                    vuln_count += data['metadata']['vulnerabilities'].get('total', 0)
                    
        outdated_count = sum(
            len(v) if isinstance(v, dict) else 0 
            for v in results['outdated'].values()
        )
        
        license_issues = len(results['licenses'].get('issues', []))
        
        results['summary'] = {
            'vulnerabilities_found': vuln_count,
            'outdated_packages': outdated_count,
            'license_issues': license_issues,
            'health_score': max(0, 100 - (vuln_count * 10) - (outdated_count * 2) - (license_issues * 5))
        }
        
        return results
    
    def generate_report(self) -> str:
        """Generate human-readable audit report."""
        results = self.full_audit()
        
        report = []
        report.append("=" * 70)
        report.append("🔒 DEPENDENCY AUDIT REPORT")
        report.append(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        report.append("")
        
        # Summary
        summary = results.get('summary', {})
        health = summary.get('health_score', 0)
        health_icon = '🟢' if health >= 80 else '🟡' if health >= 60 else '🔴'
        
        report.append(f"📊 HEALTH SCORE: {health_icon} {health}/100")
        report.append("-" * 40)
        report.append(f"  🔒 Vulnerabilities: {summary.get('vulnerabilities_found', 0)}")
        report.append(f"  📦 Outdated: {summary.get('outdated_packages', 0)}")
        report.append(f"  📜 License Issues: {summary.get('license_issues', 0)}")
        report.append("")
        
        # Vulnerabilities
        report.append("🔒 SECURITY VULNERABILITIES")
        report.append("-" * 40)
        
        for source, data in results.get('vulnerabilities', {}).items():
            if isinstance(data, dict) and 'vulnerabilities' in data:
                vulns = data['vulnerabilities']
                if isinstance(vulns, dict):
                    for name, info in list(vulns.items())[:10]:
                        sev = info.get('severity', 'unknown')
                        sev_icon = '🔴' if sev in ['critical', 'high'] else '🟡' if sev == 'moderate' else '🟢'
                        report.append(f"  {sev_icon} [{sev.upper()}] {name}")
                        report.append(f"      Via: {info.get('via', 'N/A')}")
                        
        if not any(results.get('vulnerabilities', {}).values()):
            report.append("  ✅ No vulnerabilities detected")
        report.append("")
        
        # Outdated packages
        report.append("📦 OUTDATED PACKAGES")
        report.append("-" * 40)
        
        for source, outdated in results.get('outdated', {}).items():
            if isinstance(outdated, dict):
                for pkg, info in list(outdated.items())[:10]:
                    current = info.get('current', '?')
                    wanted = info.get('wanted', '?')
                    latest = info.get('latest', '?')
                    report.append(f"  • {pkg}: {current} → {latest}")
                    
        if not any(results.get('outdated', {}).values()):
            report.append("  ✅ All packages up to date")
        report.append("")
        
        # License issues
        license_info = results.get('licenses', {})
        if license_info.get('issues'):
            report.append("📜 LICENSE ISSUES")
            report.append("-" * 40)
            
            for issue in license_info['issues'][:10]:
                sev_icon = '🔴' if issue.get('severity') == 'high' else '🟡'
                report.append(f"  {sev_icon} {issue.get('package')}: {issue.get('issue')}")
                report.append(f"      License: {issue.get('license')}")
            report.append("")
            
        # License summary
        if license_info.get('summary'):
            report.append("📜 LICENSE SUMMARY")
            report.append("-" * 40)
            for category, count in license_info['summary'].items():
                report.append(f"  • {category}: {count} packages")
            report.append("")
            
        report.append("=" * 70)
        report.append("💡 Run with --update-plan to generate safe update recommendations")
        report.append("=" * 70)
        
        return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='🔒 AI-Powered Dependency Auditor',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                      Full audit report
  %(prog)s --vulnerabilities    Security scan only
  %(prog)s --licenses           License compliance check
  %(prog)s --update-plan        Generate update plan
  %(prog)s --json               Output as JSON
        """
    )
    
    parser.add_argument('--path', '-p', default='.', help='Project path')
    parser.add_argument('--vulnerabilities', '-v', action='store_true', help='Security scan only')
    parser.add_argument('--licenses', '-l', action='store_true', help='License check only')
    parser.add_argument('--outdated', '-o', action='store_true', help='Outdated packages only')
    parser.add_argument('--update-plan', action='store_true', help='Generate update plan')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--output', help='Save to file')
    
    args = parser.parse_args()
    
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
        
    auditor = DependencyAuditor(args.path)
    
    if args.vulnerabilities:
        print("🔒 Running security scan...")
        managers = auditor.detect_package_manager()
        results = {}
        
        if 'npm' in managers:
            results['npm'] = auditor.run_npm_audit()
        if any(m in managers for m in ['pip', 'poetry', 'pipenv']):
            results['python'] = auditor.run_pip_audit()
            
        output = json.dumps(results, indent=2) if args.json else str(results)
        
    elif args.licenses:
        print("📜 Checking license compliance...")
        results = auditor.analyze_licenses()
        output = json.dumps(results, indent=2) if args.json else str(results)
        
    elif args.outdated:
        print("📦 Checking outdated packages...")
        results = auditor.check_outdated_npm()
        output = json.dumps(results, indent=2) if args.json else str(results)
        
    elif args.update_plan:
        print("📋 Generating update plan...")
        outdated = auditor.check_outdated_npm()
        plan = auditor.generate_update_plan(outdated)
        output = json.dumps(plan, indent=2) if args.json else str(plan)
        
    else:
        if args.json:
            output = json.dumps(auditor.full_audit(), indent=2)
        else:
            output = auditor.generate_report()
            
    if args.output:
        Path(args.output).write_text(output)
        print(f"✅ Saved to {args.output}")
    else:
        print(output)


if __name__ == '__main__':
    main()
