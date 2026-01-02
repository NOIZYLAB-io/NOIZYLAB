from typing import Optional
# MissionControl96 NDA Manager
# World-class digital NDA workflow and enforcement

import datetime, json, asyncio
from cryptography.fernet import Fernet

class SecureStorage:
    def __init__(self, key_path: str = 'nda_key.key') -> None:
        try:
            with open(key_path, 'rb') as f:
                self.key = f.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            with open(key_path, 'wb') as f:
                f.write(self.key)
        self.cipher = Fernet(self.key)

    async def write(self, filename: str, data: dict[str, str]) -> None:
        enc = self.cipher.encrypt(json.dumps(data).encode())
        async with aiofiles.open(filename, 'ab') as f:
            await f.write(enc + b'\n')

    async def read_all(self, filename: str) -> list[dict[str, str]]:
        try:
            async with aiofiles.open(filename, 'rb') as f:
                lines = await f.readlines()
            return [json.loads(self.cipher.decrypt(line.strip())) for line in lines]
        except FileNotFoundError:
            return []

# NOTE: Requires aiofiles package for async file operations
import aiofiles  # type: ignore


class NDAManager:
    def __init__(self) -> None:
        self.storage = SecureStorage()

    def get_template(self) -> str:
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

    async def record_signature(self, entity: str, signed_by: str, timestamp: Optional[str] = None) -> dict[str, str]:
        if not timestamp:
            timestamp = datetime.datetime.now().isoformat()
        record = {
            'entity': entity,
            'signed_by': signed_by,
            'timestamp': timestamp,
            'status': 'signed'
        }
        await self.storage.write('nda_records.secure', record)
        return record

    async def check_status(self, entity: str) -> str:
        records = await self.storage.read_all('nda_records.secure')
        for rec in records:
            if rec['entity'] == entity:
                return rec['status']
        return 'not signed'

if __name__ == '__main__':
    import asyncio
    nda = NDAManager()
    print(nda.get_template())
    async def test():
        print(await nda.record_signature('FutureAI', 'John Doe'))
        print(await nda.check_status('FutureAI'))
    asyncio.run(test())
