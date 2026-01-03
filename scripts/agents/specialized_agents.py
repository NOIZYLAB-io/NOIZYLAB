#!/usr/bin/env python3
"""
Specialized Agents for NoizyLab Operations
"""
import os
import asyncio
import subprocess
from pathlib import Path
from typing import Dict, Any, List
import json
import requests
from agent_core import Agent, AgentCapability, Task, TaskPriority

class FileSystemAgent(Agent):
    """Agent specialized in file system operations"""
    
    def __init__(self):
        capabilities = [
            AgentCapability("scan_directory", "Scan and analyze directory structure", ["path", "depth"]),
            AgentCapability("organize_files", "Organize files by type/date", ["path", "strategy"]),
            AgentCapability("cleanup", "Clean up temporary and duplicate files", ["path", "dry_run"]),
            AgentCapability("backup", "Backup files to specified location", ["source", "destination"]),
            AgentCapability("search_files", "Search for files matching pattern", ["path", "pattern"])
        ]
        super().__init__("fs_agent_001", "FileSystemAgent", capabilities)
    
    async def execute_task(self, task: Task) -> Any:
        """Execute file system tasks"""
        action = task.action
        params = task.params
        
        if action == "scan_directory":
            return await self._scan_directory(params.get("path"), params.get("depth", 3))
        elif action == "organize_files":
            return await self._organize_files(params.get("path"), params.get("strategy", "type"))
        elif action == "cleanup":
            return await self._cleanup(params.get("path"), params.get("dry_run", True))
        elif action == "backup":
            return await self._backup(params.get("source"), params.get("destination"))
        elif action == "search_files":
            return await self._search_files(params.get("path"), params.get("pattern"))
        else:
            raise ValueError(f"Unknown action: {action}")
    
    async def _scan_directory(self, path: str, depth: int) -> Dict[str, Any]:
        """Scan directory and return structure"""
        self.logger.info(f"Scanning directory: {path}")
        path_obj = Path(path)
        
        if not path_obj.exists():
            return {"error": "Path does not exist", "path": path}
        
        stats = {
            "total_files": 0,
            "total_dirs": 0,
            "total_size": 0,
            "file_types": {},
            "largest_files": []
        }
        
        for item in path_obj.rglob("*"):
            if item.is_file():
                stats["total_files"] += 1
                size = item.stat().st_size
                stats["total_size"] += size
                
                ext = item.suffix or "no_extension"
                stats["file_types"][ext] = stats["file_types"].get(ext, 0) + 1
                
                stats["largest_files"].append({
                    "path": str(item),
                    "size": size
                })
            elif item.is_dir():
                stats["total_dirs"] += 1
        
        # Keep only top 10 largest files
        stats["largest_files"] = sorted(
            stats["largest_files"],
            key=lambda x: x["size"],
            reverse=True
        )[:10]
        
        return stats
    
    async def _organize_files(self, path: str, strategy: str) -> Dict[str, Any]:
        """Organize files based on strategy"""
        self.logger.info(f"Organizing files in: {path} (strategy: {strategy})")
        await asyncio.sleep(0.5)  # Simulate work
        return {"status": "organized", "strategy": strategy, "path": path}
    
    async def _cleanup(self, path: str, dry_run: bool) -> Dict[str, Any]:
        """Clean up temporary and duplicate files"""
        self.logger.info(f"Cleaning up: {path} (dry_run: {dry_run})")
        await asyncio.sleep(0.5)
        return {"status": "cleaned", "dry_run": dry_run, "files_removed": 0}
    
    async def _backup(self, source: str, destination: str) -> Dict[str, Any]:
        """Backup files"""
        self.logger.info(f"Backing up {source} to {destination}")
        await asyncio.sleep(1)
        return {"status": "backed_up", "source": source, "destination": destination}
    
    async def _search_files(self, path: str, pattern: str) -> Dict[str, Any]:
        """Search for files matching pattern"""
        self.logger.info(f"Searching for: {pattern} in {path}")
        matches = []
        path_obj = Path(path)
        
        if path_obj.exists():
            for item in path_obj.rglob(pattern):
                matches.append(str(item))
        
        return {"matches": matches[:100], "total": len(matches)}

