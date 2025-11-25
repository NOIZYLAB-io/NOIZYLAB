#!/usr/bin/env python3
# ==============================================================================
# THE LIBRARIAN - AI HOST GUIDE
# ==============================================================================
# Interactive AI-Powered Repair Workflow Assistant
# Fish Music Inc. / MissionControl96 / NOIZYLAB
# ==============================================================================

"""
AI HOST GUIDE - Your intelligent assistant for audio/video repair workflows.

This tool provides:
- Interactive guidance through repair workflows
- Tool recommendations based on task requirements
- AI model suggestions for automated processing
- Step-by-step instructions with parameters
- Integration with third-party AI assistants
"""

import json
import os
import sys
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

# ==============================================================================
# CONSTANTS & CONFIGURATION
# ==============================================================================

VERSION = "1.0.0"

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

# ==============================================================================
# REPAIR TASK CATEGORIES
# ==============================================================================

class TaskCategory(Enum):
    NOISE_REDUCTION = "noise_reduction"
    DIALOGUE_REPAIR = "dialogue_repair"
    MUSIC_RESTORATION = "music_restoration"
    STEM_SEPARATION = "stem_separation"
    VIDEO_RESTORATION = "video_restoration"
    CLIPPING_REPAIR = "clipping_repair"
    REVERB_REMOVAL = "reverb_removal"
    AUDIO_ENHANCEMENT = "audio_enhancement"
    SYNC_ALIGNMENT = "sync_alignment"
    UPSCALING = "upscaling"

# ==============================================================================
# TOOL DATABASE
# ==============================================================================

REPAIR_TOOLS = {
    "izotope_rx": {
        "name": "iZotope RX 11",
        "developer": "iZotope",
        "type": "suite",
        "ai_powered": True,
        "modules": [
            "Spectral De-noise", "Voice De-noise", "Dialogue Isolate",
            "Music Rebalance", "De-clip", "De-click", "De-crackle",
            "De-hum", "De-reverb", "Spectral Repair", "Breath Control",
            "Mouth De-click", "De-ess", "De-plosive", "Repair Assistant"
        ],
        "platforms": ["macOS", "Windows"],
        "formats": ["VST3", "AU", "AAX", "Standalone"],
        "price_tier": "premium",
        "url": "https://izotope.com/rx"
    },
    "adobe_podcast": {
        "name": "Adobe Podcast / Enhance Speech",
        "developer": "Adobe",
        "type": "cloud",
        "ai_powered": True,
        "capabilities": ["Speech enhancement", "Noise reduction", "Reverb removal"],
        "platforms": ["Web"],
        "price_tier": "free",
        "url": "https://podcast.adobe.com"
    },
    "waves_clarity_vx": {
        "name": "Waves Clarity Vx",
        "developer": "Waves",
        "type": "plugin",
        "ai_powered": True,
        "capabilities": ["Voice isolation", "Noise removal", "Real-time"],
        "platforms": ["macOS", "Windows"],
        "formats": ["VST3", "AU", "AAX"],
        "price_tier": "mid",
        "url": "https://waves.com/clarity-vx"
    },
    "lalal_ai": {
        "name": "LALAL.AI",
        "developer": "LALAL.AI",
        "type": "cloud",
        "ai_powered": True,
        "capabilities": ["Stem separation", "Vocals", "Drums", "Bass", "Piano"],
        "models": ["Orion", "Phoenix", "Cassiopeia"],
        "platforms": ["Web", "macOS", "Windows"],
        "api_available": True,
        "url": "https://lalal.ai"
    },
    "demucs": {
        "name": "Demucs",
        "developer": "Meta AI",
        "type": "open_source",
        "ai_powered": True,
        "capabilities": ["Stem separation"],
        "models": ["htdemucs", "htdemucs_ft", "mdx_extra"],
        "platforms": ["macOS", "Windows", "Linux"],
        "local_processing": True,
        "url": "https://github.com/facebookresearch/demucs"
    },
    "topaz_video": {
        "name": "Topaz Video AI",
        "developer": "Topaz Labs",
        "type": "standalone",
        "ai_powered": True,
        "capabilities": ["Upscaling", "Frame interpolation", "Stabilization", "Noise reduction"],
        "models": ["Proteus", "Gaia", "Artemis", "Chronos", "Apollo"],
        "platforms": ["macOS", "Windows"],
        "url": "https://topazlabs.com/video-ai"
    },
    "spectralayers": {
        "name": "SpectraLayers Pro",
        "developer": "Steinberg",
        "type": "standalone",
        "ai_powered": True,
        "capabilities": ["Spectral editing", "Unmix stems", "Voice denoiser"],
        "platforms": ["macOS", "Windows"],
        "formats": ["VST3", "AU", "Standalone"],
        "url": "https://steinberg.net/spectralayers"
    },
    "valhalla": {
        "name": "ValhallaDSP Suite",
        "developer": "ValhallaDSP",
        "type": "plugins",
        "ai_powered": False,
        "capabilities": ["Reverb", "Delay", "Modulation"],
        "products": ["Room", "VintageVerb", "Delay", "Supermassive (FREE)"],
        "platforms": ["macOS", "Windows"],
        "price_tier": "budget",
        "url": "https://valhalladsp.com"
    },
    "melodyne": {
        "name": "Melodyne",
        "developer": "Celemony",
        "type": "plugin",
        "ai_powered": False,
        "capabilities": ["Pitch correction", "Time stretching", "DNA polyphonic"],
        "platforms": ["macOS", "Windows"],
        "formats": ["VST3", "AU", "AAX", "Standalone"],
        "url": "https://celemony.com"
    },
    "revoice_pro": {
        "name": "Revoice Pro",
        "developer": "Synchro Arts",
        "type": "standalone",
        "ai_powered": True,
        "capabilities": ["Time alignment", "Pitch alignment", "ADR"],
        "platforms": ["macOS", "Windows"],
        "url": "https://synchroarts.com"
    }
}

