# backend_ultra/business/client_experience.py
# NOIZYLAB CLIENT EXPERIENCE SYSTEM
# The "people actually book you, pay you, love you, and come back" layer
# ═══════════════════════════════════════════════════════════════════════════════

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json

# ═══════════════════════════════════════════════════════════════════════════════
# BRAND PILLARS (NORTH STAR - LOCK THESE IN)
# ═══════════════════════════════════════════════════════════════════════════════

BRAND_PILLARS = {
    "truth_over_appearance": {
        "statement": "Truth over appearance.",
        "meaning": "We never fake certainty, never bluff, never hide the downside."
    },
    "people_over_machines": {
        "statement": "People over machines.",
        "meaning": "Your stress, time, and memories come first; the hardware is second."
    },
    "calm_over_drama": {
        "statement": "Calm over drama.",
        "meaning": "No scare tactics, no panic prompts, no 'uh-oh!!!' nonsense."
    },
    "clarity_over_cleverness": {
        "statement": "Clarity over cleverness.",
        "meaning": "If a non-tech, tired human can't understand it, it's not good enough."
    }
}

def get_brand_pillars_text() -> str:
    """Get the brand pillars as formatted text."""
    lines = ["NOIZYLAB BRAND PILLARS", "=" * 40, ""]
    for key, pillar in BRAND_PILLARS.items():
        lines.append(f"• {pillar['statement']}")
        lines.append(f"  {pillar['meaning']}")
        lines.append("")
    lines.append("If anything in the business fights these → that thing is wrong, not the pillars.")
    return "\n".join(lines)

# ═══════════════════════════════════════════════════════════════════════════════
# SERVICE MENU V2 (CLEAN, NAMED, READY TO SHOW)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ServiceV2:
    """A service in the V2 menu."""
    id: str
    name: str
    tagline: str
    best_for: List[str]
    you_get: List[str]
    does_not_include: List[str]
    emoji: str = "🔧"

SERVICE_MENU_V2 = {
    "espresso": ServiceV2(
        id="espresso",
        name="ESPRESSO TUNE-UP",
        tagline="Make it stop sucking, fast.",
        emoji="☕",
        best_for=[
            "Slow, laggy, hot, but not dying"
        ],
        you_get=[
            "Safe system health check (drive, temps, OS basics)",
            "Startup stripped down to what actually needs to launch",
            "Junk + temp clutter cleaned (no real files touched)",
            "Short report: 'What we fixed' + 'What I'd watch next'"
        ],
        does_not_include=[
            "Deep hardware testing",
            "Data rescue",
            "OS reinstall"
        ]
    ),
    
    "deep_dive": ServiceV2(
        id="deep_dive",
        name="DEEP DIVE REPAIR",
        tagline="Let's actually figure out what's going on.",
        emoji="🛠",
        best_for=[
            "Crashes, weird behaviour, random restarts, 'something's not right'"
        ],
        you_get=[
            "Detailed diagnostics (logs, SMART, temps, CPU/RAM behaviour)",
            "Hunt for software/driver conflicts",
            "Stability-first adjustments (not risky tweaking)",
            "Clear verdict: Likely cause, How serious, How confident, What I'd do"
        ],
        does_not_include=[
            "Board-level physical repair",
            "Guaranteed 100% resolution in one hit"
        ]
    ),
    
    "data_rescue": ServiceV2(
        id="data_rescue",
        name="DATA RESCUE GAMEPLAN",
        tagline="My life is on this machine. Help.",
        emoji="🧯",
        best_for=[
            "Won't boot, clicking drive, scary errors, black screens"
        ],
        you_get=[
            "Honest risk assessment (no sugar-coating, no doom theatrics)",
            "A clear choice: Pro recovery lab / Careful DIY / Fresh rebuild",
            "A 'Rescue Brief' you can hand any tech/lab: Symptoms, What's been tried, Do's & don'ts"
        ],
        does_not_include=[
            "Guarantees of recovery",
            "Pretending software can fix physically-dead drives"
        ]
    ),
    
    "migration": ServiceV2(
        id="migration",
        name="CLEAN SLATE MIGRATION",
        tagline="Move my life to a better machine, without dragging the mess.",
        emoji="🧭",
        best_for=[
            "New machine, old machine limping, or 'I want a fresh start that stays clean'"
        ],
        you_get=[
            "Plan: what moves, what archives, what dies",
            "Guided migration of files, apps, settings (sanity > chaos)",
            "Backup + basic security set up properly on new machine",
            "A simple 'Tech Passport': What we set up, Where important stuff lives, How it's protected"
        ],
        does_not_include=[
            "'Clone all the junk exactly as-is'",
            "Infinite tweaking"
        ]
    ),
    
    "guardian": ServiceV2(
        id="guardian",
        name="GUARDIAN LOOP",
        tagline="Never face a tech crisis alone again.",
        emoji="🛡",
        best_for=[
            "People / families / small studios whose lives depend on their gear"
        ],
        you_get=[
            "Regular health checks",
            "Backup + drive monitoring",
            "Priority response when things break",
            "A couple of Espresso Tune-Ups baked in",
            "Lower pricing on Deep Dive / Migration work"
        ],
        does_not_include=[
            "Fear-mongering",
            "'Subscribe or else' nonsense",
            "One-off sessions remain fully supported"
        ]
    )
}

