#!/usr/bin/env python3
"""
Email Intelligence CLI V2 - Enhanced with Advanced Features
==========================================================
- AI-powered email enrichment
- Multi-provider AI support (Gemini, Claude, OpenAI)
- Advanced spam detection
- Google Sheets sync
- Slack notifications
- Batch processing
- Real-time monitoring
"""

import sqlite3
import pandas as pd
import json
import re
import hashlib
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import asyncio
import aiohttp

# Rich for beautiful CLI
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.live import Live
from rich.layout import Layout

# AI Providers
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

try:
    import anthropic
    CLAUDE_AVAILABLE = True
except ImportError:
    CLAUDE_AVAILABLE = False

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Google Sheets
try:
    from googleapiclient.discovery import build
    from google.oauth2.service_account import Credentials
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False

# ML
try:
    import joblib
    import numpy as np
    from sklearn.ensemble import RandomForestClassifier
    ML_AVAILABLE = True
except ImportError:
    ML_AVAILABLE = False

# HTTP
import requests

console = Console()

# Configuration
class Config:
    DB_PATH = os.getenv("EMAIL_DB_PATH", "email_intelligence.db")
    API_KEY_GEMINI = os.getenv("GEMINI_API_KEY", "")
    API_KEY_CLAUDE = os.getenv("ANTHROPIC_API_KEY", "")
    API_KEY_OPENAI = os.getenv("OPENAI_API_KEY", "")
    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")
    GOOGLE_SHEETS_CREDENTIALS = os.getenv("GOOGLE_SHEETS_JSON", "google_sheets.json")
    GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "")
    AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")  # gemini, claude, openai
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", "50"))
    ENABLE_ML = os.getenv("ENABLE_ML", "true").lower() == "true"

config = Config()

# Initialize AI
ai_model = None
if config.AI_PROVIDER == "gemini" and GEMINI_AVAILABLE and config.API_KEY_GEMINI:
    genai.configure(api_key=config.API_KEY_GEMINI)
    ai_model = genai.GenerativeModel("gemini-1.5-flash")
elif config.AI_PROVIDER == "claude" and CLAUDE_AVAILABLE and config.API_KEY_CLAUDE:
    ai_model = anthropic.Anthropic(api_key=config.API_KEY_CLAUDE)
elif config.AI_PROVIDER == "openai" and OPENAI_AVAILABLE and config.API_KEY_OPENAI:
    ai_model = openai.OpenAI(api_key=config.API_KEY_OPENAI)