# ==============================================================================
# WORKFLOW DEFINITIONS
# ==============================================================================

WORKFLOWS = {
    "noise_reduction": {
        "name": "Noise Reduction",
        "description": "Remove background noise, hiss, hum, and unwanted artifacts",
        "difficulty": "beginner",
        "estimated_time": "5-15 min",
        "primary_tools": ["izotope_rx", "waves_clarity_vx", "adobe_podcast"],
        "ai_models": ["RX Voice De-noise", "Clarity Vx Neural", "NVIDIA RTX Voice"],
        "steps": [
            {
                "order": 1,
                "name": "Analyze Recording",
                "action": "Listen through and identify noise types",
                "tools": ["Any player", "RX Spectral view"],
                "tips": "Note if noise is constant or varying"
            },
            {
                "order": 2,
                "name": "Capture Noise Profile",
                "action": "Find silent section with only noise, learn profile",
                "tools": ["RX Spectral De-noise"],
                "parameters": {"section_length": "1-2 seconds minimum"}
            },
            {
                "order": 3,
                "name": "Apply De-noise",
                "action": "Process with learned profile",
                "tools": ["RX Spectral De-noise", "Acon DeNoise"],
                "parameters": {
                    "threshold": "2-4 dB above noise floor",
                    "reduction": "6-12 dB typical",
                    "algorithm": "Adaptive for varying noise"
                }
            },
            {
                "order": 4,
                "name": "Check for Artifacts",
                "action": "Listen for musical noise, warbling, pumping",
                "tools": ["Headphones recommended"],
                "tips": "A/B compare frequently with original"
            },
            {
                "order": 5,
                "name": "Fine-tune",
                "action": "Adjust parameters if needed",
                "tips": "Less is often more - preserve naturalness"
            }
        ]
    },

    "dialogue_repair": {
        "name": "Dialogue Repair & Enhancement",
        "description": "Complete cleanup chain for speech and dialogue",
        "difficulty": "intermediate",
        "estimated_time": "15-30 min per minute of audio",
        "primary_tools": ["izotope_rx", "waves_clarity_vx", "revoice_pro"],
        "ai_models": ["RX Dialogue Isolate", "Clarity Vx DeReverb", "Adobe Podcast AI"],
        "steps": [
            {
                "order": 1,
                "name": "Dialogue Isolation",
                "action": "Separate speech from background",
                "tools": ["RX Dialogue Isolate", "Clarity Vx"],
                "parameters": {"sensitivity": "Start at 5, increase if needed"}
            },
            {
                "order": 2,
                "name": "De-reverb",
                "action": "Remove room sound",
                "tools": ["RX De-reverb", "Clarity Vx DeReverb"],
                "parameters": {"reduction": "3-4 dB to start"}
            },
            {
                "order": 3,
                "name": "Noise Reduction",
                "action": "Remove remaining noise floor",
                "tools": ["RX Voice De-noise"]
            },
            {
                "order": 4,
                "name": "De-click / Mouth Noise",
                "action": "Remove clicks and mouth sounds",
                "tools": ["RX Mouth De-click"],
                "parameters": {"sensitivity": "4-6"}
            },
            {
                "order": 5,
                "name": "De-plosive",
                "action": "Remove P-pops",
                "tools": ["RX De-plosive"],
                "parameters": {"sensitivity": "5-7", "frequency": "below 200Hz"}
            },
            {
                "order": 6,
                "name": "De-ess",
                "action": "Reduce sibilance",
                "tools": ["RX De-ess", "FabFilter Pro-DS"],
                "parameters": {"frequency": "4-8kHz range"}
            },
            {
                "order": 7,
                "name": "Breath Reduction",
                "action": "Reduce breath sounds",
                "tools": ["RX Breath Control"],
                "parameters": {"target_gain": "-12 to -18dB"}
            },
            {
                "order": 8,
                "name": "EQ & Presence",
                "action": "Shape tone",
                "tools": ["Any EQ"],
                "tips": "Boost 2-4kHz for presence, cut mud around 200-400Hz"
            },
            {
                "order": 9,
                "name": "Level & Limit",
                "action": "Normalize and limit peaks",
                "parameters": {"target": "-16 LUFS podcast, -24 LUFS broadcast"}
            }
        ]
    },

    "stem_separation": {
        "name": "AI Stem Separation",
        "description": "Separate mixed audio into individual stems",
        "difficulty": "beginner",
        "estimated_time": "5-10 min",
        "primary_tools": ["lalal_ai", "demucs", "izotope_rx"],
        "ai_models": ["LALAL.AI Orion", "Demucs htdemucs_ft", "RX Music Rebalance"],
        "steps": [
            {
                "order": 1,
                "name": "Prepare Source",
                "action": "Export highest quality version",
                "tips": "WAV/AIFF, 44.1kHz+, avoid MP3 if possible"
            },
            {
                "order": 2,
                "name": "Choose Model",
                "action": "Select appropriate AI model",
                "recommendations": {
                    "pop_rock": "Demucs htdemucs_ft",
                    "classical": "Demucs htdemucs",
                    "electronic": "LALAL.AI Orion",
                    "vocals_only": "LALAL.AI or Spleeter 2stems"
                }
            },
            {
                "order": 3,
                "name": "Run Separation",
                "action": "Process through AI",
                "tools": ["LALAL.AI web", "Demucs CLI", "SpectraLayers"]
            },
            {
                "order": 4,
                "name": "Evaluate Results",
                "action": "Check for artifacts and bleed",
                "common_issues": ["Vocal remnants", "Drum bleed", "Reverb tail artifacts"]
            },
            {
                "order": 5,
                "name": "Clean Stems",
                "action": "Apply repairs to individual stems if needed",
                "tools": ["RX", "SpectraLayers"]
            }
        ]
    },

    "video_restoration": {
        "name": "Video Restoration & Upscaling",
        "description": "Restore and enhance video quality",
        "difficulty": "advanced",
        "estimated_time": "30 min - several hours",
        "primary_tools": ["topaz_video", "davinci_resolve"],
        "ai_models": ["Topaz Proteus", "Topaz Artemis", "DaVinci Neural Engine"],
        "steps": [
            {
                "order": 1,
                "name": "Analyze Source",
                "action": "Identify resolution, frame rate, issues",
                "checklist": ["Resolution", "Frame rate", "Interlacing", "Noise", "Compression artifacts"]
            },
            {
                "order": 2,
                "name": "Deinterlace",
                "action": "Convert interlaced to progressive if needed",
                "tools": ["Topaz Video AI", "DaVinci Resolve"]
            },
            {
                "order": 3,
                "name": "Stabilize",
                "action": "Remove camera shake",
                "tools": ["Topaz", "DaVinci Resolve Stabilizer"]
            },
            {
                "order": 4,
                "name": "Denoise",
                "action": "Reduce video noise",
                "tools": ["Topaz Proteus"],
                "tips": "Balance between clean and natural"
            },
            {
                "order": 5,
                "name": "Upscale",
                "action": "Increase resolution",
                "models": {
                    "general": "Proteus",
                    "animation": "Gaia",
                    "low_quality": "Artemis"
                }
            },
            {
                "order": 6,
                "name": "Frame Interpolation (Optional)",
                "action": "Increase frame rate for slow motion",
                "tools": ["Topaz Chronos/Apollo"]
            },
            {
                "order": 7,
                "name": "Color Correct",
                "action": "Fix color issues",
                "tools": ["DaVinci Resolve Color"]
            }
        ]
    },

    "clipping_repair": {
        "name": "Clipping & Distortion Repair",
        "description": "Fix digital clipping and analog distortion",
        "difficulty": "intermediate",
        "estimated_time": "10-20 min",
        "primary_tools": ["izotope_rx", "acon_declip"],
        "ai_models": ["RX De-clip"],
        "steps": [
            {
                "order": 1,
                "name": "Identify Clipping",
                "action": "Determine if digital or analog clipping",
                "tips": "Digital = flat tops, Analog = soft saturation"
            },
            {
                "order": 2,
                "name": "Analyze Severity",
                "action": "Check how much of waveform is affected",
                "tools": ["RX Spectral view", "Waveform editor"]
            },
            {
                "order": 3,
                "name": "Apply De-clip",
                "action": "Reconstruct clipped peaks",
                "tools": ["RX De-clip", "Acon DeClip"],
                "parameters": {"quality": "High for severe, Normal for light"}
            },
            {
                "order": 4,
                "name": "Reduce Residual Distortion",
                "action": "Clean up remaining artifacts",
                "tools": ["RX Spectral Repair"]
            },
            {
                "order": 5,
                "name": "Level Match",
                "action": "Normalize repaired sections",
                "tools": ["Any leveling tool"]
            }
        ]
    },

    "reverb_removal": {
        "name": "Reverb & Room Removal",
        "description": "Remove unwanted room sound and reverb",
        "difficulty": "intermediate",
        "estimated_time": "10-15 min",
        "primary_tools": ["izotope_rx", "waves_clarity_vx"],
        "ai_models": ["RX De-reverb", "Clarity Vx DeReverb", "Zynaptiq UNVEIL"],
        "steps": [
            {
                "order": 1,
                "name": "Analyze Reverb",
                "action": "Identify reverb characteristics",
                "parameters": ["Tail length", "Early reflections", "Room size"]
            },
            {
                "order": 2,
                "name": "Set Profile",
                "action": "Configure reverb reduction parameters",
                "tools": ["RX De-reverb"]
            },
            {
                "order": 3,
                "name": "Process",
                "action": "Apply de-reverb",
                "tips": "Start conservative, increase gradually"
            },
            {
                "order": 4,
                "name": "Preserve Transients",
                "action": "Handle transients separately if needed",
                "tips": "Transients may need less processing"
            },
            {
                "order": 5,
                "name": "Add Controlled Reverb (Optional)",
                "action": "Add new, controlled reverb if too dry",
                "tools": ["Valhalla Room", "FabFilter Pro-R"]
            }
        ]
    }
}

