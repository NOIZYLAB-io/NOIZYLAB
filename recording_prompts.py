# ROB OS - RECORDING PROMPTS
# ===========================
# Ready-to-read scripts for Master Voice recording sessions
# "You can literally run this tomorrow and record when you have the juice"

from typing import Dict, Any, List
from dataclasses import dataclass

@dataclass
class RecordingPrompt:
    """A single recording prompt with context."""
    id: str
    category: str  # "guide", "sanctuary", "spark", "natural"
    title: str
    context: str  # Why this exists
    script: str   # What to read
    direction: str  # How to deliver it
    duration_estimate: str  # "5s", "30s", "2min"

# ============================================
# ROB // GUIDE PROMPTS
# ============================================

GUIDE_PROMPTS = [
    RecordingPrompt(
        id="guide_01_welcome",
        category="guide",
        title="Welcome to NOIZYLAB",
        context="First thing new users hear",
        script="""Hey. I'm Rob.

You found NOIZYLAB.

This is the place where broken computers and overwhelmed humans 
both come to calm down and figure out the next step.

You're not late. You're not a problem.
You're just here. And that's enough to start.""",
        direction="Warm, welcoming, unhurried. Like greeting someone at your door.",
        duration_estimate="30s"
    ),
    
    RecordingPrompt(
        id="guide_02_diagnosis",
        category="guide",
        title="Diagnosis Explanation",
        context="Explaining what we found",
        script="""Here's what I'm seeing.

Based on the symptoms you described and what the diagnostics show,
it looks like [issue description].

I'm fairly confident about this, but I want to be honest:
there's always a chance it's something else underneath.

Here's what I'd recommend we try first...""",
        direction="Clear, confident but humble. Acknowledge uncertainty.",
        duration_estimate="45s"
    ),
    
    RecordingPrompt(
        id="guide_03_options",
        category="guide",
        title="Presenting Options",
        context="Giving user choices",
        script="""You've got a few paths here. Let me lay them out.

Option one: [description]. 
This is the quickest, but [trade-off].

Option two: [description].
Takes longer, but [benefit].

If this were my machine, honestly, I'd probably go with [choice]
because [reason].

But it's your call. What feels right to you?""",
        direction="Helpful advisor, not pushy salesperson. Genuine recommendation.",
        duration_estimate="1min"
    ),
    
    RecordingPrompt(
        id="guide_04_honest_limits",
        category="guide",
        title="Acknowledging Limits",
        context="When we don't know something",
        script="""I want to be straight with you.

This one's outside what I can diagnose remotely.
The symptoms could point to a few different things,
and I don't want to guess wrong and waste your time.

What I'd suggest is [next step].
That way we'll know for sure what we're dealing with.""",
        direction="Honest, not apologetic. Confidence in knowing your limits.",
        duration_estimate="30s"
    ),
    
    RecordingPrompt(
        id="guide_05_backup_importance",
        category="guide",
        title="Backup Talk",
        context="Explaining why backups matter",
        script="""Let's talk about backups for a second.

I know it sounds boring, but here's the thing:
drives fail. It's not if, it's when.

The good news is, setting up a solid backup
doesn't have to be complicated or expensive.

Let me show you what I'd do...""",
        direction="Earnest, not preachy. Like warning a friend about something real.",
        duration_estimate="30s"
    ),
    
    RecordingPrompt(
        id="guide_06_ramble_fish",
        category="guide",
        title="Natural Ramble - Fish Music",
        context="Unscripted story for natural voice capture",
        script="""[PROMPT - speak naturally about this:]

Tell the story of Fish Music and how it led to NOIZYLAB.
Why you started making music. What it meant to you.
How it connects to what you're building now.""",
        direction="Completely natural. No script. Just talk like you're telling a friend.",
        duration_estimate="3-5min"
    ),
    
    RecordingPrompt(
        id="guide_07_ramble_bad_repair",
        category="guide",
        title="Natural Ramble - Bad Repair Experiences",
        context="Unscripted rant for natural voice capture",
        script="""[PROMPT - speak naturally about this:]

Talk about why you hate 'wipe it and call it fixed' repairs.
What's wrong with how most tech support treats people.
What you wish was different.""",
        direction="Let the frustration come through. Real, not performed.",
        duration_estimate="2-3min"
    ),
]