# Database setup
def init_database():
    """Initialize database with enhanced schema"""
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS email_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        category TEXT,
        enriched_info TEXT,
        spam_score REAL DEFAULT 0,
        validity_score REAL DEFAULT 0,
        is_disposable INTEGER DEFAULT 0,
        language_detected TEXT,
        company_name TEXT,
        confidence_score REAL DEFAULT 0,
        processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS processing_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        batch_id TEXT,
        total_emails INTEGER,
        valid_emails INTEGER,
        invalid_emails INTEGER,
        spam_emails INTEGER,
        processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_email ON email_list(email);
    CREATE INDEX IF NOT EXISTS idx_category ON email_list(category);
    CREATE INDEX IF NOT EXISTS idx_spam_score ON email_list(spam_score);
    """)
    
    conn.commit()
    return conn

# Email validation (enhanced)
def validate_email(email: str) -> Tuple[bool, str]:
    """Enhanced email validation"""
    if not email or not isinstance(email, str):
        return False, "Empty or invalid type"
    
    email = email.strip().lower()
    
    # Basic regex
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return False, "Invalid format"
    
    # Check for common issues
    if email.count("@") != 1:
        return False, "Multiple @ symbols"
    
    local, domain = email.split("@")
    
    if len(local) > 64:
        return False, "Local part too long"
    
    if len(domain) > 255:
        return False, "Domain too long"
    
    # Disposable email domains (common ones)
    disposable_domains = [
        "tempmail.com", "10minutemail.com", "guerrillamail.com",
        "mailinator.com", "throwaway.email", "temp-mail.org"
    ]
    
    if domain in disposable_domains:
        return True, "valid_disposable"
    
    return True, "valid"

# AI enrichment (multi-provider)
async def enrich_email_async(email: str, provider: str = None) -> Dict:
    """Enrich email using AI (async)"""
    provider = provider or config.AI_PROVIDER
    
    prompt = f"""
    Analyze this email address: {email}
    
    Return JSON with:
    - category: personal/business/spam/unknown
    - company_name: if business email
    - is_disposable: true/false
    - language_detected: ISO code
    - confidence_score: 0-100
    - spam_indicators: list of reasons if spam
    - enrichment: additional insights
    """
    
    try:
        if provider == "gemini" and ai_model:
            response = ai_model.generate_content(prompt)
            result_text = response.text
        elif provider == "claude" and ai_model:
            message = ai_model.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            result_text = message.content[0].text
        elif provider == "openai" and ai_model:
            response = ai_model.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            result_text = response.choices[0].message.content
        else:
            return {"category": "unknown", "error": "AI provider not available"}
        
        # Try to parse JSON
        json_match = re.search(r'\{.*\}', result_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            return {"category": "unknown", "enrichment": result_text}
    
    except Exception as e:
        console.print(f"[red]Error enriching {email}: {str(e)}[/red]")
        return {"category": "unknown", "error": str(e)}

def enrich_email(email: str) -> Dict:
    """Synchronous wrapper"""
    return asyncio.run(enrich_email_async(email))

# ML-based spam detection
def predict_email_quality_ml(email: str) -> float:
    """Predict email quality using ML"""
    if not ML_AVAILABLE:
        return 0.5
    
    try:
        model_path = "email_quality_model.pkl"
        if os.path.exists(model_path):
            model = joblib.load(model_path)
        else:
            # Create a simple model if none exists
            return predict_email_quality_heuristic(email)
        
        domain = email.split("@")[-1]
        features = np.array([[
            len(domain),
            len(email),
            sum(1 for c in email if c.isdigit()),
            1 if domain in ["gmail.com", "yahoo.com", "outlook.com"] else 0,
            sum(1 for c in email if c in "._-"),
            len(domain.split("."))
        ]])
        
        score = model.predict_proba(features)[0][1] if hasattr(model, "predict_proba") else model.predict(features)[0]
        return float(score)
    
    except Exception as e:
        console.print(f"[yellow]ML prediction failed: {e}, using heuristic[/yellow]")
        return predict_email_quality_heuristic(email)

def predict_email_quality_heuristic(email: str) -> float:
    """Heuristic-based quality prediction"""
    score = 0.5
    domain = email.split("@")[-1]
    
    # Positive indicators
    trusted_domains = ["gmail.com", "yahoo.com", "outlook.com", "icloud.com", "protonmail.com"]
    if domain in trusted_domains:
        score += 0.2
    
    # Negative indicators
    if len(domain) > 20:
        score -= 0.1
    
    if any(char.isdigit() for char in domain.split(".")[0]):
        score -= 0.1
    
    suspicious_patterns = ["temp", "fake", "spam", "test"]
    if any(pattern in domain.lower() for pattern in suspicious_patterns):
        score -= 0.3
    
    return max(0.0, min(1.0, score))

# Google Sheets sync
def sync_to_google_sheets(data: List[Dict]):
    """Sync data to Google Sheets"""
    if not GOOGLE_AVAILABLE or not config.GOOGLE_SHEET_ID:
        console.print("[yellow]Google Sheets not configured[/yellow]")
        return
    
    try:
        if not os.path.exists(config.GOOGLE_SHEETS_CREDENTIALS):
            console.print(f"[red]Credentials file not found: {config.GOOGLE_SHEETS_CREDENTIALS}[/red]")
            return
        
        creds = Credentials.from_service_account_file(config.GOOGLE_SHEETS_CREDENTIALS)
        service = build('sheets', 'v4', credentials=creds)
        
        values = [[
            item.get('email', ''),
            item.get('status', ''),
            item.get('category', ''),
            item.get('spam_score', 0),
            item.get('validity_score', 0),
            json.dumps(item.get('data', {}))
        ] for item in data]
        
        body = {'values': values}
        service.spreadsheets().values().append(
            spreadsheetId=config.GOOGLE_SHEET_ID,
            range="Sheet1!A:F",
            valueInputOption="RAW",
            body=body
        ).execute()
        
        console.print("[green]✅ Data synced to Google Sheets[/green]")
    
    except Exception as e:
        console.print(f"[red]Error syncing to Google Sheets: {e}[/red]")

# Slack notifications
def send_slack_notification(message: str, level: str = "info"):
    """Send notification to Slack"""
    if not config.SLACK_WEBHOOK_URL:
        return
    
    colors = {"info": "good", "warning": "warning", "error": "danger"}
    payload = {
        "text": message,
        "color": colors.get(level, "good")
    }
    
    try:
        requests.post(config.SLACK_WEBHOOK_URL, json=payload, timeout=5)
    except Exception as e:
        console.print(f"[yellow]Slack notification failed: {e}[/yellow]")

# Batch processing
async def process_batch_async(emails: List[str], batch_id: str = None) -> Dict:
    """Process emails in batch (async)"""
    if not batch_id:
        batch_id = hashlib.md5(str(datetime.now()).encode()).hexdigest()[:8]
    
    results = {
        "batch_id": batch_id,
        "total": len(emails),
        "valid": 0,
        "invalid": 0,
        "spam": 0,
        "processed": []
    }
    
    conn = init_database()
    cursor = conn.cursor()
    
    with Progress() as progress:
        task = progress.add_task(f"[cyan]Processing batch {batch_id}...", total=len(emails))
        
        for email in emails:
            is_valid, validation_msg = validate_email(email)
            
            if is_valid:
                results["valid"] += 1
                
                # Enrich with AI
                enriched = await enrich_email_async(email)
                
                # ML prediction
                validity_score = predict_email_quality_ml(email) if config.ENABLE_ML else predict_email_quality_heuristic(email)
                spam_score = enriched.get("spam_score", 0) / 100 if "spam_score" in enriched else 0
                
                if enriched.get("category") == "spam" or spam_score > 0.7:
                    results["spam"] += 1
                
                # Store in DB
                cursor.execute("""
                    INSERT OR REPLACE INTO email_list 
                    (email, category, enriched_info, spam_score, validity_score, 
                     is_disposable, language_detected, company_name, confidence_score, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    email,
                    enriched.get("category", "unknown"),
                    json.dumps(enriched),
                    spam_score,
                    validity_score,
                    1 if enriched.get("is_disposable") else 0,
                    enriched.get("language_detected", ""),
                    enriched.get("company_name", ""),
                    enriched.get("confidence_score", 0),
                    datetime.now()
                ))
                
                results["processed"].append({
                    "email": email,
                    "status": "valid",
                    "category": enriched.get("category"),
                    "spam_score": spam_score,
                    "validity_score": validity_score,
                    "data": enriched
                })
            else:
                results["invalid"] += 1
                results["processed"].append({
                    "email": email,
                    "status": "invalid",
                    "reason": validation_msg
                })
            
            progress.update(task, advance=1)
    
    # Log batch
    cursor.execute("""
        INSERT INTO processing_log 
        (batch_id, total_emails, valid_emails, invalid_emails, spam_emails)
        VALUES (?, ?, ?, ?, ?)
    """, (batch_id, results["total"], results["valid"], results["invalid"], results["spam"]))
    
    conn.commit()
    conn.close()
    
    return results

