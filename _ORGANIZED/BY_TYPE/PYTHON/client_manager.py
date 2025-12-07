#!/usr/bin/env python3
"""
FISH MUSIC INC - CLIENT MANAGEMENT SYSTEM
Manage clients, projects, invoices, and payments
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class ClientManager:
    """Complete client and project management"""

    def __init__(self):
        self.base_path = Path('/Users/m2ultra/CB-01-FISHMUSICINC')
        self.clients_path = self.base_path / 'clients'
        self.invoices_path = self.base_path / 'docs' / 'invoices'
        self.contracts_path = self.base_path / 'docs' / 'contracts'

        # Major client database
        self.major_clients = {
            'FUEL': {
                'name': 'FUEL Agency',
                'type': 'Agency',
                'status': 'past',
                'projects': [],
                'total_value': 0,
                'contact_email': ''
            },
            'McDonalds': {
                'name': "McDonald's",
                'type': 'Major Brand',
                'status': 'past',
                'projects': [],
                'total_value': 0,
                'contact_email': ''
            },
            'Microsoft': {
                'name': 'Microsoft',
                'type': 'Technology',
                'status': 'past',
                'projects': [{'name': 'Tinker Project', 'year': None}],
                'total_value': 0,
                'contact_email': ''
            },
            'Deadwood': {
                'name': 'Deadwood',
                'type': 'Entertainment',
                'status': 'past',
                'projects': [],
                'total_value': 0,
                'contact_email': ''
            },
            'Design_Reunion': {
                'name': 'Design Reunion Show',
                'type': 'Special Project',
                'status': 'in_progress',
                'projects': [{'name': 'Live Show Recording & Mix', 'year': 2025}],
                'notes': 'Filmed by Gavin Lumsden (Rogers). CRITICAL to complete!',
                'contact_email': 'gavin@rogers.com',
                'priority': 'HIGHEST'
            }
        }

    def create_invoice_template(self, client_name: str, project_name: str, amount: float) -> Dict:
        """Create professional invoice"""
        invoice_number = f"FM-{datetime.now().strftime('%Y%m%d')}-{len(os.listdir(self.invoices_path)) + 1 if self.invoices_path.exists() else 1:03d}"

        invoice = {
            'invoice_number': invoice_number,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'due_date': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
            'from': {
                'name': 'Fish Music Inc',
                'email': 'rp@fishmusicinc.com',
                'website': 'fishmusicinc.com'
            },
            'to': {
                'name': client_name,
                'project': project_name
            },
            'line_items': [
                {
                    'description': project_name,
                    'quantity': 1,
                    'rate': amount,
                    'amount': amount
                }
            ],
            'subtotal': amount,
            'tax': 0,
            'total': amount,
            'payment_terms': 'Net 30',
            'payment_methods': {
                'stripe': 'https://buy.stripe.com/fishmusicinc (setup at business/stripe/STRIPE_SETUP.md)',
                'paypal': 'rsp@noizyfish.com OR paypal.me/fishmusicinc',
                'kofi': 'ko-fi.com/noizyfish',
                'wire': 'Available upon request (for amounts > $5,000)'
            },
            'notes': 'Thank you for your business! GORUNFREE! 🎸🔥'
        }

        return invoice

    def generate_invoice_html(self, invoice: Dict) -> str:
        """Generate HTML invoice"""
        html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Invoice {invoice['invoice_number']} - Fish Music Inc</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; }}
        .header {{ text-align: center; border-bottom: 3px solid #667eea; padding-bottom: 20px; margin-bottom: 30px; }}
        .header h1 {{ color: #667eea; font-size: 2.5em; margin: 0; }}
        .info {{ display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-bottom: 40px; }}
        .invoice-details {{ background: #f8f9fa; padding: 20px; border-radius: 5px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 30px 0; }}
        th {{ background: #667eea; color: white; padding: 15px; text-align: left; }}
        td {{ padding: 15px; border-bottom: 1px solid #e2e8f0; }}
        .total {{ background: #f8f9fa; font-weight: bold; font-size: 1.2em; }}
        .footer {{ margin-top: 40px; padding-top: 20px; border-top: 2px solid #e2e8f0; text-align: center; color: #718096; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🎸 Fish Music Inc</h1>
        <p style="font-size: 1.2em; color: #4a5568;">Professional Music Production & Sound Design</p>
    </div>

    <div class="info">
        <div>
            <h3>FROM:</h3>
            <p><strong>{invoice['from']['name']}</strong><br>
            Email: {invoice['from']['email']}<br>
            Web: {invoice['from']['website']}</p>
        </div>
        <div class="invoice-details">
            <p><strong>Invoice #:</strong> {invoice['invoice_number']}</p>
            <p><strong>Date:</strong> {invoice['date']}</p>
            <p><strong>Due Date:</strong> {invoice['due_date']}</p>
            <p><strong>Terms:</strong> {invoice['payment_terms']}</p>
        </div>
    </div>

    <div>
        <h3>TO:</h3>
        <p><strong>{invoice['to']['name']}</strong><br>
        Project: {invoice['to']['project']}</p>
    </div>

    <table>
        <thead>
            <tr>
                <th>Description</th>
                <th>Qty</th>
                <th>Rate</th>
                <th>Amount</th>
            </tr>
        </thead>
        <tbody>
'''

        for item in invoice['line_items']:
            html += f'''            <tr>
                <td>{item['description']}</td>
                <td>{item['quantity']}</td>
                <td>${item['rate']:,.2f}</td>
                <td>${item['amount']:,.2f}</td>
            </tr>
'''

        html += f'''        </tbody>
        <tfoot>
            <tr class="total">
                <td colspan="3" style="text-align: right;">TOTAL:</td>
                <td>${invoice['total']:,.2f} CAD</td>
            </tr>
        </tfoot>
    </table>

    <div>
        <h3>Payment Methods:</h3>
        <ul>
            <li><strong>PayPal:</strong> {invoice['payment_methods']['paypal']}</li>
            <li><strong>Stripe:</strong> {invoice['payment_methods']['stripe']}</li>
            <li><strong>Ko-fi:</strong> {invoice['payment_methods']['kofi']}</li>
            <li><strong>Wire Transfer:</strong> {invoice['payment_methods']['wire']}</li>
        </ul>
    </div>

    <div class="footer">
        <p>{invoice['notes']}</p>
        <p style="margin-top: 10px;">© {datetime.now().year} Fish Music Inc. All Rights Reserved.</p>
    </div>
</body>
</html>
'''
        return html

    def print_client_portfolio(self):
        """Display client portfolio"""
        print("\n" + "═" * 70)
        print("🏢 FISH MUSIC INC - CLIENT PORTFOLIO")
        print("═" * 70)
        print("\n40 YEARS OF PROFESSIONAL EXCELLENCE\n")

        print("🔥 MAJOR CLIENTS:\n")
        for client_id, client in self.major_clients.items():
            status_icon = "✅" if client['status'] == 'active' else "📋" if client['status'] == 'in_progress' else "⭐"
            priority = f" [{client.get('priority', 'Normal')}]" if 'priority' in client else ""

            print(f"   {status_icon} {client['name']}{priority}")
            print(f"      Type: {client['type']}")
            if client['projects']:
                print(f"      Projects: {len(client['projects'])}")
                for proj in client['projects']:
                    print(f"         • {proj['name']}")
            if client.get('notes'):
                print(f"      Notes: {client['notes']}")
            print()

        print("=" * 70)
        print("GORUNFREE! 🎸🔥")
        print("=" * 70)

def main():
    """Main execution"""
    manager = ClientManager()
    manager.print_client_portfolio()

if __name__ == '__main__':
    main()

