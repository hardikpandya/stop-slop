---
name: stop-slop
description: Edit or audit prose for formulaic AI-writing residue while preserving the author's meaning, evidence, genre, and voice. Use for drafting, rewriting, or reviewing text; do not use style cues to claim who wrote it.
metadata:
  trigger: Writing prose, editing drafts, reviewing content for formulaic AI patterns
  author: Hardik Pandya (https://hvpandya.com)
  version: 2.0.0
---

# Stop Slop

Remove formulaic writing without flattening the writer.

## Boundary

Style is not proof of authorship. Do not label a passage human- or AI-written from prose alone. Detection research shows high false-positive rates, model and domain drift, bias against non-native English writers, and sharp performance loss after editing or paraphrase.

Use this skill to improve prose. If the user asks for detection, report clustered signals and uncertainty, recommend provenance or revision history, and never present a style score as a verdict.

## Editing order

1. **Preserve the brief.** Identify the audience, genre, purpose, facts, citations, and any sample of the author's own voice. Do not convert technical, academic, legal, or personal prose into one generic house style.
2. **Fix content before cosmetics.** Remove unsupported claims, fabricated or unverifiable citations, repeated summaries, vague attribution, empty significance claims, and generic advice. Add concrete evidence, decisions, observations, or examples when the source supports them.
3. **Find clusters, not tokens.** Mark a pattern only when it repeats, crowds out substance, or combines with other signals. One transition, adverb, passive sentence, em dash, or three-item list proves nothing.
4. **Rewrite the cause.** Replace template scaffolding with the actual claim. Combine repetitive sections. Vary syntax where cadence has become mechanical. Replace stock wording only when it is generic in context.
5. **Protect voice.** Keep useful contractions, dialect, technical terms, deliberate repetition, humor, and genre-appropriate formality. Never add mistakes or random quirks to evade a detector.
6. **Verify the result.** Check meaning, factual support, citation integrity, rhythm, and genre fit. A cleaner paragraph that changes the claim is a failed edit.

## Signal strength

### Strong editing targets

- unsupported specifics, invented quotations, or citations that cannot be verified
- generic paragraphs that could describe any subject
- repeated introductions, conclusions, or sentence-level restatements
- vague attribution such as "experts say" when a source or actor should be named
- headings, lists, or bold labels that impose a template without helping navigation
- meta-commentary that announces the next point instead of making it

### Useful only as clusters

- stock vocabulary and inflated verbs
- negative parallelism such as "not X, but Y"
- repeated rule-of-three lists
- uniformly sized sentences or paragraphs
- excessive transitions, hedges, balanced caveats, or symmetrical conclusions
- a sudden shift from the author's established vocabulary, punctuation, or level of formality

### Weak signals; never ban them

- adverbs, passive voice, first-person pronouns, contractions, or direct address
- em dashes, semicolons, questions, Wh- sentence openings, or three-item lists
- polished grammar, long sentences, short sentences, or transition words in isolation

Read [references/patterns.md](references/patterns.md) when auditing a draft and [references/research.md](references/research.md) when explaining the evidence or detection limits. Use [references/examples.md](references/examples.md) for transformations.

## Output modes

### Rewrite

Return the revised prose. Explain material changes only when the user asks or when a factual or citation problem remains.

### Audit

For each material issue, quote the shortest identifying fragment, assign `strong`, `cluster`, or `weak`, explain the writing problem, and propose a fix. Do not count isolated words as violations.

### Authorship or detector review

Separate three questions:

- Does the prose contain formulaic patterns?
- Does it contain factual, citation, or provenance problems?
- Is there independent evidence about how it was produced?

Answer the first two from the text. The third requires metadata, drafts, revision history, watermarking, or another provenance source.

## Quality check

Score each dimension from 0 to 4. Revise any dimension below 3; do not combine the numbers into an "AI probability."

| Dimension | Check |
|---|---|
| Specificity | Are claims tied to concrete facts, actors, examples, or decisions? |
| Evidence | Can the reader verify quotations, citations, numbers, and attributions? |
| Voice fidelity | Does the edit preserve the writer's vocabulary and stance? |
| Structure | Does each section advance the argument instead of filling a template? |
| Cadence | Does syntax fit the material without mechanical repetition? |
| Economy | Can filler or duplicated meaning be removed? |
| Genre fit | Would this phrasing belong in this document and for this audience? |

## Non-negotiable checks

- Preserve the writer's meaning and factual uncertainty.
- Verify citations or flag them; never repair a citation by guessing.
- Do not increase lexical complexity to look human.
- Do not penalize non-native English, accessibility-oriented plain language, or formal technical prose.
- Do not optimize against one commercial detector.

## License

MIT
