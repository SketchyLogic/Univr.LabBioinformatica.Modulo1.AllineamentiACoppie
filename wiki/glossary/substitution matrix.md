---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/SubstitutionMatrices
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

# substitution matrix

A **substitution matrix** (*matrice di sostituzione*) is the protein-world realization of a [[scoring matrix]]: a **20×20** table whose entries are **proportional to the probability that amino acid *i* mutates into amino acid *j***, for every pair. It is what lets an alignment score [[identity conservation similarity|similarity]], not just identity. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=4|L4 p.4]]

**Key properties:**
- **20×20** — one row/column per amino acid.
- **Symmetric** — $s(A,B) = s(B,A)$. Evolutionarily we **cannot tell which residue mutated into which**, so the score is direction-agnostic.
- Built by **assembling a large, diversified sample** of [[pairwise alignment|pairwise]] (or multiple) alignments and counting **real** substitutions — so the matrix should **reflect the true probability of mutation over a period of evolution**, not a chemist's guess (see [[amino acid similarity]]).
- The actual scores are **[[log-odds score|log-odds]]** values (observed vs chance).

**Two families** dominate, differing in *how* they're built:

| Family | Built from | Idea |
|---|---|---|
| **[[PAM (Point Accepted Mutation)\|PAM]]** | global alignments of **closely related** proteins, extrapolated | an **evolutionary model** |
| **[[BLOSUM matrix\|BLOSUM]]** | local blocks of **distantly related** proteins | **empirical** observation |

Their trade-offs are compared in [[PAM vs BLOSUM]].

# TLDR
A **substitution matrix** is a 20×20, **symmetric** table of [[log-odds score|log-odds]] scores proportional to the probability each amino acid mutates into another, built by counting **real** substitutions in large alignment samples. It's the protein form of a [[scoring matrix]]. The two families are **PAM** (evolutionary model) and **BLOSUM** (empirical).

# Recitation Anchors
- **20×20**, one entry per amino-acid pair
- **Symmetric**: $s(A,B)=s(B,A)$ (can't tell who mutated into whom)
- Entries ∝ probability *i* → *j*; actually [[log-odds score|log-odds]] values
- Built by counting **real** substitutions in big alignment samples
- Two families: **PAM** (evolutionary) and **BLOSUM** (empirical)
- The protein realization of a generic [[scoring matrix]]

> [!Cool] Cool fact
> The whole field runs on a notation invented by **Margaret Dayhoff**, who built the first substitution matrices: she compressed the clumsy three-letter amino-acid abbreviations into today's **single-letter code** (A, G, L, P, T…) to **save scarce computer memory** in the 1960s. She is now regarded as a **founder of bioinformatics**. [source](https://www.nature.com/articles/s43588-025-00784-y)

# Read aloud
KP.0.Definition: What a substitution matrix is.
A substitution matrix is the protein version of a scoring matrix: a twenty-by-twenty table whose entries are proportional to the probability that one amino acid mutates into another, for every possible pair. It's what lets an alignment measure similarity rather than just counting identical residues.

KP.1.Concept: Its key properties.
A few properties define it. It's twenty by twenty, one row and column per amino acid. It's symmetric: the score for A-into-B equals the score for B-into-A, because evolutionarily we can't tell which residue changed into which. And it's built empirically, by assembling a large, varied collection of real alignments and counting the substitutions that actually happen, so the numbers reflect true evolutionary probabilities rather than a chemist's guess. The actual values stored are log-odds scores — observed versus chance.

KP.2.Concept: Two families.
Two families dominate, and they differ in how they're built. PAM matrices come from global alignments of closely related proteins, extrapolated forward — an evolutionary model. BLOSUM matrices come from local blocks of distantly related proteins — pure empirical observation. We compare their trade-offs separately.

KP.3.CoolFact: Dayhoff's single-letter code.
And here's the cool part — the entire field runs on a notation invented by Margaret Dayhoff, who built the very first substitution matrices. To save scarce computer memory back in the 1960s, she compressed the clumsy three-letter amino-acid abbreviations into the single-letter code we still use today, with letters like A, G, L, P, and T. She's now considered one of the founders of bioinformatics.

# Question and Answer
Q. What is a substitution matrix, and what size is it for proteins?
A. A table of scores proportional to the probability each amino acid mutates into another; 20×20 for proteins.

Q. Why is a substitution matrix symmetric?
A. Because we cannot tell evolutionarily which residue mutated into which, so $s(A,B)=s(B,A)$.

Q. How are substitution matrices built?
A. By assembling a large, diversified sample of alignments and counting real substitutions, so the matrix reflects true mutation probabilities.

Q. What are the two main families and how do they differ?
A. PAM (evolutionary model from closely-related global alignments) and BLOSUM (empirical, from distantly-related local blocks).

Q. How does a substitution matrix relate to a scoring matrix?
A. It is the protein-specific realisation of a scoring matrix; its entries are log-odds scores.

Q. What stored value type are the entries (not raw probabilities)?
A. Log-odds scores — the log of observed-over-chance probability.
