---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Alignment Foundations (Arc 1)

**Summary**: The conceptual and biological groundwork of pairwise alignment — what it is, why it matters, and the vocabulary (identity, conservation, similarity, homology, orthologs, paralogs) needed before any algorithm.
**Sources**: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf|Teoria L3, slides 1–18]]

---

## What and why
[[pairwise alignment]] aligns two sequences to maximize identity/conservation and so assess relatedness. It is foundational because of its [[applications of pairwise alignment|many applications]] — relatedness, domains/motifs, BLAST, genome analysis. When you can choose, [[protein vs DNA alignment|protein sequences are often more informative than DNA]] (bigger alphabet, visible conservation, the genetic code's degeneracy, longer evolutionary look-back).

## The vocabulary of relatedness
Three stacked measures: [[identity conservation similarity|identity, conservation, and similarity]] (similarity = identity + conservation). These are *quantitative*. Above them sits [[homology]] — a *qualitative* claim of shared ancestry — and the single most-tested distinction, [[homology vs similarity]].

## Why it's biologically meaningful
[[sequence structure function|Sequence determines structure, which determines function]]: conserved sequence implies conserved function, which is what makes homology useful for function prediction. Homology comes in two types by the event that split the copies — [[orthologs]] (speciation, different species) and [[paralogs]] (gene duplication, same species) — laid side by side in [[orthologs vs paralogs]].

## The primitives of comparison
Every alignment column is a [[match mismatch gap|match, mismatch, or gap]]. The number of operations needed to turn one sequence into another is the [[edit distance and parsimony|edit distance]], and evolution is assumed to follow the most parsimonious (shortest) path — the idea every scoring scheme tries to capture.

## Where this leads
The next arc, [[dot-plots|Dot Plots]], turns these ideas into a first practical method; [[dynamic-programming-alignment|Dynamic Programming Alignment]] then makes the optimal alignment computable.

## Related pages
- [[dot-plots]]
- [[dynamic-programming-alignment]]
- [[alignment-foundations-key-concepts]]
