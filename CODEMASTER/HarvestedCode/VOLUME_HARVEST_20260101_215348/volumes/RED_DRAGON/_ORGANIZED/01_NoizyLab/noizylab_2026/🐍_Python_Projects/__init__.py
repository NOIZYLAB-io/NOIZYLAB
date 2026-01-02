"""
NoizyFish_Aquarium - Python Projects Collection
===============================================

This is the main Python scripts repository within the NoizyFish_Aquarium.
All stray scripts have been organized into logical categories for better 
management and reusability, following the established NoizyFish structure.

Directory Structure:
- audio_processing/: Kontakt and audio-related scripts
- automation/: Agent, genie, and fishnet automation scripts  
- file_management/: Library repair, organizers, and search tools
- utilities/: General purpose tools and helpers
- workspace_tools/: VS Code and workspace setup scripts
- NoizyFish/: Core NoizyFish project files

Related Collections:
- 🤖 AI_Toolkit/: Advanced AI tools and agents
- 🔧 Tools_And_Utilities/: System utilities
- 🌟 JavaScript_Projects/: Frontend and JS projects

To use scripts from anywhere, add this to your Python path:
    import sys
    sys.path.append('/Users/rsp_ms/NoizyFish_Aquarium/🐍 Python_Projects')

Or set PYTHONPATH environment variable:
    export PYTHONPATH="${PYTHONPATH}:/Users/rsp_ms/NoizyFish_Aquarium/🐍 Python_Projects"
"""

__version__ = "1.0.0"
__author__ = "rsp_ms"

# Quick access imports for commonly used modules
try:
    from .automation import agent_preflight
    from .file_management import hand_of_god_search
    from .utilities import auto_scan
except ImportError:
    # If relative imports fail, scripts can still be run individually
    pass