#!/usr/bin/env python3
"""
Security Enhancements - Encryption and Secure Storage
====================================================
"""

import base64
import os
from cryptography.fernet import Fernet
from pathlib import Path
from rich.console import Console

console = Console()

class SecureStorage:
    """Encrypt sensitive data"""
    
    def __init__(self, key_file: str = "config/.encryption_key"):
        """Initialize Secure Storage"""
        self.key_file = Path(key_file)
        self.key_file.parent.mkdir(parents=True, exist_ok=True)
        self.key = self._get_or_create_key()
        self.cipher = Fernet(self.key)
    
    def _get_or_create_key(self) -> bytes:
        """Get existing key or create new one"""
        if self.key_file.exists():
            with open(self.key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            # Set restrictive permissions
            os.chmod(self.key_file, 0o600)
            return key
    
    def encrypt(self, data: str) -> str:
        """Encrypt data"""
        encrypted = self.cipher.encrypt(data.encode())
        return base64.b64encode(encrypted).decode()
    
    def decrypt(self, encrypted_data: str) -> str:
        """Decrypt data"""
        try:
            decoded = base64.b64decode(encrypted_data.encode())
            decrypted = self.cipher.decrypt(decoded)
            return decrypted.decode()
        except Exception as e:
            console.print(f"[red]❌ Decryption failed: {e}[/red]")
            return ""
    
    def encrypt_password(self, password: str) -> str:
        """Encrypt password for storage"""
        return self.encrypt(password)
    
    def decrypt_password(self, encrypted_password: str) -> str:
        """Decrypt password from storage"""
        return self.decrypt(encrypted_password)