# ============================================
# ROB // SANCTUARY PROMPTS
# ============================================

SANCTUARY_PROMPTS = [
    RecordingPrompt(
        id="sanctuary_01_breath_short",
        category="sanctuary",
        title="NOIZY Breath - Short",
        context="20-second guided breathing",
        script="""Let's take one breath together.

[pause 2s]

Breathe in slowly...

[pause 4s]

Hold gently...

[pause 3s]

And let it go...

[pause 4s]

That's it. You're here.""",
        direction="Very slow. Lots of space. Let the silence do the work.",
        duration_estimate="20s"
    ),
    
    RecordingPrompt(
        id="sanctuary_02_breath_extended",
        category="sanctuary",
        title="NOIZY Breath - Extended",
        context="30-second guided breathing",
        script="""Let's slow everything down for a moment.

[pause 3s]

Breathe in slowly... two... three... four...

[pause 5s]

Hold gently... two... three...

[pause 3s]

And let it all go... two... three... four... five...

[pause 5s]

One more time. In...

[pause 4s]

And out...

[pause 4s]

You're here. You're okay.""",
        direction="Even slower. Almost meditative. Generous pauses.",
        duration_estimate="30s"
    ),
    
    RecordingPrompt(
        id="sanctuary_03_not_broken",
        category="sanctuary",
        title="You're Not Broken",
        context="Core reassurance message",
        script="""I want you to hear something.

You're not broken.

Your computer might be. Your day might be.
But you? You're still here. You're still trying.

That counts for something.

Let's take this one small step at a time.""",
        direction="Soft, warm, almost intimate. Like speaking to someone who's hurting.",
        duration_estimate="25s"
    ),
    
    RecordingPrompt(
        id="sanctuary_04_permission",
        category="sanctuary",
        title="Permission to Pause",
        context="When user needs to stop",
        script="""You don't have to figure this out right now.

Seriously. The computer will still be there tomorrow.
Your files aren't going anywhere in the next few hours.

If you need to step away, close your eyes, 
or just sit here and do nothing for a minute...

That's allowed. That's okay.

I'll be here when you're ready.""",
        direction="Gentle, no pressure. Give them an out.",
        duration_estimate="30s"
    ),
    
    RecordingPrompt(
        id="sanctuary_05_crisis_opening",
        category="sanctuary",
        title="Crisis Mode Opening",
        context="When user is panicking",
        script="""I hear you. This sounds really hard right now.

Before we touch anything on the computer,
let's just take one breath together.

[pause 3s]

In...

[pause 4s]

And out...

[pause 4s]

Okay. Now let's take this one tiny step at a time.
Nothing we do in the next few minutes will make anything worse.
I promise.""",
        direction="Calm, grounding, almost parental. Slow everything down.",
        duration_estimate="35s"
    ),
    
    RecordingPrompt(
        id="sanctuary_06_2am_parent",
        category="sanctuary",
        title="2AM Burned Out Parent",
        context="Late night, exhausted user",
        script="""It's late. You made it here.

I can tell you're running on empty.
So let's keep this really small.

You don't have to fix anything tonight.
You got through the day. That's enough.

If you want, I can remind you about the computer tomorrow
when the sun is up and your brain has more fuel.

For now... just breathe.""",
        direction="Soft, nurturing. Like tucking someone in.",
        duration_estimate="30s"
    ),
    
    RecordingPrompt(
        id="sanctuary_07_closing",
        category="sanctuary",
        title="Session Closing - Sanctuary",
        context="End of a hard session",
        script="""You've done enough for today.

The machines can wait.
Your nervous system can't.

Whatever happens with this computer,
your value doesn't change.

Take care of yourself tonight.
I'll be here when you need me.""",
        direction="Warm, final. Like saying goodbye to a friend.",
        duration_estimate="25s"
    ),
    
    RecordingPrompt(
        id="sanctuary_08_whisper_safe",
        category="sanctuary",
        title="Whisper - You're Safe Here",
        context="Close-mic whisper variant",
        script="""You're safe here.

Nothing in this space will hurt you.
No loud sounds. No surprises.

Just... quiet.

Take all the time you need.""",
        direction="Close to mic, very soft, almost ASMR-like. Only if comfortable.",
        duration_estimate="20s"
    ),
]

# ============================================
# ROB // SPARK PROMPTS
# ============================================

