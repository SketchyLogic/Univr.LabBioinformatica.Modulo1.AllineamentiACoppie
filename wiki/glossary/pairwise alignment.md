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

# pairwise alignment

**Pairwise alignment** is the process that aligns **two** sequences (nucleotides or amino acids) so as to reach the maximum possible level of **[[identity conservation similarity|identity]]** — and, for proteins, **conservation** — in order to evaluate their degree of **[[identity conservation similarity|similarity]]** and the possibility of **[[homology]]** (descent from a common ancestor). [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=2|L3 p.2]]

It is one of the most fundamental operations in bioinformatics: it underpins deciding whether two genes/proteins are related, finding shared domains and motifs, database search (BLAST), and genome/transcriptome analysis — see [[applications of pairwise alignment]].

Aligning means writing the two sequences one above the other and inserting **gaps** where needed, so each column is one of three outcomes — a [[match mismatch gap|match, a mismatch, or a gap]]:

```
S A - S A   N U O V A     (gap '-' = an inserted/deleted residue)
S A S S A   V U O T A
```

The "best" alignment is the one a scoring scheme judges optimal — typically the most identical/similar residues with the fewest gaps, mirroring the idea that evolution follows the [[edit distance and parsimony|shortest path]]. *Pairwise* means exactly two sequences (contrast: *multiple* sequence alignment, many at once).

> [!Hint] Two things at once
> An alignment is both a **hypothesis** (these positions are evolutionarily equivalent) and a **measurement** (how similar the sequences are). The same matrix that scores similarity also tells you *where* the residues correspond.

# TLDR
Pairwise alignment lines up **two** sequences (inserting gaps) to maximize identity — and, for proteins, conservation. It is simultaneously a *hypothesis* about which residues correspond and a *measurement* of how similar the sequences are, and it is the foundation for inferring [[homology]].

# Recitation Anchors
- Align **two** sequences → maximize identity (+ conservation for proteins)
- Every column is one of three: **match / mismatch / gap**
- Both a **hypothesis** (corresponding positions) and a **measurement** (similarity)
- Foundation for: relatedness, domains/motifs, BLAST, genome analysis
- "Pairwise" = exactly two (contrast: multiple sequence alignment)
- Best alignment ≈ shortest evolutionary path (parsimony)

> [!Cool] Cool fact
> The very first protein sequence alignments predate computers: in **1961** Watson & Kendrew compared sperm-whale myoglobin to human hemoglobin **by hand**, and the [Needleman–Wunsch dynamic-programming algorithm](https://doi.org/10.1016/0022-2836(70)90057-4) that automated it only arrived in 1970.

# Read aloud
KP.0.Definition: What pairwise alignment is.
Pairwise alignment is the process of lining up two sequences — two stretches of DNA letters or two protein sequences — so that they match as well as possible. We slide them against each other and, where needed, insert gaps, until we reach the highest level of identity and, for proteins, conservation. The word "pairwise" simply means exactly two sequences at a time.

KP.1.Concept: Three outcomes per column.
Once the two sequences are stacked one above the other, every column is one of three things: a match, where the two letters are the same; a mismatch, where they differ; or a gap, where one sequence has a letter and the other has a dash standing for an inserted or deleted residue.

KP.2.Concept: Why we bother.
We align to answer a biological question: are these two sequences related? A good alignment lets us measure their similarity and judge whether they share a common ancestor — that is, whether they are homologous. It's the foundation for finding shared domains, for database searches like BLAST, and for comparing whole genomes.

KP.3.Connection: Hypothesis and measurement together.
Here's the key idea: an alignment is both a hypothesis and a ruler. It proposes which positions correspond between the two sequences, and at the same time it gives us a number for how similar they are.

KP.4.CoolFact: Older than computers.
And here's the cool part — the first protein alignments were done entirely by hand back in 1961, comparing sperm-whale myoglobin with human hemoglobin. The famous computer algorithm that automated the job, Needleman–Wunsch, only appeared in 1970.

# Question and Answer
Q. Define pairwise alignment in one sentence.
A. The process of aligning two sequences to maximize identity (and, for proteins, conservation) so as to assess their similarity and possible homology.

Q. What are the three possible outcomes for a column in an alignment?
A. A match (identical residues), a mismatch (a substitution), or a gap (an indel — an inserted or deleted residue). See [[match mismatch gap]].

Q. What does "pairwise" specifically mean, and what does it contrast with?
A. Exactly two sequences are aligned; it contrasts with *multiple* sequence alignment, which aligns three or more at once.

Q. Why is an alignment described as both a hypothesis and a measurement?
A. It hypothesizes that aligned positions are evolutionarily equivalent, and it simultaneously measures how similar the two sequences are.

Q. Name three things pairwise alignment is used for.
A. Deciding if two proteins/genes are related, identifying shared domains/motifs, and database search (BLAST) — also genome/transcriptome analysis. See [[applications of pairwise alignment]].

Q. What evolutionary principle motivates choosing the alignment with fewest operations?
A. Maximum parsimony — evolution tends to follow the shortest path between two sequences. See [[edit distance and parsimony]].
