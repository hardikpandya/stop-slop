# Changelog

## 2026-08-21

### Changed

**Em-dash removal is now role-aware (SKILL.md, references/structures.md)**
- The checklist item and the structures table pointed at "remove it, use commas or periods". Replacing a clause-joining em-dash with a comma produces a comma splice, and it lands disproportionately on prominent sentences because that is where dashes get used for emphasis.
- New "Removing Em-Dashes" section documents the three roles and their correct replacements: parenthetical to comma or parens, clause-join to period or semicolon, table-cell or list placeholder to hyphen.
- Notes that only U+2014 is the AI tell. U+2013 (en-dash) belongs in numeric and date ranges and should be preserved, so a sweep should target the em-dash character specifically.
- Adds the reminder that a bulk sweep needs a second read-through, since a mechanical pass cannot distinguish the three roles.

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
