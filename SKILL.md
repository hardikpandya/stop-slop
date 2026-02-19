---
name: stop-slop
description: Remove AI writing patterns from prose. This skill should be used when drafting, editing, or reviewing text to eliminate predictable AI tells. Register-aware — handles casual, professional, academic, technical, and narrative writing.
---

# Stop Slop

Eliminate predictable AI writing patterns. Produce clear, specific, human-sounding prose across any register.

## Step 1: Detect register

Infer the register from context before applying rules. Different registers tolerate different patterns.

| Signal | Register |
|--------|----------|
| Citations, methodology, "we hypothesize" | `academic` |
| API docs, READMEs, changelogs, error messages | `technical` |
| Fiction, essays, memoir, creative nonfiction | `narrative` |
| Blog posts, social media, emails | `casual` |
| Reports, proposals, business comms | `professional` |

If the user specifies a register, use it. See [references/registers.md](references/registers.md) for per-register acceptable vs. flagged patterns.

## Step 2: Remove slop

Apply these rules, adjusted for register:

1. **Cut filler phrases and AI vocabulary.** Remove throat-clearing openers, chatbot artifacts, significance inflation, and words that appear 100-1,000x more in LLM output than human text. See [references/phrases.md](references/phrases.md).

2. **Break formulaic structures.** Avoid binary contrasts, dramatic fragmentation, format slop, synonym cycling, rule-of-three overuse, and generic conclusions. See [references/structures.md](references/structures.md).

3. **Use simple constructions.** Prefer "is" over "serves as." Prefer "has" over "boasts." Prefer "use" over "leverage." Active voice. Positive form.

4. **Be specific.** Replace vague claims with dates, names, numbers, sources. "Significant improvement" becomes "latency dropped from 340ms to 90ms."

5. **Vary rhythm.** Mix sentence lengths. Two items in a list beat three. End paragraphs differently from each other.

6. **Trust readers.** State facts. Skip softening, justification, hand-holding. If a metaphor needs explaining, rewrite the metaphor.

7. **Have a voice.** React to facts, don't just report them. Acknowledge complexity. Let personality through.

See [references/positive.md](references/positive.md) for what good writing does (not just what to avoid).

## Step 3: Score

Rate 1-10 on each dimension, adjusted for register:

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds human, not generated? |
| Density | Anything cuttable? |
| Specificity | Claims backed by evidence? |

Below 42/60: revise.

**Register adjustments** (see [references/registers.md](references/registers.md)):
- `academic`: Do not penalize precise hedging or longer qualified sentences
- `technical`: Consistent structure in reference docs is not a rhythm flaw
- `narrative`: Indirection and dramatic rhythm variation are valid techniques

## Quick checks

Before delivering prose:

- Three consecutive sentences match length? Break one.
- Paragraph ends with punchy one-liner? Vary it.
- Em-dash before a reveal? Remove it.
- Explaining a metaphor? Trust it to land.
- "Serves as," "stands as," "represents"? Rewrite with "is."
- -ing clause at end of sentence adding no information? Delete it.
- Three-item list? Try two items or one.
- Different words for the same thing in adjacent sentences? Pick one term and reuse it.

## Reference files

| File | Purpose |
|------|---------|
| [phrases.md](references/phrases.md) | Words and phrases to cut or replace |
| [structures.md](references/structures.md) | Structural patterns to avoid |
| [positive.md](references/positive.md) | What good writing does |
| [registers.md](references/registers.md) | Per-register rules and tolerances |
| [examples.md](references/examples.md) | Before/after transformations (all registers) |

## License

MIT
