#!/usr/bin/env python3
"""
Intelligent Log Analyzer
=========================
AI-powered log analysis to find issues instantly
"""

import re
from datetime import datetime
from typing import List, Dict
from pathlib import Path
import requests
import os


class IntelligentLogAnalyzer:
    """AI analyzes logs to find problems instantly"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.patterns = self._load_error_patterns()
        
    def _load_error_patterns(self) -> Dict:
        """Common error patterns"""
        return {
            "critical_errors": [
                r"CRITICAL",
                r"FATAL",
                r"Traceback",
                r"Exception",
                r"Error:",
                r"Failed to",
                r"Cannot",
                r"Timeout"
            ],
            "warnings": [
                r"WARNING",
                r"WARN",
                r"deprecated",
                r"slow query",
                r"retry"
            ],
            "performance": [
                r"took (\d+)ms",
                r"duration: (\d+)",
                r"slow",
                r"timeout"
            ]
        }
    
    def analyze_logs(self, log_file: str, lines: int = 1000) -> Dict:
        """
        Analyze log file with AI
        
        Returns:
            Analysis with issues found and recommendations
        """
        logs = self._read_logs(log_file, lines)
        
        # Quick pattern matching first
        issues = self._pattern_match(logs)
        
        # AI deep analysis for complex issues
        if issues["critical_count"] > 0 or issues["error_count"] > 5:
            ai_analysis = self._ai_analyze_logs(logs, issues)
            issues["ai_analysis"] = ai_analysis
        
        return issues
    
    def _read_logs(self, log_file: str, lines: int) -> List[str]:
        """Read last N lines from log file"""
        try:
            with open(log_file, 'r') as f:
                all_lines = f.readlines()
                return all_lines[-lines:]
        except:
            return []
    
    def _pattern_match(self, logs: List[str]) -> Dict:
        """Pattern matching for common issues"""
        issues = {
            "critical_count": 0,
            "error_count": 0,
            "warning_count": 0,
            "critical_issues": [],
            "errors": [],
            "warnings": [],
            "performance_issues": []
        }
        
        for log_line in logs:
            # Critical errors
            for pattern in self.patterns["critical_errors"]:
                if re.search(pattern, log_line, re.IGNORECASE):
                    issues["critical_count"] += 1
                    issues["critical_issues"].append(log_line.strip())
                    break
            
            # Warnings
            for pattern in self.patterns["warnings"]:
                if re.search(pattern, log_line, re.IGNORECASE):
                    issues["warning_count"] += 1
                    if len(issues["warnings"]) < 10:
                        issues["warnings"].append(log_line.strip())
                    break
            
            # Performance issues
            for pattern in self.patterns["performance"]:
                match = re.search(pattern, log_line, re.IGNORECASE):
                if match:
                    issues["performance_issues"].append(log_line.strip())
                    break
        
        # Count errors (not critical)
        issues["error_count"] = len([l for l in logs if "error" in l.lower() and not any(p in l.lower() for p in ["critical", "fatal"])])
        
        return issues
    
    def _ai_analyze_logs(self, logs: List[str], pattern_issues: Dict) -> Dict:
        """AI deep analysis of logs"""
        # Sample logs for AI (don't send everything)
        sample_logs = "\n".join(logs[-50:])  # Last 50 lines
        
        prompt = f"""Analyze these logs and provide insights:

Pattern Analysis Found:
- Critical Issues: {pattern_issues['critical_count']}
- Errors: {pattern_issues['error_count']}
- Warnings: {pattern_issues['warning_count']}

Recent Logs:
{sample_logs}

Provide:
1. Root cause (if identifiable)
2. Severity assessment
3. Immediate actions needed
4. Long-term fixes

