# Stop Slop

A bilingual skill for removing predictable AI tells from English and French prose.

<img width="3840" height="2160" alt="Stop Slop" src="https://github.com/user-attachments/assets/902afc15-1f40-4a9d-af24-8cd67afb8ebf" />

## What this is

AI writing often repeats the same phrases, structures, and rhythms. Stop Slop helps Claude, Hermes Agent, and other agentskills-compatible assistants catch those patterns without flattening the writer's voice.

The rules are editing signals, not an AI detector. One em dash, adverb, passive sentence, or common transition proves nothing. Context and repetition matter.

## Languages

- English
- French
- Mixed-language drafts and translations

The French catalogue is a native adaptation. It includes French rhetorical habits, administrative phrasing, school-like transitions, and English-to-French calques rather than translating the English list word for word.

## Skill structure

```text
stop-slop/
├── SKILL.md
├── references/
│   ├── phrases.md          # Original compact English phrase list
│   ├── structures.md       # Original compact English structure list
│   ├── patterns-en.md      # Extended contextual English catalogue
│   ├── patterns-fr.md      # French-native catalogue
│   └── examples.md         # Bilingual before/after examples
├── README.md
└── LICENSE
```

The main file stays compact enough for routine use. Language-specific catalogues load only when needed.

## Installation

### Hermes Agent

Install directly from GitHub:

```bash
hermes skills install https://raw.githubusercontent.com/hardikpandya/stop-slop/main/SKILL.md
```

Then load it in a Hermes session:

```text
/stop-slop rewrite this launch post in French
```

You can also invoke it from the CLI:

```bash
hermes -s stop-slop chat -q "Audit draft.md for AI-writing patterns"
```

Hermes stores installed skills under `~/.hermes/skills/`. Run `hermes skills list` to verify installation. In a running session, use `/reload-skills` after a manual local install.

Hermes Agent documentation: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills

### Claude Code

Add this folder as a skill, or place it in the skills directory used by your Claude Code setup.

### Claude Projects

Upload `SKILL.md` and the `references/` files to project knowledge.

### Other agents

The skill follows the `SKILL.md` format used by agentskills-compatible tools. You can also include the main file in a system prompt and make the reference files available on demand.

## Usage

Natural-language requests are enough:

- "Rewrite this without AI tells."
- "Audite ce texte sans le réécrire."
- "Humanise ce post en gardant mon ton."
- "Translate this into native French without English AI calques."
- "Edit `draft.md` in place and verify the result."

The skill supports five modes:

- `draft`: write new prose and run a silent anti-slop check;
- `rewrite`: return a revised version;
- `audit`: flag exact passages without rewriting the full text;
- `edit`: modify a named file and verify it afterward;
- `original-strict`: retain the original skill's zero-tolerance rules when explicitly requested.

## What it catches

- throat-clearing and generic scene-setting;
- mechanical "not X, but Y" contrasts;
- staged reveals and engagement bait;
- vague authority and inflated significance;
- business jargon and abstract promotional language;
- stacked hedges, transitions, and intensifiers;
- metronomic paragraphs, forced triads, and synonym cycling;
- chatbot residue, reasoning leaks, placeholders, and internal citation tokens;
- French administrative phrasing and English-to-French calques.

## What it protects

- facts, numbers, links, citations, qualifications, and technical terms;
- deliberate voice, slang, dialect, and medium-specific conventions;
- useful passive voice and uncertainty;
- quotations, legal wording, code, and attributed material;
- the boundary between adding specificity and fabricating details.

## License

MIT. Use freely and share widely.

## Author

Created by [Hardik Pandya](https://hvpandya.com), with bilingual and Hermes Agent support contributed by the community.
