#!/usr/bin/env python3
"""
Advanced Audio & Media Processing Agent
Specialized for NoizyLab's audio production workflow
"""
import os
import asyncio
from pathlib import Path
from typing import Dict, Any, List
import json
from agent_core import Agent, AgentCapability, Task

class AudioProcessingAgent(Agent):
    """Agent specialized in audio file operations"""
    
    def __init__(self):
        capabilities = [
            AgentCapability("scan_audio_library", "Scan and catalog audio files", ["path"], cost=2.0),
            AgentCapability("organize_samples", "Organize samples by type/BPM/key", ["path", "strategy"], cost=3.0),
            AgentCapability("find_duplicates", "Find duplicate audio files", ["path"], cost=2.5),
            AgentCapability("analyze_library", "Analyze library statistics", ["path"], cost=2.0),
            AgentCapability("batch_rename", "Batch rename audio files", ["path", "pattern"], cost=1.5),
            AgentCapability("create_index", "Create searchable audio index", ["path"], cost=3.0),
            AgentCapability("verify_integrity", "Check audio file integrity", ["path"], cost=2.0)
        ]
        super().__init__("audio_agent_001", "AudioProcessingAgent", capabilities)
        
        # Audio extensions
        self.audio_extensions = {
            '.wav', '.aif', '.aiff', '.mp3', '.flac', '.ogg',
            '.m4a', '.aac', '.wma', '.alac'
        }
        
        # Sample types
        self.sample_types = {
            'drum': ['kick', 'snare', 'hat', 'clap', 'perc', 'cymbal'],
            'synth': ['lead', 'pad', 'bass', 'arp', 'pluck'],
            'fx': ['riser', 'impact', 'sweep', 'transition', 'atmosphere'],
            'vocal': ['vocal', 'vox', 'voice', 'speech', 'acapella']
        }
    
    async def execute_task(self, task: Task) -> Any:
        """Execute audio processing tasks"""
        action = task.action
        params = task.params
        
        if action == "scan_audio_library":
            return await self._scan_audio_library(params.get("path"))
        elif action == "organize_samples":
            return await self._organize_samples(params.get("path"), params.get("strategy", "type"))
        elif action == "find_duplicates":
            return await self._find_duplicates(params.get("path"))
        elif action == "analyze_library":
            return await self._analyze_library(params.get("path"))
        elif action == "batch_rename":
            return await self._batch_rename(params.get("path"), params.get("pattern"))
        elif action == "create_index":
            return await self._create_index(params.get("path"))
        elif action == "verify_integrity":
            return await self._verify_integrity(params.get("path"))
        else:
            raise ValueError(f"Unknown action: {action}")
    
    async def _scan_audio_library(self, path: str) -> Dict[str, Any]:
        """Scan audio library and gather statistics"""
        self.logger.info(f"🎵 Scanning audio library: {path}")
        
        path_obj = Path(path)
        if not path_obj.exists():
            return {"error": "Path does not exist"}
        
        stats = {
            "total_files": 0,
            "total_size": 0,
            "by_extension": {},
            "by_type": {},
            "folders": [],
            "largest_files": []
        }
        
        for item in path_obj.rglob("*"):
            if item.is_file() and item.suffix.lower() in self.audio_extensions:
                stats["total_files"] += 1
                size = item.stat().st_size
                stats["total_size"] += size
                
                # Count by extension
                ext = item.suffix.lower()
                stats["by_extension"][ext] = stats["by_extension"].get(ext, 0) + 1
                
                # Detect sample type
                filename_lower = item.name.lower()
                detected_type = "other"
                for sample_type, keywords in self.sample_types.items():
                    if any(kw in filename_lower for kw in keywords):
                        detected_type = sample_type
                        break
                
                stats["by_type"][detected_type] = stats["by_type"].get(detected_type, 0) + 1
                
                # Track largest files
                stats["largest_files"].append({
                    "path": str(item),
                    "name": item.name,
                    "size": size,
                    "size_mb": round(size / (1024 * 1024), 2)
                })
        
        # Sort and limit largest files
        stats["largest_files"] = sorted(
            stats["largest_files"],
            key=lambda x: x["size"],
            reverse=True
        )[:20]
        
        stats["total_size_gb"] = round(stats["total_size"] / (1024**3), 2)
        
        self.logger.info(f"✅ Scanned {stats['total_files']} audio files ({stats['total_size_gb']} GB)")
        return stats
    
    async def _organize_samples(self, path: str, strategy: str) -> Dict[str, Any]:
        """Organize samples by specified strategy"""
        self.logger.info(f"🗂️  Organizing samples: {path} (strategy: {strategy})")
        
        # This would implement actual file organization
        # For now, return a plan
        return {
            "status": "planned",
            "strategy": strategy,
            "path": path,
            "message": "Organization plan created"
        }
    
    async def _find_duplicates(self, path: str) -> Dict[str, Any]:
        """Find duplicate audio files by size and name"""
        self.logger.info(f"🔍 Finding duplicates in: {path}")
        
        files_by_size = {}
        duplicates = []
        
        for item in Path(path).rglob("*"):
            if item.is_file() and item.suffix.lower() in self.audio_extensions:
                size = item.stat().st_size
                name = item.name.lower()
                key = f"{name}_{size}"
                
                if key in files_by_size:
                    duplicates.append({
                        "original": str(files_by_size[key]),
                        "duplicate": str(item),
                        "size_mb": round(size / (1024 * 1024), 2)
                    })
                else:
                    files_by_size[key] = item
        
        total_waste = sum(d["size_mb"] for d in duplicates)
        
        return {
            "duplicates_found": len(duplicates),
            "duplicates": duplicates[:50],  # Limit to 50
            "potential_space_saved_mb": round(total_waste, 2)
        }
    
    async def _analyze_library(self, path: str) -> Dict[str, Any]:
        """Comprehensive library analysis"""
        return await self._scan_audio_library(path)
    
    async def _batch_rename(self, path: str, pattern: str) -> Dict[str, Any]:
        """Batch rename files according to pattern"""
        self.logger.info(f"✏️  Batch renaming in: {path}")
        
        return {
            "status": "planned",
            "pattern": pattern,
            "files_to_rename": 0
        }
    
    async def _create_index(self, path: str) -> Dict[str, Any]:
        """Create searchable index of audio library"""
        self.logger.info(f"📇 Creating index for: {path}")
        
        index_path = Path(path) / "audio_library_index.json"
        scan_result = await self._scan_audio_library(path)
        
        index_data = {
            "created_at": asyncio.get_event_loop().time(),
            "library_path": path,
            "statistics": scan_result
        }
        
        try:
            with open(index_path, 'w') as f:
                json.dump(index_data, f, indent=2)
            
            return {
                "status": "created",
                "index_path": str(index_path),
                "files_indexed": scan_result.get("total_files", 0)
            }
        except Exception as e:
            return {"error": str(e)}
    
    async def _verify_integrity(self, path: str) -> Dict[str, Any]:
        """Verify audio file integrity"""
        self.logger.info(f"🔎 Verifying integrity: {path}")
        
        issues = []
        checked = 0
        
        for item in Path(path).rglob("*"):
            if item.is_file() and item.suffix.lower() in self.audio_extensions:
                checked += 1
                
                # Check if file is readable and not empty
                try:
                    if item.stat().st_size == 0:
                        issues.append({
                            "file": str(item),
                            "issue": "zero_size"
                        })
                except Exception as e:
                    issues.append({
                        "file": str(item),
                        "issue": f"read_error: {e}"
                    })
        
        return {
            "files_checked": checked,
            "issues_found": len(issues),
            "issues": issues[:20]  # Limit to 20
        }

