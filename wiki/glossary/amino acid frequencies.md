---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/SubstitutionMatrices
foundational: 3
prereqs: 1
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

# amino acid frequencies

The **(normalised) amino-acid frequencies** $f_i$ say *how often each amino acid occurs* in proteins. They sum to 100%. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=8|L4 p.8]]

- **Most common**: **Gly 8.9%**, Ala 8.7%, Leu 8.5%, Lys 8.1%, Ser 7.0%…
- **Rarest**: **Trp 1.0%**, Met 1.5%, Tyr 3.0%, Cys 3.3%…

**Why these values — codon degeneracy.** Amino acids with **more codons** tend to be **more common**; those with **one codon** are rare. In the lecture: residues marked **blue have 6 codons** (Leu, Ser, Arg), **red have 1 codon** (Met, Trp) — and indeed **Met and Trp are the two rarest**.

**Where they're used — the "chance" baseline.** The $f_i$ are the background against which substitutions are judged: the probability of pairing residues *i* and *j* **by chance** is $p_{ij} = f_i f_j$, the **denominator** of the [[log-odds score]]. Without this baseline you couldn't tell a *meaningful* match from a *common-by-accident* one.

> [!Caution] Frequency ≠ mutability
> How often a residue **appears** ([[amino acid frequencies|frequency]], here) is different from how often it **changes** ([[relative mutability]]). Trp is rare on **both** counts; Ala is common but middling in mutability.

# TLDR
Amino-acid frequencies $f_i$ give how often each residue **occurs** (Gly 8.9% … Trp 1.0%), summing to 100%. They track **codon degeneracy** (6-codon residues common, 1-codon residues rare). They are the **chance baseline** $p_{ij}=f_i f_j$ in the [[log-odds score]] denominator — distinct from [[relative mutability]].

# Recitation Anchors
- $f_i$ = how often each aa **occurs**; $\sum f_i = 100\%$
- Most common: **Gly 8.9%**, Ala 8.7%, Leu 8.5%
- Rarest: **Trp 1.0%**, Met 1.5%
- More codons ⇒ more common (blue = 6 codons; red = 1 codon)
- Used as chance baseline: $p_{ij}=f_i f_j$ → [[log-odds score]] denominator
- **Frequency ≠ [[relative mutability|mutability]]**

> [!Cool] Cool fact
> The ranking mirrors the **genetic code's redundancy**: leucine, serine and arginine each have **six** codons and are among the commonest residues, while methionine and tryptophan have just **one** codon each and are the **two rarest** — biology's amino-acid budget partly set by the structure of the codon table. [source](https://en.wikipedia.org/wiki/Genetic_code)

# Read aloud
KP.0.Definition: What the frequencies are.
The normalised amino-acid frequencies tell you how often each amino acid occurs in proteins, and they add up to one hundred percent.

KP.1.Numbers: Common and rare.
The most common are glycine at nearly nine percent, then alanine, leucine, lysine, and serine. The rarest is tryptophan at just one percent, followed by methionine at one and a half percent.

KP.2.Concept: Why — codon degeneracy.
There's a reason for the ranking: codon degeneracy. Amino acids with more codons tend to be more common, and those with a single codon are rare. In the lecture, the residues marked blue have six codons each — leucine, serine, arginine — while the ones marked red have only one, methionine and tryptophan, and those two are indeed the rarest.

KP.3.Connection: The chance baseline.
These frequencies matter because they set the baseline of chance. The probability of pairing two residues purely by accident is the product of their individual frequencies, and that product is the denominator of the log-odds score. Without it, you couldn't tell a meaningful match from one that's just common by accident. And don't confuse this with mutability: frequency is how often a residue appears, mutability is how often it changes.

KP.4.CoolFact: The code sets the budget.
And here's the cool part — the ranking mirrors the redundancy built into the genetic code. Leucine, serine, and arginine each have six codons and are among the most common residues, while methionine and tryptophan have just one codon each and are the two rarest. Biology's amino-acid budget is partly dictated by the shape of the codon table itself.

# Question and Answer
Q. What do amino-acid frequencies measure, and what do they sum to?
A. How often each amino acid occurs in proteins; they sum to 100%.

Q. Which amino acid is most common and which is rarest?
A. Most common: glycine (~8.9%); rarest: tryptophan (~1.0%).

Q. Why do some amino acids occur more than others?
A. Codon degeneracy — residues with more codons (6) tend to be common; single-codon residues (Met, Trp) are rare.

Q. How are the frequencies used in scoring?
A. As the chance baseline $p_{ij}=f_i f_j$, the denominator of the log-odds score.

Q. How does amino-acid frequency differ from relative mutability?
A. Frequency = how often a residue appears; mutability = how often it changes when present.

Q. Which residues have 6 codons vs 1 codon (per the lecture's colour code)?
A. 6 codons (blue): Leu, Ser, Arg; 1 codon (red): Met, Trp.
