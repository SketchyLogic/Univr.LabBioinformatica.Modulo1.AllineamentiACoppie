---
tags:
  - TYPE__/Concept/Procedure
  - PATH__/ComputerScience/Algorithms/DynamicProgramming
  - MODULE__/DynamicProgrammingAlignment
  - EXAM_PREP
  - MATH_UNRAVELING
foundational: 4
prereqs: 4
density: 4
value: 5
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Needleman-Wunsch recurrence

The heart of [[Needleman-Wunsch algorithm|Needleman–Wunsch]] is the rule that recomputes each cell's score from cells already filled. In the lecture's notation: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=10|L3 p.10]]

$$S(i,j) = s(a_i,b_j) + \max\big[\,S(i-1,\,j-1),\ S(i-k,\,j-1),\ S(i-1,\,j-l)\,\big]$$

## Unraveling, piece by piece

- **$S(i,j)$** — the score we are *computing* for the cell at row $i$, column $j$. This is the best score of any alignment ending with residues $a_i$ and $b_j$ paired.
- **$s(a_i,b_j)$** — the **base score** for pairing residue $a_i$ (row) with $b_j$ (column), read from the [[scoring matrix]] (or simply 1/0 for identical/different in the basic version). This is the reward for *this* cell's match/mismatch.
- **$\max[\dots]$** — choose the **best predecessor** already computed. The three candidates are the three ways to *arrive* at $(i,j)$:
  - **$S(i-1,j-1)$** — come from the **diagonal** neighbour: align $a_i$ with $b_j$ (a [[match mismatch gap|match or mismatch]], **no gap**).
  - **$S(i-k,j-1)$** — come from **above** ($k$ rows up): a **gap in the top sequence** (vertical move, an indel of length related to $k$).
  - **$S(i-1,j-l)$** — come from the **left** ($l$ columns back): a **gap in the side sequence** (horizontal move, an indel of length $l$).

> [!Hint] In words
> *New cell score = reward for pairing these two residues **+** the best score among the three legal ways to have gotten here (diagonal = no gap, vertical/horizontal = a gap).* Taking the **max** is the single "best decision" made at every step; remembering *which* neighbour won enables [[traceback]].

This recurrence is the concrete embodiment of **optimal substructure** (see [[dynamic programming]]): $S(i,j)$ is built only from already-optimal smaller cells. Sweeping it over the whole matrix fills every cell; the bottom-right cell then holds the **optimal global score**.

> [!Example] Basic init version
> In the worked example the recurrence simplifies to "add the current cell's 1/0 to the best of its up-left neighbours", which is why going to cell *(4,4)* *"increases the score by 2"* and the corner reaches 8. See [[exercise-needleman-wunsch-worked]].

# TLDR
Each cell's score is its base reward plus the best of three predecessors: $S(i,j) = s(a_i,b_j) + \max[\,\text{diagonal}, \text{up}, \text{left}\,]$ — diagonal = no gap, up/left = a gap. Taking the max is the single best decision per step; remembering which neighbour won enables traceback.

# Recitation Anchors
- $S(i,j) = s(a_i,b_j) + \max[\,S(i{-}1,j{-}1),\ S(i{-}k,j{-}1),\ S(i{-}1,j{-}l)\,]$
- $s(a_i,b_j)$ = base reward from scoring matrix (or 1/0)
- **Diagonal** = no gap (match/mismatch)
- **Up** = gap in top sequence; **Left** = gap in side sequence
- max = best decision; remember the winner → traceback
- Bottom-right cell = optimal global score
- Add a fourth option "0" → Smith–Waterman (local alignment)

> [!Cool] Cool fact
> The diagonal-vs-gap choice is the whole ballgame: the closely related **Smith–Waterman** algorithm changes this recurrence in just **one** place — it adds a fourth option, `0`, forbidding negative scores — and that single tweak turns *global* alignment into *local* alignment. [source](https://doi.org/10.1016/0022-2836(81)90087-5)

# Read aloud
KP.0.Definition: What the recurrence is for.
At the core of Needleman–Wunsch is one rule that recalculates each cell's score from cells already filled in. Let me unpack what it says, piece by piece.

KP.1.Concept: The cell being computed.
The quantity on the left, S of i and j, is the score we're working out for the cell in row i, column j. Think of it as the best possible score for any alignment that ends with these two particular residues paired together.

KP.2.Concept: The base reward.
The first term on the right is the base score for pairing this row residue with this column residue, looked up in the scoring matrix — or just a one or zero for identical or different in the simple version. That's the reward earned by this cell itself.

KP.3.Procedure: The three ways in.
Then comes the maximum of three options, which are the three ways you could have arrived at this cell. Coming from the diagonal neighbour means you paired the two residues with no gap. Coming from above means you opened a gap in the top sequence. Coming from the left means you opened a gap in the side sequence. You take whichever of these three already-computed scores is largest.

KP.4.Connection: One best decision per step.
So in plain words: the new cell's score is the reward for pairing these two residues, plus the best of the three legal ways you could have gotten here — diagonal for no gap, vertical or horizontal for a gap. Taking the maximum is the single best decision made at every step, and remembering which neighbour won is what later lets you trace the alignment back. This is optimal substructure made concrete: each cell is built only from already-optimal smaller cells, and the bottom-right corner ends up holding the best global score.

KP.5.CoolFact: One tweak makes it local.
And here's the cool part — that choice between diagonal and gap is the whole game. The closely related Smith–Waterman algorithm changes this rule in just one spot: it adds a fourth option, zero, which forbids negative scores. That single change converts global alignment into local alignment.

# Question and Answer
Q. What does S(i,j) represent in the recurrence?
A. The best score of any alignment ending with residues $a_i$ and $b_j$ paired — the value being computed for cell (i,j).

Q. What does the term $s(a_i,b_j)$ contribute?
A. The base score for pairing the row residue with the column residue, taken from the scoring matrix (or 1/0 in the basic version).

Q. What do the three terms inside the max correspond to?
A. Diagonal $S(i-1,j-1)$ = no gap (match/mismatch); $S(i-k,j-1)$ = gap in the top sequence; $S(i-1,j-l)$ = gap in the side sequence.

Q. Why take the maximum of the predecessors?
A. To make the locally best decision at each step, guaranteeing the cell's optimal score given already-optimal neighbours.

Q. How does the recurrence embody optimal substructure?
A. S(i,j) is built solely from already-optimal smaller cells, so the global optimum assembles from sub-optima.

Q. What one change to this recurrence yields Smith–Waterman (local alignment)?
A. Add a fourth option, 0, inside the max, so scores can't go negative.
