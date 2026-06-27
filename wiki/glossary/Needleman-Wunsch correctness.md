---
tags:
  - TYPE__/Concept/Theorem
  - PATH__/ComputerScience/Algorithms/DynamicProgramming
  - MODULE__/DynamicProgrammingAlignment
  - EXAM_PREP
foundational: 4
prereqs: 4
density: 4
value: 4
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Needleman-Wunsch correctness

Why does filling the table actually yield the **best** alignment — couldn't some other procedure score higher? [[optimal substructure]] alone doesn't settle this: it's a *necessary* property, not a proof of the algorithm. Correctness needs **two** ingredients:

1. **Optimal substructure** — an optimal alignment is built from optimal sub-alignments (see [[optimal substructure]]).
2. **Exhaustive choice** — every alignment column is *exactly one* of three kinds: a diagonal pair, a gap in the top sequence, or a gap in the side sequence. There is **no fourth kind**. So the recurrence's three-way `max` secretly ranges over *every* possible alignment.

The whole confusion dissolves once you separate two things:

- $OPT(i,j)$ — the **true** best score: the maximum over the *entire set* of alignments of the prefixes (defined with no reference to any algorithm);
- $S(i,j)$ — the number the **procedure** writes in the cell.

The [[Needleman-Wunsch recurrence|recurrence]] is correct precisely when $S(i,j) = OPT(i,j)$ for every cell — proved below.

**Answering the worry.** Since $S(m,n) = OPT(m,n)$, and $OPT(m,n)$ is the max over *all* alignments, **no procedure can beat it** — there simply is no higher-scoring alignment to find. A different method can only return a *different* optimum when there are ties, never a *better* one.

> [!Caution] "Best" has fine print
> Optimal is **relative to the fixed scoring scheme** — change the [[scoring matrix]] or gap costs and the optimum changes. And optimal ≠ biologically correct: NW maximizes a *score*, not evolutionary truth.

# Argument
Claim: $S(i,j) = OPT(i,j)$ for every cell. Induction on $i+j$ (base: empty-vs-empty and the all-gap edges have a single possible alignment, so $S=OPT$).

- **Achievable ($S \le OPT$).** Each branch of the `max`, e.g. $S(i{-}1,j{-}1) + s(a_i,b_j)$, is the score of a *real* alignment (an optimal sub-alignment with that last column appended). A real alignment can't beat the true maximum, so the `max` of the three is $\le OPT(i,j)$.
- **Unbeatable ($OPT \le S$).** Take any optimal alignment. Its last column is one of the three kinds (exhaustiveness). Peel it off → the rest is *some* alignment of a smaller prefix-pair, so its score $\le$ that cell's optimum $= S$ there (induction). Add the column back: $OPT(i,j) \le S(i,j)$, since the `max` already contains that branch.

Achievable **and** an upper bound on all alignments ⟹ $S(i,j)$ is the global maximum. ∎

# TLDR
The procedure is provably optimal because of **two** facts, not one: optimal substructure *plus* the fact that every column is one of only three kinds (so the `max` covers all alignments). An induction then shows the table value $S(i,j)$ equals the true best score $OPT(i,j)$ over *all* alignments — so nothing can beat it; other procedures differ only on ties.

# Recitation Anchors
- Two ingredients: **optimal substructure** + **exhaustive choice** (3 column kinds, no 4th)
- Separate $OPT(i,j)$ (true max over all alignments) from $S(i,j)$ (table value)
- Correctness = "$S = OPT$ at every cell"
- Induction, two directions: **achievable** ($S\le OPT$) + **unbeatable** ($OPT\le S$)
- $S(m,n)=OPT(m,n)$ ⟹ no procedure beats it; ties → different optimum, not better
- Fine print: optimal *for the scoring scheme*; optimal ≠ biologically true

> [!Cool] Cool fact
> The optimality guarantee doesn't scale. Optimal **pairwise** alignment is easy ($O(mn)$), but proving the same for **multiple** sequence alignment is hopeless: optimal MSA under the sum-of-pairs score is **NP-complete**, so real tools fall back on heuristics. [source](https://doi.org/10.1089/cmb.1994.1.337)

# Read aloud
KP.0.Concept: The real question.
Here's a subtle worry. We know an optimal alignment is built from optimal pieces — that's optimal substructure. But why does the procedure as a whole give the best alignment? Couldn't a cleverer method score higher? Optimal substructure by itself doesn't answer that; it's a necessary property, not a proof of the algorithm.

KP.1.Concept: Two ingredients.
Correctness rests on two facts, not one. First, optimal substructure. Second, exhaustive choice: every column of an alignment is exactly one of three kinds — a diagonal pair, a gap in the top sequence, or a gap in the side sequence. There's no fourth kind. So when the recurrence takes the best of three options, it has quietly considered every alignment that could possibly exist.

KP.2.Concept: Two things people confuse.
The confusion clears once you name two separate quantities. One is the true best score, the maximum over the entire set of alignments — call it OPT. It's defined without any algorithm. The other is simply the number the procedure writes in the cell — call it S. The algorithm is correct exactly when S equals OPT in every cell.

KP.3.Procedure: The two-direction proof.
You prove S equals OPT by induction. One direction: every option the max considers is a real, buildable alignment, so it can't exceed the true best — that keeps S from overshooting. The other direction: take a genuinely optimal alignment, peel off its last column, and what remains is some alignment of a smaller prefix, which by induction can't beat that cell's stored value. Add the column back, and the optimum can't exceed S. Being both achievable and an upper bound on all alignments, S must be the global maximum.

KP.4.Concept: The worry, answered.
So here's the payoff. The table's final value equals the maximum over all alignments — a fact about the problem, not about Needleman–Wunsch. No procedure can return a higher-scoring alignment, because none exists. A different method might pick a different best alignment when several tie, but never a strictly better one. The only fine print: "best" means best for the scoring scheme you chose, and a top score isn't a guarantee of biological truth.

KP.5.CoolFact: Optimality doesn't scale.
And here's the cool part — this clean guarantee is special to aligning two sequences. The moment you try to optimally align many sequences at once, the problem becomes NP-complete, so the big alignment tools give up on guaranteed optimality and use heuristics instead.

# Question and Answer
Q. Why isn't optimal substructure enough to prove the algorithm correct?
A. It's a necessary property of optimal solutions, not a proof that the procedure computes one. You also need exhaustive choice (the max covers every possible last column) plus an induction.

Q. What is the difference between $OPT(i,j)$ and $S(i,j)$?
A. $OPT$ is the true maximum score over *all* alignments of the prefixes (algorithm-independent); $S$ is the value the recurrence writes. Correctness means $S=OPT$ everywhere.

Q. What does "exhaustive choice" mean here?
A. Every alignment column is exactly one of three kinds (diagonal, gap-top, gap-side) — no fourth — so the three-way max implicitly ranges over every alignment.

Q. State the two directions of the correctness induction.
A. Achievable: each max branch is a real alignment, so $S\le OPT$. Unbeatable: any optimum peels to a smaller-prefix alignment bounded by $S$, so $OPT\le S$. Together $S=OPT$.

Q. Could a different procedure produce a better alignment than NW?
A. No — $S(m,n)$ equals the max over all alignments, so none scores higher. A different procedure can only return a different optimum on ties.

Q. What two caveats qualify "NW finds the best alignment"?
A. "Best" is relative to the fixed scoring scheme, and a maximal score is not a guarantee of biological correctness.
