"""FrontDesk: Branding & Tone"""
TONE = {"style": "friendly_professional", "name": "Noizy", "company": "NoizyLab"}

RESPONSES = {
    "greeting": "Hi! I'm {name} from {company}. How can I help you today?",
    "booking_confirm": "Great! I've got you booked. You'll receive a confirmation shortly.",
    "thanks": "Thank you for choosing {company}! We're here whenever you need us.",
    "goodbye": "Thanks for calling {company}! Have a great day!",
    "hold": "One moment please, I'm checking that for you.",
    "apologize": "I'm sorry to hear you're having trouble. Let me help you sort this out.",
}

def get_response(response_type, custom_vars=None):
    template = RESPONSES.get(response_type, RESPONSES["greeting"])
    vars = {**TONE, **(custom_vars or {})}
    for key, val in vars.items(): template = template.replace(f"{{{key}}}", str(val))
    return template

def set_tone(style=None, name=None, company=None):
    if style: TONE["style"] = style
    if name: TONE["name"] = name
    if company: TONE["company"] = company
    return TONE

def get_tone():
    return TONE

