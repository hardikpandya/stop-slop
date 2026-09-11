# Stop Slop

A skill for removing AI tells from prose.

<img width="3840" height="2160" alt="G-Yg4RVbIAAhVxW" src="https://github.com/user-attachments/assets/902afc15-1f40-4a9d-af24-8cd67afb8ebf" />

## What this is

AI writing has patterns. Predictable phrases, structures, rhythms. This skill teaches Claude (or any LLM) to catch and remove them.

Edit is the default: rewrite the draft, keep the writer's voice, change only what the rules require. Detect/audit is optional: name the pattern, quote the line, give a short fix, do not rewrite.

## Skill Structure

```
stop-slop/
├── SKILL.md              # Core instructions
├── references/
│   ├── phrases.md        # Phrases to remove
│   ├── structures.md     # Structural patterns to avoid
│   ├── examples.md       # Before/after transformations
│   └── eval.md           # Post-edit pass/fail checklist
├── README.md
└── LICENSE
```

## Quick start

**Claude Code:** Add this folder as a skill.

**Claude Projects:** Upload `SKILL.md` and reference files to project knowledge.

**Custom instructions:** Copy core rules from `SKILL.md`.

**API calls:** Include `SKILL.md` in your system prompt. Reference files load on demand.

## What it catches

**Banned phrases** - Throat-clearing openers, emphasis crutches, business jargon, empty adverbs, vague declaratives, meta-commentary, faux-insight setups, importance puffery, weasel attribution, interpretive metadiscourse. See `references/phrases.md`.

**Structural clichés** - Binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency, narrator-from-a-distance voice, passive voice, colon-reveal drama, superficial -ing analysis, synonym cycling, fake-profound kickers, formatting slop. See `references/structures.md`.

**Sentence-level rules** - No Wh- sentence starters, no staccato fragmentation, no lazy extremes, active voice required. Cut em dashes by default; keep a rare one in a longer draft if a comma, period, or parenthesis is worse. Cut empty adverbs; keep ones that carry emphasis, uncertainty, or spoken rhythm.

**Voice** - Minimum effective edit. Keep distinctive cadence, bluntness, humor, uncertainty, and digressions. Do not flatten every draft into the same punchy house style.

## Scoring

Rate 1-10 on each dimension:

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds like this writer, or like generic AI? |
| Density | Anything cuttable? |

Below 35/50: revise.

## Author

[Hardik Pandya](https://hvpandya.com)

## License

MIT. Use freely, share widely.
