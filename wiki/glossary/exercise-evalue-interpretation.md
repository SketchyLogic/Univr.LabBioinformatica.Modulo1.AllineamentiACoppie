---
tags:
  - TYPE__/Executable/Exercise
  - PATH__/Math/Statistics/SignificanceTesting
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentSignificance
foundational: 2
prereqs: 3
density: 2
value: 3
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-29
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# exercise-evalue-interpretation

**Tool**: calculator (or read a BLAST report) · **Source**: [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=4|L4 slides 13–14]]
*(Worked numbers below are illustrative — the lecture gives the formulas, not a numeric example.)*

## Task
Use the [[E-value (Karlin-Altschul)|E-value]] formula to (a) see how the E-value drops as the score rises, (b) convert E-values to [[Gumbel distribution and the p-value|p-values]], and (c) decide significance.

Assume two random sequences with $m=n=1000$, $K=0.1$, $\lambda=0.3$. Compute $E(S\ge x) = Kmn\,e^{-\lambda x}$ for $x = 40, 50, 60$, then convert each to $p = 1-e^{-E}$.

## Walkthrough
$Kmn = 0.1 \times 1000 \times 1000 = 10^5$. Then multiply by $e^{-0.3x}$:

| score $x$ | $e^{-0.3x}$ | $E = 10^5 \cdot e^{-0.3x}$ | $p = 1-e^{-E}$ | verdict |
|---|---|---|---|---|
| 40 | $e^{-12}\approx6.1\times10^{-6}$ | $\approx 0.61$ | $\approx 0.46$ | **not** significant |
| 50 | $e^{-15}\approx3.1\times10^{-7}$ | $\approx 0.031$ | $\approx 0.030$ | borderline |
| 60 | $e^{-18}\approx1.5\times10^{-8}$ | $\approx 0.0015$ | $\approx 0.0015$ | **significant** |

## Expected answer
- Raising the score by **20** (40→60) drops $E$ by a factor of $e^{-0.3\cdot20}=e^{-6}\approx 400$ — **exponential**, exactly as $e^{-\lambda x}$ predicts.
- For **small** $E$ (rows 50, 60), $p \approx E$ — the p-value and E-value coincide.
- For **large** $E$ (row 40), $p$ and $E$ diverge ($E$ can exceed 1; $p$ cannot).
- Using a **1% threshold**, only $x=60$ ($p\approx0.0015 < 0.01$) is significant — and you'd **still** need [[homology|biological]] support.

## E-value vs p-value (intuition)
Both answer "could chance explain this score?" — but in **different currencies**:

- **E-value = a *count*.** *How many* hits this good (or better) you'd expect to stumble on **by chance** in a search this size. It's an expected number of false alarms, so it can be anything from $10^{-50}$ to 200, and a bigger search (bigger $m\,n$) gives more chances → bigger E.
- **p-value = a *probability*.** The chance of getting **at least one** such fluke. Being a probability, it's trapped between 0 and 1.

> [!Hint] The bus-stop analogy
> The E-value is "on average how many buses arrive per minute"; the p-value is "what's the chance *at least one* arrives." If buses are **rare** ($E=0.01$), the numbers nearly coincide — expecting 0.01 buses ≈ a 1% chance of one. That's why **small $E$ ⇒ $p\approx E$**. But if you expect **five** buses ($E=5$), there's no "500% chance" — the chance of at least one is essentially certain (≈99.3%). That's why **large $E$ ⇒ they diverge**: $E$ keeps climbing past 1 while $p$ saturates at 1. The bridge $p=1-e^{-E}$ is just the rule for "at least one event when you expect $E$ of them."

**Takeaway**: $E$ *counts* the expected flukes; $p$ is the *probability* of seeing one. They agree exactly in the regime you care about — when flukes are rare.

## Concepts exercised
- [[E-value (Karlin-Altschul)]]
- [[Gumbel distribution and the p-value]]
- [[statistical significance of an alignment]]

# TLDR
Plugging into $E=Kmn\,e^{-\lambda x}$ with $m=n=1000$, $K=0.1$, $\lambda=0.3$: scores 40/50/60 give E ≈ 0.61 / 0.031 / 0.0015. Raising the score is **exponentially** rewarded; for small E, $p\approx E$; only $x=60$ clears a 1% threshold. E-values above 1 can't be read as probabilities.

