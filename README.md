# Stop Slop (Patched)

A skill for removing AI tells from prose, with one bug fixed in the reference examples.

This is a fork of [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop). The original example file broke its own rules, so I patched it. Details below.

<img width="3840" height="2160" alt="G-Yg4RVbIAAhVxW" src="https://github.com/user-attachments/assets/902afc15-1f40-4a9d-af24-8cd67afb8ebf" />

## What this is

AI writing has patterns. Predictable phrases, structures, rhythms. This skill teaches Claude (or any LLM) to catch and remove them.

## Skill Structure

```
stop-slop/
├── SKILL.md              # Core instructions
├── references/
│   ├── phrases.md        # Phrases to remove
│   ├── structures.md     # Structural patterns to avoid
│   └── examples.md       # Before/after transformations
├── README.md
└── LICENSE
```

## Quick start

**Claude Code:** Add this folder as a skill.

**Claude Projects:** Upload `SKILL.md` and reference files to project knowledge.

**Custom instructions:** Copy core rules from `SKILL.md`.

**API calls:** Include `SKILL.md` in your system prompt. Reference files load on demand.

## What it catches

**Banned phrases** - throat-clearing openers, emphasis crutches, business jargon, all adverbs, vague declaratives, meta-commentary. See `references/phrases.md`.

**Structural clichés** - binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency, narrator-from-a-distance voice, passive voice. See `references/structures.md`.

**Sentence-level rules** - no Wh- sentence starters, no em dashes, no staccato fragmentation, no lazy extremes, active voice required.

## The fix

Example 4's "after" text used an em dash: "Speed, quality, cost—pick two." That breaks the skill's own rule against em dashes. I changed it to "You can pick two of speed, quality, and cost."

Example 2 had a similar problem. It used "nobody," which `references/structures.md` bans as a lazy extreme. I changed it to "Few people admit they're confused."

Only these two examples changed. Everything else matches the original repo.

## Scoring

Rate 1-10 on each dimension:

| Dimension    | Question                      |
|--------------|--------------------------------|
| Directness   | Statements or announcements?  |
| Rhythm       | Varied or metronomic?         |
| Trust        | Respects reader intelligence? |
| Authenticity | Sounds human?                 |
| Density      | Anything cuttable?            |

Below 35/50: revise.

## Original author

Hardik Pandya (https://hvpandya.com) created the original Stop Slop skill.

## License

MIT. Use freely, share widely.
