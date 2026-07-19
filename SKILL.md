---
name: stop-slop
description: "Use when drafting, editing, reviewing, or translating French or English prose that must sound direct, specific, and human. Detects and removes AI-slop phrases, formulaic syntax, empty rhetoric, chatbot leaks, mechanical rhythm, and French-specific calques while preserving meaning, facts, register, and the writer's voice. Supports audit-only, rewrite, file-edit, and pre-delivery self-check modes."
license: MIT
compatibility: "Claude Code, Hermes Agent, and agentskills-compatible assistants"
metadata:
  author: "Hardik Pandya and contributors"
  version: "1.0.0"
  languages: "English, French"
  homepage: "https://github.com/hardikpandya/stop-slop"
---

# Stop Slop: French and English

## Overview

Remove predictable AI-writing habits without flattening the author's voice. Work in French, English, or mixed-language drafts. Preserve facts, intent, technical terms, quotations, citations, dialect, and deliberate stylistic choices.

Treat every pattern as an editing signal, not proof that AI wrote the text. Density and context matter more than one isolated phrase. Do not introduce fake anecdotes, opinions, numbers, sources, or personal experience to make prose sound human.

This version adds bilingual rules, French-native patterns, context controls, verification, and safeguards against over-editing while preserving the original skill's directness.

## When to use

Load this skill when the user asks to:

- draft publication-ready prose in French or English;
- "humanize", "de-slop", "remove AI tells", "rendre plus naturel" or "enlever le style IA";
- review a post, article, email, landing page, memo, documentation, or social post;
- translate without importing English AI syntax into French;
- edit a named text file in place;
- run a final anti-slop pass before delivering important prose.

Do not use it to judge authorship or accuse a person of using AI. Do not rewrite quoted material, legal wording, code, API names, or terminology merely because it matches a flagged word.

## Modes

Infer the mode from the request:

- `rewrite` (default): audit internally, then return the revised text.
- `audit`: list exact passages, pattern categories, severity, and suggested fixes. Do not rewrite the full text.
- `edit`: modify the named file with targeted edits, re-read it, and report changed spans.
- `draft`: write new prose, then silently run the final check before returning it.
- `original-strict`: preserve the original skill's zero-tolerance policy. Remove all adverbs, passive constructions, Wh-openers, em dashes, triads, and other listed patterns. Use only when the user explicitly asks for the original or strict behavior.

For short requests, return the result first. Do not force a long audit report unless the user asks for one.

## Editing process

1. Identify the language and register: casual, social, professional, editorial, technical, academic, legal, or marketing. Completion: the rewrite uses conventions appropriate to that register.
2. Preserve the payload: extract every fact, claim, number, proper noun, link, citation, qualification, and requested call to action. Completion: none disappears or changes meaning without explicit notice.
3. Scan phrases and structures. Use the original compact [phrase list](references/phrases.md) and [structure list](references/structures.md) for a quick English pass. Load the extended [English catalogue](references/patterns-en.md) for a full English review and the [French catalogue](references/patterns-fr.md) for French. For mixed text or translation, load both extended catalogues. Use the [worked examples](references/examples.md) when the distinction between useful style and empty pattern is unclear. Completion: every strong or clustered signal has been considered in context.
4. Rewrite the smallest useful unit. Cut filler, state the actor and action when known, replace abstractions with specifics already present, and vary rhythm naturally. Completion: the text advances with each sentence and retains the author's register.
5. Read once for voice, not rules. Restore any deliberate phrase that is the clearest choice. Completion: the prose sounds spoken or written by one consistent person, not processed by a checklist.
6. Run the final check below. Completion: no P0 leaks remain, no repeated P1 pattern dominates, and facts match the source.

## Priority

### P0: publishing defects

Always fix unless the text quotes them intentionally:

- chatbot residue: "I hope this helps", "N'hésitez pas si...", "Great question", "Voici une version...";
- reasoning scaffolding: "Let me think step by step", "Analysons cela étape par étape";
- model disclaimers or unsupported gap-filling;
- unfilled placeholders;
- internal citation tokens and AI-tool tracking parameters;
- invented facts, citations, testimony, quotations, or first-person experience.

