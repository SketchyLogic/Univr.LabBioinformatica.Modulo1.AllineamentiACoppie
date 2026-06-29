---
tags:
  - TYPE__/Concept/Definition
  - PATH__/ComputerScience/Algorithms/DynamicProgramming
  - MODULE__/LocalAlignment
  - EXAM_PREP
  - MATH_UNRAVELING
foundational: 4
prereqs: 2
density: 3
value: 4
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# affine gap penalty

Plain [[Needleman-Wunsch algorithm|Needleman–Wunsch]] has a **blind spot**: it penalises each gap position the same fixed amount, so a length-*k* gap costs exactly *k* times a single gap. But a [[match mismatch gap|gap]] is usually **one indel event**, not *k* of them. The fix is a smarter **gap penalty function** that charges a lot to *start* a gap and little to *extend* it. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=1|L4 p.1]] [^ws]

$$w(k) = g + e\,(k-1)$$

## Unraveling, piece by piece
- **$w(k)$** — the **total penalty** for a single gap of length $k$ (a run of $k$ dashes).
- **$g$** — the **gap-open** penalty: the (large) cost paid once, for the *first* position of the gap.
- **$e$** — the **gap-extend** penalty: the (small) cost paid for *each additional* position after the first.
- **$(k-1)$** — the number of *extension* positions: a length-$k$ gap has 1 opening + $(k-1)$ extensions.

So $w(1)=g$, $w(2)=g+e$, $w(3)=g+2e$, … — a straight line in $k$ with intercept $g$ and slope $e$. "**Affine**" just means *linear-plus-a-constant* (the constant being the one-time open cost $g$).

> [!Example] The lecture's numbers
> The slides use $w(k) = -12 - 4(k-1)$ — i.e. **gap-open = 12**, **gap-extend = 4** (initial values seeded from [[PAM (Point Accepted Mutation)|PAM250]]). A 1-gap costs 12; a 3-gap costs $12+4+4 = 20$, **not** $3\times12 = 36$. Opening is **3× more expensive** than extending here.

**Why this shape is biological.** A single insertion/deletion can add or remove **many residues at once**, so a long gap is *one* rare event, not many. Setting $g \gg e$ tells the aligner: "don't be afraid of a *long* gap, but don't *open* gaps gratuitously." This is the principled version of the gap-open/gap-extend split foreshadowed in [[match mismatch gap]].

**Where it plugs in.** $w(k)$ replaces the flat gap cost in the vertical/horizontal moves of the [[Needleman-Wunsch recurrence]] — the very reason that recurrence keeps the general $S(i-k,j)$ / $S(i,j-l)$ form (it must weigh **every** gap length explicitly). It is then carried into the [[Smith-Waterman algorithm|Smith–Waterman]] local recurrence. With a **linear** penalty ($g=e$) the formula collapses back to a flat per-position cost.

# TLDR
An **affine gap penalty** charges a large one-time **gap-open** cost $g$ plus a small **gap-extend** cost $e$ per extra position: $w(k)=g+e(k-1)$. It models a length-$k$ gap as *one* indel event rather than $k$ separate ones — biologically right because a single insertion/deletion can span many residues. The lecture uses $w(k)=-12-4(k-1)$.

# Recitation Anchors
- $w(k) = g + e(k-1)$ — total penalty for a length-$k$ gap
- $g$ = **gap-open** (paid once); $e$ = **gap-extend** (paid per extra position)
- $(k-1)$ = number of extensions; $w(1)=g$, $w(2)=g+e$, …
- "Affine" = **linear + constant** (line: intercept $g$, slope $e$)
- Lecture: $w(k)=-12-4(k-1)$ → open 12, extend 4
- Biological reason: one indel can span many residues → $g \gg e$
- Plugs into the NW/SW recurrence's vertical/horizontal moves; linear penalty ($g=e$) = flat cost

