"""
NoizyFish_Aquarium Idea Manager
Corrals, aligns, and consolidates ideas into smart categories for your universe.
"""
import json, re
from collections import defaultdict

class IdeaManager:
    def __init__(self):
        self.ideas = []

    def collect_ideas(self, sources):
        for src in sources:
            for idea in re.split(r'[\n;]', src):
                idea = idea.strip()
                if idea:
                    self.ideas.append(idea)

    def categorize_ideas(self):
        categories = defaultdict(list)
        keywords = {
            'AI': ['ai', 'machine learning', 'predictive', 'analytics'],
            'Strategy': ['strategy', 'plan', 'goal', 'direction'],
            'Compliance': ['compliance', 'risk', 'audit', 'ethics'],
            'Partnership': ['partner', 'alliance', 'collaboration'],
            'Productivity': ['workflow', 'tool', 'automation', 'efficiency'],
            'Innovation': ['future', 'trend', 'new', 'experiment', 'vision']
        }
        for idea in self.ideas:
            found = False
            for cat, kws in keywords.items():
                if any(kw in idea.lower() for kw in kws):
                    categories[cat].append(idea)
                    found = True
                    break
            if not found:
                categories['Other'].append(idea)
        return dict(categories)

    def align_and_consolidate(self):
        cats = self.categorize_ideas()
        consolidated = {}
        for cat, ideas in cats.items():
            consolidated[cat] = list(set(ideas))
        return consolidated
