---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Pairwise Alignment — Overview (Lecture L3)

**Summary**: The top-level map of Lecture L3, *Allineamenti a Coppie*. It walks from **why** we align sequences and the vocabulary of relatedness, through the visual **dot-plot** method, to the **dynamic-programming** algorithm (Needleman–Wunsch) that finds the optimal alignment.
**Sources**: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf|Teoria L3 — Allineamenti a Coppie (Dell'Orco, UniVR)]]

---

[[pairwise alignment]] is one of bioinformatics' foundational operations: comparing two sequences to assess their [[identity conservation similarity|similarity]] and the possibility of [[homology]]. This lecture splits into **three arcs**.

## Arc 1 — [[alignment-foundations|Alignment Foundations]]
*What alignment is and the biological vocabulary that gives it meaning.*
Start with [[pairwise alignment]] and its [[applications of pairwise alignment|applications]]; why [[protein vs DNA alignment|proteins can beat DNA]]; the trio [[identity conservation similarity|identity / conservation / similarity]]; then [[homology]] and the crucial [[homology vs similarity|homology ≠ similarity]] distinction; the [[sequence structure function|sequence→structure→function]] chain; the two homology types ([[orthologs]] vs [[paralogs]], compared in [[orthologs vs paralogs]]); and the comparison primitives [[match mismatch gap]] and [[edit distance and parsimony]].
→ Review: [[alignment-foundations-key-concepts]]

## Arc 2 — [[dot-plots|Dot Plots]]
*The simplest visual method, and how to make it usable.*
The [[dot plot]] and its [[dot plot patterns|patterns]] (inversions, repeats, deletions); noise reduction via the [[sliding window]]; measuring similarity with a [[scoring matrix]]; and quantifying results as [[sequence identity and similarity percent|% identity and % similarity]].
→ Review: [[dot-plots-key-concepts]]

## Arc 3 — [[dynamic-programming-alignment|Dynamic Programming Alignment]]
*Finding the provably optimal alignment, indels included.*
[[dynamic programming]] and optimal substructure; the [[Needleman-Wunsch algorithm]]; its [[Needleman-Wunsch recurrence|scoring recurrence]] unraveled; and [[traceback]] to recover the alignment.
→ Review: [[dynamic-programming-alignment-key-concepts]]

## Exercises
- [[exercise-needleman-wunsch-worked]] — fill & trace an NW matrix to 53% identity.
- [[exercise-sequence-identity-percent]] — compute % identity/similarity (with the gap caveat).
- [[exercise-dot-plot-construction]] — build a dot plot and read its patterns.

## Connections
- **Role of the bioinformatician** — alignment is the daily bread of interpreting sequence relationships and bridging biology with computation.
- **Modern medicine & precision medicine** — alignment underlies variant interpretation and drug-target/family identification downstream.
- **Data mining** — comparing sequences against databases (BLAST) is pattern extraction from massive datasets.

## Other sources
- EBI EMBOSS tools: <https://www.ebi.ac.uk/Tools/psa/> (`needle` = global/NW, `water` = local/Smith–Waterman).
- Needleman & Wunsch (1970), *J. Mol. Biol.* <https://doi.org/10.1016/0022-2836(70)90057-4>

## Read aloud
This is the overview of Lecture Three, on pairwise alignment. Pairwise alignment means lining up two sequences to see how alike they are and whether they share a common ancestor. The lecture unfolds in three parts. The first part builds the vocabulary: what alignment is and what it's for, why protein sequences are often more informative than DNA, the three measures of likeness — identity, conservation, and similarity — and the all-important idea of homology, which is shared ancestry, and how that differs from mere similarity. It also covers how sequence shapes structure and structure shapes function, the two flavours of homology called orthologs and paralogs, and the basic building blocks of an alignment: matches, mismatches, and gaps, and the idea of edit distance and evolutionary parsimony. The second part is about dot plots, the simplest visual way to compare two sequences, the patterns they reveal like inversions and repeats, how a sliding window cleans up the noise, how a scoring matrix lets us measure similarity rather than just identity, and how to report results as percentages. The third part is the dynamic-programming approach: the Needleman–Wunsch algorithm, which finds the single best alignment by building it up from optimal smaller pieces, the recurrence that scores each cell, and the traceback that recovers the final alignment. Three hands-on exercises tie it all together.
