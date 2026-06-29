---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/MolecularEvolution
  - MODULE__/SubstitutionMatrices
  - EXAM_PREP
foundational: 5
prereqs: 2
density: 3
value: 5
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# PAM (Point Accepted Mutation)

A **PAM — Point Accepted Mutation** (*mutazione puntuale accettata*) is the event in which DNA undergoes a mutation that **changes one amino acid** **and** that change becomes **prevalent (accepted/fixed) in a species**. "Accepted" = survived natural selection and spread through the population. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=6|L4 p.6]]

**Dayhoff's method (1978).** Margaret Dayhoff built the first [[substitution matrix|substitution matrices]] from PAMs by:
1. collecting **families of proteins ≥85% identical** (homologous, very similar);
2. **[[pairwise alignment|aligning]]** them and building **evolutionary trees**;
3. **inferring the ancestral sequences** at internal nodes → so she could see **which substitutions actually occurred**, in small, observable evolutionary steps.

**PAM as a unit of evolutionary distance.** "1 PAM" = **1 accepted point mutation per 100 residues**.
- **PAM1** = the matrix for proteins with **≤1% divergence** (1 change per 100 aa). All PAM data come from **closely related proteins (>85% identity)**, via **global** alignment.
- Higher PAM = more divergence. Other PAMs are **extrapolated** from PAM1 ([[PAM matrix extrapolation]]); PAM1 itself has little practical use. (PAM250 ≈ 250 changes per 100 residues of evolutionary distance.)

> [!Caution] PAM is *distance*, not *time*
> A PAM number counts **accepted mutations**, not years. Different proteins accumulate PAMs at very different **rates** (see the Stats below), so the same PAM distance corresponds to different amounts of elapsed time depending on the protein.

# Stats and Numbers
Dayhoff's **34 superfamilies**, in **PAMs per 100 million years** (evolutionary *rate*): fast-changing **Ig kappa chain 37**, kappa casein 33 … down to **hemoglobin 12**, myoglobin 8.9, histone H2B 0.9, and **ubiquitin ≈ 0** — essentially frozen. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=7|L4 p.7]]

# TLDR
A **Point Accepted Mutation** is an amino-acid-changing DNA mutation that becomes **fixed in a species** ("accepted" by selection). Dayhoff built substitution matrices by aligning **>85%-identical** protein families, inferring ancestors, and counting real substitutions. **1 PAM = 1 accepted change per 100 residues** — a unit of evolutionary **distance** (not time); PAM1 = 1% divergence.

# Recitation Anchors
- PAM = **point accepted mutation** = aa-changing mutation **fixed** in a species ("accepted" by selection)
- Dayhoff: **≥85%-identical** families → align → trees → infer ancestors → count substitutions
- **1 PAM = 1 accepted change / 100 residues** (a **distance** unit, not time)
- PAM1 = ≤1% divergence; built from **global** alignments of close proteins
- Higher PAM = more divergent; PAMn extrapolated from PAM1
- Rates vary by protein: Ig kappa fast (37), **ubiquitin ≈ 0** (per 100 My)

> [!Cool] Cool fact
> The slowest protein on Dayhoff's list, **ubiquitin**, is so essential that it's almost frozen in evolution: **yeast and human ubiquitin differ by only 3 of 76 amino acids** (~96% identical) despite ~1.5 billion years of separation — among the most conserved proteins known, and exactly why its rate sits at **0** PAMs per 100 My. [source](https://www.nature.com/articles/312663a0)

# Read aloud
KP.0.Definition: What a PAM is.
A PAM, a point accepted mutation, is the event where DNA mutates in a way that changes one amino acid, and that change then becomes prevalent in a species. The word accepted is key: it means the mutation survived natural selection and spread through the population.

KP.1.Procedure: Dayhoff's method.
Margaret Dayhoff built the first substitution matrices from these events. She collected families of proteins that were at least eighty-five percent identical — so, closely related and homologous. She aligned them, built evolutionary trees, and inferred the ancestral sequences at the branch points. That let her see which substitutions had actually occurred, in small, observable evolutionary steps.

KP.2.Concept: PAM as a distance unit.
PAM is also a unit of evolutionary distance. One PAM means one accepted point mutation per hundred residues. So PAM-one is the matrix for proteins that differ by about one percent, and all the PAM data come from closely related proteins, more than eighty-five percent identical, using global alignment. Bigger PAM numbers mean more divergence, and the higher matrices are extrapolated from PAM-one.

KP.3.Connection: Distance, not time.
Be careful: a PAM number counts accepted mutations, not years. Different proteins accumulate mutations at very different rates, so the same PAM distance can mean very different amounts of elapsed time depending on the protein. Dayhoff's table of thirty-four superfamilies shows this — immunoglobulin chains change fast, while histones and ubiquitin barely change at all.

KP.4.CoolFact: Ubiquitin, frozen in time.
And here's the cool part — the slowest protein on her list, ubiquitin, is so essential it's almost frozen in evolution. Yeast and human ubiquitin differ by only three of seventy-six amino acids, about ninety-six percent identical, even though their lineages split well over a billion years ago. It's one of the most conserved proteins known, which is exactly why its rate sits right at zero.

# Question and Answer
Q. What is a Point Accepted Mutation?
A. A DNA mutation that changes an amino acid and becomes prevalent (accepted/fixed by selection) in a species.

Q. What does "accepted" mean in PAM?
A. The mutation passed natural selection and spread through the population — not every mutation is accepted.

Q. Outline Dayhoff's method for building PAM matrices.
A. Collect ≥85%-identical protein families, align them, build trees, infer ancestral sequences, and count the substitutions that actually occurred.

Q. What does "1 PAM" mean as a unit?
A. One accepted point mutation per 100 residues — a unit of evolutionary distance.

Q. Why is PAM a measure of distance, not time?
A. Proteins accumulate accepted mutations at different rates, so equal PAM distance ≠ equal elapsed time.

Q. From what kind of proteins/alignments is PAM1 built?
A. Closely related proteins (>85% identity), via global alignment (≤1% divergence).

Q. Which protein sits at the bottom of Dayhoff's rate table, and why?
A. Ubiquitin (~0 PAMs/100 My) — it is functionally critical and extremely conserved.
