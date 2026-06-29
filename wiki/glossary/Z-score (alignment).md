---
tags:
  - TYPE__/Concept/Procedure
  - PATH__/Math/Statistics/SignificanceTesting
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentSignificance
  - MATH_UNRAVELING
foundational: 3
prereqs: 3
density: 3
value: 4
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-29
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Z-score (alignment)

The **Z-score** measures the [[statistical significance of an alignment|significance]] of a **[[global vs local alignment|global]]** alignment **empirically**, by comparing the real score against scores from **randomized** sequences. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=3|L4 p.3]]

**Procedure:**
1. Keep sequence **A fixed**; **shuffle** ("anagram") sequence **B** *n* times. Shuffling preserves B's amino-acid **composition** but destroys its **order** — a sequence that is "like B but meaningless".
2. **Globally align** each shuffled B to A, recording a random score $S_i$.
3. The $S_i$ form a **distribution**; compute its **mean** $\mu$ and **standard deviation** $\sigma$.
4. Place your **real** score $S$ on that distribution:

$$Z = \frac{S - \mu}{\sigma}$$

## Unraveling, piece by piece
- **$S$** — the score of the **real** alignment (A vs the true B).
- **$\mu$** — the **mean** of the random scores: what chance typically produces.
- **$\sigma$** — the **standard deviation** of the random scores: the typical spread of chance.
- **$S - \mu$** — how far your score beats the random average.
- **$Z$** — that gap measured **in units of $\sigma$**: "how many standard deviations above chance". The **tail area beyond $S$** is the probability of scoring $\ge S$ by chance.

**Reading Z:** $Z=0$ means $S=\mu$ — the alignment is **no better than random** and could be pure chance. The larger Z, the further into the tail, the less likely by chance (a common rule of thumb treats $Z \gtrsim 5$ as significant).

> [!Caution] The normal-distribution assumption
> Computing a probability from Z **assumes the random scores are normally (Gaussian) distributed** — but alignment scores generally are **not** (they follow an [[Gumbel distribution and the p-value|extreme-value]] law).
> **Why not?** An alignment score is the **maximum** over millions of possible alignments — you keep the *best* one, never a typical one. "Best-of-many" quantities are lopsided, like the **tallest person in a crowd**: there's always room to be surprisingly *taller*, but not surprisingly *shorter*. So the random scores get stretched into a long tail on the **high** side and squashed on the low side — exactly the symmetry a bell curve forbids.
> So Z is best used as a **significance threshold**, not as an exact *p*-value. This very flaw is why **local** alignment uses the [[E-value (Karlin-Altschul)|Karlin–Altschul E-value]] instead.

# TLDR
The Z-score tests a **global** alignment's significance by **shuffling** one sequence many times, building a random-score distribution with mean $\mu$ and SD $\sigma$, and measuring how many SDs the real score sits above chance: $Z=(S-\mu)/\sigma$. $Z=0$ = no better than random. It assumes a normal distribution (often wrong), so treat it as a threshold.

# Recitation Anchors
- For **global** alignment significance, done **empirically**
- Shuffle B *n*× (keep composition, destroy order); align each to A
- Build random-score distribution → mean $\mu$, SD $\sigma$
- $Z = (S-\mu)/\sigma$ = SDs above the random mean
- $Z=0$ → no better than chance; bigger Z → rarer; $Z\gtrsim5$ ≈ significant
- **Assumes normal** distribution → use as a threshold, not exact *p*

> [!Cool] Cool fact
> The Z-score quietly assumes a bell curve, but optimal alignment scores actually follow the **extreme-value (Gumbel)** distribution — which has a much fatter high-score tail. Treating that fat tail as Gaussian *under*-estimates how often big scores happen by chance, so a "significant" Z can mislead. Recognising this is exactly what led Karlin and Altschul to the [[E-value (Karlin-Altschul)|E-value]] for local alignments. [source](https://www.ncbi.nlm.nih.gov/BLAST/tutorial/Altschul-1.html)

# Read aloud
KP.0.Concept: What the Z-score is for.
The Z-score measures whether a global alignment is significant, and it does so empirically — by comparing your real score against scores you'd get from scrambled sequences.

KP.1.Procedure: Shuffling and aligning.
Here's the recipe. Keep sequence A fixed, and shuffle sequence B many times. Shuffling keeps the same amino acids in B but jumbles their order, giving you a sequence that's like B but biologically meaningless. Align each shuffled version to A and record its score. Those random scores form a distribution, and you compute its mean and its standard deviation.

KP.2.Concept: The formula.
Then you place your real score on that distribution. The Z-score is your real score minus the random mean, divided by the standard deviation. Let me unpack it. The real score is what the true alignment got. The mean is what chance typically produces. The standard deviation is the typical spread of those chance scores. So the numerator is how far you beat the random average, and dividing by the standard deviation expresses that gap in units of spread — how many standard deviations above chance you are.

KP.3.Concept: Reading the number.
If the Z-score is zero, your score equals the random mean — the alignment is no better than chance and could be a fluke. The bigger the Z-score, the further out in the tail, and the less likely it happened by chance. A common rule of thumb treats a Z of about five or more as significant.

KP.4.Concept: Why the scores aren't a bell curve.
There's a catch in that probability step. An alignment score isn't one random measurement — it's the best score out of millions of possible alignments. And best-of-many things are lopsided. Think of the tallest person in a crowd: there's always room to be surprisingly taller, but you can't be surprisingly shorter. So the random scores pile up with a long tail stretching toward high values and a squashed low side — exactly the symmetry a bell curve doesn't allow. That's why treating them as normal is the wrong shape.

KP.5.CoolFact: The hidden bell-curve assumption.
And here's the cool part — turning a Z-score into a probability quietly assumes a bell curve. But real alignment scores follow the extreme-value distribution, which has a much fatter tail at high scores. Treating that fat tail as a bell curve underestimates how often big scores happen by chance, so a "significant" Z-score can fool you. Spotting exactly this problem is what led Karlin and Altschul to the E-value for local alignments.

# Question and Answer
Q. What does the Z-score assess, and for which alignment type?
A. The statistical significance of a (global) alignment, by comparing its score to randomised-sequence scores.

Q. What is the shuffling step, and what does it preserve vs destroy?
A. Sequence B is shuffled *n* times: amino-acid composition is preserved, order is destroyed.

Q. Write the Z-score formula and define each term.
A. $Z=(S-\mu)/\sigma$: $S$ real score, $\mu$ mean of random scores, $\sigma$ their standard deviation.

Q. What does $Z=0$ mean?
A. The real score equals the random mean — the alignment is no better than chance.

Q. What assumption makes the Z-score's probability unreliable?
A. It assumes the random scores are normally distributed, but alignment scores follow an extreme-value distribution.

Q. Intuitively, why aren't alignment scores normally distributed?
A. An alignment score is the **maximum** over millions of possible alignments — a "best-of-many" value. Maxima are lopsided (like the tallest person in a crowd: room to be taller, not shorter), so the distribution has a long high-side tail instead of a symmetric bell curve.

Q. Given the normality flaw, how should Z be used?
A. As a significance threshold rather than an exact probability; for local alignments, prefer the Karlin–Altschul E-value.
