# Stop Slop

A skill for removing AI tells from prose.

<img width="3840" height="2160" alt="G-Yg4RVbIAAhVxW" src="https://github.com/user-attachments/assets/902afc15-1f40-4a9d-af24-8cd67afb8ebf" />

## What this is

AI writing has patterns. Predictable phrases, structures, rhythms. This skill teaches Claude (or any LLM) to catch and remove them.

## Skill Structure

```
stop-slop/
├── skills/
│   └── stop-slop/
│       ├── SKILL.md          # Core instructions
│       └── references/
│           ├── phrases.md    # Phrases to remove
│           ├── structures.md # Structural patterns to avoid
│           └── examples.md   # Before/after transformations
├── README.md
└── LICENSE
```

`skills/stop-slop/` is the [Agent Skills](https://agentskills.io/specification) convention. Installers look there.

## Quick start

**Claude Code, one command:**

```bash
gh skill install hardikpandya/stop-slop stop-slop --agent claude-code --scope user
```

`--scope user` puts it in `~/.claude/skills/`, available in every project. Drop it to install into the current repo only. Other agents work the same way: `--agent cursor`, `--agent codex`, `--agent gemini-cli`, and [more](https://cli.github.com/manual/gh_skill_install). Upgrade later with `gh skill update`.

**Claude Code, by hand:** clone the repo anywhere and symlink the skill folder, which keeps `git pull` working as the upgrade path.

```bash
git clone https://github.com/hardikpandya/stop-slop.git ~/src/stop-slop
ln -s ~/src/stop-slop/skills/stop-slop ~/.claude/skills/stop-slop
```

**Claude Projects:** Upload `SKILL.md` and reference files to project knowledge.

**Custom instructions:** Copy core rules from `SKILL.md`.

**API calls:** Include `SKILL.md` in your system prompt. Reference files load on demand.

## What it catches

**Banned phrases** - Throat-clearing openers, emphasis crutches, business jargon, all adverbs, vague declaratives, meta-commentary. See `skills/stop-slop/references/phrases.md`.

**Structural clichés** - Binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency, narrator-from-a-distance voice, passive voice. See `skills/stop-slop/references/structures.md`.

**Sentence-level rules** - No Wh- sentence starters, no em dashes, no staccato fragmentation, no lazy extremes, active voice required.

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

## Author

[Hardik Pandya](https://hvpandya.com)

## License

MIT. Use freely, share widely.
