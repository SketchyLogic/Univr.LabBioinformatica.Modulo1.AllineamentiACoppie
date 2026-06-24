---
tags:
  - TYPE__/Executable/Exercise
  - PATH__/ComputerScience/Algorithms/DynamicProgramming
  - MODULE__/DynamicProgrammingAlignment
  - EXAM_PREP
foundational: 4
prereqs: 3
density: 3
value: 5
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# exercise-needleman-wunsch-worked

**Tool**: pen & paper (or EMBOSS `needle`) · **Source**: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=9|L3 slides 33–36]]

## Task
Align the two sequences below by hand with [[Needleman-Wunsch algorithm|Needleman–Wunsch]], using the basic scoring (identity init: `1` if residues match, `0` otherwise; choose the best up-left predecessor at each step). Then read off the optimal alignment and its % identity.

```
S1 (columns): A D C N Y R Q C L C R P M
S2 (rows):    A Y C Y N R   C K C R D P
```

## Walkthrough
1. **Build the matrix.** 13 columns (S1) × 12 rows (S2). Initialize each cell to `1` if its column residue equals its row residue, else `0`.
2. **Fill it.** Going column by column, replace each cell *(i,j)* with its init value **plus** the maximum of its already-computed up/left/diagonal predecessors (the [[Needleman-Wunsch recurrence]]). Watch how accumulated scores climb toward the bottom-right.
   - e.g. moving toward *(4,4)* the running alignment `CN/CY → CNY/...` gains; the lecture notes the best route "increases the score of (4,4) by 2".
3. **Reach the corner.** The bottom-right cell ends at **8**.
4. **[[traceback|Trace back]].** From the bottom-right, follow the stored best moves to the top-left; diagonal = paired residues, vertical/horizontal = a gap.

## Expected answer
The optimal alignment (one of the co-optimal paths shown in the slides):

```
A D C N Y R Q C L C R P M
A Y C - Y N R - C K C R D P   →  matches scored: 1 0 1 0 1 0 1 0 1 1 0 1 0 = 8
```

- **Final score = 8**, equal to the number of identical residues along the path.
- **% identity = 8 / 15 = 0.53 = 53%** — note the denominator **15** is the **alignment length (including gaps)**, not the original 13, per [[sequence identity and similarity percent]].

## Concepts exercised
- [[Needleman-Wunsch algorithm]]
- [[Needleman-Wunsch recurrence]]
- [[traceback]]
- [[sequence identity and similarity percent]]
- [[dynamic programming]]

# TLDR
Align two sequences by hand with basic Needleman–Wunsch (init 1/0, each cell += best up/left/diagonal predecessor), reach the corner score **8**, trace back, and report **8/15 = 53% identity** — denominator is the *alignment length* (15), not the original 13.

# Recitation Anchors
- Init: **1** if residues match, else **0**
- Fill: cell = init + max(up, left, diagonal)
- Corner score = **8** = number of identical residues on the path
- Traceback: diagonal = pair, vertical/horizontal = gap
- % identity = 8/15 = **53%** (denominator = alignment length 15, not 13)
- Ties → multiple co-optimal alignments

> [!Cool] Cool fact
> Doing NW by hand is a rite of passage, but the matrix grows fast: aligning two 1,000-residue proteins means filling **a million cells** — which is exactly why the algorithm was a landmark of practical computing, not just theory. [source](https://doi.org/10.1016/0022-2836(70)90057-4)

# Read aloud
KP.0.Procedure: What the exercise asks.
This exercise has you align two short sequences by hand using Needleman–Wunsch. You start with the simple scoring: put a one in a cell if its row and column letters match, and a zero if they don't.

KP.1.Procedure: Filling the grid.
Then you fill the grid. Going column by column, you replace each cell with its starting value plus the best of the neighbours you've already computed — the one above, the one to the left, or the diagonal one. As you sweep across, the scores accumulate and grow toward the bottom-right corner. At one point, taking the best route into a particular cell bumps its score up by two.

KP.2.Procedure: Reaching the corner and tracing back.
Eventually the bottom-right cell lands on eight. Then you trace back: from that corner you follow the best moves you stored, all the way to the top-left. A diagonal step pairs two residues; a vertical or horizontal step is a gap.

KP.3.Numbers: The answer.
The final score is eight, which equals the number of identical residues along your path. To get percent identity you divide eight by fifteen — and fifteen is the alignment's length including the gaps, not the original thirteen. That gives fifty-three percent identity.

KP.4.CoolFact: A million cells.
And here's the cool part — doing this by hand is a rite of passage, but the grid balloons quickly. Aligning two thousand-residue proteins means filling a million cells, which is exactly why this algorithm was such a milestone for practical computing.

# Question and Answer
Q. What initialization rule does the basic NW use here?
A. Put 1 in a cell if its row and column residues are identical, 0 otherwise.

Q. How is each cell's final score computed during the fill?
A. Its init value plus the maximum of its already-computed predecessors (up/left/diagonal), per the recurrence.

Q. What final corner score does this example reach?
A. 8 — equal to the number of identical residues along the optimal path.

Q. What % identity results, and what is the denominator?
A. 8/15 = 53%; the denominator is the alignment length (15, including gaps), not the original 13.

Q. During traceback, what does a diagonal move versus a vertical move mean?
A. Diagonal = the two residues are paired (match/mismatch); vertical (or horizontal) = a gap in one sequence.

Q. Why might your alignment differ slightly from a classmate's yet still be correct?
A. Ties in the max produce multiple co-optimal alignments with the same score.
