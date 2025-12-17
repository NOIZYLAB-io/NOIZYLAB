#!/usr/bin/env python3
"""
SenseMaker - AI-Powered File Classification System
Uses Claude AI to intelligently categorize files with dynamic category evolution
"""

import os
import sqlite3
import json
import logging
from typing import Dict, List, Optional, Tuple
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to import anthropic, make it optional
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    logger.warning("Anthropic library not available. AI classification disabled.")


class SenseMaker:
    """AI-powered file classifier with dynamic categories"""
    
    # Default category taxonomy
    DEFAULT_CATEGORIES = {
        'Audio': ['music', 'samples', 'loops', 'sfx', 'voice', 'podcast'],
        'Design': ['logos', 'layouts', 'mockups', 'illustrations', 'photos'],
        'Code': ['python', 'javascript', 'shell', 'config', 'notebook'],
        'Documents': ['contracts', 'invoices', 'reports', 'notes', 'presentations'],
        'Video': ['raw', 'edited', 'renders', 'motion_graphics'],
        'Archives': ['backups', 'compressed', 'installers'],
        'Misc': ['uncategorized', 'temporary']
    }
    
    def __init__(self, db_path: str, api_key: Optional[str] = None):
        self.db_path = db_path
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        self.client = None
        
        if ANTHROPIC_AVAILABLE and self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)
            logger.info("AI classification enabled")
        else:
            logger.warning("AI classification disabled (no API key or library)")
    
    def _get_file_context(self, file_path: str, extension: str, mime_type: str) -> str:
        """Build context string for AI classification"""
        context = f"File: {Path(file_path).name}\n"
        context += f"Extension: {extension}\n"
        context += f"MIME Type: {mime_type}\n"
        context += f"Directory: {Path(file_path).parent.name}\n"
        
        return context
    
    def _classify_with_rules(self, extension: str, mime_type: str) -> Tuple[str, float]:
        """Rule-based classification fallback"""
        ext = extension.lower()
        mime = (mime_type or '').lower()
        
        # Audio
        if ext in ['.mp3', '.wav', '.flac', '.aiff', '.m4a', '.ogg'] or 'audio' in mime:
            return 'Audio', 0.95
        
        # Design/Images
        if ext in ['.psd', '.ai', '.sketch', '.fig', '.png', '.jpg', '.jpeg', '.svg'] or 'image' in mime:
            return 'Design', 0.95
        
        # Video
        if ext in ['.mp4', '.mov', '.avi', '.mkv', '.webm'] or 'video' in mime:
            return 'Video', 0.95
        
        # Code
        if ext in ['.py', '.js', '.ts', '.sh', '.zsh', '.json', '.yaml', '.yml', '.xml']:
            return 'Code', 0.95
        
        # Documents
        if ext in ['.pdf', '.doc', '.docx', '.txt', '.md', '.rtf'] or 'text' in mime:
            return 'Documents', 0.90
        
        # Archives
        if ext in ['.zip', '.tar', '.gz', '.rar', '.7z', '.dmg', '.pkg']:
            return 'Archives', 0.95
        
        return 'Misc', 0.50
    
    def _classify_with_ai(self, file_context: str) -> Tuple[str, float]:
        """AI-powered classification using Claude"""
        if not self.client:
            return None, 0.0
        
        try:
            prompt = f"""Analyze this file and categorize it into ONE of these categories:
{json.dumps(list(self.DEFAULT_CATEGORIES.keys()), indent=2)}

File Information:
{file_context}

Respond with JSON only:
{{"category": "CategoryName", "confidence": 0.95, "reasoning": "brief explanation"}}"""

            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = message.content[0].text.strip()
            
            # Parse JSON response
            if response_text.startswith('```'):
                response_text = response_text.split('```')[1]
                if response_text.startswith('json'):
                    response_text = response_text[4:]
            
            result = json.loads(response_text.strip())
            return result.get('category', 'Misc'), result.get('confidence', 0.8)
            
        except Exception as e:
            logger.error(f"AI classification error: {e}")
            return None, 0.0
    
    def classify_file(self, file_path: str, use_ai: bool = True) -> Dict:
        """Classify a single file"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get file info from database
        cursor.execute('''
            SELECT extension, mime_type, size, filename
            FROM files WHERE path = ?
        ''', (file_path,))
        
        row = cursor.fetchone()
        if not row:
            conn.close()
            return {'error': 'File not found in database'}
        
        extension, mime_type, size, filename = row
        
        # Try AI classification first if enabled
        category, confidence = None, 0.0
        
        if use_ai and self.client:
            context = self._get_file_context(file_path, extension, mime_type)
            category, confidence = self._classify_with_ai(context)
        
        # Fallback to rule-based
        if not category or confidence < 0.7:
            category, confidence = self._classify_with_rules(extension, mime_type)
        
        # Update database
        cursor.execute('''
            UPDATE files 
            SET ai_category = ?, ai_confidence = ?
            WHERE path = ?
        ''', (category, confidence, file_path))
        
        conn.commit()
        conn.close()
        
        return {
            'path': file_path,
            'filename': filename,
            'category': category,
            'confidence': confidence
        }
    
    def classify_batch(self, limit: int = 100, use_ai: bool = True) -> List[Dict]:
        """Classify multiple unclassified files"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get unclassified files
        cursor.execute('''
            SELECT path FROM files 
            WHERE ai_category IS NULL 
            LIMIT ?
        ''', (limit,))
        
        paths = [row[0] for row in cursor.fetchall()]
        conn.close()
        
        logger.info(f"Classifying {len(paths)} files...")
        
        results = []
        for i, path in enumerate(paths, 1):
            result = self.classify_file(path, use_ai=use_ai)
            results.append(result)
            
            if i % 10 == 0:
                logger.info(f"Progress: {i}/{len(paths)}")
        
        return results
    
    def get_category_stats(self) -> Dict:
        """Get statistics by category"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT ai_category, COUNT(*), SUM(size), AVG(ai_confidence)
            FROM files
            WHERE ai_category IS NOT NULL
            GROUP BY ai_category
            ORDER BY COUNT(*) DESC
        ''')
        
        categories = []
        for row in cursor.fetchall():
            category, count, total_size, avg_conf = row
            categories.append({
                'category': category,
                'count': count,
                'size': total_size,
                'size_gb': round(total_size / (1024**3), 2),
                'avg_confidence': round(avg_conf, 2)
            })
        
        cursor.execute('''
            SELECT COUNT(*) FROM files WHERE ai_category IS NULL
        ''')
        unclassified = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'categories': categories,
            'unclassified': unclassified
        }
    
    def export_category_map(self, output_file: str):
        """Export category mapping to JSON"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT path, filename, ai_category, ai_confidence
            FROM files
            WHERE ai_category IS NOT NULL
        ''')
        
        mapping = {}
        for path, filename, category, confidence in cursor.fetchall():
            if category not in mapping:
                mapping[category] = []
            mapping[category].append({
                'path': path,
                'filename': filename,
                'confidence': confidence
            })
        
        conn.close()
        
        with open(output_file, 'w') as f:
            json.dump(mapping, f, indent=2)
        
        logger.info(f"Category map exported to {output_file}")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python sensemaker.py <database_path> [--ai] [--batch 100]")
        sys.exit(1)
    
    db_path = sys.argv[1]
    use_ai = '--ai' in sys.argv
    batch_size = 100
    
    if '--batch' in sys.argv:
        idx = sys.argv.index('--batch')
        if idx + 1 < len(sys.argv):
            batch_size = int(sys.argv[idx + 1])
    
    classifier = SenseMaker(db_path)
    
    print(f"\nClassifying {batch_size} files (AI: {use_ai})...")
    results = classifier.classify_batch(limit=batch_size, use_ai=use_ai)
    
    print(f"\nClassified {len(results)} files")
    print(f"\nCategory Statistics:")
    stats = classifier.get_category_stats()
    print(json.dumps(stats, indent=2))
