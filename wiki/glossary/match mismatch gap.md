---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentFoundations
foundational: 5
prereqs: 1
density: 1
value: 5
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# match mismatch gap

Every column of a [[pairwise alignment]] is exactly one of three outcomes, each mirroring a kind of evolutionary event: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=5|L3 p.5]]

- **Match** — the two residues are **identical** ("residui appaiati"). Evolutionarily: no change.
- **Mismatch** — the two residues **differ** — a **substitution** (point mutation). The position is aligned but the letters are not the same.
- **Gap** — one sequence has a residue, the other has a dash `-`. This represents an **indel** (**in**sertion or **del**etion): a residue was inserted in one lineage or deleted in the other.

```
L A   C A - S A   N U O V A      match: L↔L,  A↔A …
L A   C A S S A   V U O T A      mismatch: N↔V (substitution)
                                 gap: -↔S (indel)
```

These three are the alphabet of every alignment and of every scoring scheme: a typical scheme rewards matches (`+1`), neutral/penalises mismatches (`0`), and penalises gaps (`−1`) — see [[Needleman-Wunsch algorithm]]. Gaps are penalised because indels are evolutionarily **less frequent** than substitutions, so an alignment should not invent them freely.

> [!Caution] A gap is one event, not one residue
> A run of several dashes usually reflects a **single** insertion/deletion event of that length, not many independent ones — which is why advanced schemes use a larger "gap-open" penalty plus a smaller "gap-extend" penalty (cf. the EMBOSS `needle` parameters).

# TLDR
Every alignment column is exactly one of three outcomes: a **match** (identical residues), a **mismatch** (a substitution), or a **gap** (an indel). Gaps are penalized most because indels are evolutionarily rarer than substitutions.

# Recitation Anchors
- Three column outcomes: **match / mismatch / gap**
- Match = identical (no change); mismatch = substitution; gap = indel (dash `-`)
- Simple scoring: **+1 / 0 / −1**
- Gaps penalized most (indels rarer than substitutions)
- A run of dashes = one indel event → gap-open vs gap-extend penalties

> [!Cool] Cool fact
> Indels are rarer than substitutions but structurally louder: in the lecture's globin example, the alignment positions carrying **gaps** are precisely the regions where the two 3-D structures stop superimposing — see [[sequence structure function]]. [source](https://doi.org/10.1016/0022-2836(70)90057-4)

# Read aloud
KP.0.Definition: Three outcomes per column.
Once two sequences are stacked one on top of the other, every single column is one of just three things: a match, a mismatch, or a gap. And each one mirrors a kind of evolutionary event.

KP.1.Definition: Match and mismatch.
A match is when the two residues are identical — nothing changed. A mismatch is when they differ; the position lines up but the letters don't, which represents a substitution, a point mutation.

KP.2.Definition: Gap.
A gap is when one sequence has a residue and the other has a dash. That dash stands for an indel — an insertion or a deletion — meaning a residue was added in one lineage or removed in the other.

KP.3.Concept: Why gaps are penalised.
These three outcomes are the alphabet of every scoring scheme. A simple scheme might give plus one for a match, zero for a mismatch, and minus one for a gap. Gaps cost the most because insertions and deletions happen less often than substitutions in evolution, so the algorithm shouldn't sprinkle them around freely.

KP.4.CoolFact: Gaps mark structural breaks.
And here's the cool part — although indels are rarer than substitutions, they're structurally loud. In the globin example from the lecture, the very positions that carry gaps are exactly where the two proteins' three-dimensional structures stop matching up.

# Question and Answer
Q. What are the three possible outcomes of an alignment column?
A. Match (identical residues), mismatch (substitution), gap (indel).

Q. What evolutionary event does a mismatch represent?
A. A substitution — a point mutation changing one residue to another.

Q. What does a gap represent, and what does the symbol look like?
A. An indel (insertion or deletion), shown as a dash `-` opposite a residue.

Q. In a simple scheme, what scores go to match/mismatch/gap?
A. +1 for a match, 0 for a mismatch, −1 for a gap (as in the lecture's Needleman–Wunsch example).

Q. Why are gaps penalised more heavily than mismatches?
A. Because indels are evolutionarily rarer than substitutions, so the alignment shouldn't introduce them gratuitously.

Q. Why do gap-open and gap-extend penalties differ?
A. A run of dashes usually reflects one multi-residue indel event, so opening a gap is penalised more than extending an existing one.
