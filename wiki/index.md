---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Index — LLM Wiki: Pairwise Alignment (Modulo 1)

Table of contents for the wiki. See also [[study_path]] for a suggested order and [[log]] for the change history. Covers **Lecture L3** (foundations → dot plots → Needleman–Wunsch) and **Lecture L4** (local alignment & gaps → significance → substitution matrices).

## Overview & navigation pages
- [[pairwise-alignment-overview]] — top-level map of Modulo 1 (L3 + L4).
- [[alignment-foundations]] — Arc 1: what alignment is + the vocabulary.
- [[dot-plots]] — Arc 2: the dot-matrix method and its refinements.
- [[dynamic-programming-alignment]] — Arc 3: Needleman–Wunsch.
- [[local-alignment]] — Arc 4: gap penalties + local (Smith–Waterman).
- [[alignment-significance]] — Arc 5: is the score meaningful? (Z-score, E-value).
- [[substitution-matrices]] — Arc 6: PAM, BLOSUM, the twilight zone.

## Key Concepts (review sheets)
- [[alignment-foundations-key-concepts]]
- [[dot-plots-key-concepts]]
- [[dynamic-programming-alignment-key-concepts]]
- [[local-alignment-key-concepts]]
- [[alignment-significance-key-concepts]]
- [[substitution-matrices-key-concepts]]

## Glossary — Arc 1: Alignment Foundations
- [[pairwise alignment]] — aligning two sequences to assess similarity & homology.
- [[applications of pairwise alignment]] — relatedness, domains/motifs, BLAST, genomes.
- [[protein vs DNA alignment]] — why proteins can be more informative (incl. codon degeneracy).
- [[identity conservation similarity]] — the three stacked measures; similarity = identity + conservation.
- [[homology]] — similarity from common ancestry (qualitative).
- [[homology vs similarity]] — qualitative vs quantitative; the classic exam trap.
- [[sequence structure function]] — sequence→structure→function; basis of function prediction.
- [[orthologs]] — homologs in different species (speciation).
- [[paralogs]] — homologs in one species (gene duplication).
- [[orthologs vs paralogs]] — side-by-side comparison.
- [[match mismatch gap]] — the three alignment column outcomes.
- [[edit distance and parsimony]] — minimum operations; evolution's shortest path.

## Glossary — Arc 2: Dot Plots
- [[dot plot]] — visual dot matrix of identities.
- [[dot plot patterns]] — diagonals, inversions, repeats, deletions.
- [[dot plot patterns visualized]] — a worked figure gallery building each pattern step by step.
- [[sliding window]] — segment-based noise filtering (g, L=2g+1, N).
- [[scoring matrix]] — per-pair scores; defines "similar".
- [[sequence identity and similarity percent]] — the % formulas + gap caveat.

## Glossary — Arc 3: Dynamic Programming Alignment
- [[dynamic programming]] — optimal solutions from optimal sub-solutions.
- [[optimal substructure]] — the property that justifies DP for alignment (with cut-and-paste proof).
- [[Needleman-Wunsch correctness]] — why the procedure provably returns the *global* best alignment.
- [[Needleman-Wunsch algorithm]] — global optimal alignment via DP.
- [[Needleman-Wunsch recurrence]] — the scoring rule, unraveled (MATH_UNRAVELING).
- [[traceback]] — recovering the alignment from the filled matrix.

## Glossary — Arc 4: Local Alignment & Gap Penalties
- [[global vs local alignment]] — end-to-end vs best-subsequence; the database-search workhorse.
- [[affine gap penalty]] — w(k)=g+e(k−1): gap-open + gap-extend (MATH_UNRAVELING).
- [[Smith-Waterman algorithm]] — optimal local alignment = NW + a `0` option.

## Glossary — Arc 5: Alignment Significance
- [[statistical significance of an alignment]] — is the score better than chance? (score is not absolute).
- [[Z-score (alignment)]] — global significance by shuffling (MATH_UNRAVELING).
- [[E-value (Karlin-Altschul)]] — local: expected # of chance alignments ≥ x (MATH_UNRAVELING).
- [[Gumbel distribution and the p-value]] — p=1−e^(−E); extreme-value, not Gaussian.
- [[Karlin-Altschul p-value erratum]] — why slide 14's p-value formula is wrong.

## Glossary — Arc 6: Substitution Matrices
- [[substitution matrix]] — 20×20 symmetric log-odds table; PAM & BLOSUM families.
- [[amino acid similarity]] — measured empirically (observed substitutions), not from chemistry.
- [[PAM (Point Accepted Mutation)]] — accepted point mutation; a unit of evolutionary distance.
- [[relative mutability]] — how readily each aa changes (Ala≡100; Trp/Cys least).
- [[amino acid frequencies]] — background occurrence (Gly 8.9%…Trp 1.0%); the chance baseline.
- [[PAM1 mutation probability matrix]] — counts → probabilities; ~99% diagonal.
- [[PAM matrix extrapolation]] — (PAM1)ⁿ; PAM0 identity → PAM2000 chance.
- [[log-odds score]] — s=10·log(q/p), the engine of PAM & BLOSUM (MATH_UNRAVELING).
- [[BLOSUM matrix]] — BLOck SUbstitution Matrix; BLOSUM62 = BLAST default.
- [[PAM vs BLOSUM]] — model vs empirical; the inverse-numbering trap.
- [[twilight zone]] — ~20–25% identity; homology undetectable from sequence below it.

## Exercises
- [[exercise-needleman-wunsch-worked]] — fill & trace an NW matrix to 53% identity.
- [[exercise-sequence-identity-percent]] — compute % identity/similarity (gap caveat).
- [[exercise-dot-plot-construction]] — build a dot plot and read its patterns.
- [[exercise-smith-waterman-local]] — Smith–Waterman global vs local on one peptide pair (AL ⊄ AG).
- [[exercise-evalue-interpretation]] — compute & read E-values / p-values.
- [[exercise-blosum62-scoring]] — score an alignment with BLOSUM62 → 15.
- [[exercise-log-odds-score]] — compute S(W,W) ≈ 17.4 and interpret it.

## Source maps
- [[Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26]] — raw→wiki crosswalk for Lecture L3.
- [[Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO]] — raw→wiki crosswalk for Lecture L4.