def get_service_menu_text() -> str:
    """Get the service menu as formatted text."""
    lines = ["NOIZYLAB SERVICE MENU V2", "=" * 40, ""]
    
    for service in SERVICE_MENU_V2.values():
        lines.append(f"{service.emoji} {service.name}")
        lines.append(f'"{service.tagline}"')
        lines.append("")
        lines.append("Best for:")
        for item in service.best_for:
            lines.append(f"  • {item}")
        lines.append("")
        lines.append("You get:")
        for item in service.you_get:
            lines.append(f"  ✓ {item}")
        lines.append("")
        lines.append("Does NOT include:")
        for item in service.does_not_include:
            lines.append(f"  ✗ {item}")
        lines.append("")
        lines.append("-" * 40)
        lines.append("")
    
    return "\n".join(lines)

# ═══════════════════════════════════════════════════════════════════════════════
# CLIENT WELCOME ONE-PAGER V2
# ═══════════════════════════════════════════════════════════════════════════════

CLIENT_WELCOME_ONEPAGER = """
WELCOME TO NOIZYLAB
MC96 Mission Control for your tech life.

Hi, I'm Rob.
NOIZYLAB is how I turn "my computer is killing me" into "okay, I know what's going on and what happens next."

═══════════════════════════════════════════════════════════════════════════════
1. WHAT NOIZYLAB IS
═══════════════════════════════════════════════════════════════════════════════

• A calm control center that watches over your machines.
• A mix of my repair experience + a stack of smart AIs.
• A place where we care more about you and your data than we do about the hardware.

What it is NOT:
• A faceless ticket system.
• A "wipe it and call it fixed" shop.
• A guilt machine for not backing up.

═══════════════════════════════════════════════════════════════════════════════
2. HOW I TREAT YOU
═══════════════════════════════════════════════════════════════════════════════

You can expect:

STRAIGHT TALK.
I'll tell you what I know, what I don't know yet, and what I think, clearly labelled.

KIND DELIVERY.
No shaming, no "you should've known better," no ego games.

PLAIN LANGUAGE.
You get the human version first. Nerd details only if you want them.

SAFETY-FIRST DECISIONS.
I don't format, wipe, or do risky changes without explaining what it means and getting your clear "yes."

═══════════════════════════════════════════════════════════════════════════════
3. WHAT I NEED FROM YOU
═══════════════════════════════════════════════════════════════════════════════

Tell the story in your own words.
"It feels cursed" is valid input.

Tell me what's sacred.
Photos? Work? One specific project? That shapes everything.

Don't nuke first, ask later.
Please don't:
• Reinstall
• Format
• Repeatedly force a failing machine on and off
...before we talk.

Be honest about your energy.
If you're fried, just say "I'm overwhelmed" and I'll keep it ultra simple and slow.

═══════════════════════════════════════════════════════════════════════════════
4. WHAT A SESSION FEELS LIKE
═══════════════════════════════════════════════════════════════════════════════

We set the emotional level.
You: "I'm fine / I'm stressed / I'm freaking out."
I match that and keep you out of overload.

We get the facts.
I use tools + experience + NOIZYLAB's brain to figure out:
• What's happening
• How risky it is
• How urgent it is

I give you options.
Usually:
• Quick relief
• Deeper fix
• Bigger-picture move (upgrade / migrate / retire)

You decide.
No pressure, no tricks. I'll tell you what I'd do if it were my own machine.

You get a summary.
In plain English:
• What was wrong
• What we did
• What I recommend next

═══════════════════════════════════════════════════════════════════════════════
5. WHEN TO REACH OUT IMMEDIATELY
═══════════════════════════════════════════════════════════════════════════════

Message me ASAP if:

• Your machine suddenly won't boot
• You hear clicking/grinding from a drive
• You see "no boot device" / "disk error" / similar scary messages
• You're about to hand it to a shop and your gut says "I don't fully trust this"

Even a short message like:

"Old laptop, clicking, won't boot, family photos on it."

...is enough for me to start steering you safely.

═══════════════════════════════════════════════════════════════════════════════
6. MY PROMISE
═══════════════════════════════════════════════════════════════════════════════

I can't promise nothing will ever break.

I can promise:

• You won't have to face it alone.
• I'll always be honest, even when the news is hard.
• I'll always be kind, especially when you're stressed.
• I will give you the exact advice I'd give someone I love,
  not what's easiest or most profitable.

That's NOIZYLAB.

— Rob
"""

