# NOIZYLAB – POWER-OUT / EMERGENCY MODE

> RULE 0: PROTECT DRIVES FIRST. EVERYTHING ELSE CAN WAIT.

---

## 1️⃣ PREP MODE (BEFORE ANYTHING GOES WRONG)

These are "do once and you're safer forever" items:

### If possible, put this gear on UPS / surge:

- [ ] MC96 switch
- [ ] GABRIEL
- [ ] NOIZY-CORE (M2 Ultra)
- [ ] BACKLINE-12 (Mac Pro)

### Label power strips clearly:

```
"CORE / GABRIEL / BACKLINE / SCOUTS"
```

### Create this file (you're doing it now):

- `POWER-OUT-MODE.md` (this doc)
- **Print it and stick it where you can see it.**

---

## 2️⃣ WHEN LIGHTS FLICKER / YOU SUSPECT POWER ISSUES

**If you get flickers, brownouts, or storms incoming:**

### Save current work immediately

- Hit save on whatever is open.
- Close anything writing heavily to disk (render, big copy, etc.) if you can.

### Pause non-essential activities

- Don't start new installs, OS updates, big renders, or large file moves.

### If it feels sketchy, pre-emptively shut down BACKLINE-12 first

- It's muscle + archive – protect it early.

---

## 3️⃣ WHEN POWER ACTUALLY GOES OUT

### HARD RULE: DO NOT PANIC-POWER THINGS BACK ON AND OFF.

### Step 1 – Hands off

- Don't start hitting buttons in the dark.
- Let everything power down fully.

### Step 2 – Mentally note what was running

If you can, note in your head or on paper:

- Was GABRIEL actively copying or rendering?
- Were you mid-OS update or software install?
- Which machine were you on (NOIZY-CORE / BACKLINE / SCOUT)?

We'll log this later.

---

## 4️⃣ WHEN POWER RETURNS – ORDER OF RESURRECTION

### RULE: BRING THE NERVOUS SYSTEM UP FIRST, THEN ORGANS, THEN MUSCLE.

**Start in this order:**

| Order | Component | Notes |
|-------|-----------|-------|
| 1 | **MC96 (NETWORK SWITCH)** | Turn on / verify power and lights. Give it 30–60 seconds to settle. |
| 2 | **ROUTER / MODEM (INTERNET)** | Only if you need internet right away. Can delay for local work. |
| 3 | **GABRIEL (STORAGE)** | Power on calmly. Wait for full spin up & mount. |
| 4 | **NOIZY-CORE (M2 ULTRA)** | Boot only after MC96 + GABRIEL are stable. Let it chill before opening apps. |
| 5 | **BACKLINE-12 (MAC PRO)** | Boot this last. It's muscle/backup – not first priority. |
| 6 | **SCOUT MACHINES** | Only when needed. |

---

## 5️⃣ FIRST BOOT CHECKLIST (RIGHT AFTER POWER COMES BACK)

### On NOIZY-CORE:

**Check: Is GABRIEL mounted?**
- Path: `/Volumes/GABRIEL/`
- **IF YES** → Good.
- **IF NO** → Don't brute force; treat it like a possible drive event (use `RECOVERY-MODE.md`).

**Check: Can you see MC96-connected devices?**
- Ping / browse BACKLINE-12 if it's up.

**Open MC96-MISSION-CONTROL**
- Confirm you can reach:
  - `LIFELUV.md`
  - `2NDLIFE.md`
  - `FLOW.md`

### Log the event

In `RECOVERY-LOG.md`, add:

```markdown
## [DATE – POWER OUTAGE]

WHAT HAPPENED:
- Power cut while I was [doing X] on [machine].

WHAT WAS RUNNING:
- Machines: [NOIZY-CORE / BACKLINE-12 / SCOUTS]
- Storage: [GABRIEL – idle / copying / unknown]

FIRST CHECKS:
- Did GABRIEL mount? (Yes/No)
- Any obvious corruption / missing volumes? (Yes/No)
```

---

## 6️⃣ IF SOMETHING FEELS "WRONG" AFTER POWER IS BACK

### Common issues:

- Drive not mounting
- System slow / weird errors
- Apps complaining about corrupted databases/projects

### Don't freestyle this. Use:

| Issue | Go To |
|-------|-------|
| GABRIEL is weird | `RECOVERY-MODE.md` Section 3 |
| NOIZY-CORE is wonky | `RECOVERY-MODE.md` Section 4 |
| BACKLINE-12 is weird | `RECOVERY-MODE.md` Section 5 |

**You already wrote those muscles. Use them.**

---

## 7️⃣ WHAT YOU SHOULD NOT DO AFTER A POWER EVENT

**For the first hours after a serious outage:**

### ❌ Don't run:

- Major OS upgrades
- Firmware updates
- Massive file moves between drives
- Disk "repair" tools you don't fully trust

### ✅ Do:

- Work on low-risk tasks
- Check backups & mirrors
- Verify key client folders and important archives exist in at least one healthy location.

---

## 8️⃣ QUICK "AM I SAFE?" SELF-CHECK

After you've done the basics, ask:

| Question | Yes/No |
|----------|--------|
| Is GABRIEL visible and behaving normally? | |
| Is BACKLINE-12 alive (or at least not making scary drive noises)? | |
| Can I open NOIZY_OS and a few client folders without errors? | |
| Do I have at least one recent backup or mirror of NOIZY_OS? | |

**If most of those are "yes,"** you're inconvenienced, not doomed.

**If your gut says something's off** → write it in `RECOVERY-LOG.md` and flag "NEEDS DEEPER CHECK."

---

## 9️⃣ EMERGENCY LOW-ENERGY SCRIPT (WHEN YOU'RE FRIED)

When you're exhausted and something goes wrong, **read this literally:**

```
STEP 1: STOP TOUCHING THINGS.

STEP 2: WAIT UNTIL POWER IS STABLE.

STEP 3: TURN ON MC96 → GABRIEL → NOIZY-CORE IN THAT ORDER.

STEP 4: CHECK IF /Volumes/GABRIEL/NOIZY_OS/ OPENS.

STEP 5: WRITE ONE LINE IN RECOVERY-LOG.md ABOUT WHAT HAPPENED.

STEP 6: IF ANYTHING SEEMS BAD, OPEN RECOVERY-MODE.md AND FOLLOW THAT INSTEAD OF GUESSING.
```

---

**You don't have to be clever in emergencies.**
**You just have to follow your own script.**

---

```
MC96 = THE NERVOUS SYSTEM
GABRIEL = THE MEMORY
NOIZY-CORE = THE BRAIN
BACKLINE-12 = THE MUSCLE

PROTECT DRIVES FIRST. EVERYTHING ELSE CAN WAIT.
```