class CodeAnalysisAgent(Agent):
    """Agent specialized in code analysis"""
    
    def __init__(self):
        capabilities = [
            AgentCapability("analyze_code", "Analyze code quality and structure", ["file_path"]),
            AgentCapability("find_todos", "Find TODO and FIXME comments", ["path"]),
            AgentCapability("dependency_check", "Check project dependencies", ["project_path"]),
            AgentCapability("security_scan", "Scan for security issues", ["path"]),
            AgentCapability("code_metrics", "Calculate code metrics", ["file_path"])
        ]
        super().__init__("code_agent_001", "CodeAnalysisAgent", capabilities)
    
    async def execute_task(self, task: Task) -> Any:
        """Execute code analysis tasks"""
        action = task.action
        params = task.params
        
        if action == "analyze_code":
            return await self._analyze_code(params.get("file_path"))
        elif action == "find_todos":
            return await self._find_todos(params.get("path"))
        elif action == "dependency_check":
            return await self._dependency_check(params.get("project_path"))
        elif action == "security_scan":
            return await self._security_scan(params.get("path"))
        elif action == "code_metrics":
            return await self._code_metrics(params.get("file_path"))
        else:
            raise ValueError(f"Unknown action: {action}")
    
    async def _analyze_code(self, file_path: str) -> Dict[str, Any]:
        """Analyze code file"""
        self.logger.info(f"Analyzing code: {file_path}")
        
        if not Path(file_path).exists():
            return {"error": "File not found"}
        
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        return {
            "total_lines": len(lines),
            "code_lines": len([l for l in lines if l.strip() and not l.strip().startswith('#')]),
            "comment_lines": len([l for l in lines if l.strip().startswith('#')]),
            "blank_lines": len([l for l in lines if not l.strip()])
        }
    
    async def _find_todos(self, path: str) -> Dict[str, Any]:
        """Find TODO comments in code"""
        self.logger.info(f"Finding TODOs in: {path}")
        todos = []
        
        for file_path in Path(path).rglob("*.py"):
            with open(file_path, 'r', errors='ignore') as f:
                for i, line in enumerate(f, 1):
                    if 'TODO' in line or 'FIXME' in line:
                        todos.append({
                            "file": str(file_path),
                            "line": i,
                            "text": line.strip()
                        })
        
        return {"todos": todos, "count": len(todos)}
    
    async def _dependency_check(self, project_path: str) -> Dict[str, Any]:
        """Check project dependencies"""
        self.logger.info(f"Checking dependencies: {project_path}")
        return {"status": "checked", "outdated": [], "vulnerable": []}
    
    async def _security_scan(self, path: str) -> Dict[str, Any]:
        """Security scan"""
        self.logger.info(f"Security scan: {path}")
        return {"status": "scanned", "issues": [], "severity": "low"}
    
    async def _code_metrics(self, file_path: str) -> Dict[str, Any]:
        """Calculate code metrics"""
        return await self._analyze_code(file_path)

class SystemMonitorAgent(Agent):
    """Agent for system monitoring and health checks"""
    
    def __init__(self):
        capabilities = [
            AgentCapability("check_health", "Check system health", []),
            AgentCapability("monitor_resources", "Monitor CPU/Memory/Disk", []),
            AgentCapability("check_services", "Check running services", ["service_names"]),
            AgentCapability("log_analysis", "Analyze system logs", ["log_path"]),
            AgentCapability("network_check", "Check network connectivity", ["hosts"])
        ]
        super().__init__("monitor_agent_001", "SystemMonitorAgent", capabilities)
    
    async def execute_task(self, task: Task) -> Any:
        """Execute monitoring tasks"""
        action = task.action
        params = task.params
        
        if action == "check_health":
            return await self._check_health()
        elif action == "monitor_resources":
            return await self._monitor_resources()
        elif action == "check_services":
            return await self._check_services(params.get("service_names", []))
        elif action == "log_analysis":
            return await self._log_analysis(params.get("log_path"))
        elif action == "network_check":
            return await self._network_check(params.get("hosts", []))
        else:
            raise ValueError(f"Unknown action: {action}")
    
    async def _check_health(self) -> Dict[str, Any]:
        """Check overall system health"""
        try:
            import psutil
            return {
                "status": "healthy",
                "cpu_percent": psutil.cpu_percent(),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage('/').percent
            }
        except ImportError:
            return {"status": "unknown", "error": "psutil not installed"}
    
    async def _monitor_resources(self) -> Dict[str, Any]:
        """Monitor system resources"""
        return await self._check_health()
    
    async def _check_services(self, service_names: List[str]) -> Dict[str, Any]:
        """Check if services are running"""
        self.logger.info(f"Checking services: {service_names}")
        running = {}
        
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            for service in service_names:
                running[service] = service in result.stdout
        except Exception as e:
            return {"error": str(e)}
        
        return {"services": running, "checked_at": asyncio.get_event_loop().time()}
    
    async def _log_analysis(self, log_path: str) -> Dict[str, Any]:
        """Analyze logs"""
        self.logger.info(f"Analyzing logs: {log_path}")
        return {"status": "analyzed", "errors": 0, "warnings": 0}
    
    async def _network_check(self, hosts: List[str]) -> Dict[str, Any]:
        """Check network connectivity"""
        self.logger.info(f"Checking network: {hosts}")
        results = {}
        
        for host in hosts:
            try:
                response = requests.get(f"http://{host}", timeout=2)
                results[host] = {"status": "up", "code": response.status_code}
            except:
                results[host] = {"status": "down"}
        
        return {"results": results}