# ═══════════════════════════════════════════════════════════════════════════════
# CALL/ZOOM SCRIPT
# ═══════════════════════════════════════════════════════════════════════════════

CALL_SCRIPT = """
"Alright, here's how I work so there are no surprises.

First, I care more about you and your files than about the machine. We're on the same side, and I'm not here to judge anything you did or didn't do with it.

Second, I'm going to tell you what I actually know, what I'm guessing, and how sure I am. If I don't know yet, I'll say that and explain how we'll find out.

Third, I'm going to give you a small number of options, not twenty. I'll tell you what I'd do if this were my own machine, and you can agree, disagree, or ask for something lighter.

Last, I don't do surprise wipes or risky stuff without your clear yes. If something could cost you files or money, I'll say it out loud first.

Does that all sound good before we poke at anything?"
"""

# ═══════════════════════════════════════════════════════════════════════════════
# EMAIL TEMPLATES
# ═══════════════════════════════════════════════════════════════════════════════

EMAIL_TEMPLATES = {
    "inquiry_acknowledgement": {
        "subject": "Got your message – NOIZYLAB's on it",
        "body": """Hi {name},

Thanks for reaching out – I know dealing with a misbehaving computer is never fun.

I've received your message about:
{issue_summary}

Here's what happens next:

• I'll review what you sent and put together a simple plan.
• We'll decide together whether you need an Espresso Tune-Up, Deep Dive, or Data Rescue.
• You'll always know the risks, options, and costs before we do anything.

If your situation feels urgent (e.g., clicking drive, won't boot, "my whole life is on there"), please reply with:
"CRITICAL" and a one-line description, and I'll treat it as a priority data issue.

Talk soon,
Rob
NOIZYLAB – MC96 Mission Control"""
    },
    
    "booking_confirmation": {
        "subject": "Your NOIZYLAB session is booked – here's what to expect",
        "body": """Hi {name},

Your NOIZYLAB session is confirmed:

• Type: {session_type}
• Date & Time: {datetime}
• Device: {device_description}

What I'll do:
• Meet you online and walk through what's going on in simple language
• Run safe diagnostics first – nothing destructive, no surprise wipes
• Give you clear options with pros/cons, not geek-speak

What would help on your side:
• Have the device plugged in (and charger ready)
• Make sure you can stay connected to the internet during the session
• If there are files you absolutely can't lose, make a quick list so we can prioritize them

One important thing:
Please don't reinstall, format, or keep power-cycling a failing machine before our session.
Those steps can make data recovery harder.

If anything changes before we meet (new noises, new errors), hit reply and tell me – even a quick photo of the screen helps.

Looking forward to helping you get your sanity back,
Rob
NOIZYLAB"""
    },
    
    "post_session_summary": {
        "subject": "NOIZYLAB summary – what we did for {device_name}",
        "body": """Hi {name},

Thanks again for working with me today on {device_name}.
Here's a clear record of what we found and what we did.

═══════════════════════════════════════════════════════════════════════════════
1. WHAT WAS HAPPENING (in plain language)
═══════════════════════════════════════════════════════════════════════════════
{original_problem}

═══════════════════════════════════════════════════════════════════════════════
2. WHAT WE FOUND
═══════════════════════════════════════════════════════════════════════════════
{findings}

═══════════════════════════════════════════════════════════════════════════════
3. WHAT WE DID IN THIS SESSION
═══════════════════════════════════════════════════════════════════════════════
{actions_taken}

═══════════════════════════════════════════════════════════════════════════════
4. WHAT SHOULD FEEL DIFFERENT NOW
═══════════════════════════════════════════════════════════════════════════════
{improvements}

═══════════════════════════════════════════════════════════════════════════════
5. MY HONEST RECOMMENDATION (if this were my machine)
═══════════════════════════════════════════════════════════════════════════════
{recommendation}

═══════════════════════════════════════════════════════════════════════════════
6. OPTIONAL NEXT STEPS
═══════════════════════════════════════════════════════════════════════════════
{next_steps}

If anything feels off, or if the same issue starts creeping back sooner than expected, just reply and tell me. I'd rather catch things early than have you go through another tech nightmare.

You're not alone with this stuff anymore.

Rob
NOIZYLAB"""
    },
    
    "data_rescue_followup": {
        "subject": "Next steps for your data on {device_name}",
        "body": """Hi {name},

This is a quick follow-up on your data-first rescue situation with {device_name}.

Here's where we landed today:

• Likely issue: {likely_issue}
• Risk level: {risk_level}

Based on what you told me about your files ({critical_data}), my honest recommendation was:
{recommendation}

If you go the lab route, you can literally say:

"My drive is {symptoms}. It has irreplaceable {data_type}.
I have not formatted or reinstalled anything. I've stopped powering it on.
I need an evaluation and a quote for recovery."

If lab pricing ends up being out of reach, reply and we can talk about the safest possible Plan B (careful DIY or local shop), with eyes wide open about the risks.

I know this is one of the worst tech feelings there is.
If nothing else, you made one extremely smart move: you stopped and asked for help before pushing the drive further. That matters.

Whatever path you choose, I've got your back if you need translation, advice, or sanity checks.

Rob
NOIZYLAB"""
    },
    
    "one_week_checkin": {
        "subject": "Quick check-in – how's {device_name} treating you?",
        "body": """Hi {name},

Just a quick check-in from NOIZYLAB: how has {device_name} been treating you since our session?

If you have 10 seconds, hit reply and pick one:

• "All good, feels better"
• "Better, but still a bit off"
• "No change / got worse"

If anything feels weird, I'd rather hear about it while it's still small than when it becomes a full-blown crisis.

And if it's been solid, we can also start thinking about the next smartest move (backups, upgrades, or just leaving it alone).

Either way, you're not bothering me – this is literally what NOIZYLAB is here for.

Rob
NOIZYLAB"""
    }
}

