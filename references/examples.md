# Before/After Examples

## Example 1: Throat-Clearing + Binary Contrast

**Before:**
> "Here's the thing: building products is hard. Not because the technology is complex. Because people are complex. Let that sink in."

**After:**
> "Building products is hard. Technology is manageable. People aren't."

**Changes:** Removed opener, binary contrast structure, and emphasis crutch. Direct statements.

---

## Example 2: Filler + Unnecessary Reassurance

**Before:**
> "It turns out that most teams struggle with alignment. The uncomfortable truth is that nobody wants to admit they're confused. And that's okay."

**After:**
> "Teams struggle with alignment. Nobody admits confusion."

**Changes:** Cut hedging ("most"), removed throat-clearing phrases, deleted permission-granting ending.

---

## Example 3: Business Jargon Stack

**Before:**
> "In today's fast-paced landscape, we need to lean into discomfort and navigate uncertainty with clarity. This matters because your competition isn't waiting."

**After:**
> "Move faster. Your competition is."

**Changes:** Eliminated jargon entirely. Core message in six words.

---

## Example 4: Dramatic Fragmentation

**Before:**
> "Speed. Quality. Cost. You can only pick two. That's it. That's the tradeoff."

**After:**
> "Speed, quality, cost—pick two."

**Changes:** Single sentence. No performative emphasis.

---

## Example 5: Rhetorical Setup

**Before:**
> "What if I told you that the best teams don't optimize for productivity? Here's what I mean: they optimize for learning. Think about it."

**After:**
> "The best teams optimize for learning, not productivity."

**Changes:** Direct claim. No rhetorical scaffolding.

---

# Register-Specific Examples

## Academic

### Example 6: Significance Inflation + Vague Attribution

**Register:** `academic`

**Before:**
> "Scholars have long debated the relationship between Minoan and Semitic cultures, a multifaceted topic that underscores the importance of cross-cultural analysis. It is well-established that trade networks facilitated linguistic exchange, fostering a vibrant tapestry of shared cultural elements. This pivotal finding has profound implications for our understanding of Bronze Age connectivity."

**After:**
> "Gordon (1966) and Astour (1967) proposed cognate links between Linear A sequences and West Semitic lexemes. Trade networks between Crete and the Levant are attested by LM I pottery at Ugarit and Canaanite amphora handles at Kommos. These finds suggest regular contact, though the degree of linguistic exchange remains unresolved."

**Changes:** Named specific scholars. Replaced "well-established" with cited evidence. Cut "multifaceted," "tapestry," "pivotal," "profound"—all AI vocabulary. Replaced "fostering" -ing clause with concrete archaeological evidence.

---

### Example 7: Academic Hedging Done Right vs. Wrong

**Register:** `academic`

**Before (wrong hedging):**
> "It could potentially be argued that the evidence may suggest a possible connection between the Minoan and Phoenician writing systems, which could have implications for further research."

**After (precise hedging):**
> "The sign correspondence between Linear A *AB 04* and Proto-Sinaitic *bet* suggests a shared graphic ancestor, though the sample size (n=7 secure parallels) limits statistical confidence."

**Changes:** Hedging should express genuine epistemic uncertainty with specifics, not stack qualifiers. "Could potentially be argued that... may suggest a possible" is four layers of nothing. One precise hedge ("suggests... though") with a stated reason ("sample size") is stronger.

---

## Technical

### Example 8: Promotional Adjectives + Buzzwords

**Register:** `technical`

**Before:**
> "Our cutting-edge, robust authentication module leverages state-of-the-art JWT handling to deliver a seamless, enterprise-grade security experience. This groundbreaking approach enhances the overall security posture of your application."

**After:**
> "The auth module uses RS256-signed JWTs with automatic key rotation every 24 hours. Tokens expire after 15 minutes. Refresh tokens are stored in HttpOnly cookies with SameSite=Strict."

**Changes:** Removed every promotional adjective. Replaced "leverages" with "uses." Replaced vague claims with specific configuration. "Cutting-edge," "robust," "seamless," "enterprise-grade," "groundbreaking"—none of these tell you what the code does.

---

### Example 9: Format Slop — Inline-Header Vertical List

**Register:** `technical`

**Before:**
> **Key Features:**
> - **Blazing Fast Performance:** Our module processes requests with minimal latency
> - **Effortless Integration:** Simply drop in the middleware and you're good to go
> - **Rock-Solid Reliability:** Built to handle millions of requests without breaking a sweat

**After:**
> The middleware processes requests in under 2ms at p99 (benchmarked on a 4-core VM with 1,000 concurrent connections). Add it to your Express pipeline with `app.use(authMiddleware())`. No configuration required for default settings.

**Changes:** Replaced inline-header vertical list with prose. Removed promotional adjectives ("blazing fast," "effortless," "rock-solid"). Added a benchmark instead of asserting performance. Described integration concretely instead of vaguely.

---

### Example 10: -ing Clauses in Technical Docs

**Register:** `technical`

**Before:**
> "The database migration adds a composite index on (user_id, created_at), ensuring reliability and enhancing query performance while showcasing the team's commitment to scalability."

**After:**
> "The migration adds a composite index on (user_id, created_at). The `GET /users/:id/events` query drops from 340ms to 12ms on a table with 2M rows."

**Changes:** Cut all three -ing clauses. They claimed outcomes without evidence. The after version gives the benchmark.

---

## Narrative

### Example 11: Synonym Cycling + Rule of Three

**Register:** `narrative`

**Before:**
> "The archaeologist descended into the chamber. The researcher paused at the threshold. The scholar steadied herself against the wall. The academic took a breath. Innovation, curiosity, and determination drove her forward."

**After:**
> "She descended into the chamber, paused at the threshold, and steadied herself against the wall. She took a breath and kept moving."

**Changes:** "Archaeologist," "researcher," "scholar," "academic"—four names for one person. Pick one and reuse it (or use a pronoun). Cut the rule-of-three abstract nouns. People don't think in triads of virtues; they just act.

---

### Example 12: Generic Positive Conclusion

**Register:** `narrative`

**Before:**
> "As the sun set over the ancient ruins, she realized that the journey had changed her in ways she couldn't fully articulate. The future looked bright, full of endless possibilities. And maybe that was enough."

**After:**
> "She sat on the broken wall and watched the sun go down. She didn't know what she'd found. She wasn't sure she wanted to."

**Changes:** Cut "the future looked bright" and "endless possibilities"—generic positive closers. Cut "maybe that was enough"—false profundity. The rewrite lets ambiguity exist without announcing it.

---

## Professional

### Example 13: Business Jargon + Throat-Clearing

**Register:** `professional`

**Before:**
> "I wanted to circle back and take a step back to unpack the current landscape. Moving forward, we need to lean into the challenges and double down on our commitment to synergy across cross-functional teams."

**After:**
> "Three problems from last quarter's review are still open. I'll send specifics by Thursday with a proposed owner for each."

**Changes:** Seven jargon phrases in two sentences, zero information. The rewrite says what's happening, when, and who's responsible.

---

### Example 14: Chatbot Artifacts in Professional Writing

**Register:** `professional`

**Before:**
> "Great question! I'd be happy to help with that. Here is an overview of the quarterly results. It's worth noting that revenue increased significantly. I hope this helps! Let me know if you have any questions."

**After:**
> "Q4 revenue was $2.3M, up 18% from Q3. Full breakdown attached."

**Changes:** Stripped five chatbot artifacts. Replaced "significantly" with a number. Professional writing respects the reader's time.