# Recitation Anchors
- $Kmn=10^5$; multiply by $e^{-0.3x}$
- $x{=}40{\to}E{\approx}0.61$; $x{=}50{\to}0.031$; $x{=}60{\to}0.0015$
- +20 score ⇒ ÷ ~400 in E (exponential)
- small E ⇒ $p\approx E$; large E ⇒ $p<E<\infty$ but $p\le1$
- only $x=60$ significant at 1%; still need biology

> [!Cool] Cool fact
> Web BLAST's **default Expect threshold is 10** — it deliberately shows you hits you'd expect *ten* of by chance, so you don't miss a borderline homolog. Confident homology calls typically want $E$ far smaller (often $<10^{-3}$ or much less). [source](https://www.ncbi.nlm.nih.gov/BLAST/tutorial/Altschul-1.html)

# Read aloud
KP.0.Procedure: The setup.
This exercise uses the E-value formula on some illustrative numbers. Take two random sequences, each a thousand residues long, with K equal to nought point one and lambda equal to nought point three. We'll compute the E-value at three score thresholds — forty, fifty, and sixty — and then turn each into a probability.

KP.1.Procedure: Doing the arithmetic.
First, K times m times n is nought point one times a thousand times a thousand, which is a hundred thousand. Then you multiply by e to the minus nought-point-three times the score. At a score of forty that gives an E-value of about nought point six. At fifty, about nought point zero three. At sixty, about nought point zero zero one five. Converting with one minus e-to-the-minus-E gives probabilities of roughly nought point four six, nought point zero three, and nought point zero zero one five.

KP.2.Numbers: What the pattern shows.
Notice two things. Raising the score by twenty, from forty to sixty, divides the E-value by about four hundred — that's the exponential reward for a higher score. And for the small E-values, the probability is essentially equal to the E-value, while for the large one they diverge, because an E-value can exceed one but a probability cannot.

KP.3.Concept: E-value versus p-value.
It's worth being clear on the difference between these two. The E-value is a count — how many hits this good you'd expect to find purely by chance in a search this size. The p-value is a probability — the chance of getting at least one such fluke, so it's stuck between zero and one. Picture waiting at a bus stop: the E-value is how many buses you expect per minute, the p-value is the chance at least one shows up. When buses are rare, those two numbers almost match — that's why for small E-values the p-value is essentially the same. But if you expect five buses, you can't have a five-hundred-percent chance; the chance of at least one is basically certain. That's why for large E-values the two part ways: the count keeps climbing while the probability flattens out at one.

KP.4.Concept: The verdict.
Using a one-percent threshold, only the score of sixty counts as significant. And even then, you'd still want biological evidence before declaring the sequences homologous.

KP.5.CoolFact: BLAST shows you the marginal hits.
And here's the cool part — web BLAST's default Expect threshold is ten. It deliberately shows you hits you'd expect ten of by chance, so you don't accidentally miss a borderline homolog. For a confident call, you'd want an E-value far smaller, often below a thousandth.

# Question and Answer
Q. With $m=n=1000$, $K=0.1$, what is $Kmn$?
A. $0.1 \times 1000 \times 1000 = 10^5$.

Q. What is $E$ at $x=60$ (with $\lambda=0.3$), and is it significant?
A. $E = 10^5 e^{-18} \approx 0.0015$ — significant (well below 1).

Q. By what factor does $E$ change going from $x=40$ to $x=60$?
A. By $e^{-0.3\cdot20}=e^{-6}\approx 1/400$ — about 400× smaller.

Q. When does $p \approx E$, and when do they diverge?
A. For small $E$, $p\approx E$; for large $E$ they diverge ($E$ can exceed 1, $p$ cannot).

Q. Intuitively, how do the E-value and p-value differ?
A. The E-value is an expected **count** of chance hits this good (unbounded, scales with search size); the p-value is the **probability** of at least one such chance hit (capped at 1). They nearly coincide when $E$ is small.

Q. Which score passes a 1% significance threshold here?
A. Only $x=60$ ($p\approx0.0015 < 0.01$).

Q. After a significant E-value, what is still required?
A. Biological significance — function/structure/ancestry support.
