import os, smtplib, ssl
from email.message import EmailMessage
from pathlib import Path

LICENSE_DIR = Path("licenses")

def send_license(recipient, plan="pro"):
    """Email a license token as attachment to the client."""
    sender = os.getenv("ADMIN_EMAIL", "rsp@noizy.ai")
    smtp_server = os.getenv("SMTP_SERVER", "smtp.secureserver.net")
    smtp_port = int(os.getenv("SMTP_PORT", "465"))
    smtp_user = os.getenv("SMTP_USER", sender)
    smtp_pass = os.getenv("SMTP_PASS", "")
    use_tls = os.getenv("SMTP_USE_TLS", "1") == "1"

    jwt_path = LICENSE_DIR / f"{recipient}.jwt"
    if not jwt_path.exists():
        raise FileNotFoundError(f"License file not found: {jwt_path}")

    msg = EmailMessage()
    msg["Subject"] = f"🚀 Noizy.ai License Activation — {plan.upper()}"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(
        f"""
Hello {recipient},

Welcome to Noizy.ai Mission Control! 🎯

Your {plan.upper()} license is ready and activated.

🔧 INSTALLATION STEPS:
1. Place the attached license.jwt file in your Mission Control directory
2. Restart Noizy.ai Mission Control
3. You now have access to all {96 if plan == 'pro' else 6} agents!

📊 Your Dashboard: {os.getenv('HOSTING_URL', 'https://noizy.ai')}/dashboard
🎸 Rock Mode Portal: {os.getenv('PORTAL_URL', 'https://portal.noizy.ai')}

🆘 NEED HELP?
- Email: {os.getenv('SUPPORT_EMAIL', 'rsp@noizy.ai')}
- Docs: https://docs.noizy.ai
- Discord: https://discord.gg/noizy-ai

Rock on with your new AI mission control center!

— The Noizy.ai Team
"""
    )

    # Attach license file
    msg.add_attachment(jwt_path.read_bytes(),
                       maintype="application",
                       subtype="jwt",
                       filename="license.jwt")

    # Send email
    context = ssl.create_default_context()
    
    if use_tls and smtp_port == 465:
        # Use SMTP_SSL for port 465
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
            server.send_message(msg)
    else:
        # Use SMTP with STARTTLS for other ports
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            if use_tls:
                server.starttls(context=context)
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
            server.send_message(msg)
    
    print(f"📨 License email sent to {recipient}")

def send_welcome_email(recipient, plan="pro"):
    """Send a welcome email without license attachment."""
    sender = os.getenv("ADMIN_EMAIL", "rsp@noizy.ai")
    smtp_server = os.getenv("SMTP_SERVER", "smtp.secureserver.net")
    smtp_port = int(os.getenv("SMTP_PORT", "465"))
    smtp_user = os.getenv("SMTP_USER", sender)
    smtp_pass = os.getenv("SMTP_PASS", "")
    use_tls = os.getenv("SMTP_USE_TLS", "1") == "1"

    msg = EmailMessage()
    msg["Subject"] = f"🎉 Welcome to Noizy.ai {plan.upper()}!"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(
        f"""
Welcome to the Noizy.ai family! 🧠

Your {plan.upper()} subscription is now active. Your license will be delivered shortly.

What you get with {plan.upper()}:
{'✅ 96 autonomous agents' if plan == 'pro' else '✅ 6 starter agents'}
✅ Multi-provider AI (OpenAI, Claude, GitHub Copilot)
✅ VS Code integration
{'✅ HTTPS deployment support' if plan == 'pro' else ''}
{'✅ Priority support' if plan == 'pro' else '✅ Community support'}

Next steps:
1. Download the installer from https://noizy.ai/download
2. Watch for your license email (arriving soon!)
3. Join our Discord community for tips and support

Ready to revolutionize your workflow? Let's go! 🚀

— The Noizy.ai Team
"""
    )

    # Send email (same logic as send_license)
    context = ssl.create_default_context()
    
    if use_tls and smtp_port == 465:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
            server.send_message(msg)
    else:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            if use_tls:
                server.starttls(context=context)
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
            server.send_message(msg)
    
    print(f"📧 Welcome email sent to {recipient}")