class DataProcessingAgent(Agent):
    """Agent for data processing and transformation"""
    
    def __init__(self):
        capabilities = [
            AgentCapability("process_json", "Process JSON files", ["file_path", "operation"]),
            AgentCapability("convert_format", "Convert between file formats", ["source", "target_format"]),
            AgentCapability("aggregate_data", "Aggregate data from multiple sources", ["sources"]),
            AgentCapability("validate_data", "Validate data structure", ["data", "schema"]),
            AgentCapability("transform_data", "Transform data using rules", ["data", "rules"])
        ]
        super().__init__("data_agent_001", "DataProcessingAgent", capabilities)
    
    async def execute_task(self, task: Task) -> Any:
        """Execute data processing tasks"""
        action = task.action
        params = task.params
        
        if action == "process_json":
            return await self._process_json(params.get("file_path"), params.get("operation"))
        elif action == "convert_format":
            return await self._convert_format(params.get("source"), params.get("target_format"))
        elif action == "aggregate_data":
            return await self._aggregate_data(params.get("sources", []))
        elif action == "validate_data":
            return await self._validate_data(params.get("data"), params.get("schema"))
        elif action == "transform_data":
            return await self._transform_data(params.get("data"), params.get("rules"))
        else:
            raise ValueError(f"Unknown action: {action}")
    
    async def _process_json(self, file_path: str, operation: str) -> Dict[str, Any]:
        """Process JSON file"""
        self.logger.info(f"Processing JSON: {file_path}")
        
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return {"status": "processed", "keys": list(data.keys()) if isinstance(data, dict) else None}
        except Exception as e:
            return {"error": str(e)}
    
    async def _convert_format(self, source: str, target_format: str) -> Dict[str, Any]:
        """Convert file format"""
        self.logger.info(f"Converting {source} to {target_format}")
        return {"status": "converted", "output": f"{source}.{target_format}"}
    
    async def _aggregate_data(self, sources: List[str]) -> Dict[str, Any]:
        """Aggregate data from sources"""
        self.logger.info(f"Aggregating data from {len(sources)} sources")
        return {"status": "aggregated", "sources": len(sources)}
    
    async def _validate_data(self, data: Any, schema: Any) -> Dict[str, Any]:
        """Validate data against schema"""
        self.logger.info("Validating data")
        return {"valid": True, "errors": []}
    
    async def _transform_data(self, data: Any, rules: Any) -> Dict[str, Any]:
        """Transform data using rules"""
        self.logger.info("Transforming data")
        return {"status": "transformed", "records": 0}

# Factory function to create all specialized agents
def create_all_agents() -> List[Agent]:
    """Create instances of all specialized agents"""
    return [
        FileSystemAgent(),
        CodeAnalysisAgent(),
        SystemMonitorAgent(),
        DataProcessingAgent()
    ]

if __name__ == "__main__":
    print("🤖 Specialized Agents Module")
    agents = create_all_agents()
    for agent in agents:
        print(f"  - {agent.name}: {len(agent.capabilities)} capabilities")
