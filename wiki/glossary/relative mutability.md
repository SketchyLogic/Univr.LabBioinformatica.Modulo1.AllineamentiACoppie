---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/MolecularEvolution
  - MODULE__/SubstitutionMatrices
foundational: 2
prereqs: 2
density: 2
value: 3
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# relative mutability

**Relative mutability** answers: *how often does each amino acid mutate* (change to something else) in proteins? Dayhoff measured it and set **alanine = 100** arbitrarily as the reference. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=8|L4 p.8]]

- **Most mutable** (change readily): **Asn 134**, Ser 120, Asp 106, Glu 102, Ala 100, Thr 97, Ile 96…
- **Least mutable** (resist change): **Trp 18**, **Cys 20**, Leu 40, Phe 41, Tyr 41, Gly 49…

The least-mutable residues are the **functionally/structurally constrained** ones: **Cys** forms **disulfide bridges**, **Trp** is bulky, rare and structurally special — changing either tends to break the protein, so selection rejects the change.

> [!Caution] Mutability ≠ frequency
> Relative mutability is *how readily a residue changes when it appears* — **not** how often it appears. That second quantity is the [[amino acid frequencies|background frequency]]. (Trp is both rarely-occurring *and* rarely-mutated.) Mutability feeds the construction of the [[PAM1 mutation probability matrix]].

# TLDR
**Relative mutability** ranks how readily each amino acid changes in proteins, with **Ala ≡ 100**. **Asn (134)** is the most mutable; **Trp (18)** and **Cys (20)** the least — because Trp and Cys are structurally/functionally critical (disulfide bonds, bulky aromatic). It is distinct from background **frequency**, and it feeds PAM1's construction.

# Recitation Anchors
- "How often does each aa **change**?" — reference **Ala = 100**
- Most mutable: **Asn 134**, Ser 120, Asp 106
- Least mutable: **Trp 18**, **Cys 20** (then Leu 40)
- Low mutability ⇐ structural/functional constraint (Cys disulfides; Trp bulky/special)
- **Mutability ≠ [[amino acid frequencies|frequency]]** (change-rate vs occurrence-rate)
- Feeds [[PAM1 mutation probability matrix|PAM1]]

> [!Cool] Cool fact
> The two least-mutable amino acids double as two of the **rarest**: **tryptophan** is encoded by a **single codon (UGG)** and is the least common amino acid in proteins (~1%). Being rare, large, and hard to replace, a conserved Trp is such strong evidence of homology that [[BLOSUM matrix|BLOSUM62]] gives **W↔W its highest score (+11)**. [source](https://en.wikipedia.org/wiki/Tryptophan)

# Read aloud
KP.0.Definition: What relative mutability is.
Relative mutability answers a simple question: how often does each amino acid actually mutate — change into something else — in proteins? Dayhoff measured this and set alanine equal to one hundred as an arbitrary reference point.

KP.1.Numbers: The rankings.
At the top, the most mutable residues, are asparagine at one hundred thirty-four, then serine, aspartate, glutamate, and alanine itself at one hundred. At the bottom, the least mutable, are tryptophan at eighteen and cysteine at twenty, followed by leucine and phenylalanine.

KP.2.Concept: Why some resist change.
The least mutable residues are the ones under the tightest structural or functional constraints. Cysteine forms disulfide bridges that hold a protein together; tryptophan is bulky, rare, and structurally special. Changing either tends to break the protein, so natural selection rejects the change.

KP.3.Connection: Mutability is not frequency.
One important distinction: relative mutability is how readily a residue changes when it's present — not how often it appears in the first place. How often it appears is the background frequency, a separate idea. Tryptophan happens to be both rarely present and rarely mutated. Mutability is one of the ingredients used to build the PAM-one matrix.

KP.4.CoolFact: Tryptophan, rare and irreplaceable.
And here's the cool part — the two least-mutable amino acids are also among the rarest. Tryptophan is encoded by just a single codon and is the least common amino acid in proteins, around one percent. Because it's rare, large, and hard to replace, a conserved tryptophan is such strong evidence of homology that the BLOSUM62 matrix gives a tryptophan-to-tryptophan match its highest score of all, plus eleven.

# Question and Answer
Q. What does relative mutability measure, and what is the reference value?
A. How readily each amino acid changes in proteins; alanine is set to 100.

Q. Which amino acid is most mutable, and which are least?
A. Most mutable: asparagine (134). Least mutable: tryptophan (18) and cysteine (20).

Q. Why are Cys and Trp so resistant to mutation?
A. They are structurally/functionally critical — Cys forms disulfide bonds, Trp is bulky/aromatic/rare — so changes are selected against.

Q. How does relative mutability differ from amino-acid frequency?
A. Mutability = how often a residue changes when present; frequency = how often it occurs at all.

Q. What is relative mutability used for?
A. It feeds the construction of the PAM1 mutation probability matrix.

Q. Why does a conserved tryptophan strongly suggest homology?
A. Trp is rare and rarely mutated, so its conservation is unlikely by chance — BLOSUM62 scores W↔W highest (+11).
