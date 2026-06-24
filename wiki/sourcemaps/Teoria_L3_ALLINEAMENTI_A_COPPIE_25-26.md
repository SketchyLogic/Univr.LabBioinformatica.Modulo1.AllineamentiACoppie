---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Source map — Teoria L3: Allineamenti a Coppie

**Summary**: Birdseye crosswalk for [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf|Teoria L3 (Dell'Orco, UniVR Lab. Bioinformatica)]] — an 11-page slide deck (≈44 slides) introducing pairwise sequence alignment: biological foundations, dot plots, and the Needleman–Wunsch dynamic-programming algorithm. Each raw span below maps to the wiki content it produced.

---

| Raw span | Topic | Wiki targets | `PATH__` |
| --- | --- | --- | --- |
| p.1 sl.1–2 | History — globin alignment (1961) | [[pairwise alignment]] | `Bioinformatics/SequenceAnalysis` |
| p.1 sl.3 | Why alignment is fundamental | [[applications of pairwise alignment]] | `Bioinformatics/SequenceAnalysis` |
| p.1 sl.4 + p.2 sl.5 | Protein vs DNA; codon table/degeneracy | [[protein vs DNA alignment]] | `Bioinformatics/SequenceAnalysis`, `Bioinformatics/Genomics` |
| p.2 sl.6 | Definition of pairwise alignment | [[pairwise alignment]] | `Bioinformatics/SequenceAnalysis` |
| p.2 sl.7 | Identity / conservation / similarity | [[identity conservation similarity]] | `Bioinformatics/SequenceAnalysis` |
| p.2 sl.8 | Homology (qualitative) vs similarity | [[homology]], [[homology vs similarity]] | `Bioinformatics/MolecularEvolution` |
| p.3 sl.9–12 | Seq→struct→function; globin examples | [[sequence structure function]] | `Bioinformatics/SequenceAnalysis` |
| p.4 sl.13–16 | Orthologs vs paralogs; globin trees | [[orthologs]], [[paralogs]], [[orthologs vs paralogs]] | `Bioinformatics/MolecularEvolution` |
| p.5 sl.17–18 | String transformation; parsimony; match/mismatch/gap | [[match mismatch gap]], [[edit distance and parsimony]] | `Bioinformatics/SequenceAnalysis` |
| p.5 sl.19–20 + p.6 sl.21 | Dot plot; patterns (inversion, repeat, deletion) | [[dot plot]], [[dot plot patterns]] | `Bioinformatics/SequenceAnalysis` |
| p.6 sl.22–24 | Noise, sliding window (g, L=2g+1, N) | [[sliding window]] | `Bioinformatics/SequenceAnalysis` |
| p.7 sl.25–27 | Threshold, scoring matrix, DOTTER | [[scoring matrix]] | `Bioinformatics/SequenceAnalysis` |
| p.7 sl.28 | % identity & % similarity formulas | [[sequence identity and similarity percent]] | `Bioinformatics/SequenceAnalysis` |
| p.8 sl.29–32 | DP alignment; NW; rules; optimal substructure | [[dynamic programming]], [[Needleman-Wunsch algorithm]] | `ComputerScience/Algorithms/DynamicProgramming` |
| p.9 sl.33–36 | NW worked example → 53% identity | [[exercise-needleman-wunsch-worked]], [[traceback]] | `ComputerScience/Algorithms/DynamicProgramming` |
| p.10 sl.37 | Formal recurrence S(i,j) | [[Needleman-Wunsch recurrence]] | `ComputerScience/Algorithms/DynamicProgramming` |
| p.10 sl.38 | NW as dynamic programming | [[dynamic programming]] | `ComputerScience/Algorithms/DynamicProgramming` |
| p.10–11 sl.39–40 | EMBOSS needle (EBI); β/α-globin run | [[exercise-sequence-identity-percent]], [[Needleman-Wunsch algorithm]] | `ComputerScience/Algorithms/DynamicProgramming` |

## Figures (embedded as PDF pages)
Codon table (p.2), globin superposition (p.3), ortholog/paralog trees (p.4), dot-plot patterns (p.6), sliding-window diagram (p.6), scoring-matrix example (p.7), NW worked matrix (p.9), EMBOSS output (p.11). No `raw/graphics/` folder exists, so figures are referenced via `[[raw/...pdf#page=N|caption]]`.

## Gaps / not yet ingested
- The **genetic-code/codon table** itself is referenced only as supporting context inside [[protein vs DNA alignment]]; no standalone codon-table entry was created.
- **Smith–Waterman / local alignment** is mentioned only as a contrast (in [[Needleman-Wunsch recurrence]] and [[traceback]]); it belongs to a later lecture and was not given its own entry.
- **BLAST** is flagged as "next lectures" and only referenced, not ingested here.
- **Gap-open vs gap-extend** penalties are noted in passing ([[match mismatch gap]]); the EMBOSS parameters (gap 10.0 / extend 0.5) are recorded but not expanded.
