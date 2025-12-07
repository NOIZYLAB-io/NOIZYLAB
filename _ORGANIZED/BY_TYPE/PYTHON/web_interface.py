#!/usr/bin/env python3
"""
Web-based interface for browsing and searching audio files.
Uses Flask for the web server and the SQLite database for fast queries.
"""

from flask import Flask, render_template, jsonify, request, send_file
import sqlite3
import json
from pathlib import Path
from collections import defaultdict

app = Flask(__name__)

DB_PATH = "/Volumes/4TB_Utility/Waves To Sort/audio_database.db"

def get_db_connection():
    """Get database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Main page."""
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    """Get overall statistics."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    stats = {
        'total_files': cursor.execute('SELECT COUNT(*) FROM audio_files').fetchone()[0],
        'categories': {},
        'locations': {},
        'types': {}
    }
    
    # Category stats
    for row in cursor.execute('SELECT category, COUNT(*) as count FROM audio_files WHERE category IS NOT NULL GROUP BY category'):
        stats['categories'][row['category']] = row['count']
    
    # Location stats
    for row in cursor.execute('SELECT location, COUNT(*) as count FROM audio_files WHERE location IS NOT NULL GROUP BY location'):
        stats['locations'][row['location']] = row['count']
    
    # Type stats
    for row in cursor.execute('SELECT type, COUNT(*) as count FROM audio_files WHERE type IS NOT NULL GROUP BY type'):
        stats['types'][row['type']] = row['count']
    
    conn.close()
    return jsonify(stats)

@app.route('/api/search')
def search():
    """Search audio files."""
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    location = request.args.get('location', '')
    file_type = request.args.get('type', '')
    limit = int(request.args.get('limit', 50))
    offset = int(request.args.get('offset', 0))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    conditions = []
    params = []
    
    if query:
        conditions.append('(filename LIKE ? OR description LIKE ? OR tags LIKE ? OR keywords LIKE ?)')
        search_term = f'%{query}%'
        params.extend([search_term, search_term, search_term, search_term])
    
    if category:
        conditions.append('category = ?')
        params.append(category)
    
    if location:
        conditions.append('location = ?')
        params.append(location)
    
    if file_type:
        conditions.append('type = ?')
        params.append(file_type)
    
    where_clause = ' AND '.join(conditions) if conditions else '1=1'
    
    sql = f'''
        SELECT * FROM audio_files 
        WHERE {where_clause}
        ORDER BY filename
        LIMIT ? OFFSET ?
    '''
    params.extend([limit, offset])
    
    results = []
    for row in cursor.execute(sql, params):
        results.append(dict(row))
    
    # Get total count
    count_sql = f'SELECT COUNT(*) FROM audio_files WHERE {where_clause}'
    total = cursor.execute(count_sql, params[:-2]).fetchone()[0]
    
    conn.close()
    
    return jsonify({
        'results': results,
        'total': total,
        'limit': limit,
        'offset': offset
    })

@app.route('/api/categories')
def get_categories():
    """Get all categories."""
    conn = get_db_connection()
    cursor = conn.cursor()
    categories = [row[0] for row in cursor.execute('SELECT DISTINCT category FROM audio_files WHERE category IS NOT NULL ORDER BY category')]
    conn.close()
    return jsonify(categories)

@app.route('/api/locations')
def get_locations():
    """Get all locations."""
    conn = get_db_connection()
    cursor = conn.cursor()
    locations = [row[0] for row in cursor.execute('SELECT DISTINCT location FROM audio_files WHERE location IS NOT NULL ORDER BY location')]
    conn.close()
    return jsonify(locations)

@app.route('/api/file/<int:file_id>')
def get_file_details(file_id):
    """Get detailed information about a specific file."""
    conn = get_db_connection()
    cursor = conn.cursor()
    file_data = cursor.execute('SELECT * FROM audio_files WHERE id = ?', (file_id,)).fetchone()
    conn.close()
    
    if file_data:
        return jsonify(dict(file_data))
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

