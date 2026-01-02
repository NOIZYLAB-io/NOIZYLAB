"""
NoizyFish_Aquarium SuperBrain Controller
Orchestrates all agents, adapts strategies, and enables unmatched business intelligence.
"""

import asyncio
import importlib
import json
import os

# Config-driven agent registry
AGENT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'agent_registry.json')

def load_agent_config():
    if os.path.exists(AGENT_CONFIG_PATH):
        with open(AGENT_CONFIG_PATH) as f:
            return json.load(f)
    # Default registry
    return [
        {"name": "ai_health", "module": "daemons.ai_health", "class": None, "async_func": "analyze_logs_async", "args": ["/Users/rsp_ms/NOIZYGRID_LOGS"]},
        {"name": "business_ai", "module": "daemons.ai_business", "class": "BusinessAI", "async_func": "evaluate_idea", "args": ["Next-gen AI platform"]},
        {"name": "alliance_officer", "module": "business_modules.alliance_officer", "class": "AllianceOfficer", "async_func": "find_partners", "args": [{"industry": "AI & Automation", "values": ["innovation"], "goals": ["growth"]}, [{"name": "FutureAI", "industry": "AI & Automation", "values": ["innovation"], "goals": ["growth"]}]]},
        {"name": "nda_manager", "module": "business_modules.nda_manager", "class": "NDAManager", "async_func": "get_template", "args": []},
        {"name": "idea_manager", "module": "business_modules.idea_manager", "class": "IdeaManager", "async_func": "align_and_consolidate", "args": []},
        {"name": "compliance_agent", "module": "business_modules.intuitive_compliance", "class": "ComplianceAgent", "async_func": "check_compliance", "args": [["Data Privacy"], {"Data Privacy": "complete"}]}
    ]

def dynamic_load_agent(agent):
    mod = importlib.import_module(agent["module"])
    if agent["class"]:
        instance = getattr(mod, agent["class"])()
        func = getattr(instance, agent["async_func"])
    else:
        func = getattr(mod, agent["async_func"])
    return func, agent["args"]


async def main():
    # Plug-and-play agent orchestration
    agent_config = load_agent_config()
    tasks = []
    for agent in agent_config:
        func, args = dynamic_load_agent(agent)
        if asyncio.iscoroutinefunction(func):
            tasks.append(func(*args))
        else:
            # Wrap sync function for async
            loop = asyncio.get_event_loop()
            tasks.append(loop.run_in_executor(None, func, *args))
    results = await asyncio.gather(*tasks)
    for agent, result in zip(agent_config, results):
        print(f'{agent["name"]}:', result)

if __name__ == '__main__':
    asyncio.run(main())
