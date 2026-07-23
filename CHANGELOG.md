# Changelog

## 2026-07-23

### Added

**Core rules (SKILL.md)**
- Zero em dashes promoted to its own absolute Core Rule, separated from the "vary rhythm" rule it was previously bundled into. Covers headings, captions, and table cells explicitly, not just body prose.
- "Fix the pattern, not the punctuation": removing an em dash from a binary-contrast sentence but leaving the negate-then-assert clause shape intact (e.g. swapping "not X — it's Y" for "not X. It's Y.") still leaves the tell in place. The sentence needs a full rewrite.
- Trailing "not just X" / "not simply X" / "not only X" qualifiers called out as the same binary-contrast pattern as "not X, it's Y," just reordered so the negation comes second. Affirmation-first doesn't exempt it.

**Structures (references/structures.md)**
- New "Em Dashes: Zero, Not Fewer" section, replacing the single row previously buried in the Rhythm Patterns table. States the zero-tolerance rule explicitly and heads off substituting an en dash as a workaround.
- New "Punctuation Swaps Are Not Fixes" section with a worked example showing that re-punctuating a contrast sentence without rewriting it preserves the AI tell.
- New "The Soft Form Counts Too" subsection under Binary Contrasts, extending the existing (but easy to miss) "not just X but also Y" row to its trailing, sentence-final form.

**Examples (references/examples.md)**
- New Example 6: a "wrong fix" step showing a plausible-looking but incorrect edit (em dash removed, contrast structure kept) next to the actual fix.
- New Example 7: trailing "not just" qualifier removed from a sentence that already stated its point.

Rationale: these rules already existed in the reference files in weaker or more buried forms, and testing the skill against a long real-world document surfaced that they were easy to satisfy technically (dash removed) while leaving the actual AI tell (the rhetorical contrast shape) untouched.

## 2026-01-13

### Added

**Phrases (references/phrases.md)**
- Throat-clearing: "Here's what I find interesting", "Here's the problem though"
- Performative emphasis: "creeps in", "I promise", "They exist, I promise"
- Telling instead of showing: "This is genuinely hard", "This is what leadership actually looks like"

**Structures (references/structures.md)**
- Binary contrasts: "Not X. But Y.", "It's not this. It's that.", "stops being X and starts being Y"
- Rhythm patterns: staccato fragmentation, dashes for dramatic pause, hedging as reassurance
- Word patterns: absolute words (always, never, everyone, etc.), AI-overused intensifiers (deeply, truly, fundamentally, inherently, simply, literally, inevitably)

## 2026-01-12

- Restructured skill following Claude Code best practices (PR #1)
- Split into SKILL.md and references/ folder

## 2025-01-12

- Initial release
