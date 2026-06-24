---
tags:
  - TYPE__/Concept/Procedure
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/DotPlots
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

# sliding window

A **sliding window** is the filter that cleans up a noisy [[dot plot]]. Instead of comparing single positions, compare whole **segments**, so isolated chance matches fade and true diagonals survive. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=6|L3 p.6]]

**Key observation:** locally similar regions line up along **diagonals**; spurious point matches are scattered **at random**. So compare a window of one sequence against the aligned window of the other and only mark the center if the *segment* matches well.

**Geometry of the window** (centered on cell *(x, y)*):
- choose a **radius** *g*;
- the window **length** is $L = 2g + 1$;
- count the identical residues along the diagonal of that window:

$$N(x,y) = \sum_{h=-g}^{+g} S(x+h,\, y+h), \qquad S = 1 \text{ if } x{+}h \text{ matches } y{+}h,\ \text{else } 0$$

Then apply a **threshold**: mark cell *(x, y)* only if $N(x,y) > s$. Raising *L* demands longer matching stretches (less noise, less sensitivity); lowering it keeps more signal (and more noise).

This identity-only rule is **too strict** — it ignores [[identity conservation similarity|similarity]]. The fix is to let *S* come from a [[scoring matrix]] and average over the window (see [[scoring matrix]]), turning the binary count into a graded similarity score.

> [!Hint] In practice
> Fix **two** of the three parameters (*L*, similarity measure, threshold) and vary the **third** to make the similar zones pop. Tools like DOTTER do exactly this, e.g. comparing *L=1* vs *L=11*.

# TLDR
A sliding window cleans up a noisy dot plot by scoring whole **segments** instead of single positions: count matches along a length-$L$ window centered on a cell, and mark the center only if the count beats a threshold $s$. Letting scores come from a scoring matrix turns the match count into a graded similarity score.

# Recitation Anchors
- Compare **segments**, not single positions → noise fades, diagonals survive
- True matches lie on diagonals; noise is scattered at random
- Radius $g$ → length $L = 2g+1$
- $N(x,y)$ = matches along window diagonal; mark if $N > s$
- Longer $L$ → less noise, less sensitivity
- Identity → similarity: let $S$ come from a scoring matrix, average over window

> [!Cool] Cool fact
> The same sliding-window trick underlies **hydropathy plots** (Kyte–Doolittle, 1982), where averaging amino-acid hydrophobicity over a ~19-residue window predicts membrane-spanning helices — one of the most cited methods in membrane biology. [source](https://doi.org/10.1016/0022-2836(82)90515-0)

# Read aloud
KP.0.Concept: The problem it solves.
A sliding window is the filter that cleans up a noisy dot plot. The trick is to stop comparing single positions and start comparing whole segments, so that isolated chance matches fade away while the genuine diagonals stay.

KP.1.Concept: The key observation.
Why does this work? Because regions that are truly similar line up along diagonals, whereas accidental single matches are scattered at random. So instead of asking "is this one letter the same," we slide a window along and ask "does this whole stretch match," marking the centre only when the segment as a whole agrees.

KP.2.Procedure: The geometry.
The window is built around a centre cell. You pick a radius, call it g. The window's length is two-g-plus-one. Then you count how many residues are identical along the window's diagonal — a residue scores one if it matches and zero if it doesn't, and you add those up to get a number N for the centre cell.

KP.3.Procedure: The threshold.
Then comes a threshold. You only place a mark at the centre cell if that count N is bigger than some cutoff s. Make the window longer and you demand longer matching stretches, cutting noise but also sensitivity. Make it shorter and you keep more signal, but more noise too.

KP.4.Connection: From identity to similarity.
Counting only exact matches is too strict, because it ignores similarity. The fix is to let each position's score come from a scoring matrix instead of just one-or-zero, and then average over the window. That turns the rigid match count into a graded similarity score. In practice you fix two of the three knobs and vary the third to make the similar zones stand out.

KP.5.CoolFact: The same trick beyond alignment.
And here's the cool part — this very same sliding-window averaging powers hydropathy plots. By averaging amino-acid water-loving-or-hating values over a window of about nineteen residues, biologists predict which parts of a protein cross a membrane. It's one of the most cited methods in membrane biology.

# Question and Answer
Q. What problem does a sliding window solve?
A. It filters background noise in a dot plot by comparing segments instead of single positions, so random point matches fade and real diagonals survive.

Q. Why do true matches survive windowing while noise doesn't?
A. Real similarity lies along diagonals (consecutive matches), while chance matches are randomly scattered and rarely form a run.

Q. If the radius is g, what is the window length L?
A. $L = 2g + 1$.

Q. What does N(x,y) count, and when is a cell marked?
A. The number of matching residues along the window's diagonal; the cell is marked if N(x,y) > s (a threshold).

Q. What is the effect of increasing the window length L?
A. It requires longer matching stretches: less noise but lower sensitivity.

Q. How is the strict identity-only rule relaxed to capture similarity?
A. Let S come from a scoring matrix and average over the window, producing a graded similarity score instead of a binary count.
