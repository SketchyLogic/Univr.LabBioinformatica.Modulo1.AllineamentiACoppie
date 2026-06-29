---
tags:
  - TYPE__/Concept/Procedure
  - PATH__/ComputerScience/Algorithms/DynamicProgramming
  - MODULE__/LocalAlignment
  - EXAM_PREP
foundational: 5
prereqs: 3
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

# Smith-Waterman algorithm

The **Smith–Waterman (SW)** algorithm (Smith & Waterman, 1981) computes the **optimal [[global vs local alignment|local]] alignment** of two sequences by [[dynamic programming]]. It reuses the entire [[Needleman-Wunsch algorithm|Needleman–Wunsch]] machinery — matrix, [[affine gap penalty|gap penalties]], [[traceback]] — and changes it in **exactly one place**. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=3|L4 p.3]]

**The one change — add `0` to the `max`.** The [[Needleman-Wunsch recurrence|recurrence]] gains a fourth option, **zero**, so a cell's score can never go negative:

$$S(i,j) = \max\big[\,\textbf{0},\ \ S(i-1,j-1)+s(a_i,b_j),\ \ S(i-k,j)-w(k),\ \ S(i,j-l)-w(l)\,\big]$$

A `0` means *"a worse-than-nothing alignment ending here is thrown away — start fresh."* That single tweak converts **global** alignment into **local**.

**Procedure (three phases — note the two differences from NW):**
1. **Initialize.** The 0-th row and column are **all 0** (not a cumulative gap penalty). Base scores come from a [[scoring matrix]] / [[substitution matrix]] (e.g. [[PAM (Point Accepted Mutation)|PAM250]] or [[BLOSUM matrix|BLOSUM]]).
2. **Fill.** Apply the recurrence; whenever all three "real" options are negative, the cell becomes **0**.
3. **[[traceback|Traceback]] — ① start at the global *maximum* cell** anywhere in the matrix (not the bottom-right corner), and **② stop at the first `0`**. The stretch between them is the optimal local alignment.

> [!Caution] Where NW and SW differ
> **NW**: 0-th row/col = cumulative gap penalty · no `0` in the `max` · traceback **corner → corner**. **SW**: 0-th row/col = `0` · `0` added to the `max` · traceback **max-cell → a `0`**. Same matrix, two small rules.

Because the local alignment starts at the max cell, it is **not** a sub-piece of the global one ([[exercise-smith-waterman-local|AL ⊄ AG]]). SW is available online as **EMBOSS `water`** at EBI (`emboss_water`); the global counterpart is `needle`. Local alignment is the basis of **database search** ([[global vs local alignment|BLAST]]).

# TLDR
Smith–Waterman finds the **optimal local alignment** by dynamic programming. It is Needleman–Wunsch with **one change**: add `0` as a fourth option in the `max` (scores can't go negative). Initialize the 0-th row/col to 0, then **trace back from the highest-scoring cell until you hit a 0**. EMBOSS `water` at EBI.

# Recitation Anchors
- **Optimal local alignment** by DP (Smith & Waterman, 1981)
- One change vs NW: **add `0` to the `max`** (no negative scores)
- `0` = "throw this away, start fresh"
- Init 0-th row/col = **0**; base scores from a substitution matrix
- Traceback: **start at the global max cell**, **stop at the first `0`**
- NW = corner→corner; SW = max-cell→`0`
- Local ⊄ global; EMBOSS **`water`** (vs `needle`); basis of BLAST

> [!Cool] Cool fact
> Smith–Waterman is **guaranteed** to find the optimal local alignment — but it's slow ($O(mn)$), which is precisely why fast *heuristics* like BLAST and FASTA were invented. The slowness was attacked head-on: **Farrar's 2007 "striped" SIMD** implementation sped exact Smith–Waterman up several-fold on ordinary CPUs, and GPU versions go far further — keeping the *optimal* algorithm usable at genome scale. [source](https://doi.org/10.1093/bioinformatics/btl582)

# Read aloud
KP.0.Definition: What Smith–Waterman does.
The Smith–Waterman algorithm, from 1981, finds the best local alignment of two sequences using dynamic programming. It reuses everything from Needleman–Wunsch — the matrix, the gap penalties, the traceback — and changes just one thing.

KP.1.Concept: The one change.
That one change is to add a fourth option, zero, to the maximum in the recurrence, so a cell's score can never drop below zero. A zero means: any alignment ending here that scores worse than nothing is thrown away, and we start fresh. That single tweak turns global alignment into local alignment.

KP.2.Procedure: Initialize and fill.
It runs in three phases. First, initialize: the top row and left column are all zeros — not a growing gap penalty as in Needleman–Wunsch. The base scores come from a substitution matrix like PAM or BLOSUM. Second, fill the matrix with the recurrence, and whenever all the real options come out negative, the cell just becomes zero.

KP.3.Procedure: Traceback, the local way.
Third, traceback, and this is the other big difference. You don't start at the bottom-right corner. You start at the single highest-scoring cell anywhere in the matrix, and you walk backwards until you hit a zero. The stretch between the maximum cell and that zero is your optimal local alignment.

KP.4.Connection: NW versus SW, and the tools.
So the two algorithms share one matrix but differ in three small rules: the initialization, the extra zero in the max, and where traceback starts and stops. Because the local alignment begins at the max cell, it is not just a slice of the global alignment. Online, Smith–Waterman is the EMBOSS tool called water, while the global version is needle, and local alignment is the foundation of database searching with BLAST.

KP.5.CoolFact: Optimal but slow — and accelerated.
And here's the cool part — Smith–Waterman is guaranteed to find the best local alignment, but it's slow, which is exactly why fast approximate tools like BLAST and FASTA were invented. People fought back against the slowness: in 2007 Michael Farrar's striped vectorized version sped the exact algorithm up several-fold on ordinary processors, and graphics-card versions go much further, keeping the optimal method usable even at genome scale.

# Question and Answer
Q. What does the Smith–Waterman algorithm compute?
A. The optimal local alignment of two sequences, by dynamic programming.

Q. What is the single change to the Needleman–Wunsch recurrence that makes it local?
A. Add a fourth option, `0`, inside the `max`, so no cell score can be negative.

Q. What does a `0` cell mean during the fill?
A. The alignment ending there scores worse than nothing, so it is discarded and a new local alignment can start fresh from there.

Q. How is SW initialized differently from NW?
A. SW sets the entire 0-th row and column to 0; NW fills them with a cumulative gap penalty.

Q. Where does SW traceback start and stop?
A. It starts at the highest-scoring cell anywhere in the matrix and stops at the first `0` — unlike NW, which goes corner to corner.

Q. Is the SW local alignment a sub-region of the NW global alignment?
A. Not necessarily — it follows a different path from the max cell, so it can differ entirely (AL ⊄ AG).

Q. What are the EMBOSS tool names for local and global alignment at EBI?
A. `water` for local (Smith–Waterman), `needle` for global (Needleman–Wunsch).

Q. Why were heuristics like BLAST/FASTA created if SW is optimal?
A. SW is $O(mn)$ and too slow for large database searches; BLAST/FASTA trade some accuracy for speed.
