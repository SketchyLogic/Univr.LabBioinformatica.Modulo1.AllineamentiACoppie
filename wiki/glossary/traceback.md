---
tags:
  - TYPE__/Concept/Procedure
  - PATH__/ComputerScience/Algorithms/DynamicProgramming
  - MODULE__/DynamicProgrammingAlignment
foundational: 4
prereqs: 3
density: 3
value: 4
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# traceback

**Traceback** is the second half of [[Needleman-Wunsch algorithm|Needleman–Wunsch]]: once the matrix is filled, you recover the actual **alignment** by walking **backwards** from the last cell (the bottom-right corner for global NW; the **maximum-scoring** cell for local [[Smith-Waterman algorithm|Smith–Waterman]]). The fill phase finds the optimal *score*; traceback turns that score into the optimal *alignment*. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=9|L3 p.9]]

**How it works:**
- Start at the **bottom-right** cell (it holds the optimal global score).
- At each cell, move to the **predecessor that produced its value** in the [[Needleman-Wunsch recurrence]] — diagonal, up, or left.
- Each step **emits a column** of the alignment:
  - **diagonal** → align the two residues (a [[match mismatch gap|match/mismatch]]),
  - **up** → a gap in one sequence,
  - **left** → a gap in the other.
- Continue until you reach the **top-left** cell; reverse the emitted columns to read the alignment left-to-right.

This is possible **only because** the problem has **[[optimal substructure]]** (see also [[dynamic programming]]): *"removing residues one by one from the end, the alignment must stay optimal, so the path can be reconstructed backwards."* Each cell effectively **memorised** which neighbour gave its best score.

> [!Caution] Ties = multiple optimal alignments
> When two predecessors give the same max, there are **multiple** equally-optimal alignments. The lecture's rule — *"choose the one with the higher final score"* — resolves the path, but real tools may report several co-optimal alignments.

# TLDR
Traceback is the second half of Needleman–Wunsch: starting at the bottom-right cell, walk **backwards** along each cell's best predecessor (diagonal = paired column, up/left = a gap) to the top-left, then reverse. The fill gives the optimal *score*; traceback turns it into the optimal *alignment*.

# Recitation Anchors
- Fill → optimal **score**; traceback → optimal **alignment**
- Start bottom-right (optimal score) → end top-left
- Diagonal = paired column; up/left = a gap
- Reverse emitted columns to read left-to-right
- Valid because of **optimal substructure**; cells memorise best predecessor
- Ties → multiple co-optimal alignments

> [!Cool] Cool fact
> Storing a "back-pointer" in every cell is what makes traceback O(L) fast, but it costs O(mn) memory. **Hirschberg's algorithm** cleverly recomputes the path in **linear space** by divide-and-conquer — essential for aligning sequences too long to hold a full matrix in memory. [source](https://doi.org/10.1145/360825.360861)

# Read aloud
KP.0.Definition: What traceback is.
Traceback is the second half of Needleman–Wunsch. Once the scoring matrix is completely filled in, you recover the actual alignment by walking backwards from the final cell. The filling phase gives you the best score; traceback turns that score into the best alignment.

KP.1.Procedure: How to walk back.
You start at the bottom-right cell, which holds the optimal score. At each cell, you step to whichever neighbour produced its value during the fill — the diagonal, the one above, or the one to the left. Every step writes one column of the alignment: a diagonal step pairs the two residues, a step from above puts a gap in one sequence, a step from the left puts a gap in the other. You keep going until you reach the top-left corner, then reverse what you wrote to read the alignment forwards.

KP.2.Connection: Why it works at all.
This only works because the problem has optimal substructure. As the lecture puts it, if you peel residues off the end one by one, the alignment must stay optimal — which means the path can be rebuilt backwards. In effect, each cell remembered which neighbour gave it its best score.

KP.3.Concept: Ties and multiple answers.
A subtlety: when two neighbours give the same best value, there's more than one equally-good alignment. The lecture's rule is to pick the one with the higher final score, but real software may simply report several co-optimal alignments.

KP.4.CoolFact: The memory trick.
And here's the cool part — keeping a back-pointer in every cell makes traceback fast, but it uses memory proportional to the product of the two lengths. Hirschberg's algorithm cleverly recomputes the path using only linear memory, by divide and conquer — which is what lets us align sequences too long to ever fit a full matrix in memory.

# Question and Answer
Q. What does traceback produce that the fill phase does not?
A. The actual optimal alignment (the path), whereas filling produces only the optimal score.

Q. Where does traceback start and end?
A. It starts at the bottom-right cell (optimal score) and ends at the top-left cell.

Q. What does each move emit during traceback?
A. Diagonal → a paired column (match/mismatch); up → a gap in one sequence; left → a gap in the other.

Q. Which property makes traceback valid?
A. Optimal substructure — sub-alignments of an optimal alignment are themselves optimal, so the path can be rebuilt backwards.

Q. What happens when two predecessors tie for the max?
A. There are multiple co-optimal alignments; a rule (or the software) chooses among them.

Q. What does Hirschberg's algorithm improve about traceback?
A. It recovers the path in linear space instead of O(mn) memory, enabling very long alignments.
