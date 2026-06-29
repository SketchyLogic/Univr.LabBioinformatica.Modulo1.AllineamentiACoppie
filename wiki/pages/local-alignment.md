---
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Local Alignment & Gap Penalties (Arc 4)

**Summary**: Lecture L4 first **patches** Needleman–Wunsch's crude gap handling with an **affine gap penalty**, then **extends** alignment from *global* (end-to-end) to *local* (best-matching region) with the **Smith–Waterman** algorithm — the engine behind database search.
**Sources**: [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf|Teoria L4, slides 2–9]]

---

## Fixing Needleman–Wunsch — gap penalties
[[Needleman-Wunsch algorithm|NW]] has a blind spot: it charges every gap position the same, so a long gap costs as much as many separate ones. The [[affine gap penalty]] `w(k)=g+e(k−1)` fixes this — a large one-time **gap-open** `g` plus a small **gap-extend** `e` per extra position (the lecture uses `−12 −4(k−1)`). This models a [[match mismatch gap|gap]] as **one indel event**, the principled form of the gap-open/extend split first hinted at in L3.

## Global vs local
The [[global vs local alignment|global-vs-local]] distinction is the heart of this arc. **Global** (NW) aligns both sequences end-to-end; **local** finds only the subsequence regions that align best. Global alignment can **mask** a short conserved block by drowning it in non-homologous flanks — so local alignment is what you use to find **domains** and **motifs**, and the basis of **BLAST** database search.

## The Smith–Waterman algorithm
The [[Smith-Waterman algorithm]] computes the optimal *local* alignment by changing the [[Needleman-Wunsch recurrence]] in **one place**: it adds `0` as a fourth option in the `max`, so scores can't go negative. With the 0-th row/col set to 0, you fill the matrix and then [[traceback|trace back]] from the **maximum-scoring cell** until you hit a `0`. Online: EMBOSS **`water`** (vs `needle` for global).

## Putting it to work
The lecture aligns the same two peptides globally and locally to show the local result is **not** a slice of the global one (AL ⊄ AG) — work it through in [[exercise-smith-waterman-local]].
→ Review: [[local-alignment-key-concepts]]

## Connections
- **Data mining** — local alignment + BLAST is pattern extraction from massive sequence databases.
- **Role of the bioinformatician** — choosing global vs local (and the right gap penalties) is a daily judgement call when interpreting similarity.

## Related pages
- [[dynamic-programming-alignment]] (Arc 3 — the global algorithm this builds on)
- [[alignment-significance]] (Arc 5 — is the local score meaningful?)
- [[substitution-matrices]] (Arc 6 — the scores plugged into the matrix)

## Read aloud
This arc is about two upgrades to sequence alignment. The first fixes a weakness in Needleman–Wunsch: it treated every gap position as equally costly, but a long gap is usually a single insertion or deletion event, not many. The affine gap penalty captures this with a large one-time cost to open a gap plus a small cost to extend it. The second upgrade is bigger: moving from global alignment, which forces both sequences to line up end to end, to local alignment, which finds only the best-matching region. This matters because a global alignment can hide a short shared block by surrounding it with unrelated sequence. The Smith–Waterman algorithm finds the optimal local alignment, and remarkably it's just Needleman–Wunsch with one change — adding a zero option so scores never go negative — plus a different traceback that starts at the highest-scoring cell. Local alignment is the foundation of database searching with BLAST, and the lecture drives the point home by aligning the same two peptides both ways and showing the local result is not simply a piece of the global one.
