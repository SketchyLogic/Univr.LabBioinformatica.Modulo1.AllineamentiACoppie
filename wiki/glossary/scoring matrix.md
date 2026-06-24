---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/DotPlots
foundational: 5
prereqs: 2
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

# scoring matrix

A **scoring matrix** (*matrice di punteggio* — **not** a dot matrix!) assigns a numerical score to **every pair of residues**, encoding how interchangeable they are. It is what lets an alignment measure [[identity conservation similarity|similarity]], not just identity. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=7|L3 p.7]]

For nucleotides it can be a small 4×4 table; for proteins it is a 20×20 table. The diagonal (identical pairs) carries the highest scores; off-diagonal entries are positive for **conservative** substitutions and low/negative for unlike pairs.

> [!Example] Nucleotide scoring matrix
> With a matrix where identical bases score `+2` and others `0` or `±1`, aligning `AAATCCGAA` vs `ATACAGATT` sums to `2+1+2+0+0+1+0+1+1 = 8`. The matrix — not raw identity — sets the score. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=7|L3 p.7]]

**Used inside the [[sliding window]]:** the window score becomes the *average* of per-pair scores pulled from the matrix:

$$N(x,y) = \frac{1}{L}\sum_{h=-g}^{+g} S(x+h,\, y+h)$$

Now *S* depends on **which scoring matrix** you choose and on the window length *L*. The threshold *s* for marking a cell is therefore set by the scoring matrix — i.e. by your definition of "similar". This same matrix later seeds the [[Needleman-Wunsch algorithm]] (its $s(a_i,b_j)$ term), letting it weigh similarity, not just identity.

# TLDR
A scoring matrix assigns a number to **every residue pair** (4×4 for DNA, 20×20 for proteins), encoding how interchangeable they are. It is what lets an alignment measure **similarity**, not just identity, and it feeds both the sliding window and Needleman–Wunsch.

# Recitation Anchors
- Score for **every residue pair** (NOT the dot matrix!)
- 4×4 for nucleotides, 20×20 for amino acids
- Diagonal (identical) highest; conservative swaps positive; unlike pairs low/negative
- Lets alignment measure **similarity**, not just identity
- Feeds sliding window (averaged) and NW's $s(a_i,b_j)$
- Real example: **BLOSUM62**

> [!Cool] Cool fact
> Real protein scoring matrices are derived from observed evolution: **BLOSUM62** — the default for protein alignment — was built by counting substitutions in **blocks** of conserved protein regions, and a coding bug discovered in 2008 means the matrix everyone used for years wasn't quite the intended one… yet it worked *better*. [source](https://doi.org/10.1038/nbt0808-274)

# Read aloud
KP.0.Definition: What a scoring matrix is.
A scoring matrix, in Italian matrice di punteggio, gives a number to every possible pair of residues, capturing how interchangeable the two are. Be careful: this is a matrix of scores, not the dot matrix from before. The scoring matrix is what lets an alignment measure similarity, not just plain identity.

KP.1.Concept: What it looks like.
For DNA it can be a small four-by-four table; for proteins it's a twenty-by-twenty table. Identical pairs, along the diagonal, get the highest scores. Off the diagonal, conservative substitutions — swaps between similar residues — get positive scores, while swaps between very different residues get low or negative scores.

KP.2.Concept: A worked example.
Imagine a DNA matrix where identical bases score plus two and the rest score zero or one. Aligning two short sequences and adding up the per-position scores from the matrix might total eight. The point is that the matrix sets the score, not a simple count of identical letters.

KP.3.Connection: Plugged into the sliding window.
Inside a sliding window, the score becomes the average of the per-pair scores looked up in the matrix. So the window's value now depends on which scoring matrix you chose and on how long the window is. That means the threshold for marking a cell is really decided by the scoring matrix — by your own definition of what counts as similar.

KP.4.Connection: Seeding the alignment algorithm.
That same matrix returns later: it feeds the Needleman–Wunsch algorithm, supplying the score for each residue pair, so the algorithm can weigh true similarity rather than just identity.

KP.5.CoolFact: BLOSUM62's lucky bug.
And here's the cool part — real protein matrices are built from observed evolution. The famous BLOSUM62 matrix was made by counting substitutions inside blocks of conserved protein regions. A bug discovered in 2008 revealed that the version everyone had used for years wasn't quite the one intended — yet, oddly, it actually performed a little better.

# Question and Answer
Q. What is a scoring matrix, and what does it let you measure?
A. A table giving a score to every residue pair; it lets an alignment measure similarity (conservation), not just identity.

Q. How does a scoring matrix differ from a dot matrix?
A. A dot matrix is the visual plot of matches; a scoring matrix is a table of per-pair scores ("matrice di punteggio", not "di punti").

Q. What sizes are nucleotide vs protein scoring matrices?
A. 4×4 for nucleotides, 20×20 for amino acids.

Q. How is a scoring matrix combined with a sliding window?
A. The window score is the average of per-pair scores looked up from the matrix: $N(x,y)=\frac{1}{L}\sum S(x+h,y+h)$.

Q. What sets the threshold s for marking a cell once a matrix is used?
A. The scoring matrix itself — i.e. the chosen definition of "similar" — together with the window length.

Q. Name a real protein scoring matrix and how it was built.
A. BLOSUM62, derived by counting substitutions in conserved blocks of related proteins.
