---
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Key Concepts — Local Alignment & Gap Penalties

**Summary**: Exam-ready review sheet for [[local-alignment|Arc 4]]. Affine gap penalties, the global-vs-local distinction, and the Smith–Waterman algorithm.

---

## Definitions
- **[[affine gap penalty]]** — `w(k)=g+e(k−1)`: gap-open `g` (once) + gap-extend `e` (per extra position).
- **[[global vs local alignment]]** — global = end-to-end (NW); local = best subsequence region(s) (SW).
- **[[Smith-Waterman algorithm]]** — optimal local alignment by DP; NW + a `0` option.

## Key formulas
**Affine gap penalty:** $w(k) = g + e(k-1)$ — e.g. lecture's $-12 - 4(k-1)$ (open 12, extend 4).

**Smith–Waterman recurrence** (the one change = the `0`):
$$S(i,j) = \max\big[\,0,\ S(i-1,j-1)+s(a_i,b_j),\ S(i-k,j)-w(k),\ S(i,j-l)-w(l)\,\big]$$

## Procedure (SW skeleton)
1. **Initialize** 0-th row/col to **0** (base scores from a substitution matrix).
2. **Fill** with the recurrence; negative → write **0** (fresh start).
3. **Traceback** from the **maximum cell** anywhere → stop at the first **0**.
**NW vs SW:** init (gap penalty vs 0) · the `0` in the max · traceback (corner→corner vs maxcell→0).

## Questions & answers
Q. NW's gap blind spot? → It penalises every gap position equally, so a length-*k* gap costs *k* singles.
Q. What does affine `g≫e` encode? → A long gap is one indel event; don't open gaps gratuitously, but tolerate long ones.
Q. One change that makes NW local? → Add `0` to the `max`.
Q. Where does SW traceback start/stop? → Max-scoring cell → first `0`.
Q. Is the local alignment a slice of the global one? → No, AL ⊄ AG.
Q. Why is local the default for database search? → It finds domains/homology regions inside larger sequences (BLAST).
Q. EMBOSS tool names? → `water` (local), `needle` (global).

## Key facts / numbers
- Lecture gap penalty: **open 12, extend 4** (`w(k)=−12−4(k−1)`).
- Local block in [[exercise-smith-waterman-local]]: `YRQCLCR` / `YNRCKCR` (4/7 identical).
- Smith–Waterman is $O(mn)$ and **optimal** — slowness motivated BLAST/FASTA.
- Gotoh (1982): affine gaps still $O(mn)$.