def generate_email(template_id: str, **kwargs) -> Dict[str, str]:
    """Generate an email from a template with filled-in values."""
    template = EMAIL_TEMPLATES.get(template_id)
    if not template:
        return {"error": f"Template '{template_id}' not found"}
    
    return {
        "subject": template["subject"].format(**kwargs),
        "body": template["body"].format(**kwargs)
    }

# ═══════════════════════════════════════════════════════════════════════════════
# BOOKING FLOW
# ═══════════════════════════════════════════════════════════════════════════════

class EmotionalLevel(Enum):
    OKAY = "okay"           # "I'm fine, just annoyed"
    STRESSED = "stressed"   # "I'm stressed, please be gentle"
    CRISIS = "crisis"       # "I'm freaking out"

@dataclass
class ClientIntake:
    """Client intake form data."""
    name: str
    email: str
    phone: Optional[str] = None
    
    # Device info
    device_type: str = "unknown"  # laptop, desktop, all-in-one, not sure
    os_type: str = "unknown"      # mac, windows, not sure
    device_age: str = "unknown"   # rough age
    
    # Problem description
    problem_feeling: str = ""     # How it feels: slow, won't boot, weird, cursed
    problem_details: str = ""     # Their own words
    
    # Critical data
    has_critical_data: bool = False
    critical_data_types: List[str] = field(default_factory=list)  # photos, work, school, etc.
    
    # Emotional state
    emotional_level: EmotionalLevel = EmotionalLevel.OKAY
    
    # Preferred session
    preferred_session_type: str = "not_sure"  # espresso, deep_dive, data_rescue, not_sure
    preferred_time_window: str = ""           # morning, afternoon, evening
    timezone: str = ""
    
    def to_noizycase_summary(self) -> str:
        """Generate a NOIZYCASE summary for Rob's dashboard."""
        return f"""
NOIZYCASE: {self.name}
═══════════════════════════════════════════════════════════════════════════════

DEVICE: {self.device_type} / {self.os_type} / ~{self.device_age} old
EMOTIONAL LEVEL: {self.emotional_level.value.upper()}
PRIORITY: {"HIGH - CRITICAL DATA AT RISK" if self.has_critical_data and self.emotional_level == EmotionalLevel.CRISIS else "NORMAL"}

SYMPTOMS (client phrasing):
"{self.problem_details}"

CRITICAL DATA:
{"YES - " + ", ".join(self.critical_data_types) if self.has_critical_data else "No critical data mentioned"}

RECOMMENDED APPROACH:
{self._get_recommended_approach()}

SUGGESTED SESSION TYPE: {self.preferred_session_type}
PREFERRED TIME: {self.preferred_time_window}
"""
    
    def _get_recommended_approach(self) -> str:
        """Get recommended approach based on intake."""
        if self.emotional_level == EmotionalLevel.CRISIS and self.has_critical_data:
            return "DATA-FIRST RESCUE - Treat as emergency. Protect files before anything else."
        elif "won't boot" in self.problem_details.lower() or "clicking" in self.problem_details.lower():
            return "DATA RESCUE GAMEPLAN - Assess drive health before any repair attempts."
        elif "slow" in self.problem_details.lower() or "laggy" in self.problem_details.lower():
            return "ESPRESSO TUNE-UP - Quick wins first, assess if deeper dive needed."
        elif "crash" in self.problem_details.lower() or "random" in self.problem_details.lower():
            return "DEEP DIVE REPAIR - Need to investigate root cause."
        else:
            return "Start with ESPRESSO TUNE-UP, escalate if needed."

