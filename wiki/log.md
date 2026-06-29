---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-29
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Operation Log

Append-only record of wiki changes (newest first).

## 2026-06-29 — Update: [[exercise-evalue-interpretation]] — E-value vs p-value intuition
- **Reason**: user wanted an intuitive contrast of E-value and p-value.
- **Change**: added an "E-value vs p-value (intuition)" subsection — E = expected *count* of chance hits (unbounded, scales with search size) vs p = *probability* of at least one (capped at 1), with a bus-stop `[!Hint]` analogy explaining why $p\approx E$ when small and why they diverge when large ($p=1-e^{-E}$). Mirrored as Read aloud KP.3.Concept (verdict→KP.4, CoolFact→KP.5) and a new Q&A pair. `LastUpdateAt` bumped to 2026-06-29.

## 2026-06-29 — Update: [[Z-score (alignment)]] — "best-of-many" intuition for non-normality
- **Reason**: user asked *why* alignment scores aren't normally distributed — wanted intuition, not derivation.
- **Change**: expanded the `[!Caution]` normal-distribution callout with the maximum-of-many-alignments → lopsided ("tallest person in a crowd") intuition; mirrored it as a new Read aloud beat (KP.4.Concept, CoolFact renumbered to KP.5) and a new Q&A pair. `LastUpdateAt` bumped to 2026-06-29.

