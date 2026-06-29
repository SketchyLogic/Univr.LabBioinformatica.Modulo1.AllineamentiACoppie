---
tags:
  - TYPE__/Concept/Model
  - PATH__/Math/Statistics/SignificanceTesting
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentSignificance
  - EXAM_PREP
foundational: 3
prereqs: 4
density: 4
value: 4
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Gumbel distribution and the p-value

The [[E-value (Karlin-Altschul)|E-value]] is an expected *count*. To get an actual **probability** — the chance of seeing a [[global vs local alignment|local]] alignment scoring $\ge x$ purely by chance — convert it: [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=4|L4 p.4]]

$$p(S \ge x) = 1 - e^{-E} = 1 - \exp\!\big(-K m n\, e^{-\lambda x}\big)$$

This is the **extreme-value distribution (EVD)**, also called the **Gumbel** distribution — and it is **not** the Gaussian/bell curve.

> [!Caution] The slide drops a minus sign
> Lecture slide 14 prints $p = 1 - \exp(Kmn\,e^{-\lambda x})$ — **without the inner minus**. That form gives *negative* "probabilities" and is wrong; the correct Karlin–Altschul law is $p = 1 - e^{-E}$. Full explanation: [[Karlin-Altschul p-value erratum]].

**Why extreme-value, not Gaussian?** A local-alignment score is the **maximum** over a huge number of possible sub-alignments. The statistics of the **maximum** of many random quantities is governed by extreme-value theory, whose limiting law is the Gumbel distribution — which has a **longer, fatter right tail** than the bell curve. Using a Gaussian (as the [[Z-score (alignment)|Z-score]] implicitly does) would **underestimate** chance high scores.

**Using it in practice:**
1. Align two sequences **locally**; get score $x$.
2. Compute $p(S\ge x)$ **under the null hypothesis** that the sequences are *not* [[homology|homologous]].
3. If $p <$ threshold (e.g. **0.01 = 1%**), you are **confident they are homologous**.

For small $E$, $1-e^{-E}\approx E$, so tiny E-values read **almost directly** as probabilities.

> [!Caution] Still need biology
> A small *p* says "unlikely by chance" — you **always** also need **biological** significance (function, structure, ancestry) before claiming homology.

# TLDR
The probability of a chance local alignment scoring $\ge x$ is $p = 1 - e^{-E}$, the **extreme-value (Gumbel)** distribution — not a Gaussian, because an alignment score is a **maximum** over many sub-alignments (fat right tail). In practice: compute $p$ under "not homologous"; if $p < 0.01$, claim homology — but biology must still back it up.

# Recitation Anchors
- $p(S\ge x) = 1 - e^{-E} = 1 - \exp(-Kmn\,e^{-\lambda x})$
- **Extreme-value / Gumbel**, NOT Gaussian (score = a **maximum** → fat tail)
- Slide drops a minus → see [[Karlin-Altschul p-value erratum]]
- Procedure: local align → $p$ under H0 (not homologous) → $p<0.01$ ⇒ homologous
- Small $E$: $p \approx E$
- Statistical significance still needs **biological** significance

> [!Cool] Cool fact
> The Gumbel distribution is named for **Emil Gumbel**, who used it to model **extreme floods** — the worst river level expected in 100 years. The *same* mathematics of "the maximum of many random events" governs record rainfalls, peak earthquakes… **and the score of your best local sequence alignment**. [source](https://en.wikipedia.org/wiki/Gumbel_distribution)

# Read aloud
KP.0.Concept: From a count to a probability.
The E-value is an expected count of chance alignments. To turn it into an actual probability — the chance of getting a local alignment this good purely by luck — you convert it: the probability of scoring at least x equals one minus e to the minus E.

KP.1.Definition: The extreme-value distribution.
This curve is the extreme-value distribution, also called the Gumbel distribution, and it is crucially not the familiar bell curve.

KP.2.Concept: Why not a bell curve.
Why extreme-value rather than Gaussian? Because a local alignment score is the maximum over an enormous number of possible sub-alignments. And the statistics of the maximum of many random things is governed by extreme-value theory, whose limiting shape is the Gumbel curve. It has a longer, fatter tail on the high-score side than a bell curve does. If you wrongly used a bell curve — which is what the Z-score quietly does — you'd underestimate how often high scores happen by chance.

KP.3.Procedure: Using it.
In practice you align two sequences locally and get a score. Then you compute the probability of scoring at least that high under the assumption that the sequences are not related. If that probability is below your threshold, say one percent, you're confident they really are homologous. And when the E-value is small, the probability is almost equal to it, so tiny E-values read off directly as probabilities.

KP.4.Connection: Biology still matters.
But remember, a small probability only says "unlikely by chance." You still need biological evidence — shared function, structure, or ancestry — before you truly claim homology.

KP.5.CoolFact: Floods and alignments.
And here's the cool part — the Gumbel distribution is named after Emil Gumbel, who used it to model extreme floods, like the worst river level expected in a century. The very same mathematics of "the maximum of many random events" describes record rainfalls, the biggest earthquakes, and the score of your best local sequence alignment.

# Question and Answer
Q. What is the formula for the p-value of a local alignment score?
A. $p(S\ge x) = 1 - e^{-E} = 1 - \exp(-Kmn\,e^{-\lambda x})$.

Q. What distribution does this represent, and is it Gaussian?
A. The extreme-value (Gumbel) distribution — not Gaussian.

Q. Why do alignment scores follow an extreme-value distribution?
A. A local score is the maximum over many possible sub-alignments, and maxima of many random variables follow extreme-value statistics (fat right tail).

Q. How is the p-value used to decide homology?
A. Compute $p$ under the null "not homologous"; if $p$ < threshold (e.g. 0.01), conclude the sequences are likely homologous.

Q. What is the relationship between $p$ and $E$ for small $E$?
A. $p = 1 - e^{-E} \approx E$, so small E-values approximate probabilities directly.

Q. What's wrong with the slide's printed p-value formula?
A. It omits the inner minus sign ($1-\exp(+E)$), which yields negative probabilities; the correct form is $1-e^{-E}$ (see the erratum).

Q. Does a significant p-value prove homology?
A. No — biological significance (function/structure/ancestry) is still required.
