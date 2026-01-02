#!/usr/bin/env python3
"""
Power BI Export Utility - Standalone script for Power BI exports
"""

import sqlite3
import pandas as pd
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

# Get parent directory for default paths
_parent_dir_api = Path(__file__).parent.parent
_default_db_path_api = str(_parent_dir_api / "data" / "email_intelligence.db")

def export_to_powerbi(db_path: str = None, output_file: str = "powerbi_export.csv"):
    """Export email data to Power BI optimized CSV"""
    
    if db_path is None:
        db_path = _default_db_path_api
    
    if not Path(db_path).exists():
        console.print(f"[red]Database not found: {db_path}[/red]")
        return False
    
    conn = sqlite3.connect(db_path)
    
    # Power BI optimized query
    query = """
        SELECT 
            id,
            email,
            category,
            spam_score * 100 as spam_score_percent,
            validity_score * 100 as validity_score_percent,
            is_disposable,
            language_detected,
            company_name,
            confidence_score,
            processed_at,
            updated_at,
            json_extract(enriched_info, '$.enrichment') as enrichment,
            json_extract(enriched_info, '$.spam_indicators') as spam_indicators,
            json_extract(enriched_info, '$.category') as ai_category
        FROM email_list
        ORDER BY processed_at DESC
    """
    
    try:
        df = pd.read_sql_query(query, conn)
        
        # Format dates
        df['processed_at'] = pd.to_datetime(df['processed_at'])
        df['updated_at'] = pd.to_datetime(df['updated_at'])
        
        # Fill NaN values
        df['spam_score_percent'] = df['spam_score_percent'].fillna(0)
        df['validity_score_percent'] = df['validity_score_percent'].fillna(0)
        df['confidence_score'] = df['confidence_score'].fillna(0)
        
        # Export
        df.to_csv(output_file, index=False)
        
        # Summary
        table = Table(title="Power BI Export Summary")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_row("File", output_file)
        table.add_row("Total Rows", str(len(df)))
        table.add_row("Categories", str(df['category'].nunique()))
        table.add_row("Avg Spam Score", f"{df['spam_score_percent'].mean():.2f}%")
        table.add_row("Avg Validity", f"{df['validity_score_percent'].mean():.2f}%")
        table.add_row("Disposable Emails", str(df['is_disposable'].sum()))
        
        console.print(table)
        console.print(f"[green]✅ Exported to {output_file}[/green]")
        
        return True
    
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return False
    
    finally:
        conn.close()

if __name__ == "__main__":
    import sys
    
    db_path = sys.argv[1] if len(sys.argv) > 1 else _default_db_path_api
    output_file = sys.argv[2] if len(sys.argv) > 2 else "powerbi_export.csv"
    
    export_to_powerbi(db_path, output_file)

