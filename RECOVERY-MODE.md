# NOIZYLAB – RECOVERY MODE PLAYBOOK (WHEN SH*T BREAKS)

> RULE 0: PANIC IS BANNED. CHECKLISTS ONLY.

---

## 1️⃣ FIRST 60 SECONDS – DON'T TOUCH ANYTHING

### WHEN SOMETHING GOES WRONG:

- **HANDS OFF.**
- DON'T START RANDOM FIXES.
- DON'T CLICK EVERY POPUP.

### ASK 3 QUESTIONS:

1. **WHAT EXACTLY BROKE?** (Device / Drive / Network / App / Files?)
2. **CAN I STILL ACCESS GABRIEL?**
3. **IS THIS URGENT FOR MONEY / CLIENT / FAMILY?** (YES/NO)

### WRITE ONE LINE IN A NOTE / PAPER:

```
DATE – WHAT I SAW – WHAT I WAS DOING WHEN IT HAPPENED
```

**THAT ONE LINE SAVES FUTURE YOU.**

---

## 2️⃣ QUICK TRIAGE TREE – WHAT KIND OF DISASTER IS THIS?

**PICK THE CLOSEST MATCH:**

| Symptom | Jump To |
|---------|---------|
| GABRIEL NOT MOUNTING / STORAGE ISSUE | Section 3 |
| NOIZY-CORE (M2 ULTRA) ACTING DEAD / WON'T BOOT | Section 4 |
| BACKLINE-12 (MAC PRO) ISSUE | Section 5 |
| NO INTERNET / NETWORK CHAOS (MC96?) | Section 6 |
| FILES GONE / FOLDER MISSING / "WHERE DID IT GO?" | Section 7 |
| WEIRD POP-UPS / POSSIBLE MALWARE | Section 8 |

---

## 3️⃣ GABRIEL ISSUE – MAIN STORAGE NOT MOUNTING

**SYMPTOMS:** Gabriel not showing up, timeouts, strange noises, errors when accessing.

### STEP A – DO NOT:

- ❌ DO NOT RUN RANDOM "CLEANER" APPS.
- ❌ DO NOT FORCE FORMAT ANYTHING.
- ❌ DO NOT FORCE DISCONNECT IN A PANIC.

### STEP B – BASIC CHECKS

**CHECK CABLE / POWER / PORT:**
- Physically confirm: power light on, cable seated.
- Try another port on MC96 or direct to NOIZY-CORE.

**CHECK IF ANY OTHER MACHINE SEES GABRIEL:**
- Try on BACKLINE-12 or a Scout machine.

**IF IT'S JUST NOT MOUNTING BUT MAKING NO HORRIBLE NOISES:**
- Note the time + symptoms in `RECOVERY-LOG.md`.

### STEP C – FALLBACK BEHAVIOUR

**SWITCH TO MIRROR FOR CRITICAL STUFF:**
- USE: `BACKLINE-12/NOIZY_OS_MIRROR/` for any urgent work.
- MARK CLEARLY: "WORKING FROM MIRROR" in your notes.
- Mark system as "DEGRADED BUT OPERABLE."

**NEXT ACTION (WHEN CALM):**
- Later: Run a proper disk check / get help with drive diagnostics.
- Until then: Minimize new writes to GABRIEL.

---

## 4️⃣ NOIZY-CORE (M2 ULTRA) WON'T BOOT / IS FREAKING OUT

**SYMPTOMS:** Won't start, boots to error, constant crashes.

### STEP A – PRIORITY QUESTION

> "DO I NEED SOMETHING RIGHT NOW FOR A CLIENT OR FAMILY?"

- **IF YES** → Use another machine + Backline mirror to access files.
- **IF NO** → Take breath, continue.

### STEP B – DON'T:

- ❌ DON'T IMMEDIATELY NUKE / REINSTALL WITHOUT THINKING.
- ❌ DON'T TRY 12 EXPERIMENTS IN A ROW. Pick a path, document.

### STEP C – DATA COMFORT CHECK

> IS MOST OF YOUR IMPORTANT STUFF ON GABRIEL/NOIZY_OS?

- **IF YES** → Your data is likely safe. Machine is just a tool.
- Switch to Scout machine temporarily if needed.

### STEP D – TEMPORARY WORKAROUND

