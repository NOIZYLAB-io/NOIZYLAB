"""NoizyEconomy - Automated Billing & Receipts"""
import uuid
from datetime import datetime

INVOICE_DB = {}
PAYMENT_DB = {}

def generate_invoice(client_id, items, tax_rate=0.13):
    """Generate an invoice for a client"""
    invoice_id = f"INV-{uuid.uuid4().hex[:8].upper()}"
    
    subtotal = sum(item.get("amount", 0) for item in items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    invoice = {
        "id": invoice_id,
        "client_id": client_id,
        "items": items,
        "subtotal": round(subtotal, 2),
        "tax": round(tax, 2),
        "tax_rate": tax_rate,
        "total": round(total, 2),
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "due_date": None,
        "paid_at": None,
    }
    INVOICE_DB[invoice_id] = invoice
    return invoice

def send_receipt(invoice_id, payment_method="stripe"):
    """Send receipt after payment"""
    if invoice_id not in INVOICE_DB:
        return None
    
    invoice = INVOICE_DB[invoice_id]
    receipt = {
        "invoice_id": invoice_id,
        "client_id": invoice["client_id"],
        "amount_paid": invoice["total"],
        "payment_method": payment_method,
        "paid_at": datetime.now().isoformat(),
        "receipt_number": f"RCP-{uuid.uuid4().hex[:8].upper()}",
    }
    
    INVOICE_DB[invoice_id]["status"] = "paid"
    INVOICE_DB[invoice_id]["paid_at"] = receipt["paid_at"]
    PAYMENT_DB[receipt["receipt_number"]] = receipt
    
    return receipt

def get_outstanding():
    """Get all outstanding invoices"""
    return [i for i in INVOICE_DB.values() if i["status"] == "pending"]

def get_invoice(invoice_id):
    """Get invoice by ID"""
    return INVOICE_DB.get(invoice_id)

def get_client_invoices(client_id):
    """Get all invoices for a client"""
    return [i for i in INVOICE_DB.values() if i["client_id"] == client_id]

def calculate_revenue(period_days=30):
    """Calculate revenue for a period"""
    from datetime import timedelta
    cutoff = datetime.now() - timedelta(days=period_days)
    total = 0
    for inv in INVOICE_DB.values():
        if inv["status"] == "paid" and inv["paid_at"]:
            paid_date = datetime.fromisoformat(inv["paid_at"])
            if paid_date > cutoff:
                total += inv["total"]
    return round(total, 2)

