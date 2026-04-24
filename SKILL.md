---
name: stop-slop
description: Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells.
version: 0.1.0
creator: Hardik Pandya (https://hvpandya.com)
license: MIT
metadata:
  trigger: Writing prose, editing drafts, reviewing content for AI patterns
  author: Hardik Pandya (https://hvpandya.com)
  effort: medium
---

# Stop Slop

Eliminate predictable AI writing patterns from prose.

## When to Use

- Drafting any prose destined for a human reader (essays, blog posts, docs, release notes).
- Editing a draft that feels AI-generated — hedged, metronomic, or padded with throat-clearing.
- Reviewing someone else's copy for the tells listed in `references/phrases.md` and `references/structures.md`.

Skip for: code, code comments, structured data, or transcripts where voice is preserved verbatim.

## Prerequisites

None. This skill edits prose only — it runs no shell commands, modifies no files on disk, and needs no tools beyond a text editor. The verbs "Cut", "Kill", "Remove", and "Delete" in the rules below refer to words and sentences in the draft, not to filesystem operations.

### Safety

This skill only edits prose in a text buffer. It issues no shell commands, touches no filesystems, and needs no permissions.

- **Back up the draft before a pass.** Copy the original text into version control (or a "v1" file) so edits are reversible. The rules below ask you to cut and rewrite aggressively — a backup makes that safe.
- **Confirm before destructive rewrites.** When a rule would remove a full paragraph or restructure a section, show the before/after to the author and get explicit confirmation (a dry-run) before applying it to the final draft.
- **On error / recovery.** If an edit changes meaning or loses the author's voice, revert that edit and keep the original line. Never rewrite a direct quote. When in doubt, prefer the author's phrasing over a more "efficient" one — the goal is to sound human, not to minimize word count.

## Instructions

1. Apply the eight Core Rules below to every paragraph, in order.
2. Run the Quick Checks on the full draft.
3. Score the result with the Scoring table; if it totals below 35/50, revise and re-score.
4. Stop when the draft reads like a person wrote it — further edits past that point risk over-polishing.

## Core Rules

1. **Cut filler phrases.** Remove throat-clearing openers, emphasis crutches, and all adverbs. See [references/phrases.md](references/phrases.md).

2. **Break formulaic structures.** Avoid binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency. See [references/structures.md](references/structures.md).

3. **Use active voice.** Every sentence needs a human subject doing something. No passive constructions. No inanimate objects performing human actions ("the complaint becomes a fix").

4. **Be specific.** No vague declaratives ("The reasons are structural"). Name the specific thing. No lazy extremes ("every," "always," "never") doing vague work.

5. **Put the reader in the room.** No narrator-from-a-distance voice. "You" beats "People." Specifics beat abstractions.

6. **Vary rhythm.** Mix sentence lengths. Two items beat three. End paragraphs differently. No em dashes.

7. **Trust readers.** State facts directly. Skip softening, justification, hand-holding.

8. **Cut quotables.** If it sounds like a pull-quote, rewrite it.

## Quick Checks

Before delivering prose:

- Any adverbs? Kill them.
- Any passive voice? Find the actor, make them the subject.
- Inanimate thing doing a human verb ("the decision emerges")? Name the person.
- Sentence starts with a Wh- word? Restructure it.
- Any "here's what/this/that" throat-clearing? Cut to the point.
- Any "not X, it's Y" contrasts? State Y directly.
- Three consecutive sentences match length? Break one.
- Paragraph ends with punchy one-liner? Vary it.
- Em-dash anywhere? Remove it.
- Vague declarative ("The implications are significant")? Name the specific implication.
- Narrator-from-a-distance ("Nobody designed this")? Put the reader in the scene.
- Meta-joiners ("The rest of this essay...")? Delete. Let the essay move.

## Scoring

Rate 1-10 on each dimension:

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds human? |
| Density | Anything cuttable? |

Below 35/50: revise.

## Example

One before/after to set expectations. See [references/examples.md](references/examples.md) for more.

**Before:**

```
Here's the thing: building products is hard. Not because the
technology is complex. Because people are complex. Let that sink in.
```

**After:**

```
Building products is hard. Technology is manageable. People aren't.
```

Removed the opener, the binary contrast, and the emphasis crutch. Two direct statements, same meaning.

### Expected output

- Every adverb removed unless load-bearing.
- No em dashes; no passive constructions; no inanimate subjects performing human verbs.
- No "not X, it's Y" contrasts, rhetorical questions, or meta-joiners.
- Scoring table totals ≥ 35/50 across the five dimensions.

## Edge cases

- **Direct quotes** — leave them alone; quoting a hedging speaker verbatim is not slop.
- **Technical prose where precision > rhythm** — API reference sentences can be metronomic; don't force variation that loses accuracy.
- **Lists and tables** — structural repetition is the point; don't "vary rhythm" inside a parameter list.
- **First-person personal voice** — `you`/`I` is fine; don't strip writer presence in the name of directness.

## License

MIT
