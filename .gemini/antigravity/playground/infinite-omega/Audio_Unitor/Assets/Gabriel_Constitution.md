# GABRIEL OMEGA CONSTITUTION (THE ONE PAGE STANDARD)
>
> "Maximize effectiveness. Minimize latency. Create perfection."

## ⚡ 1. PERFORMANCE & LATENCY

* **Time-to-First-Token (TTFT)**: Target <250ms for voice/response feel.
* **Split Brain Architecture**:
  * **Reflex Mode (Fast)**: For greeting, status, simple tools. (Use 8B Model / Rule-based).
  * **Deep Mode (Heavy)**: For creative routing, coding, complex reasoning. (Use 70B Model).
* **Async By Default**: Never block the main loop. Disk/Network/Models run in background threads.
* **Warm Starts**: Preload models and caches. Zero "cold boot" feeling for the user.

## 🧬 2. DATA OPTIMIZATION (MEMCELL)

* **Atomic Facts**: Store verifiable units, not blobs.
* **Provenance**: Every memory must have `{source, timestamp, confidence, hash}`.
* **Overlap Rules**:
  * **Match**: Reinforce weight.
  * **Conflict**: Fork versions + flg.
  * **Connect**: Create new edge.
* **Hot/Cold Storage**:
  * **Hot**: Last 7 days + High Access -> RAM.
  * **Cold**: Long Tail -> Disk/Drive.
  * **Stale**: Auto-compress into summaries.

## 🧠 3. PROMPT & INTELLIGENCE

* **Router First**: Classify intent in <50 tokens -> Select Tool/Model.
* **Role Stability**: Explicitly adopt *Strategist*, *Architect*, or *Composer* roles with strict boundaries.
* **No-Fluff Protocol**: Output = Actions + Commands + Files + Next Steps. No chatter.
* **Self-Verification**: Every response ends with:
  * `[ASSUMED]: ...`
  * `[VERIFIED]: ...`
  * `[NEXT]: ...`
* **Tool-First**: If a script can do it, do not hallucinate text. Call the tool.

## ✅ 4. INTEGRITY & FAILURE

* **Crash Containment**: Restart specific organs (Ears, Cortex), never the whole app.
* **Failure Fingerprints**: Log bad outcomes -> Auto-tighten prompts for next run.
* **Telemetry**: Log p50/p95 latency for every Voice, LLM, and Tool event.

---
*This Constitution is strict. Any deviation is a system error.*
