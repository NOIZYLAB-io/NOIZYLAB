# MissionControl96 Idea Manager
# Corrals, aligns, and consolidates ideas into smart categories
import json, re
from collections import defaultdict

class IdeaManager:
    def __init__(self):
        self.ideas = []

    def collect_ideas(self, sources: list[str]) -> None:
        # sources: list of strings (idea text from files, modules, notes)
        for src in sources:
            for idea in re.split(r'[\n;]', src):
                idea = idea.strip()
                if idea:
                    self.ideas.append(idea)

    def categorize_ideas(self) -> dict[str, list[str]]:
        # Simple AI: group by keywords (can be replaced with ML)
        categories: defaultdict[str, list[str]] = defaultdict(list)
        keywords: dict[str, list[str]] = {
            'AI': ['ai', 'machine learning', 'predictive', 'analytics'],
            'Strategy': ['strategy', 'plan', 'goal', 'direction'],
            'Compliance': ['compliance', 'risk', 'audit', 'ethics'],
            'Partnership': ['partner', 'alliance', 'collaboration'],
            'Productivity': ['workflow', 'tool', 'automation', 'efficiency'],
            'Innovation': ['future', 'trend', 'new', 'experiment', 'vision']
        }
        for idea in self.ideas:
            found: bool = False
            for cat, kws in keywords.items():
                if any(kw in idea.lower() for kw in kws):
                    categories[cat].append(idea)
                    found = True
                    break
            if not found:
                categories['Other'].append(idea)
        return dict(categories)

    def align_and_consolidate(self) -> dict[str, list[str]]:
        # Find overlaps and suggest consolidation
        cats: dict[str, list[str]] = self.categorize_ideas()
        consolidated: dict[str, list[str]] = {}
        for cat, ideas in cats.items():
            consolidated[cat] = list(set(ideas))  # Remove duplicates
        return consolidated

if __name__ == '__main__':
    manager = IdeaManager()
    sources = [
        'AI-driven analytics for business; Strategic planning dashboard',
        'Compliance automation tool; Partner matching agent',
        'Workflow optimization; Future trend analysis; Visionary leadership'
    ]
    manager.collect_ideas(sources)
    print(json.dumps(manager.align_and_consolidate(), indent=2))
