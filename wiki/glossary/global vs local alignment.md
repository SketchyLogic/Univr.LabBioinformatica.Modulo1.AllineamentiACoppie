---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/LocalAlignment
  - EXAM_PREP
foundational: 5
prereqs: 2
density: 2
value: 5
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# global vs local alignment

A [[pairwise alignment]] can be computed in **two modes**, differing in *how much* of each sequence must be aligned. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=2|L4 p.2]]

- **Global** — the alignment runs **end to end**, from the first residue to the last of **both** sequences. This is what [[Needleman-Wunsch algorithm|Needleman–Wunsch]] (and global Smith–Waterman) produce. Best when the two sequences are **of similar length and similar throughout**.
- **Local** — the alignment finds only the **region(s) (subsequences)** of the two sequences that align **optimally**, ignoring the poorly-matching flanks. This is what [[Smith-Waterman algorithm|Smith–Waterman]] produces. Best when similarity is **confined to a domain or motif** inside otherwise-different sequences.

[[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=2|Global vs local alignment — global drags the whole length, local isolates the matching block]]

> [!Caution] Global alignment can **hide** real similarity
> When two sequences share only a short conserved block, forcing an end-to-end (global) alignment dilutes that block with forced matches/gaps in the non-homologous regions — the similarity gets *masked*. Local alignment isolates the block and makes it **apparent**. (Lecture ESEMPIO 1: a flavohemoprotein vs a human hemoglobin chain — the shared globin domain is obvious locally, hard to see globally.)

**Local is not a sub-piece of global.** The optimal local alignment is computed by a *different* path through the matrix (start at the maximum-scoring cell), so it can pair residues the global alignment never would — *AL ⊄ AG* in the lecture's notation. (ESEMPIO 2: `ADCNYRQCLCRPM` / `AYCYNRCKCRDP` give different global vs local results — see [[exercise-smith-waterman-local]].)

**Why local dominates in practice.** Local alignment is **almost always** used for **database search** (via **BLAST**): it finds **domains** and **limited regions of homology** buried inside larger sequences. Whatever method you pick, it returns a **score *S* that is not absolute** — *S* depends on the [[scoring matrix]] and gap model, so it only has meaning relative to a [[statistical significance of an alignment|null model]].

# TLDR
**Global** alignment runs end-to-end across both sequences (Needleman–Wunsch); **local** alignment finds only the best-matching subsequence regions (Smith–Waterman). Global can mask similarity that is confined to a small block; local isolates it, which is why local alignment is the workhorse of database search (BLAST).

# Recitation Anchors
- **Global** = end-to-end (NW); **local** = best subsequence(s) (SW)
- Global best for *similar-length, similar-throughout*; local best for *shared domain/motif*
- Global can **mask** a short conserved block; local makes it **apparent**
- Local ⊄ global (different path; start at the max cell)
- **Local → BLAST → database search** (find domains / homology regions)
- Score *S* is **not absolute** (depends on matrix + gaps)

> [!Cool] Cool fact
> Local alignment is so central that **BLAST** — the heuristic that finds local alignments against a database — is one of the **most-cited scientific papers of all time**: both the 1990 BLAST paper and the 1997 Gapped/PSI-BLAST paper sit in Nature's list of the *top 100 most-cited papers ever*, alongside landmarks of physics and chemistry. [source](https://www.nature.com/news/the-top-100-papers-1.16224)

# Read aloud
KP.0.Definition: Two modes of alignment.
Any pairwise alignment can be done in one of two modes, and they differ in how much of each sequence has to line up. The first is global, the second is local.

KP.1.Concept: Global alignment.
A global alignment runs from end to end — the very first residue to the very last, in both sequences. That's what Needleman–Wunsch gives you. It's the right choice when the two sequences are roughly the same length and similar all the way along.

KP.2.Concept: Local alignment.
A local alignment instead hunts for just the region, or regions, where the two sequences match best, and it simply ignores the poorly-matching ends. That's what Smith–Waterman gives you. It's the right choice when the similarity is confined to one domain or motif sitting inside otherwise-different sequences.

KP.3.Connection: Global can hide similarity.
Here's the subtle part. If two proteins share only a short conserved block, forcing a full end-to-end alignment buries that block among forced matches and gaps in the unrelated regions, and the real similarity gets masked. A local alignment isolates the block and makes it jump out. In the lecture's example, a flavohemoprotein and a human hemoglobin chain share a globin domain that's obvious locally but hard to see globally.

KP.4.Concept: Local is not a slice of global.
And a local alignment is not just a piece cut out of the global one. It's computed by a different path through the matrix, starting from the highest-scoring cell, so it can pair up residues the global alignment never would.

KP.5.Connection: Why local wins in practice.
This is why local alignment is almost always the one used for searching databases, through BLAST — it finds domains and limited regions of homology hidden inside bigger sequences. And remember: whatever method you choose, the score it returns is not absolute. It depends on your scoring matrix and gap penalties, so a score only means something compared against a null model of chance.

KP.6.CoolFact: BLAST among the all-time greats.
And here's the cool part — local alignment is so central to biology that BLAST, the tool that finds local alignments against a database, is one of the most-cited scientific papers ever written. Both the original 1990 paper and the 1997 gapped version appear in Nature's list of the hundred most-cited papers of all time, right beside the great results of physics and chemistry.

# Question and Answer
Q. What is the difference between a global and a local alignment?
A. Global aligns both sequences end-to-end; local finds only the best-matching subsequence region(s), ignoring poorly-matching flanks.

Q. Which algorithm produces each, and when is each appropriate?
A. Needleman–Wunsch → global (similar-length, similar-throughout sequences); Smith–Waterman → local (similarity confined to a domain/motif).

Q. How can a global alignment "mask" similarity?
A. A short shared block gets diluted by forced matches/gaps in the non-homologous regions, so the real similarity is hard to see; local alignment isolates the block.

Q. Is the optimal local alignment always a sub-region of the optimal global alignment?
A. No — it is computed by a different path (starting at the max-scoring cell), so it can differ entirely (AL ⊄ AG).

Q. Why is local alignment the standard for database searches?
A. It locates domains and limited homology regions buried inside larger sequences — exactly what BLAST does when scanning a database.

Q. What does it mean that the alignment score S is "not absolute"?
A. S depends on the chosen scoring matrix and gap penalties, so it is only meaningful relative to a statistical null model (significance), not as a standalone number.