def process_csv(file_path: str):
    """Process CSV file"""
    if not os.path.exists(file_path):
        console.print(f"[red]File not found: {file_path}[/red]")
        return
    
    try:
        df = pd.read_csv(file_path)
        
        # Find email column
        email_col = None
        for col in df.columns:
            if "email" in col.lower():
                email_col = col
                break
        
        if not email_col:
            console.print("[red]No email column found in CSV[/red]")
            return
        
        emails = df[email_col].dropna().tolist()
        console.print(f"[cyan]Found {len(emails)} emails to process[/cyan]")
        
        # Process in batches
        batch_id = hashlib.md5(str(datetime.now()).encode()).hexdigest()[:8]
        results = asyncio.run(process_batch_async(emails, batch_id))
        
        # Sync to Google Sheets
        if GOOGLE_AVAILABLE:
            sync_to_google_sheets(results["processed"])
        
        # Auto-export to Power BI format
        if Confirm.ask("Export to Power BI format?", default=True):
            df_results = pd.DataFrame(results["processed"])
            df_results.to_csv("powerbi_export.csv", index=False)
            console.print("[green]✅ Power BI export created: powerbi_export.csv[/green]")
        
        # Send notification
        send_slack_notification(
            f"✅ Email processing complete!\n"
            f"Batch: {batch_id}\n"
            f"Total: {results['total']}\n"
            f"Valid: {results['valid']}\n"
            f"Invalid: {results['invalid']}\n"
            f"Spam: {results['spam']}"
        )
        
        # Show summary
        table = Table(title="Processing Summary")
        table.add_column("Metric", style="cyan")
        table.add_column("Count", style="magenta")
        table.add_row("Total", str(results["total"]))
        table.add_row("Valid", str(results["valid"]))
        table.add_row("Invalid", str(results["invalid"]))
        table.add_row("Spam", str(results["spam"]))
        console.print(table)
        
        console.print("[bold green]✅ Processing complete![/bold green]")
    
    except Exception as e:
        console.print(f"[red]Error processing CSV: {e}[/red]")

