---
tags:
  - TYPE__/Executable/Exercise
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/SubstitutionMatrices
foundational: 2
prereqs: 3
density: 3
value: 4
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# exercise-log-odds-score

**Tool**: calculator · **Source**: [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=10|L4 slide 39]]

## Task
Using the Dayhoff [[log-odds score]] formula $s_{i,j} = 10\log_{10}(q_{i,j}/p_{i,j})$, (a) compute the PAM250 score for a conserved tryptophan given $q_{W,W}=0.55$ and $p_{W,W}=0.010$, and (b) interpret a score of **−10**.

## Walkthrough
**(a) S(W, W):**
$$s_{W,W} = 10\log_{10}\!\left(\frac{0.55}{0.010}\right) = 10\log_{10}(55) = 10 \times 1.740 \approx \mathbf{17.4}$$
The odds ratio is $0.55/0.010 = \mathbf{55}$ — a conserved W is **~50× more likely** by homology than by chance.

**(b) A score of −10:**
$$-10 = 10\log_{10}(r) \;\Rightarrow\; \log_{10}(r) = -1 \;\Rightarrow\; r = 10^{-1} = \tfrac{1}{10}.$$
So that pairing is only **1/10 as likely** as chance — strongly *unfavourable*.

## Expected answer
- **S(W,W) ≈ 17** (the integer part keeps the first decimal, by the ×10 convention).
- Each **+10** points = one factor of **10×** more likely than chance; **−10** = 1/10 as likely.
- The score is **positive** when observed > chance, **zero** at parity, **negative** when rarer than chance.

## Concepts exercised
- [[log-odds score]]
- [[amino acid frequencies]] (the $p=f_i f_j$ baseline)
- [[PAM (Point Accepted Mutation)]]

# TLDR
$s_{W,W}=10\log_{10}(0.55/0.010)=10\log_{10}(55)\approx 17.4$ — odds ratio 55, so a conserved W is ~50× likelier by homology than chance. A score of −10 means a log-ratio of −1, i.e. 1/10 of chance. Each ±10 points = one order of magnitude in the odds.

# Recitation Anchors
- $s=10\log_{10}(q/p)$; here $q=0.55$, $p=0.010$
- ratio $=55$; $s=10\log_{10}(55)\approx 17.4$ (~50× chance)
- score **−10** ⇒ log-ratio −1 ⇒ **1/10** of chance
- each ±10 points = ×10 / ÷10 in odds
- positive = favourable, 0 = chance, negative = unfavourable

> [!Cool] Cool fact
> The logarithm is the whole trick: it converts the **product** of per-column odds across an alignment into a **sum** of column scores — the same idea that let slide rules multiply by adding. That's why you can just **add up** matrix scores down an alignment to get the total log-odds of the whole thing. [source](https://doi.org/10.1016/0022-2836(91)90193-A)

# Read aloud
KP.0.Procedure: The task.
This exercise uses Dayhoff's log-odds formula: the score equals ten times the base-ten logarithm of q over p. You'll compute the PAM-two-fifty score for a conserved tryptophan, given q equals nought point five five and p equals nought point zero one zero, and then interpret a score of minus ten.

KP.1.Numbers: Computing S of W, W.
Plug in: ten times the log of nought-point-five-five over nought-point-zero-one-zero. That inside ratio is fifty-five. The log of fifty-five is about one point seven four, and ten times that is roughly seventeen point four. So the odds ratio is fifty-five — a conserved tryptophan is about fifty times more likely by homology than by chance.

KP.2.Numbers: Interpreting minus ten.
Now a score of minus ten. Set minus ten equal to ten times the log of the ratio, so the log of the ratio is minus one, which means the ratio is one-tenth. That pairing is only a tenth as likely as chance — strongly unfavourable. In general, every plus ten points means ten times more likely than chance, and every minus ten means a tenth as likely. Positive scores are favourable, zero is exactly chance, negative is rarer than chance.

KP.3.CoolFact: Why logarithms.
And here's the cool part — the logarithm is the whole trick. It turns the product of the per-column odds across an alignment into a simple sum of column scores, the same idea that once let slide rules multiply by adding. That's exactly why you can just add up the matrix scores down an alignment to get the total log-odds for the whole thing.

# Question and Answer
Q. Compute S(W,W) given q = 0.55, p = 0.010.
A. $10\log_{10}(0.55/0.010)=10\log_{10}(55)\approx 17.4$.

Q. What does the odds ratio of 55 mean in words?
A. A conserved tryptophan is about 50× more likely to occur by homology than by chance.

Q. Interpret a log-odds score of −10.
A. The log-ratio is −1, so the pairing is 1/10 as likely as chance — unfavourable.

Q. By the ×10 convention, what does each 10 points of score correspond to?
A. One order of magnitude (10×) in the odds ratio.

Q. When is a log-odds score positive, zero, or negative?
A. Positive when observed > chance, zero at parity, negative when rarer than chance.

Q. Why can per-column scores simply be added across an alignment?
A. Because log turns the product of per-column odds into a sum of log-odds scores.
