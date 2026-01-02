"""
NoizyFish_Aquarium Alliance Officer
Finds and recommends strategic partners for your universe.
"""
import json, asyncio
class AllianceOfficer:
    async def find_partners(self, my_profile, companies):
        await asyncio.sleep(0)
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