# Reports
def generate_report():
    """Generate comprehensive report"""
    conn = init_database()
    cursor = conn.cursor()
    
    # Category summary
    cursor.execute("SELECT category, COUNT(*) FROM email_list GROUP BY category")
    rows = cursor.fetchall()
    
    table = Table(title="Email Category Summary")
    table.add_column("Category", style="cyan")
    table.add_column("Count", style="magenta")
    table.add_column("Percentage", style="green")
    
    total = sum(row[1] for row in rows)
    for row in rows:
        pct = (row[1] / total * 100) if total > 0 else 0
        table.add_row(row[0] or "unknown", str(row[1]), f"{pct:.1f}%")
    
    console.print(table)
    
    # Spam statistics
    cursor.execute("SELECT AVG(spam_score), COUNT(*) FROM email_list WHERE spam_score > 0.7")
    spam_avg, spam_count = cursor.fetchone()
    
    if spam_avg:
        console.print(f"\n[red]High-risk spam emails: {spam_count} (avg score: {spam_avg:.2f})[/red]")
    
    # Recent processing
    cursor.execute("""
        SELECT batch_id, total_emails, valid_emails, spam_emails, processed_at
        FROM processing_log
        ORDER BY processed_at DESC
        LIMIT 5
    """)
    
    recent = cursor.fetchall()
    if recent:
        table2 = Table(title="Recent Processing Batches")
        table2.add_column("Batch ID", style="cyan")
        table2.add_column("Total", style="magenta")
        table2.add_column("Valid", style="green")
        table2.add_column("Spam", style="red")
        table2.add_column("Processed At", style="yellow")
        
        for row in recent:
            table2.add_row(*[str(c) for c in row])
        
        console.print(table2)
    
    conn.close()

def predict_email_quality(email: str):
    """Predict email quality"""
    is_valid, msg = validate_email(email)
    
    if not is_valid:
        console.print(f"[red]Invalid email: {msg}[/red]")
        return
    
    # ML prediction
    validity_score = predict_email_quality_ml(email) if config.ENABLE_ML else predict_email_quality_heuristic(email)
    
    # AI enrichment
    enriched = enrich_email(email)
    spam_score = enriched.get("spam_score", 0) / 100 if "spam_score" in enriched else 0
    
    # Display results
    panel = Panel(
        f"[cyan]Email:[/cyan] {email}\n"
        f"[green]Validity Score:[/green] {validity_score*100:.2f}%\n"
        f"[yellow]Spam Score:[/yellow] {spam_score*100:.2f}%\n"
        f"[magenta]Category:[/magenta] {enriched.get('category', 'unknown')}\n"
        f"[blue]Company:[/blue] {enriched.get('company_name', 'N/A')}\n"
        f"[red]Disposable:[/red] {'Yes' if enriched.get('is_disposable') else 'No'}",
        title="Email Analysis",
        border_style="green"
    )
    console.print(panel)

