---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Study Path — Pairwise Alignment (Modulo 1: L3–L4)

A suggested order for studying the wiki, building from concepts to algorithms to scoring. Start with [[pairwise-alignment-overview]] for the map.

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
8. [[dot plot]] → [[dot plot patterns]] → [[dot plot patterns visualized]] — the visual method (with a worked figure gallery).
9. [[sliding window]] — filtering noise.
10. [[scoring matrix]] — measuring similarity, not just identity.
11. [[sequence identity and similarity percent]] — quantifying results.
   → practice [[exercise-dot-plot-construction]] and [[exercise-sequence-identity-percent]].
   → consolidate with [[dot-plots-key-concepts]].

## 3. Dynamic programming — *the optimal global alignment* ([[dynamic-programming-alignment]])
12. [[dynamic programming]] → [[optimal substructure]] → [[Needleman-Wunsch correctness]] — the strategy, the property that justifies it, and the proof it's globally optimal.
13. [[Needleman-Wunsch algorithm]] — the procedure.
14. [[Needleman-Wunsch recurrence]] — the maths, unraveled.
15. [[traceback]] — reading out the alignment.
   → practice [[exercise-needleman-wunsch-worked]].
   → consolidate with [[dynamic-programming-alignment-key-concepts]].

## 4. Local alignment & gaps — *fixing and extending NW* ([[local-alignment]])
16. [[affine gap penalty]] — a smarter gap model (gap-open + gap-extend).
17. [[global vs local alignment]] — the key distinction (exam).
18. [[Smith-Waterman algorithm]] — local alignment = NW + a `0`.
   → practice [[exercise-smith-waterman-local]].
   → consolidate with [[local-alignment-key-concepts]].

## 5. Significance — *is the score meaningful?* ([[alignment-significance]])
19. [[statistical significance of an alignment]] — the question and the null model.
20. [[Z-score (alignment)]] — global significance by shuffling.
21. [[E-value (Karlin-Altschul)]] → [[Gumbel distribution and the p-value]] — local significance (exam); see the [[Karlin-Altschul p-value erratum|erratum]].
   → practice [[exercise-evalue-interpretation]].
   → consolidate with [[alignment-significance-key-concepts]].

## 6. Substitution matrices — *where the scores come from* ([[substitution-matrices]])
22. [[amino acid similarity]] → [[substitution matrix]] — why empirical, and what the matrix is.
23. [[PAM (Point Accepted Mutation)]] → [[relative mutability]] → [[amino acid frequencies]] → [[PAM1 mutation probability matrix]] → [[PAM matrix extrapolation]] — the PAM family, built up.
24. [[log-odds score]] — the scoring engine (exam).
25. [[BLOSUM matrix]] → [[PAM vs BLOSUM]] — the empirical family and the comparison (exam).
26. [[twilight zone]] — where sequence similarity runs out (exam).
   → practice [[exercise-blosum62-scoring]] and [[exercise-log-odds-score]].
   → consolidate with [[substitution-matrices-key-concepts]].

## Before the exam
Re-read the six Key Concepts pages, then re-do the seven exercises from scratch. Pay special attention to the `EXAM_PREP`-flagged entries:
- **L3**: [[homology vs similarity]], [[orthologs vs paralogs]], [[sequence identity and similarity percent]], [[Needleman-Wunsch algorithm]], [[Needleman-Wunsch recurrence]], [[optimal substructure]], [[Needleman-Wunsch correctness]].
- **L4**: [[global vs local alignment]], [[affine gap penalty]], [[Smith-Waterman algorithm]], [[statistical significance of an alignment]], [[E-value (Karlin-Altschul)]], [[Gumbel distribution and the p-value]], [[substitution matrix]], [[PAM (Point Accepted Mutation)]], [[PAM matrix extrapolation]], [[log-odds score]], [[BLOSUM matrix]], [[PAM vs BLOSUM]], [[twilight zone]].


test
