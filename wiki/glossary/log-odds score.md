---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/SubstitutionMatrices
  - EXAM_PREP
  - MATH_UNRAVELING
foundational: 5
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

# log-odds score

A [[substitution matrix]] doesn't store raw probabilities — it stores **log-odds scores**. Dayhoff's rule for the score of aligning residues *i* and *j*: [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=10|L4 p.10]]

$$s_{i,j} = 10 \times \log\!\left(\frac{q_{i,j}}{p_{i,j}}\right)$$

## Unraveling, piece by piece
- **$q_{i,j}$** — the probability that *i* and *j* are aligned **because they are [[homology|homologous]]** (the *observed* substitution probability, from the [[PAM matrix extrapolation|PAM]]/[[BLOSUM matrix|BLOSUM]] data).
- **$p_{i,j}$** — the probability of pairing *i* and *j* **by chance**: the product of their [[amino acid frequencies|background frequencies]], $f_i f_j$.
- **$\dfrac{q_{i,j}}{p_{i,j}}$** — the **odds ratio**: observed ÷ chance. $>1$ = "this pairing happens **more** than chance" (favourable); $<1$ = rarer than chance (unfavourable).
- **$\log(\cdots)$** — take the logarithm so scores become **additive**: the log of a *product* is a *sum*, so a whole alignment's score = the **sum** of its column scores (instead of a product of odds). Ratio $=1$ ⇒ score $0$.
- **$\times 10$** — a scaling so that taking the **integer part keeps one decimal** of precision (the matrices are stored as small integers).

> [!Example] Worked: S(W, W)
> $s_{W,W} = 10\log\!\frac{0.55}{0.010} = 10\log(55) \approx \mathbf{17.4}$. The ratio is **55** — a conserved tryptophan is **~50× more likely** by homology than by chance. Conversely a score of **−10** means $\log$-ratio $=-1$, i.e. that pairing is only **1/10** as likely as chance. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=10|L4 p.10]]

This one formula powers **both** [[PAM (Point Accepted Mutation)|PAM]] and [[BLOSUM matrix|BLOSUM]] (and search tools like BLAST) — they differ only in where $q$ comes from and the scaling constant (PAM uses ×10; [[BLOSUM matrix|BLOSUM]] uses $1/\lambda$ with $\lambda=2$). See the worked [[exercise-log-odds-score]].

# TLDR
A substitution-matrix score is a **log-odds** value: $s_{ij}=10\log(q_{ij}/p_{ij})$, where $q$ = probability of pairing by **homology** and $p=f_i f_j$ = probability **by chance**. The **log** makes scores **additive** (alignment score = sum of columns); **×10** keeps a decimal. $s_{W,W}\approx17.4$ ⇒ conserved W is ~50× likelier than chance; negative ⇒ rarer than chance.

# Recitation Anchors
- $s_{i,j} = 10\log(q_{i,j}/p_{i,j})$
- $q$ = observed (homology) prob; $p = f_i f_j$ = chance prob
- ratio $>1$ favourable, $<1$ unfavourable, $=1$ → score 0
- **log → additive** scores (sum columns, not multiply odds)
- **×10** → keep one decimal as an integer
- $s_{W,W}=10\log(0.55/0.010)\approx 17.4$ (~50× chance); $-10$ ⇒ 1/10 of chance
- shared by **PAM** (×10) and **BLOSUM** ($1/\lambda$, $\lambda=2$)

> [!Cool] Cool fact
> There's a deep theorem behind this (Altschul, 1991): **every** substitution matrix that's any good is *implicitly* a log-odds matrix, and a usable one **must have a negative expected score** on random sequences — otherwise random alignments would score higher and higher the longer you make them, and nothing would ever look significant. [source](https://doi.org/10.1016/0022-2836(91)90193-A)

# Read aloud
KP.0.Definition: What's actually stored.
A substitution matrix doesn't store raw probabilities — it stores log-odds scores. Dayhoff's rule for the score of aligning two residues is: ten times the logarithm of q over p. Let me unpack every piece.

KP.1.Concept: The numerator and denominator.
The numerator, q, is the probability that the two residues are aligned because they're genuinely homologous — the observed substitution probability from the PAM or BLOSUM data. The denominator, p, is the probability of pairing them purely by chance, which is just the product of their two background frequencies.

KP.2.Concept: The ratio and the log.
Their ratio, q over p, is the odds: observed divided by chance. Above one means the pairing happens more than chance would predict — favourable. Below one means rarer than chance — unfavourable. Then we take the logarithm, and that's the clever part: the log turns products into sums, so a whole alignment's score becomes the sum of its column scores instead of a product of odds. A ratio of one gives a score of zero.

KP.3.Concept: The factor of ten.
Finally we multiply by ten. That's just a scaling so that taking the integer part still keeps one decimal of precision, because the matrices are stored as small whole numbers.

KP.4.Numbers: A worked example.
Take tryptophan against tryptophan. Ten times the log of nought-point-five-five over nought-point-zero-one-zero is ten times the log of fifty-five, which is about seventeen point four. The ratio is fifty-five, so a conserved tryptophan is roughly fifty times more likely by homology than by chance. Going the other way, a score of minus ten means a log-ratio of minus one, so that pairing is only one-tenth as likely as chance. This same formula powers both PAM and BLOSUM, and search tools like BLAST — they differ only in where q comes from and the scaling constant.

KP.5.CoolFact: Scores must be negative on average.
And here's the cool part — there's a deep theorem behind all this, due to Altschul in 1991. Every good substitution matrix is secretly a log-odds matrix, and a usable one must have a negative expected score on random sequences. Otherwise random alignments would just score higher and higher the longer you made them, and nothing would ever stand out as significant.

# Question and Answer
Q. Write the log-odds score formula and define $q$ and $p$.
A. $s_{ij}=10\log(q_{ij}/p_{ij})$; $q$ = probability of pairing by homology, $p=f_i f_j$ = probability by chance.

Q. Why take the logarithm?
A. So scores are additive — the log of a product is a sum, letting an alignment's score be the sum of its column scores.

Q. What does the ×10 accomplish?
A. It scales the value so the integer part retains one decimal of precision (matrices stored as small integers).

Q. What does a positive vs negative log-odds score mean?
A. Positive ⇒ pairing more likely than chance (favourable); negative ⇒ rarer than chance (unfavourable); zero ⇒ equal to chance.

Q. Compute and interpret $s_{W,W}$ from $q=0.55$, $p=0.010$.
A. $10\log(55)\approx17.4$; a conserved W is ~50× more likely by homology than by chance.

Q. How do PAM and BLOSUM differ in this formula?
A. Only in the source of $q$ and the scaling: PAM uses ×10, BLOSUM uses $1/\lambda$ with $\lambda=2$.

Q. Why must a useful substitution matrix have a negative expected score on random sequences?
A. Otherwise random alignment scores would grow without bound with length, so no alignment could be deemed significant (Altschul 1991).
