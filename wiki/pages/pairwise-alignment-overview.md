---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Pairwise Alignment — Overview (Modulo 1: L3–L4)

**Summary**: The top-level map of **Modulo 1, *Allineamenti a Coppie***, spanning **Lecture L3** (foundations → dot plots → Needleman–Wunsch) and **Lecture L4** (local alignment & gap penalties → statistical significance → substitution matrices). It walks from *why* we align sequences all the way to *how* the scores are derived from evolution and judged for significance.
**Sources**: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf|Teoria L3]] · [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf|Teoria L4]] (Dell'Orco, UniVR)

---

[[pairwise alignment]] is one of bioinformatics' foundational operations: comparing two sequences to assess their [[identity conservation similarity|similarity]] and possible [[homology]]. The module splits into **six arcs** — three per lecture.

## — Lecture L3 —

### Arc 1 — [[alignment-foundations|Alignment Foundations]]
*What alignment is and the biological vocabulary that gives it meaning.*
[[pairwise alignment]] and its [[applications of pairwise alignment|applications]]; [[protein vs DNA alignment|proteins vs DNA]]; [[identity conservation similarity|identity / conservation / similarity]]; [[homology]] and [[homology vs similarity|homology ≠ similarity]]; [[sequence structure function|sequence→structure→function]]; [[orthologs]] vs [[paralogs]] ([[orthologs vs paralogs|compared]]); [[match mismatch gap]] and [[edit distance and parsimony]].
→ Review: [[alignment-foundations-key-concepts]]

### Arc 2 — [[dot-plots|Dot Plots]]
*The simplest visual method, and how to make it usable.*
The [[dot plot]] and its [[dot plot patterns|patterns]] ([[dot plot patterns visualized|visualized]]); the [[sliding window]]; the [[scoring matrix]]; and [[sequence identity and similarity percent|% identity & similarity]].
→ Review: [[dot-plots-key-concepts]]

### Arc 3 — [[dynamic-programming-alignment|Dynamic Programming Alignment]]
*Finding the provably optimal alignment, indels included.*
[[dynamic programming]] and [[optimal substructure]]; the [[Needleman-Wunsch algorithm]] ([[Needleman-Wunsch correctness|why it's optimal]]); its [[Needleman-Wunsch recurrence|recurrence]]; and [[traceback]].
→ Review: [[dynamic-programming-alignment-key-concepts]]

## — Lecture L4 —

### Arc 4 — [[local-alignment|Local Alignment & Gap Penalties]]
*Patch NW's gaps, then extend it from global to local.*
The [[affine gap penalty]] (gap-open + gap-extend); [[global vs local alignment]]; and the [[Smith-Waterman algorithm]] (NW + a `0` option).
→ Review: [[local-alignment-key-concepts]]

### Arc 5 — [[alignment-significance|Alignment Significance]]
*Is the score meaningful, or chance?*
[[statistical significance of an alignment]]; the global [[Z-score (alignment)|Z-score]]; the local [[E-value (Karlin-Altschul)|E-value]] and [[Gumbel distribution and the p-value|Gumbel p-value]] (with a source [[Karlin-Altschul p-value erratum|erratum]]).
→ Review: [[alignment-significance-key-concepts]]

### Arc 6 — [[substitution-matrices|Substitution Matrices]]
*Where the scores come from — evolution.*
[[amino acid similarity]] and the [[substitution matrix]]; the [[PAM (Point Accepted Mutation)|PAM]] family ([[relative mutability]], [[amino acid frequencies]], [[PAM1 mutation probability matrix]], [[PAM matrix extrapolation]], [[log-odds score]]); the [[BLOSUM matrix|BLOSUM]] family; [[PAM vs BLOSUM]]; and the [[twilight zone]].
→ Review: [[substitution-matrices-key-concepts]]

## Exercises
- L3: [[exercise-needleman-wunsch-worked]] · [[exercise-sequence-identity-percent]] · [[exercise-dot-plot-construction]]
- L4: [[exercise-smith-waterman-local]] · [[exercise-evalue-interpretation]] · [[exercise-blosum62-scoring]] · [[exercise-log-odds-score]]

## Connections
- **Role of the bioinformatician** — alignment is the daily bread of interpreting sequence relationships; reading an E-value and choosing a matrix are judgement calls.
- **Modern & precision medicine** — alignment + substitution scores underlie variant-effect interpretation and drug-target/family identification.
- **Data mining** — local alignment + BLAST is pattern extraction from massive databases; PAM extrapolation is a Markov process.

## Other sources
- EBI EMBOSS tools: <https://www.ebi.ac.uk/Tools/psa/> (`needle` = global/NW, `water` = local/Smith–Waterman).
- Needleman & Wunsch (1970) <https://doi.org/10.1016/0022-2836(70)90057-4>; Smith & Waterman (1981) <https://doi.org/10.1016/0022-2836(81)90087-5>; Karlin & Altschul (1990) <https://doi.org/10.1073/pnas.87.6.2264>.

## Read aloud
This is the overview of Modulo One, on pairwise alignment, and it covers two lectures, three arcs each. Lecture three builds the foundations. First, the vocabulary: what alignment is and what it's for, why protein sequences are often more informative than DNA, the three measures — identity, conservation, and similarity — and the key idea of homology, shared ancestry, and how it differs from mere similarity. Then dot plots, the simplest visual way to compare two sequences, cleaned up with a sliding window and a scoring matrix. And then dynamic programming: the Needleman–Wunsch algorithm, which finds the single best global alignment by building it from optimal pieces, with its recurrence and its traceback. Lecture four takes it further. It first patches Needleman–Wunsch's crude gap handling with the affine gap penalty — a big cost to open a gap, a small cost to extend it — and then extends alignment from global to local with the Smith–Waterman algorithm, which is just Needleman–Wunsch with a zero added to the recurrence. Next it asks whether a score is even meaningful: for global alignments you shuffle and compute a Z-score, and for local alignments you use the Karlin–Altschul E-value and its Gumbel distribution. Finally it explains where the scores themselves come from — evolution — through the PAM and BLOSUM families of substitution matrices, the log-odds formula that powers both, and the twilight zone, the point below about twenty percent identity where sequence similarity can no longer reveal homology and you must turn to structure.
