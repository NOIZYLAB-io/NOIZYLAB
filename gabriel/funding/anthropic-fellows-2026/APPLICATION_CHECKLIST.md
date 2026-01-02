# NoizyLab - Anthropic Fellows 2026 Application

## Application Checklist

**Deadline: January 12, 2026** ⏰

---

## 📋 Required Materials

### ✅ Complete
- [x] Research Statement (RESEARCH_STATEMENT.md)
- [x] Technical Specification (TECHNICAL_SPECIFICATION.md)

### 🔲 To Complete
- [ ] CV/Resume (academic format)
- [ ] Code samples (link to GABRIEL repo)
- [ ] 2-minute video pitch (optional but recommended)
- [ ] Reference contact (if required)

---

## 📝 Application Form Answers

### 1. Research Area
**Primary:** Adversarial Robustness  
**Secondary:** Scalable Oversight

### 2. One-Sentence Summary
> "Building AI systems that verify hardware integrity to prevent supply-chain attacks on AI infrastructure itself."

### 3. Why Anthropic?
Claude's extended thinking capability is uniquely suited for the multi-step reasoning required to synthesize visual evidence into tamper probability assessments. Unlike pure vision models, hardware integrity verification requires understanding context, history, and intent—exactly what Claude excels at. Additionally, as AI systems scale, the hardware running them becomes a critical attack surface that Anthropic has a vested interest in securing.

### 4. Why Now?
- The semiconductor counterfeit market has grown 15% YoY to $75B
- State-sponsored hardware trojans are confirmed (Bloomberg 2018, ongoing)
- AI compute demand is outpacing supply chain verification capacity
- Gemini 3 Flash enables real-time vision analysis at viable cost
- Cloudflare Workers AI enables edge deployment globally

### 5. What Will You Build?
**GABRIEL** (Generative Adversarial Board Inspection for Electronic Logic):
- A multimodal AI system combining Gemini vision + Claude reasoning
- "Golden Reference" database of verified-authentic hardware
- Public API for researchers and repair professionals
- Open-source core detection models
- Research paper on AI-driven hardware verification

### 6. Milestones (16 weeks)
| Week | Deliverable |
|------|-------------|
| 1-2 | Golden Reference database v1 (10K images) |
| 3-4 | Anomaly detection model fine-tuned |
| 5-6 | Claude reasoning integration |
| 7-8 | Evaluation benchmark (500 samples) |
| 9-10 | API public beta |
| 11-12 | Red-team testing |
| 13-14 | Paper draft complete |
| 15-16 | Open-source release + publication |

### 7. Location Preference
**Hybrid - Canada/London/Berkeley**

Rationale: Based in Canada but available for London or Berkeley collaborative sessions. Hardware samples and repair equipment are in home lab, so fully remote periods are optimal for hands-on research.

### 8. Compute Requirements
- **Claude API:** ~$2,000/month (Extended Thinking for complex analyses)
- **GPU:** Access to fine-tuning infrastructure for vision models
- **Storage:** ~500GB for reference image database

---

## 🎯 Key Talking Points

### For Reviewers
1. **Novel Application:** No one is applying LLMs to hardware security at scale
2. **Clear Safety Angle:** Hardware attacks undermine all software security
3. **Practical Impact:** Democratizes $500K inspection equipment to $50 smartphone
4. **Open Research:** All outputs will be open-source and published

### Differentiation from Existing Work
| Existing | GABRIEL |
|----------|---------|
| X-ray inspection | Visual + thermal + reasoning |
| Binary pass/fail | Calibrated probability + evidence chain |
| Specialist-only | Accessible to repair professionals |
| Single-component | Full board analysis |
| Proprietary | Open-source research |

---

## 📧 Submission Template

**Subject:** Anthropic Fellows 2026 - Hardware Integrity AI (NoizyLab)

**Body:**
```
Dear Anthropic Fellows Review Committee,

I am applying for the 2026 Anthropic Fellows Program with a research proposal 
on "Adversarial Robustness for Hardware Integrity."

My research addresses a critical gap in AI safety: while we invest heavily in 
aligning AI systems, the hardware running these systems remains vulnerable to 
supply-chain attacks. GABRIEL (Generative Adversarial Board Inspection for 
Electronic Logic) combines Claude's reasoning capabilities with computer vision 
to detect tampering, counterfeits, and defects in electronic hardware.

Key highlights:
• Novel application of multimodal AI to a $75B counterfeit market
• Direct relevance to AI infrastructure security
• Practical tool for the Right-to-Repair community
• Open-source deliverables and research publication

Attached:
• Research Statement
• Technical Specification
• GitHub: github.com/Noizyfish/GABRIEL

I am based in Canada and available for hybrid arrangements in London or Berkeley.

Thank you for your consideration.

Best regards,
[Your Name]
NoizyLab
```

---

## 🔗 Links to Include

- **GitHub Repo:** https://github.com/Noizyfish/GABRIEL
- **Demo (when ready):** https://scan.noizylab.ai
- **Personal Site:** https://noizylab.ai
- **LinkedIn:** [Your LinkedIn]

---

## ⏰ Timeline to Submission

| Date | Action |
|------|--------|
| Jan 2 | ✅ Research statement complete |
| Jan 3-4 | Record 2-min video pitch |
| Jan 5-6 | Update CV, gather code samples |
| Jan 7-8 | Get feedback from trusted reviewers |
| Jan 9-10 | Final revisions |
| Jan 11 | Submit application |
| Jan 12 | DEADLINE |

---

## 💡 Video Pitch Script (2 minutes)

```
[0:00 - 0:15] HOOK
"What if the chip running your AI has been compromised before you even 
plugged it in? I'm building an AI that can tell."

[0:15 - 0:45] PROBLEM
"The semiconductor counterfeit market is worth 75 billion dollars. 
Fake and tampered chips enter supply chains for medical devices, 
data centers, and yes—AI training clusters. Current detection requires 
half-million dollar X-ray equipment and PhD metallurgists."

[0:45 - 1:15] SOLUTION
"GABRIEL uses Claude's reasoning combined with Gemini's vision to 
analyze hardware photos. It compares them against a 'golden reference' 
database of verified authentic components, identifies anomalies, and 
explains WHY something looks suspicious—not just that it does."

[1:15 - 1:45] DEMO
[Show: Photo of CPU socket → AI overlay highlighting bent pin → 
Voice guidance explaining the issue]

[1:45 - 2:00] ASK
"With Anthropic's support, I'll build this into an open-source tool 
that puts hardware security in every repair technician's hands. 
Because AI safety has to include the atoms, not just the bits."
```

---

*Last updated: January 2, 2026*
