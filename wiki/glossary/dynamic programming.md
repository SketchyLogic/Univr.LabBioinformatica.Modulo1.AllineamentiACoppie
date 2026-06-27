---
tags:
  - TYPE__/Concept/Definition
  - PATH__/ComputerScience/Algorithms/DynamicProgramming
  - MODULE__/DynamicProgrammingAlignment
foundational: 5
prereqs: 3
density: 3
value: 5
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# dynamic programming

**Dynamic programming (DP)** is an algorithmic strategy that solves a big problem by **building it up from optimal solutions to overlapping sub-problems**, storing each sub-result so it is never recomputed. In alignment it is the engine of [[Needleman-Wunsch algorithm|Needleman–Wunsch]]. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=10|L3 p.10]]

Why it's needed for alignment: the number of possible alignments of two sequences is **astronomically large** (it grows combinatorially with length), so brute-force enumeration is hopeless. DP finds the **provably optimal** alignment **without** computing all of them — a series of local decisions, one per step, each picking the best-scoring move.

## Optimal substructure
DP works only when the problem has **[[optimal substructure]]**: *an optimal solution is composed of optimal sub-solutions.* For alignment this is the lecture's "**IMPORTANT**" rule: **an optimal alignment is always made of optimal sub-alignments.** [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=8|L3 p.8]] (The dedicated entry [[optimal substructure]] gives the cut-and-paste proof and the alignment-specific three-way ending.)

> [!Hint] The test for optimal substructure
> Peel residues off the **end** of an optimal alignment one at a time; what remains must *still* be optimal for the shorter sequences. If that holds, you can build the full optimum from smaller optima — and reconstruct the path by working backwards ([[traceback]]).

This is exactly why each cell can be filled from its neighbors via a recurrence (see [[Needleman-Wunsch recurrence]]): the best score to reach cell *(i,j)* depends only on the best scores already computed for cells before it. The principle generalizes far beyond biology.

# TLDR
Dynamic programming solves a big problem by **combining optimal solutions of overlapping sub-problems** (and storing them so none is recomputed). It finds the *provably optimal* alignment without enumerating the astronomically many possibilities — possible because alignment has **optimal substructure**.

# Recitation Anchors
- Build the big optimum from stored **optimal sub-solutions**
- Needed because the number of alignments grows combinatorically
- Requires **optimal substructure**
- Alignment rule: optimal alignment = optimal sub-alignments
- Test: peel residues off the end → remainder must stay optimal
- Each cell filled from its neighbors (the recurrence)

> [!Cool] Cool fact
> The name has nothing to do with computer code: Richard **Bellman** coined "dynamic programming" in the 1950s partly because "programming" meant *planning/scheduling* and the word sounded impressive to a research-averse Secretary of Defense — he deliberately picked a name no one "could possibly object to." [source](https://en.wikipedia.org/wiki/Dynamic_programming#History)

# Read aloud
KP.0.Definition: What dynamic programming is.
Dynamic programming is a strategy for solving a big problem by building it up out of the best solutions to smaller, overlapping pieces — and storing each piece so you never have to work it out twice. In sequence alignment, it's the engine inside the Needleman–Wunsch algorithm.

KP.1.Concept: Why alignment needs it.
Here's why we need it. The number of ways to align two sequences is astronomically large; it explodes as the sequences get longer, so trying them all is hopeless. Dynamic programming finds the provably best alignment without ever computing them all. It makes one local decision at a time, each step choosing the best-scoring move.

KP.2.Concept: Optimal substructure.
Dynamic programming only works when a problem has what's called optimal substructure: the best overall solution is made up of best sub-solutions. The lecture flags this as the important rule — an optimal alignment is always built from optimal sub-alignments.

KP.3.Connection: The test and the payoff.
There's a neat test for it. Take an optimal alignment and peel residues off the end, one by one. What's left must still be the optimal alignment of the shorter sequences. If that's true, you can construct the full optimum from smaller optima — and later walk backwards through your stored choices to recover the actual alignment, a step called traceback. This is exactly why each cell of the matrix can be filled from its neighbours: the best way to reach a cell depends only on the best scores already worked out for the cells before it.

KP.4.CoolFact: The name is a marketing trick.
And here's the cool part — the name "dynamic programming" has nothing to do with computer code. Richard Bellman invented it in the 1950s, partly because "programming" then meant planning, and partly because it sounded impressive enough that a research-skeptical Secretary of Defense couldn't possibly object to it.

# Question and Answer
Q. Define dynamic programming.
A. An algorithmic strategy that solves a problem by combining optimal solutions of overlapping sub-problems, storing sub-results to avoid re-computation.

Q. Why can't we just enumerate all alignments?
A. The number of possible alignments grows combinatorically with sequence length — astronomically large, so brute force is infeasible.

Q. What property must a problem have for DP to apply?
A. Optimal substructure — an optimal solution is composed of optimal sub-solutions.

Q. State the alignment version of optimal substructure.
A. An optimal alignment is always composed of optimal sub-alignments.

Q. How can you test for optimal substructure in an alignment?
A. Remove residues from the end one at a time; the remainder must stay optimal for the shorter sequences.

Q. Does NW guarantee the optimal alignment even though it skips most alignments? Explain.
A. Yes — by exploiting optimal substructure it provably reaches the optimum without enumerating all alignments.
