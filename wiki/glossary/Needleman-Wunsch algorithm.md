---
tags:
  - TYPE__/Concept/Procedure
  - PATH__/ComputerScience/Algorithms/DynamicProgramming
  - MODULE__/DynamicProgrammingAlignment
  - EXAM_PREP
foundational: 5
prereqs: 3
density: 4
value: 5
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Needleman-Wunsch algorithm

The **Needleman–Wunsch (NW)** algorithm (1970) computes the **globally optimal** [[pairwise alignment]] of two sequences by [[dynamic programming]]. Unlike a [[dot plot]], it explicitly handles [[match mismatch gap|indels]]. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=8|L3 p.8–10]]

**Idea:** lay the two sequences on a matrix (one along the top, one down the side). An alignment is a **path** through the matrix connecting paired cells. NW finds the highest-scoring path.

**Allowed moves along the path.** Each step is one of **three** moves — diagonal *and* orthogonal are both allowed:
- **Diagonal** (↘, from *(i−1, j−1)*) — align the two residues here: a [[match mismatch gap|match/mismatch]], **no gap**. This is the default step.
- **Vertical** (↓) — a **gap in the top sequence** (an indel).
- **Horizontal** (→) — a **gap in the side sequence** (an indel).

> Move in one direction add on the orthogonal sequence

