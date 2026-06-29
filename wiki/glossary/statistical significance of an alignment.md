---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Math/Statistics/SignificanceTesting
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentSignificance
  - EXAM_PREP
foundational: 4
prereqs: 2
density: 2
value: 5
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# statistical significance of an alignment

You aligned two sequences A and B and got a score *S*. **Is that score meaningful — or could you get it by chance?** That is the question of statistical significance. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=3|L4 p.3]]

The problem is real because **any two sequences align to *some* score** — even random ones. A high *S* only implies [[homology]] if it is **far higher than what chance produces**. And *S* itself is **not absolute**: it depends on the [[scoring matrix]] and [[affine gap penalty|gap penalties]], so it has no meaning until compared against a **null model** ("the two sequences are *not* related").

**Two regimes, two tools:**

| | Method | How |
|---|---|---|
| **[[global vs local alignment\|Global]]** alignment | [[Z-score (alignment)\|Z-score]] | shuffle B many times, build a random-score distribution, measure how many SDs *S* sits above its mean |
| **[[global vs local alignment\|Local]]** alignment | [[E-value (Karlin-Altschul)\|E-value]] / [[Gumbel distribution and the p-value\|p-value]] | a closed-form (Karlin–Altschul) for the expected number of chance alignments scoring ≥ *S* |

The lecture notes the **local** case is the one with clean theory; the **global** case is handled empirically by shuffling.

> [!Caution] Statistical ≠ biological significance
> A statistically significant score says the similarity is *unlikely by chance* — it does **not** prove the sequences share a function or ancestry. You **always** need **biological** plausibility on top of the *p*-value.

# TLDR
Statistical significance asks whether an alignment score *S* is **better than chance** — because any two sequences align to *some* score, and *S* is matrix-dependent, not absolute. **Global** alignments are tested by **shuffling** (the [[Z-score (alignment)|Z-score]]); **local** alignments by the **Karlin–Altschul [[E-value (Karlin-Altschul)|E-value]]**. Statistical significance never replaces *biological* significance.

# Recitation Anchors
- Question: could score *S* arise **by chance**?
- Any two sequences align to **some** score → need a **null model**
- *S* is **not absolute** (depends on matrix + gaps)
- **Global → Z-score** (shuffling); **local → E-value** (Karlin–Altschul)
- Local case = clean theory; global = empirical
- **Statistical ≠ biological** significance (always need both)

> [!Cool] Cool fact
> Significance depends on **how big the database is**: the *same* alignment score becomes *less* significant the larger the search space, because more sequences mean more chances for a fluke. This is why a BLAST hit's **E-value rises as the database grows** even though the raw score is identical. [source](https://www.ncbi.nlm.nih.gov/BLAST/tutorial/Altschul-1.html)

# Read aloud
KP.0.Definition: The question.
You've aligned two sequences and gotten a score. The crucial question is: is that score actually meaningful, or could you have gotten it just by chance? That's what statistical significance is about.

KP.1.Concept: Why it's a real problem.
It matters because any two sequences, even completely random ones, will align to some score. So a high score only suggests the sequences are related if it's much higher than what chance alone would produce. And the score isn't an absolute number — it depends on which scoring matrix and gap penalties you chose. Until you compare it against a null model, where the two sequences are assumed unrelated, the score means nothing on its own.

KP.2.Concept: Two regimes, two tools.
There are two situations. For global alignment, you test significance empirically: you shuffle one sequence many times, align each shuffle, and see how far your real score stands above the random ones — that's the Z-score. For local alignment, there's a clean mathematical formula from Karlin and Altschul that gives the expected number of chance alignments scoring at least as high — that's the E-value. The local case is the one with beautiful theory; the global case is handled by shuffling.

KP.3.Connection: Statistical is not biological.
And a vital warning: statistical significance only tells you the similarity is unlikely by chance. It does not prove the two sequences share a function or a common ancestor. You always need biological plausibility on top of the statistics.

KP.4.CoolFact: Bigger database, weaker significance.
And here's the cool part — significance depends on how big your database is. The exact same alignment score becomes less significant the larger the search space, because more sequences give more chances for a coincidence. That's why a BLAST hit's E-value actually goes up as the database grows, even when the raw score hasn't changed at all.

# Question and Answer
Q. What does statistical significance of an alignment measure?
A. Whether the score *S* is higher than would be expected by chance under a null model where the sequences are unrelated.

Q. Why isn't a high raw score enough to claim homology?
A. Any two sequences align to some score, and *S* depends on the scoring matrix/gaps; only a score far above chance is meaningful.

Q. Which significance tool is used for global vs local alignments?
A. Global → Z-score (by shuffling); local → Karlin–Altschul E-value / p-value.

Q. Which regime has cleaner theory, global or local?
A. Local — it has a closed-form (Karlin–Altschul) distribution; global is handled empirically.

Q. How do statistical and biological significance differ?
A. Statistical = unlikely by chance; biological = actually shares function/ancestry. You need both.

Q. Why does the same score become less significant in a larger database?
A. More sequences mean more opportunities for a high-scoring fluke, so the expected number of chance hits (E-value) rises.