# Main menu
def main_menu():
    """Enhanced main menu"""
    while True:
        console.print("\n[bold blue]Email Intelligence CLI V2[/bold blue]")
        console.print("[dim]Enhanced with multi-AI support, ML, and advanced features[/dim]\n")
        
        console.print("1. Process CSV file")
        console.print("2. Generate report")
        console.print("3. Predict email quality")
        console.print("4. View database stats")
        console.print("5. Export to CSV")
        console.print("6. Settings")
        console.print("7. Exit")
        
        choice = Prompt.ask("\n[cyan]Choose an option[/cyan]", default="7")
        
        if choice == "1":
            file_path = Prompt.ask("Enter CSV file path")
            process_csv(file_path)
        
        elif choice == "2":
            generate_report()
        
        elif choice == "3":
            email = Prompt.ask("Enter email to analyze")
            predict_email_quality(email)
        
        elif choice == "4":
            conn = init_database()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM email_list")
            total = cursor.fetchone()[0]
            console.print(f"[green]Total emails in database: {total}[/green]")
            conn.close()
        
        elif choice == "5":
            console.print("\n[cyan]Export Options:[/cyan]")
            console.print("1. Standard CSV export")
            console.print("2. Power BI export (optimized)")
            console.print("3. Custom export")
            
            export_choice = Prompt.ask("Choose export type", default="1")
            
            conn = init_database()
            
            if export_choice == "1":
                output_file = Prompt.ask("Enter output CSV path", default="exported_emails.csv")
                df = pd.read_sql_query("SELECT * FROM email_list", conn)
                df.to_csv(output_file, index=False)
                console.print(f"[green]Exported to {output_file}[/green]")
            
            elif export_choice == "2":
                # Power BI optimized export
                console.print("[cyan]Preparing Power BI export...[/cyan]")
                
                # Query with flattened JSON for Power BI
                query = """
                    SELECT 
                        id,
                        email,
                        category,
                        spam_score,
                        validity_score,
                        is_disposable,
                        language_detected,
                        company_name,
                        confidence_score,
                        processed_at,
                        updated_at,
                        json_extract(enriched_info, '$.enrichment') as enrichment,
                        json_extract(enriched_info, '$.spam_indicators') as spam_indicators
                    FROM email_list
                    ORDER BY processed_at DESC
                """
                
                df = pd.read_sql_query(query, conn)
                
                # Format for Power BI
                df['processed_at'] = pd.to_datetime(df['processed_at'])
                df['updated_at'] = pd.to_datetime(df['updated_at'])
                df['spam_score'] = df['spam_score'].fillna(0) * 100  # Convert to percentage
                df['validity_score'] = df['validity_score'].fillna(0) * 100
                df['confidence_score'] = df['confidence_score'].fillna(0)
                
                # Export to Power BI format
                output_file = "powerbi_export.csv"
                df.to_csv(output_file, index=False)
                
                console.print(f"[green]✅ Power BI export created: {output_file}[/green]")
                console.print(f"[dim]Rows exported: {len(df)}[/dim]")
                
                # Show summary
                table = Table(title="Power BI Export Summary")
                table.add_column("Metric", style="cyan")
                table.add_column("Value", style="magenta")
                table.add_row("Total Rows", str(len(df)))
                table.add_row("Categories", str(df['category'].nunique()))
                table.add_row("Avg Spam Score", f"{df['spam_score'].mean():.2f}%")
                table.add_row("Avg Validity", f"{df['validity_score'].mean():.2f}%")
                console.print(table)
            
            elif export_choice == "3":
                output_file = Prompt.ask("Enter output CSV path", default="custom_export.csv")
                columns = Prompt.ask("Enter columns (comma-separated)", default="email,category,spam_score,validity_score")
                col_list = [c.strip() for c in columns.split(",")]
                
                query = f"SELECT {', '.join(col_list)} FROM email_list"
                df = pd.read_sql_query(query, conn)
                df.to_csv(output_file, index=False)
                console.print(f"[green]Exported to {output_file}[/green]")
            
            conn.close()
        
        elif choice == "6":
            console.print(f"\n[cyan]Current Settings:[/cyan]")
            console.print(f"AI Provider: {config.AI_PROVIDER}")
            console.print(f"Database: {config.DB_PATH}")
            console.print(f"Batch Size: {config.BATCH_SIZE}")
            console.print(f"ML Enabled: {config.ENABLE_ML}")
        
        elif choice == "7":
            console.print("[bold red]Exiting...[/bold red]")
            break
        
        else:
            console.print("[red]Invalid choice[/red]")

if __name__ == "__main__":
    # Initialize database
    init_database()
    
    # Check AI availability
    if not ai_model:
        console.print("[yellow]⚠️  No AI provider configured. Set API keys in environment variables.[/yellow]")
        console.print("[dim]GEMINI_API_KEY, ANTHROPIC_API_KEY, or OPENAI_API_KEY[/dim]\n")
    
    main_menu()