# ═══════════════════════════════════════════════════════════════════════════════
# SMS/WHATSAPP BOOKING FLOW
# ═══════════════════════════════════════════════════════════════════════════════

SMS_BOOKING_FLOW = {
    "greeting": """Hey, it's NOIZYLAB. I've got you.
We'll go one step at a time and keep this as easy as possible.""",
    
    "q1_device": """1) Is it a laptop or desktop?
2) Mac, Windows, or not sure?
(just reply like: Laptop – Mac)""",
    
    "q2_symptoms": """Thanks. In your own words, what's it doing?
Examples: 'super slow', 'won't start', 'noisy', 'I think I got a virus'.""",
    
    "q3_critical_data": """Is there anything on it you absolutely can't lose?
(photos, work, school stuff, etc.)
Reply: Yes – [what] or No.""",
    
    "q4_emotional_level": """Last one: how are you doing with all this?

1 = I'm okay, just annoyed
2 = I'm stressed, please be gentle
3 = I'm freaking out""",
    
    "summary_template": """Got it.

Device: {device}
Symptoms: {symptoms}
Critical files: {critical_files}
Stress level: {stress_level}

Here's my honest read:

This sounds like: {suspected_cause}
The good news: {good_news}
The priority: {priority}

I recommend we do a {recommended_session}.

I have time:
• {slot_1}
• {slot_2}

Which works better?""",
    
    "booking_confirmed": """Perfect. You're booked.

Before our session:
• Please don't reinstall or format anything.
• Don't keep power-cycling if it's failing to boot.
• If anything changes (new noises, new error messages), send me a photo or screenshot.

We'll handle the rest together. You're not on your own with this anymore."""
}