class ProjectManagementAgent(Agent):
    """Agent for managing NoizyLab projects"""
    
    def __init__(self):
        capabilities = [
            AgentCapability("scan_projects", "Scan and catalog projects", ["path"]),
            AgentCapability("analyze_project", "Analyze project structure", ["project_path"]),
            AgentCapability("backup_project", "Backup project files", ["project_path", "backup_location"]),
            AgentCapability("organize_projects", "Organize projects by date/type", ["path"]),
            AgentCapability("find_project_assets", "Find all assets for project", ["project_path"]),
            AgentCapability("generate_report", "Generate project report", ["project_path"])
        ]
        super().__init__("project_agent_001", "ProjectManagementAgent", capabilities)
        
        self.project_extensions = {
            '.logic', '.logicx',  # Logic Pro
            '.als',  # Ableton Live
            '.flp',  # FL Studio
            '.ptx', '.ptf',  # Pro Tools
            '.cpr',  # Cubase
            '.rpp',  # REAPER
        }
    
    async def execute_task(self, task: Task) -> Any:
        """Execute project management tasks"""
        action = task.action
        params = task.params
        
        if action == "scan_projects":
            return await self._scan_projects(params.get("path"))
        elif action == "analyze_project":
            return await self._analyze_project(params.get("project_path"))
        elif action == "backup_project":
            return await self._backup_project(
                params.get("project_path"),
                params.get("backup_location")
            )
        elif action == "organize_projects":
            return await self._organize_projects(params.get("path"))
        elif action == "find_project_assets":
            return await self._find_project_assets(params.get("project_path"))
        elif action == "generate_report":
            return await self._generate_report(params.get("project_path"))
        else:
            raise ValueError(f"Unknown action: {action}")
    
    async def _scan_projects(self, path: str) -> Dict[str, Any]:
        """Scan for project files"""
        self.logger.info(f"📁 Scanning projects: {path}")
        
        projects = []
        
        for item in Path(path).rglob("*"):
            if item.is_file() and item.suffix.lower() in self.project_extensions:
                projects.append({
                    "name": item.name,
                    "path": str(item),
                    "type": item.suffix,
                    "size_mb": round(item.stat().st_size / (1024 * 1024), 2),
                    "modified": item.stat().st_mtime
                })
        
        return {
            "projects_found": len(projects),
            "projects": sorted(projects, key=lambda x: x["modified"], reverse=True)
        }
    
    async def _analyze_project(self, project_path: str) -> Dict[str, Any]:
        """Analyze a specific project"""
        self.logger.info(f"🔍 Analyzing project: {project_path}")
        
        project_file = Path(project_path)
        if not project_file.exists():
            return {"error": "Project not found"}
        
        return {
            "name": project_file.name,
            "type": project_file.suffix,
            "size_mb": round(project_file.stat().st_size / (1024 * 1024), 2),
            "location": str(project_file.parent),
            "last_modified": project_file.stat().st_mtime
        }
    
    async def _backup_project(self, project_path: str, backup_location: str) -> Dict[str, Any]:
        """Backup a project"""
        self.logger.info(f"💾 Backing up: {project_path} -> {backup_location}")
        
        return {
            "status": "planned",
            "source": project_path,
            "destination": backup_location
        }
    
    async def _organize_projects(self, path: str) -> Dict[str, Any]:
        """Organize projects"""
        self.logger.info(f"🗂️  Organizing projects: {path}")
        
        return {"status": "planned", "path": path}
    
    async def _find_project_assets(self, project_path: str) -> Dict[str, Any]:
        """Find all assets related to a project"""
        self.logger.info(f"🔍 Finding assets for: {project_path}")
        
        project_dir = Path(project_path).parent
        assets = {
            "audio": [],
            "midi": [],
            "presets": [],
            "other": []
        }
        
        for item in project_dir.rglob("*"):
            if item.is_file():
                ext = item.suffix.lower()
                if ext in ['.wav', '.aif', '.mp3', '.flac']:
                    assets["audio"].append(str(item))
                elif ext in ['.mid', '.midi']:
                    assets["midi"].append(str(item))
                elif ext in ['.fxp', '.preset']:
                    assets["presets"].append(str(item))
                else:
                    assets["other"].append(str(item))
        
        return {
            "project": project_path,
            "assets_found": sum(len(v) for v in assets.values()),
            "breakdown": {k: len(v) for k, v in assets.items()}
        }
    
    async def _generate_report(self, project_path: str) -> Dict[str, Any]:
        """Generate comprehensive project report"""
        analysis = await self._analyze_project(project_path)
        assets = await self._find_project_assets(project_path)
        
        return {
            "project_info": analysis,
            "assets": assets,
            "report_generated": True
        }

# Factory function
def create_advanced_agents() -> List[Agent]:
    """Create advanced specialized agents"""
    return [
        AudioProcessingAgent(),
        ProjectManagementAgent()
    ]

if __name__ == "__main__":
    print("🎨 Advanced Agents Module")
    agents = create_advanced_agents()
    for agent in agents:
        print(f"  - {agent.name}: {len(agent.capabilities)} capabilities")
