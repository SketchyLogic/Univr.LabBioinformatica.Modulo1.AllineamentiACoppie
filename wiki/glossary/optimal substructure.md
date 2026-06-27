---
tags:
  - TYPE__/Concept/Argument
  - PATH__/ComputerScience/Algorithms/DynamicProgramming
  - MODULE__/DynamicProgrammingAlignment
  - EXAM_PREP
foundational: 4
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

# optimal substructure

**Optimal substructure** is the property a problem must have for [[dynamic programming]] to be valid: *an optimal solution to the whole problem is built from optimal solutions to its sub-problems.* It is the lecture's "**IMPORTANT**" rule, and it is the precise reason [[Needleman-Wunsch algorithm|Needleman–Wunsch]] is allowed to find the best alignment without ever enumerating all alignments. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=8|L3 p.8]]

**The alignment statement:** *an optimal alignment is always composed of optimal sub-alignments.* Concretely, let $S(i,j)$ be the best score for aligning the prefixes $a_{1..i}$ and $b_{1..j}$. An optimal alignment of those prefixes must **end** in exactly one of three ways — and whichever it is, removing that last column leaves an **optimal** alignment of the shorter prefixes:

- ends in a **diagonal** step (pair $a_i$ with $b_j$) → the rest is optimal for $a_{1..i-1}, b_{1..j-1}$;
- ends in a **gap in the top sequence** → the rest is optimal for $a_{1..i}, b_{1..j-1}$;
- ends in a **gap in the side sequence** → the rest is optimal for $a_{1..i-1}, b_{1..j}$.

Because of this, the best full score depends *only* on three already-solved smaller cells — which is exactly the [[Needleman-Wunsch recurrence]]. Optimal substructure is the bridge from *"compare these two sequences"* to *"fill a table cell by cell"*.

> [!Hint] The peel test
> To check optimal substructure in an alignment: **peel residues off the end** one at a time. If what remains must *always still be optimal* for the shorter sequences, the property holds — and you can both build the optimum forward (the fill) and rebuild the path backward ([[traceback]]).

**Why it justifies DP.** The number of possible alignments grows combinatorically, so brute force is hopeless. Optimal substructure collapses that explosion: instead of comparing whole alignments, each cell makes **one local best decision** from optimal neighbors, and the $O(mn)$ table holds every sub-answer exactly once. Without this property, a greedy/local choice could not be trusted, and DP would give the wrong answer.

