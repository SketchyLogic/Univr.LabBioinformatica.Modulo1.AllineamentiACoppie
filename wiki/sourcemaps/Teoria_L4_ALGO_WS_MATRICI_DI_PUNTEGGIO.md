---
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Source map — Teoria L4: ALGO_WS_MATRICI_DI_PUNTEGGIO

**Summary**: Birdseye crosswalk for [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf|Teoria L4 (Dell'Orco, UniVR)]] — a 12-page deck (**48 slides**, 4 per page; page *N* = slides *4N−3…4N*), titled *Allineamenti di sequenze 2 — Matrici di Sostituzione*. It extends L3 with **local alignment & gap penalties**, **statistical significance**, and **substitution matrices (PAM/BLOSUM)**. Each raw span below maps to the wiki content it produced.

---

| Raw span | Topic | Wiki targets | `PATH__` |
| --- | --- | --- | --- |
| p.1 sl.2–4 | Gap-penalty function `w(k)=g+e(k−1)`; init from PAM/BLOSUM; the 3 moves | [[affine gap penalty]] | `ComputerScience/Algorithms/DynamicProgramming` |
| p.2 sl.5–6 | EBI `water`; global vs local; local = add `0` | [[global vs local alignment]], [[Smith-Waterman algorithm]] | `Bioinformatics/SequenceAnalysis`, `ComputerScience/Algorithms/DynamicProgramming` |
| p.2 sl.7–8 | ESEMPIO 1–2 (global vs local; AL ⊄ AG) | [[exercise-smith-waterman-local]] | `ComputerScience/Algorithms/DynamicProgramming` |
| p.3 sl.9 | Local ≈ BLAST/DB search; score not absolute | [[global vs local alignment]] | `Bioinformatics/SequenceAnalysis` |
| p.3 sl.10–12 | Significance question; **Z-score** (shuffling) | [[statistical significance of an alignment]], [[Z-score (alignment)]] | `Math/Statistics/SignificanceTesting`, `Bioinformatics/SequenceAnalysis` |
| p.4 sl.13 | **E-value** `Kmn·e^(−λx)` (Karlin–Altschul) | [[E-value (Karlin-Altschul)]] | `Math/Statistics/SignificanceTesting`, `Bioinformatics/SequenceAnalysis` |
| p.4 sl.14 | **Gumbel** p-value `1−e^(−E)`; in practice; (slide drops a minus) | [[Gumbel distribution and the p-value]], [[Karlin-Altschul p-value erratum]] | `Math/Statistics/SignificanceTesting`, `Bioinformatics/SequenceAnalysis` |
| p.4 sl.15–16 | Scoring matrices 20×20 symmetric; aa-similarity Venn | [[substitution matrix]], [[amino acid similarity]] | `Bioinformatics/SequenceAnalysis` |
| p.5 sl.17–18 | Zuckerkandl & Pauling substitutions in 18 globins | [[amino acid similarity]] | `Bioinformatics/SequenceAnalysis` |
| p.5 sl.19–20 | Goal: PAM250…PAM10 score matrices (W·W, W·T examples) | [[log-odds score]], [[PAM matrix extrapolation]] | `Bioinformatics/SequenceAnalysis`, `Bioinformatics/MolecularEvolution` |
| p.6 sl.21–22 | PAM = point accepted mutation; Dayhoff; PAM1 = 1% / >85% | [[PAM (Point Accepted Mutation)]] | `Bioinformatics/MolecularEvolution` |
| p.6–7 sl.23–27 | 34 superfamilies — PAMs/100My (Ig κ 37 … ubiquitin 0) | [[PAM (Point Accepted Mutation)]] (Stats) | `Bioinformatics/MolecularEvolution` |
| p.7 sl.28 | Observed substitution **counts** (Dayhoff 1978) | [[PAM1 mutation probability matrix]] | `Bioinformatics/MolecularEvolution` |
| p.8 sl.29 | Relative mutability (Ala≡100) | [[relative mutability]] | `Bioinformatics/MolecularEvolution` |
| p.8 sl.30 | Normalised aa frequencies; codon link | [[amino acid frequencies]] | `Bioinformatics/SequenceAnalysis` |
| p.8 sl.31–32 | MSA conservation; **PAM1 probability** matrix | [[PAM1 mutation probability matrix]] | `Bioinformatics/MolecularEvolution` |
| p.9 sl.33–36 | Substitution matrices ∝ P(i→j); `(PAM1)ⁿ`; PAM0; PAM2000 | [[substitution matrix]], [[PAM matrix extrapolation]] | `Bioinformatics/MolecularEvolution` |
| p.10 sl.37–39 | PAM250 prob; **log-odds** `10log(q/p)`; S(W,W)≈17 | [[PAM matrix extrapolation]], [[log-odds score]], [[exercise-log-odds-score]] | `Bioinformatics/SequenceAnalysis`, `Bioinformatics/MolecularEvolution` |
| p.10–11 sl.40–41 | PAM heatmaps; score-vs-PAM curve | [[PAM vs BLOSUM]], [[twilight zone]] | `Bioinformatics/SequenceAnalysis`, `Bioinformatics/MolecularEvolution` |
| p.11 sl.42–44 | BLOSUM (BLOCKS, BLOSUM62, λ=2); numbering | [[BLOSUM matrix]] | `Bioinformatics/SequenceAnalysis` |
| p.12 sl.45 | BLOSUM62 matrix; worked VDS-CY/VESLCY → 15 | [[exercise-blosum62-scoring]], [[BLOSUM matrix]] | `Bioinformatics/SequenceAnalysis` |
| p.12 sl.46 | BLOSUM vs PAM; inverse numbering; correspondences | [[PAM vs BLOSUM]] | `Bioinformatics/SequenceAnalysis` |
| p.12 sl.47–48 | Twilight zone; PAM milestones; <20–25% | [[twilight zone]] | `Bioinformatics/MolecularEvolution` |

## Figures (embedded as PDF pages)
No `raw/graphics/` folder exists, so figures are referenced via `[[raw/...pdf#page=N|caption]]`: global-vs-local schematic (p.2), aa-similarity Venn (p.4), PAM0/PAM2000 matrices (p.9), twilight-zone curve (p.12) are embedded in their entries; others (Z-score & Gumbel curves p.3–4, Zuckerkandl table p.5, Dayhoff trees p.6, ubiquitin BLAST p.7, PAM1 matrix p.8, PAM250 log-odds + heatmaps p.10, BLOSUM62 matrix p.12) are available by page reference.

## Source corrections
- **Slide 14** prints the p-value as $1-\exp(Kmn\,e^{-\lambda x})$ (missing the inner minus → negative probabilities). The wiki uses the correct $p=1-e^{-E}$ and documents the discrepancy in [[Karlin-Altschul p-value erratum]].
- The slides label the 1976 affine-gap work "Waterman–Smith" and the 1981 local method "Smith–Waterman"; the wiki standardises on **Smith–Waterman** (noted once in [[affine gap penalty]]).

## Gaps / not yet ingested
- **BLAST / FASTA** are referenced as faster heuristics for database search but deferred to a later lecture (only cross-linked from [[global vs local alignment]] / [[Smith-Waterman algorithm]]).
- The **bit-score** normalisation ($S' = (\lambda S - \ln K)/\ln 2$) is implied by the significance theory but not in the slides; mentioned only in passing.
- Full numeric **PAM250 / BLOSUM62 tables** are shown as figures, not transcribed; the worked examples ([[exercise-blosum62-scoring]], [[exercise-log-odds-score]]) use the specific cells the slides highlight.
- **Gotoh's** O(mn) affine-gap algorithm and **Hirschberg** linear space are wiki enrichments (cool facts), not in the source.
