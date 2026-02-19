# Stop Slop

A skill for removing AI tells from prose. Register-aware — works across casual, professional, academic, technical, and narrative writing.

<img width="3840" height="2160" alt="G-Yg4RVbIAAhVxW" src="https://github.com/user-attachments/assets/902afc15-1f40-4a9d-af24-8cd67afb8ebf" />

## What this is

AI writing has patterns. Predictable phrases, structures, rhythms. Once you notice them, you see them everywhere. This skill teaches Claude (or any LLM) to avoid them — and replaces them with clear, specific, human-sounding prose.

## Skill structure

```
stop-slop/
├── SKILL.md              # Core instructions (register detection → slop removal → scoring)
├── references/
│   ├── phrases.md        # 200+ phrases to cut or replace (AI vocabulary, chatbot artifacts, jargon)
│   ├── structures.md     # 14 structural patterns to avoid (format slop, synonym cycling, -ing clauses)
│   ├── positive.md       # What good writing does (specificity, active voice, rhythm, voice)
│   ├── registers.md      # Per-register rules (academic, technical, narrative, casual, professional)
│   └── examples.md       # 14 before/after transformations across all registers
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Quick start

**Claude Code:** Add this folder as a skill.

**Claude Projects:** Upload `SKILL.md` and reference files to project knowledge.

**Custom instructions:** Copy core rules from `SKILL.md`.

**API calls:** Include `SKILL.md` in your system prompt. Reference files load on demand.

## What it catches

**Phrases** — Throat-clearing openers, emphasis crutches, business jargon, AI vocabulary (delve, tapestry, multifaceted), chatbot artifacts, copula avoidance, significance inflation, sycophantic tone. See `references/phrases.md`.

**Structures** — Binary contrasts, dramatic fragmentation, rhetorical setups, format slop (emoji headings, inline-header lists), superficial -ing clauses, synonym cycling, rule-of-three overuse, generic conclusions, knowledge-cutoff disclaimers. See `references/structures.md`.

**What to do instead** — Be specific, use simple constructions, active voice, vary rhythm, have a voice, trust readers, acknowledge complexity. See `references/positive.md`.

## Register awareness

Different writing contexts tolerate different patterns. The skill detects register from context and adjusts rules:

| Register | Key adjustments |
|----------|----------------|
| Academic | Hedging OK when expressing epistemic uncertainty. Passive OK when agent unknown. |
| Technical | Bullets and headers OK. Promotional adjectives still flagged. |
| Narrative | Rhythm variation is a feature. Em dashes valid. Synonym cycling still flagged. |
| Casual | All rules at full force. |
| Professional | Similar to casual, tolerates more structure. |

See `references/registers.md` for full details.

## Scoring

Rate 1-10 on each dimension (adjusted for register):

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds human, not generated? |
| Density | Anything cuttable? |
| Specificity | Claims backed by evidence? |

Below 42/60: revise.

## Sources

Based on [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) by [Hardik Pandya](https://hvpandya.com). Enhanced with register-aware rules, positive writing guidance, and expanded pattern coverage synthesized from Antislop (Paech et al., ICLR 2026), Wikipedia AI Cleanup patterns, and Strunk's *Elements of Style*.

## License

MIT. Use freely, share widely.
