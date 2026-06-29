---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/SubstitutionMatrices
  - EXAM_PREP
foundational: 5
prereqs: 2
density: 3
value: 5
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# BLOSUM matrix

**BLOSUM** = **BLO**ck **SU**bstitution **M**atrix. It is a [[substitution matrix]] built **empirically**, from the **BLOCKS database** — collections of **blocks** (conserved *regions*) taken from **[[global vs local alignment|local]] alignments of distantly related sequences**. No evolutionary model is assumed; you just count what's there. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=11|L4 p.11]]

**What the number means — a clustering threshold.** In **BLOSUM*n***, sequences that are **≥ *n*% identical are clustered** (merged and down-weighted) *before* counting substitutions, so near-duplicates don't dominate. **BLOSUM62** = built after clustering at **62% identity** — and it is the **default matrix for BLAST**.

**The score** is a [[log-odds score]] just like PAM, but with scaling $1/\lambda$ (and $\lambda = 2$ for BLOSUM, vs ×10 for PAM):

$$S_{ij} = \frac{1}{\lambda}\,\log\!\left(\frac{p_{ij}}{q_i\,q_j}\right)$$

> [!Caution] Letter convention flips vs PAM
> In **this** (BLOSUM) formula $p_{ij}$ is the **observed** pair probability and $q_i q_j$ is the **chance** product — the **opposite** lettering to the PAM [[log-odds score]] ($q$=observed, $p$=chance). The *idea* (observed ÷ chance, logged) is identical; only the symbols swap.

The usable BLOSUM range is roughly **90–45**, narrower than PAM's 30–250. Comparison and the (inverse) numbering logic: [[PAM vs BLOSUM]].

# TLDR
**BLOSUM** (BLOck SUbstitution Matrix) is an **empirical** [[substitution matrix]] from the **BLOCKS** database of conserved local-alignment blocks. **BLOSUM*n*** clusters sequences **≥ *n*% identical** before counting; **BLOSUM62** (cluster at 62%) is **BLAST's default**. Scores are [[log-odds score|log-odds]] with $1/\lambda$, $\lambda=2$.

# Recitation Anchors
- **BLO**ck **SU**bstitution **M**atrix — **empirical**, no evolutionary model
- From the **BLOCKS** database: conserved **blocks** of **local** alignments (distant sequences)
- **BLOSUM*n*** = cluster sequences **≥ *n*% identical** before counting
- **BLOSUM62** = clustered at 62% = **BLAST default**
- Score = log-odds, $S_{ij}=\frac1\lambda\log(p_{ij}/q_iq_j)$, $\lambda=2$
- Lettering flips vs PAM ($p$=observed here); range ~90–45

> [!Cool] Cool fact
> **BLOSUM62** is the single most-used substitution matrix in biology — and in **2008** researchers found the version shipped in standard software for **~15 years contained a bug** (the clustering was miscoded). The twist: the *miscalculated* matrix actually performed **slightly better** at finding homologs, so the "wrong" BLOSUM62 stayed the default. [source](https://doi.org/10.1038/nbt0808-274)

# Read aloud
KP.0.Definition: What BLOSUM stands for.
BLOSUM stands for block substitution matrix. It's a substitution matrix built empirically, from the BLOCKS database — collections of blocks, meaning conserved regions, taken from local alignments of distantly related sequences. No evolutionary model is assumed; you simply count what you actually observe.

KP.1.Concept: What the number means.
The number is a clustering threshold. In BLOSUM-n, any sequences that are at least n percent identical get clustered together and down-weighted before substitutions are counted, so that near-duplicate sequences don't dominate the statistics. BLOSUM-sixty-two is built after clustering at sixty-two percent identity, and it's the default matrix for BLAST.

KP.2.Concept: The score formula.
The score is a log-odds value, exactly like PAM, but scaled by one over lambda, with lambda equal to two for BLOSUM, versus times ten for PAM. One warning: in the BLOSUM formula the letters flip — p is the observed pair probability and q-i times q-j is the chance product, the opposite of the PAM convention. The idea is identical, observed over chance then logged; only the symbols swap.

KP.3.CoolFact: The famous bug.
And here's the cool part — BLOSUM-sixty-two is the most-used substitution matrix in all of biology, and in 2008 researchers discovered that the version shipped in standard software for about fifteen years contained a bug: the clustering step was miscoded. The twist is that the miscalculated matrix actually performed slightly better at finding homologs, so the wrong BLOSUM-sixty-two simply stayed the default.

# Question and Answer
Q. What does BLOSUM stand for, and from what is it built?
A. BLOck SUbstitution Matrix; built empirically from the BLOCKS database of conserved local-alignment blocks of distantly related sequences.

Q. What does the number in BLOSUM62 mean?
A. Sequences ≥62% identical are clustered before counting substitutions (a clustering threshold), so near-duplicates don't dominate.

Q. Which BLOSUM matrix is the BLAST default?
A. BLOSUM62.

Q. How does the BLOSUM score formula relate to PAM's log-odds?
A. Same log-odds idea (observed ÷ chance, logged); BLOSUM scales by $1/\lambda$ with $\lambda=2$, PAM by ×10.

Q. What's the lettering pitfall between the PAM and BLOSUM formulas?
A. They swap symbols: in BLOSUM $p_{ij}$ is observed and $q_iq_j$ is chance; in PAM $q$ is observed and $p$ is chance.

Q. Why is clustering before counting important?
A. It prevents large families of nearly-identical sequences from biasing the substitution counts.