> [!Cool] Cool fact
> The obvious way to handle affine gaps re-scans the whole row/column at every cell, costing $O(mn(m+n))$. In **1982 Osamu Gotoh** showed affine gaps can be scored in just $O(mn)$ — *the same cost as a flat penalty* — by tracking three matrices at once. That trick is what makes affine gaps practical in every modern aligner. [source](https://doi.org/10.1016/0022-2836(82)90398-9)

# Read aloud
KP.0.Concept: Needleman–Wunsch's blind spot.
Plain Needleman–Wunsch has a weakness. It charges the same fixed amount for every gap position, so a gap of length five costs exactly five times a single gap. But in biology a gap is usually one event — a single insertion or deletion — not five separate ones. So we want a smarter penalty.

KP.1.Definition: The gap penalty function.
The fix is a function: the penalty for a gap of length k equals g plus e times the quantity k minus one. Let me unpack that.

KP.2.Concept: Open versus extend.
The whole thing, w of k, is the total penalty for one gap that is k positions long. The term g is the gap-open penalty — a large cost you pay once, for the first position. The term e is the gap-extend penalty — a small cost for each additional position. And k minus one is just how many of those extension positions there are: one opening plus k-minus-one extensions. So a length-one gap costs g, a length-two gap costs g plus e, and so on. It's a straight line in k. That's what "affine" means — linear plus a constant.

KP.3.Numbers: The lecture's values.
The slides use minus twelve minus four times k-minus-one. So gap-open is twelve and gap-extend is four. A single gap costs twelve; a gap of length three costs twelve plus four plus four, which is twenty — not thirty-six. Opening a gap is three times more expensive than extending it.

KP.4.Connection: Why this shape is biological, and where it plugs in.
This shape is biological because a single insertion or deletion can add or remove many residues at once, so a long gap is one rare event, not many. Making open much costlier than extend tells the aligner: don't be scared of a long gap, but don't open gaps for no reason. This penalty replaces the flat gap cost in the Needleman–Wunsch recurrence — which is exactly why that recurrence keeps its general form that scans every possible gap length — and it carries straight over into the Smith–Waterman local algorithm.

KP.5.CoolFact: Gotoh's trick.
And here's the cool part — done naively, affine gaps make the algorithm much slower, because you rescan a whole row or column at every cell. In 1982 Osamu Gotoh showed you can score affine gaps in the same time as a flat penalty, by cleverly tracking three matrices at once. That trick is why affine gaps are practical in every aligner today.

# Question and Answer
Q. What is an affine gap penalty, and what is its formula?
A. A gap-scoring scheme with a large one-time open cost plus a small per-position extend cost: $w(k)=g+e(k-1)$ for a gap of length $k$.

Q. What do $g$ and $e$ stand for?
A. $g$ = gap-open (paid once for the first gap position); $e$ = gap-extend (paid for each additional position).

Q. Why is it called "affine"?
A. Because $w(k)$ is a linear function of $k$ plus a constant — a straight line with slope $e$ and intercept $g$.

Q. Using the lecture's $w(k)=-12-4(k-1)$, what does a length-3 gap cost?
A. $12 + 4 + 4 = 20$ (open 12 once, extend 4 twice) — not $3\times12=36$.

Q. Why is an affine penalty more biologically realistic than a linear one?
A. A single indel event can insert/delete many residues at once, so a long gap is one rare event; charging $g\gg e$ avoids opening gaps gratuitously while tolerating long ones.

Q. How does the affine penalty relate to the linear (flat) penalty?
A. Linear is the special case $g=e$ (every position costs the same); then the recurrence collapses to a flat per-position cost.

Q. Where does $w(k)$ enter the alignment algorithm?
A. In the vertical/horizontal (gap) moves of the Needleman–Wunsch and Smith–Waterman recurrences, subtracted as $-w(k)$.

[^ws]: The slides label the 1976 affine-gap refinement of NW "Waterman–Smith" and the 1981 local-alignment method "Smith–Waterman". For simplicity this wiki uses **Smith–Waterman** throughout and treats the affine gap penalty as part of that framework.
