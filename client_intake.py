import os, email, imaplib, time
from pathlib import Path
from .registry import register
from .base import BaseAgent

@register("agent17_client_intake")
class AgentClientIntake(BaseAgent):
    """Fetches client submissions from info@noizy.ai via IMAP, stores attachments, and summarizes."""
    def setup(self):
        self.intake_dir = Path("client_intake")
        self.intake_dir.mkdir(exist_ok=True)
        self.last_ids = set()

    def _connect(self):
        M = imaplib.IMAP4_SSL("imap.secureserver.net")
        M.login(os.getenv("CLIENT_INTAKE_EMAIL"), os.getenv("CLIENT_INTAKE_PASSWORD"))
        M.select("INBOX")
        return M

    def step(self):
        try:
            M = self._connect()
            _, data = M.search(None, "UNSEEN")
            for num in data[0].split():
                _, msg_data = M.fetch(num, "(RFC822)")
                msg = email.message_from_bytes(msg_data[0][1])
                sender = msg["From"]; subject = msg["Subject"]
                attachments = []
                for part in msg.walk():
                    if part.get_content_disposition() == "attachment":
                        fname = part.get_filename()
                        fpath = self.intake_dir / fname
                        with open(fpath, "wb") as f: f.write(part.get_payload(decode=True))
                        attachments.append(str(fpath))
                payload = {
                    "client": sender,
                    "subject": subject,
                    "attachments": attachments,
                    "timestamp": time.time()
                }
                self.bus.publish("client_intake", payload)
            M.logout()
        except Exception as e:
            self.bus.publish("client_intake", {"error": str(e)})