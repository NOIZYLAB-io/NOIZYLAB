"""
NoizyFish_Aquarium NDA Manager
Digital NDA workflow and enforcement for your universe.
"""
import datetime, json

class NDAManager:
    def get_template(self):
        return '''
NON-DISCLOSURE AGREEMENT (NDA)

This Agreement is made on {date} between:
Disclosing Party: [Your Company Name]
Receiving Party: [Outside Entity Name]
1. Purpose: To protect confidential information shared during discussions and potential partnership.
2. Definition: "Confidential Information" includes all non-public, proprietary, technical, business, and strategic data.
3. Obligations: Receiving Party shall not disclose, copy, or use Confidential Information except as permitted.
4. Term: This NDA remains in effect for 5 years from the date of signing.
5. Enforcement: Breach may result in legal action, damages, and injunctive relief.
6. Jurisdiction: [Your State/Country]
7. Digital Signature: This NDA may be signed electronically and is legally binding.
Disclosing Party Signature: ______________________
Receiving Party Signature: ______________________
Date: {date}
'''.format(date=datetime.date.today())

    def record_signature(self, entity, signed_by, timestamp=None):
        if not timestamp:
            timestamp = datetime.datetime.now().isoformat()
        record = {
            'entity': entity,
            'signed_by': signed_by,
            'timestamp': timestamp,
            'status': 'signed'
        }
        with open('nda_records.json', 'a') as f:
            f.write(json.dumps(record) + '\n')
        return record

    def check_status(self, entity):
        try:
            with open('nda_records.json') as f:
                for line in f:
                    rec = json.loads(line)
                    if rec['entity'] == entity:
                        return rec['status']
        except FileNotFoundError:
            return 'not signed'
        return 'not signed'
