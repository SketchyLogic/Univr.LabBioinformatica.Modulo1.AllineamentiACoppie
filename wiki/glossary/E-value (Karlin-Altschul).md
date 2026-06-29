---
tags:
  - TYPE__/Concept/Model
  - PATH__/Math/Statistics/SignificanceTesting
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentSignificance
  - MATH_UNRAVELING
  - EXAM_PREP
foundational: 4
prereqs: 3
density: 4
value: 5
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# E-value (Karlin-Altschul)

For **[[global vs local alignment|local]]** alignment, significance has a **closed-form** answer — no shuffling needed. Karlin and Altschul proved that for two **random** sequences of lengths $m$ and $n$, the **expected number $E$** of locally-aligned (ungapped) subsequences scoring $\ge x$ is: [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=4|L4 p.4]]

$$E(S \ge x) = K\,m\,n\,e^{-\lambda x}$$

## Unraveling, piece by piece
- **$E(S\ge x)$** — the **E-value**: the *expected count* of distinct alignments that random chance would produce scoring at least $x$. Not a probability — a **number of expected hits** (can exceed 1).
- **$m, n$** — the **lengths** of the two sequences. Their product $mn$ is the **size of the search space** — how many places an alignment could start. More/longer sequence ⇒ more chances ⇒ bigger $E$.
- **$K$** — a constant set by the **scoring matrix** (and sequence correlations); a scaling of the search space.
- **$\lambda$** (lambda) — a positive **score-scaling** parameter set by the scoring scheme and **amino-acid composition**; it puts raw scores onto a natural ("nat") scale.
- **$e^{-\lambda x}$** — the **exponential decay** in the score threshold: raising $x$ makes chance hits **exponentially** rarer.

**In words:** $E = (\text{search space}) \times (\text{score rarity})$. Double the sequence length and $E$ doubles; raise the score and $E$ plummets exponentially.

> [!Hint] Reading an E-value
> $E \ll 1$ ⇒ **significant** (you'd expect far less than one such alignment by chance). $E = 0.001$: ~1-in-1000 chance hit — strong. $E = 10$: you'd expect **ten** by chance — meaningless. The threshold (e.g. $E < 0.01$) turns $E$ into a yes/no homology call — see [[Gumbel distribution and the p-value]].

This is the number **BLAST reports** for every hit. It connects to the *probability* of seeing such a score via $p = 1 - e^{-E}$ (the [[Gumbel distribution and the p-value|Gumbel form]]).

# TLDR
For **local** alignment, the **E-value** $E(S\ge x)=Kmn\,e^{-\lambda x}$ gives the **expected number** of chance alignments scoring $\ge x$. 
$mn$ = search-space size; 
$K$, $\lambda$ = constants from the scoring scheme/composition; 
$e^{-\lambda x}$ = exponential rarity of high scores. $E \ll 1$ means significant. It's the number BLAST reports.

# Recitation Anchors
- **Local** significance, closed-form (no shuffling)
- $E(S\ge x) = K\,m\,n\,e^{-\lambda x}$
- $E$ = **expected number** of chance alignments $\ge x$ (not a probability)
- $m,n$ = lengths; $mn$ = **search space**; $K$ = matrix constant; $\lambda$ = score scale (aa composition)
- $E \propto mn$ (linear) $\times\, e^{-\lambda x}$ (exponential in score)
- $E \ll 1$ ⇒ significant; the number **BLAST reports**
- Probability link: $p = 1 - e^{-E}$

> [!Cool] Cool fact
> A deep consequence of this formula: the expected **best** local-alignment score of two random sequences grows only like $\ln(mn)/\lambda$ — **logarithmically** with size. So if a database **doubles**, you need only a *tiny* score increase to stay just as significant — which is why sequence search scaled gracefully as databases exploded. [source](https://doi.org/10.1073/pnas.87.6.2264)

# Read aloud
KP.0.Concept: A formula instead of shuffling.
For local alignment, significance has a clean formula — you don't need to shuffle anything. Karlin and Altschul proved that for two random sequences, the expected number of high-scoring local matches follows a simple equation.

KP.1.Definition: The E-value.
The expected number E of locally-aligned subsequences scoring at least x equals K, times m, times n, times e to the minus lambda x. The left side, the E-value, is the expected count of chance alignments that score at least x. Notice it's a count, not a probability — it can be bigger than one.

KP.2.Concept: What each piece means.
Let me unpack the right side. m and n are the lengths of the two sequences, and their product is the size of the search space — how many places an alignment could begin. More or longer sequence means more chances, so a bigger E. K is a constant set by the scoring matrix. Lambda is a positive scaling factor set by the scoring scheme and the amino-acid composition, and it puts raw scores onto a natural scale. Finally, e to the minus lambda x is an exponential decay: as you raise the score threshold, chance hits become exponentially rarer.

KP.3.Concept: Reading an E-value.
So E is the search space times the rarity of the score. Double the sequence length and E doubles; raise the score and E plunges. When E is far below one, the alignment is significant — you'd expect far less than one such match by chance. An E-value of one-thousandth is strong; an E-value of ten means you'd expect ten by chance, so it's meaningless. This is exactly the number BLAST prints next to every hit.

KP.4.CoolFact: Logarithmic growth.
And here's the cool part — a deep consequence of this formula is that the expected best random score grows only with the logarithm of the search-space size. So when a database doubles, you need only a tiny bump in score to stay just as significant. That logarithmic growth is why sequence searching kept working gracefully even as databases exploded in size.

# Question and Answer
Q. What does the E-value represent?
A. The expected number of distinct local alignments that random chance would produce scoring at least *x* — a count, not a probability.

Q. State the Karlin–Altschul formula and name each symbol.
A. $E(S\ge x)=Kmn\,e^{-\lambda x}$: $m,n$ sequence lengths; $K$ matrix constant; $\lambda$ score-scaling (aa composition); $x$ score threshold.

Q. What is $mn$ interpreted as?
A. The size of the search space — how many places an alignment could start.

Q. How does $E$ change with sequence length vs with score?
A. Linearly in $mn$ (longer ⇒ bigger $E$) and exponentially down in $x$ (higher score ⇒ much smaller $E$).

Q. Is $E=0.001$ or $E=10$ significant?
A. $E=0.001$ is significant (≪1 expected by chance); $E=10$ is not (ten expected by chance).

Q. How does the E-value relate to a probability?
A. Via $p = 1 - e^{-E}$ (the Gumbel/extreme-value form); for small $E$, $p \approx E$.

Q. Why did searching scale well as databases grew? 
A. The expected best random score grows only like $\ln(mn)$, so doubling the database needs only a tiny score increase to stay significant.