> [!Caution] Necessary, not sufficient
> Optimal substructure alone does **not** prove the procedure finds the best alignment — it must be paired with *exhaustive choice* (the recurrence's `max` covers every possible last column) and an induction. See [[Needleman-Wunsch correctness]].

# Argument
A **cut-and-paste** proof (the standard way to prove optimal substructure):

1. Let $A$ be an *optimal* alignment of $a_{1..i}$ and $b_{1..j}$, and let $c$ be its **last column** (a diagonal pair, or a gap).
2. Remove $c$, leaving $A'$, an alignment of the corresponding shorter prefixes.
3. **Suppose $A'$ were not optimal.** Then some alignment $B'$ of those same prefixes scores strictly higher.
4. Re-append column $c$ to $B'$: this is a valid alignment of the original prefixes scoring $\text{score}(B') + \text{score}(c) > \text{score}(A') + \text{score}(c) = \text{score}(A)$.
5. That contradicts $A$ being optimal. Therefore $A'$ **must** be optimal. ∎

The key is that the score is **additive** over columns and the last column's cost is **independent** of how the prefix was aligned — so an improvement to the prefix would carry straight through to the whole.

# TLDR
Optimal substructure means an optimal alignment is made of optimal sub-alignments: its last column can be peeled off to leave an optimal alignment of the shorter prefixes. Because the score is additive, the best full score depends only on three smaller optimal cells — which is what licenses the [[Needleman-Wunsch recurrence]] and makes [[dynamic programming]] correct.

# Recitation Anchors
- Optimal solution = built from **optimal sub-solutions**
- Alignment form: optimal alignment = optimal **sub-alignments**
- Optimal alignment ends 3 ways: diagonal / top-gap / side-gap
- Peel last column → remainder must stay optimal (the test)
- Holds because score is **additive** + last column **independent** of prefix
- Proof technique: **cut-and-paste** (contradiction)
- This is what turns "compare sequences" into "fill a table" (DP)

> [!Cool] Cool fact
> Optimal substructure is not automatic — and its absence has teeth. **Shortest** simple path in a graph has it (so it's easy, e.g. Dijkstra), but **longest** simple path does *not*: a longest path is not made of longest sub-paths, and the problem is famously **NP-hard**. The same structural property that makes alignment tractable is exactly what separates easy problems from intractable ones. [source](https://en.wikipedia.org/wiki/Optimal_substructure)

# Read aloud
KP.0.Definition: What optimal substructure is.
Optimal substructure is the property a problem needs before dynamic programming is allowed to work on it. It says that an optimal solution to the whole problem is built out of optimal solutions to its smaller sub-problems. The lecture marks this as the important rule, and it's the exact reason Needleman–Wunsch can find the best alignment without ever trying them all.

KP.1.Concept: The alignment version.
For alignment it reads: an optimal alignment is always made of optimal sub-alignments. Think about how an optimal alignment of two prefixes must end. It ends in one of just three ways — either the last two residues are paired on the diagonal, or there's a gap in the top sequence, or there's a gap in the side sequence. And whichever way it ends, if you strip off that last column, what's left must itself be an optimal alignment of the slightly shorter prefixes.

KP.2.Connection: Why this gives the recurrence.
That's a powerful constraint. It means the best score for a cell depends only on three already-solved smaller cells, one for each of those three endings. That is precisely the Needleman–Wunsch recurrence. Optimal substructure is the bridge that turns the vague task "compare these two sequences" into the concrete task "fill in a table, one cell at a time."

KP.3.Procedure: The peel test.
Here's a quick way to test for it: peel residues off the end of an optimal alignment, one at a time. If what remains is always still optimal for the shorter sequences, the property holds. And that same peeling is what lets you walk the path backwards during traceback to recover the actual alignment.

KP.4.Concept: Why it justifies dynamic programming.
Why does this matter so much? The number of possible alignments explodes combinatorially, so brute force is impossible. Optimal substructure collapses that explosion: each cell just makes one local best decision from its optimal neighbours, and the table stores every sub-answer exactly once. Without this property, a local choice couldn't be trusted, and dynamic programming would simply give wrong answers.

KP.5.Concept: The cut-and-paste proof.
You can prove it by contradiction, an argument called cut-and-paste. Take an optimal alignment and look at its last column. Remove that column. If the remaining piece were not optimal, then some better alignment of those shorter prefixes exists — but then gluing the same last column back on would beat the original, which we said was optimal. That's a contradiction, so the remaining piece must have been optimal all along. The whole argument works because the score adds up column by column, and the last column's cost doesn't depend on how the rest was aligned.

KP.6.CoolFact: When it fails, problems get hard.
And here's the cool part — optimal substructure is not guaranteed. Finding the shortest simple path in a graph has it, which is why it's easy. But finding the longest simple path does not: a longest path is not built from longest sub-paths, and that problem is NP-hard. The very same property that makes sequence alignment tractable is what separates the easy problems from the truly hard ones.

# Question and Answer
Q. Define optimal substructure.
A. The property that an optimal solution to a problem is composed of optimal solutions to its sub-problems — required for dynamic programming to be correct.

Q. State the alignment-specific version.
A. An optimal alignment is always composed of optimal sub-alignments; peeling its last column leaves an optimal alignment of the shorter prefixes.

Q. What are the three ways an optimal prefix alignment can end?
A. A diagonal pair of $a_i,b_j$; a gap in the top sequence; or a gap in the side sequence — the three predecessors in the recurrence.

Q. How does optimal substructure produce the Needleman–Wunsch recurrence?
A. Since each ending leaves an optimal smaller alignment, $S(i,j)$ depends only on those three already-optimal neighbour cells plus the last column's base score.

Q. Outline the cut-and-paste proof.
A. Take an optimal alignment, remove its last column; if the remainder weren't optimal, a better prefix alignment plus the same column would beat the original — a contradiction. So the remainder is optimal.

Q. Why does the proof need scores to be additive over columns?
A. Additivity (and the last column's cost being independent of the prefix) lets any improvement to the prefix carry straight through to the full alignment's score.

Q. Give a problem that lacks optimal substructure, and the consequence.
A. Longest simple path in a graph — it isn't built from longest sub-paths, and the problem is NP-hard (unlike shortest path, which has the property).

Q. What everyday test confirms the property for alignment?
A. The peel test: remove residues from the end one at a time; the remainder must stay optimal for the shorter sequences.
