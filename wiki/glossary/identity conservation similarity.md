---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentFoundations
foundational: 5
prereqs: 1
density: 2
value: 5
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# identity conservation similarity

Three tightly linked measurements describe how related two aligned sequences are. They build on each other: **similarity = identity + conservation**. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=2|L3 p.2]]

- **Identity** — the measure of how far two sequences (nucleotides or amino acids) are **invariant**, i.e. literally the *same* letter in the same aligned position. *Example:* "32% identity" means that, across 100 aligned positions, **32 residues are identical, position-by-position**. It is the strictest criterion.
- **Conservation** — modifications at a specific position that **preserve the physico-chemical properties** of the original residue (e.g. swapping leucine for isoleucine — both small and hydrophobic). Applies mostly to amino acids; rarely to nucleotides. A conserved position is *not* identical but is biochemically equivalent.
- **Similarity** (*similitudine*) — the measure of how far two sequences are **correlated**. It is **based on identity + conservation**: it credits both exact matches and conservative substitutions, so it is always ≥ identity.

> [!Caution] Identity ⊆ similarity
> Every identical position is also "similar", but not every similar position is identical. Quoting identity and similarity as if they were the same thing is a classic mistake — they are measured against different criteria (see [[sequence identity and similarity percent]]).

The criterion that decides whether two residues count as "similar" comes from a **[[scoring matrix]]**: it assigns a score to every residue pair, encoding how biochemically interchangeable they are. Both quantities can be expressed as percentages — see [[sequence identity and similarity percent]] — and are the raw evidence for inferring [[homology]].

# TLDR
Three stacked measures of relatedness: **identity** (literally the same residue), **conservation** (a property-preserving substitution), and **similarity = identity + conservation** (so similarity is always ≥ identity). A scoring matrix decides what counts as "similar".

# Recitation Anchors
- **Similarity = identity + conservation**
- Identity = same letter, same position (strictest); "32%" = 32/100 identical
- Conservation = property-preserving swap (Leu↔Ile); mostly proteins
- Similarity ≥ identity always; identity ⊆ similarity
- A **scoring matrix** decides what counts as "similar"

> [!Cool] Cool fact
> Two proteins can share well under **20%** sequence identity yet fold into nearly the same 3-D shape — the "twilight zone" of sequence similarity — which is exactly why **conservation** and **similarity**, not identity alone, are needed to detect distant relationships. [source](https://doi.org/10.1093/protein/12.2.85)

# Read aloud
KP.0.Definition: Identity.
There are three related ways to measure how alike two aligned sequences are, and they stack on top of each other. The first is identity. Identity is how often the two sequences carry the very same letter in the same position. When we say two proteins are thirty-two percent identical, we mean that out of a hundred aligned spots, thirty-two are exactly the same residue. It's the strictest measure.

KP.1.Definition: Conservation.
The second is conservation. Sometimes a position isn't identical, but the substitute amino acid has the same physical and chemical character — say, swapping leucine for isoleucine, both small and water-fearing. The residue changed, but its properties were preserved. That's a conserved position, and it mostly matters for proteins rather than DNA.

KP.2.Definition: Similarity.
The third is similarity. Similarity measures how correlated two sequences are, and it's built from the first two: it's identity plus conservation. It gives credit both for exact matches and for conservative substitutions, so similarity is always at least as high as identity, and usually higher.

KP.3.Connection: Where the "similar" judgement comes from.
What decides whether two different residues count as similar? A scoring matrix — a table that gives every pair of residues a score reflecting how interchangeable they are biochemically. Both identity and similarity can be reported as percentages, and together they're the evidence we use to argue that two sequences are homologous.

KP.4.CoolFact: The twilight zone.
And here's the cool part — two proteins can share less than twenty percent identity and still fold into almost the same shape. That region is nicknamed the twilight zone, and it's the very reason we lean on conservation and similarity, not identity alone, to catch distant relatives.

# Question and Answer
Q. Give the one-line relationship between the three measures.
A. Similarity = identity + conservation; similarity ≥ identity always.

Q. What does "32% identity" mean precisely?
A. Across the aligned positions, 32 out of every 100 residues are the identical letter in the same position.

Q. Define conservation and give an example.
A. A substitution that preserves the residue's physico-chemical properties, e.g. leucine→isoleucine (both small, hydrophobic). The residue differs but its character is kept.

Q. Why is conservation mostly relevant to proteins, not nucleotides?
A. Amino acids have varied biophysical properties that can be preserved across substitutions; the four nucleotides lack such graded similarity.

Q. Which tool decides whether two residues count as "similar"?
A. A scoring matrix, which scores each residue pair by biochemical interchangeability. See [[scoring matrix]].

Q. Can two sequences be very similar but not very identical? Explain.
A. Yes — if many positions are conservative substitutions rather than exact matches, similarity is high while identity is lower (the "twilight zone").