def generate_sms_summary(
    device: str,
    symptoms: str,
    critical_files: str,
    stress_level: str,
    suspected_cause: str,
    good_news: str,
    priority: str,
    recommended_session: str,
    slot_1: str,
    slot_2: str
) -> str:
    """Generate the SMS summary message."""
    return SMS_BOOKING_FLOW["summary_template"].format(
        device=device,
        symptoms=symptoms,
        critical_files=critical_files,
        stress_level=stress_level,
        suspected_cause=suspected_cause,
        good_news=good_news,
        priority=priority,
        recommended_session=recommended_session,
        slot_1=slot_1,
        slot_2=slot_2
    )

# ═══════════════════════════════════════════════════════════════════════════════
# LANDING PAGE COPY
# ═══════════════════════════════════════════════════════════════════════════════

LANDING_PAGE_COPY = {
    "hero": {
        "headline": "The Calmest Place on Earth for Broken Computers",
        "subhead": "NOIZYLAB is your always-on repair brain: 25 specialist AIs + a human who actually cares, turning tech panic into clear, kind, ridiculously simple fixes.",
        "cta_primary": "Book a Repair Session",
        "cta_secondary": "See How NOIZYLAB Works",
        "reassurance": "No wipes. No blame. No BS. Just the truth, a plan, and your sanity back."
    },
    
    "what_is": {
        "title": "Not a Plugin. Not a 'Bot.' Your Tech Control Tower.",
        "copy": """Most repair tools treat you like a problem.
NOIZYLAB treats you like a person whose life runs on these machines.

Behind the scenes, 25 specialized "Genius" AIs:
• Watch your devices for trouble
• Help diagnose what's really wrong
• Protect your files first, not the hardware
• Explain everything in human language

On the surface, you just get:
• One calm dashboard
• One trusted guide
• One clear next step when things go sideways"""
    },
    
    "how_it_feels": {
        "title": "Like Coffee With a Brilliant Friend Who Fixes Computers",
        "bullets": [
            "Talks to you like a human, not a manual",
            "Knows when you're stressed and slows everything down",
            "Never fakes what it knows, never hides bad news",
            "Always offers 2–3 honest options, not 'just reinstall'"
        ],
        "pull_quote": "If this were my own machine, here's what I'd do…"
    },
    
    "what_we_do": {
        "title": "From 'Kind of Annoying' to 'Oh No, It Just Died'",
        "lanes": [
            {
                "name": "SLOW / WEIRD / LOUD",
                "symptoms": ["Boot takes forever", "Fans screaming", "Random freezes & lag"],
                "solution": "We declutter, tune, and stabilize without nuking your setup."
            },
            {
                "name": "NOT BOOTING / CRASHING / 'I THINK IT'S DEAD'",
                "symptoms": ["Black screens", "Clicky drives", "Looping logos"],
                "solution": "We treat it as a data rescue first, computer second."
            },
            {
                "name": "UPGRADES & FUTURE-PROOFING",
                "symptoms": ["Old but loved machines", "SSD/RAM/OS upgrade planning"],
                "solution": "We design the least painful path into the future."
            }
        ]
    },
    
    "how_session_works": {
        "title": "Three Steps From Panic to Plan",
        "steps": [
            {
                "name": "Tell Us What's Wrong (In Your Words)",
                "examples": ["'It's stupid slow.'", "'It won't start.'", "'I'm scared I lost everything.'"],
                "note": "NOIZYLAB listens & sorts the signal from the noise."
            },
            {
                "name": "Get a Clear, Honest Diagnosis",
                "points": ["What's likely wrong", "How serious it is", "How sure we are (we label confidence)"]
            },
            {
                "name": "Pick Your Path",
                "options": ["Quick tune-up today", "Deep repair with a long-term plan", "Data-first rescue with lab referral if needed"],
                "note": "You always know: What we recommend, What it will affect, How risky it is, How to say 'no' or 'not today'"
            }
        ]
    },
    
    "ethics": {
        "title": "We Don't Just Fix Tech. We Protect Your Trust.",
        "pillars": [
            {"name": "No Lies. Ever.", "detail": "If we don't know, we say so. We show you how we'll find out."},
            {"name": "No Shame. Ever.", "detail": "No 'you should've backed up.' No guilt for not being techy."},
            {"name": "No Hidden Trade-Offs.", "detail": "We always explain the risks, costs, and alternatives in plain language."},
            {"name": "No Cowboy Moves With Your Data.", "detail": "We never run destructive actions without clear warnings and your consent."}
        ],
        "footer": "If it's not something we'd recommend to our own family, we don't recommend it to you."
    },
    
    "for_who": {
        "title": "Who NOIZYLAB Is Perfect For",
        "audiences": [
            "Creators and freelancers who live on one main machine",
            "Small studios with 'too many aging computers'",
            "Families with years of photos and school work on old laptops",
            "Anyone who's already had a tech nightmare and never wants that feeling again"
        ]
    },
    
    "cta_final": {
        "title": "Tell Us What's Wrong. We'll Take It From There.",
        "buttons": ["Book a Remote Session", "Tell NOIZYLAB What's Going On"],
        "microcopy": "No commitment just to talk. We'll tell you honestly if repair, replacement, or data rescue makes the most sense."
    },
    
    "manifesto": """NOIZYLAB: WHERE BROKEN COMPUTERS MEET HUMAN BEINGS

Most computer repair feels like this:
• Confusing words
• Shrugging answers
• Wiped systems
• Blame when you "didn't back up"

NOIZYLAB was built to be the opposite.

We believe:

PEOPLE COME BEFORE MACHINES.
Your stress, your work, your memories matter more than blinking lights.

NO LIES. NO BLUFFING. NO FAKE MAGIC.
If we don't know yet, we'll say so—and we'll show you how we'll find out.

YOU SHOULD NEVER FACE A TECH CRISIS ALONE.
When your laptop won't start or your files seem gone, we're the calm voice
that knows exactly what to do next.

MIRACLES SHOULD FEEL SIMPLE.
Fixing complex problems shouldn't feel complicated on your side.
One clear step at a time is enough.

NOIZYLAB is:

• A council of 25 "Genius" AIs that watch over your devices,
  guided by strict ethics, real-world repair experience, and actual empathy.

• A quiet guardian that spots trouble early,
  so we can fix it when it's a nuisance, not a nightmare.

• A repair ally that explains everything in normal human language—
  always honest, always kind, always on your side.

We don't promise that nothing will ever break.
We promise you'll never be left alone with it again."""
}

# ═══════════════════════════════════════════════════════════════════════════════
# EXPORT FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def export_welcome_onepager(format: str = "text") -> str:
    """Export the client welcome one-pager."""
    if format == "text":
        return CLIENT_WELCOME_ONEPAGER
    elif format == "markdown":
        return CLIENT_WELCOME_ONEPAGER.replace("═", "-")
    else:
        return CLIENT_WELCOME_ONEPAGER

def export_service_menu(format: str = "text") -> str:
    """Export the service menu."""
    return get_service_menu_text()

def export_brand_pillars() -> str:
    """Export the brand pillars."""
    return get_brand_pillars_text()

def export_call_script() -> str:
    """Export the call/zoom script."""
    return CALL_SCRIPT