Respond in JSON format."""
        
        if not self.api_key:
            return self._rule_based_log_analysis(pattern_issues)
        
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {"role": "system", "content": "You are an expert log analyzer."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": 800,
                    "temperature": 0.3
                },
                timeout=20
            )
            
            if response.status_code == 200:
                import json
                data = response.json()
                return json.loads(data["choices"][0]["message"]["content"])
        except:
            pass
        
        return self._rule_based_log_analysis(pattern_issues)
    
    def _rule_based_log_analysis(self, issues: Dict) -> Dict:
        """Fallback rule-based analysis"""
        if issues["critical_count"] > 0:
            return {
                "root_cause": "Critical errors detected in logs",
                "severity": "High",
                "immediate_actions": [
                    "Review critical error messages",
                    "Check system resources",
                    "Restart affected services if needed"
                ],
                "long_term_fixes": [
                    "Add monitoring for these errors",
                    "Implement error handling",
                    "Review and fix root cause"
                ]
            }
        elif issues["error_count"] > 10:
            return {
                "root_cause": "Multiple errors in logs",
                "severity": "Medium",
                "immediate_actions": [
                    "Review error patterns",
                    "Check for common causes"
                ],
                "long_term_fixes": [
                    "Improve error handling",
                    "Add preventive checks"
                ]
            }
        else:
            return {
                "root_cause": "No significant issues detected",
                "severity": "Low",
                "immediate_actions": [],
                "long_term_fixes": []
            }
    
    def find_anomalies(self, logs: List[str]) -> List[str]:
        """Find anomalous log patterns"""
        # Count message types
        message_counts = {}
        for log in logs:
            # Extract message pattern (remove timestamps, numbers, IDs)
            pattern = re.sub(r'\d{4}-\d{2}-\d{2}', 'DATE', log)
            pattern = re.sub(r'\d+', 'NUM', pattern)
            pattern = re.sub(r'[a-f0-9]{8,}', 'ID', pattern)
            
            message_counts[pattern] = message_counts.get(pattern, 0) + 1
        
        # Find rare messages (potential anomalies)
        total = len(logs)
        anomalies = []
        
        for pattern, count in message_counts.items():
            frequency = count / total
            if frequency < 0.01 and "error" in pattern.lower():  # < 1% and contains error
                anomalies.append(pattern)
        
        return anomalies[:10]  # Top 10 anomalies
    
    def summarize_logs(self, log_file: str, hours: int = 24) -> str:
        """AI-generated log summary"""
        logs = self._read_logs(log_file, 1000)
        
        # Get statistics
        total_lines = len(logs)
        errors = len([l for l in logs if "error" in l.lower()])
        warnings = len([l for l in logs if "warn" in l.lower()])
        
        summary = f"""Log Summary (last {hours} hours):
- Total log lines: {total_lines}
- Errors: {errors}
- Warnings: {warnings}
- Error rate: {errors/total_lines*100:.1f}%

"""
        
        # Get AI summary if available
        if self.api_key and (errors > 0 or warnings > 5):
            sample = "\n".join(logs[-30:])
            
            prompt = f"""Summarize these logs in 2-3 sentences:

{sample}

Focus on what happened and any issues."""
            
            try:
                response = requests.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    json={
                        "model": "gpt-4o-mini",
                        "messages": [{"role": "user", "content": prompt}],
                        "max_tokens": 200
                    },
                    timeout=15
                )
                
                if response.status_code == 200:
                    data = response.json()
                    summary += "AI Summary:\n" + data["choices"][0]["message"]["content"]
            except:
                pass
        
        return summary


# Convenience function
def analyze_logs_now(log_file: str = "/Users/m2ultra/NOIZYLAB/logs/noizylab.log") -> Dict:
    """Quick log analysis"""
    analyzer = IntelligentLogAnalyzer()
    return analyzer.analyze_logs(log_file)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    else:
        log_file = "/Users/m2ultra/NOIZYLAB/logs/noizylab.log"
    
    print(f"🔍 Analyzing {log_file}...\n")
    
    analyzer = IntelligentLogAnalyzer()
    results = analyzer.analyze_logs(log_file)
    
    print(f"📊 Results:")
    print(f"  Critical: {results['critical_count']}")
    print(f"  Errors: {results['error_count']}")
    print(f"  Warnings: {results['warning_count']}")
    
    if results['critical_count'] > 0:
        print(f"\n🚨 Critical Issues:")
        for issue in results['critical_issues'][:5]:
            print(f"  - {issue}")
    
    if "ai_analysis" in results:
        print(f"\n🤖 AI Analysis:")
        ai = results['ai_analysis']
        print(f"  Root Cause: {ai.get('root_cause', 'Unknown')}")
        print(f"  Severity: {ai.get('severity', 'Unknown')}")

