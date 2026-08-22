# Research Basis

This reference summarizes ten influential or widely used sources. It is not a ranking of universal detectors. Results depend on model, year, domain, language, text length, prompting, and post-editing.

## Ten sources and what they found

1. **Gehrmann, Strobelt, and Rush, “GLTR: Statistical Detection and Visualization of Generated Text” (ACL 2019).** GLTR exposed token-probability artifacts so people could see unusually predictable word choices. Its interface raised human detection in the reported study from 54% to 72%. This supports examining predictability and repetition with tool assistance, not judging from a blacklist. [Source](https://aclanthology.org/P19-3019/)

2. **Ippolito et al., “Automatic Detection of Generated Text is Easiest when Humans are Fooled” (ACL 2020).** Humans and classifiers relied on different cues. Decoding tuned for fluent text fooled people more often while leaving statistical abnormalities that machines could detect. Longer excerpts helped both, but expert raters were still fooled more than 30% of the time on multi-sentence samples. [Source](https://aclanthology.org/2020.acl-main.164/)

3. **Mitchell et al., “DetectGPT” (ICML 2023).** DetectGPT used curvature in the source model's probability function rather than visible punctuation or phrase rules. It reported 0.95 AUROC on one GPT-NeoX fake-news setting versus 0.81 for the strongest zero-shot baseline. The method assumes access to a suitable model and does not create a universal prose test. [Source](https://proceedings.mlr.press/v202/mitchell23a.html)

4. **Sadasivan et al., “Can AI-Generated Text be Reliably Detected?” (2023/2024 revision).** The paper showed that paraphrasing attacks defeat neural, zero-shot, watermark, and retrieval-based approaches under studied conditions. It also demonstrated spoofing attacks that can make human text look machine-generated. Detection scores are brittle after ordinary editing. [Source](https://arxiv.org/abs/2303.11156)

5. **Liang et al., “GPT detectors are biased against non-native English writers” (Patterns 2023).** Seven detectors mislabeled 61.3% of 91 human-written TOEFL essays on average. Richer vocabulary reduced the false-positive rate to 11.6%, showing that low perplexity and limited lexical variety can punish non-native writers. Never make prose more ornate merely to appear human. [Source](https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7)

6. **Jakesch et al., “Human heuristics for AI-generated language are flawed” (PNAS 2023).** Across six experiments with 4,600 participants, people could not reliably identify AI-written self-presentations. They treated first-person pronouns, contractions, and family topics as human signals, and models could exploit those assumptions. Personal language is not provenance. [Source](https://pubmed.ncbi.nlm.nih.gov/36881628/)

7. **Weber-Wulff et al., “Testing of detection tools for AI-generated text” (International Journal for Educational Integrity 2023).** The study tested 14 tools and found none reliably accurate; all scored below 80%, and obfuscation made results worse. False positives and false negatives make detector output unsuitable as a sole verdict. [Source](https://link.springer.com/article/10.1007/s40979-023-00146-z)

8. **OpenAI, “New AI classifier for indicating AI-written text” (retired 2023).** OpenAI reported 26% true positives and 9% false positives on its challenge set, then removed the classifier because of low accuracy. Even a model provider could not turn surface style into dependable authorship evidence. [Source](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/)

9. **Guo et al., “How Close is ChatGPT to Human Experts?” / HC3 (2023).** In the studied corpus, ChatGPT answers were longer but used a smaller vocabulary than human answers. English ChatGPT answers used more nouns, verbs, determiners, adjectives, auxiliaries, conjunctions, and particles, and fewer adverbs and punctuation marks. These are corpus-level tendencies from an early ChatGPT version, not bans for individual sentences. [Source](https://arxiv.org/abs/2301.07597)

10. **Wikipedia, “Signs of AI writing” (living community guide).** Editors document practical clusters such as stock vocabulary, negative parallelism, repeated section summaries, rule-of-three lists, canned headings, markup residue, and fictitious citations. The guide warns that the signs are potential clues, not the underlying problem, and that isolated transitions or em dashes are weak evidence. [Source](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

## What this changes in Stop Slop

### Retain

- remove empty throat-clearing and meta narration
- replace vague importance claims with specifics
- break repeated binary contrasts, summary loops, and mechanical cadence
- review clustered stock words and inflated business language
- protect citation and factual integrity

### Replace

- replace word bans with cluster-based review
- replace “sounds human” scoring with voice fidelity and genre fit
- replace forced active voice with clear responsibility
- replace arbitrary rhythm variation with meaning-driven cadence

### Reject

- banning all adverbs, passive voice, em dashes, Wh- openings, or three-item lists
- forcing first person, contractions, direct address, anecdotes, or mistakes to look human
- treating detector scores or prose cues as proof of authorship
- increasing vocabulary complexity to raise perplexity

## Practical conclusion

The reliable editing question is not “Can I hide the AI?” It is “Does this draft make supported, specific claims in the writer's voice?” Provenance answers authorship; editing improves the article.