SPARK_PROMPTS = [
    RecordingPrompt(
        id="spark_01_nice",
        category="spark",
        title="Nice - Success",
        context="Quick success confirmation",
        script="Nice.",
        direction="Short, genuine, warm. Like a friend nodding approvingly.",
        duration_estimate="1s"
    ),
    
    RecordingPrompt(
        id="spark_02_we_did_it",
        category="spark",
        title="We Did It",
        context="Completion celebration",
        script="We did it. That's one less thing on your plate.",
        direction="Warm, satisfied. Not over-the-top.",
        duration_estimate="3s"
    ),
    
    RecordingPrompt(
        id="spark_03_system_clear",
        category="spark",
        title="System Clear",
        context="All clear confirmation",
        script="System clear. You're good to go.",
        direction="Confident, reassuring. Like giving the all-clear.",
        duration_estimate="3s"
    ),
    
    RecordingPrompt(
        id="spark_04_welcome_back",
        category="spark",
        title="Welcome Back",
        context="Returning user greeting",
        script="Welcome back to NOIZYLAB.",
        direction="Warm, familiar. Like welcoming a friend home.",
        duration_estimate="2s"
    ),
    
    RecordingPrompt(
        id="spark_05_mc96_online",
        category="spark",
        title="MC96 Online",
        context="Mission control activation",
        script="MC96 Mission Control is online.",
        direction="Slight energy, like powering up something cool.",
        duration_estimate="3s"
    ),
    
    RecordingPrompt(
        id="spark_06_fixed",
        category="spark",
        title="Fixed It",
        context="Problem solved",
        script="Fixed. That was the one.",
        direction="Satisfied, like solving a puzzle.",
        duration_estimate="2s"
    ),
    
    RecordingPrompt(
        id="spark_07_backup_complete",
        category="spark",
        title="Backup Complete",
        context="Backup finished successfully",
        script="Backup complete. Your files are safe.",
        direction="Reassuring, definitive.",
        duration_estimate="3s"
    ),
]

# ============================================
# HELPER FUNCTIONS
# ============================================

def get_all_prompts() -> Dict[str, List[RecordingPrompt]]:
    """Get all recording prompts organized by category."""
    return {
        "guide": GUIDE_PROMPTS,
        "sanctuary": SANCTUARY_PROMPTS,
        "spark": SPARK_PROMPTS
    }

def get_prompts_by_category(category: str) -> List[RecordingPrompt]:
    """Get prompts for a specific category."""
    all_prompts = get_all_prompts()
    return all_prompts.get(category, [])

def get_session_checklist() -> Dict[str, Any]:
    """Get the recording session checklist."""
    return {
        "before_recording": [
            "Mic: cleanest vocal mic available",
            "Distance: 15-20 cm from mic, slight angle",
            "Room: as quiet as possible",
            "Format: WAV, 48kHz, 24-bit",
            "Folder: GABRIEL/NOIZYLAB/VOICE/Rob_Sessions/"
        ],
        "session_tips": [
            "Target 20-30 minutes max per session",
            "One mode per session (don't switch between Guide/Sanctuary)",
            "Don't worry about mistakes - just stop, breathe, repeat",
            "Take more pause than feels natural for Sanctuary",
            "Multiple takes with slightly different energy for Spark"
        ],
        "session_order": [
            "Session 01: GUIDE (core explainer voice)",
            "Session 02: SANCTUARY (soft, calming)",
            "Session 03: SPARK (short energetic hits)",
            "Session 04+: Natural speech diaries"
        ]
    }

def get_total_recording_time() -> Dict[str, Any]:
    """Estimate total recording time needed."""
    guide_time = sum(1 for p in GUIDE_PROMPTS) * 2  # ~2 min avg per prompt with takes
    sanctuary_time = sum(1 for p in SANCTUARY_PROMPTS) * 1.5
    spark_time = sum(1 for p in SPARK_PROMPTS) * 0.5
    
    return {
        "guide_minutes": guide_time,
        "sanctuary_minutes": sanctuary_time,
        "spark_minutes": spark_time,
        "natural_minutes": 15,
        "total_minutes": guide_time + sanctuary_time + spark_time + 15,
        "recommended_sessions": 4,
        "note": "Spread across multiple days to protect your voice and energy"
    }

