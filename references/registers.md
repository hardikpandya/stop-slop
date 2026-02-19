# Register-Specific Rules

Different writing contexts tolerate different patterns. Detect the register from context, then apply the right rules.

## Register Detection

Infer the register from the content and context:

| Signal | Register |
|--------|----------|
| Citations, methodology, "we hypothesize" | `academic` |
| API docs, READMEs, changelogs, error messages | `technical` |
| Fiction, essays, memoir, creative nonfiction | `narrative` |
| Blog posts, social media, emails, LinkedIn | `casual` |
| Reports, proposals, business comms | `professional` |

If the user specifies a register, use it. Otherwise, infer from content.

---

## Academic

**Principle**: Precision over brevity. Claims require evidence.

### Acceptable in academic writing

- Hedging qualifiers: "may", "suggests", "appears to", "it is possible that" — these are epistemic precision, not weakness
- Passive voice when agent is unknown: "The temple was constructed in the 3rd century BCE"
- Longer sentences when subordinate clauses add necessary qualification
- Citation stacking: "(Gordon 1966; Astour 1967; Harrison 1912)" is not slop
- Field-specific terminology used precisely

### Flag in academic writing

- **Significance inflation without evidence**: "marking a pivotal moment" — pivotal according to whom?
- **Vague attribution**: "scholars have long debated" — which scholars? Name them.
- **-ing padding**: "highlighting the importance of this finding" — just state the finding
- **Promotional adjectives**: "groundbreaking study" — let the reader judge
- **Empty hedging**: "further research is needed" as a conclusion — this is true of everything
- **"The literature"** without specific citations — which literature?
- **Synonym cycling**: switching between "study", "research", "investigation", "inquiry" for the same thing

### Scoring adjustments

- Density: do not penalize longer sentences that carry necessary qualification
- Directness: hedging that reflects genuine epistemic uncertainty is direct, not evasive
- Trust: citing sources IS trusting the reader to evaluate evidence

---

## Technical

**Principle**: Clarity and accuracy. Say what it does, not what it means.

### Acceptable in technical writing

- Bullet points and numbered lists for steps, options, parameters
- Headers and subheaders for navigation
- Code blocks and examples
- Domain jargon when used precisely ("idempotent", "backpressure", "memoization")
- Imperative voice: "Run the migration", "Set the environment variable"

### Flag in technical writing

- **Promotional adjectives**: "robust", "seamless", "cutting-edge", "blazing fast", "elegant" — give benchmarks or remove
- **Vague claims**: "significantly faster" — how much faster? Benchmark it.
- **Chatbot artifacts**: "I hope this helps!", "Let me know if you have questions"
- **Explanation padding**: "It's worth noting that..." — just note it
- **Buzzword stacking**: "leveraging our cloud-native, AI-powered, enterprise-grade platform"
- **Emoji-decorated headings**: remove
- **Inline-header vertical lists** when prose would work better

### Scoring adjustments

- Rhythm: consistent structure is a feature in reference docs, not a flaw
- Density: technical docs should be scannable; some redundancy aids comprehension
- Authenticity: measured, impersonal tone is appropriate

---

## Narrative

**Principle**: Voice, rhythm, and imagery. Technique serves story.

### Acceptable in narrative writing

- Em dashes for parenthetical asides, interruption, tonal shifts
- Sentence fragments for deliberate effect (not as default compression)
- Metaphor and imagery without explanation
- Varying sentence length dramatically — short punches followed by long flowing passages
- First person, strong opinions, emotional register
- Repetition for rhetorical effect (distinct from synonym cycling)

### Flag in narrative writing

- **Synonym cycling**: "The protagonist... The main character... The central figure..." — pick one and use it
- **Rule of three**: forcing every list into three items
- **AI vocabulary clusters**: delve, tapestry, multifaceted, nuanced, intricate, interplay
- **Generic conclusions**: "the future looks bright", "exciting times lie ahead"
- **Dramatic fragmentation when unearned**: "Hope. That's it. That's the word." — earn the emphasis
- **Physical tell cliches**: "jaw tightened", "breath caught", "something shifted behind his eyes"
- **Explaining metaphors**: if you need to explain it, rewrite it
- **False profundity**: "And maybe that was enough." as a paragraph closer

### Scoring adjustments

- Rhythm: variation is the goal, not consistency
- Authenticity: voice and personality matter more than neutrality
- Directness: indirection is a valid narrative technique

---

## Casual

**Principle**: All stop-slop rules apply at full force.

Current `phrases.md` and `structures.md` rules are calibrated for this register. Shortest path from thought to reader. No throat-clearing, no filler, no jargon.

### Additional casual flags

- Exclamation mark overuse (more than 1 per paragraph)
- Emoji in professional-adjacent contexts
- "Actually" and "literally" as filler intensifiers
- Starting sentences with "So," or "Look,"

---

## Professional

**Principle**: Clear and direct. Respect the reader's time.

Similar to casual but tolerates slightly more structure:

### Acceptable in professional writing

- Bullet points for action items, decisions, or options
- Formal salutations and closings in emails
- Measured hedging: "We recommend X, though Y may also work"
- Executive summary format

### Flag in professional writing

- **Business jargon**: "synergy", "leverage", "circle back", "double down", "move the needle"
- **Throat-clearing**: "I wanted to reach out to share that..." — just share it
- **Filler adverbs**: "basically", "essentially", "fundamentally"
- **Vague commitments**: "We'll look into this" — when? What specifically?
- **Meeting-speak**: "Let's take this offline", "parking lot this"
