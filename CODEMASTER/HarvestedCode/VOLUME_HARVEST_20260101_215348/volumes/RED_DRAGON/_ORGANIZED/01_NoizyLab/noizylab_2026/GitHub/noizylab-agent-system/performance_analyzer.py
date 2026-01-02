#!/usr/bin/env python3
"""
Agent Performance Analyzer
Analyzes agent performance and provides optimization suggestions
"""
import time
from datetime import datetime
from typing import Dict, Any, List
from agent_core import coordinator

class PerformanceAnalyzer:
    """Analyzes agent fleet performance"""
    
    def __init__(self):
        self.snapshots = []
    
    def take_snapshot(self) -> Dict[str, Any]:
        """Take a performance snapshot"""
        status = coordinator.get_fleet_status()
        
        snapshot = {
            "timestamp": time.time(),
            "datetime": datetime.now().isoformat(),
            "agents": {},
            "totals": {
                "total_tasks": status['coordinator_metrics']['total_tasks'],
                "completed": status['coordinator_metrics']['completed_tasks'],
                "failed": status['coordinator_metrics']['failed_tasks']
            }
        }
        
        for agent_id, agent_status in status['agents'].items():
            snapshot['agents'][agent_id] = {
                "status": agent_status['status'],
                "queue_size": agent_status['queue_size'],
                "completed": agent_status['metrics']['tasks_completed'],
                "failed": agent_status['metrics']['tasks_failed'],
                "avg_time": agent_status['metrics']['avg_task_time']
            }
        
        self.snapshots.append(snapshot)
        return snapshot
    
    def analyze(self) -> Dict[str, Any]:
        """Analyze performance data"""
        if len(self.snapshots) < 2:
            return {"error": "Need at least 2 snapshots for analysis"}
        
        first = self.snapshots[0]
        last = self.snapshots[-1]
        duration = last['timestamp'] - first['timestamp']
        
        analysis = {
            "duration_seconds": duration,
            "duration_formatted": f"{int(duration // 60)}m {int(duration % 60)}s",
            "task_throughput": {},
            "agent_utilization": {},
            "bottlenecks": [],
            "recommendations": []
        }
        
        # Calculate throughput per agent
        for agent_id in last['agents'].keys():
            if agent_id in first['agents']:
                completed_delta = (
                    last['agents'][agent_id]['completed'] - 
                    first['agents'][agent_id]['completed']
                )
                
                if duration > 0:
                    throughput = completed_delta / duration
                    analysis['task_throughput'][agent_id] = {
                        "tasks_completed": completed_delta,
                        "tasks_per_second": round(throughput, 3),
                        "avg_task_time": last['agents'][agent_id]['avg_time']
                    }
                
                # Check for bottlenecks
                if last['agents'][agent_id]['queue_size'] > 10:
                    analysis['bottlenecks'].append({
                        "agent": agent_id,
                        "issue": "high_queue_size",
                        "queue": last['agents'][agent_id]['queue_size']
                    })
                
                # Check for slow agents
                if last['agents'][agent_id]['avg_time'] > 5.0:
                    analysis['bottlenecks'].append({
                        "agent": agent_id,
                        "issue": "slow_processing",
                        "avg_time": last['agents'][agent_id]['avg_time']
                    })
        
        # Generate recommendations
        if analysis['bottlenecks']:
            analysis['recommendations'].append(
                "Consider adding more agents for overloaded capabilities"
            )
        
        total_completed = last['totals']['completed']
        total_failed = last['totals']['failed']
        
        if total_failed > 0 and total_completed > 0:
            failure_rate = total_failed / (total_completed + total_failed)
            if failure_rate > 0.1:
                analysis['recommendations'].append(
                    f"High failure rate ({failure_rate:.1%}). Review error logs."
                )
        
        return analysis
    
    def print_report(self):
        """Print a formatted performance report"""
        analysis = self.analyze()
        
        if "error" in analysis:
            print(f"⚠️  {analysis['error']}")
            return
        
        print("\n" + "=" * 70)
        print("📊 AGENT FLEET PERFORMANCE REPORT")
        print("=" * 70)
        print(f"Analysis Period: {analysis['duration_formatted']}")
        print()
        
        print("Task Throughput by Agent:")
        print("-" * 70)
        for agent_id, data in analysis['task_throughput'].items():
            print(f"  {agent_id}:")
            print(f"    • Tasks Completed: {data['tasks_completed']}")
            print(f"    • Throughput: {data['tasks_per_second']:.3f} tasks/sec")
            print(f"    • Avg Task Time: {data['avg_task_time']:.2f}s")
            print()
        
        if analysis['bottlenecks']:
            print("⚠️  Bottlenecks Detected:")
            print("-" * 70)
            for bottleneck in analysis['bottlenecks']:
                print(f"  • {bottleneck['agent']}: {bottleneck['issue']}")
                if 'queue' in bottleneck:
                    print(f"    Queue size: {bottleneck['queue']}")
                if 'avg_time' in bottleneck:
                    print(f"    Avg time: {bottleneck['avg_time']:.2f}s")
            print()
        
        if analysis['recommendations']:
            print("💡 Recommendations:")
            print("-" * 70)
            for i, rec in enumerate(analysis['recommendations'], 1):
                print(f"  {i}. {rec}")
            print()
        
        print("=" * 70 + "\n")

# Example usage
if __name__ == "__main__":
    analyzer = PerformanceAnalyzer()
    
    # Take initial snapshot
    print("📸 Taking initial snapshot...")
    analyzer.take_snapshot()
    
    # Simulate some work
    import time
    print("⏳ Simulating 10 seconds of work...")
    time.sleep(10)
    
    # Take final snapshot
    print("📸 Taking final snapshot...")
    analyzer.take_snapshot()
    
    # Print report
    analyzer.print_report()
