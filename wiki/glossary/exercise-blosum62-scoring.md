---
tags:
  - TYPE__/Executable/Exercise
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/SubstitutionMatrices
  - EXAM_PREP
foundational: 2
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

# exercise-blosum62-scoring

**Tool**: pen & paper + a [[BLOSUM matrix|BLOSUM62]] table · **Source**: [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=12|L4 slide 45]]

## Task
Score this alignment using **BLOSUM62**, with a **gap penalty of −11** for the single gap column. Sum the per-column scores.

```
Seq1:  V  D  S  -  C  Y
Seq2:  V  E  S  L  C  Y
```

## Walkthrough
Look up each aligned pair in the BLOSUM62 matrix (the gap column uses the gap penalty, not the matrix):

| Column | Pair | BLOSUM62 score |
|---|---|---|
| 1 | V·V | **+4** |
| 2 | D·E | **+2** |
| 3 | S·S | **+4** |
| 4 | –·L | **−11** (gap) |
| 5 | C·C | **+9** |
| 6 | Y·Y | **+7** |

## Expected answer
$$\text{Total} = 4 + 2 + 4 - 11 + 9 + 7 = \mathbf{15}$$
- The general rule (slide 45): **$\text{Total} = \sum \text{similarities} - \sum \text{gap penalties}$**.
- Note the **identity scores are not all equal**: C·C = 9 and Y·Y = 7 outscore V·V = 4, because rare/constrained residues carry **more information** when conserved (a [[log-odds score]] effect).
- The **conservative** swap D·E still scores **positive** (+2); the single gap costs more than any match rewards.

## Concepts exercised
- [[BLOSUM matrix]]
- [[log-odds score]]
- [[substitution matrix]]
- [[affine gap penalty]]

# TLDR
Scoring `VDS-CY` / `VESLCY` with BLOSUM62 (gap = −11): $4+2+4-11+9+7 = \mathbf{15}$. Identity scores differ by residue (C·C=9, Y·Y=7 > V·V=4) because conserving rare residues is more informative; the conservative D·E still scores +2.

# Recitation Anchors
- Score each pair from BLOSUM62; gap column = **−11**
- V·V 4 · D·E 2 · S·S 4 · gap −11 · C·C 9 · Y·Y 7
- Total = **15** = Σ similarities − Σ gap penalties
- Identity scores vary: C·C 9, Y·Y 7 > V·V 4 (information content)
- Conservative swap D·E is still **positive**

> [!Cool] Cool fact
> In BLOSUM62 the **highest** diagonal score is **W·W = +11** — conserving a tryptophan is the strongest single-column signal of homology, because Trp is rare and almost never tolerated to change. By contrast a common, flexible residue like Ser scores only **+4** for an exact match. [source](https://doi.org/10.1073/pnas.89.22.10915)

# Read aloud
KP.0.Procedure: The task.
This exercise has you score a short alignment with the BLOSUM-sixty-two matrix, treating the single gap column with a penalty of minus eleven, and then add up the per-column scores.

KP.1.Procedure: Looking up each column.
Go column by column. V against V scores plus four. D against E scores plus two. S against S scores plus four. The gap against L costs minus eleven. C against C scores plus nine. And Y against Y scores plus seven.

KP.2.Numbers: The total.
Adding those up: four plus two plus four minus eleven plus nine plus seven gives fifteen. The general rule on the slide is: the total equals the sum of the similarities minus the sum of the gap penalties.

KP.3.Concept: Why identities aren't all equal.
Notice the identical-residue scores aren't all the same. C against C is nine and Y against Y is seven, both beating V against V at four. That's because conserving a rare or constrained residue carries more information than conserving a common one — a log-odds effect. And the conservative swap D against E still scores positive, while the single gap costs more than any of the matches reward.

KP.4.CoolFact: Tryptophan is king.
And here's the cool part — in BLOSUM-sixty-two the highest diagonal score of all is tryptophan against tryptophan, at plus eleven. Conserving a tryptophan is the strongest single-column signal of homology, because tryptophan is rare and almost never allowed to change. A common, flexible residue like serine scores only plus four for an exact match.

# Question and Answer
Q. What is the total BLOSUM62 score for `VDS-CY` / `VESLCY` (gap −11)?
A. $4+2+4-11+9+7 = 15$.

Q. What is the general scoring rule shown on the slide?
A. Total = Σ similarities − Σ gap penalties.

Q. Why does C·C (9) score higher than V·V (4) even though both are exact matches?
A. Conserving a rarer/more-constrained residue is more informative (a log-odds effect), so it earns a higher score.

Q. Does the conservative substitution D·E score positive or negative?
A. Positive (+2) — D and E are chemically similar, a favourable substitution.

Q. Which single column hurt the score most, and by how much?
A. The gap column (–·L), at −11.

Q. What is the highest diagonal score in BLOSUM62, and why?
A. W·W = +11 — tryptophan is rare and almost never tolerated to change, so its conservation is strong evidence.
