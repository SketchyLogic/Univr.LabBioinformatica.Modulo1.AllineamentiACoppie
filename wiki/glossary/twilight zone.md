---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/MolecularEvolution
  - MODULE__/SubstitutionMatrices
  - EXAM_PREP
foundational: 4
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

# twilight zone

The **twilight zone** is the range of low sequence identity (**~20–25%**) below which two proteins can no longer be reliably told apart from **unrelated** sequences — even if they *are* [[homology|homologous]]. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=12|L4 p.12]]

**Why it exists — exponential decay of identity.** As mutations accumulate, the percentage identity between two 100-residue sequences **falls as a negative exponential** with evolutionary ([[PAM (Point Accepted Mutation)|PAM]]) distance:

![[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=12|Percent identity decays exponentially with PAM distance; the twilight zone is where the curve flattens near 20%]]

**The milestones** (differences per 100 residues):

| Distance | Identity / differences |
|---|---|
| **PAM1** | **99%** identical |
| **PAM10.7** | 10 differences / 100 |
| **PAM80** | 50 differences / 100 |
| **PAM250** | 80 differences / 100 (≈20% identity) |

Below ~20–25% identity, **[[statistical significance of an alignment|chance and homology look the same]]** — so **PAM250 defines the twilight zone**. To detect relationships there you must go **beyond pairwise sequence**: multiple-sequence alignments, profiles/HMMs, or **3-D structure** comparison and modeling.

# TLDR
The **twilight zone** is the ~**20–25% identity** range below which homology can no longer be reliably detected from sequence alone, because % identity **decays exponentially** with [[PAM (Point Accepted Mutation)|PAM]] distance (PAM1 = 99%, PAM250 ≈ 20%). **PAM250 defines it**; below it you need multiple alignments, profiles, or **structure**.

# Recitation Anchors
- **Twilight zone ≈ 20–25% identity** — homology no longer reliably detectable from sequence
- % identity **decays as a negative exponential** with PAM distance
- Milestones: PAM1 99% · PAM10.7 = 10/100 · PAM80 = 50/100 · PAM250 = 80/100 (~20%)
- **PAM250 defines** the twilight zone
- Below it: use MSAs, profiles/HMMs, **3-D structure**/modeling

> [!Cool] Cool fact
> **Structure outlasts sequence.** Two proteins can fall deep in the twilight zone — sometimes **below 15% identity** — yet still share the *same 3-D fold*, because structure is far more evolutionarily conserved than sequence. Burkhard **Rost (1999)** mapped the zone precisely, showing that below ~25% identity sequence similarity stops being a trustworthy signal of homology. [source](https://doi.org/10.1093/protein/12.2.85)

# Read aloud
KP.0.Definition: What the twilight zone is.
The twilight zone is the range of low sequence identity, roughly twenty to twenty-five percent, below which two proteins can no longer be reliably distinguished from completely unrelated sequences — even when they genuinely are homologous.

KP.1.Concept: Why it exists.
It exists because of exponential decay. As mutations pile up, the percentage identity between two hundred-residue sequences falls off as a negative exponential with evolutionary distance, measured in PAMs. Early on, identity drops fast; later the curve flattens out near twenty percent.

KP.2.Numbers: The milestones.
Some landmarks, in differences per hundred residues. At PAM-one, the sequences are ninety-nine percent identical. At PAM-ten-point-seven, there are ten differences per hundred. At PAM-eighty, fifty differences per hundred. And at PAM-two-fifty, eighty differences per hundred — only about twenty percent identity. Below twenty to twenty-five percent, chance and homology start to look the same, so PAM-two-fifty is taken to define the twilight zone.

KP.3.Connection: What to do below it.
Once you're in the twilight zone, pairwise sequence comparison isn't enough. To detect relationships you have to go further — multiple-sequence alignments, profiles and hidden Markov models, or comparing three-dimensional structures and building models.

KP.4.CoolFact: Structure outlasts sequence.
And here's the cool part — structure outlasts sequence. Two proteins can sit deep in the twilight zone, sometimes below fifteen percent identity, and still share the very same three-dimensional fold, because structure is far more conserved over evolution than sequence is. Burkhard Rost mapped this zone precisely in 1999, showing that below about twenty-five percent identity, sequence similarity simply stops being a trustworthy sign of homology.

# Question and Answer
Q. What is the twilight zone?
A. The ~20–25% identity range below which homology can't be reliably detected from sequence alone.

Q. Why does identity enter a twilight zone as proteins diverge?
A. Percent identity decays as a negative exponential with PAM distance, flattening toward ~20%.

Q. What identity does PAM250 correspond to, and what does it define?
A. ~20% identity (80 differences/100 residues); it defines the twilight zone.

Q. List the lecture's PAM/identity milestones.
A. PAM1 = 99%; PAM10.7 = 10 diff/100; PAM80 = 50 diff/100; PAM250 = 80 diff/100.

Q. How can you detect homology for sequences in the twilight zone?
A. Use multiple-sequence alignments, profiles/HMMs, or 3-D structure comparison and modeling.

Q. Why can structure reveal homology that sequence cannot?
A. Structure (3-D fold) is far more conserved than sequence, so it persists even below ~15% identity.