### P1: strong slop signals

Fix repeated or obvious instances:

- throat-clearing and generic context openings;
- negative pivot templates such as "not X, but Y" and "il ne s'agit pas de X, mais de Y";
- staged reveals, infomercial hooks, fake profundity, and slogan-like kickers;
- vague authority, significance inflation, promotional abstractions;
- symmetrical triads, metronomic paragraphs, synonym cycling;
- stacked transitions, hedges, intensifiers, or business jargon;
- excessive em dashes, bold labels, emoji decoration, and needless headings.

### P2: context-dependent polish

Change only when density hurts the piece:

- passive voice when the actor is known and relevant;
- adverbs that add no precision;
- rhetorical questions answered immediately;
- first-person or second-person phrasing inappropriate to the register;
- ordinary transitions repeated too often.

## Core rules

### Cut announcements, keep content

Delete sentences that announce importance, honesty, structure, or emotion instead of carrying information. Replace "Here's why this matters" with the reason itself. Replace "Il est important de souligner que" with the claim.

### Prefer named actors and concrete consequences

When the source identifies who acted, put that actor near the verb. Do not invent an actor when the source does not provide one. Passive voice is valid when the actor is unknown, irrelevant, deliberately withheld, or when the object is the topic.

### Break template syntax

Directly state the positive claim when a negation pivot only manufactures contrast. Keep contrast when both sides are factual and necessary. Vary list size and sentence shape; do not mechanically turn every three-item list into two items.

### Preserve useful words

Do not ban every adverb, `-ly` word, French `-ment` word, Wh-question, copula, metaphor, or em dash on sight. Remove empty or repeated uses. Keep the word when it adds scope, manner, timing, precision, or the writer's recognizable voice.

Always keep common technical words used in their exact sense. In `original-strict` mode, apply the original absolute rules instead of these contextual exceptions.

### Add specificity without fabrication

Use names, dates, numbers, examples, and mechanisms already present or verified. If the draft says only "the implications are significant", ask for the missing implication or keep a cautious edit. Never manufacture a concrete detail.

### Match the medium

- Social: allow fragments, hooks, slang, and occasional emoji when they fit the author's established voice. Cut generic engagement bait.
- Technical/docs: keep precise repetition, passive constructions, lists, headings, and terms when they improve reference use.
- Academic/legal: preserve qualifications and conventional transitions that carry logical or legal meaning.
- Sales: persuasion is allowed. Replace unsupported superlatives with evidence or specific benefits.
- Casual messages: do not over-polish grammar or erase idiosyncrasies.

## Final check

Before delivery, verify:

- [ ] Facts, numbers, names, links, caveats, and intent match the source.
- [ ] No P0 artifact remains outside quotations or examples.
- [ ] The opening reaches the subject without generic scene-setting.
- [ ] No repeated negation-pivot, reveal, triad, or transition template controls the rhythm.
- [ ] Abstract praise has evidence, a concrete consequence, or has been cut.
- [ ] Sentence and paragraph lengths vary without forced fragmentation.
- [ ] French reads as native French; English syntax has not been translated word for word.
- [ ] The conclusion adds a decision, consequence, prediction with criteria, or stops cleanly.
- [ ] No fabricated specificity or personal experience was introduced.
- [ ] The rewrite still sounds like the same author.

## Output

For `rewrite` or `draft`, give the final text first. Add a short change note only when useful.

For `audit`, group findings by P0, P1, and P2. Quote exact spans and distinguish clear defects from judgment calls.

For `edit`, make targeted file changes, re-read the result, then report file locations and verification. Do not claim success until the edited file has been read back.

## Attribution

Created by Hardik Pandya and released under the MIT License. Additional categories were cross-checked against Wikipedia's "Signs of AI writing" guide maintained by WikiProject AI Cleanup and the public `blader/humanizer` project derived from it. The French catalogue is an original native-language adaptation, not a literal translation of the English list.
