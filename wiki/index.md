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

Table of contents for the wiki. See also [[study_path]] for a suggested order and [[log]] for the change history.

## Overview & navigation pages
- [[pairwise-alignment-overview]] — top-level map of Lecture L3.
- [[alignment-foundations]] — Arc 1: what alignment is + the vocabulary.
- [[dot-plots]] — Arc 2: the dot-matrix method and its refinements.
- [[dynamic-programming-alignment]] — Arc 3: Needleman–Wunsch.

## Key Concepts (review sheets)
- [[alignment-foundations-key-concepts]]
- [[dot-plots-key-concepts]]
- [[dynamic-programming-alignment-key-concepts]]

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

## Exercises
- [[exercise-needleman-wunsch-worked]] — fill & trace an NW matrix to 53% identity.
- [[exercise-sequence-identity-percent]] — compute % identity/similarity (gap caveat).
- [[exercise-dot-plot-construction]] — build a dot plot and read its patterns.

## Source maps
- [[Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26]] — raw→wiki crosswalk for Lecture L3.
