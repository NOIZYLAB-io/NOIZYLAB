#!/usr/bin/env python3
"""
AI-Enhanced Audio Organizer with Claude Integration
Uses Claude AI for intelligent categorization, metadata extraction, and suggestions
"""

import os
import json
import sqlite3
import hashlib
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import mutagen
from mutagen.wave import WAVE
from mutagen.id3 import ID3, ID3NoHeaderError
import logging
import sys

# Add NOIZYLAB to path for Claude integration
sys.path.insert(0, str(Path.home() / 'NOIZYLAB'))
try:
    from claude_integration import get_api_key, get_workspace_path, is_enabled
    CLAUDE_AVAILABLE = True
except ImportError:
    CLAUDE_AVAILABLE = False
    logging.warning("Claude integration not available")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class AIEnhancedOrganizer:
    def __init__(self, source_dir, destination_dir=None, use_ai=True):
        self.source_dir = Path(source_dir)
        self.destination_dir = Path(destination_dir) if destination_dir else Path.home() / 'NOIZYLAB' / 'Audio'
        self.use_ai = use_ai and CLAUDE_AVAILABLE
        self.api_key = get_api_key() if CLAUDE_AVAILABLE else None
        
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'ai_suggestions': 0,
            'ai_categorized': 0,
            'errors': 0
        }
        
        self.metadata_list = []
    
    def ask_claude(self, prompt, context=None):
        """Ask Claude AI for categorization or metadata suggestions."""
        if not self.use_ai or not self.api_key:
            return None
        
        try:
            import anthropic
            
            client = anthropic.Anthropic(api_key=self.api_key)
            
            full_prompt = f"""You are an expert audio file organizer. {prompt}
            
Context: {context if context else 'No additional context'}
            
Provide a JSON response with:
- category: best category name
- subcategory: specific subcategory
- tags: array of relevant tags
- description: improved description
- confidence: 0.0-1.0 confidence score
"""
            
            message = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=500,
                messages=[{
                    "role": "user",
                    "content": full_prompt
                }]
            )
            
            response_text = message.content[0].text
            
            # Try to extract JSON
            try:
                # Find JSON in response
                json_start = response_text.find('{')
                json_end = response_text.rfind('}') + 1
                if json_start >= 0 and json_end > json_start:
                    json_str = response_text[json_start:json_end]
                    return json.loads(json_str)
            except:
                pass
            
            return {'suggestion': response_text}
        
        except ImportError:
            logging.warning("anthropic library not installed. Install with: pip install anthropic")
            return None
        except Exception as e:
            logging.error(f"Claude API error: {e}")
            return None
    
    def ai_categorize_file(self, filename, file_info=None):
        """Use Claude AI to categorize a file."""
        prompt = f"""Analyze this audio filename and suggest the best categorization:
Filename: {filename}

Categories available: Crowd, Traffic, Footsteps, Aircraft, Ambience, Water, Nature, Music, Industry, Sports, Restaurant, City, Party

Provide categorization in JSON format."""
        
        context = f"File size: {file_info.get('size', 0) if file_info else 'unknown'} bytes" if file_info else None
        
        result = self.ask_claude(prompt, context)
        
        if result:
            self.stats['ai_categorized'] += 1
            return result
        
        return None
    
    def ai_suggest_metadata(self, filename, existing_metadata=None):
        """Use Claude AI to suggest improved metadata."""
        prompt = f"""Improve and enhance metadata for this audio file:
Filename: {filename}
Existing metadata: {json.dumps(existing_metadata) if existing_metadata else 'None'}

Suggest:
- Better title/description
- Relevant tags
- Keywords
- Category improvements
- Any missing metadata

Provide in JSON format."""
        
        result = self.ask_claude(prompt)
        
        if result:
            self.stats['ai_suggestions'] += 1
            return result
        
        return None
    
    def extract_metadata_hybrid(self, filename, filepath):
        """Extract metadata using both pattern matching and AI."""
        # First, use pattern matching (fast)
        metadata = self.pattern_based_extraction(filename)
        
        # Then enhance with AI if enabled
        if self.use_ai:
            ai_result = self.ai_categorize_file(filename, {'size': filepath.stat().st_size if filepath.exists() else 0})
            
            if ai_result:
                # Merge AI suggestions
                if ai_result.get('category'):
                    metadata['category'] = ai_result['category']
                if ai_result.get('subcategory'):
                    metadata['subcategory'] = ai_result['subcategory']
                if ai_result.get('tags'):
                    metadata['tags'].extend(ai_result['tags'])
                if ai_result.get('description'):
                    metadata['description'] = ai_result['description']
                metadata['ai_confidence'] = ai_result.get('confidence', 0.0)
                metadata['ai_enhanced'] = True
        
        return metadata
    
    def pattern_based_extraction(self, filename):
        """Fast pattern-based metadata extraction."""
        import re
        
        metadata = {
            'original_filename': filename,
            'category': None,
            'subcategory': None,
            'tags': [],
            'description': filename,
            'ai_enhanced': False
        }
        
        name_lower = filename.lower()
        
        # Quick pattern matching
        patterns = {
            'Crowd': ['crowd', 'audience', 'applause'],
            'Traffic': ['traffic', 'car', 'vehicle'],
            'Footsteps': ['footstep', 'walking'],
            'Aircraft': ['aircraft', 'airplane', 'jet'],
            'Ambience': ['ambience', 'atmosphere'],
            'Water': ['water', 'rain', 'ocean'],
            'Music': ['music', 'instrument']
        }
        
        for category, keywords in patterns.items():
            if any(kw in name_lower for kw in keywords):
                metadata['category'] = category
                break
        
        return metadata
    
    def process_file(self, filepath):
        """Process a single file with AI enhancement."""
        try:
            filename = filepath.name
            
            # Extract metadata (hybrid: pattern + AI)
            metadata = self.extract_metadata_hybrid(filename, filepath)
            
            # Get audio info
            audio_info = self.get_audio_info(filepath)
            
            # Merge metadata
            full_metadata = {
                **metadata,
                **audio_info,
                'file_path': str(filepath),
                'file_name': filename,
                'processed_date': datetime.now().isoformat()
            }
            
            self.metadata_list.append(full_metadata)
            self.stats['processed'] += 1
            
            return full_metadata
        
        except Exception as e:
            logging.error(f"Error processing {filepath}: {e}")
            self.stats['errors'] += 1
            return None
    
    def get_audio_info(self, filepath):
        """Get audio file information."""
        info = {
            'file_size': filepath.stat().st_size if filepath.exists() else 0,
            'duration': None,
            'sample_rate': None,
            'channels': None
        }
        
        try:
            audio = mutagen.File(filepath)
            if audio and hasattr(audio, 'info'):
                info['duration'] = audio.info.length if hasattr(audio.info, 'length') else None
                info['sample_rate'] = audio.info.sample_rate if hasattr(audio.info, 'sample_rate') else None
                info['channels'] = audio.info.channels if hasattr(audio.info, 'channels') else None
        except:
            pass
        
        return info
    
    def organize_files(self, max_workers=8):
        """Organize files with AI enhancement."""
        logging.info("=" * 80)
        logging.info("AI-ENHANCED AUDIO ORGANIZER")
        logging.info("=" * 80)
        logging.info(f"AI Mode: {'ENABLED' if self.use_ai else 'DISABLED'}")
        
        # Find files
        wav_files = list(self.source_dir.glob('*.wav')) + \
                    list(self.source_dir.glob('*.WAV'))
        
        self.stats['total_files'] = len(wav_files)
        logging.info(f"Found {self.stats['total_files']} files")
        
        # Process files
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.process_file, f): f for f in wav_files}
            
            for future in as_completed(futures):
                pass  # Results stored in metadata_list
        
        # Organize files
        self.move_files()
        
        # Generate report
        self.generate_report()
    
    def move_files(self):
        """Move files to organized structure."""
        self.destination_dir.mkdir(parents=True, exist_ok=True)
        
        for metadata in self.metadata_list:
            try:
                category = metadata.get('category', 'Uncategorized')
                dest_dir = self.destination_dir / category
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                source_path = Path(metadata['file_path'])
                dest_path = dest_dir / source_path.name
                
                if not dest_path.exists():
                    shutil.move(str(source_path), str(dest_path))
                    logging.info(f"Moved: {source_path.name} → {category}/")
            except Exception as e:
                logging.error(f"Error moving {metadata.get('file_name')}: {e}")
    
    def generate_report(self):
        """Generate organization report."""
        logging.info("\n" + "=" * 80)
        logging.info("ORGANIZATION COMPLETE")
        logging.info("=" * 80)
        logging.info(f"Total files: {self.stats['total_files']}")
        logging.info(f"Processed: {self.stats['processed']}")
        logging.info(f"AI categorized: {self.stats['ai_categorized']}")
        logging.info(f"AI suggestions: {self.stats['ai_suggestions']}")
        logging.info(f"Errors: {self.stats['errors']}")
        logging.info("=" * 80)


def main():
    """Main execution."""
    source_dir = "/Volumes/4TB_Utility/Waves To Sort"
    destination_dir = Path.home() / 'NOIZYLAB' / 'Audio'
    
    organizer = AIEnhancedOrganizer(source_dir, destination_dir, use_ai=True)
    organizer.organize_files(max_workers=8)

if __name__ == '__main__':
    main()

