---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Key Concepts — Dynamic Programming Alignment

**Summary**: Exam-ready review sheet for [[dynamic-programming-alignment|Arc 3]]. The NW procedure, its recurrence, and the dynamic-programming logic that makes it optimal.

---

## Definitions
- **[[dynamic programming]]** — solve a problem from optimal sub-solutions, stored to avoid re-computation.
- **Optimal substructure** — an optimal alignment is composed of optimal sub-alignments.
- **[[Needleman-Wunsch algorithm]]** — 1970 DP algorithm for the globally optimal alignment (handles indels).
- **[[traceback]]** — walk back from the last cell to recover the alignment.

## Procedure (NW skeleton)
1. **Initialize** the matrix (1 if residues identical, 0 otherwise — or use a [[scoring matrix]]).
2. **Fill**: column by column, each cell = its base score + best predecessor (the recurrence).
3. **Traceback**: from bottom-right → top-left; diagonal = paired residues, up/left = gap.
**Rules:** forward-only path; maximize identities, minimize indels; account for similarity.

## Key formula
$$S(i,j) = s(a_i,b_j) + \max\big[\,S(i-1,j-1),\ S(i-k,j-1),\ S(i-1,j-l)\,\big]$$
- $s(a_i,b_j)$ = base reward for pairing the two residues.
- diagonal $S(i-1,j-1)$ = no gap; $S(i-k,j-1)$ = gap in top seq; $S(i-1,j-l)$ = gap in side seq.
- the **max** = the single best decision per step. See [[Needleman-Wunsch recurrence]].

## Questions & answers
Q. Why not enumerate all alignments? → Their number explodes combinatorially with length.
Q. What property makes DP work? → Optimal substructure.
Q. Does NW guarantee optimality? → Yes, without computing all alignments.
Q. What do the three terms in the max mean? → Diagonal = match/mismatch (no gap); up = gap in one seq; left = gap in the other.
Q. What does traceback produce vs the fill phase? → The alignment (path) vs only the optimal score.
Q. One change that turns NW into Smith–Waterman? → Add a 4th option `0` in the max (local alignment).
Q. NW complexity? → O(mn) time and space.

## Key facts / numbers
- Worked example: final score **8** = 8/15 = **53%** identity.
- Online tool: **EMBOSS `needle`** at EBI (`water` = local / Smith–Waterman).
- Practice with [[exercise-needleman-wunsch-worked]].
