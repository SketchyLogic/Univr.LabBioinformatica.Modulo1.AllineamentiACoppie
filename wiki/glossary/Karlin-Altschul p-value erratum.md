---
tags:
  - TYPE__/Concept/Argument
  - PATH__/Math/Statistics/SignificanceTesting
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentSignificance
foundational: 2
prereqs: 4
density: 3
value: 3
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Karlin-Altschul p-value erratum

> [!Danger] Source error
> **Lecture L4, slide 14** prints the local-alignment p-value as
> $$p(S \ge x) = 1 - \exp\!\big(K m n\, e^{-\lambda x}\big) \quad\text{(as printed — WRONG)}$$
> The correct Karlin–Altschul form has an **inner minus sign**:
> $$p(S \ge x) = 1 - \exp\!\big(\mathbf{-}\,K m n\, e^{-\lambda x}\big) = 1 - e^{-E}.$$

This note exists because the wiki uses the **correct** form in [[Gumbel distribution and the p-value]] and [[E-value (Karlin-Altschul)]], so the discrepancy with the slide is documented here rather than cluttering those entries. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=4|L4 p.4]]

# Argument
**Why the minus sign is mandatory** (three independent checks):

1. **A probability can't be negative.** The [[E-value (Karlin-Altschul)|E-value]] $E = Kmn\,e^{-\lambda x}$ is a count of expected events, so $E > 0$ always ($K, m, n > 0$ and $\exp > 0$). As *printed*, $\exp(+E) > 1$, hence $1 - \exp(+E) < 0$ — a **negative "probability"**. Impossible. With the minus, $e^{-E} \in (0,1]$, so $p \in [0,1)$. ✓

2. **It follows from the Poisson law.** The number of chance high-scoring alignments is **Poisson**-distributed with mean $E$. The probability of seeing **at least one** is
$$p = 1 - P(\text{none}) = 1 - e^{-E}.$$
The exponent is $-E$, not $+E$.

3. **Limiting behaviour is only right with the minus.**
   - $x \to \infty \Rightarrow E \to 0 \Rightarrow p \to 0$ (a sky-high score is essentially impossible by chance). ✓
   - $x$ small $\Rightarrow E$ large $\Rightarrow p \to 1$ (a low bar is almost certainly cleared by chance). ✓
   The printed form gives the opposite, nonsensical, trend.

**Verdict:** the slide almost certainly **dropped a minus sign** in transcription. Always use $p = 1 - e^{-E}$.

# TLDR
Slide 14's p-value $1-\exp(Kmn\,e^{-\lambda x})$ is **missing a minus**: it yields negative probabilities. The correct Karlin–Altschul form is $p = 1 - e^{-E} = 1-\exp(-Kmn\,e^{-\lambda x})$, which follows from the Poisson "probability of at least one event" and stays within $[0,1]$.

# Recitation Anchors
- Slide: $1-\exp(+Kmn\,e^{-\lambda x})$ ❌ → gives **negative** probabilities
- Correct: $p = 1 - e^{-E} = 1-\exp(\mathbf{-}Kmn\,e^{-\lambda x})$ ✓
- Reason 1: $E>0$ so $\exp(+E)>1$ ⇒ $1-\exp(+E)<0$ (impossible)
- Reason 2: Poisson — $p = 1 - P(\text{none}) = 1 - e^{-E}$
- Reason 3: limits ($x{\to}\infty{:}\,p{\to}0$; $x$ small${:}\,p{\to}1$) only work with the minus

> [!Cool] Cool fact
> The form $1 - e^{-\text{mean}}$ — "the probability of **at least one** rare event" — is one of the most reused results in all of probability: it gives the chance of at least one radioactive decay in an interval, at least one typo on a page, or at least one chance alignment in a database. Same Poisson maths, everywhere. [source](https://en.wikipedia.org/wiki/Poisson_distribution)

# Read aloud
KP.0.Concept: What's wrong on the slide.
This is a correction note. Slide 14 of the lecture writes the p-value for a local alignment as one minus the exponential of K m n e-to-the-minus-lambda-x. But that's missing a minus sign inside the exponential. The correct formula has a minus there, giving one minus e-to-the-minus-E.

KP.1.Concept: Why a probability can't be negative.
Here's the first reason the minus must be there. The E-value is a count of expected events, so it's always positive. If you exponentiate a positive number you get something bigger than one, and one minus something bigger than one is negative. A negative probability is impossible. Put the minus back, and the exponential lands between zero and one, so the probability sits properly between zero and one.

KP.2.Procedure: Where the right form comes from.
The second reason is that the correct form follows from the Poisson law. The number of chance high-scoring alignments is Poisson-distributed with mean E. The probability of seeing at least one is one minus the probability of seeing none, and the probability of none is e-to-the-minus-E. So the answer is one minus e-to-the-minus-E — the exponent is minus E.

KP.3.Concept: The sanity checks.
And third, the limits only make sense with the minus. Push the score very high and E goes to zero and the probability goes to zero — a huge score is essentially impossible by chance. Drop the score low and E gets large and the probability goes to one — a low bar is almost always cleared by chance. The printed version gives the opposite, nonsensical trend. So the slide simply dropped a minus sign; always use one minus e-to-the-minus-E.

KP.4.CoolFact: A universal formula.
And here's the cool part — this form, one minus e-to-the-minus-mean, the probability of at least one rare event, is one of the most reused results in all of probability. It gives the chance of at least one radioactive decay in an interval, at least one typo on a page, or at least one chance alignment in a database. The same Poisson mathematics, turning up everywhere.

# Question and Answer
Q. What is wrong with the p-value formula on slide 14?
A. It omits the inner minus sign, printing $1-\exp(+Kmn e^{-\lambda x})$, which produces negative probabilities.

Q. What is the correct Karlin–Altschul p-value?
A. $p = 1 - e^{-E} = 1 - \exp(-Kmn e^{-\lambda x})$.

Q. Give a one-line reason the minus must be present.
A. $E>0$, so $\exp(+E)>1$ and $1-\exp(+E)<0$ — a probability cannot be negative.

Q. From which probability law does $1-e^{-E}$ come?
A. The Poisson distribution: $p(\ge 1) = 1 - P(0) = 1 - e^{-E}$.

Q. What are the correct limits as $x\to\infty$ and as $x$ gets small?
A. $x\to\infty$: $p\to0$ (high score impossible by chance); $x$ small: $p\to1$ (low score certain by chance).

Q. Why is this kept in a separate file?
A. So the main entries can use the correct form cleanly, with the source discrepancy documented in one dedicated place.
