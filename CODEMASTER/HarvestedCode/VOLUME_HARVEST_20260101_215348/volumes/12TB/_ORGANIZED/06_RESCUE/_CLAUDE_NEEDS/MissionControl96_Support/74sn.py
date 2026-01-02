# Alliance Officer Agent for MissionControl96
# Finds and recommends like-minded companies for strategic partnerships
import json

AI_AUTOMATION = 'AI & Automation'

class AllianceOfficer:
    def find_partners(
        self,
        my_profile: dict[str, list[str] | str],
        companies: list[dict[str, list[str] | str]]
    ) -> list[dict[str, object]]:
        """
        Find and recommend strategic partners based on shared industry, values, and goals.
        Args:
            my_profile: Dictionary with 'industry', 'values', and 'goals' for the user.
            companies: List of company profiles to evaluate.
        Returns:
            List of recommended companies with match score and suggestion.
        """
        matches: list[dict[str, object]] = []
        for company in companies:
            score = 0
            if (
                company.get('industry') == AI_AUTOMATION
                and my_profile.get('industry') == AI_AUTOMATION
            ):
                score += 40
            if set(company.get('values', [])).intersection(my_profile.get('values', [])):
                score += 30
            if set(company.get('goals', [])).intersection(my_profile.get('goals', [])):
                score += 30
            if score > 50:
                matches.append({
                    'company': company.get('name', ''),
                    'score': score,
                    'suggestion': 'Reach out for partnership.'
                })
        return matches

if __name__ == '__main__':
    my_profile: dict[str, list[str] | str] = {
        'industry': AI_AUTOMATION,
        'values': ['innovation', 'ethics', 'impact'],
        'goals': ['growth', 'global reach']
    }
    companies: list[dict[str, list[str] | str]] = [
        {'name': 'FutureAI', 'industry': AI_AUTOMATION, 'values': ['innovation', 'ethics'], 'goals': ['growth']},
        {'name': 'EcoTech', 'industry': 'Green Energy', 'values': ['sustainability'], 'goals': ['impact']},
        {'name': 'GlobalBots', 'industry': AI_AUTOMATION, 'values': ['impact', 'ethics'], 'goals': ['global reach']}
    ]
    print(json.dumps(AllianceOfficer().find_partners(my_profile, companies), indent=2))
