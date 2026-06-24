---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Operation Log

Append-only record of wiki changes (newest first).

## 2026-06-23 — Add mandatory `# TLDR` + `# Recitation Anchors` to all glossary entries
- **Reason**: `CLAUDE.md` updated to require both sections on every glossary entry (previously optional). Recitation Anchors is a dotted list of recall hooks.
- **Scope**: all **24** glossary entries (21 concepts + 3 exercises) — none previously had either section.
- **Placement**: inserted after the body, immediately before the `[!Cool]` callout, per the new ordering rule.
- No frontmatter dates changed (all entries already carry `LastUpdateAt: 2026-06-23`).

## 2026-06-23 — Ingest: Teoria L3 *Allineamenti a Coppie*
- **Source**: `raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf` (11 pages, ≈44 slides; Dell'Orco, UniVR Lab. Bioinformatica, Modulo 1).
- **Plan**: `PLAN-20260623.md` (approved — 3 arcs; new PATH `Bioinformatics/MolecularEvolution`; trimmed/merged a few entries).
- **New modules/arcs**: `AlignmentFoundations`, `DotPlots`, `DynamicProgrammingAlignment`.
- **New PATH tag**: `PATH__/Bioinformatics/MolecularEvolution` (homology/orthologs/paralogs).
- **Pages created (7)**: [[pairwise-alignment-overview]]; arc pages [[alignment-foundations]], [[dot-plots]], [[dynamic-programming-alignment]]; key-concepts [[alignment-foundations-key-concepts]], [[dot-plots-key-concepts]], [[dynamic-programming-alignment-key-concepts]].
- **Glossary created (21)**: pairwise alignment, applications of pairwise alignment, protein vs DNA alignment, identity conservation similarity, homology, homology vs similarity, sequence structure function, orthologs, paralogs, orthologs vs paralogs, match mismatch gap, edit distance and parsimony, dot plot, dot plot patterns, sliding window, scoring matrix, sequence identity and similarity percent, dynamic programming, Needleman-Wunsch algorithm, Needleman-Wunsch recurrence (MATH_UNRAVELING), traceback.
- **Exercises created (3)**: exercise-needleman-wunsch-worked, exercise-sequence-identity-percent, exercise-dot-plot-construction.
- **Merges applied**: codon degeneracy → [[protein vs DNA alignment]]; optimal substructure → [[dynamic programming]]; identity/conservation/similarity → single [[identity conservation similarity]] entry.
- **Source map**: [[Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26]].
- **Updated**: `index.md`, `study_path.md` created.
- **Deferred** (see source map gaps): standalone codon table, Smith–Waterman/local alignment, BLAST, gap-open/extend detail.