## 2026-06-27 — Ingest: Teoria L4 *ALGO_WS_MATRICI_DI_PUNTEGGIO* (Allineamenti di sequenze 2 — Matrici di Sostituzione)
- **Source**: `raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf` (12 pages, 48 slides; Dell'Orco, UniVR Lab. Bioinformatica, Modulo 1).
- **Plan**: `PLAN-20260627-L4.md` (approved with inline answers — 3 arcs; dual significance PATH; expand overview; all exercises; keep entries split; correct K–A formula + erratum file; standardise on "Smith–Waterman").
- **New modules/arcs**: `LocalAlignment`, `AlignmentSignificance`, `SubstitutionMatrices` (→ 6 arcs total in Modulo 1).
- **New PATH tag**: `Math/Statistics/SignificanceTesting` (carried *alongside* `Bioinformatics/SequenceAnalysis` on the 5 significance entries, per user request — dual PATH).
- **Pages created (7)**: arc pages [[local-alignment]], [[alignment-significance]], [[substitution-matrices]]; key-concepts [[local-alignment-key-concepts]], [[alignment-significance-key-concepts]], [[substitution-matrices-key-concepts]]; source map [[Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO]].
- **Glossary created (19)**: Arc 4 — global vs local alignment, affine gap penalty (MATH_UNRAVELING), Smith-Waterman algorithm. Arc 5 — statistical significance of an alignment, Z-score (alignment) (MATH_UNRAVELING), E-value (Karlin-Altschul) (MATH_UNRAVELING), Gumbel distribution and the p-value, Karlin-Altschul p-value erratum. Arc 6 — substitution matrix, amino acid similarity, PAM (Point Accepted Mutation), relative mutability, amino acid frequencies, PAM1 mutation probability matrix, PAM matrix extrapolation, log-odds score (MATH_UNRAVELING), BLOSUM matrix, PAM vs BLOSUM, twilight zone.
- **Exercises created (4)**: exercise-smith-waterman-local, exercise-evalue-interpretation, exercise-blosum62-scoring, exercise-log-odds-score.
- **Source correction**: slide 14's p-value drops a minus sign → wiki uses $p=1-e^{-E}$; discrepancy documented in [[Karlin-Altschul p-value erratum]] (per user request, in its own file).
- **Existing entries updated (cross-links to L4)**: [[scoring matrix]] (→ substitution matrix/log-odds; `LastUpdateAt` bumped), [[match mismatch gap]] (→ affine gap penalty; bumped), [[Needleman-Wunsch recurrence]] (→ affine gap penalty, Smith-Waterman), [[Needleman-Wunsch algorithm]] (→ affine/SW limitations), [[traceback]] (→ local traceback).
- **Overview**: [[pairwise-alignment-overview]] expanded from "Lecture L3" to the **Modulo-1 (L3+L4)** map (6 arcs).
- **Updated**: `index.md` (3 new arc sections + 4 exercises + L4 source map), `study_path.md` (sections 4–6 + L4 exam list).

## 2026-06-27 — New entry: [[Needleman-Wunsch correctness]] (why the procedure is globally optimal)
- **Reason**: user pressed on a real gap — optimal substructure is *necessary* but doesn't prove the procedure yields the best alignment.
- **New glossary entry**: `Needleman-Wunsch correctness` (TYPE Concept/Theorem, EXAM_PREP) — two ingredients (optimal substructure + **exhaustive choice**), the $OPT$-vs-$S$ distinction, a tight two-direction induction (`# Argument`), the "no procedure can beat it / ties only" payoff, and caveats (scoring-relative; optimal ≠ biological). Cool fact: optimal MSA is NP-complete.
- **Linked from**: [[optimal substructure]] (new `[!Caution]` "necessary, not sufficient") and [[Needleman-Wunsch algorithm]].
- **Updated**: `index.md`, `study_path.md` (Arc 3 chain + exam list).

## 2026-06-27 — Explain the $i-k$ gap-length index in [[Needleman-Wunsch recurrence]]
- **Reason**: user confusion over why the vertical term is $S(i-k,j-1)$ ($k$ rows up) rather than one row up.
- **Edit**: added body section "**Why $i-k$ rather than $i-1$ — to model larger gaps**" ($k$ = gap length; scans whole column; original 1970 form + affine gaps; linear penalty collapses to $S(i-1,j)$, $O(mn)$ vs $O(mn(m+n))$).
- **Synced**: 2 Recitation Anchors, a Read aloud beat (new KP.5, CoolFact → KP.6), and 2 Q&A pairs. No new callout (note already has Hint + Example).

## 2026-06-27 — New entry: [[optimal substructure]] (justifies DP for alignment)
- **Reason**: user request for a dedicated note on the optimal-substructure property behind DP alignment.
- **New glossary entry**: `optimal substructure` (TYPE Concept/Argument, EXAM_PREP, MODULE DynamicProgrammingAlignment) — the three-way ending of an optimal alignment, the peel test, a full `# Argument` **cut-and-paste proof**, and the longest-vs-shortest-path cool fact.
- **Extracted from** the section inside [[dynamic programming]] (kept there as a brief treatment + pointer to the new note).
- **Re-pointed references** to the dedicated note in [[Needleman-Wunsch algorithm]], [[Needleman-Wunsch recurrence]], [[traceback]] (`LastUpdateAt` bumped on each).
- **Updated**: `index.md`, `study_path.md` (Arc 3 + exam list).

## 2026-06-27 — Clarify allowed path moves in [[Needleman-Wunsch algorithm]]
- **Reason**: user question — are path moves only orthogonal, or also diagonal?
- **Edit**: added an **Allowed moves** block (diagonal = no gap; vertical/horizontal = gap) + a `[!Caution]` that "forward only" means *direction*, not a ban on diagonals. Cross-linked to [[Needleman-Wunsch recurrence]] and [[dot plot patterns visualized]].
- **Synced**: Recitation Anchors, Read aloud (KP.1), and Q&A (2 new pairs); clarified the "forward only" practical rule. `LastUpdateAt` bumped.

## 2026-06-26 — New entry: [[dot plot patterns visualized]] (worked figure gallery)
- **Reason**: user request to visualize how [[dot plot patterns]] arise, with incrementally complex examples.
- **New glossary entry**: `dot plot patterns visualized` (TYPE Concept/Procedure, MODULE DotPlots) — six ASCII dot-plot figures built step by step: identity→main diagonal, substitution→hole, repeat→parallel diagonals, inversion→anti-diagonal, indel→shifted diagonal, DNA noise→sliding-window cleanup. Each grid is hand-verifiable.
- **Linked from**: [[dot plot patterns]] (added pointer + `LastUpdateAt`).
- **Updated**: `index.md`, `study_path.md` (added to Arc 2 / dot-plots flow).

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
