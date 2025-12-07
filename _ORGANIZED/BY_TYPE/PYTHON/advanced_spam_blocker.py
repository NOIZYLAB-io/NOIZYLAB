#!/usr/bin/env python3

import subprocess
import re
import json
import sqlite3
import os
import time
from datetime import datetime, timedelta
import hashlib

class iMessageSpamBlocker:
    def __init__(self):
        self.home_dir = os.path.expanduser("~")
        self.chat_db = f"{self.home_dir}/Library/Messages/chat.db"
        self.spam_patterns = [
            r'\b(?:free|win|winner|congratulations)\b.*\b(?:money|prize|gift)\b',
            r'\b(?:click|tap)\s+(?:here|link|url)\b',
            r'\b(?:verify|confirm|update)\s+(?:account|identity|payment)\b',
            r'\b(?:suspended|locked|expired)\s+account\b',
            r'\$\d+[\d,]*(?:\.\d{2})?\s*(?:free|win|earned)',
            r'\b(?:bitcoin|crypto|investment)\s+(?:opportunity|offer)\b',
            r'\bact\s+(?:now|immediately|fast|quick)\b',
            r'(?:\+1-?)?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}',  # Phone numbers
            r'https?://(?:bit\.ly|tinyurl|goo\.gl|t\.co)/',  # Shortened URLs
        ]
        
        self.spam_keywords = {
            'financial': ['bitcoin', 'cryptocurrency', 'investment', 'money', 'cash', 'profit'],
            'urgency': ['urgent', 'immediate', 'asap', 'hurry', 'limited time', 'expires'],
            'verification': ['verify', 'confirm', 'update', 'suspended', 'locked', 'expired'],
            'prizes': ['winner', 'won', 'prize', 'gift', 'free', 'congratulations'],
            'links': ['click here', 'tap here', 'visit', 'go to', 'check out']
        }
        
        self.blocked_numbers = set()
        self.spam_score_threshold = 3
        
    def calculate_spam_score(self, message_text, sender):
        """Calculate spam probability score (0-10)"""
        score = 0
        message_lower = message_text.lower()
        
        # Pattern matching
        for pattern in self.spam_patterns:
            if re.search(pattern, message_text, re.IGNORECASE):
                score += 2
        
        # Keyword detection
        for category, keywords in self.spam_keywords.items():
            keyword_count = sum(1 for keyword in keywords if keyword in message_lower)
            if keyword_count > 0:
                score += keyword_count
        
        # Check for excessive caps
        if len(re.findall(r'[A-Z]', message_text)) > len(message_text) * 0.5:
            score += 1
        
        # Check for excessive punctuation
        if len(re.findall(r'[!?]{2,}', message_text)) > 0:
            score += 1
        
        # Check if sender is unknown (not in contacts)
        if not self.is_in_contacts(sender):
            score += 1
        
        # Check for repeated characters
        if re.search(r'(.)\1{3,}', message_text):
            score += 1
        
        return min(score, 10)  # Cap at 10
    
    def is_in_contacts(self, phone_number):
        """Check if sender is in contacts"""
        try:
            result = subprocess.run([
                'osascript', '-e', 
                f'tell application "Contacts" to return (count of people whose phones contains "{phone_number}") > 0'
            ], capture_output=True, text=True)
            return result.stdout.strip() == 'true'
        except:
            return False
    
    def block_sender(self, phone_number):
        """Block a phone number using AppleScript"""
        try:
            applescript = f'''
            tell application "Messages"
                try
                    set targetBuddy to buddy "{phone_number}"
                    block targetBuddy
                    return "Blocked: {phone_number}"
                on error errMsg
                    return "Error blocking {phone_number}: " & errMsg
                end try
            end tell
            '''
            
            result = subprocess.run(['osascript', '-e', applescript], 
                                  capture_output=True, text=True)
            
            if "Blocked:" in result.stdout:
                self.blocked_numbers.add(phone_number)
                self.log_action("BLOCKED", phone_number, "Sender blocked successfully")
                return True
            else:
                self.log_action("BLOCK_FAILED", phone_number, result.stdout)
                return False
                
        except Exception as e:
            self.log_action("BLOCK_ERROR", phone_number, str(e))
            return False
    
    def delete_message(self, message_guid):
        """Delete a specific message"""
        try:
            applescript = f'''
            tell application "Messages"
                try
                    delete message id "{message_guid}"
                    return "Deleted message: {message_guid}"
                on error errMsg
                    return "Error deleting message: " & errMsg
                end try
            end tell
            '''
            
            result = subprocess.run(['osascript', '-e', applescript], 
                                  capture_output=True, text=True)
            return "Deleted message:" in result.stdout
            
        except Exception as e:
            self.log_action("DELETE_ERROR", message_guid, str(e))
            return False
    
    def log_action(self, action, target, details):
        """Log spam blocking actions"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {action}: {target} - {details}\n"
        
        with open("imessage_spam_log.txt", "a") as log_file:
            log_file.write(log_entry)
        
        print(log_entry.strip())
    
    def send_notification(self, title, message):
        """Send macOS notification"""
        try:
            subprocess.run([
                'osascript', '-e', 
                f'display notification "{message}" with title "{title}" sound name "Funk"'
            ])
        except:
            pass
    
    def get_recent_messages(self, minutes=5):
        """Get recent messages from Messages database"""
        try:
            # Note: This requires Full Disk Access permission
            conn = sqlite3.connect(self.chat_db)
            cursor = conn.cursor()
            
            # Get messages from last X minutes
            cutoff_time = int((datetime.now() - timedelta(minutes=minutes)).timestamp() * 1000000000)
            
            query = '''
            SELECT 
                message.ROWID,
                message.guid,
                message.text,
                handle.id as sender,
                message.date
            FROM message
            LEFT JOIN handle ON message.handle_id = handle.ROWID
            WHERE message.date > ? AND message.text IS NOT NULL
            ORDER BY message.date DESC
            '''
            
            cursor.execute(query, (cutoff_time,))
            messages = cursor.fetchall()
            conn.close()
            
            return messages
            
        except Exception as e:
            self.log_action("DB_ERROR", "database", str(e))
            return []
    
    def process_message(self, message_data):
        """Process a single message for spam"""
        row_id, guid, text, sender, date = message_data
        
        if not text or not sender:
            return
        
        spam_score = self.calculate_spam_score(text, sender)
        
        print(f"\n📧 Message from {sender}")
        print(f"📝 Content: {text[:100]}...")
        print(f"🎯 Spam Score: {spam_score}/10")
        
        if spam_score >= self.spam_score_threshold:
            print(f"⚠️ SPAM DETECTED! (Score: {spam_score})")
            
            # Block the sender
            if self.block_sender(sender):
                print(f"🚫 Blocked: {sender}")
            
            # Delete the message
            if self.delete_message(guid):
                print(f"🗑️ Deleted message: {guid}")
            
            # Log the action
            self.log_action("SPAM_BLOCKED", sender, f"Score: {spam_score}, Text: {text[:50]}...")
            
            # Send notification
            self.send_notification("Spam Blocked", f"Blocked spam from {sender}")
            
        else:
            print("✅ Message appears legitimate")
    
    def start_monitoring(self):
        """Start the spam monitoring system"""
        print("🚀 iMessage Spam Blocker Started")
        print(f"📊 Spam threshold: {self.spam_score_threshold}/10")
        print("👁️ Monitoring messages...")
        
        while True:
            try:
                messages = self.get_recent_messages(1)  # Check last minute
                
                for message in messages:
                    self.process_message(message)
                
                time.sleep(30)  # Check every 30 seconds
                
            except KeyboardInterrupt:
                print("\n🛑 Spam blocker stopped by user")
                break
            except Exception as e:
                self.log_action("MONITOR_ERROR", "system", str(e))
                time.sleep(60)  # Wait longer on error

if __name__ == "__main__":
    blocker = iMessageSpamBlocker()
    blocker.start_monitoring()