**USE SCOUT OR BACKLINE-12 TO:**
- Access `NOIZY_OS_MIRROR` or GABRIEL (if it's still OK).
- Continue urgent work from there.

**LATER, PROPER PATH:**
- Run basic Mac Recovery / Safe Mode / Disk Utility.
- If complex → Document and get external help if needed.

---

## 5️⃣ BACKLINE-12 (MAC PRO) ISSUE

**REMEMBER:** BACKLINE-12 = Backup / Archive / Muscle. NOT your only brain.

### IF BACKLINE-12 GOES DOWN:

**CHECK:**
- Is GABRIEL OK?
- **IF YES** → Primary work is still alive.

**RULE:**
- Don't start massive experiments on Backline that risk connected drives.

**TEMP OPERATION MODE:**
- NOTE: "BACKLINE-12 DOWN – TEMPORARY LOSS OF MIRROR / ARCHIVES."
- PRIORITY: Keep GABRIEL clean & safe. Backline can be fixed later.

---

## 6️⃣ NETWORK / MC96 ISSUE (NO INTERNET / WEIRD CONNECTIVITY)

**SYMPTOMS:** No internet, machines can't see each other, everything "offline".

### STEP A – SIMPLE LADDER

1. CHECK: Is router / modem online?
2. CHECK: Is MC96 powered / lights on?
3. CHECK: Can machines see GABRIEL/other machines locally?
   - **IF YES** → Local network partly OK, internet might be the only problem.
   - **IF NO** → Issue may be MC96 / internal switch / cabling.

### STEP B – LOCAL VS INTERNET

**IF INTERNET IS DOWN BUT LAN WORKS:**
- You can still access GABRIEL, BACKLINE, client files.
- Make a note: "INTERNET DOWN, LOCAL OK – CONTINUE OFFLINE WORK."

**IF LOCAL IS DOWN:**
- Use a direct cable connection to GABRIEL from NOIZY-CORE if possible.
- That gives you a temp lifeline to files.

---

## 7️⃣ FILES GONE / FOLDER MISSING

**SYMPTOMS:** "I swear this folder was here." / "Where did that file go?"

### STEP A – DO NOT:

- ❌ DO NOT INSTALL RANDOM "RECOVERY" SOFTWARE YET.
- ❌ DO NOT SAVE NEW FILES OVER THE SAME AREA IF YOU SUSPECT DELETION.

### STEP B – LOOK INTELLIGENTLY

**SEARCH ON:**
- GABRIEL → Use Spotlight by name
- BACKLINE MIRROR → Check equivalent path
- Check Trash / Recent Items.

**IF CLIENT FOLDER:**
- Check: `Clients/[CLIENT]/20-ASSETS/` & related.

### STEP C – TEMP STATUS

**IF FOUND ON MIRROR BUT NOT ON GABRIEL:**
- MARK: "SOURCE DESYNCED – USE MIRROR COPY, RESYNC LATER."

**IF NOT FOUND ANYWHERE:**
- Write event in `RECOVERY-LOG.md`
- Flag for possible recovery later when you have energy/help.

---

## 8️⃣ POSSIBLE MALWARE / WEIRD POP-UPS / SOMETHING FEELS "OFF"

**SYMPTOMS:** Random popups, "call this number," strange security messages, fake "cleaner" apps.

### STEP A – ABSOLUTE RULES

- ❌ **DO NOT CALL ANY NUMBER IN A POPUP.**
- ❌ **DO NOT GIVE ANYONE REMOTE ACCESS WHO JUST "CALLED FROM MICROSOFT / APPLE."**
- ❌ **DO NOT ENTER PASSWORDS INTO RANDOM POPUP WINDOWS.**

### STEP B – IMMEDIATE CONTAINMENT

- Disconnect from internet if it feels really bad.
- Close browser / app that triggered it.
- Take a quick photo / screenshot of weird popup for later reference.

### STEP C – CLEANUP APPROACH

- Use known, trusted tools only (no "random internet fix this" apps).
- If in doubt → Park it, work off backup machine / Scout until you have a clear plan.

---

## 9️⃣ RECOVERY-LOG FILE (MANDATORY)

**CREATE:** `/Users/m2ultra/NOIZYLAB/MC96-MISSION-CONTROL/RECOVERY-LOG.md`

**EVERY TIME SOMETHING BAD HAPPENS, ADD A LINE OR BLOCK:**

```markdown
## [DATE – ISSUE SUMMARY]

WHAT HAPPENED:
- (one or two lines)

WHAT I DID:
- Step 1:
- Step 2:

STATUS:
- RESOLVED / TEMP WORKAROUND / NEEDS PRO HELP

NOTES FOR FUTURE ME:
- "Next time, do this first:"
```

**THIS BUILDS YOUR OWN DOCUMENTED EXPERIENCE, SO THE SYSTEM GETS SMARTER OVER TIME.**

---

## 🔟 "RECOVERY MODE MINDSET" (THE MOST IMPORTANT PART)

| Situation | Reality |
|-----------|---------|
| Device problem but data is on GABRIEL | You're inconvenienced, not dead. |
| GABRIEL + Mirror are healthy | You still own your past. |
| Something goes very wrong | STOP, LOG, DO LEAST-HARM ACTIONS, ASK FOR HELP. |

---

**YOU'RE NOT ALLOWED TO CALL YOURSELF "BAD WITH TECH" HERE.**

You're the one who built a whole eco-universe. This playbook is how you keep it alive.

---

```
MC96 = THE NERVOUS SYSTEM
GABRIEL = THE MEMORY
NOIZY-CORE = THE BRAIN
BACKLINE-12 = THE MUSCLE

PANIC IS BANNED. CHECKLISTS ONLY.
```

