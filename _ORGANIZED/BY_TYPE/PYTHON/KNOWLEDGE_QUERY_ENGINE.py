#!/usr/bin/env python3
"""
🔥 CB_01 KNOWLEDGE QUERY ENGINE 🔥
Ultimate search and retrieval system for all NOIZYLAB knowledge

GORUNFREE!!!
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict

class KnowledgeEngine:
    """OMNISCIENT KNOWLEDGE SEARCH ENGINE"""
    
    def __init__(self, workspace_path):
        self.workspace = Path(workspace_path)
        self.docs_path = self.workspace / "Documentation"
        self.knowledge_path = self.workspace / "Knowledge"
        self.index = self._build_index()
    
    def _build_index(self):
        """Build searchable index of all knowledge"""
        print("🔥 Building omniscient knowledge index...")
        index = {
            'documents': {},
            'keywords': defaultdict(list),
            'topics': defaultdict(list)
        }
        
        # Index all markdown files
        if self.docs_path.exists():
            for md_file in self.docs_path.glob("*.md"):
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    words = re.findall(r'\b\w+\b', content.lower())
                    
                    index['documents'][md_file.name] = {
                        'path': str(md_file),
                        'size': md_file.stat().st_size,
                        'word_count': len(words),
                        'topics': self._extract_topics(content)
                    }
                    
                    # Build keyword index
                    for word in set(words):
                        if len(word) > 3:  # Skip short words
                            index['keywords'][word].append(md_file.name)
        
        # Index all JSON files
        if self.knowledge_path.exists():
            for json_file in self.knowledge_path.glob("*.json"):
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        index['documents'][json_file.name] = {
                            'path': str(json_file),
                            'size': json_file.stat().st_size,
                            'type': 'json',
                            'keys': self._extract_json_keys(data)
                        }
                except:
                    pass
        
        return index
    
    def _extract_topics(self, content):
        """Extract main topics from markdown content"""
        topics = []
        # Find all headers
        for line in content.split('\n'):
            if line.startswith('#'):
                topic = line.lstrip('#').strip()
                topics.append(topic)
        return topics[:10]  # Top 10 topics
    
    def _extract_json_keys(self, data, prefix=''):
        """Extract all keys from JSON recursively"""
        keys = []
        if isinstance(data, dict):
            for k, v in data.items():
                keys.append(prefix + k)
                if isinstance(v, (dict, list)):
                    keys.extend(self._extract_json_keys(v, prefix + k + '.'))
        elif isinstance(data, list) and data:
            if isinstance(data[0], dict):
                keys.extend(self._extract_json_keys(data[0], prefix))
        return keys[:50]  # Top 50 keys
    
    def search(self, query):
        """OMNISCIENT SEARCH - Find anything instantly"""
        query_lower = query.lower()
        results = {
            'query': query,
            'exact_matches': [],
            'partial_matches': [],
            'related_docs': []
        }
        
        # Search in document names
        for doc_name, doc_info in self.index['documents'].items():
            if query_lower in doc_name.lower():
                results['exact_matches'].append({
                    'file': doc_name,
                    'path': doc_info['path'],
                    'type': 'filename'
                })
        
        # Search in keywords
        for word in query_lower.split():
            if word in self.index['keywords']:
                for doc_name in self.index['keywords'][word]:
                    if doc_name not in [r['file'] for r in results['partial_matches']]:
                        results['partial_matches'].append({
                            'file': doc_name,
                            'path': self.index['documents'][doc_name]['path'],
                            'type': 'keyword',
                            'keyword': word
                        })
        
        return results
    
    def stats(self):
        """Get complete knowledge statistics"""
        total_docs = len(self.index['documents'])
        total_keywords = len(self.index['keywords'])
        
        md_files = [d for d in self.index['documents'].keys() if d.endswith('.md')]
        json_files = [d for d in self.index['documents'].keys() if d.endswith('.json')]
        
        return {
            'total_documents': total_docs,
            'markdown_files': len(md_files),
            'json_files': len(json_files),
            'total_keywords': total_keywords,
            'index_size': len(str(self.index))
        }
    
    def list_all(self):
        """List all available knowledge files"""
        print("\n" + "="*80)
        print("📚 COMPLETE KNOWLEDGE CATALOG")
        print("="*80)
        
        print("\n📖 DOCUMENTATION FILES:")
        for doc_name, info in sorted(self.index['documents'].items()):
            if doc_name.endswith('.md'):
                size_kb = info['size'] / 1024
                word_count = info.get('word_count', 0)
                print(f"  {doc_name:60s} {size_kb:6.1f}KB  {word_count:>6,} words")
        
        print("\n🗂️  KNOWLEDGE DATABASES:")
        for doc_name, info in sorted(self.index['documents'].items()):
            if doc_name.endswith('.json'):
                size_kb = info['size'] / 1024
                print(f"  {doc_name:60s} {size_kb:6.1f}KB")
        
        stats = self.stats()
        print("\n" + "="*80)
        print(f"TOTAL: {stats['total_documents']} files")
        print(f"  - Markdown: {stats['markdown_files']}")
        print(f"  - JSON: {stats['json_files']}")
        print(f"  - Keywords indexed: {stats['total_keywords']:,}")
        print("="*80)


def main():
    """Main execution"""
    print("="*80)
    print("🔥 CB_01 KNOWLEDGE QUERY ENGINE - OMNISCIENT SEARCH 🔥")
    print("="*80)
    
    # Get workspace path
    workspace = Path(__file__).parent.parent
    
    # Initialize engine
    engine = KnowledgeEngine(workspace)
    
    # Show statistics
    print(f"\n✅ Knowledge index built successfully!")
    stats = engine.stats()
    print(f"   - Documents indexed: {stats['total_documents']}")
    print(f"   - Keywords indexed: {stats['total_keywords']:,}")
    
    # Example usage
    print("\n" + "="*80)
    print("EXAMPLE SEARCHES:")
    print("="*80)
    
    # Search examples
    queries = ["composition", "film score", "nexus", "rob plowman", "revenue"]
    
    for query in queries:
        print(f"\n🔍 Searching: '{query}'")
        results = engine.search(query)
        
        if results['exact_matches']:
            print(f"   ✅ Exact matches: {len(results['exact_matches'])}")
            for match in results['exact_matches'][:3]:
                print(f"      - {match['file']}")
        
        if results['partial_matches']:
            print(f"   📌 Partial matches: {len(results['partial_matches'])}")
            for match in results['partial_matches'][:3]:
                print(f"      - {match['file']} (keyword: {match['keyword']})")
    
    # List all files
    engine.list_all()
    
    print("\n" + "="*80)
    print("🔥 KNOWLEDGE ENGINE READY - GORUNFREE!!! 🔥")
    print("="*80)
    print("\nUSAGE:")
    print("  from KNOWLEDGE_QUERY_ENGINE import KnowledgeEngine")
    print("  engine = KnowledgeEngine('/path/to/workspace')")
    print("  results = engine.search('your query')")
    print("  stats = engine.stats()")
    print("  engine.list_all()")
    print("="*80)


if __name__ == "__main__":
    main()

