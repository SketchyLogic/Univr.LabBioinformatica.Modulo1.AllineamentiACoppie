---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Key Concepts — Dot Plots

**Summary**: Exam-ready review sheet for [[dot-plots|Arc 2]]. Definitions, the window/score procedure, the % formulas, and the patterns to recognise.

---

## Definitions
- **[[dot plot]]** — visual matrix; a dot at every identity; diagonals = similarity.
- **[[dot plot patterns|Patterns]]** — main diagonal (similar), anti-diagonal (inversion), parallel repeats (repetition), offset diagonal (indel).
- **[[sliding window]]** — segment comparison to filter noise; radius *g*, length *L = 2g+1*.
- **[[scoring matrix]]** — table of per-pair scores ("matrice di punteggio", **not** dot matrix); defines "similar".

## Procedures (skeletons)
**Dot plot:** seq1 on top → seq2 on side → dot where residues match → read diagonals.
**Sliding window:** pick radius *g* → window length *L = 2g+1* → count/score residues along the window diagonal *N(x,y)* → mark centre if *N(x,y) > s*.
**A dot plot depends on 3 choices:** window length *L*, similarity measure *S(x,y)*, threshold *s*.

## Key formulas
- Window count (identity): $N(x,y) = \sum_{h=-g}^{+g} S(x+h,y+h)$, with $S=1$ if match else $0$.
- Window score (similarity): $N(x,y) = \frac{1}{L}\sum_{h=-g}^{+g} S(x+h,y+h)$ using the [[scoring matrix]].
- **% identity** = (#matches / $L_1$) × 100.
- **% similarity** = (score $S_1$vs$S_2$ / score $S_1$vs$S_1$) × 100. See [[sequence identity and similarity percent]].

## Questions & answers
Q. What does a diagonal mean? → A region of local similarity.
Q. How does an inversion appear? → As an anti-diagonal (perpendicular).
Q. Why do nucleotide dot plots need filtering? → Only 4 letters → many random matches (noise).
Q. If radius g, what is L? → $L = 2g + 1$.
Q. With gaps present, what denominator for % identity? → The **alignment length** (gaps included), not the original length.
Q. Why is similarity ≥ identity? → It also credits conservative substitutions.

## Key facts / numbers
- Real β/α-globin (EMBOSS): identity **43.6%**, similarity **60.4%**, gaps **6.0%** over length 149.
- DOTTER/Dotlet colour cells by score; varying *L* (e.g. L=1 vs L=11) sharpens diagonals.
