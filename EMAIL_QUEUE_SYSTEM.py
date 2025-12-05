#!/usr/bin/env python3
"""
🚀 FISH MUSIC EMAIL QUEUE SYSTEM
Handles bulk emails, scheduled sends, rate limiting, and newsletter campaigns
"""

import json
import time
import threading
from datetime import datetime, timedelta
from queue import Queue, PriorityQueue
import os
from ULTIMATE_FISH_MAILER import UltimateFishMailer

class EmailQueue:
    """Advanced email queue with scheduling and rate limiting"""
    
    def __init__(self):
        self.mailer = UltimateFishMailer()
        self.queue = PriorityQueue()
        self.running = False
        self.worker_thread = None
        self.rate_limit = 10  # emails per minute
        self.sent_times = []
        
    def add_to_queue(self, email_data, priority=5, schedule_time=None):
        """
        Add email to queue
        priority: 1-10 (1=highest, 10=lowest)
        schedule_time: datetime object or None for immediate
        """
        if schedule_time is None:
            schedule_time = datetime.now()
        
        email_job = {
            'id': f"{int(time.time() * 1000)}",
            'schedule_time': schedule_time,
            'priority': priority,
            'data': email_data,
            'attempts': 0,
            'max_attempts': 3
        }
        
        # Priority queue uses (priority, secondary_sort, item)
        self.queue.put((
            priority,
            schedule_time.timestamp(),
            email_job
        ))
        
        self.save_queue_state()
        return email_job['id']
    
    def add_bulk_emails(self, recipients, email_type, **kwargs):
        """Add multiple emails at once"""
        job_ids = []
        
        for i, recipient in enumerate(recipients):
            email_data = {
                'type': email_type,
                'to': recipient['email'],
                'name': recipient.get('name', 'Customer'),
                **kwargs
            }
            
            # Spread bulk sends over time to avoid rate limits
            schedule_time = datetime.now() + timedelta(seconds=i * 6)  # 10/minute
            
            job_id = self.add_to_queue(email_data, priority=5, schedule_time=schedule_time)
            job_ids.append(job_id)
        
        print(f"✅ Added {len(recipients)} emails to queue")
        return job_ids
    
    def send_newsletter(self, subscribers, subject, content_text, content_html):
        """Send newsletter to all subscribers"""
        recipients = []
        for sub in subscribers:
            recipients.append({
                'email': sub['email'],
                'name': sub.get('name', 'Friend')
            })
        
        return self.add_bulk_emails(
            recipients,
            'newsletter',
            subject=subject,
            text=content_text,
            html=content_html
        )
    
    def start_worker(self):
        """Start the queue worker thread"""
        if self.running:
            print("⚠️  Worker already running")
            return
        
        self.running = True
        self.worker_thread = threading.Thread(target=self._process_queue, daemon=True)
        self.worker_thread.start()
        print("✅ Email queue worker started")
    
    def stop_worker(self):
        """Stop the queue worker"""
        self.running = False
        if self.worker_thread:
            self.worker_thread.join(timeout=5)
        print("⏹️  Email queue worker stopped")
    
    def _process_queue(self):
        """Process emails from queue"""
        while self.running:
            try:
                if not self.queue.empty():
                    priority, timestamp, job = self.queue.get(timeout=1)
                    
                    # Check if scheduled time has arrived
                    if datetime.fromtimestamp(timestamp) > datetime.now():
                        # Put it back and wait
                        self.queue.put((priority, timestamp, job))
                        time.sleep(1)
                        continue
                    
                    # Check rate limit
                    while not self._check_rate_limit():
                        time.sleep(1)
                    
                    # Send email
                    success = self._send_email(job)
                    
                    if not success and job['attempts'] < job['max_attempts']:
                        # Retry with lower priority
                        job['attempts'] += 1
                        job['schedule_time'] = datetime.now() + timedelta(minutes=5)
                        self.queue.put((
                            priority + 1,
                            job['schedule_time'].timestamp(),
                            job
                        ))
                        print(f"🔄 Retrying email {job['id']} (attempt {job['attempts']})")
                else:
                    time.sleep(1)
            
            except Exception as e:
                print(f"❌ Queue worker error: {e}")
                time.sleep(1)
    
    def _check_rate_limit(self):
        """Check if we're within rate limits"""
        now = time.time()
        # Remove sends older than 1 minute
        self.sent_times = [t for t in self.sent_times if now - t < 60]
        
        if len(self.sent_times) >= self.rate_limit:
            return False
        
        return True
    
    def _send_email(self, job):
        """Send a single email from job data"""
        try:
            data = job['data']
            email_type = data.get('type')
            
            if email_type == 'receipt':
                success = self.mailer.send_purchase_receipt(
                    data['to'],
                    data['name'],
                    data['track'],
                    data['price'],
                    data['order_id']
                )
            
            elif email_type == 'download':
                success = self.mailer.send_download_link(
                    data['to'],
                    data['name'],
                    data['track'],
                    data['url']
                )
            
            elif email_type == 'welcome':
                success = self.mailer.send_welcome(
                    data['to'],
                    data['name']
                )
            
            elif email_type == 'newsletter':
                success = self.mailer.send_email_bulletproof(
                    data['to'],
                    data['subject'],
                    data['text'].replace('{{name}}', data['name']),
                    data['html'].replace('{{name}}', data['name'])
                )
            
            elif email_type == 'custom':
                success = self.mailer.send_email_bulletproof(
                    data['to'],
                    data['subject'],
                    data['text'],
                    data.get('html')
                )
            
            else:
                print(f"❌ Unknown email type: {email_type}")
                return False
            
            if success:
                self.sent_times.append(time.time())
                print(f"✅ Sent email {job['id']} to {data['to']}")
            
            return success
        
        except Exception as e:
            print(f"❌ Error sending email {job['id']}: {e}")
            return False
    
    def save_queue_state(self):
        """Save queue state to file"""
        state = {
            'queue_size': self.queue.qsize(),
            'running': self.running,
            'rate_limit': self.rate_limit
        }
        
        with open('queue_state.json', 'w') as f:
            json.dump(state, f, indent=2)
    
    def get_stats(self):
        """Get queue statistics"""
        return {
            'queue_size': self.queue.qsize(),
            'running': self.running,
            'rate_limit': self.rate_limit,
            'recent_sends': len(self.sent_times)
        }

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print("🚀 FISH MUSIC EMAIL QUEUE SYSTEM")
    print("=" * 60)
    
    queue = EmailQueue()
    
    if len(sys.argv) < 2:
        print("""
USAGE:
  Start queue worker:
    python3 EMAIL_QUEUE_SYSTEM.py start
  
  Add single email to queue:
    python3 EMAIL_QUEUE_SYSTEM.py add-receipt email@test.com "John" "Track" 9.99 "ORD123"
  
  Send newsletter (from JSON file):
    python3 EMAIL_QUEUE_SYSTEM.py newsletter subscribers.json "Subject" "Text" "HTML"
  
  Queue stats:
    python3 EMAIL_QUEUE_SYSTEM.py stats
        """)
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "start":
        print("Starting queue worker (Ctrl+C to stop)...")
        queue.start_worker()
        try:
            while True:
                time.sleep(1)
                if queue.queue.qsize() > 0:
                    stats = queue.get_stats()
                    print(f"📊 Queue: {stats['queue_size']} | Recent: {stats['recent_sends']}")
        except KeyboardInterrupt:
            print("\n🛑 Stopping...")
            queue.stop_worker()
    
    elif command == "add-receipt":
        email_data = {
            'type': 'receipt',
            'to': sys.argv[2],
            'name': sys.argv[3],
            'track': sys.argv[4],
            'price': float(sys.argv[5]),
            'order_id': sys.argv[6]
        }
        job_id = queue.add_to_queue(email_data)
        print(f"✅ Added to queue: {job_id}")
    
    elif command == "stats":
        stats = queue.get_stats()
        print(f"""
📊 QUEUE STATISTICS:
  Queue Size: {stats['queue_size']}
  Worker Running: {stats['running']}
  Rate Limit: {stats['rate_limit']}/minute
  Recent Sends: {stats['recent_sends']}
        """)
    
    else:
        print(f"❌ Unknown command: {command}")

