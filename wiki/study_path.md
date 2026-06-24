---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Study Path — Pairwise Alignment (Lecture L3)

A suggested order for studying the wiki, building from concepts to algorithm. Start with [[pairwise-alignment-overview]] for the map.

## 1. Foundations — *why and what* ([[alignment-foundations]])
1. [[pairwise alignment]] — the core definition.
2. [[protein vs DNA alignment]] — choosing the right alphabet.
3. [[identity conservation similarity]] — the three measures.
4. [[homology]] → [[homology vs similarity]] — the key distinction (exam).
5. [[sequence structure function]] — why homology predicts function.
6. [[orthologs]] → [[paralogs]] → [[orthologs vs paralogs]] — the two homology types.
7. [[match mismatch gap]] → [[edit distance and parsimony]] — comparison primitives.
   → consolidate with [[alignment-foundations-key-concepts]].

## 2. Dot plots — *a first method* ([[dot-plots]])
9. [[dot plot]] → [[dot plot patterns]] — the visual method.
10. [[sliding window]] — filtering noise.
11. [[scoring matrix]] — measuring similarity, not just identity.
12. [[sequence identity and similarity percent]] — quantifying results.
   → practice [[exercise-dot-plot-construction]] and [[exercise-sequence-identity-percent]].
   → consolidate with [[dot-plots-key-concepts]].

## 3. Dynamic programming — *the optimal alignment* ([[dynamic-programming-alignment]])
13. [[dynamic programming]] — the strategy + optimal substructure.
14. [[Needleman-Wunsch algorithm]] — the procedure.
15. [[Needleman-Wunsch recurrence]] — the maths, unraveled.
16. [[traceback]] — reading out the alignment.
   → practice [[exercise-needleman-wunsch-worked]].
   → consolidate with [[dynamic-programming-alignment-key-concepts]].

## Before the exam
Re-read the three Key Concepts pages, then re-do the three exercises from scratch. Pay special attention to the `EXAM_PREP`-flagged entries: [[homology vs similarity]], [[orthologs vs paralogs]], [[sequence identity and similarity percent]], [[Needleman-Wunsch algorithm]], [[Needleman-Wunsch recurrence]].