# ==============================================================================
# AI HOST CLASS
# ==============================================================================

class AIHostGuide:
    """Interactive AI-powered repair workflow assistant."""

    def __init__(self):
        self.tools = REPAIR_TOOLS
        self.workflows = WORKFLOWS
        self.current_workflow = None
        self.current_step = 0

    def welcome(self):
        """Display welcome message."""
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}  THE LIBRARIAN - AI HOST GUIDE v{VERSION}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}  Audio/Video Repair Workflow Assistant{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"\n{Colors.YELLOW}Fish Music Inc. / MissionControl96 / NOIZYLAB{Colors.END}\n")

    def list_workflows(self):
        """List all available workflows."""
        print(f"\n{Colors.BOLD}Available Repair Workflows:{Colors.END}\n")
        for key, workflow in self.workflows.items():
            difficulty_color = {
                "beginner": Colors.GREEN,
                "intermediate": Colors.YELLOW,
                "advanced": Colors.RED
            }.get(workflow["difficulty"], Colors.BLUE)

            print(f"  {Colors.CYAN}{key:20}{Colors.END} - {workflow['name']}")
            print(f"    {difficulty_color}[{workflow['difficulty']}]{Colors.END} "
                  f"Est. time: {workflow['estimated_time']}")
            print()

    def list_tools(self):
        """List all available tools."""
        print(f"\n{Colors.BOLD}Available Repair Tools:{Colors.END}\n")
        for key, tool in self.tools.items():
            ai_badge = f"{Colors.YELLOW}[AI]{Colors.END} " if tool.get("ai_powered") else ""
            print(f"  {ai_badge}{Colors.CYAN}{tool['name']}{Colors.END}")
            print(f"    Developer: {tool['developer']}")
            print(f"    Type: {tool['type']}")
            if tool.get("capabilities"):
                print(f"    Capabilities: {', '.join(tool['capabilities'][:3])}")
            print()

    def start_workflow(self, workflow_key: str):
        """Start a specific workflow."""
        if workflow_key not in self.workflows:
            print(f"{Colors.RED}Unknown workflow: {workflow_key}{Colors.END}")
            print(f"Available: {', '.join(self.workflows.keys())}")
            return

        self.current_workflow = self.workflows[workflow_key]
        self.current_step = 0

        print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.GREEN}  {self.current_workflow['name']}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.END}")
        print(f"\n{Colors.CYAN}{self.current_workflow['description']}{Colors.END}")
        print(f"\nDifficulty: {self.current_workflow['difficulty']}")
        print(f"Estimated time: {self.current_workflow['estimated_time']}")

        print(f"\n{Colors.BOLD}Primary Tools:{Colors.END}")
        for tool_key in self.current_workflow['primary_tools']:
            tool = self.tools.get(tool_key, {"name": tool_key})
            print(f"  - {tool.get('name', tool_key)}")

        print(f"\n{Colors.BOLD}AI Models Available:{Colors.END}")
        for model in self.current_workflow['ai_models']:
            print(f"  - {Colors.YELLOW}{model}{Colors.END}")

        print(f"\n{Colors.BOLD}Workflow Steps:{Colors.END}")
        for step in self.current_workflow['steps']:
            print(f"  {step['order']}. {step['name']}")

        print(f"\n{Colors.GREEN}Type 'next' to begin step-by-step guide{Colors.END}")

    def next_step(self):
        """Show next step in current workflow."""
        if not self.current_workflow:
            print(f"{Colors.RED}No workflow active. Use 'start <workflow>' first.{Colors.END}")
            return

        steps = self.current_workflow['steps']
        if self.current_step >= len(steps):
            print(f"\n{Colors.GREEN}Workflow complete!{Colors.END}")
            self.current_workflow = None
            self.current_step = 0
            return

        step = steps[self.current_step]
        total = len(steps)

        print(f"\n{Colors.BOLD}{Colors.BLUE}{'─'*60}{Colors.END}")
        print(f"{Colors.BOLD}Step {step['order']}/{total}: {step['name']}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.BLUE}{'─'*60}{Colors.END}")

        print(f"\n{Colors.CYAN}Action:{Colors.END} {step['action']}")

        if step.get('tools'):
            print(f"\n{Colors.CYAN}Tools:{Colors.END}")
            for tool in step['tools']:
                print(f"  - {tool}")

        if step.get('parameters'):
            print(f"\n{Colors.CYAN}Parameters:{Colors.END}")
            params = step['parameters']
            if isinstance(params, dict):
                for key, value in params.items():
                    print(f"  {key}: {value}")
            else:
                print(f"  {params}")

        if step.get('tips'):
            print(f"\n{Colors.YELLOW}Tip:{Colors.END} {step['tips']}")

        if step.get('recommendations'):
            print(f"\n{Colors.CYAN}Recommendations:{Colors.END}")
            for use_case, rec in step['recommendations'].items():
                print(f"  {use_case}: {rec}")

        self.current_step += 1

        if self.current_step < total:
            print(f"\n{Colors.GREEN}Type 'next' for next step{Colors.END}")
        else:
            print(f"\n{Colors.GREEN}Final step! Type 'next' to complete.{Colors.END}")

    def recommend_tools(self, task_type: str):
        """Recommend tools for a specific task type."""
        print(f"\n{Colors.BOLD}Tool Recommendations for: {task_type}{Colors.END}\n")

        recommendations = {
            "noise": ["izotope_rx", "waves_clarity_vx", "adobe_podcast"],
            "dialogue": ["izotope_rx", "waves_clarity_vx", "revoice_pro"],
            "stems": ["lalal_ai", "demucs", "spectralayers"],
            "video": ["topaz_video"],
            "pitch": ["melodyne", "izotope_rx"],
            "reverb": ["izotope_rx", "waves_clarity_vx"]
        }

        tool_keys = recommendations.get(task_type.lower(), [])
        if not tool_keys:
            print(f"  No specific recommendations for '{task_type}'")
            print(f"  Available task types: {', '.join(recommendations.keys())}")
            return

        print(f"  {Colors.BOLD}Primary:{Colors.END}")
        for key in tool_keys:
            tool = self.tools.get(key)
            if tool:
                ai = f" {Colors.YELLOW}[AI]{Colors.END}" if tool.get("ai_powered") else ""
                print(f"    - {tool['name']}{ai}")
                print(f"      {tool.get('url', 'N/A')}")

    def get_api_info(self, tool_key: str):
        """Get API information for a tool."""
        tool = self.tools.get(tool_key)
        if not tool:
            print(f"{Colors.RED}Unknown tool: {tool_key}{Colors.END}")
            return

        print(f"\n{Colors.BOLD}API Information: {tool['name']}{Colors.END}\n")

        if tool.get("api_available"):
            print(f"  {Colors.GREEN}API Available{Colors.END}")
            print(f"  URL: {tool.get('url', 'N/A')}")
        elif tool.get("local_processing"):
            print(f"  {Colors.CYAN}Local Processing Available{Colors.END}")
            print(f"  Can be integrated via Python/CLI")
            print(f"  URL: {tool.get('url', 'N/A')}")
        else:
            print(f"  {Colors.YELLOW}No public API - Plugin/Standalone only{Colors.END}")

    def export_workflow(self, workflow_key: str, output_file: str = None):
        """Export workflow to JSON for third-party integration."""
        if workflow_key not in self.workflows:
            print(f"{Colors.RED}Unknown workflow: {workflow_key}{Colors.END}")
            return

        workflow = self.workflows[workflow_key]

        # Add tool details
        export_data = {
            "workflow": workflow,
            "tools": {}
        }

        for tool_key in workflow.get("primary_tools", []):
            if tool_key in self.tools:
                export_data["tools"][tool_key] = self.tools[tool_key]

        if output_file:
            with open(output_file, 'w') as f:
                json.dump(export_data, f, indent=2)
            print(f"{Colors.GREEN}Exported to: {output_file}{Colors.END}")
        else:
            print(json.dumps(export_data, indent=2))

    def interactive_mode(self):
        """Run in interactive mode."""
        self.welcome()

        print("Commands:")
        print("  list         - Show available workflows")
        print("  tools        - Show available tools")
        print("  start <name> - Start a workflow")
        print("  next         - Next step in workflow")
        print("  recommend <type> - Tool recommendations")
        print("  api <tool>   - API information")
        print("  export <workflow> [file] - Export workflow")
        print("  quit         - Exit")
        print()

        while True:
            try:
                cmd = input(f"{Colors.CYAN}ai-host>{Colors.END} ").strip().lower()

                if not cmd:
                    continue
                elif cmd == "quit" or cmd == "exit":
                    print("Goodbye!")
                    break
                elif cmd == "list":
                    self.list_workflows()
                elif cmd == "tools":
                    self.list_tools()
                elif cmd == "next":
                    self.next_step()
                elif cmd.startswith("start "):
                    workflow = cmd.split(" ", 1)[1]
                    self.start_workflow(workflow)
                elif cmd.startswith("recommend "):
                    task = cmd.split(" ", 1)[1]
                    self.recommend_tools(task)
                elif cmd.startswith("api "):
                    tool = cmd.split(" ", 1)[1]
                    self.get_api_info(tool)
                elif cmd.startswith("export "):
                    parts = cmd.split(" ")
                    workflow = parts[1] if len(parts) > 1 else None
                    output = parts[2] if len(parts) > 2 else None
                    if workflow:
                        self.export_workflow(workflow, output)
                else:
                    print(f"Unknown command: {cmd}")

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                break


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="AI Host Guide - Audio/Video Repair Assistant"
    )
    parser.add_argument("--interactive", "-i", action="store_true",
                       help="Run in interactive mode")
    parser.add_argument("--list", "-l", action="store_true",
                       help="List workflows")
    parser.add_argument("--tools", "-t", action="store_true",
                       help="List tools")
    parser.add_argument("--workflow", "-w", type=str,
                       help="Show specific workflow")
    parser.add_argument("--export", "-e", type=str,
                       help="Export workflow to JSON")
    parser.add_argument("--output", "-o", type=str,
                       help="Output file for export")

    args = parser.parse_args()

    guide = AIHostGuide()

    if args.list:
        guide.welcome()
        guide.list_workflows()
    elif args.tools:
        guide.welcome()
        guide.list_tools()
    elif args.workflow:
        guide.welcome()
        guide.start_workflow(args.workflow)
    elif args.export:
        guide.export_workflow(args.export, args.output)
    elif args.interactive or len(sys.argv) == 1:
        guide.interactive_mode()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