These are exactly the three options inside the [[Needleman-Wunsch recurrence|recurrence's `max`]]. The diagonal is the *most common* move — it pairs residues — while the orthogonal moves are what introduce gaps; on a [[dot plot patterns visualized|dot-plot grid]] an orthogonal step is what makes a diagonal "shift" (the indel signature).

> [!Caution] "Forward only" ≠ "no diagonals"
> The rule that the path goes *forward only* refers to **direction** — it always advances toward the bottom-right corner — **not** to forbidding diagonal steps. A diagonal move is a forward move too.

**Procedure (three phases):**
1. **Initialize.** Fill the matrix with a base score per cell — in the lecture's simplest version, `1` if the row/column residues are identical, `0` otherwise (a more refined init uses a [[scoring matrix]] or sliding-window + scoring-matrix).
2. **Fill (score recalculation).** Sweep one **column at a time, top→bottom, left→right**, replacing each cell *(i,j)* with its own base score **plus the best reachable predecessor**, per the [[Needleman-Wunsch recurrence]]. This propagates accumulated best scores toward the bottom-right.
3. **[[traceback|Traceback]].** From the bottom-right cell, walk **backwards** along the stored best choices to reconstruct the optimal alignment.

**Practical rules** [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=8|L3 p.8]]:
- The path has a **direction** and goes **forward only** — never backtracks while filling (this constrains *direction*, not *move type* — see **Allowed moves** above).
- Seek the path with the **most identical residues** and the **fewest indels**.
- Account for amino-acid **similarity** (evolutionary meaning), via the scoring matrix.
- Relies on **[[optimal substructure]]**: optimal alignment = optimal sub-alignments (see [[dynamic programming]]); the proof that NW returns the *global* optimum is in [[Needleman-Wunsch correctness]].

The worked example (`ADCNYRQCLCRPM` vs `AYCYNRCKCRDP`) terminates at the bottom-right with total **8 = 8/15 = 53% identity** — the score there equals the number of identical residues. See the exercise [[exercise-needleman-wunsch-worked]]. NW's two limitations — a flat gap model and global-only scope — are lifted in L4 by the [[affine gap penalty]] and the [[Smith-Waterman algorithm]] (local). NW is available online as **EMBOSS `needle`** at EBI.

# TLDR
Needleman–Wunsch finds the **globally optimal** alignment of two sequences by dynamic programming, in three phases — **initialize, fill (recurrence), traceback** — and explicitly handles indels. An alignment is the highest-scoring path through the matrix; the algorithm is O(mn).

# Recitation Anchors
- **Global** optimal alignment by dynamic programming (1970)
- Alignment = highest-scoring **path** through the matrix
- Three phases: **initialize → fill → traceback**
- Fill: each cell = base score + best predecessor
- Three move types: **diagonal** (no gap) + **vertical/horizontal** (gap)
- Path is forward-only (direction, not move type); most identities, fewest indels
- **O(mn)** time & space; available as EMBOSS `needle`

> [!Cool] Cool fact
> NW is **O(mn)** in time and memory — quadratic — which becomes painful for whole genomes; this very limit drove later breakthroughs like the Hirschberg linear-space trick and the heuristic shortcuts behind **BLAST**. The original [1970 paper](https://doi.org/10.1016/0022-2836(70)90057-4) has been cited tens of thousands of times. [source](https://doi.org/10.1016/0022-2836(70)90057-4)

# Read aloud
KP.0.Definition: What Needleman–Wunsch does.
The Needleman–Wunsch algorithm, from 1970, finds the single best alignment of two sequences across their entire length, using dynamic programming. Unlike a dot plot, it deals with insertions and deletions head-on.

KP.1.Concept: The matrix-and-path picture.
The idea is to lay the two sequences on a grid, one across the top and one down the side. Any alignment corresponds to a path through that grid connecting paired-up cells. Needleman–Wunsch hunts for the path with the highest total score. That path takes three kinds of step: a diagonal move, which pairs the two residues with no gap, and the two orthogonal moves — down or right — which each open a gap. So diagonal steps are not only allowed, they're the usual move; the orthogonal ones are what add insertions and deletions. And when the rule says the path goes forward only, that's about direction — always heading toward the bottom-right — not about banning diagonals.

KP.2.Procedure: Initialize.
It works in three phases. First, initialize. Fill every cell with a base score. In the simplest version from the lecture, that's a one if the row and column residues are identical and a zero otherwise. A more refined version uses a scoring matrix instead.

KP.3.Procedure: Fill the matrix.
Second, fill. Sweep through the grid, one column at a time, top to bottom and left to right. Replace each cell with its own base score plus the best score you can reach it from. This pushes the accumulated best scores steadily toward the bottom-right corner.

KP.4.Procedure: Traceback.
Third, traceback. Starting from the bottom-right cell, walk backwards along the best choices you stored, and that reconstructs the optimal alignment.

KP.5.Concept: The practical rules.
A few rules keep it honest. The path moves forward only and never backtracks while filling. You're looking for the path with the most identical residues and the fewest gaps. You weigh in amino-acid similarity through the scoring matrix, for evolutionary meaning. And the whole thing rests on optimal substructure — the best alignment is built from best sub-alignments. In the worked example, the path ends in the corner with a score of eight, which is eight out of fifteen, or fifty-three percent identity.

KP.6.CoolFact: Quadratic cost and its legacy.
And here's the cool part — Needleman–Wunsch needs time and memory proportional to the product of the two sequence lengths. That quadratic cost gets painful for whole genomes, and it's exactly what drove later inventions: clever linear-space versions and the fast heuristics behind BLAST.

# Question and Answer
Q. What does the Needleman–Wunsch algorithm compute, and via what technique?
A. The globally optimal alignment of two sequences, using dynamic programming.

Q. What are the three phases of NW?
A. Initialize the matrix, fill it (score recalculation via the recurrence), and trace back to recover the alignment.

Q. How is an alignment represented in the NW matrix?
A. As a path through the matrix connecting paired (aligned) cells; the best alignment is the highest-scoring path.

Q. In which direction is the matrix filled, and may the path backtrack?
A. Filled forward (e.g. column by column, top→bottom, left→right); the path moves forward only and never backtracks during filling.

Q. Are the path's moves only orthogonal, or are diagonal moves allowed too?
A. Both: three move types — diagonal (pair the residues, no gap), vertical (gap in the top sequence), horizontal (gap in the side sequence). The diagonal is the default move; orthogonal moves insert gaps.

Q. Does "the path goes forward only" forbid diagonal steps?
A. No — "forward only" constrains *direction* (always toward the bottom-right), not move type. A diagonal step is itself a forward step.

Q. What does NW handle that a dot plot does not?
A. Indels (gaps) as explicit alignment operations.

Q. What is NW's time/space complexity, and why does it matter?
A. O(mn) (quadratic), which becomes costly for long sequences/genomes and motivated faster methods like BLAST.

Q. In the worked example, what final score is reached and what identity does it correspond to?
A. 8, i.e. 8/15 ≈ 53% identity (the corner score equals the number of identical residues there).
