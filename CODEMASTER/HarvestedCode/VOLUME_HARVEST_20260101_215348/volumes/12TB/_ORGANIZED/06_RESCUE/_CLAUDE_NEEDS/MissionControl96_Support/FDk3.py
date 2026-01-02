# Alliance Officer Agent for MissionControl96
# Finds and recommends like-minded companies for strategic partnerships
import json

class AllianceOfficer:
    def find_partners(self, my_profile: dict[str, list[str] | str], companies: list[dict[str, list[str] | str]]) -> list[dict[str, object]]:
        # Placeholder: match by shared values, goals, and industry
        matches = []
        for company in companies:
            score = 0
            if company['industry'] == my_profile['industry']:
                score += 40
            if set(company['values']).intersection(my_profile['values']):
                score += 30
            if set(company['goals']).intersection(my_profile['goals']):
                score += 30
            if score > 50:
                matches.append({'company': company['name'], 'score': score, 'suggestion': 'Reach out for partnership.'})
        return matches

if __name__ == '__main__':
    my_profile: dict[str, list[str] | str] = {
        'industry': 'AI & Automation',
        'values': ['innovation', 'ethics', 'impact'],
        'goals': ['growth', 'global reach']
    }
    companies: list[dict[str, list[str] | str]] = [
        {'name': 'FutureAI', 'industry': 'AI & Automation', 'values': ['innovation', 'ethics'], 'goals': ['growth']},
        {'name': 'EcoTech', 'industry': 'Green Energy', 'values': ['sustainability'], 'goals': ['impact']},
        {'name': 'GlobalBots', 'industry': 'AI & Automation', 'values': ['impact', 'ethics'], 'goals': ['global reach']}
    ]
    print(json.dumps(AllianceOfficer().find_partners(my_profile, companies), indent=2))
